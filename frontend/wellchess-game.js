// ==================== 水井棋游戏逻辑 - 完全按照鸿蒙代码实现 ====================
const COLS = 3, ROWS = 5;
const AI_EASY = 0, AI_MEDIUM = 1, AI_HARD = 2;
const LEVELS = [
    [1, 1, '第1关 - 热身', true], [1, 2, '第2关 - 起步', true],
    [2, 2, '第3关 - 入门', false], [2, 3, '第4关 - 初级', false],
    [2, 4, '第5关 - 初级+', false], [3, 3, '第6关 - 中级', false],
    [3, 4, '第7关 - 进阶', false], [3, 5, '第8关 - 挑战', false],
    [4, 4, '第9关 - 困难', false], [4, 5, '第10关 - 大师', false]
];
const ACHIEVEMENTS = [
    { id: 'firstWin', name: '初出茅庐', desc: '获得第一场胜利', icon: '🏆' },
    { id: 'streak3', name: '小试牛刀', desc: '达成3连胜', icon: '🔥' },
    { id: 'streak5', name: '势如破竹', desc: '达成5连胜', icon: '⚡' },
    { id: 'streak10', name: '战神降临', desc: '达成10连胜', icon: '👑' },
    { id: 'aiSlayer', name: 'AI杀手', desc: '击败AI 10次', icon: '🤖' },
    { id: 'speedster', name: '神速', desc: '30秒内获胜', icon: '💨' },
    { id: 'challenger', name: '挑战者', desc: '闯关模式通过第5关', icon: '🎯' },
    { id: 'master', name: '水井棋大师', desc: '通关全部关卡', icon: '🎓' },
    { id: 'veteran', name: '沙场老兵', desc: '累计进行50场对局', icon: '🎖️' },
    { id: 'dedicated', name: '专注玩家', desc: '累计游戏时长1小时', icon: '⏰' },
    { id: 'socialite', name: '社交达人', desc: '本地双人对战10局', icon: '🤝' }
];

let gameState = { mode: 'local', cols: COLS, rows: ROWS, horizontalLines: [], verticalLines: [], squares: [], selectedDot: null, currentPlayer: 1, scores: [0, 0], gameOver: false, history: [], aiThinking: false, aiDifficulty: AI_MEDIUM, hintMove: null, showingHint: false, timerInterval: null, startTime: 0, gameTime: 0, currentLevel: 0 };
let isDarkMode = false;
let stats = { totalGames: 0, totalWins: 0, totalLosses: 0, totalDraws: 0, aiGames: 0, aiWins: 0, localGames: 0, challengeGames: 0, challengeWins: 0, maxLevel: 0, totalPlayTime: 0, fastestWin: 0, fastestChallenge: 0, currentWinStreak: 0, maxWinStreak: 0, unlockedLevel: 1, achievements: {} };

function init() { loadStats(); loadTheme(); }
function loadStats() { try { const s = localStorage.getItem('wellchess_stats'); if (s) stats = { ...stats, ...JSON.parse(s) }; } catch (e) {} }
function saveStats() { try { localStorage.setItem('wellchess_stats', JSON.stringify(stats)); } catch (e) {} }
function loadTheme() { try { isDarkMode = localStorage.getItem('wellchess_dark') === 'true'; applyTheme(); } catch (e) {} }
function toggleTheme() { isDarkMode = !isDarkMode; applyTheme(); try { localStorage.setItem('wellchess_dark', isDarkMode); } catch (e) {} }
function applyTheme() { document.body.classList.toggle('dark-mode', isDarkMode); const btn = document.getElementById('themeBtn'); btn.textContent = isDarkMode ? '☀️ 浅色模式' : '🌙 深色模式'; btn.classList.toggle('light', isDarkMode); }

function showPage(id) { document.querySelectorAll('.page').forEach(p => p.classList.remove('active')); document.getElementById(id).classList.add('active'); }
function backToMenu() { if (gameState.timerInterval) clearInterval(gameState.timerInterval); showPage('menuPage'); }
function showStats() { renderStats(); switchTab(0); showPage('statsPage'); }
function switchTab(tab) { document.getElementById('tabStats').className = 'tab-btn' + (tab === 0 ? ' active-stats' : ''); document.getElementById('tabAchieve').className = 'tab-btn' + (tab === 1 ? ' active-achieve' : ''); document.getElementById('statsContent').style.display = tab === 0 ? 'block' : 'none'; document.getElementById('achieveContent').style.display = tab === 1 ? 'block' : 'none'; }

