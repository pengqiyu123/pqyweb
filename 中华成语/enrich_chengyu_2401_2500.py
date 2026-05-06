import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    enrich = {
        2401: {
            "pinyin": "dà qiǎo ruò zhuō",
            "meaning": "最高的技巧反而像拙笨，形容真正有本领的人不露锋芒、朴实自然。",
            "example": "他写出来的文字看似平淡，其实大巧若拙，回味无穷。"
        },
        2402: {
            "pinyin": "dà quán dú lǎn",
            "meaning": "把重要权力完全抓在自己一人手里。",
            "example": "若让个人大权独揽而缺乏监督，极易滋生腐败。"
        },
        2403: {
            "pinyin": "dà quán páng luò",
            "meaning": "重要权力旁落到别人手里。",
            "example": "他退休后，公司的人事大权旁落于新经理。"
        },
        2404: {
            "pinyin": "dà quán zài wò",
            "meaning": "重要权力掌握在手中。",
            "example": "一旦大权在握，他立刻着手推进改革。"
        },
        2405: {
            "pinyin": "dà rén hǔ biàn",
            "meaning": "出自《周易》，比喻品德、学问或地位有巨大变化，气象焕然一新。",
            "example": "经过几年历练，他已大人虎变，不可同日而语。"
        },
        2406: {
            "pinyin": "dà rén dà yì",
            "meaning": "极高的仁德和道义，多用来称赞乐于助人、扶危济困的人。",
            "example": "他在危难之际伸手相救，真是大仁大义。"
        },
        2407: {
            "pinyin": "dà shà fēng jǐng",
            "meaning": "极大地破坏兴趣和兴致，使人扫兴。",
            "example": "刚准备出游却下起大雨，真是大煞风景。"
        },
        2408: {
            "pinyin": "dà shà dòng liáng",
            "meaning": "大厦的栋梁，比喻肩负重任的中坚力量。",
            "example": "青年学子是祖国未来的大厦栋梁。"
        },
        2409: {
            "pinyin": "dà shà jiāng qīng",
            "meaning": "大厦就要倒塌，比喻局势极其危急、即将崩溃。",
            "example": "那时的旧政权早已大厦将倾。"
        },
        2410: {
            "pinyin": "dà shēng jí hū",
            "meaning": "提高嗓门，大声急切地呼吁。",
            "example": "他多次为环境保护问题大声疾呼。"
        },
        2411: {
            "pinyin": "dà shī rén wàng",
            "meaning": "严重丧失群众的信任和拥护。",
            "example": "接连不断的丑闻让他在选民中大失人望。"
        },
        2412: {
            "pinyin": "dà shī suǒ wàng",
            "meaning": "结果与期望相差很大，使人非常失望。",
            "example": "新作质量平平，令影迷大失所望。"
        },
        2413: {
            "pinyin": "dà shì bù hú tu",
            "meaning": "在重大原则问题或关键事情上头脑清醒，不含糊。",
            "example": "他平时大大咧咧，关键时刻却大事不糊涂。"
        },
        2414: {
            "pinyin": "dà shì dà fēi",
            "meaning": "重大的的是与非、原则性问题。",
            "example": "在大是大非面前必须立场坚定，不能摇摆。"
        },
        2415: {
            "pinyin": "dà shì pū zhāng",
            "meaning": "在事情上大肆铺张、讲排场，多含贬义。",
            "example": "办婚礼不必大事铺张，简简单单也很好。"
        },
        2416: {
            "pinyin": "dà shì qù yǐ",
            "meaning": "大事已去，比喻大局已定，事情已无法挽回。",
            "example": "敌军攻破城门，他长叹一声：\"大事去矣。\""
        },
        2417: {
            "pinyin": "dà shì suǒ qū",
            "meaning": "大势发展所趋向的方向，指客观形势必然走向。",
            "example": "绿色发展已经是大势所趋。"
        },
        2418: {
            "pinyin": "dà shì yǐ qù",
            "meaning": "形势已不可挽回，接近失败或灭亡。",
            "example": "连番失利之后，人们都感到大势已去。"
        },
        2419: {
            "pinyin": "dà shǒu dà jiǎo",
            "meaning": "花钱或用东西很不节省，浪费严重。",
            "example": "他花钱一向大手大脚，从不记账。"
        },
        2420: {
            "pinyin": "dà shū tè shū",
            "meaning": "着重记述或大加赞扬。",
            "example": "他在科研上的突出贡献值得大书特书。"
        },
        2421: {
            "pinyin": "dà shù jiāng jūn",
            "meaning": "原指东汉名将冯异，后用来称赞不居功自傲的将领或有功之人。",
            "example": "这位老将功勋卓著却从不争功，真可谓大树将军。"
        },
        2422: {
            "pinyin": "dà sì jué cí",
            "meaning": "大肆铺张辞藻，大展文采，也指夸夸其谈、大发议论。",
            "example": "他在会上大肆厥辞，说得天花乱坠。"
        },
        2423: {
            "pinyin": "dà tí xiǎo zuò",
            "meaning": "题目重大而写得轻浅，或对重要题材处理得过于简单。",
            "example": "如此重大的历史题材，却被他写成闲笔，未免大题小作。"
        },
        2424: {
            "pinyin": "dà tiān bái rì",
            "meaning": "光天化日，大白天。多用来强调公开、明显的场合。",
            "example": "大天白日之下竟敢行抢，实在猖狂。"
        },
        2425: {
            "pinyin": "dà tíng guǎng zhòng",
            "meaning": "公开的场合，在众多人面前。",
            "example": "他在大庭广众之下向大家郑重道歉。"
        },
        2426: {
            "pinyin": "dà tóng xiǎo yì",
            "meaning": "大体相同而略有差异。",
            "example": "两家公司的方案大同小异。"
        },
        2427: {
            "pinyin": "dà tóu xiǎo wěi",
            "meaning": "开头铺张、结尾草率，或前多后少、首尾不相称。",
            "example": "这篇文章结构大头小尾，结局收得太匆忙。"
        },
        2428: {
            "pinyin": "dà xǐ guò wàng",
            "meaning": "喜出望外，比原先预料的还要高兴。",
            "example": "听到录取的消息，全家都大喜过望。"
        },
        2429: {
            "pinyin": "dà xián hǔ biàn",
            "meaning": "比喻贤德之人大有进步或显露出卓越的才能。",
            "example": "他出游归来，学识气度大贤虎变。"
        },
        2430: {
            "pinyin": "dà xiǎn shēn shǒu",
            "meaning": "充分显示自己的本领和才能。",
            "example": "这次比赛正是他大显身手的好机会。"
        },
        2431: {
            "pinyin": "dà xiǎn shén tōng",
            "meaning": "充分施展本领，多指本领高超、手段神奇。",
            "example": "高手们在赛场上各自大显神通。"
        },
        2432: {
            "pinyin": "dà xīng tǔ mù",
            "meaning": "大规模地建造或修缮房屋等工程。",
            "example": "为了迎接盛会，城市里到处大兴土木。"
        },
        2433: {
            "pinyin": "dà xiāng jìng tíng",
            "meaning": "比喻相差很远，大不相同。",
            "example": "实际效果与最初的宣传大相径庭。"
        },
        2434: {
            "pinyin": "dà yán bù cán",
            "meaning": "说极大的大话而一点也不感到惭愧。",
            "example": "他总爱大言不惭地吹嘘自己的功劳。"
        },
        2435: {
            "pinyin": "dà yáo dà bǎi",
            "meaning": "迈着夸张的步伐行走，形容神气十足或傲慢得意的样子。",
            "example": "他大摇大摆地走进会场，引来众人侧目。"
        },
        2436: {
            "pinyin": "dà yì lǐn rán",
            "meaning": "坚持正义，气节严正不可侵犯。",
            "example": "面对威胁利诱，他仍大义凛然，毫不退缩。"
        },
        2437: {
            "pinyin": "dà yì miè qīn",
            "meaning": "为了维护大义而不徇私情，严肃处理亲属的错误。",
            "example": "他秉公执法，对亲属也毫不留情，真是大义灭亲。"
        },
        2438: {
            "pinyin": "dà yǒu bì yì",
            "meaning": "有很大的帮助和益处。",
            "example": "多读经典名著，对提高写作水平大有裨益。"
        },
        2439: {
            "pinyin": "dà yǒu jìng tíng",
            "meaning": "形容差别很大，大不相同。",
            "example": "他的说法与事实大有径庭。"
        },
        2440: {
            "pinyin": "dà yǒu kě wéi",
            "meaning": "很有发展前途，大有施展才能的空间。",
            "example": "这个新兴行业前景广阔，年轻人来干大有可为。"
        },
        2441: {
            "pinyin": "dà yǒu kě guān",
            "meaning": "很有看头，很值得注意或重视。",
            "example": "这次作品展内容充实，实在大有可观。"
        },
        2442: {
            "pinyin": "dà yǒu qǐ sè",
            "meaning": "情势有了明显的好转。",
            "example": "经过一段时间治疗，病人的病情大有起色。"
        },
        2443: {
            "pinyin": "dà yǒu rén zài",
            "meaning": "有许多这样的人，说明并非个别。",
            "example": "肯默默奉献的人在社会上大有人在。"
        },
        2444: {
            "pinyin": "dà yǒu zuò wéi",
            "meaning": "很有作为，能够成就大事业。",
            "example": "只要方向正确、方法得当，你一定大有作为。"
        },
        2445: {
            "pinyin": "dà zhǎn jīng lún",
            "meaning": "经纶：治理国家的才能。充分施展政治抱负或治理才能。",
            "example": "他一心从政，希望有朝一日大展经纶。"
        },
        2446: {
            "pinyin": "dà zhāng qí cí",
            "meaning": "说话或写文章时大肆铺陈词藻，多有夸张之意。",
            "example": "新闻报道要实事求是，不能一味大张其词。"
        },
        2447: {
            "pinyin": "dà zhāng qí gǔ",
            "meaning": "张开旗帜，击鼓助威，形容声势浩大、广泛宣传或行动。",
            "example": "他们大张旗鼓地开展了环保宣传活动。"
        },
        2448: {
            "pinyin": "dà zhāng shēng shì",
            "meaning": "到处张扬，以壮声势。",
            "example": "这不过是小事一桩，没必要大张声势。"
        },
        2449: {
            "pinyin": "dà zhāng tà fá",
            "meaning": "大举讨伐或公开声讨、抨击。",
            "example": "媒体对破坏环境的企业大张挞伐。"
        },
        2450: {
            "pinyin": "dà zhàng zé zǒu",
            "meaning": "指儿女受父责打时，小杖可受，大杖则应躲避，以免父母因过度伤人而陷于不义；为旧时宣扬的孝道观念。",
            "example": "古人所谓小杖则受，大杖则走，体现的是一种传统的孝道观。"
        },
        2451: {
            "pinyin": "dà zhèng fāng zhēn",
            "meaning": "国家或单位在重大事务上的根本政策和方向。",
            "example": "企业的发展战略必须服从国家的大政方针。"
        },
        2452: {
            "pinyin": "dà zhì ruò yú",
            "meaning": "真正聪明的人表面上好像愚笨，形容深藏不露。",
            "example": "他处世低调，大智若愚，从不夸耀自己。"
        },
        2453: {
            "pinyin": "dà zhōng zhì zhèng",
            "meaning": "最公正而合乎中道。多用来称颂公允正直的言论或主张。",
            "example": "他的评论持平稳健，可谓大中至正。"
        },
        2454: {
            "pinyin": "dāi lǐ sā jiān",
            "meaning": "外表痴呆，内心奸诈。",
            "example": "你别再装老实人，其实是在呆里撒奸、暗中算计别人。"
        },
        2455: {
            "pinyin": "dāi ruò mù jī",
            "meaning": "呆得像木雕的鸡一样，形容因惊恐、惊讶而发愣的样子。",
            "example": "听到这个噩耗，他一下子呆若木鸡。"
        },
        2456: {
            "pinyin": "dāi tóu dāi nǎo",
            "meaning": "形容人愚笨迟钝或反应慢。",
            "example": "他小时候看上去有点呆头呆脑，其实心思很细。"
        },
        2457: {
            "pinyin": "dài duò yīn xún",
            "meaning": "怠惰：懈怠懒惰；因循：拖延敷衍。形容懒散拖沓、不思进取。",
            "example": "若总是怠惰因循，终究难有作为。"
        },
        2458: {
            "pinyin": "dài wú jié yí",
            "meaning": "殆：几乎；孑遗：剩余。几乎没有一点残存。",
            "example": "虫灾之后，地里的庄稼殆无孑遗。"
        },
        2459: {
            "pinyin": "dài wú xū rì",
            "meaning": "殆：几乎；虚日：空闲的日子。几乎没有一天是空着的，形容经常如此或十分忙碌。",
            "example": "近来会议频繁，他几乎殆无虚日。"
        },
        2460: {
            "pinyin": "dài lì chéng chē",
            "meaning": "比喻不因为贫富、地位的变化而改变贫贱之交。",
            "example": "他对少年时的旧友始终礼敬，可谓戴笠乘车。"
        },
        2461: {
            "pinyin": "dài pén wàng tiān",
            "meaning": "头顶着盆子看天，比喻受遮蔽而看不清全貌，也比喻眼界狭窄。",
            "example": "若只凭片面信息判断，无异于戴盆望天。"
        },
        2462: {
            "pinyin": "dài tiān lǚ dì",
            "meaning": "戴：顶着；履：踩着。头顶着天，脚踩着地，比喻人活在天地之间，也借指恩德深厚如天高地厚。",
            "example": "芸芸众生皆戴天履地，当怀敬畏之心。"
        },
        2463: {
            "pinyin": "dài tóu shí liǎn",
            "meaning": "比喻有面子、有身份，有一定社会地位的人。",
            "example": "他在本地算是颇有声望的戴头识脸人物。"
        },
        2464: {
            "pinyin": "dài yuán lǚ fāng",
            "meaning": "圆借指天，方借指地。头顶圆天，脚踏方地，指活在人世间的普通人。",
            "example": "我们不过是戴圆履方的小人物，却也各有责任。"
        },
        2465: {
            "pinyin": "dài yuè pī xīng",
            "meaning": "顶着月亮，披着星光，形容早出晚归、辛勤奔波。",
            "example": "工人们戴月披星，加紧抢修受损的电网。"
        },
        2466: {
            "pinyin": "dài zuì lì gōng",
            "meaning": "带着罪责立功，用功劳来赎罪。",
            "example": "他主动请缨戴罪立功，立下了不小的战功。"
        },
        2467: {
            "pinyin": "dài chāi dài xíng",
            "meaning": "代为拆阅来文、批示并执行，形容在机关中权力极大。",
            "example": "主要领导长期不在时，大小事务都由他代拆代行。"
        },
        2468: {
            "pinyin": "dài dài xiāng chuán",
            "meaning": "一代一代地传下去，形容延续长久。",
            "example": "这门手艺在村里代代相传，至今已有百年历史。"
        },
        2469: {
            "pinyin": "dài rén shòu guò",
            "meaning": "替别人承担过错或罪责。",
            "example": "为朋友代人受过，往往要付出沉重代价。"
        },
        2470: {
            "pinyin": "dài rén zhuō dāo",
            "meaning": "替别人执笔写文章，多指代人作文或撰写文稿。",
            "example": "这篇檄文其实是他替主帅代人捉刀写成的。"
        },
        2471: {
            "pinyin": "dài jīn pèi zǐ",
            "meaning": "身佩金印紫绶，比喻身居高官显位。",
            "example": "他年轻时便带金佩紫，一度被看好前途无量。"
        },
        2472: {
            "pinyin": "dài lì shān hé",
            "meaning": "带：衣带；砺：磨刀石；山：泰山；河：黄河。黄河细如衣带、泰山小若砺石，比喻时间再久远、世事再变迁也决不改变心志或约定。",
            "example": "二人立下誓言，要带砺山河，永不相负。"
        },
        2473: {
            "pinyin": "dài niú pèi dú",
            "meaning": "原指劝人卖剑买牛、弃武从农，后比喻改业归农或重视农业。",
            "example": "战乱平息后，许多士兵卸甲归田，带牛佩犊。"
        },
        2474: {
            "pinyin": "dài zhe líng dāng qù zuò zéi",
            "meaning": "戴着铃铛去偷东西，比喻做坏事却张扬，必然暴露。",
            "example": "公款外借还留字据，简直是带着铃铛去做贼。"
        },
        2475: {
            "pinyin": "dài jià ér gū",
            "meaning": "等待合适的价钱再出卖，比喻等待时机以求更好的职位或报酬。",
            "example": "他宁愿在家著书立说，也要待价而沽，择良主而仕。"
        },
        2476: {
            "pinyin": "dài lǐ bù lǐ",
            "meaning": "对人态度冷淡，爱答不理。",
            "example": "服务员对顾客总是待理不理，生意怎么会好？"
        },
        2477: {
            "pinyin": "dài rén jiē wù",
            "meaning": "与人相处和应酬事物的方式、态度。",
            "example": "一个人待人接物是否得体，很大程度决定了人际关系。"
        },
        2478: {
            "pinyin": "dài shí ér dòng",
            "meaning": "等待适当的时机再行动。",
            "example": "现在不必急于出手，只需静观其变，待时而动。"
        },
        2479: {
            "pinyin": "dài shí shǒu fèn",
            "meaning": "等待时机，守住本分，不妄自行动或越分。",
            "example": "他深知进退之道，一向待时守分，从不逾矩。"
        },
        2480: {
            "pinyin": "dài zì guī zhōng",
            "meaning": "指少女成年未嫁，还待字于闺房之中。",
            "example": "她自幼饱读诗书，至今仍待字闺中。"
        },
        2481: {
            "pinyin": "dān bīng gū chéng",
            "meaning": "单兵：寡弱无援的军队；孤城：孤立无援的城池。形容军队和城池孤立无依、势单力薄。",
            "example": "在敌军重围之中，他只率单兵孤城苦苦坚守。"
        },
        2482: {
            "pinyin": "dān dāo fù huì",
            "meaning": "一个人或带极少随从赴约会见对方，多用来形容勇敢果决。",
            "example": "他单刀赴会，与对方首领面谈和解。"
        },
        2483: {
            "pinyin": "dān dāo zhí rù",
            "meaning": "像单人持刀直冲一样，比喻说话做事开门见山，直接进入主题。",
            "example": "发言时不必拐弯抹角，可以单刀直入讲重点。"
        },
        2484: {
            "pinyin": "dān hú guǎ fú",
            "meaning": "鹄：天鹅；凫：野鸭。原为琴曲名，后比喻失去配偶的人。",
            "example": "战乱之后，村中单鹄寡凫者不在少数。"
        },
        2485: {
            "pinyin": "dān qiāng pǐ mǎ",
            "meaning": "一支枪、一匹马，比喻单身一人、没有援助。",
            "example": "他凭着单枪匹马闯天下，终于闯出了一番事业。"
        },
        2486: {
            "pinyin": "dān sī bù chéng xiàn",
            "meaning": "一根丝线不能织成一条线，比喻个人力量有限，必须团结协作。",
            "example": "单丝不成线，团队合作才能完成这项大工程。"
        },
        2487: {
            "pinyin": "dān zé yì zhé, zhòng zé nán cuī",
            "meaning": "单独时容易被折断，众人在一起就难以摧毁，比喻团结力量大。",
            "example": "大家明白单则易折，众则难摧的道理后，更加懂得团结的重要。"
        },
        2488: {
            "pinyin": "dān cái jié lì",
            "meaning": "殚：竭尽。用尽财力和气力。",
            "example": "父母为供孩子上学几乎殚财竭力。"
        },
        2489: {
            "pinyin": "dān jiàn qià wén",
            "meaning": "殚：尽；洽：广博。该见的都见过了，该听的都听过了，形容见多识广、知识渊博。",
            "example": "他博览群书，殚见洽闻，对各个领域都有独到见解。"
        },
        2490: {
            "pinyin": "dān jīng bì lì",
            "meaning": "用尽精力和全部力量。",
            "example": "为写好这部专著，他可谓殚精毕力。"
        },
        2491: {
            "pinyin": "dān jīng jié lǜ",
            "meaning": "殚：竭尽；虑：思虑。用尽精力和心思。",
            "example": "为解决贫困问题，基层干部们殚精竭虑。"
        },
        2492: {
            "pinyin": "dān sī jí lǜ",
            "meaning": "殚：竭尽；虑：思虑。形容用尽心思，反复思量谋划。",
            "example": "他为企业转型殚思极虑，几乎夜夜难眠。"
        },
        2493: {
            "pinyin": "dān zhì jié lì",
            "meaning": "殚：竭尽。用尽智慧和力量。",
            "example": "科研团队殚智竭力，终于攻克了关键技术难关。"
        },
        2494: {
            "pinyin": "dān dòu jiàn sè",
            "meaning": "比喻为了一点小利就露出喜色，形容过分计较小利。",
            "example": "若为区区奖金争吵不休，未免箪豆见色。"
        },
        2495: {
            "pinyin": "dān piáo lǚ kōng",
            "meaning": "箪：盛饭的竹器；瓢：舀水的器具。吃的喝的常常没有，形容生活非常贫困。",
            "example": "他虽箪瓢屡空，却依旧乐观向上。"
        },
        2496: {
            "pinyin": "dān shí hú jiāng",
            "meaning": "箪：盛饭竹器；食：食物；浆：汤。百姓用箪盛饭、壶盛汤来欢迎所拥戴的军队，形容军队深受群众欢迎。",
            "example": "义军进村时，百姓箪食壶浆，相迎于道。"
        },
        2497: {
            "pinyin": "dān sì hú jiǔ",
            "meaning": "一箪饭、一壶酒，形容饮食简单或数量不多。",
            "example": "二人对坐松下，不过箪食壶酒，亦自清欢。"
        },
        2498: {
            "pinyin": "dān sì piáo yǐn",
            "meaning": "一箪食物，一瓢饮料，形容读书人安于贫穷的清高生活，后来也泛指清苦的生活。",
            "example": "他宁愿箪食瓢饮，也不肯违背自己的原则。"
        },
        2499: {
            "pinyin": "dān jīng shòu pà",
            "meaning": "经常处在惊惧不安之中。",
            "example": "那段时间他天天担惊受怕，夜里难以入睡。"
        },
        2500: {
            "pinyin": "dān xuě sāi jǐng",
            "meaning": "挑雪去填塞水井，比喻徒劳无功。",
            "example": "不找准问题根源，光在表面做文章，无异于担雪塞井。"
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

    print(f"已为 2401–2500 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
