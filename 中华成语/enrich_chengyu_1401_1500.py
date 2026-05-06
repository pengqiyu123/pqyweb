import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    enrich = {
        1401: {
            "pinyin": "cǎo tì qín xiǎn",
            "meaning": "薙：割除；禽、狝：打猎所得的禽兽。指除草打猎，清除祸患，肃清残余。",
            "example": "官军一路草薙禽狝，终于平定叛乱。"
        },
        1402: {
            "pinyin": "cǎo tóu tiān zǐ",
            "meaning": "比喻拥兵自立、盘踞一方的割据势力首领。",
            "example": "群雄并起之时，各地草头天子层出不穷。"
        },
        1403: {
            "pinyin": "cǎo xíng lù sù",
            "meaning": "在草地行走，在露天住宿，形容旅途劳顿、行程艰辛。",
            "example": "他们为搜集资料，长年草行露宿于边塞。"
        },
        1404: {
            "pinyin": "cǎo zhǎng yīng fēi",
            "meaning": "草长得茂盛，黄莺飞来飞去，形容暮春时节生机盎然的景象。",
            "example": "每到草长莺飞的季节，郊外到处是一片新绿。"
        },
        1405: {
            "pinyin": "cè shēn qí jiān",
            "meaning": "把自己置身在其中，多指参与某种活动或事务。",
            "example": "他不愿置身事外，而是主动厕身其间，出谋划策。"
        },
        1406: {
            "pinyin": "cè zú qí jiān",
            "meaning": "把脚踏入其中，比喻参与到某种活动或是非当中。",
            "example": "这种黑心买卖，他绝不肯厕足其间。"
        },
        1407: {
            "pinyin": "cè mù ér shì",
            "meaning": "斜着眼睛看人，表示厌恶、憎恨或惊惧。",
            "example": "他的卑劣行径，引得众人侧目而视。"
        },
        1408: {
            "pinyin": "cè zú ér lì",
            "meaning": "侧着脚站立，形容恭敬拘谨或站立不安。",
            "example": "在长辈面前，他总是侧足而立，不敢随意。"
        },
        1409: {
            "pinyin": "cè yǐn zhī xīn",
            "meaning": "对别人的不幸产生同情和怜悯之心。",
            "example": "见到灾民的境况，无不激起他的恻隐之心。"
        },
        1410: {
            "pinyin": "cēn cī bù qí",
            "meaning": "高低不齐、长短不一，比喻参差杂乱、不够整齐统一。",
            "example": "街道两旁的房屋参差不齐，颇具老城风貌。"
        },
        1411: {
            "pinyin": "cēn cī cuò luò",
            "meaning": "高低错落、参差不齐，多用来形容建筑、山石、树木等排列不一却富有层次美。",
            "example": "山城屋舍参差错落，极具特色。"
        },
        1412: {
            "pinyin": "céng jǐ hé shí",
            "meaning": "表示时间过去没有多久，曾几何时即可意为“没过多少时候”。",
            "example": "曾几何时，这里还是一片荒地。"
        },
        1413: {
            "pinyin": "céng jīng cāng hǎi",
            "meaning": "出自“曾经沧海难为水”，比喻见过、经历过大世面之后，平常事物便难以入眼。",
            "example": "他游历世界名校，再看一般校园，已是曾经沧海。"
        },
        1414: {
            "pinyin": "céng chū bù qióng",
            "meaning": "一层接一层地出现，没有穷尽，形容接连不断地发生。",
            "example": "各种新技术层出不穷。"
        },
        1415: {
            "pinyin": "céng jiàn dié chū",
            "meaning": "一层一层地呈现出来，形容事物不断涌现。",
            "example": "近年网络新词层见叠出。"
        },
        1416: {
            "pinyin": "céng luán dié zhàng",
            "meaning": "重重山峦像屏障一样层层叠起，形容山势连绵起伏、雄伟壮丽。",
            "example": "远处群山层峦叠嶂，景色壮观。"
        },
        1417: {
            "pinyin": "chā qiáng rén yì",
            "meaning": "大体上还能使人满意，虽不十分理想但还过得去。",
            "example": "这次考试成绩虽不出色，也算差强人意。"
        },
        1418: {
            "pinyin": "chā sān cuò sì",
            "meaning": "错误百出、杂乱无章，形容次序、数字等十分混乱。",
            "example": "他报的那些数据差三错四，难以采信。"
        },
        1419: {
            "pinyin": "chā yǐ háo lí, shī zhī qiān lǐ",
            "meaning": "开始时只差一点点，结果却相差极远，形容小小的差错会导致重大的失误。",
            "example": "设计参数若有偏差，便会差以毫厘，失之千里。"
        },
        1420: {
            "pinyin": "chā zhī háo lí, miù yǐ qiān lǐ",
            "meaning": "同“差以毫厘，失之千里”，强调微小的误差会造成极大的错误。",
            "example": "做学问必须严谨，稍有疏忽就会差之毫厘，谬以千里。"
        },
        1421: {
            "pinyin": "chā chì nán fēi",
            "meaning": "就算插上翅膀也难以飞走，形容被围困得非常严密，难以逃脱。",
            "example": "四面设伏，叫他插翅难飞。"
        },
        1422: {
            "pinyin": "chā chì nán táo",
            "meaning": "插上翅膀也难逃脱，比喻被包围得严密，无法逃走。",
            "example": "证据确凿，他已是插翅难逃。"
        },
        1423: {
            "pinyin": "chā kē dǎ hùn",
            "meaning": "戏曲中演员插入科白、打趣逗乐，后指说笑话、讲俏皮话来调节气氛。",
            "example": "他善于插科打诨，能很快活跃气氛。"
        },
        1424: {
            "pinyin": "chā quān nòng tào",
            "meaning": "原指给牲畜上圈套，后比喻用各种手段设法控制或陷害他人。",
            "example": "别在合同里插圈弄套，耍这些小聪明早晚要出事。"
        },
        1425: {
            "pinyin": "chá wú shí jù",
            "meaning": "检查查问后发现没有可以作为根据的事实。",
            "example": "这只是传言，查无实据。"
        },
        1426: {
            "pinyin": "chá yú fàn hòu",
            "meaning": "喝茶吃饭后的空闲时间，多指人们饭后闲谈的场合。",
            "example": "这种话题最适合在茶余饭后慢慢聊。"
        },
        1427: {
            "pinyin": "chá yú jiǔ hòu",
            "meaning": "喝茶饮酒之后的闲暇时光。",
            "example": "大家茶余酒后，说说往事也挺惬意。"
        },
        1428: {
            "pinyin": "chá zhī mǒ fěn",
            "meaning": "涂脂抹粉，形容过分打扮、浓妆艳抹。",
            "example": "她并不爱搽脂抹粉，自然之美更动人。"
        },
        1429: {
            "pinyin": "chá chá wéi míng",
            "meaning": "过分吹毛求疵地追求明察，往往因此忽略大体。",
            "example": "做领导若一味察察为明，难免使人无所适从。"
        },
        1430: {
            "pinyin": "chá jǐ zhī rén",
            "meaning": "先审察自己，再了解别人，强调反省自我才能真正懂人。",
            "example": "古人主张察己知人，以免妄下评断。"
        },
        1431: {
            "pinyin": "chá jiàn yuān yú",
            "meaning": "在深潭中都能看见鱼，比喻观察过于苛细，连别人隐秘之事也要看透。",
            "example": "用人若处处察见渊鱼，反而难得人心。"
        },
        1432: {
            "pinyin": "chá jīn zhī gǔ",
            "meaning": "考察现在就能推知从前，指以今证古、由今推古。",
            "example": "历史研究常需察今知古，联系现实加以理解。"
        },
        1433: {
            "pinyin": "chá yán guān sè",
            "meaning": "从别人的言语和脸色来揣摩心意。",
            "example": "他在职场摸爬滚打多年，最会察言观色。"
        },
        1434: {
            "pinyin": "chà zǐ yān hóng",
            "meaning": "形容花朵色彩艳丽繁多。",
            "example": "园中春花姹紫嫣红，美不胜收。"
        },
        1435: {
            "pinyin": "chāi bái dào zì",
            "meaning": "逐字逐句拆开讲解，多指把艰深的文字用浅显的话解释出来。",
            "example": "老师耐心地为学生拆白道字。"
        },
        1436: {
            "pinyin": "chāi dōng bǔ xī",
            "meaning": "拆下东边去补西边，比喻这里挪用、那里填补，勉强维持局面。",
            "example": "资金紧张，只好拆东补西周转。"
        },
        1437: {
            "pinyin": "chāi héng bìn luàn",
            "meaning": "发髻散乱、钗饰横斜，形容妇女头发散乱的样子。",
            "example": "她一路奔走，早已钗横鬓乱。"
        },
        1438: {
            "pinyin": "chāi jīng qún bù",
            "meaning": "头戴荆钗、身着粗布裙，形容妇女装束朴素，家境清贫。",
            "example": "她自幼钗荆裙布，却勤劳持家。"
        },
        1439: {
            "pinyin": "chái huǐ gǔ lì",
            "meaning": "因极度悲痛而瘦得只剩骨头，形容极度哀伤、憔悴。",
            "example": "他为亡母守孝，几乎柴毁骨立。"
        },
        1440: {
            "pinyin": "chái mǐ fū qī",
            "meaning": "为柴米油盐奔忙的夫妻，形容平凡百姓的夫妻生活。",
            "example": "他们不过一对柴米夫妻，却相濡以沫数十年。"
        },
        1441: {
            "pinyin": "chái láng chéng xìng",
            "meaning": "凶恶残忍像豺狼一样已经成了本性，形容人极端凶残。",
            "example": "这伙匪徒豺狼成性，作恶多端。"
        },
        1442: {
            "pinyin": "chái láng dāng dào",
            "meaning": "比喻坏人当权执政，正直之人难以立身。",
            "example": "在豺狼当道的年代，好人备受欺凌。"
        },
        1443: {
            "pinyin": "chái láng zhī wěn",
            "meaning": "豺狼的咬噬，比喻残酷的迫害或打击。",
            "example": "一旦落入他们手中，便要饱受豺狼之吻。"
        },
        1444: {
            "pinyin": "chán xián yù dī",
            "meaning": "馋得口水都要滴下来，形容非常馋嘴或对事物极其渴望。",
            "example": "一闻到烤鸭的香味，他就馋涎欲滴。"
        },
        1445: {
            "pinyin": "chán mián fěi cè",
            "meaning": "感情缠绵、言辞哀怨动人。",
            "example": "这首词情意深挚，句句缠绵悱恻。"
        },
        1446: {
            "pinyin": "chán bù zhī xuě",
            "meaning": "夏蝉一生不见冬雪，比喻见识短浅或只知眼前、不识大局。",
            "example": "若只在小圈子里打转，难免蝉不知雪。"
        },
        1447: {
            "pinyin": "chán fù guī cháng",
            "meaning": "古人认为蝉只饮朝露、龟只饮清水，比喻长期处于饥饿困乏之中。",
            "example": "他穷得蝉腹龟肠，却仍不肯屈节求荣。"
        },
        1448: {
            "pinyin": "chán yì wéi zhòng, qiān jūn wéi qīng",
            "meaning": "本义是蝉翼极轻而却被看得很重，千钧极重反被看轻，比喻颠倒轻重、是非不明。",
            "example": "若对小节斤斤计较，却对大事漫不经心，便是蝉翼为重，千钧为轻了。"
        },
        1449: {
            "pinyin": "chán gōng zhé guì",
            "meaning": "蟾宫指月宫，折得月中桂树上的桂枝，比喻科举高中或考试夺魁。",
            "example": "他金榜题名，算是蟾宫折桂了。"
        },
        1450: {
            "pinyin": "chǎn shàng qī xià",
            "meaning": "对上谄媚逢迎，对下欺压凌辱。",
            "example": "这种谄上欺下的作风，最令人不齿。"
        },
        1451: {
            "pinyin": "chǎn jì xiāo shēng",
            "meaning": "把行迹铲除干净、声音消失无踪，比喻隐居不出或从公开场合中消失。",
            "example": "案子平反后，他便铲迹销声，淡出公众视野。"
        },
        1452: {
            "pinyin": "chǎn rán ér xiào",
            "meaning": "形容人嘴角大张、笑容灿烂的样子。",
            "example": "听到孩子考上大学的消息，她冁然而笑。"
        },
        1453: {
            "pinyin": "chāng jué yī shí",
            "meaning": "一时非常猖獗、嚣张。",
            "example": "这些不良风气曾猖獗一时。"
        },
        1454: {
            "pinyin": "chàng tiáo yě yè",
            "meaning": "原指树木枝叶茂盛摇曳，后多用来形容女子姿态轻盈、妩媚。",
            "example": "她步履轻盈，如倡条冶叶般袅袅婷婷。"
        },
        1455: {
            "pinyin": "cháng ān dào shàng",
            "meaning": "长安大道上，比喻京城街道上车马喧阗、人来人往的繁华景象。",
            "example": "昔日长安道上，商贾云集，热闹非凡。"
        },
        1456: {
            "pinyin": "cháng ān jū dà bù yì",
            "meaning": "在长安居住实在不容易，比喻在大城市谋生或在权力中心立足非常艰难。",
            "example": "他常感叹长安居大不易，却仍咬牙坚持。"
        },
        1457: {
            "pinyin": "cháng ān qí jú",
            "meaning": "长安的棋局，比喻政局或形势复杂多变，如同棋盘上的博弈。",
            "example": "当时朝堂如长安棋局，形势瞬息万变。"
        },
        1458: {
            "pinyin": "cháng cǐ yǐ wǎng",
            "meaning": "如果一直这样下去，形容某种状态若持续发展下去会产生的后果。",
            "example": "长此以往，恐怕习气难改。"
        },
        1459: {
            "pinyin": "cháng fēng pò làng",
            "meaning": "乘着长风破浪前进，比喻怀抱理想，勇往直前，奋力实现抱负。",
            "example": "他立志将来长风破浪，一展宏图。"
        },
        1460: {
            "pinyin": "cháng gē dāng kū",
            "meaning": "以长歌来代替哭泣，用悲歌抒发内心的痛苦和愤懑。",
            "example": "诗人长歌当哭，以笔为剑，寄托家国之忧。"
        },
        1461: {
            "pinyin": "cháng jiāng tiān qiàn",
            "meaning": "指长江像天险一样难以逾越，比喻天然的屏障或难以攻克的防线。",
            "example": "长江天堑，使两军一时难以对峙决战。"
        },
        1462: {
            "pinyin": "cháng jǐng niǎo huì",
            "meaning": "喙：鸟嘴。长脖子、尖嘴巴，比喻相貌阴险刻薄或为人狠毒。",
            "example": "史书中说越王长颈鸟喙，可与共患难，不可与共安乐。"
        },
        1463: {
            "pinyin": "cháng lè wèi yāng",
            "meaning": "长久快乐，永远没有终结，常用作对美好前景或太平盛世的祝愿。",
            "example": "人们都希望国家长乐未央。"
        },
        1464: {
            "pinyin": "cháng lín fēng cǎo",
            "meaning": "树木高大、草木丰盛，形容自然景色繁茂。",
            "example": "山谷之中长林丰草，景色宜人。"
        },
        1465: {
            "pinyin": "cháng lǜ gù hòu",
            "meaning": "深谋远虑，周到地考虑以后可能发生的情况。",
            "example": "治国之道，当长虑顾后，不能只图眼前之利。"
        },
        1466: {
            "pinyin": "cháng mián bù qǐ",
            "meaning": "长久地睡下去再也不醒，指死亡的委婉说法。",
            "example": "老人安然长眠不起，走得十分安详。"
        },
        1467: {
            "pinyin": "cháng mìng bǎi suì",
            "meaning": "祝人能活到一百岁，常用作祝寿吉辞。",
            "example": "晚辈齐声祝他长命百岁。"
        },
        1468: {
            "pinyin": "cháng mìng fù guì",
            "meaning": "既长寿又富贵，形容理想的人生境遇。",
            "example": "古人多以长命富贵为人生四福之一。"
        },
        1469: {
            "pinyin": "cháng mù fēi ěr",
            "meaning": "目光所及、耳朵所闻都非常广远，形容见闻广博、消息灵通。",
            "example": "他在朝中长目飞耳，对政局变化了如指掌。"
        },
        1470: {
            "pinyin": "cháng nián lěi yuè",
            "meaning": "年复一年、月复一月，形容时间长久。",
            "example": "他在这条战线上长年累月地坚守。"
        },
        1471: {
            "pinyin": "cháng pèi yuǎn yù",
            "meaning": "拉着长长的缰绳驾驭远行，形容统御全局、驾驭局势的能力。",
            "example": "治国之道，在于长辔远驭，而非一味急进。"
        },
        1472: {
            "pinyin": "cháng piān dà lùn",
            "meaning": "篇幅很长的文章或言论，多含“冗长、啰嗦”之意。",
            "example": "他一说起专业问题，便长篇大论。"
        },
        1473: {
            "pinyin": "cháng piān lěi dú",
            "meaning": "文章篇幅很多、篇章连篇累牍，形容文字繁多。",
            "example": "报告不必长篇累牍，要言不烦更好。"
        },
        1474: {
            "pinyin": "cháng qū zhí rù",
            "meaning": "乘胜一路向前，直接攻入敌方腹地。",
            "example": "大军长驱直入，直抵敌城下。"
        },
        1475: {
            "pinyin": "cháng shé zhī fù",
            "meaning": "爱说长道短、多嘴多舌的妇人，含贬义。",
            "example": "乡里人都怕与长舌之妇结怨。"
        },
        1476: {
            "pinyin": "cháng shēng bù lǎo",
            "meaning": "永远活着而不衰老，多用作对健康长寿的祝愿或神话传说中的境界。",
            "example": "自古以来，长生不老只是人们的美好想象。"
        },
        1477: {
            "pinyin": "cháng shēng bù sǐ",
            "meaning": "永远不死，常指神仙境界或不朽的生命。",
            "example": "神话中诸神长生不死，超脱生死轮回。"
        },
        1478: {
            "pinyin": "cháng shēng jiǔ shì",
            "meaning": "长久地生存、久久地被看见，后来多用作祝寿之词。",
            "example": "祝二老长生久视，福寿绵长。"
        },
        1479: {
            "pinyin": "cháng shéng xì rì",
            "meaning": "用长绳子把太阳拴住，比喻想挽留光阴或延长好时光。",
            "example": "少壮不努力，哪有人能长绳系日？"
        },
        1480: {
            "pinyin": "cháng tíng duǎn tíng",
            "meaning": "一座又一座驿亭，形容旅途中的多次停留与离别。",
            "example": "古人送别，多在长亭短亭把酒话离情。"
        },
        1481: {
            "pinyin": "cháng tú bá shè",
            "meaning": "道路遥远而行走艰难，形容旅途劳苦。",
            "example": "为了考察民情，他长途跋涉走遍山乡。"
        },
        1482: {
            "pinyin": "cháng xiù shàn wǔ",
            "meaning": "长袖子便于舞动，比喻条件有利，更善于施展才能；也用来形容手腕灵活、善于应对局势。",
            "example": "他人脉广、手腕活，真可谓长袖善舞。"
        },
        1483: {
            "pinyin": "cháng xū duǎn tàn",
            "meaning": "时而长叹、时而短叹，形容感慨烦闷。",
            "example": "他近来长吁短叹，看来心事重重。"
        },
        1484: {
            "pinyin": "cháng yè nán míng",
            "meaning": "漫漫长夜难以明亮，比喻黑暗的时期难以结束。",
            "example": "在战乱年代，百姓总觉得长夜难明。"
        },
        1485: {
            "pinyin": "cháng yè zhī yǐn",
            "meaning": "通宵达旦的饮酒欢聚。",
            "example": "昔日好友把酒言欢，长夜之饮，不觉天明。"
        },
        1486: {
            "pinyin": "cháng yī bù bài",
            "meaning": "只作长揖而不下拜，形容自尊自重或对礼节有所简略。",
            "example": "二人相交以礼，长揖不拜，更显平等之意。"
        },
        1487: {
            "pinyin": "cháng zhāi lǐ fó",
            "meaning": "长久持斋、虔诚礼佛，形容笃信佛教。",
            "example": "他晚年长斋礼佛，远避尘嚣。"
        },
        1488: {
            "pinyin": "cháng zhāi xiù fó",
            "meaning": "一面持斋，一面绣制佛像，比喻心无旁骛、专心修行。",
            "example": "寺中老尼长斋绣佛，日子过得极为清苦。"
        },
        1489: {
            "pinyin": "cháng zhěn dà bèi",
            "meaning": "长枕大被，比喻夫妻同床共寝，亦借指婚姻生活。",
            "example": "他盼着早日与佳人长枕大被，共度余生。"
        },
        1490: {
            "pinyin": "cháng zhì jiǔ ān",
            "meaning": "长期治理得好，天下安定太平。",
            "example": "政治清明，方能长治久安。"
        },
        1491: {
            "pinyin": "cháng féi nǎo mǎn",
            "meaning": "肠子肥大、脑袋丰满，形容人肥头大耳、养尊处优而无所用心。",
            "example": "他整日无所事事，活成了肠肥脑满的酒囊饭袋。"
        },
        1492: {
            "pinyin": "cháng hóng huà bì",
            "meaning": "典出苌弘被冤杀，其血三年化为碧玉的传说，多用以比喻忠臣含冤而死、冤情终被昭雪。",
            "example": "历史上的许多冤案，终有一日可以苌弘化碧。"
        },
        1493: {
            "pinyin": "cháng dǎn wò xīn",
            "meaning": "同“卧薪尝胆”，睡在柴草上、时时尝胆汁，以此刻苦自励、发奋图强。",
            "example": "他立志东山再起，甘愿尝胆卧薪。"
        },
        1494: {
            "pinyin": "cháng dǐng yī luán",
            "meaning": "鼎里尝一块肉，就能知道整鼎的滋味，比喻根据局部就能推知整体。",
            "example": "只看他一篇文章，便可尝鼎一脔，知其学养不凡。"
        },
        1495: {
            "pinyin": "cháng bèi bù xiè",
            "meaning": "时刻做好准备而毫不松懈，形容警惕性高。",
            "example": "面对突发风险，政府部门必须常备不懈。"
        },
        1496: {
            "pinyin": "cháng lín fán jiè",
            "meaning": "一般的鱼类、贝类，比喻平凡普通的人。",
            "example": "他自谦不过常鳞凡介，却在岗位上默默奉献。"
        },
        1497: {
            "pinyin": "cháng shèng jiāng jūn",
            "meaning": "屡战屡胜、从未打过败仗的将领。",
            "example": "在大家心中，他是久经沙场的常胜将军。"
        },
        1498: {
            "pinyin": "chǎng huǎng mí lí",
            "meaning": "惝恍：失意迷惘；迷离：模糊不清。形容神情恍惚、景象虚幻模糊的样子。",
            "example": "大雨后的山城云雾缭绕，令人有惝恍迷离之感。"
        },
        1499: {
            "pinyin": "chàng ér bù hè",
            "meaning": "倡：发起、领唱；和：附和、响应。形容有人带头却无人响应的冷清局面。",
            "example": "改革之初，他的建议一度倡而不和。"
        },
        1500: {
            "pinyin": "chàng chóu liáng shā",
            "meaning": "把沙子当作粮食来计量，高声唱报数字，比喻制造假象以安定军心或迷惑对手。",
            "example": "为稳住军心，他只得唱筹量沙，伪装粮草充足。"
        },
    }

    updated = 0
    for item in data:
        cid = item.get("id")
        info = enrich.get(cid)
        if info:
            item.update(info)
            updated += 1

    with json_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"已为 1401–1500 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