function showChallenge() { renderLevelGrid(); document.getElementById('levelSelectView').style.display = 'block'; document.getElementById('challengeGameView').style.display = 'none'; showPage('challengePage'); }
function renderLevelGrid() { const grid = document.getElementById('levelGrid'); grid.innerHTML = ''; for (let i = 0; i < LEVELS.length; i++) { const btn = document.createElement('button'); btn.className = 'level-btn ' + (i < stats.unlockedLevel ? 'unlocked' : 'locked'); btn.textContent = i + 1; if (i < stats.unlockedLevel) btn.onclick = () => selectLevel(i); grid.appendChild(btn); } document.getElementById('levelProgress').textContent = `已解锁: ${stats.unlockedLevel} / ${LEVELS.length} 关`; }
function selectLevel(levelIndex) { gameState.currentLevel = levelIndex; gameState.mode = 'challenge'; const level = LEVELS[levelIndex]; gameState.cols = level[0]; gameState.rows = level[1]; document.getElementById('levelSelectView').style.display = 'none'; document.getElementById('challengeGameView').style.display = 'flex'; document.getElementById('challengeLevelName').textContent = level[2]; document.getElementById('nextLevelBtn').style.display = 'none'; initGameState(); renderBoard(); startTimer(); if (level[3] === true) { gameState.currentPlayer = 2; updateStatus('AI 先手，观察它的策略...'); gameState.aiThinking = true; setTimeout(() => { aiMove(); gameState.aiThinking = false; }, 800); } else { gameState.currentPlayer = 1; updateStatus('击败 AI 进入下一关！'); } }
function showLevelSelect() { if (gameState.timerInterval) clearInterval(gameState.timerInterval); renderLevelGrid(); document.getElementById('levelSelectView').style.display = 'block'; document.getElementById('challengeGameView').style.display = 'none'; }
function nextLevel() { if (gameState.currentLevel < LEVELS.length - 1) selectLevel(gameState.currentLevel + 1); }
function unlockNextLevel() { if (gameState.currentLevel + 1 >= stats.unlockedLevel && gameState.currentLevel + 1 < LEVELS.length) { stats.unlockedLevel = gameState.currentLevel + 2; saveStats(); } }

function startGame(mode) { gameState.mode = mode; gameState.cols = COLS; gameState.rows = ROWS; initGameState(); renderBoard(); showPage(mode === 'local' ? 'localPage' : 'aiPage'); startTimer(); }
function restartGame(mode) { if (mode === 'challenge') selectLevel(gameState.currentLevel); else { initGameState(); renderBoard(); startTimer(); } }
function initGameState() { const rows = gameState.rows, cols = gameState.cols; gameState.horizontalLines = []; for (let r = 0; r <= rows; r++) gameState.horizontalLines.push(new Array(cols).fill(0)); gameState.verticalLines = []; for (let r = 0; r < rows; r++) gameState.verticalLines.push(new Array(cols + 1).fill(0)); gameState.squares = []; for (let r = 0; r < rows; r++) gameState.squares.push(new Array(cols).fill(0)); gameState.currentPlayer = 1; gameState.scores = [0, 0]; gameState.gameOver = false; gameState.selectedDot = null; gameState.history = []; gameState.aiThinking = false; gameState.hintMove = null; gameState.showingHint = false; updateUI(); }

function startTimer() { if (gameState.timerInterval) clearInterval(gameState.timerInterval); gameState.startTime = Date.now(); gameState.gameTime = 0; gameState.timerInterval = setInterval(() => { if (!gameState.gameOver) { gameState.gameTime = Math.floor((Date.now() - gameState.startTime) / 1000); updateTimerDisplay(); } }, 1000); }
function updateTimerDisplay() { const min = Math.floor(gameState.gameTime / 60), sec = gameState.gameTime % 60; const timeStr = `⏱️ ${min.toString().padStart(2, '0')}:${sec.toString().padStart(2, '0')}`; let timerId = gameState.mode === 'local' ? 'localTimer' : gameState.mode === 'ai' ? 'aiTimer' : 'challengeTimer'; document.getElementById(timerId).textContent = timeStr; }

