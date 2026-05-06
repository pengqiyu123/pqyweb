import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    enrich = {
        1601: {
            "pinyin": "chéng rén bù zì zài, zì zài bù chéng rén",
            "meaning": "要想有所成就，就不能贪图安逸自在；若只图自在享乐，往往难以成器成名。",
            "example": "老师常勉励我们说：成人不自在，自在不成人，要吃得了苦才有出息。"
        },
        1602: {
            "pinyin": "chéng rén qǔ yì",
            "meaning": "成仁：以牺牲生命成全仁德；取义：舍生以取正义。指为正义事业牺牲生命。",
            "example": "无数先烈为了民族解放而成仁取义，值得后人永远铭记。"
        },
        1603: {
            "pinyin": "chéng rén zhī měi",
            "meaning": "成：成全；美：好事。成全别人的好事，也指帮助别人实现美好的愿望。",
            "example": "他一向乐于成人之美，总是尽力为同事创造机会。"
        },
        1604: {
            "pinyin": "chéng shì bù shuō",
            "meaning": "说：解说、多言。已经做成的事情就不必再多加解释，引申为事情既已过去就不必重提。",
            "example": "这件事已经圆满解决，就成事不说，好好向前看吧。"
        },
        1605: {
            "pinyin": "chéng shì bù zú, bài shì yǒu yú",
            "meaning": "指没有本事把事情办成，反而常常把事情弄糟。",
            "example": "他做事一贯成事不足，败事有余，大家都不敢放心把重任交给他。"
        },
        1606: {
            "pinyin": "chéng shuāng zuò duì",
            "meaning": "配成一对，多指男女、夫妻或成双成对的事物。",
            "example": "节日的街头，到处是成双作对散步的情侣。"
        },
        1607: {
            "pinyin": "chéng suàn zài xīn",
            "meaning": "心中早已盘算好应付的办法，形容胸有成竹、早有安排。",
            "example": "虽然他话不多，但对项目进度早已成算在心。"
        },
        1608: {
            "pinyin": "chéng yě xiāo hé, bài yě xiāo hé",
            "meaning": "成事由于萧何，败事也由于萧何。比喻事情的成败或好坏都由同一个人造成。",
            "example": "这家公司的发展可以说是成也萧何，败也萧何，全系于创始人一人身上。"
        },
        1609: {
            "pinyin": "chéng yī jiā yán",
            "meaning": "学术或言论自成体系，独树一帜，形成自己的一家之言。",
            "example": "经过多年研究，他在这个领域终于成一家言，受到同行重视。"
        },
        1610: {
            "pinyin": "chéng zé wéi wáng, bài zé wéi zéi",
            "meaning": "旧指争夺政权斗争中，成功者被称为君王，失败者被视为盗贼，引申为只以成败论是非。",
            "example": "历史的评价往往带有成则为王，败则为贼的残酷色彩。"
        },
        1611: {
            "pinyin": "chéng zhú zài xiōng",
            "meaning": "成竹：已有完整形象。原指画竹前胸中早有竹子的成形意象，比喻做事之前已有周密打算，胸有成竹。",
            "example": "对这次谈判，他早已成竹在胸，应对从容不迫。"
        },
        1612: {
            "pinyin": "chéng xīn chéng yì",
            "meaning": "形容十分真挚诚恳，心意完全出于真心。",
            "example": "只要你诚心诚意道歉，朋友未必不会原谅你。"
        },
        1613: {
            "pinyin": "chéng huáng chéng kǒng",
            "meaning": "诚：实在；惶、恐：害怕不安。原为臣下奏章中的谦词，形容十分恭敬而又惶恐不安。",
            "example": "忽然被点名发言，他不免有些诚惶诚恐。"
        },
        1614: {
            "pinyin": "chéng běi xú gōng",
            "meaning": "指战国时齐国城北的徐姓美男子，后用作美男子的代称。",
            "example": "他相貌俊朗，人称当代城北徐公。"
        },
        1615: {
            "pinyin": "chéng hú shè shǔ",
            "meaning": "城墙上的狐狸、社庙里的老鼠，比喻依仗权势为非作歹、一时难以驱除的小人。",
            "example": "这些盘踞多年的城狐社鼠，不整治难以还百姓清平。"
        },
        1616: {
            "pinyin": "chéng mén shī huǒ, yāng jí chí yú",
            "meaning": "城门着火，人们从护城河取水救火，致使池中之鱼跟着遭殃。比喻无辜者因他人之祸而被连累。",
            "example": "这次整顿虽然针对个别害群之马，却免不了城门失火，殃及池鱼。"
        },
        1617: {
            "pinyin": "chéng xià zhī méng",
            "meaning": "敌军兵临城下，被迫在城下签订的屈辱条约，引申为被迫接受的屈辱性协议。",
            "example": "若一味妥协退让，恐怕难免再订城下之盟。"
        },
        1618: {
            "pinyin": "chéng mén lì xuě",
            "meaning": "原指宋代杨时等在程颐门下冒雪久立求教的故事，后用来比喻尊师重道、求学恭敬虔诚。",
            "example": "他远赴名师门下，几乎有程门立雪之诚。"
        },
        1619: {
            "pinyin": "chéng chē dài lì",
            "meaning": "乘车的是贵者，戴笠者多为贫者，比喻不因富贵贫贱而改变旧日交情。",
            "example": "即使他后来飞黄腾达，对老朋友仍是一片乘车戴笠之情。"
        },
        1620: {
            "pinyin": "chéng féi yì qīng",
            "meaning": "乘肥：骑乘肥壮的马；衣轻：穿轻暖的裘衣。形容生活奢侈豪华。",
            "example": "昔日的权臣们个个乘肥衣轻，穷奢极欲。"
        },
        1621: {
            "pinyin": "chéng fēng pò làng",
            "meaning": "船只乘着风势破浪前进，比喻排除困难，奋勇前进，也指事业迅猛发展。",
            "example": "青年人应当胸怀理想，勇于乘风破浪。"
        },
        1622: {
            "pinyin": "chéng jiān cè féi",
            "meaning": "乘坚车、策肥马，形容车马华贵，比喻生活富足奢华。",
            "example": "他出入皆乘坚策肥，与百姓疾苦渐行渐远。"
        },
        1623: {
            "pinyin": "chéng jiān qū liáng",
            "meaning": "乘坐坚固的车，驱使良马，形容生活豪华。",
            "example": "末世权贵温衣美食，日夜乘坚驱良。"
        },
        1624: {
            "pinyin": "chéng lóng jiā xù",
            "meaning": "乘龙：比喻女子得佳婿。旧时称赞才貌双全、极为称心的女婿。",
            "example": "父母常以能得一位乘龙佳婿为荣。"
        },
        1625: {
            "pinyin": "chéng lóng kuài xù",
            "meaning": "乘龙：比喻得佳婿；快婿：称心如意的女婿。指才貌出众、极得称意的好女婿。",
            "example": "这女儿出嫁，的确是找了一位乘龙快婿。"
        },
        1626: {
            "pinyin": "chéng luán kuà fèng",
            "meaning": "乘鸾、跨凤，比喻结成美满姻缘的佳偶。",
            "example": "新婚宴上，亲友都祝福他们乘鸾跨凤、白头偕老。"
        },
        1627: {
            "pinyin": "chéng qí bù bèi",
            "meaning": "乘：趁。趁对方没有防备之时采取行动，多指乘人之机加以袭击或算计。",
            "example": "敌军乘其不备，突然发起夜袭。"
        },
        1628: {
            "pinyin": "chéng rén zhī wēi",
            "meaning": "趁别人处于危难之际加以要挟或侵害，含贬义。",
            "example": "在别人落难时乘人之危，实在不厚道。"
        },
        1629: {
            "pinyin": "chéng shí chéng shì",
            "meaning": "趁着时机和有利形势而采取行动，做成事业。",
            "example": "改革开放要善于乘时乘势，加快发展。"
        },
        1630: {
            "pinyin": "chéng wěi xíng zhà",
            "meaning": "伪：虚伪；行诈：施展欺诈手段。指弄虚作假、以诈取利。",
            "example": "企业一旦习惯乘伪行诈，终将失去市场信任。"
        },
        1631: {
            "pinyin": "chéng xì ér rù",
            "meaning": "乘：趁；隙：空隙、弱点。趁对方防备疏漏之机进入或攻击，多用于军事或比喻趁机介入。",
            "example": "对手防线松弛，我军不可让敌人乘隙而入。"
        },
        1632: {
            "pinyin": "chéng xìng ér lái, bài xìng ér guī",
            "meaning": "兴：兴致。趁着兴致而来，却扫兴地回去，形容期待落空。",
            "example": "本想看一场精彩比赛，不料因雨取消，只好乘兴而来，败兴而归。"
        },
        1633: {
            "pinyin": "chéng xū dié chū",
            "meaning": "虚：空虚、薄弱处；迭：屡次。指屡次向对方防守薄弱之处出击，多用于军事。",
            "example": "游击队乘虚迭出，搅得敌军疲于奔命。"
        },
        1634: {
            "pinyin": "chéng xū ér rù",
            "meaning": "乘：趁；虚：空虚、薄弱。趁对方力量虚弱或防备松懈时侵入或发动攻击。",
            "example": "系统一旦漏洞未补，黑客就可能乘虚而入。"
        },
        1635: {
            "pinyin": "chéng è quàn shàn",
            "meaning": "惩：惩罚；劝：勉励。惩罚作恶者，勉励行善者。",
            "example": "法律的宗旨之一，就是惩恶劝善，维护社会正义。"
        },
        1636: {
            "pinyin": "chéng fèn zhì yù",
            "meaning": "惩：惩戒；忿：愤怒；窒：抑止；欲：嗜欲。克制愤怒，抑制欲望。",
            "example": "修身之道，在于惩忿窒欲，以保内心平和。"
        },
        1637: {
            "pinyin": "chéng gēng chuī jī",
            "meaning": "因吃热汤被烫而连冷菜也要吹一吹，比喻因一次教训而过分小心，见微知惧。",
            "example": "自从项目失败之后，他在投资上简直到了惩羹吹齑的地步。"
        },
        1638: {
            "pinyin": "chéng qián bì hòu",
            "meaning": "惩：警戒；毖：谨慎。以以往的错误为教训，使以后小心谨慎，不再重犯。",
            "example": "这次事故之后，公司召开会议，要求全体员工惩前毖后。"
        },
        1639: {
            "pinyin": "chéng yī jǐng bǎi",
            "meaning": "惩：惩罚；儆：警戒。惩罚一个或少数人，用来警戒多数人。",
            "example": "对严重违规者必须严肃处理，以惩一儆百。"
        },
        1640: {
            "pinyin": "chéng jiāng rú liàn",
            "meaning": "澄：清澈；练：洁白的绢。形容江水清澈平静，如同一条白练。",
            "example": "登高远眺，只见澄江如练，风光旖旎。"
        },
        1641: {
            "pinyin": "chéng huáng jú lǜ",
            "meaning": "橙子金黄、橘子翠绿，形容深秋初冬果树成熟、景色宜人的时节。",
            "example": "江南水乡，一到橙黄橘绿的季节分外迷人。"
        },
        1642: {
            "pinyin": "chéng huān xī xià",
            "meaning": "子女在父母膝前承欢娱悦，形容孝子能在父母身边尽孝。",
            "example": "远在他乡的游子，最盼的就是回家承欢膝下。"
        },
        1643: {
            "pinyin": "chéng píng shèng shì",
            "meaning": "承平：长久安定。指国家长期太平、百姓安乐的盛世局面。",
            "example": "生于承平盛世，更应珍惜来之不易的安宁生活。"
        },
        1644: {
            "pinyin": "chéng qián qǐ hòu",
            "meaning": "继承前人的成果，开辟后来的道路，多形容在历史或学术发展中的承续作用。",
            "example": "这部著作在本学科中具有承前启后的重要意义。"
        },
        1645: {
            "pinyin": "chéng shàng qǐ xià",
            "meaning": "承接上文，启发下文，比喻在中间起衔接过渡作用。",
            "example": "这段话承上启下，使全文结构更加严谨。"
        },
        1646: {
            "pinyin": "chéng tiān zhī yòu",
            "meaning": "承受上天的保佑和庇护，形容幸运得到了天命眷顾。",
            "example": "多亏承天之祐，才让他逢凶化吉、转危为安。"
        },
        1647: {
            "pinyin": "chéng xiān qǐ hòu",
            "meaning": "承继先人、开导后学，形容在学问或事业上承上启下的作用。",
            "example": "他毕生从事教育事业，可谓承先启后、桃李满门。"
        },
        1648: {
            "pinyin": "chéng yán hòu sè",
            "meaning": "察言观色，小心揣摩他人脸色以讨好奉承。多形容事人逢迎的态度。",
            "example": "在旧社会，许多小官吏终日承颜候色，只为保住一官半职。"
        },
        1649: {
            "pinyin": "chěng xìng wàng wéi",
            "meaning": "任性胡为，不加节制地按照个人脾气去做事。",
            "example": "一个人若总是逞性妄为，终会为自己的冲动付出代价。"
        },
        1650: {
            "pinyin": "chěng xiōng sì nüè",
            "meaning": "逞：任意施展；肆虐：肆意残害。形容凶恶的人恣意横行、残害百姓。",
            "example": "这伙匪徒在山中逞凶肆虐，民不聊生。"
        },
        1651: {
            "pinyin": "chèng bù lí tuó",
            "meaning": "秤总要有砣，比喻彼此关系密切、常相随不分离。",
            "example": "他俩从小一起长大，简直是秤不离砣。"
        },
        1652: {
            "pinyin": "chèng píng dǒu mǎn",
            "meaning": "秤得平、斗装满，比喻买卖公平或收支充足。",
            "example": "老店一向秤平斗满，从不亏负顾客。"
        },
        1653: {
            "pinyin": "chī ér dāi nǚ",
            "meaning": "天真痴呆的少年男女，形容质朴单纯、不谙世事的年轻人。",
            "example": "一群痴儿呆女，在村口追逐嬉戏。"
        },
        1654: {
            "pinyin": "chī nán yuàn nǚ",
            "meaning": "为情所困的男女，形容恋爱中多愁善感的一对男女。",
            "example": "戏里演的无非是几个痴男怨女的爱恨纠葛。"
        },
        1655: {
            "pinyin": "chī rén shuō mèng",
            "meaning": "痴人说梦话，比喻荒诞不经、根本办不到的空想或言论。",
            "example": "想一夜之间暴富，不过是痴人说梦。"
        },
        1656: {
            "pinyin": "chī xīn wàng xiǎng",
            "meaning": "一味凭主观愿望胡思乱想，比喻不切实际的幻想。",
            "example": "不踏实学习，只靠痴心妄想，是不可能成功的。"
        },
        1657: {
            "pinyin": "chī mèi wǎng liǎng",
            "meaning": "古代传说中的山川鬼怪，后泛指各种魑魅魍魉，比喻隐藏的坏人坏事。",
            "example": "只有阳光透明的制度，才能让魑魅魍魉无处藏身。"
        },
        1658: {
            "pinyin": "chī bù liǎo dōu zhe zǒu",
            "meaning": "吃不完还得兜着走，比喻闯下的祸太大，自身难以承受其后果。",
            "example": "乱投资一旦亏损，你可就吃不了兜着走了。"
        },
        1659: {
            "pinyin": "chī chuān yòng dù",
            "meaning": "吃的、穿的以及日常费用的总称，指生活开支。",
            "example": "一家人的吃穿用度，全靠他一人支撑。"
        },
        1660: {
            "pinyin": "chī lǐ pá wài",
            "meaning": "吃的是这一方的饭，却替另一方卖力，比喻受一方恩惠却暗中帮助别的人。",
            "example": "做事要讲良心，可不能吃里爬外。"
        },
        1661: {
            "pinyin": "chī liáng bù guǎn shì",
            "meaning": "领着粮饷却不做事，比喻只拿报酬不负责任的人。",
            "example": "这种吃粮不管事的干部，早该好好整顿。"
        },
        1662: {
            "pinyin": "chī yī qiàn, zhǎng yī zhì",
            "meaning": "堑：陷坑，比喻挫折。遭受一次挫折就增长一分见识，指从失败中吸取教训。",
            "example": "吃一堑，长一智，这次失误至少让他懂得了谨慎。"
        },
        1663: {
            "pinyin": "chī zhe bù jìn",
            "meaning": "东西多得吃不完，形容物资十分充足富足。",
            "example": "如今家里粮食充裕，真是吃着不尽。"
        },
        1664: {
            "pinyin": "chī mù hǔ wěn",
            "meaning": "鸱目：猫头鹰的眼睛；虎吻：老虎的嘴。形容相貌丑恶凶狠。",
            "example": "那恶吏一副鸱目虎吻的样子，令人望而生畏。"
        },
        1665: {
            "pinyin": "chī yā shì shǔ",
            "meaning": "鸱鸦喜吃老鼠，比喻嗜好低下或指人贪婪残忍。",
            "example": "这些鸱鸦嗜鼠之徒，只顾捞取不义之财。"
        },
        1666: {
            "pinyin": "chī zhī yǐ bí",
            "meaning": "发出冷笑、用鼻子哼气表示轻蔑，形容极端看不起。",
            "example": "听到这种谎言，人们无不嗤之以鼻。"
        },
        1667: {
            "pinyin": "chí mù zhī nián",
            "meaning": "迟暮：日将落山，比喻人的老年。指临近晚年的岁月。",
            "example": "虽已到迟暮之年，他仍笔耕不辍。"
        },
        1668: {
            "pinyin": "chí chóu wò suàn",
            "meaning": "筹与算都是古代计算用具，比喻善于谋划、精于计算收支。",
            "example": "作为财务主管，他最擅长持筹握算。"
        },
        1669: {
            "pinyin": "chí héng yōng xuán",
            "meaning": "衡、璇皆为权衡、圭璇之器，比喻执掌权柄、主持公道。",
            "example": "身居要职者，当能持衡拥璇，不徇私情。"
        },
        1670: {
            "pinyin": "chí lí cè hǎi",
            "meaning": "蠡：瓠壳做的勺子。用小勺子去量大海，比喻见识短浅，难以穷尽事物全貌。",
            "example": "若只凭片面材料下结论，无异于持蠡测海。"
        },
        1671: {
            "pinyin": "chí lù yǎng jiāo",
            "meaning": "持禄：保住官位俸禄；养交：结交权贵。指依附权势、拉拢交往以巩固自己的职位。",
            "example": "他一味持禄养交，只知巴结上司，并无半点担当。"
        },
        1672: {
            "pinyin": "chí píng zhī lùn",
            "meaning": "公正不偏的议论或评论。",
            "example": "这篇社论对事件分析客观，可谓持平之论。"
        },
        1673: {
            "pinyin": "chí wēi fú diān",
            "meaning": "扶持危困、挽救倾颓的局面。",
            "example": "国难当头，更需有人挺身持危扶颠。"
        },
        1674: {
            "pinyin": "chí yíng bǎo tài",
            "meaning": "盈：盛满；泰：安泰。指在事业、权势正盛时保持谨慎，从而维持长久的安定局面。",
            "example": "身居高位，更要持盈保泰，戒骄戒躁。"
        },
        1675: {
            "pinyin": "chí zhāi bǎ sù",
            "meaning": "持斋、吃素，比喻虔诚守戒，多指信佛者遵守戒律、长期茹素。",
            "example": "她自中年以后便持斋把素，清心寡欲。"
        },
        1676: {
            "pinyin": "chí zhī yǐ héng",
            "meaning": "长期坚持不懈，恒久不变。",
            "example": "学习贵在持之以恒，而非三天打鱼两天晒网。"
        },
        1677: {
            "pinyin": "chí zhī yǒu gù",
            "meaning": "所持见解与主张有充分根据。",
            "example": "他的观点持之有故，言之成理，颇具说服力。"
        },
        1678: {
            "pinyin": "chí yú lóng niǎo",
            "meaning": "池中的鱼、笼中的鸟，比喻受拘束而失去自由的人。",
            "example": "这些昔日豪杰，如今却成了池鱼笼鸟，令人唏嘘。"
        },
        1679: {
            "pinyin": "chí yú zhī yāng",
            "meaning": "比喻因受牵连而蒙受的无端祸害。",
            "example": "此案牵连甚广，不少无辜之人也成了池鱼之殃。"
        },
        1680: {
            "pinyin": "chí chěng jiāng chǎng",
            "meaning": "在疆场上纵马奔驰，形容英勇善战、活跃于战场。",
            "example": "他青年从军，屡立战功，终生驰骋疆场。"
        },
        1681: {
            "pinyin": "chí míng zhōng wài",
            "meaning": "名声传到中国和外国，形容声誉极大。",
            "example": "这所大学在科研领域早已驰名中外。"
        },
        1682: {
            "pinyin": "chí chú bù qián",
            "meaning": "犹豫不决、徘徊不前，形容畏缩不前的样子。",
            "example": "机会就在眼前，他却踟蹰不前，终究错失良机。"
        },
        1683: {
            "pinyin": "chǐ bái chún hóng",
            "meaning": "牙齿洁白、嘴唇红润，形容青少年的容貌俊美。",
            "example": "那孩子齿白唇红，一看就是个聪明伶俐的。"
        },
        1684: {
            "pinyin": "chǐ ruò biān bèi",
            "meaning": "牙齿整齐洁白，如同串联起来的贝壳，形容牙齿洁白美丽。",
            "example": "她笑起来齿若编贝，十分动人。"
        },
        1685: {
            "pinyin": "chǐ wáng shé cún",
            "meaning": "牙齿虽亡而舌头尚在，比喻处境虽危但仍有转机或力量尚存。",
            "example": "国家多难之秋，犹如齿亡舌存，尤须同心自强。"
        },
        1686: {
            "pinyin": "chǐ yá chūn sè",
            "meaning": "形容开怀大笑、笑容灿烂的样子。",
            "example": "听了这番妙语，众人无不齿牙春色。"
        },
        1687: {
            "pinyin": "chǐ yá yú lùn",
            "meaning": "微不足道的褒奖言辞，比喻随口称誉、不费力的奖励话。",
            "example": "不过是几句齿牙余论，何足挂齿。"
        },
        1688: {
            "pinyin": "chǐ bù dǒu sù",
            "meaning": "尺许长的布、斗内量得出的谷，形容财物极其微薄。",
            "example": "家贫如洗，也就只剩尺布斗粟的家当。"
        },
        1689: {
            "pinyin": "chǐ chuán piàn wǎ",
            "meaning": "一尺的椽木、一片瓦片，比喻极为简陋的房屋或微薄的产业。",
            "example": "他一生清贫，不过尺椽片瓦，聊以栖身。"
        },
        1690: {
            "pinyin": "chǐ cùn kě qǔ",
            "meaning": "虽然面积很小，却仍有可取之处，形容事物虽微却有其价值。",
            "example": "这块地虽小，却紧邻主干道，实为尺寸可取。"
        },
        1691: {
            "pinyin": "chǐ cùn zhī dì",
            "meaning": "极小的一块地方，多用来形容寸土寸金的地皮。",
            "example": "闹市之中，真可谓尺寸之地皆为高价。"
        },
        1692: {
            "pinyin": "chǐ cùn zhī gōng",
            "meaning": "极小的功劳或成绩。",
            "example": "他虽只是略尽尺寸之功，却也心安理得。"
        },
        1693: {
            "pinyin": "chǐ duǎn cùn cháng",
            "meaning": "尺有短、寸有所长，比喻人或事物各有所长，也各有不足。",
            "example": "人才使用要看到尺短寸长，扬长避短。"
        },
        1694: {
            "pinyin": "chǐ fú qiān lǐ",
            "meaning": "在一尺见方的画幅中表现出千里江山，比喻以小见大、气象宏阔。",
            "example": "这幅山水画真有尺幅千里的气势。"
        },
        1695: {
            "pinyin": "chǐ huò qiú shēn",
            "meaning": "尺蠖先屈后伸，比喻事物发展的曲折性，也比喻暂时受挫是为了更大的进取。",
            "example": "人生起伏本如尺蠖求伸，关键在于蓄势再发。"
        },
        1696: {
            "pinyin": "chǐ shù cùn hóng",
            "meaning": "泓：水深。泛指地方虽小，却有花木扶疏、泉水回环的清幽景致。",
            "example": "这处庭院尺树寸泓，自有一番雅趣。"
        },
        1697: {
            "pinyin": "chǐ shuǐ zhàng bō",
            "meaning": "一尺的水面却起丈高的波浪，比喻因小事而引起巨大的波澜或矛盾。",
            "example": "本是小小误会，却被炒成尺水丈波。"
        },
        1698: {
            "pinyin": "chǐ yǐn chuān dī, néng piāo yī yì",
            "meaning": "尺长的蚯蚓也能把堤岸穿透冲毁一城，比喻微小的因素若不重视，也会酿成大祸。",
            "example": "安全隐患切莫轻视，所谓尺蚓穿堤，能漂一邑。"
        },
        1699: {
            "pinyin": "chǐ yǒu suǒ duǎn, cùn yǒu suǒ cháng",
            "meaning": "比喻任何人或事物都有不足和长处。常用来劝人不要妄自菲薄或妄自尊大。",
            "example": "世间万物尺有所短，寸有所长，相互取长补短方能共进。"
        },
        1700: {
            "pinyin": "chǐ zé zhī ní",
            "meaning": "尺许见方的小水洼中的小鱼，比喻见识短浅、眼光局限之人。",
            "example": "若只局限一隅而自满，不过尺泽之鲵耳。"
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

    print(f"已为 1601–1700 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
