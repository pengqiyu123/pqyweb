import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    enrich = {
        1501: {
            "pinyin": "chàng duì tái xì",
            "meaning": "原指两个戏班在同一戏院轮流演出，后来多比喻彼此对立、公开与对方竞争或作对。",
            "example": "两家公司在同一条街开店，价格战打得像唱对台戏。"
        },
        1502: {
            "pinyin": "chàng rán ruò shī",
            "meaning": "形容失意惆怅，好像失去了什么似的。",
            "example": "比赛失利后，他独自坐在看台上，怅然若失。"
        },
        1503: {
            "pinyin": "chàng suǒ yù yán",
            "meaning": "痛痛快快地把心里想说的话都说出来。",
            "example": "会上大家畅所欲言，提出了许多中肯的建议。"
        },
        1504: {
            "pinyin": "chàng tōng wú zǔ",
            "meaning": "十分通畅，没有任何阻碍，多形容交通、手续等非常顺利。",
            "example": "高速公路建成后，几座城市之间往来畅通无阻。"
        },
        1505: {
            "pinyin": "chāo chāo xuán zhù",
            "meaning": "超超：高超；玄：微妙；著：明显。形容言论、文辞高妙精深而又明白透彻。",
            "example": "这篇评论立论精当、文字优美，可谓超超玄著。"
        },
        1506: {
            "pinyin": "chāo chén bá sú",
            "meaning": "超出尘世、拔出凡俗，形容人品、气质或艺术风格高雅不俗。",
            "example": "他的画风清逸洒脱，给人以超尘拔俗之感。"
        },
        1507: {
            "pinyin": "chāo dù zhòng shēng",
            "meaning": "佛教用语，为亡者诵经做法事，使其脱离苦海；也泛指劝人向善、解脱烦恼。",
            "example": "寺中法会，为战乱中逝去的百姓超度众生。"
        },
        1508: {
            "pinyin": "chāo fán chū shì",
            "meaning": "超出凡俗、脱离尘世，多形容超然物外的境界或高洁脱俗的气质。",
            "example": "隐者栖居山林，举止间自有一股超凡出世的气息。"
        },
        1509: {
            "pinyin": "chāo fán rù shèng",
            "meaning": "由凡入圣，比喻学问、技艺或修养达到极高的境界。",
            "example": "这位大师书法已臻超凡入圣之境。"
        },
        1510: {
            "pinyin": "chāo qún bá lèi",
            "meaning": "才能远远超过同类和一般人。",
            "example": "他在同龄人中可谓超群拔类，颇受器重。"
        },
        1511: {
            "pinyin": "chāo qún chū zhòng",
            "meaning": "才能、成就大大高出同辈和一般人。",
            "example": "她在科研领域超群出众，屡获大奖。"
        },
        1512: {
            "pinyin": "chāo qún jué lún",
            "meaning": "在同类中超出群伦、没有可以相比的，形容非常杰出。",
            "example": "此画构思精妙、笔法老练，可谓超群绝伦。"
        },
        1513: {
            "pinyin": "chāo rán wù wài",
            "meaning": "超脱于世俗事物之外，不为外物所扰，多形容人淡泊名利、心境高远。",
            "example": "他隐居山林，读书种竹，一副超然物外的神态。"
        },
        1514: {
            "pinyin": "chāo rán xiàng wài",
            "meaning": "超出具象形貌之外，形容诗文或画作意境高远，不拘泥于表面形象。",
            "example": "这幅山水画笔墨简约，却有超然象外之致。"
        },
        1515: {
            "pinyin": "chāo rán zì dé",
            "meaning": "神情超脱而自得其乐，形容内心宁静、悠然自适。",
            "example": "他闲坐窗前品茶观雨，显得超然自得。"
        },
        1516: {
            "pinyin": "chāo rán zì yì",
            "meaning": "举止从容、不为世俗所累，自得其乐的样子。",
            "example": "虽居闹市，他却能超然自逸。"
        },
        1517: {
            "pinyin": "chāo yǐ xiàng wài",
            "meaning": "超越物象之外，形容诗文意境高远超脱。",
            "example": "司空图所谓“超以象外，得其环中”，正是论诗要意境高远。"
        },
        1518: {
            "pinyin": "chāo yì jué chén",
            "meaning": "原形容马奔跑极快，以后也比喻远远超过他人、出类拔萃。",
            "example": "他的成绩在同行中超轶绝尘。"
        },
        1519: {
            "pinyin": "cháo yáng dān fèng",
            "meaning": "本作“丹凤朝阳”，比喻贤才遇到明主或良好的时代。",
            "example": "新政推行之际，众多人才如朝阳丹凤般竞相而来。"
        },
        1520: {
            "pinyin": "cháo lǐ wú rén mò zuò guān",
            "meaning": "旧时俗语，意思是朝廷中没人做靠山，办事就难以成功，比喻做官离不开权势背景。",
            "example": "俗话说朝里无人莫做官，他对此感触甚深。"
        },
        1521: {
            "pinyin": "cháo fēng nòng yuè",
            "meaning": "本指吟咏风月、寄情山水，后多用来形容只顾风花雪月、不问世事的文艺活动。",
            "example": "他早年一味嘲风弄月，后来才开始关心现实人生。"
        },
        1522: {
            "pinyin": "cháo fēng yǒng yuè",
            "meaning": "吟咏风月，形容沉迷于写景抒情而不问世事。",
            "example": "诗人并非只会嘲风咏月，也能为民生鼓与呼。"
        },
        1523: {
            "pinyin": "cháo huǐ luǎn pò",
            "meaning": "巢毁则卵破，比喻整体遭殃，局中人无一幸免，或祸及无辜。",
            "example": "若任由金融体系崩溃，势必巢毁卵破，殃及百姓。"
        },
        1524: {
            "pinyin": "cháo jū xué chǔ",
            "meaning": "住在树巢、穴居土中，形容原始简陋的居住生活。",
            "example": "先民曾经巢居穴处，逐水草而居。"
        },
        1525: {
            "pinyin": "chē dài mǎ fán",
            "meaning": "车子损坏、马匹疲惫，形容长途奔波、行旅劳顿。",
            "example": "一路车殆马烦，总算在天黑前赶到了城里。"
        },
        1526: {
            "pinyin": "chē lì zhī méng",
            "meaning": "贫贱时同乘一车，富贵时共戴斗笠，比喻朋友之间不因贫富贵贱而改变情谊的约定。",
            "example": "他们少年立下车笠之盟，几十年始终不负。"
        },
        1527: {
            "pinyin": "chē mǎ yíng mén",
            "meaning": "车马满门，形容宾客络绎不绝或门庭十分显赫。",
            "example": "从他升官以后，家中车马盈门。"
        },
        1528: {
            "pinyin": "chē shuǐ mǎ lóng",
            "meaning": "车像流水，马如游龙，形容车马往来不绝、街道繁华热闹。",
            "example": "节日期间，商业街上车水马龙，热闹非凡。"
        },
        1529: {
            "pinyin": "chē wú tuì biǎo",
            "meaning": "古代战车前进有标记、后退无标记，比喻只许前进、不许后退的决心。",
            "example": "将军下令车无退表，誓与敌军决一死战。"
        },
        1530: {
            "pinyin": "chē zǎi dǒu liáng",
            "meaning": "用车来装、用斗来量，形容数量极多、不足为奇。",
            "example": "那样的人才在大城市简直是车载斗量。"
        },
        1531: {
            "pinyin": "chē zài mǎ qián",
            "meaning": "大马拖车在前，小马系在车后，比喻初学者在前辈带领下见习，做事就容易学会。",
            "example": "新员工车在马前，在师傅的指导下很快熟悉了流程。"
        },
        1532: {
            "pinyin": "chě péng lā qiàn",
            "meaning": "比喻从事不正当的介绍撮合、说情拉拢，以从中牟利。",
            "example": "他专靠扯篷拉纤过活，名声极坏。"
        },
        1533: {
            "pinyin": "chè shàng chè xià",
            "meaning": "彻：贯通。形容上下贯通、前后通达，也指理解得十分透彻。",
            "example": "只有把制度精神彻上彻下地吃透，落实才不会走样。"
        },
        1534: {
            "pinyin": "chè tóu chè wěi",
            "meaning": "从头到尾，完完全全，毫无遗漏。",
            "example": "这件事他参与其中，是个彻头彻尾的见证人。"
        },
        1535: {
            "pinyin": "chè jīn lù zhǒu",
            "meaning": "掣衣襟就露出胳膊肘，形容衣服破烂、生活贫困，也比喻处境窘迫、应付不过来。",
            "example": "这些年生意不景气，他已是掣襟露肘，难以为继。"
        },
        1536: {
            "pinyin": "chēn quán bù dǎ xiào miàn",
            "meaning": "比喻不宜欺辱态度和悦、对人和气的人。",
            "example": "他并无恶意，你也该记得嗔拳不打笑面。"
        },
        1537: {
            "pinyin": "chēn mù qiè chǐ",
            "meaning": "瞪大眼睛，咬紧牙齿，形容极端愤怒的样子。",
            "example": "听到敌军暴行，士兵们无不瞋目切齿。"
        },
        1538: {
            "pinyin": "chén bó jué lì",
            "meaning": "亦作“沉博绝丽”，形容文章含意深远、内容渊博、辞藻华美。",
            "example": "这篇序文沈博绝丽，一时传诵。"
        },
        1539: {
            "pinyin": "chén bó jué lì",
            "meaning": "同“沈博绝丽”，指诗文深沉渊博、文辞极其华丽。",
            "example": "他早年的作品多为沉博绝丽之作。"
        },
        1540: {
            "pinyin": "chén fú fǔ yǎng",
            "meaning": "形容人事或世道的盛衰起落。",
            "example": "他一生历经沉浮俯仰，看淡了功名。"
        },
        1541: {
            "pinyin": "chén gù zì ruò",
            "meaning": "沉痼：积久难治的顽疾。比喻积久难改的社会弊病、习俗或嗜好依旧如故。",
            "example": "屡禁黄牛党而风气仍旧，真是沉痼自若。"
        },
        1542: {
            "pinyin": "chén jìng guǎ yán",
            "meaning": "性格深沉安静，不爱多说话。",
            "example": "他平日沉静寡言，但关键时刻总能一语中的。"
        },
        1543: {
            "pinyin": "chén kē nán qǐ",
            "meaning": "沉疴：久治不愈的重病。形容长期患重病，以致难以下床；也可比喻长期积累的严重问题难以解决。",
            "example": "多年劳损终于沉疴难起，只好卧床休养。"
        },
        1544: {
            "pinyin": "chén lǐ fú guā",
            "meaning": "把李子沉在水中、瓜浮在水面，比喻夏日以冷浸瓜果来消暑的情景。",
            "example": "盛夏午后，几位老友对坐井台旁，沉李浮瓜，清谈往事。"
        },
        1545: {
            "pinyin": "chén miǎn jiǔ sè",
            "meaning": "沉湎：沉迷。沉溺在酒色之中，形容贪恋享乐、荒于正事。",
            "example": "他年轻时一度沉湎酒色，差点误了前程。"
        },
        1546: {
            "pinyin": "chén mò guǎ yán",
            "meaning": "沉着稳重，话不多说，形容性格寡言内敛。",
            "example": "他平素沉默寡言，却很擅长用行动表达关心。"
        },
        1547: {
            "pinyin": "chén qián gāng kè",
            "meaning": "沉潜：性情深藏不露；刚克：刚健能胜。形容人性格深沉内敛而又刚强有力。",
            "example": "这位老将军沉潜刚克，不轻易表露情绪。"
        },
        1548: {
            "pinyin": "chén yín bù jué",
            "meaning": "沉吟：低声自语、反复思量。形容遇事犹豫不决、拿不定主意。",
            "example": "面对两个机会，他沉吟不决，反复权衡利弊。"
        },
        1549: {
            "pinyin": "chén yín zhāng jù",
            "meaning": "默默揣摩、琢磨诗文的章句，形容苦心推敲文字。",
            "example": "他常夜半灯下沉吟章句，力求文辞精当。"
        },
        1550: {
            "pinyin": "chén yú luò yàn",
            "meaning": "鱼沉水底、雁落沙洲，比喻女子容貌极其美丽，令飞禽亦自惭形秽。",
            "example": "她一袭素衣步入厅堂，真有沉鱼落雁之姿。"
        },
        1551: {
            "pinyin": "chén yù dùn cuò",
            "meaning": "多用来形容诗文、乐曲等意境深沉、气势郁勃，声调和节奏抑扬顿挫。",
            "example": "这篇散文格调沉郁顿挫，读来颇有余味。"
        },
        1552: {
            "pinyin": "chén yuān mò bái",
            "meaning": "深沉的冤屈得不到昭雪，形容蒙受重大冤屈而长期得不到申诉。",
            "example": "多少人死于战乱，其沉冤莫白，令人扼腕。"
        },
        1553: {
            "pinyin": "chén zào chǎn wā",
            "meaning": "灶台都沉入水中生出青蛙，形容水患严重、积水极深。",
            "example": "连年暴雨，河水泛滥，沿岸村庄几乎沉灶产蛙。"
        },
        1554: {
            "pinyin": "chén zǐ fàn qǐ",
            "meaning": "沉在水底的渣滓又翻浮上来，比喻平时隐藏的问题、矛盾重新暴露出来。",
            "example": "整顿不力，只会让旧弊沉滓泛起。"
        },
        1555: {
            "pinyin": "chén guāng xī wēi",
            "meaning": "形容清晨微弱而柔和的曙光。",
            "example": "山谷间晨光熹微，薄雾尚未散尽。"
        },
        1556: {
            "pinyin": "chén hūn dìng xǐng",
            "meaning": "早晚问安侍奉父母，形容子女对父母十分孝敬。",
            "example": "他自幼晨昏定省，从不怠慢双亲。"
        },
        1557: {
            "pinyin": "chén xīng yè mèi",
            "meaning": "天刚亮就起床，夜深了才睡，形容非常勤劳辛苦。",
            "example": "农忙时节，乡亲们晨兴夜寐，抢收稻谷。"
        },
        1558: {
            "pinyin": "chén zhōng mù gǔ",
            "meaning": "早晨的钟声、傍晚的鼓声，多指寺院中敲钟击鼓的仪式，也比喻能使人警醒的声音或言论。",
            "example": "佛寺的晨钟暮鼓，提醒世人莫忘修心。"
        },
        1559: {
            "pinyin": "chén mén rú shì",
            "meaning": "大臣门前如同集市一般热闹，形容权贵之家门庭若市、求见者众多。",
            "example": "当权之时，他家臣门如市；一朝失势，宾客顿散。"
        },
        1560: {
            "pinyin": "chén xīn rú shuǐ",
            "meaning": "心境平静如水，多用以形容忠臣一片清正之心，也指内心十分平静。",
            "example": "面对诱惑，他自称臣心如水，不为所动。"
        },
        1561: {
            "pinyin": "chén fàn tú gēng",
            "meaning": "用尘土作饭、泥土作羹，比喻儿童游戏之物；也借指毫无用处的东西。",
            "example": "这些夸张的谣言，不过尘饭涂羹，不足采信。"
        },
        1562: {
            "pinyin": "chén gòu bǐ kāng",
            "meaning": "尘土污垢、秕谷米糠，比喻琐碎而没有价值的东西。",
            "example": "与其在尘垢秕糠上斤斤计较，不如集中精力办正事。"
        },
        1563: {
            "pinyin": "chén chén xiāng yīn",
            "meaning": "原指皇仓陈粮层层相压，后比喻沿袭老一套、毫无创新。",
            "example": "文章若只陈陈相因，难以给人新鲜感。"
        },
        1564: {
            "pinyin": "chén cí làn diào",
            "meaning": "陈旧的词句、滥用的论调，形容说话或文章毫无新意、公式化。",
            "example": "他的发言尽是陈词滥调，听众兴味索然。"
        },
        1565: {
            "pinyin": "chén gǔ zi làn zhī ma",
            "meaning": "旧谷烂芝麻，比喻陈年旧事、无足轻重的话题。",
            "example": "这些陈谷子烂芝麻，就别再翻来覆去了。"
        },
        1566: {
            "pinyin": "chén guī lòu xí",
            "meaning": "陈旧的规章、鄙陋的习俗，指过时而不合理的旧制度和坏习惯。",
            "example": "要推进改革，首先得破除这些陈规陋习。"
        },
        1567: {
            "pinyin": "chén lì jiù liè",
            "meaning": "陈力：施展才力；就列：走上岗位。指根据各人能力安排适当的职务。",
            "example": "用人应当陈力就列，各尽其才。"
        },
        1568: {
            "pinyin": "chén shàn bì xié",
            "meaning": "向君主进言善政，以堵塞邪念与错误，比喻以正道遏止邪风。",
            "example": "士大夫当以陈善闭邪为己任。"
        },
        1569: {
            "pinyin": "chén shī jū lǚ",
            "meaning": "陈列兵马、整肃军旅，指出征前集合军队、发布誓师命令。",
            "example": "古时每逢大战，必先陈师鞠旅，以振军威。"
        },
        1570: {
            "pinyin": "chén yán wù qù",
            "meaning": "陈言：陈旧的言辞。写作或说话时务必去除陈旧套话，力求创新。",
            "example": "他治学严谨，尤重陈言务去。"
        },
        1571: {
            "pinyin": "chèn huǒ dǎ jié",
            "meaning": "趁着人家失火抢劫财物，比喻乘人之危、落井下石。",
            "example": "在别人困难时趁火打劫，是最为不齿的行为。"
        },
        1572: {
            "pinyin": "chèn rè dǎ tiě",
            "meaning": "铁要趁热锻打，比喻抓住时机、及时行事。",
            "example": "机会难得，项目推进要趁热打铁。"
        },
        1573: {
            "pinyin": "chèn rén zhī wēi",
            "meaning": "借他人危难之机谋取私利或加以打击。",
            "example": "对手公司资金紧张，他却不愿趁人之危。"
        },
        1574: {
            "pinyin": "chèn shì luò péng",
            "meaning": "原比喻乘机把船篷收起，后多指趁势收手或见好就收。",
            "example": "见形势不利，他干脆趁势落篷，停止争执。"
        },
        1575: {
            "pinyin": "chèn jiā yǒu wú",
            "meaning": "办事花费要与家庭经济状况相适宜，既不能奢侈也不要过分寒酸。",
            "example": "婚丧嫁娶都应称家有无，切莫打肿脸充胖子。"
        },
        1576: {
            "pinyin": "chèn tǐ zài yī",
            "meaning": "按照身材裁剪衣服，比喻根据实际情况办事。",
            "example": "制度设计要称体载衣，不能一刀切。"
        },
        1577: {
            "pinyin": "chèn xīn rú yì",
            "meaning": "心满意足、一切合乎心意。",
            "example": "这份工作既稳定又自由，让他称心如意。"
        },
        1578: {
            "pinyin": "chèn xū ér rù",
            "meaning": "利用对方空虚薄弱之机乘机侵入或进攻。",
            "example": "黑客往往趁虚而入，攻击防护薄弱的系统。"
        },
        1579: {
            "pinyin": "chēng chén nà gòng",
            "meaning": "自称臣子、进献贡物，指向强者屈服称臣。",
            "example": "战败之后，只得称臣纳贡，以求苟安。"
        },
        1580: {
            "pinyin": "chēng dé duó gōng",
            "meaning": "衡量德行和功绩，指根据功德大小加以奖惩或评定。",
            "example": "封赏必须称德度功，方能服众。"
        },
        1581: {
            "pinyin": "chēng gū dào guǎ",
            "meaning": "“孤”“寡”原是君主自称，指做诸侯、帝王的人自称孤、寡以示自谦。",
            "example": "古时诸侯常称孤道寡，自谦德薄。"
        },
        1582: {
            "pinyin": "chēng xián jiàn néng",
            "meaning": "称扬贤者、推荐能人，指积极举荐人才。",
            "example": "用人之道，在于广开言路，称贤荐能。"
        },
        1583: {
            "pinyin": "chēng wáng chēng bà",
            "meaning": "自立为王、妄图称霸，形容仗势欺人或争权夺利。",
            "example": "他在行业内一味称王称霸，终致众叛亲离。"
        },
        1584: {
            "pinyin": "chēng xīn ér cuàn",
            "meaning": "称量柴薪再用来烧火做饭，比喻只顾小事、斤斤计较或过分吝啬。",
            "example": "管理者若事事称薪而爨，反而失掉大局。"
        },
        1585: {
            "pinyin": "chēng xiōng dào dì",
            "meaning": "以兄弟相称，多指彼此关系亲密，也可指虚与委蛇、假意亲近。",
            "example": "他们口口声声称兄道弟，实则各怀心思。"
        },
        1586: {
            "pinyin": "chēng yǔ dào qíng",
            "meaning": "一方说下雨，一方说天晴，比喻话不投机、意见完全不合。",
            "example": "两人商量方案，总是称雨道晴，难以达成一致。"
        },
        1587: {
            "pinyin": "chēng cháng zhǔ fù",
            "meaning": "形容吃得肚子非常饱，仿佛肠子都被撑住了。",
            "example": "这顿饭大家都吃得撑肠拄腹。"
        },
        1588: {
            "pinyin": "chēng hū qí hòu",
            "meaning": "在别人后面干瞪眼赶不上，形容远远落在后面。",
            "example": "在科技创新方面，我们已瞠乎其后，不得不加倍努力。"
        },
        1589: {
            "pinyin": "chēng mù jié shé",
            "meaning": "瞠目：瞪大眼睛；结舌：说不出话来。形容大吃一惊或理屈说不出话。",
            "example": "听到这个消息，他一时瞠目结舌。"
        },
        1590: {
            "pinyin": "chèng jīn zhù liǎng",
            "meaning": "按斤秤量、按两登记，比喻过分计较细节或小利。",
            "example": "做学问不能秤斤注两地抠字眼，而要把握要旨。"
        },
        1591: {
            "pinyin": "chēng xīn ér cuàn",
            "meaning": "同“称薪而爨”，形容斤斤计较、只会料理琐碎小事。",
            "example": "若只会秤薪而爨，难以成就大业。"
        },
        1592: {
            "pinyin": "chéng bài dé shī",
            "meaning": "事情成功或失败，以及由此带来的得与失。",
            "example": "成败得失，应冷静总结经验教训。"
        },
        1593: {
            "pinyin": "chéng bài lì dùn",
            "meaning": "成败以及利钝，指事情结果的好坏与利害。",
            "example": "纵论古今成败利钝，不外乎人事与时势。"
        },
        1594: {
            "pinyin": "chéng bài lùn rén",
            "meaning": "根据成败来评价一个人，含有只看结果、不问过程之意。",
            "example": "历史往往以成败论人，却忽略了许多复杂因素。"
        },
        1595: {
            "pinyin": "chéng jǐ chéng wù",
            "meaning": "既成就自己，也帮助他人成就事业，强调内外兼修。",
            "example": "真正的君子，当能成己成物，而非独善其身。"
        },
        1596: {
            "pinyin": "chéng jiā lì yè",
            "meaning": "成就家庭、建立事业，指立家创业、安身立命。",
            "example": "他白手起家，终于成家立业。"
        },
        1597: {
            "pinyin": "chéng lóng pèi tào",
            "meaning": "把零散部分配合起来，形成完整配套的系统。",
            "example": "只有基础设施成龙配套，产业才能健康发展。"
        },
        1598: {
            "pinyin": "chéng nián lěi yuè",
            "meaning": "成年又累月，形容时间长久。",
            "example": "他在这个岗位上成年累月，兢兢业业。"
        },
        1599: {
            "pinyin": "chéng qiān shàng wàn",
            "meaning": "形容数量极多，达到成千上万。",
            "example": "节日期间，景区里成千上万的游客络绎不绝。"
        },
        1600: {
            "pinyin": "chéng qún jié duì",
            "meaning": "许多人或动物结成一群群、一队队，形容数量多而聚集在一起。",
            "example": "傍晚时分，广场上成群结队的市民在散步锻炼。"
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

    print(f"已为 1501–1600 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