function renderBoard() { let boardId = gameState.mode === 'local' ? 'localBoard' : gameState.mode === 'ai' ? 'aiBoard' : 'challengeBoard'; const board = document.getElementById(boardId); board.innerHTML = ''; const rows = gameState.rows, cols = gameState.cols; const uiRows = 2 * (rows + 1) - 1, uiCols = 2 * (cols + 1) - 1; let colTemplate = ''; for (let i = 0; i < uiCols; i++) colTemplate += (i % 2 === 0 ? 'auto ' : 'auto '); board.style.gridTemplateColumns = colTemplate.trim(); board.style.gridTemplateRows = ''; for (let i = 0; i < uiRows; i++) board.style.gridTemplateRows += (i % 2 === 0 ? 'auto ' : 'auto '); for (let uiRow = 0; uiRow < uiRows; uiRow++) { for (let uiCol = 0; uiCol < uiCols; uiCol++) { const cell = document.createElement('div'); if (uiRow % 2 === 0 && uiCol % 2 === 0) { cell.className = 'dot'; cell.id = `dot-${uiRow / 2}-${uiCol / 2}`; cell.onclick = () => onDotClick(uiRow / 2, uiCol / 2); } else if (uiRow % 2 === 0 && uiCol % 2 === 1) { cell.className = 'h-line-cell'; const line = document.createElement('div'); line.className = 'h-line'; line.id = `hline-${uiRow / 2}-${(uiCol - 1) / 2}`; cell.appendChild(line); } else if (uiRow % 2 === 1 && uiCol % 2 === 0) { cell.className = 'v-line-cell'; const line = document.createElement('div'); line.className = 'v-line'; line.id = `vline-${(uiRow - 1) / 2}-${uiCol / 2}`; cell.appendChild(line); } else { cell.className = 'square-cell'; const square = document.createElement('div'); square.className = 'square'; square.id = `square-${(uiRow - 1) / 2}-${(uiCol - 1) / 2}`; cell.appendChild(square); } board.appendChild(cell); } } updateBoardDisplay(); }
function updateBoardDisplay() { const rows = gameState.rows, cols = gameState.cols; for (let r = 0; r <= rows; r++) for (let c = 0; c < cols; c++) { const line = document.getElementById(`hline-${r}-${c}`); if (line) line.className = 'h-line ' + getLineClass('h', r, c); } for (let r = 0; r < rows; r++) for (let c = 0; c <= cols; c++) { const line = document.getElementById(`vline-${r}-${c}`); if (line) line.className = 'v-line ' + getLineClass('v', r, c); } for (let r = 0; r < rows; r++) for (let c = 0; c < cols; c++) { const square = document.getElementById(`square-${r}-${c}`); if (square) square.className = 'square ' + (gameState.squares[r][c] === 1 ? 'square-p1' : gameState.squares[r][c] === 2 ? 'square-p2' : ''); } document.querySelectorAll('.dot').forEach(d => d.classList.remove('selected')); if (gameState.selectedDot) { const dot = document.getElementById(`dot-${gameState.selectedDot[0]}-${gameState.selectedDot[1]}`); if (dot) dot.classList.add('selected'); } }
function getLineClass(type, row, col) { const owner = type === 'h' ? gameState.horizontalLines[row][col] : gameState.verticalLines[row][col]; if (owner === 1) return 'line-p1'; if (owner === 2) return 'line-p2'; if (gameState.showingHint && gameState.hintMove && gameState.hintMove.type === type && gameState.hintMove.row === row && gameState.hintMove.col === col) return 'line-hint'; return ''; }

