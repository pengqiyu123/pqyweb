import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    enrich = {
        1201: {
            "pinyin": "bù zhī bù jué",
            "meaning": "在没有察觉的情况下就发生或完成了，形容过程自然、不易发觉。",
            "example": "时间在聊天中不知不觉就过去了。"
        },
        1202: {
            "pinyin": "bù zhī dīng dǒng",
            "meaning": "一点儿也不知道，多形容对情况毫不知情。",
            "example": "这件事他压根儿不知丁董。"
        },
        1203: {
            "pinyin": "bù zhī duān ní",
            "meaning": "不知道事情的起因和底细。",
            "example": "真相未明之前，大家都不知端倪。"
        },
        1204: {
            "pinyin": "bù zhī fán jǐ",
            "meaning": "不知有多少，形容数量很多。",
            "example": "这条街上来往的行人不知凡几。"
        },
        1205: {
            "pinyin": "bù zhī gān kǔ",
            "meaning": "不知道其中的甘甜与辛苦，比喻不懂得其中的艰辛。",
            "example": "外人只看到他的成功，却不知甘苦。"
        },
        1206: {
            "pinyin": "bù zhī gāo dī",
            "meaning": "不知道事情的轻重和自己的分量，多指人自不量力。",
            "example": "他年纪轻轻就想独挑大梁，实在有点不知高低。"
        },
        1207: {
            "pinyin": "bù zhī hǎo dǎi",
            "meaning": "不知道好坏，形容人不识好歹或不领情。",
            "example": "你好心相劝，他却全然不知好歹。"
        },
        1208: {
            "pinyin": "bù zhī jì jí",
            "meaning": "不知道有多少，形容数量极多、无从计算。",
            "example": "他为此事操过的心不知纪极。"
        },
        1209: {
            "pinyin": "bù zhī jìn tuì",
            "meaning": "不知道进退，形容言行不知分寸。",
            "example": "在长辈面前言语轻浮，未免太不知进退。"
        },
        1210: {
            "pinyin": "bù zhī jiù lǐ",
            "meaning": "不知道事情的内情、缘由。",
            "example": "不知就里的人很容易被谣言误导。"
        },
        1211: {
            "pinyin": "bù zhī lì hài",
            "meaning": "不知道事情的利弊得失。",
            "example": "他一时冲动做出决定，全然不知利害。"
        },
        1212: {
            "pinyin": "bù zhī qí xiáng",
            "meaning": "不知道事情的详细情况。",
            "example": "事情的来龙去脉我不知其详，不好妄加评论。"
        },
        1213: {
            "pinyin": "bù zhī qīng zhòng",
            "meaning": "不知道事情的轻重缓急或严重程度。",
            "example": "在紧要关头还闹着玩，实在是不知轻重。"
        },
        1214: {
            "pinyin": "bù zhī qù xiàng",
            "meaning": "不知道人或事物去了哪里。",
            "example": "他突然离开家中，至今不知去向。"
        },
        1215: {
            "pinyin": "bù zhī rén jiān yǒu xiū chǐ shì",
            "meaning": "好像不知道世上还有羞耻这种事，形容人厚颜无耻。",
            "example": "明知自己错了还死不认账，简直是不知人间有羞耻事。"
        },
        1216: {
            "pinyin": "bù zhī ròu wèi",
            "meaning": "尝不到肉的味道，比喻专心于某事而忘记了饮食的滋味。",
            "example": "他沉迷读书，连饭菜如何都不知肉味。"
        },
        1217: {
            "pinyin": "bù zhī shēn qiǎn",
            "meaning": "不知道水有多深，比喻不清楚事情的难易、危险程度。",
            "example": "对这个行业不熟，就贸然投资，未免是不知深浅。"
        },
        1218: {
            "pinyin": "bù zhī shì wù",
            "meaning": "不了解世间事务，形容人涉世未深。",
            "example": "他自小在山中长大，颇有几分不知世务的天真。"
        },
        1219: {
            "pinyin": "bù zhī yǒu hàn, hé lùn wèi jìn",
            "meaning": "连汉朝都不知道，更谈不上魏晋，形容与世隔绝，对外界情况一无所知。",
            "example": "他远离都市，自给自足，几乎到了不知有汉，何论魏晋的地步。"
        },
        1220: {
            "pinyin": "bù zhī sǐ huó",
            "meaning": "不知道是死是活，比喻人愚昧无知，或形容行为冒失鲁莽。",
            "example": "在暴风雨中还跑去海边玩水，真是不知死活。"
        },
        1221: {
            "pinyin": "bù zhī suǒ cuò",
            "meaning": "不知道怎么办才好，形容一时慌乱为难的样子。",
            "example": "突遇事故，他一时不知所措。"
        },
        1222: {
            "pinyin": "bù zhī suǒ yǐ",
            "meaning": "不知道是什么缘故或原因。",
            "example": "气氛突然紧张起来，让人不知所以。"
        },
        1223: {
            "pinyin": "bù zhī suǒ yún",
            "meaning": "不知道说的是什么意思，用来形容话语晦涩难懂。",
            "example": "他讲得东拉西扯，听的人都不知所云。"
        },
        1224: {
            "pinyin": "bù zhī suǒ zhōng",
            "meaning": "不知道事情最后会怎样或下落如何。",
            "example": "他外出多年，音讯全无，生死不明，不知所终。"
        },
        1225: {
            "pinyin": "bù zhí yī gù",
            "meaning": "不值得正眼看一下，形容极为轻视。",
            "example": "这种粗制滥造的作品，实在不值一顾。"
        },
        1226: {
            "pinyin": "bù zhí yī qián",
            "meaning": "不值一文钱，比喻毫无价值。",
            "example": "虚假的承诺不值一钱。"
        },
        1227: {
            "pinyin": "bù zhì bù qiú",
            "meaning": "不嫉妒人，也不贪求更多，形容为人知足、宽厚。",
            "example": "诗中所说“不忮不求”，正是他一生为人的写照。"
        },
        1228: {
            "pinyin": "bù zhì zhī zhèng",
            "meaning": "无法医治的病症，比喻很难挽回的祸患或弊病。",
            "example": "若任其发展，恐怕会演变成不治之症。"
        },
        1229: {
            "pinyin": "bù zhì jìn shì",
            "meaning": "不梳头的进士，比喻人勤于读书或工作而无暇修饰仪容。",
            "example": "他整日埋头攻读，俨然一副不栉进士的模样。"
        },
        1230: {
            "pinyin": "bù zhì bāo biǎn",
            "meaning": "不加以褒奖或贬斥，形容对事物不作明确评价。",
            "example": "他对这篇文章只转述内容，并不置褒贬。"
        },
        1231: {
            "pinyin": "bù zhì kě fǒu",
            "meaning": "既不表示赞成，也不表示反对，形容态度暧昧。",
            "example": "他对这项提议始终不置可否。"
        },
        1232: {
            "pinyin": "bù zhǔ gù cháng",
            "meaning": "不拘守旧有的成规，敢于变革。",
            "example": "这位改革者素来不主故常，勇于尝试新路。"
        },
        1233: {
            "pinyin": "bù zhuó biān jì",
            "meaning": "说话写文章离题太远，没有边际。",
            "example": "他的发言有些不着边际，难以抓住重点。"
        },
        1234: {
            "pinyin": "bù zì liàng lì",
            "meaning": "不衡量自己的能力，做力所不及的事。",
            "example": "不做好准备就贸然上阵，未免有点不自量力。"
        },
        1235: {
            "pinyin": "bù zì yóu, wú níng sǐ",
            "meaning": "如果不能自由生活，宁愿去死，表达对自由的极度珍视。",
            "example": "他一生追求思想和言论的自由，正所谓不自由，毋宁死。"
        },
        1236: {
            "pinyin": "bù zú chǐ shǔ",
            "meaning": "不足以列入齿录，形容价值或地位很低微。",
            "example": "这点小成绩不足齿数，不值一提。"
        },
        1237: {
            "pinyin": "bù zú guà chǐ",
            "meaning": "不足以挂在牙齿上，比喻事情、成就微不足道。",
            "example": "这些小失误不足挂齿。"
        },
        1238: {
            "pinyin": "bù zú jiè yì",
            "meaning": "用不着太在意，形容事情无关紧要。",
            "example": "他偶尔迟到一次，不足介意。"
        },
        1239: {
            "pinyin": "bù zú wéi jù",
            "meaning": "不足以作为根据或证据。",
            "example": "个别现象不足为据，不能代表整体情况。"
        },
        1240: {
            "pinyin": "bù zú wéi píng",
            "meaning": "不足以作为凭借或依据。",
            "example": "传言多半失真，不足为凭。"
        },
        1241: {
            "pinyin": "bù zú wéi qí",
            "meaning": "不足以觉得奇怪，形容事情很平常。",
            "example": "他勤奋好学，取得好成绩并不足为奇。"
        },
        1242: {
            "pinyin": "bù zú wéi wài rén dào",
            "meaning": "不足对外人诉说，多指家务或隐私不便外扬。",
            "example": "这些只是家中小事，不足为外人道。"
        },
        1243: {
            "pinyin": "bù zú wéi xùn",
            "meaning": "不足以作为法则或楷模。",
            "example": "他的做法有失公允，不足为训。"
        },
        1244: {
            "pinyin": "bù zú yǔ móu",
            "meaning": "不足以共同谋划大事，形容能力或见识不够。",
            "example": "此人目光短浅，不足与谋。"
        },
        1245: {
            "pinyin": "bù bó shū sù",
            "meaning": "布帛与豆类粮食，泛指日常衣食，亦指社会经济的基本物资。",
            "example": "治国之道，在于使百姓布帛菽粟有备无患。"
        },
        1246: {
            "pinyin": "bù bèi wǎ qì",
            "meaning": "布做的被子和瓦做的器皿，形容生活俭朴。",
            "example": "他家世代清贫，不过布被瓦器，却十分安然。"
        },
        1247: {
            "pinyin": "bù dài lǐ lǎo yā",
            "meaning": "装在布袋里的老鸦，比喻被人牢牢控制，难以翻身。",
            "example": "被证据抓住把柄后，他只像布袋里老鸦，再难狡辩。"
        },
        1248: {
            "pinyin": "bù fān wú yàng",
            "meaning": "风平浪静，船帆安然无恙，多用以比喻旅途或局势平稳。",
            "example": "一路上风平浪静，可谓布帆无恙。"
        },
        1249: {
            "pinyin": "bù gǔ léi mén",
            "meaning": "拿自己的小鼓到雷鸣的地方敲，比喻在高手面前卖弄本领，自取其辱。",
            "example": "在大家面前炫耀这点小才华，无异于布鼓雷门。"
        },
        1250: {
            "pinyin": "bù yī qián shǒu",
            "meaning": "平民百姓的统称。",
            "example": "他虽然位居高位，却常以布衣黔首自期。"
        },
        1251: {
            "pinyin": "bù yī shū shí",
            "meaning": "平民穿布衣、吃粗菜，形容生活清苦朴素。",
            "example": "他即便身居要职，饮食起居仍如布衣蔬食般简单。"
        },
        1252: {
            "pinyin": "bù yī wéi dài",
            "meaning": "穿布衣、系革带，形容平民打扮，也指不做官的人。",
            "example": "他辞官归里，自甘布衣韦带。"
        },
        1253: {
            "pinyin": "bù yī zhī jiāo",
            "meaning": "平民之间的交情，形容交往真挚朴素。",
            "example": "二人少年相识，情同手足，乃一段布衣之交。"
        },
        1254: {
            "pinyin": "bù bù lián huá",
            "meaning": "每走一步都像踩在莲花上，比喻步履轻盈优雅，也形容仕途、事业顺利。",
            "example": "她舞姿轻盈，如步步莲花。"
        },
        1255: {
            "pinyin": "bù bù wéi yíng",
            "meaning": "每前进一步都要先稳固阵地，比喻行事谨慎，准备周密。",
            "example": "在竞争激烈的市场中，公司只能步步为营。"
        },
        1256: {
            "pinyin": "bù diào yī zhì",
            "meaning": "步伐、行动完全一致，比喻想法和行动协调统一。",
            "example": "大家步调一致，项目进展十分顺利。"
        },
        1257: {
            "pinyin": "bù lǚ pán shān",
            "meaning": "形容走路时脚步不稳、摇摇晃晃的样子。",
            "example": "他年纪大了，走起路来略显步履蹒跚。"
        },
        1258: {
            "pinyin": "bù lǚ wéi jiān",
            "meaning": "形容行走十分艰难。",
            "example": "山路崎岖，众人冒雨前行，步履维艰。"
        },
        1259: {
            "pinyin": "bù rén hòu chén",
            "meaning": "走在人后面的脚印，比喻依循前人的路子，缺乏创新。",
            "example": "若总是步人后尘，终难有所突破。"
        },
        1260: {
            "pinyin": "bù xiàn xíng zhēn",
            "meaning": "沿着线来走针，比喻做事有章可循，循规蹈矩。",
            "example": "办事还得步线行针，不能随意更改流程。"
        },
        1261: {
            "pinyin": "bā chuāng líng lóng",
            "meaning": "原指屋舍开窗众多，光线明亮通透。后多比喻心思灵巧、通达。",
            "example": "这座小楼八窗玲珑，站在屋内即可眺望远山。"
        },
        1262: {
            "pinyin": "bā fāng fēng yǔ",
            "meaning": "来自各个方向的风雨，比喻局势动荡或压力来自四面八方。",
            "example": "在八方风雨之中，他依然稳住了公司。"
        },
        1263: {
            "pinyin": "bā fāng zhī chí",
            "meaning": "来自各方面的支持和拥护。",
            "example": "新政策得到了社会各界八方支持。"
        },
        1264: {
            "pinyin": "bā fāng zhī yuán",
            "meaning": "从各个方向赶来的支援和帮助。",
            "example": "灾情发生后，八方支援迅速汇聚。"
        },
        1265: {
            "pinyin": "bā fǔ xún àn",
            "meaning": "明清时奉旨巡行各地、监察地方官吏的官员。",
            "example": "小说中常写八府巡按下江南，体察民情。"
        },
        1266: {
            "pinyin": "bā hóng tóng guǐ",
            "meaning": "天下统一，车轨一致，比喻国家统一、政令一致。",
            "example": "先贤以八纮同轨为理想，期望天下大同。"
        },
        1267: {
            "pinyin": "bā miàn shǐ fēng",
            "meaning": "比喻办事圆滑，善于应对各方面。",
            "example": "他能说会道，处事八面驶风。"
        },
        1268: {
            "pinyin": "bā miàn shòu dí",
            "meaning": "四面八方都受到敌人的进攻，比喻处境极为艰难。",
            "example": "兵力分散，导致前线八面受敌。"
        },
        1269: {
            "pinyin": "bā nàn sān zāi",
            "meaning": "佛教语，指人生所遭受的种种灾难和不幸，亦泛指灾难众多。",
            "example": "古人常说八难三灾，人世多艰。"
        },
        1270: {
            "pinyin": "bā wàn sì qiān",
            "meaning": "原为佛教用语，指烦恼或法门数目众多，后泛指数量极多。",
            "example": "他在书房里藏书八万四千，读也读不完。"
        },
        1271: {
            "pinyin": "bā xiān guò hǎi",
            "meaning": "八仙各显神通过海，比喻各自拿出本领、独立想办法完成事情。",
            "example": "应对这次考验，只能八仙过海，各显其能。"
        },
        1272: {
            "pinyin": "bā yīn è mì",
            "meaning": "形容音乐和声谐调、音色优美动听。",
            "example": "乐曲悠扬，八音遏密，令人沉醉。"
        },
        1273: {
            "pinyin": "bā zì méi jiàn yī piě",
            "meaning": "连“八”字的第一个笔画都还没写出来，比喻事情刚刚开始或尚未有任何眉目。",
            "example": "项目还在论证阶段，八字没见一撇呢。"
        },
        1274: {
            "pinyin": "bā bā jí jí",
            "meaning": "形容极为焦急、心神不安的样子。",
            "example": "他在门口巴巴急急地等候结果。"
        },
        1275: {
            "pinyin": "bā bā jié jié",
            "meaning": "形容忧惧不安或局促不宁的样子。",
            "example": "听说要抽查，他心里巴巴劫劫。"
        },
        1276: {
            "pinyin": "bā bā jiē jiē",
            "meaning": "形容说话结结巴巴、吞吞吐吐。",
            "example": "他一紧张就说得巴巴结结。"
        },
        1277: {
            "pinyin": "bā gāo zhī ér",
            "meaning": "巴附在高枝上，比喻攀附权贵或巴结有权势的人。",
            "example": "他一心只想巴高枝儿，忽视了自身能力的提升。"
        },
        1278: {
            "pinyin": "bā rén xià lǐ",
            "meaning": "指通俗质朴的民间音乐或文学作品。",
            "example": "这支曲调源自巴人下里，质朴而动人。"
        },
        1279: {
            "pinyin": "bá lèi chāo qún",
            "meaning": "才能、品行从同类中超出一大截。",
            "example": "他在书法上的造诣可谓拔类超群。"
        },
        1280: {
            "pinyin": "bá máo jì shì",
            "meaning": "拔下一根毫毛就能拯救世人，比喻尽微薄之力以济世助人。",
            "example": "若能为公益拔毛济世，他总是义不容辞。"
        },
        1281: {
            "pinyin": "bá máo lián rú",
            "meaning": "比喻事物相互牵连，动一处而带动其余。",
            "example": "这件案子牵涉甚广，拔毛连茹，很难一下说清楚。"
        },
        1282: {
            "pinyin": "bá qún chū cuì",
            "meaning": "才德出众，从同类中脱颖而出。",
            "example": "在众多候选人中，她的表现可谓拔群出萃。"
        },
        1283: {
            "pinyin": "bá shān jǔ dǐng",
            "meaning": "形容力大无比，气势雄壮。",
            "example": "古书常用拔山举鼎来形容猛士的神力。"
        },
        1284: {
            "pinyin": "bá shí shī wǔ",
            "meaning": "十个里失去五个，比喻选拔或做事难以尽善尽美，难免有失。",
            "example": "若不慎重考察人才，往往会拔十失五。"
        },
        1285: {
            "pinyin": "bá shù hàn shān",
            "meaning": "连树都能拔起、山都能撼动，形容力量巨大或声势浩大。",
            "example": "大军压境，声势如拔树撼山。"
        },
        1286: {
            "pinyin": "bá shù sōu gēn",
            "meaning": "连根拔起并搜寻根底，比喻彻底查清根源。",
            "example": "整治腐败必须拔树搜根，斩断利益链。"
        },
        1287: {
            "pinyin": "bǎ jiǔ chí áo",
            "meaning": "手持酒杯与蟹螯，形容秋日对酒食蟹的闲适情景。",
            "example": "金风送爽，好友相聚把酒持螯，谈笑风生。"
        },
        1288: {
            "pinyin": "bǎ xīn zhù huǒ",
            "meaning": "往火里添柴，比喻助长恶势或扩大矛盾。",
            "example": "在争吵时再说刻薄话，只会把薪助火。"
        },
        1289: {
            "pinyin": "bà dào héng xíng",
            "meaning": "依仗权势，蛮横行事，不讲道理。",
            "example": "他仗势欺人，在当地霸道横行。"
        },
        1290: {
            "pinyin": "bái bái zhū zhū",
            "meaning": "形容皮肤白里透红、气色很好。",
            "example": "孩子在山里养得白白朱朱，十分健康。"
        },
        1291: {
            "pinyin": "bái bì sān xiàn",
            "meaning": "比喻一再举荐有德之人，或屡次献上珍贵事物。",
            "example": "这位贤士屡经白璧三献，方才被朝廷重用。"
        },
        1292: {
            "pinyin": "bái cǎo huáng yún",
            "meaning": "形容北方秋天枯草连天、云气苍黄的荒凉景象。",
            "example": "入秋之后，塞外原野白草黄云，景象萧瑟。"
        },
        1293: {
            "pinyin": "bái chǐ qīng méi",
            "meaning": "形容青年容貌清秀俊美。",
            "example": "那少年白齿青眉，气度不凡。"
        },
        1294: {
            "pinyin": "cāi méi xíng lìng",
            "meaning": "酒席间猜拳行令的游戏，多用以助兴。",
            "example": "古人宴饮时常以猜枚行令取乐。"
        },
        1295: {
            "pinyin": "cái dé jiān bèi",
            "meaning": "既有才能又有品德。",
            "example": "他为人正直、能力出众，可谓才德兼备。"
        },
        1296: {
            "pinyin": "cái duǎn sī sè",
            "meaning": "才学浅、思路不流畅。",
            "example": "文章写得才短思涩，颇显生疏。"
        },
        1297: {
            "pinyin": "cái gāo bā dǒu",
            "meaning": "形容才华极高。",
            "example": "人们都说他才高八斗，却性情恬淡。"
        },
        1298: {
            "pinyin": "cái gāo shí yuǎn",
            "meaning": "才华出众、见识深远。",
            "example": "只有才高识远的人，才能把握时代机遇。"
        },
        1299: {
            "pinyin": "cái gāo xíng hòu",
            "meaning": "才华出众而品行淳厚。",
            "example": "长者称赞他才高行厚，可托大任。"
        },
        1300: {
            "pinyin": "cái gāo xíng jié",
            "meaning": "才华出众而操行高洁。",
            "example": "诗人一生清廉自守，堪称才高行洁。"
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

    print(f"已为 1201–1300 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
