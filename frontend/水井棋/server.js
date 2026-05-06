const WebSocket = require('ws');

const PORT = 3000;
const wss = new WebSocket.Server({ port: PORT });

// 存储房间信息
const rooms = new Map();

// 生成6位房间号
function generateRoomId() {
    return Math.random().toString(36).substring(2, 8).toUpperCase();
}

wss.on('connection', (ws) => {
    console.log('新玩家连接');
    
    ws.on('message', (data) => {
        try {
            const msg = JSON.parse(data);
            
            switch (msg.type) {
                case 'create':
                    // 创建房间
                    const roomId = generateRoomId();
                    rooms.set(roomId, {
                        players: [ws],
                        gameState: null,
                        currentPlayer: 1
                    });
                    ws.roomId = roomId;
                    ws.playerNum = 1;
                    ws.send(JSON.stringify({
                        type: 'created',
                        roomId: roomId,
                        playerNum: 1
                    }));
                    console.log(`房间 ${roomId} 已创建`);
                    break;
                    
                case 'join':
                    // 加入房间
                    const room = rooms.get(msg.roomId);
                    if (!room) {
                        ws.send(JSON.stringify({ type: 'error', message: '房间不存在' }));
                        return;
                    }
                    if (room.players.length >= 2) {
                        ws.send(JSON.stringify({ type: 'error', message: '房间已满' }));
                        return;
                    }
                    room.players.push(ws);
                    ws.roomId = msg.roomId;
                    ws.playerNum = 2;
                    ws.send(JSON.stringify({
                        type: 'joined',
                        roomId: msg.roomId,
                        playerNum: 2
                    }));
                    // 通知房主游戏开始
                    room.players[0].send(JSON.stringify({
                        type: 'start',
                        message: '对手已加入，游戏开始！'
                    }));
                    ws.send(JSON.stringify({
                        type: 'start',
                        message: '已加入房间，游戏开始！'
                    }));
                    console.log(`玩家加入房间 ${msg.roomId}`);
                    break;
                    
                case 'move':
                    // 同步移动
                    const moveRoom = rooms.get(ws.roomId);
                    if (moveRoom) {
                        moveRoom.players.forEach(player => {
                            if (player !== ws && player.readyState === WebSocket.OPEN) {
                                player.send(JSON.stringify({
                                    type: 'move',
                                    move: msg.move,
                                    player: ws.playerNum
                                }));
                            }
                        });
                    }
                    break;
                    
                case 'sync':
                    // 同步完整游戏状态
                    const syncRoom = rooms.get(ws.roomId);
                    if (syncRoom) {
                        syncRoom.players.forEach(player => {
                            if (player !== ws && player.readyState === WebSocket.OPEN) {
                                player.send(JSON.stringify({
                                    type: 'sync',
                                    gameState: msg.gameState
                                }));
                            }
                        });
                    }
                    break;
                    
                case 'restart':
                    // 重新开始
                    const restartRoom = rooms.get(ws.roomId);
                    if (restartRoom) {
                        restartRoom.players.forEach(player => {
                            player.send(JSON.stringify({ type: 'restart' }));
                        });
                    }
                    break;
            }
        } catch (e) {
            console.error('消息解析错误:', e);
        }
    });
    
    ws.on('close', () => {
        console.log('玩家断开连接');
        if (ws.roomId) {
            const room = rooms.get(ws.roomId);
            if (room) {
                // 通知另一个玩家
                room.players.forEach(player => {
                    if (player !== ws && player.readyState === WebSocket.OPEN) {
                        player.send(JSON.stringify({
                            type: 'opponent_left',
                            message: '对手已离开'
                        }));
                    }
                });
                // 如果房间空了，删除房间
                room.players = room.players.filter(p => p !== ws);
                if (room.players.length === 0) {
                    rooms.delete(ws.roomId);
                    console.log(`房间 ${ws.roomId} 已删除`);
                }
            }
        }
    });
});

console.log(`🎮 水井棋对战服务器已启动: ws://localhost:${PORT}`);
console.log('等待玩家连接...');