function onDotClick(row, col) { if (gameState.gameOver || gameState.aiThinking) return; if (gameState.selectedDot === null) { gameState.selectedDot = [row, col]; } else { const [sr, sc] = gameState.selectedDot; const rowDiff = Math.abs(row - sr), colDiff = Math.abs(col - sc); if (rowDiff === 0 && colDiff === 1) { const lineRow = sr, lineCol = Math.min(sc, col); if (gameState.horizontalLines[lineRow][lineCol] === 0) drawHorizontalLine(lineRow, lineCol); gameState.selectedDot = null; } else if (rowDiff === 1 && colDiff === 0) { const lineRow = Math.min(sr, row), lineCol = sc; if (gameState.verticalLines[lineRow][lineCol] === 0) drawVerticalLine(lineRow, lineCol); gameState.selectedDot = null; } else { gameState.selectedDot = [row, col]; } } updateBoardDisplay(); }
function drawHorizontalLine(row, col) { if (gameState.currentPlayer === 1) { saveState(); gameState.showingHint = false; gameState.hintMove = null; } gameState.horizontalLines[row][col] = gameState.currentPlayer; let gained = checkAndFillSquare(row - 1, col) + checkAndFillSquare(row, col); afterMove(gained); }
function drawVerticalLine(row, col) { if (gameState.currentPlayer === 1) { saveState(); gameState.showingHint = false; gameState.hintMove = null; } gameState.verticalLines[row][col] = gameState.currentPlayer; let gained = checkAndFillSquare(row, col - 1) + checkAndFillSquare(row, col); afterMove(gained); }
function checkAndFillSquare(row, col) { const rows = gameState.rows, cols = gameState.cols; if (row < 0 || row >= rows || col < 0 || col >= cols) return 0; if (gameState.squares[row][col] !== 0) return 0; const top = gameState.horizontalLines[row][col], bottom = gameState.horizontalLines[row + 1][col], left = gameState.verticalLines[row][col], right = gameState.verticalLines[row][col + 1]; if (top !== 0 && bottom !== 0 && left !== 0 && right !== 0) { gameState.squares[row][col] = gameState.currentPlayer; return 1; } return 0; }
function afterMove(gained) { const isAI = gameState.mode === 'ai' || gameState.mode === 'challenge'; if (gained > 0) { gameState.scores[gameState.currentPlayer - 1] += gained; if (gameState.currentPlayer === 1) { showScorePopup('+' + gained); vibrate(50); updateStatus(gameState.mode === 'local' ? `玩家1 吃到 ${gained} 个格子，继续！` : `你吃到 ${gained} 个格子，继续！`); } else if (gameState.mode === 'local') { showScorePopup('+' + gained); vibrate(50); updateStatus(`玩家2 吃到 ${gained} 个格子，继续！`); } else { updateStatus(`AI 吃到 ${gained} 个格子，继续思考...`); } } else { gameState.currentPlayer = gameState.currentPlayer === 1 ? 2 : 1; if (isAI) updateStatus(gameState.currentPlayer === 1 ? '轮到你了' : 'AI 思考中...'); else updateStatus(`轮到 玩家${gameState.currentPlayer}`); } const total = gameState.rows * gameState.cols; if (gameState.scores[0] + gameState.scores[1] === total) { endGame(); return; } updateUI(); updateBoardDisplay(); if (isAI && gameState.currentPlayer === 2 && !gameState.gameOver) { gameState.aiThinking = true; setTimeout(() => { aiMove(); gameState.aiThinking = false; }, 500); } }
function endGame() { gameState.gameOver = true; if (gameState.timerInterval) clearInterval(gameState.timerInterval); const [s1, s2] = gameState.scores; let statusMsg = '', playerWon = false, isDraw = false; if (gameState.mode === 'local') { statusMsg = s1 > s2 ? '🎉 游戏结束！玩家1 获胜！' : s2 > s1 ? '🎉 游戏结束！玩家2 获胜！' : '🤝 游戏结束！平局！'; stats.localGames++; } else if (gameState.mode === 'challenge') { stats.challengeGames++; if (s1 > s2) { unlockNextLevel(); playerWon = true; vibrate(200); stats.challengeWins++; if (gameState.currentLevel + 1 > stats.maxLevel) stats.maxLevel = gameState.currentLevel + 1; if (stats.fastestChallenge === 0 || gameState.gameTime < stats.fastestChallenge) stats.fastestChallenge = gameState.gameTime; statusMsg = gameState.currentLevel < LEVELS.length - 1 ? '🎉 恭喜过关！点击下方进入下一关' : '🎉 恭喜通关！你是水井棋大师！'; document.getElementById('nextLevelBtn').style.display = gameState.currentLevel < LEVELS.length - 1 ? 'block' : 'none'; } else { statusMsg = s2 > s1 ? '😢 挑战失败，再试一次！' : '🤝 平局！再接再励！'; isDraw = s1 === s2; } } else { stats.aiGames++; if (s1 > s2) { statusMsg = '🎉 恭喜！你战胜了 AI！'; playerWon = true; vibrate(200); stats.aiWins++; } else { statusMsg = s2 > s1 ? '😢 AI 获胜！再接再厱！' : '🤝 平局！势均力敌！'; isDraw = s1 === s2; } } updateStatus(statusMsg, true); recordGameResult(playerWon, isDraw); updateUI(); }
function recordGameResult(playerWon, isDraw) { stats.totalGames++; stats.totalPlayTime += gameState.gameTime; if (playerWon) { stats.totalWins++; stats.currentWinStreak++; if (stats.currentWinStreak > stats.maxWinStreak) stats.maxWinStreak = stats.currentWinStreak; if (stats.fastestWin === 0 || gameState.gameTime < stats.fastestWin) stats.fastestWin = gameState.gameTime; } else if (!isDraw) { stats.totalLosses++; stats.currentWinStreak = 0; } else { stats.totalDraws++; stats.currentWinStreak = 0; } checkAchievements(playerWon); saveStats(); }
function checkAchievements(playerWon) { const newAch = [], now = Date.now(); if (playerWon && !stats.achievements.firstWin) { stats.achievements.firstWin = now; newAch.push('firstWin'); } if (stats.currentWinStreak >= 3 && !stats.achievements.streak3) { stats.achievements.streak3 = now; newAch.push('streak3'); } if (stats.currentWinStreak >= 5 && !stats.achievements.streak5) { stats.achievements.streak5 = now; newAch.push('streak5'); } if (stats.currentWinStreak >= 10 && !stats.achievements.streak10) { stats.achievements.streak10 = now; newAch.push('streak10'); } if (stats.aiWins >= 10 && !stats.achievements.aiSlayer) { stats.achievements.aiSlayer = now; newAch.push('aiSlayer'); } if (playerWon && gameState.gameTime <= 30 && !stats.achievements.speedster) { stats.achievements.speedster = now; newAch.push('speedster'); } if (stats.maxLevel >= 5 && !stats.achievements.challenger) { stats.achievements.challenger = now; newAch.push('challenger'); } if (stats.maxLevel >= 10 && !stats.achievements.master) { stats.achievements.master = now; newAch.push('master'); } if (stats.totalGames >= 50 && !stats.achievements.veteran) { stats.achievements.veteran = now; newAch.push('veteran'); } if (stats.totalPlayTime >= 3600 && !stats.achievements.dedicated) { stats.achievements.dedicated = now; newAch.push('dedicated'); } if (stats.localGames >= 10 && !stats.achievements.socialite) { stats.achievements.socialite = now; newAch.push('socialite'); } if (newAch.length > 0) showAchievementToast(newAch[0]); }

