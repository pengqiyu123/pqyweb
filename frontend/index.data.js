(function (global) {
  const INDEX_DATA = {
    tools: [
      {
        id: 'music',
        url: 'um-web.legacy.v1.10.8/index.html',
        title: '音乐解码器',
        description: '轻松处理音乐文件格式，卡通面板内置操作提示，适配多平台。',
        target: '_blank'
      },
      {
        id: 'suffix',
        url: 'suffix_converter.html',
        title: '后缀批量转换',
        description: '快速转换文件类型，搭配科技感提示灯，确保批量操作安全。'
      },
      {
        id: 'wallpaper',
        url: 'https://gallery.timeline.ink/latest',
        title: '拾光壁纸库',
        description: '银河质感壁纸一键收藏，背景与本站的星轨风格相呼应。',
        target: '_blank'
      },
      {
        id: 'video_no_watermark',
        url: 'https://www.datatool.vip/',
        title: '无水印视频下载',
        description: '支持抖音 / 快手等平台。',
        target: '_blank'
      },
      {
        id: 'obs',
        url: 'https://obsproject.com/',
        title: 'OBS 录制与直播',
        description: '开源屏幕录制与直播推流软件，适合课堂演示与录屏。',
        target: '_blank'
      },
      {
        id: 'gamepad_viewer',
        url: 'https://ezgame.cc/tools/gamepadviewer.com/#',
        title: '手柄按键可视化',
        description: '在线展示手柄按键输入状态，适合录制教学或直播演示。',
        target: '_blank'
      },
      {
        id: 'xjlz',
        url: 'https://www.xjlz365.com/',
        title: '乡间郎中',
        description: '跳转到乡间郎中站点。',
        target: '_blank'
      },
      {
        id: 'steam',
        url: 'https://store.steampowered.com/',
        title: 'Steam 官网',
        description: '游戏下载与社区，获取最新 PC 游戏资讯。',
        target: '_blank'
      },
      {
        id: 'bilitools',
        url: 'https://github.com/btjawa/BiliTools',
        title: 'BiliTools',
        description: '开源哔哩哔哩工具集合，支持多种辅助操作。',
        target: '_blank'
      },
      {
        id: 'chinese_bqb',
        url: 'https://github.com/zhaoolee/ChineseBQB?tab=readme-ov-file',
        title: '中文表情包仓库',
        description: '丰富的中文表情包资源，直接下载使用。',
        target: '_blank'
      },
      {
        id: 'china_textbook',
        url: 'https://github.com/TapXWorld/ChinaTextbook?tab=readme-ov-file',
        title: '所有年级教材下载',
        description: '收录各年级教材电子版，便于查阅与备课。',
        target: '_blank'
      },
      {
        id: 'extractor_pdf',
        url: 'https://mineru.net/OpenSourceTools/Extractor',
        title: 'ExtractorPDF',
        description: 'PDF 提取工具，便捷获取文档内容。',
        target: '_blank'
      },
      {
        id: 'abra',
        url: 'https://abra.js.org/',
        title: 'Abra.js 文本加密',
        description: '简洁的前端文本加解密工具。',
        target: '_blank'
      },
      {
        id: 'pakeplus',
        url: 'https://pakeplus.pages.dev/zh/',
        title: 'PakePlus 网页打包',
        description: '将网页快速打包为桌面应用的简便工具。',
        target: '_blank'
      },
      {
        id: 'aishort',
        url: 'https://www.aishort.top/en/',
        title: 'aishort',
        description: '精选 AI 提示词库，涵盖写作、编程、教育等多领域，提升对话效率。',
        target: '_blank'
      },
      {
        id: 'image_to_excel',
        url: '表格转Excel.html',
        title: '图片转Excel表格',
        description: '上传图片到AI识别表格，自动生成Excel并支持下载。'
      }
    ],
    funGames: [
      {
        id: 'drum',
        url: '敲木鱼.html',
        title: '敲木鱼',
        description: '节奏敲击放松身心'
      },
      {
        id: 'earth3d',
        url: '3D地球模型.html',
        title: '3D地球模型',
        description: '旋转地球，认识家园'
      },
      {
        id: 'solar',
        url: '太阳系.html',
        title: '太阳系模型',
        description: '浏览行星轨道与距离'
      },
      {
        id: 'g2048',
        url: '2048.html',
        title: '2048',
        description: '经典数字合成小游戏'
      },
      {
        id: 'tetris',
        url: '俄罗斯方块.html',
        title: '俄罗斯方块',
        description: '方块消除，训练思维'
      },
      {
        id: 'minesweeper',
        url: '扫雷.html',
        title: '扫雷',
        description: '经典雷区挑战'
      },
      {
        id: 'klotski',
        url: '华容道.html',
        title: '华容道',
        description: '滑块移动，解锁出口'
      },
      {
        id: 'snake',
        url: '贪吃蛇.html',
        title: '贪吃蛇',
        description: '灵活走位，吃到更多'
      },
      {
        id: 'particles',
        url: 'particles.html',
        title: '粒子幻境',
        description: '手势交互的 3D 粒子体验'
      },
      {
        id: 'sudoku',
        url: '数独.html',
        title: '数独',
        description: '数字逻辑挑战'
      },
      {
        id: 'memory_flip',
        url: '记忆翻牌.html',
        title: '记忆翻牌',
        description: '训练记忆配对'
      },
      {
        id: 'tictactoe',
        url: '井字棋.html',
        title: '井字棋',
        description: '三子连线对决'
      },
      {
        id: 'gomoku',
        url: '五子棋.html',
        title: '五子棋',
        description: '经典对弈练习'
      },
      {
        id: 'breakout',
        url: '弹球消砖.html',
        title: '弹球消砖',
        description: '反弹击碎方块'
      },
      {
        id: 'maze',
        url: '迷宫逃脱.html',
        title: '迷宫逃脱',
        description: '寻找出口，脱离迷宫'
      },
      {
        id: 'piano',
        url: '音乐钢琴键.html',
        title: '音乐钢琴键',
        description: '键盘触控演奏钢琴'
      },
      {
        id: 'wellchess',
        url: '水井棋.html',
        title: '水井棋',
        description: '策略棋类小游戏'
      },
      {
        id: 'pipechess',
        url: 'https://pipe.tslow.cn/game/790838/',
        title: '水井棋(在线)',
        description: '在线对弈小棋类',
        target: '_blank'
      },
      {
        id: 'voidslicer',
        url: '虚空切水果.html',
        title: '虚空切水果',
        description: '挥刀切水果，反应训练'
      }
    ],
    learning: [
      {
        id: 'idiom',
        url: '成语学习.html',
        title: '成语学习',
        description: '卡片翻翻记成语，提升语文积累'
      },
      {
        id: 'quadratic',
        url: '二次方程学习.html',
        title: '二次方程学习',
        description: '配图讲解抛物线与方程解法'
      },
      {
        id: 'fraction_compare',
        url: '分数大小比较.html',
        title: '分数大小比较',
        description: '拖拽操作练习分数大小判断'
      },
      {
        id: 'poem_order',
        url: '古诗排序.html',
        title: '古诗排序',
        description: '拖动句子，按顺序拼出完整古诗'
      },
      {
        id: 'dictionary',
        url: '现代汉语词典/汉语字典.html',
        title: '汉语字典',
        description: '查询汉字释义与用法',
        target: '_blank'
      },
      {
        id: 'radical',
        url: '偏旁部首拼汉字.html',
        title: '偏旁部首拼汉字',
        description: '拼合部首完成汉字练习'
      },
      {
        id: 'projection',
        url: '三视图教学.html',
        title: '三视图教学',
        description: '立体图形与投影的学习'
      },
      {
        id: 'food_chain',
        url: '食物链学习.html',
        title: '食物链学习',
        description: '理解生态系统中的能量传递'
      },
      {
        id: 'fast_skill',
        url: '速算技巧.html',
        title: '速算技巧',
        description: '掌握常用的心算快捷方法'
      },
      {
        id: 'fast_calc',
        url: '速算.html',
        title: '速算练习',
        description: '通过练习巩固速算技巧'
      },
      {
        id: 'linear',
        url: '一次方程学习.html',
        title: '一次方程学习',
        description: '认识一次方程与基础解法'
      },
      {
        id: 'js_reverse',
        url: 'JS Reverse/index.html',
        title: 'JS逆向闯关',
        description: '以侦探破案方式学习加密、混淆与逆向分析'
      }
    ],
    baiduResources: [
      {
        id: 'bd_raster_wallpaper',
        title: '光栅壁纸',
        description: '光栅壁纸网盘资源',
        url: 'https://pan.baidu.com/s/10smcMF36m2XFZ4XFAsYXSw?pwd=9b14',
        category: '设计素材',
        tags: ['壁纸', '光栅']
      },
      {
        id: 'bd_open_autoglm',
        title: 'Open-AutoGLM',
        description: 'Open-AutoGLM 网盘资源',
        url: 'https://pan.baidu.com/s/1PUC-H_30ybZwSzpzrCh16Q?pwd=vwcp',
        category: 'AI 工具',
        tags: ['AI', '开源']
      },
      {
        id: 'bd_printer',
        title: '打印机',
        description: '网盘资源链接，包含打印机相关文件',
        url: 'https://pan.baidu.com/s/1Shun68rVKWgBTv3AgmGBwA?pwd=v1o7',
        category: '办公设备',
        tags: ['打印机', '驱动']
      },
      {
        id: 'bd_open_autoglm_html',
        title: 'Open-AutoGLM-HTML',
        description: 'Open-AutoGLM-HTML 网盘资源',
        url: 'https://pan.baidu.com/s/1yjLtYPGpmbFKEHWOoQVqqw?pwd=7ccc',
        category: 'AI 工具',
        tags: ['AI', 'HTML']
      },
      {
        id: 'bd_forza_horizon5',
        title: '极限竞速：地平线5',
        description: '极限竞速：地平线5 游戏资源',
        url: 'https://pan.baidu.com/s/1L5mZTJbk7rvjhUvjkLMshQ?pwd=d4es',
        category: '游戏',
        tags: ['赛车', '游戏']
      },
      {
        id: 'bd_vscode_claude_codex',
        title: 'VSCode 插件桥接 ClaudeCode 与 Codex',
        description: 'VSCode 插件桥接 claudecode 与 Codex',
        url: 'https://pan.baidu.com/s/1_b76rZygozWIsTvl_X8Iyw?pwd=yfpr',
        category: '开发工具',
        tags: ['VSCode', 'Claude', 'Codex']
      },
      {
        id: 'bd_jianying_10_7',
        title: '剪映邪修导出 10.7.0',
        description: '剪映邪修导出10.7.0 版本',
        url: 'https://pan.baidu.com/s/1rzBMX1oQ9O5hSODgz-wTrg?pwd=5gf3',
        category: '视频工具',
        tags: ['剪映', '视频编辑']
      }
    ],
    ai: [
      {
        id: 'qianwen',
        url: 'https://www.qianwen.com/chat',
        title: '通义千问',
        description: '阿里巴巴大模型助手',
        target: '_blank'
      },
      {
        id: 'doubao',
        url: 'https://www.doubao.com/chat',
        title: '豆包 AI',
        description: '字节跳动智能助手',
        target: '_blank'
      },
      {
        id: 'deepseek',
        url: 'https://chat.deepseek.com/',
        title: 'DeepSeek',
        description: '国产大模型探索站',
        target: '_blank'
      },
      {
        id: 'kimi',
        url: 'https://www.kimi.com/',
        title: 'Kimi',
        description: '长文档理解与创作助手',
        target: '_blank'
      },
      {
        id: 'chatgpt',
        url: 'https://chatgpt.com/',
        title: 'ChatGPT',
        description: '多场景通用型 AI 聊天助手',
        target: '_blank'
      },
      {
        id: 'gemini',
        url: 'https://gemini.google.com/app',
        title: 'Gemini',
        description: 'Google 智能助手',
        target: '_blank'
      }
    ]
  };

  global.INDEX_DATA = INDEX_DATA;
})(window);
