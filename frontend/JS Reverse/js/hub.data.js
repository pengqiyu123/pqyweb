(function (global) {
  var LEVELS = [
    {
      id: 'level1',
      title: '编码还是加密？',
      group: '现场勘查',
      difficulty: 'concept',
      type: 'quiz',
      caseBrief: '你在入侵现场发现了一串可疑的编码字符串。调查员怀疑它只是传输伪装，而不是严格意义上的加密。',
      clueFragment: '攻击者先用 Base64 编码隐藏了明文数据，说明早期通信并不复杂。',
      evidenceFile: 'evidence_01_encoded.txt',
      acceptance: '提交正确的 Base64 编码结果与还原明文',
      hints: [
        '先想清楚编码和加密的区别，Base64 可以直接逆向还原。',
        '浏览器里可用 btoa() 和 atob() 快速验证结果。',
        '把 hello-pqy 编码成 Base64，并把给定编码重新解码回原文即可。'
      ],
      tutorial: '<p>Base64 是编码，不是加密。它的作用是把二进制或文本转成更适合传输的字符形式，因此天然可逆。</p><p>逆向场景里，如果一段看似随机的字符串只经过 Base64 处理，那么核心工作不是破译，而是识别它只是伪装。</p>',
      verifyMode: 'multi-field',
      answerFormat: 'multi-field',
      starterInput: {
        plainText: 'hello-pqy',
        encodedText: 'YWxlcnQoJ3BxeScp'
      },
      expectedOutput: {
        encoded: 'aGVsbG8tcHF5',
        decoded: "alert('pqy')"
      },
      answerHash: '',
      salt: '',
      tags: ['base64', 'concept'],
      codePreview: "const message = 'hello-pqy';\nconst hidden = 'YWxlcnQoJ3BxeScp';\n// 识别这里到底是编码还是加密",
      script: ''
    },
    {
      id: 'level2',
      title: '指纹与摘要',
      group: '现场勘查',
      difficulty: 'concept',
      type: 'quiz',
      caseBrief: '日志中出现了固定长度的十六进制字符串。你需要判断它们属于哪一类摘要，并说明为何无法像 Base64 一样直接还原。',
      clueFragment: '攻击者开始使用摘要校验数据完整性，说明脚本里已经出现签名思维。',
      evidenceFile: 'evidence_02_hash.log',
      acceptance: '提交 MD5、SHA256 摘要，并选对“摘要不可逆”',
      hints: [
        'MD5 和 SHA256 都是单向摘要，不负责解密。',
        '用 CryptoJS.MD5 和 CryptoJS.SHA256 分别算同一段文本。',
        '最终要提交同一原文的两个摘要值，并确认摘要不是可逆编码。'
      ],
      tutorial: '<p>摘要函数把任意长度输入压缩成固定长度输出，典型用途是校验与签名。MD5 和 SHA256 都是单向函数，不提供“还原明文”的能力。</p><p>逆向时遇到摘要函数，更常见的任务是还原参与摘要的拼接规则，而不是反推出原文。</p>',
      verifyMode: 'multi-field',
      answerFormat: 'multi-field',
      starterInput: {
        plainText: 'shadow-entry'
      },
      expectedOutput: {
        md5: '1e877c51542abb783d71845c0e2ab62d',
        sha256: '1d0bdb2ccaca599827e3ec26447ff03bb9dc8dd86ed82376ecacb010fa108c40',
        reversible: '不可逆'
      },
      answerHash: '',
      salt: '',
      tags: ['hash', 'md5', 'sha256'],
      codePreview: "const source = 'shadow-entry';\n// 计算它的 MD5 和 SHA256，并判断摘要能否逆向回原文",
      script: ''
    },
    {
      id: 'level3',
      title: '对称的秘密',
      group: '现场勘查',
      difficulty: 'concept',
      type: 'quiz',
      caseBrief: '你截获了一段密文，同时在配置片段里找到了一个固定密钥。请验证它是否属于典型对称加密通信。',
      clueFragment: '攻击者与服务器共享同一把密钥，说明后续证据里可能会出现固定 AES 加密流程。',
      evidenceFile: 'evidence_03_aes.bin',
      acceptance: '用给定密钥完成加密和解密',
      hints: [
        'AES 属于对称加密，加解密都用同一把密钥。',
        '本关只需要用 CryptoJS.AES 处理固定明文和固定密文。',
        '先验证你能解出密文，再把指定明文加密后提交。'
      ],
      tutorial: '<p>AES 是典型的对称加密。逆向中如果能找到固定 key、iv 和 mode，通常就能直接在本地复现加解密流程。</p><p>这类题的核心不是记 API，而是理解“同一密钥可双向处理数据”的特征。</p>',
      verifyMode: 'multi-field',
      answerFormat: 'multi-field',
      starterInput: {
        key: 'shadow-key-2026',
        plainText: 'case-open',
        encryptedText: 'U2FsdGVkX18JPsY+ePVg5pPI9G6PFGui6LbphIEn0cI='
      },
      expectedOutput: {
        encryptedPlainText: 'case-open',
        decrypted: 'shadow-terminal'
      },
      answerHash: '',
      salt: '',
      tags: ['aes', 'symmetric'],
      codePreview: "const key = 'shadow-key-2026';\nconst encrypted = 'U2FsdGVkX18JPsY+ePVg5pPI9G6PFGui6LbphIEn0cI=';\n// 验证这段通信是否使用固定密钥 AES",
      script: ''
    },
    {
      id: 'level4',
      title: '签名的秘密',
      group: '现场勘查',
      difficulty: 'concept',
      type: 'quiz',
      caseBrief: 'API 日志显示每个请求都带有 sign 参数。你需要根据给定规则还原签名生成方式，判断攻击者如何伪造合法请求。',
      clueFragment: '攻击者已经掌握签名规则，后续所有伪装请求都可能基于同类拼接逻辑。',
      evidenceFile: 'evidence_04_sign.req',
      acceptance: '根据 timestamp 和 uid 提交正确 sign',
      hints: [
        '签名常见做法是把参数与 salt 拼接后再做 MD5。',
        '本关的关键不是破解哈希，而是还原拼接顺序。',
        '把 timestamp + secret + uid 拼成字符串后做 MD5。'
      ],
      tutorial: '<p>签名题的重点从来不是 MD5 本身，而是“哪些参数参与签名、按什么顺序拼接”。</p><p>真实站点中，你往往需要通过断点、调用栈或日志来定位拼接逻辑，再本地复现算法。</p>',
      verifyMode: 'multi-field',
      answerFormat: 'multi-field',
      starterInput: {
        timestamp: '1715088888',
        uid: '10086',
        secret: 'pqy-shadow'
      },
      expectedOutput: {
        sign: '92f5d11d4fed528b8768ae2148bda4e9'
      },
      answerHash: '',
      salt: '',
      tags: ['sign', 'md5'],
      codePreview: "function getSign(timestamp, uid) {\n  var secret = 'pqy-shadow';\n  return md5(timestamp + secret + uid);\n}",
      script: ''
    }
  ];

  function createReverseLevel(config) {
    return {
      id: config.id,
      title: config.title,
      group: config.group,
      difficulty: config.difficulty,
      type: 'reverse',
      caseBrief: config.caseBrief,
      clueFragment: config.clueFragment,
      evidenceFile: config.evidenceFile,
      acceptance: config.acceptance,
      hints: config.hints,
      tutorial: config.tutorial,
      verifyMode: 'hash',
      answerFormat: 'text',
      starterInput: {},
      expectedOutput: {},
      answerHash: config.answerHash,
      salt: config.salt,
      tags: config.tags,
      codePreview: config.codePreview,
      script: 'js/challenges/' + config.id + '.js'
    };
  }

  LEVELS = LEVELS.concat([
    createReverseLevel({
      id: 'level5',
      title: '被“藏起来”的密码',
      group: '初步取证',
      difficulty: 'easy',
      caseBrief: '攻击者遗留的脚本中变量名全是 a/b/c。你要从混淆变量中定位密码生成函数，并提交真正的密码字符串。',
      clueFragment: '变量名混淆只是表面伪装，真正的关键逻辑仍然藏在固定函数里。',
      evidenceFile: 'evidence_05_password.js',
      acceptance: '提交还原出的最终密码字符串',
      hints: ['先从返回值看哪个函数最终产出了密码。', '变量名可以乱，但字符串和拼接顺序不会凭空消失。', '最终密码是由 3 段固定字符串拼接而成。'],
      tutorial: '<p>变量重命名是最基础的混淆。新手最容易被奇怪命名吓住，但真正要看的不是名字，而是数据流向。</p>',
      salt: 'jsr_l5',
      answerHash: '41bd5b82656b62b1a48d6d9876f5779343688c460b75e73d270d2a21b3fde72c',
      tags: ['rename', 'easy'],
      codePreview: "var a='sha';var b='dow';var c='-pw';\nfunction x(){return a+b+c;}"
    }),
    createReverseLevel({
      id: 'level6',
      title: 'IIFE 自执行之谜',
      group: '初步取证',
      difficulty: 'easy',
      caseBrief: '一个自执行函数包裹着整个脚本。你需要找出真正的入口结果，而不是被外层封装误导。',
      clueFragment: '攻击者开始用 IIFE 隐藏入口，说明后续逻辑会越来越依赖包装层。',
      evidenceFile: 'evidence_06_iife.js',
      acceptance: '提交 IIFE 最终计算结果',
      hints: ['把注意力放在 IIFE 返回值上。', '自执行函数外层只是在“包”，核心逻辑仍在内部。', '最终结果是内部函数对 token 片段的拼接。'],
      tutorial: '<p>IIFE 的核心价值是隔离作用域。逆向时不需要被包裹形式吓住，直接跟返回值和调用关系即可。</p>',
      salt: 'jsr_l6',
      answerHash: '47158dd3e79579de517417d5e074ea6cc835e4e27ff6e2f7574613b9db02ba79',
      tags: ['iife', 'easy'],
      codePreview: "(function(){var p='case';var q='-entry';function run(){return p+q;}return run();})();"
    }),
    createReverseLevel({
      id: 'level7',
      title: '签名算法还原',
      group: '初步取证',
      difficulty: 'easy',
      caseBrief: '攻击者篡改了 sign 算法并重命名了变量。你需要还原拼接顺序，并提交最终 sign。',
      clueFragment: '签名顺序被改成 uid+timestamp+secret，这和正常实现相反。',
      evidenceFile: 'evidence_07_sign.js',
      acceptance: '提交给定参数对应的 sign',
      hints: ['变量名不重要，拼接顺序才重要。', '观察拼接时谁在前谁在后。', '本关是 uid + timestamp + secret 再做 MD5。'],
      tutorial: '<p>一旦参数顺序改变，摘要结果就会完全不同。逆向时最常见的坑不是函数名，而是“看似一样其实顺序不同”。</p>',
      salt: 'jsr_l7',
      answerHash: '5a11ce709990c98db4192b60ae8b64064267a0d851f12ec6c890a42eb61c1f42',
      tags: ['sign', 'rename'],
      codePreview: "function s(u,t){var k='trace';return md5(u+t+k);}\n// uid=10010,timestamp=1715000000"
    }),
    createReverseLevel({
      id: 'level8',
      title: 'Base64 伪装术',
      group: '初步取证',
      difficulty: 'easy',
      caseBrief: '关键参数被 Base64 包裹，看似随机字符串。你要识别并解出它真正表示的权限字段。',
      clueFragment: 'atob 解开后出现 isAdmin，说明攻击者在权限判断上做了最轻量级伪装。',
      evidenceFile: 'evidence_08_base64.js',
      acceptance: '提交解码后的明文参数',
      hints: ['先判断它是否只是 Base64。', '浏览器原生就能解这类编码。', '最终得到的是一个布尔权限字段。'],
      tutorial: '<p>很多“加密参数”其实只是编码伪装。看到字符分布很像 Base64 时，应先快速验证，避免过度分析。</p>',
      salt: 'jsr_l8',
      answerHash: 'c2f8f838a9573d99b71c15e0b783e5a32d1ddf5f1453adda72be18dda060b29e',
      tags: ['base64', 'easy'],
      codePreview: "const hidden='aXNBZG1pbg==';\nfunction openFlag(){return atob(hidden);}"
    }),
    createReverseLevel({
      id: 'level9',
      title: '变量迷宫',
      group: '深度分析',
      difficulty: 'medium',
      caseBrief: '自动化混淆把变量名全部改成 _0x 开头。你需要跟踪 3 个关键变量的意义，并提交最终业务结果。',
      clueFragment: '变量映射关系被还原后，攻击者的核心 token 生成流程开始显形。',
      evidenceFile: 'evidence_09_mangled.js',
      acceptance: '提交还原后的最终 token',
      hints: ['先找返回值，再倒查参与运算的 3 个变量。', 'Watch 变量最适合这种题。', '本关真正的业务值是 3 段字符串拼成的 token。'],
      tutorial: '<p>自动混淆让变量不可读，但执行时的数据流依旧存在。逆向时先抓“谁返回了最终结果”，再反推中间变量含义。</p>',
      salt: 'jsr_l9',
      answerHash: 'a3056cd3ae536ce1b3253f3d5e9e459baff844b0f54512ec8563bea768e74dc4',
      tags: ['mangled', 'medium'],
      codePreview: "var _0x1='trace';var _0x2='-';var _0x3='seed';\nfunction _0x4(){return _0x1+_0x2+_0x3;}"
    }),
    createReverseLevel({
      id: 'level10',
      title: '字符串数组 Base64',
      group: '深度分析',
      difficulty: 'medium',
      caseBrief: '所有关键字符串都被提取到了数组里，并做了 Base64 编码。你需要解出真正的目标 token。',
      clueFragment: '字符串数组里藏着命令参数，攻击者开始系统性地隐藏关键文本。',
      evidenceFile: 'evidence_10_stringarray.js',
      acceptance: '提交数组解码后的目标 token',
      hints: ['先整体找数组，再逐个解码。', 'Base64 解开后不要忘了还原访问顺序。', '只有一段字符串最终参与了 token 生成。'],
      tutorial: '<p>stringArray 是最常见的阅读干扰手段。遇到这类结构，第一步不是硬看，而是整体抽取数组内容后批量解码。</p>',
      salt: 'jsr_l10',
      answerHash: 'a7bac329a73c82164b039c1d25c17adc3bbfce415d286a7eb4e998545d96db8f',
      tags: ['stringArray', 'base64'],
      codePreview: "var arr=['Y2FzZQ==','LXRva2Vu','LWFjY2Vzcw=='];\nfunction pick(i){return atob(arr[i]);}"
    }),
    createReverseLevel({
      id: 'level11',
      title: '字符串数组 RC4',
      group: '深度分析',
      difficulty: 'medium',
      caseBrief: '这次字符串数组不再是 Base64，而是 RC4 处理过的伪装内容。你需要找到密钥并提交签名种子。',
      clueFragment: 'RC4 还原后出现的 seed 证明攻击者已经开始用更系统的字符串保护策略。',
      evidenceFile: 'evidence_11_rc4.js',
      acceptance: '提交 RC4 解出的签名种子',
      hints: ['本关不要求你真正手写 RC4，只要识别“密钥在代码里”。', '关注 rc4(key,data) 里的 key。', '解出的目标 seed 是一个短横线连接的短语。'],
      tutorial: '<p>看到 rc4、解码函数包装或字符串表恢复逻辑时，要优先找“密钥从哪里来”。首版训练重点是识别流程，而不是自己重写整套解码器。</p>',
      salt: 'jsr_l11',
      answerHash: 'acde032512864ddad8f7178af5945a29aad39b3677df805b78d62c6566ea5059',
      tags: ['rc4', 'stringArray'],
      codePreview: "function rc4(k,d){return 'hidden-seed';}\nvar key='shadow';\nvar encoded='...';\n// 目标是还原最终 seed"
    }),
    createReverseLevel({
      id: 'level12',
      title: '数组旋转与偏移',
      group: '深度分析',
      difficulty: 'medium',
      caseBrief: '字符串数组被旋转和打乱，索引也发生偏移。你需要恢复数组顺序并提交最终拼接结果。',
      clueFragment: '攻击者开始同时隐藏字符串和访问索引，普通搜索已经不够用了。',
      evidenceFile: 'evidence_12_rotate.js',
      acceptance: '提交还原后的最终拼接结果',
      hints: ['先搞清数组原始顺序，再看索引如何偏移。', '旋转和 shuffle 会让“取值正确但顺序错误”成为常见陷阱。', '最终结果是 3 段单词按正确顺序拼接。'],
      tutorial: '<p>数组 rotate / shuffle 的本质是破坏“看上去顺手”的访问顺序。逆向时要把数组内容和索引访问拆开看，分别恢复。</p>',
      salt: 'jsr_l12',
      answerHash: '682758d29cd94c7984c3120361f4370bb6e63d269de0a10a391dba602bf8bffa',
      tags: ['rotate', 'shuffle'],
      codePreview: "var arr=['token','case','trace'];\narr.push(arr.shift());\nfunction g(i){return arr[i-1];}"
    }),
    createReverseLevel({
      id: 'level13',
      title: '控制流迷宫',
      group: '追踪溯源',
      difficulty: 'hard',
      caseBrief: '正常的 if-else 被拆成了 switch-case 跳转表。你需要根据执行顺序还原逻辑，提交最终 sign。',
      clueFragment: '控制流被拆散后，攻击者的验证路径终于显露出固定顺序。',
      evidenceFile: 'evidence_13_cfg.js',
      acceptance: '提交还原流程后的 sign',
      hints: ['不要试图一次看懂全部分支，先跟主执行顺序。', '记录 case 的跳转顺序比读注释更重要。', '主逻辑执行顺序固定后，就能推回真正的拼接流程。'],
      tutorial: '<p>controlFlowFlattening 的关键破坏是顺序感。逆向时应把“分支块”和“执行路径”分开处理，先恢复路径，再还原语义。</p>',
      salt: 'jsr_l13',
      answerHash: 'f00526d6778f4ea6b826f8f44b6f14f2423245a1f879b445c3fb855be601e9f6',
      tags: ['controlFlowFlattening'],
      codePreview: "var order='2|0|3|1'.split('|');\nvar idx=0;while(true){switch(order[idx++]){case '0': ... }}"
    }),
    createReverseLevel({
      id: 'level14',
      title: '死代码迷雾',
      group: '追踪溯源',
      difficulty: 'hard',
      caseBrief: '脚本里充满了永远不会执行的分支。你需要排除噪声，找到真实入口函数并提交正确结果。',
      clueFragment: '大量死代码只是烟雾弹，真正的入口只藏在一小段执行路径里。',
      evidenceFile: 'evidence_14_deadcode.js',
      acceptance: '提交真实入口产出的结果',
      hints: ['死代码通常“长得吓人但跑不到”。', '断点或手动执行路径能帮你快速筛掉噪声。', '最终结果来自唯一被调用的入口函数。'],
      tutorial: '<p>死代码注入的目标是让你在不重要的地方耗时间。逆向时要优先回答“这段代码真的会执行吗”。</p>',
      salt: 'jsr_l14',
      answerHash: 'd51b455147816331ccc1b1afd216923d980e0e6d2be7a248148f0de8e204cb21',
      tags: ['deadCodeInjection'],
      codePreview: "function fake(){return 'noise';}\nfunction entry(){return 'shadow-core';}\nif(false){fake();} else {entry();}"
    }),
    createReverseLevel({
      id: 'level15',
      title: 'eval 黑洞',
      group: '追踪溯源',
      difficulty: 'hard',
      caseBrief: '关键代码被包进了 eval(atob(...))。你要把它扣出来运行，提交运行后得到的密钥或 token。',
      clueFragment: '真正的加密逻辑藏在动态代码里，攻击者已经开始使用运行时展开技巧。',
      evidenceFile: 'evidence_15_eval.js',
      acceptance: '提交动态代码运行结果',
      hints: ['eval 前通常会先还原字符串。', '先解开 atob 内容，再把真正代码单独跑。', '本关目标结果是一个终端访问 token。'],
      tutorial: '<p>动态执行并不可怕。第一步是让“即将执行的源码”显形，第二步才是分析它做了什么。</p>',
      salt: 'jsr_l15',
      answerHash: '9465f0f68413d2f5ff8b515c1df44828689de809516b9630211c41dd93e83b8c',
      tags: ['eval', 'dynamic'],
      codePreview: "eval(atob('Y29uc29sZS5sb2coJ3NoYWRvdy10b2tlbicpOw=='));"
    }),
    createReverseLevel({
      id: 'level16',
      title: '调用链追踪',
      group: '追踪溯源',
      difficulty: 'hard',
      caseBrief: '加密入口被包在多层函数里。你需要从最终输出回溯到源头，并提交正确计算结果。',
      clueFragment: '调用链被剥离后，完整加密入口终于被确认，攻击者的封装套路也暴露了。',
      evidenceFile: 'evidence_16_stack.js',
      acceptance: '提交给定参数的最终计算结果',
      hints: ['先看最终输出从哪一层返回。', '别试图同时看 10 层函数，按调用方向逐层回溯。', '最终结果仍然是可复现的固定字符串。'],
      tutorial: '<p>多层封装常见于真实前端。逆向时最稳的做法是以最终输出为起点，沿调用链逐层缩小范围。</p>',
      salt: 'jsr_l16',
      answerHash: '3b7999c4972ae7d828c4f47cc98447cc1b3caf959db225c239f115d6e6493227',
      tags: ['stack', 'trace'],
      codePreview: "function a(){return b();}\nfunction b(){return c();}\nfunction c(){return 'trace-linked';}"
    }),
    createReverseLevel({
      id: 'level17',
      title: '全副武装',
      group: '终极揭秘',
      difficulty: 'boss',
      caseBrief: '攻击者的主控脚本把变量混淆、字符串伪装、控制流扁平和死代码全部混在一起。你需要在限定输入下还原最终结果。',
      clueFragment: '主控服务器地址与关键调度 token 被确认，攻击者身份已经初步锁定。',
      evidenceFile: 'evidence_17_master.js',
      acceptance: '提交主控脚本的最终加密结果',
      hints: ['先不要被“全混淆”吓住，仍然先找最终输出。', '主控脚本只是把前面学过的套路叠在一起。', '先拆字符串，再拆顺序，最后还原输出。'],
      tutorial: '<p>综合题不意味着需要新知识，往往只是把旧手法叠加。关键是保持“先结果、后路径、再语义”的分析顺序。</p>',
      salt: 'jsr_l17',
      answerHash: '23b677207db8106eeba9d8e74a1cd2bf1431a3aad97958bf41e733339ae8a379',
      tags: ['boss', 'all-in-one'],
      codePreview: "var pack=['master','trace','node'];\nfunction run(){return pack[0]+'-'+pack[1]+'-'+pack[2];}"
    }),
    createReverseLevel({
      id: 'level18',
      title: 'VM 虚拟机终极',
      group: '终极揭秘',
      difficulty: 'boss',
      caseBrief: '最终证据被简化 VM 解释器保护。你需要读懂指令含义，还原业务函数输出，完成结案。',
      clueFragment: '所有线索拼图完成：真正的入侵者通过一套简化脚本引擎批量伪造请求并窃取数据。',
      evidenceFile: 'evidence_18_vm.js',
      acceptance: '提交 VM 解释后的业务输出结果',
      hints: ['先别把它想得太复杂，首版 VM 只是几个简单指令。', '观察 opcode 如何把字符串压栈和拼接。', '最终输出是一个完整的结案口令。'],
      tutorial: '<p>VM 保护的难点在于“逻辑不再直接写在 JS 语句里”，而是藏在指令序列和解释器行为中。理解每条指令在做什么，就是还原业务逻辑的开始。</p>',
      salt: 'jsr_l18',
      answerHash: 'e5a90bf123abbba9129b10929168f40a2fce6da13a1e450556a119664b637115',
      tags: ['vm', 'boss'],
      codePreview: "var code=[['PUSH','shadow'],['PUSH','-case'],['ADD'],['PUSH','-closed'],['ADD']];\n// VM 执行后得到最终口令"
    })
  ]);

  var ACHIEVEMENTS = [
    { id: 'first_case', title: '初入案场', description: '完成第 1 关', check: function (s) { return !!s.completedLevels.level1; } },
    { id: 'no_hint_once', title: '零提示破译', description: '任意 1 关无提示通关', check: function (s) { return Object.keys(s.completedLevels).some(function (id) { return (s.usedHintsByLevel[id] || 0) === 0; }); } },
    { id: 'three_star_chain', title: '连胜调查员', description: '连续 3 关获得 3 星', check: function (s) { return hasStreak(s, 3); } },
    { id: 'hash_apprentice', title: '哈希学徒', description: '完成第 2 与第 4 关', check: function (s) { return !!s.completedLevels.level2 && !!s.completedLevels.level4; } },
    { id: 'obf_hunter', title: '混淆猎手', description: '完成第 5-8 关', check: function (s) { return completedRange(s, 5, 8); } },
    { id: 'string_decoder', title: '字符串解码员', description: '完成第 10-12 关', check: function (s) { return completedRange(s, 10, 12); } },
    { id: 'cfg_tracker', title: '控制流追踪者', description: '完成第 13 关', check: function (s) { return !!s.completedLevels.level13; } },
    { id: 'code_forensics', title: '代码法医', description: '完成第 14 关', check: function (s) { return !!s.completedLevels.level14; } },
    { id: 'sandbox_breaker', title: '沙盒破译者', description: '完成第 15 关', check: function (s) { return !!s.completedLevels.level15; } },
    { id: 'chain_inspector', title: '链路侦查专家', description: '完成第 16 关', check: function (s) { return !!s.completedLevels.level16; } },
    { id: 'shadow_ender', title: '暗影终结者', description: '完成第 18 关', check: function (s) { return !!s.completedLevels.level18; } },
    { id: 'perfect_case', title: '完美结案', description: '18 关全部 3 星通关', check: function (s) { return completedRange(s, 1, 18) && Object.keys(s.starsByLevel).length >= 18 && Object.keys(s.starsByLevel).every(function (id) { return s.starsByLevel[id] === 3; }); } }
  ];

  var BADGES = [
    { id: 'badge_1', title: '现场勘查员', group: '现场勘查', range: [1, 4] },
    { id: 'badge_2', title: '初步取证员', group: '初步取证', range: [5, 8] },
    { id: 'badge_3', title: '深度分析员', group: '深度分析', range: [9, 12] },
    { id: 'badge_4', title: '溯源追踪员', group: '追踪溯源', range: [13, 16] },
    { id: 'badge_5', title: '终局破译师', group: '终极揭秘', range: [17, 18] }
  ];

  var TIMELINE = [
    '入侵发生：初步伪装通信被发现。',
    '数据编码/加密：攻击者开始保护传输数据。',
    '签名被伪造：请求伪装成合法调用。',
    '主控脚本曝光：多重混淆开始集中出现。',
    '身份暴露：所有线索汇总完成结案。'
  ];

  var STAGE_ARCS = [
    {
      id: 'scene-entry',
      group: '现场勘查',
      title: '第一幕 · 现场勘查',
      summary: '从最浅层的传输伪装开始，确认攻击者如何藏匿最初的通信痕迹。',
      objective: '锁定编码、摘要、AES 与签名四类基础证据的真实用途。',
      atmosphere: '案发终端仍在发热，最原始的痕迹还没有完全散去。',
      range: [1, 4]
    },
    {
      id: 'scene-evidence',
      group: '初步取证',
      title: '第二幕 · 初步取证',
      summary: '攻击脚本开始对变量、入口和权限字段做轻量伪装，调查进入第一层混淆。',
      objective: '从表层混淆中提取真实密码、入口结果与签名流程。',
      atmosphere: '脚本被人为打乱，但攻击者还没有来得及彻底封装所有入口。',
      range: [5, 8]
    },
    {
      id: 'scene-decode',
      group: '深度分析',
      title: '第三幕 · 深度分析',
      summary: '字符串表、偏移索引与解码器开始系统化出现，证据墙进入中级解混淆阶段。',
      objective: '恢复字符串真实内容，拆开索引扰动，回到业务逻辑本身。',
      atmosphere: '表面文字已经不可信，真正的线索被塞进了解码流程里。',
      range: [9, 12]
    },
    {
      id: 'scene-trace',
      group: '追踪溯源',
      title: '第四幕 · 追踪溯源',
      summary: '控制流、死代码与动态执行开始把阅读路径彻底打碎，必须顺着调用链回到源头。',
      objective: '排除噪声、追踪执行顺序、还原入口与关键返回值。',
      atmosphere: '攻击者显然在拖延阅读时间，你需要只看真正会跑的那条路径。',
      range: [13, 16]
    },
    {
      id: 'scene-finale',
      group: '终极揭秘',
      title: '第五幕 · 终极揭秘',
      summary: '所有套路开始叠加，主控脚本和简化 VM 一起出场，结案只差最后两份硬证据。',
      objective: '拼合整条攻击链，确认主控逻辑与最终结案口令。',
      atmosphere: '所有证据终于汇聚到一张桌面上，最后的遮挡只剩下演出层。',
      range: [17, 18]
    }
  ];

  var PRESENTATION = {
    level1: {
      objective: '确认可疑字符串只是编码伪装，不是加密通信。',
      action: '对比可逆与不可逆处理方式，先还原再判断。',
      deliverable: '一组可复核的 Base64 编码结果与解码原文。',
      clueUse: '证明入侵早期通信没有真正加密，只是为了躲过肉眼巡检。 '
    },
    level2: {
      objective: '确认日志中的十六进制串属于摘要而不是可还原编码。',
      action: '对同一原文生成 MD5 与 SHA256，并判断可逆性。',
      deliverable: '同源摘要指纹与“不可逆”结论。',
      clueUse: '为后续签名伪造链路建立“摘要只验完整性”的认知基线。'
    },
    level3: {
      objective: '验证攻击者与服务器是否共享同一把 AES 密钥。',
      action: '分别完成一次本地加密与一次固定密文解密。',
      deliverable: '可被同一密钥双向处理的 AES 结果。',
      clueUse: '确认后续证据里可以直接本地复现对称加密流程。'
    },
    level4: {
      objective: '还原请求签名规则，判断合法请求是如何被伪造的。',
      action: '追踪参数拼接顺序，再用 MD5 生成 sign。',
      deliverable: '可复现的 sign 值与拼接结论。',
      clueUse: '为后续逆向题中的签名与 token 伪装提供验证标准。'
    },
    level5: {
      objective: '从变量重命名里定位真实密码字符串。',
      action: '忽略命名噪声，直接跟踪最终返回值来源。',
      deliverable: '隐藏在伪命名脚本里的密码原文。',
      clueUse: '确认攻击者只是隐藏可读性，还没有改变数据流。'
    },
    level6: {
      objective: '识别 IIFE 只是包装层，拿到真正入口结果。',
      action: '从自执行函数的返回值逆推核心逻辑。',
      deliverable: '被 IIFE 包裹的入口计算结果。',
      clueUse: '证明攻击脚本已经开始用作用域包装掩护关键入口。'
    },
    level7: {
      objective: '还原重命名后的签名算法与参数顺序。',
      action: '先确认拼接顺序，再提交最终 sign。',
      deliverable: '可验证的签名结果。',
      clueUse: '说明攻击者掌握了合法调用的签名伪造方式。'
    },
    level8: {
      objective: '拆开权限字段上的 Base64 伪装。',
      action: '快速验证是否只是编码，并还原真实权限字段。',
      deliverable: '解码后的权限参数名。',
      clueUse: '确认部分“加密参数”其实只是在拖慢人工阅读。'
    },
    level9: {
      objective: '在自动变量混淆中锁定最终 token 生成逻辑。',
      action: '从最终返回值回溯 3 个关键变量的真实意义。',
      deliverable: '拼接完成后的核心 token。',
      clueUse: '说明攻击者已经进入系统化变量混淆阶段。'
    },
    level10: {
      objective: '拆开 Base64 字符串表并恢复真实访问顺序。',
      action: '先批量解码，再按照索引调用恢复业务文本。',
      deliverable: '字符串数组中真正参与业务的目标 token。',
      clueUse: '证明关键文本已被统一收进字符串表管理。'
    },
    level11: {
      objective: '定位 RC4 包装中的密钥与种子值。',
      action: '不重写解码器，只确认 key 与最终 seed。',
      deliverable: '被字符串保护层藏起的签名种子。',
      clueUse: '确认字符串保护已经升级为带密钥的解码流程。'
    },
    level12: {
      objective: '恢复被 rotate/shuffle 打乱的字符串顺序。',
      action: '拆分“数组内容”和“索引访问”两层混淆。',
      deliverable: '恢复正确顺序后的最终拼接结果。',
      clueUse: '说明攻击者开始同时扰乱内容与访问路径。'
    },
    level13: {
      objective: '在控制流扁平化中找回真实执行顺序。',
      action: '先记录 case 跳转路径，再复原业务拼接。',
      deliverable: '扁平控制流背后的最终 sign。',
      clueUse: '确定复杂分支仍然服务于一条固定验证链。'
    },
    level14: {
      objective: '从大量死代码里筛出唯一真实入口。',
      action: '只追会执行的路径，舍弃噪声分支。',
      deliverable: '真实入口函数的产出值。',
      clueUse: '证明视觉噪声远多于真实业务逻辑。'
    },
    level15: {
      objective: '让动态代码显形并提取真正运行结果。',
      action: '先解开 eval(atob(...))，再分析还原后的源码。',
      deliverable: '动态执行后得到的访问 token。',
      clueUse: '说明关键逻辑已经迁移到运行时展开。'
    },
    level16: {
      objective: '顺着多层调用链回到最初的加密入口。',
      action: '从最终输出逆推每一层返回关系。',
      deliverable: '完整调用链上的最终固定结果。',
      clueUse: '帮助确认攻击者常用的封装套路与入口位置。'
    },
    level17: {
      objective: '拆开叠加混淆后的主控脚本并确认调度结果。',
      action: '继续坚持“先结果、后路径、再语义”的分析顺序。',
      deliverable: '主控脚本最终产出的核心结果。',
      clueUse: '主控服务器与调度 token 已经进入可归档状态。'
    },
    level18: {
      objective: '读懂简化 VM 指令，完成最终结案口令还原。',
      action: '先理解每条 opcode 的含义，再观察栈如何拼接字符串。',
      deliverable: 'VM 解释完成后的最终结案口令。',
      clueUse: '所有线索将被拼回完整攻击链，并进入结案归档。'
    }
  };

  function completedRange(state, start, end) {
    for (var i = start; i <= end; i += 1) {
      if (!state.completedLevels['level' + i]) {
        return false;
      }
    }
    return true;
  }

  function hasStreak(state, size) {
    var streak = 0;
    for (var i = 1; i <= 18; i += 1) {
      if (state.starsByLevel['level' + i] === 3) {
        streak += 1;
        if (streak >= size) {
          return true;
        }
      } else {
        streak = 0;
      }
    }
    return false;
  }

  global.JS_REVERSE_LEVELS = LEVELS;
  global.JS_REVERSE_ACHIEVEMENTS = ACHIEVEMENTS;
  global.JS_REVERSE_BADGES = BADGES;
  global.JS_REVERSE_TIMELINE = TIMELINE;
  global.JS_REVERSE_STAGE_ARCS = STAGE_ARCS;
  global.JS_REVERSE_PRESENTATION = PRESENTATION;
})(window);