function aiMove() { if (gameState.gameOver || gameState.currentPlayer !== 2) return; const move = getBestMove(); if (move) { if (move.type === 'h') drawHorizontalLine(move.row, move.col); else drawVerticalLine(move.row, move.col); updateBoardDisplay(); } }
function getBestMove() { const rows = gameState.rows, cols = gameState.cols; const gainMoves = [], normalMoves = [], lostMoves = [], allMoves = []; for (let r = 0; r <= rows; r++) for (let c = 0; c < cols; c++) if (gameState.horizontalLines[r][c] === 0) { const result = evaluateMove('h', r, c), move = { type: 'h', row: r, col: c }; allMoves.push(move); if (result.gain > 0) gainMoves.push(move); else if (result.lost === 0) normalMoves.push(move); else lostMoves.push({ ...move, lostCount: result.lost }); } for (let r = 0; r < rows; r++) for (let c = 0; c <= cols; c++) if (gameState.verticalLines[r][c] === 0) { const result = evaluateMove('v', r, c), move = { type: 'v', row: r, col: c }; allMoves.push(move); if (result.gain > 0) gainMoves.push(move); else if (result.lost === 0) normalMoves.push(move); else lostMoves.push({ ...move, lostCount: result.lost }); } if (gameState.mode === 'challenge') { if (gainMoves.length > 0) return gainMoves[Math.floor(Math.random() * gainMoves.length)]; if (normalMoves.length > 0) return normalMoves[Math.floor(Math.random() * normalMoves.length)]; if (lostMoves.length > 0) { lostMoves.sort((a, b) => a.lostCount - b.lostCount); const minLost = lostMoves[0].lostCount; const minLostMoves = lostMoves.filter(m => m.lostCount === minLost); return minLostMoves[Math.floor(Math.random() * minLostMoves.length)]; } return null; } if (gameState.aiDifficulty === AI_EASY && Math.random() < 0.5 && allMoves.length > 0) return allMoves[Math.floor(Math.random() * allMoves.length)]; if (gameState.aiDifficulty === AI_HARD && gainMoves.length > 0) return gainMoves[0]; if (gainMoves.length > 0) return gainMoves[Math.floor(Math.random() * gainMoves.length)]; if (normalMoves.length > 0) return normalMoves[Math.floor(Math.random() * normalMoves.length)]; if (lostMoves.length > 0) { lostMoves.sort((a, b) => a.lostCount - b.lostCount); const minLost = lostMoves[0].lostCount; const minLostMoves = lostMoves.filter(m => m.lostCount === minLost); return minLostMoves[Math.floor(Math.random() * minLostMoves.length)]; } return null; }
function evaluateMove(type, row, col) { let gain = 0, lost = 0; if (type === 'h') { gain += checkSquareComplete(row - 1, col, 'h', row, col); gain += checkSquareComplete(row, col, 'h', row, col); if (gain === 0) { lost += checkSquareAlmostComplete(row - 1, col, 'h', row, col); lost += checkSquareAlmostComplete(row, col, 'h', row, col); } } else { gain += checkSquareComplete(row, col - 1, 'v', row, col); gain += checkSquareComplete(row, col, 'v', row, col); if (gain === 0) { lost += checkSquareAlmostComplete(row, col - 1, 'v', row, col); lost += checkSquareAlmostComplete(row, col, 'v', row, col); } } return { gain, lost }; }
function checkSquareComplete(sRow, sCol, lineType, lRow, lCol) { const rows = gameState.rows, cols = gameState.cols; if (sRow < 0 || sRow >= rows || sCol < 0 || sCol >= cols) return 0; if (gameState.squares[sRow][sCol] !== 0) return 0; let edgeCount = 0; if (gameState.horizontalLines[sRow][sCol] !== 0 || (lineType === 'h' && lRow === sRow && lCol === sCol)) edgeCount++; if (gameState.horizontalLines[sRow + 1][sCol] !== 0 || (lineType === 'h' && lRow === sRow + 1 && lCol === sCol)) edgeCount++; if (gameState.verticalLines[sRow][sCol] !== 0 || (lineType === 'v' && lRow === sRow && lCol === sCol)) edgeCount++; if (gameState.verticalLines[sRow][sCol + 1] !== 0 || (lineType === 'v' && lRow === sRow && lCol === sCol + 1)) edgeCount++; return edgeCount === 4 ? 1 : 0; }
function checkSquareAlmostComplete(sRow, sCol, lineType, lRow, lCol) { const rows = gameState.rows, cols = gameState.cols; if (sRow < 0 || sRow >= rows || sCol < 0 || sCol >= cols) return 0; if (gameState.squares[sRow][sCol] !== 0) return 0; let edgeCount = 0; if (gameState.horizontalLines[sRow][sCol] !== 0 || (lineType === 'h' && lRow === sRow && lCol === sCol)) edgeCount++; if (gameState.horizontalLines[sRow + 1][sCol] !== 0 || (lineType === 'h' && lRow === sRow + 1 && lCol === sCol)) edgeCount++; if (gameState.verticalLines[sRow][sCol] !== 0 || (lineType === 'v' && lRow === sRow && lCol === sCol)) edgeCount++; if (gameState.verticalLines[sRow][sCol + 1] !== 0 || (lineType === 'v' && lRow === sRow && lCol === sCol + 1)) edgeCount++; return edgeCount === 3 ? 1 : 0; }

function saveState() { gameState.history.push({ horizontalLines: gameState.horizontalLines.map(r => [...r]), verticalLines: gameState.verticalLines.map(r => [...r]), squares: gameState.squares.map(r => [...r]), currentPlayer: gameState.currentPlayer, scores: [...gameState.scores] }); updateUndoButton(); }
function undoMove(mode) { const isAI = mode === 'ai' || mode === 'challenge', minHistory = isAI ? 2 : 1; if (gameState.history.length < minHistory || gameState.aiThinking) return; if (isAI) gameState.history.pop(); const lastState = gameState.history.pop(); if (lastState) { gameState.horizontalLines = lastState.horizontalLines.map(r => [...r]); gameState.verticalLines = lastState.verticalLines.map(r => [...r]); gameState.squares = lastState.squares.map(r => [...r]); gameState.currentPlayer = lastState.currentPlayer; gameState.scores = [...lastState.scores]; gameState.gameOver = false; gameState.hintMove = null; gameState.showingHint = false; if (mode === 'challenge') document.getElementById('nextLevelBtn').style.display = 'none'; updateStatus('已悔棋，轮到' + (isAI ? '你' : `玩家${gameState.currentPlayer}`)); updateUI(); updateBoardDisplay(); } updateUndoButton(); }
function showHint() { if (gameState.gameOver || gameState.aiThinking || gameState.currentPlayer !== 1) return; const move = getBestMove(); if (move) { gameState.hintMove = move; gameState.showingHint = true; updateStatus('💡 建议位置已高亮显示'); updateBoardDisplay(); setTimeout(() => { gameState.showingHint = false; gameState.hintMove = null; updateBoardDisplay(); if (!gameState.gameOver && gameState.currentPlayer === 1) updateStatus('轮到你了'); }, 3000); } }
function cycleDifficulty() { gameState.aiDifficulty = (gameState.aiDifficulty + 1) % 3; const btn = document.getElementById('difficultyBtn'), names = ['简单', '中等', '困难'], classes = ['diff-easy', 'diff-medium', 'diff-hard']; btn.textContent = names[gameState.aiDifficulty]; btn.className = 'difficulty-btn ' + classes[gameState.aiDifficulty]; restartGame('ai'); }

function updateUI() { let prefix = gameState.mode === 'local' ? 'local' : gameState.mode === 'ai' ? 'ai' : 'challenge'; document.getElementById(`${prefix}Score1`).textContent = gameState.scores[0]; document.getElementById(`${prefix}Score2`).textContent = gameState.scores[1]; updateUndoButton(); }
function updateStatus(text, isGameOver = false) { let statusId = gameState.mode === 'local' ? 'localStatus' : gameState.mode === 'ai' ? 'aiStatus' : 'challengeStatus'; const status = document.getElementById(statusId); status.textContent = text; status.className = 'status-text' + (isGameOver ? ' gameover' : ''); }
function updateUndoButton() { let prefix = gameState.mode === 'local' ? 'local' : gameState.mode === 'ai' ? 'ai' : 'challenge'; const btn = document.getElementById(`${prefix}UndoBtn`); if (!btn) return; const minHistory = (gameState.mode === 'ai' || gameState.mode === 'challenge') ? 2 : 1; btn.disabled = gameState.history.length < minHistory || gameState.aiThinking; }
function showScorePopup(text) { const popup = document.getElementById('scorePopup'); popup.textContent = text; popup.classList.add('show'); setTimeout(() => popup.classList.remove('show'), 800); }
function showAchievementToast(achievementId) { const achievement = ACHIEVEMENTS.find(a => a.id === achievementId); if (!achievement) return; const toast = document.getElementById('achievementToast'); toast.textContent = `${achievement.icon} ${achievement.name}`; toast.classList.add('show'); setTimeout(() => toast.classList.remove('show'), 3000); }
function vibrate(duration) { try { if (navigator.vibrate) navigator.vibrate(duration); } catch (e) {} }

function renderStats() { document.getElementById('statTotal').textContent = stats.totalGames; document.getElementById('statWinRate').textContent = stats.totalGames > 0 ? Math.round(stats.totalWins / stats.totalGames * 100) + '%' : '0%'; document.getElementById('statStreak').textContent = stats.maxWinStreak; document.getElementById('statTime').textContent = Math.floor(stats.totalPlayTime / 60) + '分'; document.getElementById('statAiGames').textContent = stats.aiGames; document.getElementById('statAiWins').textContent = stats.aiWins; document.getElementById('statChallengeGames').textContent = stats.challengeGames; document.getElementById('statMaxLevel').textContent = stats.maxLevel > 0 ? '第' + stats.maxLevel + '关' : '--'; const list = document.getElementById('achievementList'); list.innerHTML = ''; let unlockedCount = 0; ACHIEVEMENTS.forEach(a => { const unlocked = !!stats.achievements[a.id]; if (unlocked) unlockedCount++; const item = document.createElement('div'); item.className = 'achievement-item' + (unlocked ? '' : ' locked'); item.innerHTML = `<div class="achievement-icon">${unlocked ? a.icon : '🔒'}</div><div class="achievement-info"><div class="achievement-name">${a.name}</div><div class="achievement-desc">${a.desc}</div></div>`; list.appendChild(item); }); document.getElementById('achieveCount').textContent = unlockedCount + ' / ' + ACHIEVEMENTS.length; }

// ==================== 远程对战功能 ====================
let onlinePlayerNum = 0;

function initOnlineGame(playerNum) {
    onlinePlayerNum = playerNum;
    gameState.mode = 'online';
    gameState.cols = COLS;
    gameState.rows = ROWS;
    initGameState();
    renderOnlineBoard();
    startOnlineTimer();
}

function renderOnlineBoard() {
    const board = document.getElementById('onlineBoard');
    board.innerHTML = '';
    const rows = gameState.rows, cols = gameState.cols;
    const uiRows = 2 * (rows + 1) - 1, uiCols = 2 * (cols + 1) - 1;
    board.style.gridTemplateColumns = `repeat(${uiCols}, auto)`;
    const rowSizes = [];
    for (let r = 0; r < uiRows; r++) rowSizes.push(r % 2 === 0 ? 'auto' : '1fr');
    board.style.gridTemplateRows = rowSizes.join(' ');
    
    for (let uiRow = 0; uiRow < uiRows; uiRow++) {
        for (let uiCol = 0; uiCol < uiCols; uiCol++) {
            const cell = document.createElement('div');
            if (uiRow % 2 === 0 && uiCol % 2 === 0) {
                cell.className = 'dot';
                cell.id = `online-dot-${uiRow / 2}-${uiCol / 2}`;
                cell.onclick = () => onOnlineDotClick(uiRow / 2, uiCol / 2);
            } else if (uiRow % 2 === 0 && uiCol % 2 === 1) {
                cell.className = 'h-line-cell';
                const line = document.createElement('div');
                line.className = 'h-line';
                line.id = `online-hline-${uiRow / 2}-${(uiCol - 1) / 2}`;
                cell.appendChild(line);
            } else if (uiRow % 2 === 1 && uiCol % 2 === 0) {
                cell.className = 'v-line-cell';
                const line = document.createElement('div');
                line.className = 'v-line';
                line.id = `online-vline-${(uiRow - 1) / 2}-${uiCol / 2}`;
                cell.appendChild(line);
            } else {
                cell.className = 'square-cell';
                const square = document.createElement('div');
                square.className = 'square';
                square.id = `online-square-${(uiRow - 1) / 2}-${(uiCol - 1) / 2}`;
                cell.appendChild(square);
            }
            board.appendChild(cell);
        }
    }
    updateOnlineBoard();
}

function onOnlineDotClick(row, col) {
    if (gameState.gameOver) return;
    if (gameState.currentPlayer !== onlinePlayerNum) {
        updateOnlineStatus('等待对手操作...');
        return;
    }
    
    if (!gameState.selectedDot) {
        gameState.selectedDot = { row, col };
        const dot = document.getElementById(`online-dot-${row}-${col}`);
        if (dot) dot.classList.add('selected');
    } else {
        const sr = gameState.selectedDot.row, sc = gameState.selectedDot.col;
        const oldDot = document.getElementById(`online-dot-${sr}-${sc}`);
        if (oldDot) oldDot.classList.remove('selected');
        
        if (row === sr && col === sc) {
            gameState.selectedDot = null;
            return;
        }
        
        const move = getMove(sr, sc, row, col);
        if (move && isValidMove(move)) {
            applyMove(move);
            sendMove(move); // 发送给对手
            updateOnlineBoard();
            updateOnlineUI();
            checkOnlineGameOver();
        }
        gameState.selectedDot = null;
    }
}

function getMove(sr, sc, er, ec) {
    if (sr === er && Math.abs(sc - ec) === 1) {
        return { type: 'h', row: sr, col: Math.min(sc, ec) };
    } else if (sc === ec && Math.abs(sr - er) === 1) {
        return { type: 'v', row: Math.min(sr, er), col: sc };
    }
    return null;
}

function isValidMove(move) {
    if (move.type === 'h') {
        return gameState.horizontalLines[move.row][move.col] === 0;
    } else {
        return gameState.verticalLines[move.row][move.col] === 0;
    }
}

function applyMove(move) {
    const player = gameState.currentPlayer;
    let scored = false;
    
    if (move.type === 'h') {
        gameState.horizontalLines[move.row][move.col] = player;
        // 检查上下格子
        if (move.row > 0) {
            if (checkSquare(move.row - 1, move.col)) {
                gameState.squares[move.row - 1][move.col] = player;
                gameState.scores[player - 1]++;
                scored = true;
            }
        }
        if (move.row < gameState.rows) {
            if (checkSquare(move.row, move.col)) {
                gameState.squares[move.row][move.col] = player;
                gameState.scores[player - 1]++;
                scored = true;
            }
        }
    } else {
        gameState.verticalLines[move.row][move.col] = player;
        // 检查左右格子
        if (move.col > 0) {
            if (checkSquare(move.row, move.col - 1)) {
                gameState.squares[move.row][move.col - 1] = player;
                gameState.scores[player - 1]++;
                scored = true;
            }
        }
        if (move.col < gameState.cols) {
            if (checkSquare(move.row, move.col)) {
                gameState.squares[move.row][move.col] = player;
                gameState.scores[player - 1]++;
                scored = true;
            }
        }
    }
    
    if (!scored) {
        gameState.currentPlayer = gameState.currentPlayer === 1 ? 2 : 1;
    }
}

function checkSquare(row, col) {
    if (gameState.squares[row][col] !== 0) return false;
    return gameState.horizontalLines[row][col] !== 0 &&
           gameState.horizontalLines[row + 1][col] !== 0 &&
           gameState.verticalLines[row][col] !== 0 &&
           gameState.verticalLines[row][col + 1] !== 0;
}

function handleOnlineMove(move) {
    applyMove(move);
    updateOnlineBoard();
    updateOnlineUI();
    checkOnlineGameOver();
}

function updateOnlineBoard() {
    for (let r = 0; r <= gameState.rows; r++) {
        for (let c = 0; c < gameState.cols; c++) {
            const line = document.getElementById(`online-hline-${r}-${c}`);
            if (line) {
                const val = gameState.horizontalLines[r][c];
                line.className = 'h-line' + (val === 1 ? ' line-p1' : val === 2 ? ' line-p2' : '');
            }
        }
    }
    for (let r = 0; r < gameState.rows; r++) {
        for (let c = 0; c <= gameState.cols; c++) {
            const line = document.getElementById(`online-vline-${r}-${c}`);
            if (line) {
                const val = gameState.verticalLines[r][c];
                line.className = 'v-line' + (val === 1 ? ' line-p1' : val === 2 ? ' line-p2' : '');
            }
        }
    }
    for (let r = 0; r < gameState.rows; r++) {
        for (let c = 0; c < gameState.cols; c++) {
            const square = document.getElementById(`online-square-${r}-${c}`);
            if (square) {
                const val = gameState.squares[r][c];
                square.className = 'square' + (val === 1 ? ' square-p1' : val === 2 ? ' square-p2' : '');
            }
        }
    }
}

function updateOnlineUI() {
    document.getElementById('onlineScore1').textContent = gameState.scores[0];
    document.getElementById('onlineScore2').textContent = gameState.scores[1];
    
    if (!gameState.gameOver) {
        if (gameState.currentPlayer === onlinePlayerNum) {
            updateOnlineStatus('轮到你了，点击圆点画线');
        } else {
            updateOnlineStatus('等待对手操作...');
        }
    }
}

function updateOnlineStatus(text) {
    document.getElementById('onlineStatus').textContent = text;
}

function checkOnlineGameOver() {
    let allFilled = true;
    for (let r = 0; r < gameState.rows; r++) {
        for (let c = 0; c < gameState.cols; c++) {
            if (gameState.squares[r][c] === 0) allFilled = false;
        }
    }
    
    if (allFilled) {
        gameState.gameOver = true;
        const s1 = gameState.scores[0], s2 = gameState.scores[1];
        let result;
        if (s1 > s2) {
            result = onlinePlayerNum === 1 ? '🎉 你赢了！' : '😢 你输了';
        } else if (s2 > s1) {
            result = onlinePlayerNum === 2 ? '🎉 你赢了！' : '😢 你输了';
        } else {
            result = '🤝 平局！';
        }
        updateOnlineStatus(result);
    }
}

let onlineTimerInterval = null;
let onlineStartTime = 0;

function startOnlineTimer() {
    if (onlineTimerInterval) clearInterval(onlineTimerInterval);
    onlineStartTime = Date.now();
    onlineTimerInterval = setInterval(() => {
        const elapsed = Math.floor((Date.now() - onlineStartTime) / 1000);
        const min = String(Math.floor(elapsed / 60)).padStart(2, '0');
        const sec = String(elapsed % 60).padStart(2, '0');
        document.getElementById('onlineTimer').textContent = `⏱️ ${min}:${sec}`;
    }, 1000);
}

init();
