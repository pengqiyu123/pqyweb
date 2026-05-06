import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    enrich = {
        2001: {
            "pinyin": "cóng kuān fā luò",
            "meaning": "处理别人的过错时从宽发落，指处罚比较宽大。",
            "example": "考虑到他初犯又能认错，这次就从宽发落。"
        },
        2002: {
            "pinyin": "cóng lìng rú liú",
            "meaning": "听从命令像流水一样顺畅，形容部属执行命令非常迅速、毫不迟疑。",
            "example": "这支队伍训练有素，军令一下，人人从令如流。"
        },
        2003: {
            "pinyin": "cóng róng yìng duì",
            "meaning": "态度镇定、不慌不忙地加以应对。",
            "example": "面对媒体的尖锐提问，他始终从容应对。"
        },
        2004: {
            "pinyin": "cóng shàn rú dēng, cóng è rú bēng",
            "meaning": "走上善道如同登山一般艰难，走向罪恶却像山崩一样容易，比喻为善不易，从恶甚易。",
            "example": "古语云，从善如登，从恶如崩，做人要时刻警惕自己的言行。"
        },
        2005: {
            "pinyin": "cóng shàn rú liú",
            "meaning": "像流水那样顺势而下，比喻乐于接受别人善意的规劝。",
            "example": "一个真正的君子，必能从善如流，广纳谏言。"
        },
        2006: {
            "pinyin": "cóng sú jiù jiǎn",
            "meaning": "遵从习俗、力求简便，多指制度、仪节不尚繁琐。",
            "example": "这次婚礼从俗就简，却更显得朴素温馨。"
        },
        2007: {
            "pinyin": "cóng tiān ér jiàng",
            "meaning": "从天上降落下来，比喻事物突然出现或机会出乎意料地到来。",
            "example": "这份资助简直像从天而降，解了他们的燃眉之急。"
        },
        2008: {
            "pinyin": "cóng tiān ér xià",
            "meaning": "从天而降的另一种说法，形容事物突然到来或出现。",
            "example": "那场意外的成功并不是从天而下，而是长期积累的结果。"
        },
        2009: {
            "pinyin": "cóng xīn suǒ yù",
            "meaning": "随心所欲地去做自己想做的事，多用来形容不受拘束的自在状态。",
            "example": "他退休后终于可以从心所欲地安排自己的生活。"
        },
        2010: {
            "pinyin": "cóng yī ér zhōng",
            "meaning": "自始至终只归顺、坚持于一人或一事，形容忠贞不渝。",
            "example": "她对科研事业从一而终，几十年如一日。"
        },
        2011: {
            "pinyin": "cóng zhōng yú lì",
            "meaning": "在中间利用机会谋取私利。",
            "example": "他利用信息不对称从中渔利，终被严厉查处。"
        },
        2012: {
            "pinyin": "cóng zhōng zuò gěng",
            "meaning": "在事情中间从中作梗，暗中破坏或阻挠。",
            "example": "合作谈判一再受阻，显然有人从中作梗。"
        },
        2013: {
            "pinyin": "cōng míng cái zhì",
            "meaning": "聪慧的头脑和出众的才能。",
            "example": "凭借他的聪明才智，这点困难难不倒他。"
        },
        2014: {
            "pinyin": "cōng míng líng lì",
            "meaning": "形容人反应敏捷、机智伶俐。",
            "example": "这个孩子从小聪明伶俐，讨人喜欢。"
        },
        2015: {
            "pinyin": "cōng míng yī shì",
            "meaning": "一辈子都很聪明，多含“却在关键处糊涂”的感叹意味。",
            "example": "他聪明一世，却在这件事上栽了跟头。"
        },
        2016: {
            "pinyin": "cōng míng zhèng zhí",
            "meaning": "既聪明又正直，形容品行端正、头脑清明。",
            "example": "她为人聪明正直，在单位很有威信。"
        },
        2017: {
            "pinyin": "cōng míng zhì huì",
            "meaning": "聪慧而富有智慧，常用来称赞人的才智。",
            "example": "团队中既需要勤奋，也需要聪明智慧。"
        },
        2018: {
            "pinyin": "cū chá dàn fàn",
            "meaning": "粗茶淡饭，形容饮食简单、生活朴素。",
            "example": "他虽身居高位，日常不过粗茶淡饭。"
        },
        2019: {
            "pinyin": "cū fú luàn tóu",
            "meaning": "穿着粗布衣服、头发蓬乱，形容衣着简陋、不修边幅。",
            "example": "工地上的工人多是粗服乱头，却个个干劲十足。"
        },
        2020: {
            "pinyin": "cū tōng wén mò",
            "meaning": "对文章典籍略知一二，形容学识不深，只知粗浅。",
            "example": "我不过粗通文墨，这点意见仅供参考。"
        },
        2021: {
            "pinyin": "cū xīn dà yì",
            "meaning": "做事不细心、疏忽大意。",
            "example": "因为粗心大意，他又把重要文件弄错了。"
        },
        2022: {
            "pinyin": "cū xīn fú qì",
            "meaning": "粗鲁浮躁、心思不细，形容做事毛躁、不稳重。",
            "example": "做科研最忌粗心浮气，必须踏实严谨。"
        },
        2023: {
            "pinyin": "cū yī dàn fàn",
            "meaning": "粗布衣裳、简单饭食，形容生活俭朴。",
            "example": "即便事业有成，他仍保持粗衣淡饭的习惯。"
        },
        2024: {
            "pinyin": "cū yī lì shí",
            "meaning": "粗布衣裳、粗糙饭食，比喻生活清苦简朴。",
            "example": "创业初期他们粗衣粝食，却毫无怨言。"
        },
        2025: {
            "pinyin": "cū zhī dà yè",
            "meaning": "做事不求细致，只求大概，形容工作粗糙、疏忽细节。",
            "example": "工程设计不可粗枝大叶，否则后患无穷。"
        },
        2026: {
            "pinyin": "cū zhì làn zào",
            "meaning": "做工粗糙、制造马虎，形容产品质量极差或工作不负责任。",
            "example": "这批货明显粗制滥造，根本达不到标准。"
        },
        2027: {
            "pinyin": "cū zhōng yǒu xì",
            "meaning": "表面粗豪，内心细致，形容性格粗犷但做事细心。",
            "example": "别看他大大咧咧，其实粗中有细。"
        },
        2028: {
            "pinyin": "cù bù jí fáng",
            "meaning": "事情来得突然，来不及防备。",
            "example": "事故发生得猝不及防，让人措手不及。"
        },
        2029: {
            "pinyin": "cù xī tán xīn",
            "meaning": "拉近距离、挨着膝盖坐下谈心，形容亲切、深入地谈话。",
            "example": "师长常与年轻干部促膝谈心，了解他们的真实想法。"
        },
        2030: {
            "pinyin": "cù jí bù ān",
            "meaning": "形容局促不安、拘谨紧张的样子。",
            "example": "初次上台演讲，他难免踧踖不安。"
        },
        2031: {
            "pinyin": "cù hǎi fān bō",
            "meaning": "醋海：醋意之海，比喻嫉妒心很强。形容吃醋心情翻腾不平。",
            "example": "她见男友和别人说笑，心中不免醋海翻波。"
        },
        2032: {
            "pinyin": "cuān fáng yuè jǐ",
            "meaning": "翻房越脊，形容小偷翻屋越墙、偷偷摸摸出入。",
            "example": "那伙贼专门在夜里蹿房越脊行窃。"
        },
        2033: {
            "pinyin": "cuán méi cù é",
            "meaning": "双眉紧锁、额头深皱，形容忧愁不乐或思虑重重。",
            "example": "听到经济不景气的消息，他不由攒眉蹙额。"
        },
        2034: {
            "pinyin": "cuán sān jù wǔ",
            "meaning": "三三两两聚在一起，形容人数不多而聚集成群。",
            "example": "傍晚的广场上，人们攒三聚五地散步聊天。"
        },
        2035: {
            "pinyin": "cuàn duān nì jì",
            "meaning": "藏起行迹，不让人发现，形容躲躲藏藏、逃避追查。",
            "example": "他干了坏事后四处窜端匿迹，企图逃脱法律制裁。"
        },
        2036: {
            "pinyin": "cuàn wèi duó quán",
            "meaning": "夺取帝位和权力，多指以不正当手段夺权。",
            "example": "这位权臣妄图篡位夺权，最终众叛亲离。"
        },
        2037: {
            "pinyin": "cuī rén lèi xià",
            "meaning": "使人感动得流下眼泪。",
            "example": "这部纪录片许多情节都催人泪下。"
        },
        2038: {
            "pinyin": "cuī fēng xiàn zhèn",
            "meaning": "冲破敌锋、攻入阵地，形容英勇善战、所向披靡。",
            "example": "这支部队多次摧锋陷阵，屡建奇功。"
        },
        2039: {
            "pinyin": "cuī gāng wéi róu",
            "meaning": "把刚强变为柔顺，形容以柔克刚，转变对方态度。",
            "example": "她的真诚和耐心最终摧刚为柔，化解了对方的敌意。"
        },
        2040: {
            "pinyin": "cuī jiān xiàn zhèn",
            "meaning": "攻破坚固防御、深入敌阵，形容攻势猛烈、战绩显著。",
            "example": "在主力部队摧坚陷阵之下，敌军节节败退。"
        },
        2041: {
            "pinyin": "cuī kū lā xiǔ",
            "meaning": "摧折枯朽的树木，比喻力量极大，轻而易举就能摧毁对方。",
            "example": "在强大民意面前，一切阻挠不过摧枯拉朽。"
        },
        2042: {
            "pinyin": "cuī kū zhé fǔ",
            "meaning": "摧折枯朽之木、败坏腐朽之物，比喻轻易就能战胜腐朽势力。",
            "example": "这支新兴力量的崛起，对旧制度而言无异于摧枯折腐。"
        },
        2043: {
            "pinyin": "cuī lán zhé yù",
            "meaning": "摧折兰花和美玉，比喻摧残美好的人或事物，多指毁灭才华出众、品格高洁的人。",
            "example": "战争总是摧兰折玉，让无数青年才俊陨落。"
        },
        2044: {
            "pinyin": "cuī méi zhé yāo",
            "meaning": "低眉折腰，形容屈辱逢迎、阿谀奉承。",
            "example": "他宁可清贫也不愿摧眉折腰事权贵。"
        },
        2045: {
            "pinyin": "cuī shēn suì shǒu",
            "meaning": "身体粉碎、头颅破裂，比喻为某种事业或信念献出生命。",
            "example": "他们为保家卫国甘愿摧身碎首。"
        },
        2046: {
            "pinyin": "cuī xiàn kuò qīng",
            "meaning": "攻破敌人堡垒、清除残余势力，形容战局彻底扭转。",
            "example": "大军一路摧陷廓清，平定了整个地区。"
        },
        2047: {
            "pinyin": "cuī xīn pōu gān",
            "meaning": "把心肝剖开一样，形容极度悲痛或推心置腹的真情流露。",
            "example": "读到那段描写母爱的文字，真可谓摧心剖肝。"
        },
        2048: {
            "pinyin": "cuī zhé háo qiáng",
            "meaning": "打击、摧毁豪强势力。",
            "example": "新政重在摧折豪强，匡扶正义。"
        },
        2049: {
            "pinyin": "cuǐ càn duó mù",
            "meaning": "光彩夺目、十分耀眼。",
            "example": "夜空中烟花璀璨夺目，美不胜收。"
        },
        2050: {
            "pinyin": "cuì rào zhū wéi",
            "meaning": "翠色环绕、珠光围绕，形容装饰华丽、高贵富丽的景象。",
            "example": "宫殿周围翠绕珠围，尽显皇家气派。"
        },
        2051: {
            "pinyin": "cuì xiāo hóng jiǎn",
            "meaning": "翠色消退、红色减淡，形容花木凋残，也比喻美貌衰退或盛况不再。",
            "example": "园中花事已过，早已是翠消红减的景象。"
        },
        2052: {
            "pinyin": "cuì zhú huáng huā",
            "meaning": "青翠的竹子、金黄的花朵，形容景色清新幽美、富有田园情趣。",
            "example": "村口一带翠竹黄花，景色分外宜人。"
        },
        2053: {
            "pinyin": "cūn fū sú zǐ",
            "meaning": "乡村里的粗俗之人，比喻见识浅陋、不谙礼节的人。",
            "example": "他自谦不过村夫俗子，不敢与诸君并论高下。"
        },
        2054: {
            "pinyin": "cūn fū yě lǎo",
            "meaning": "乡间的男子和老人，多用作自谦，表示地位卑微或见识浅陋。",
            "example": "我等村夫野老，所言不过肺腑之言。"
        },
        2055: {
            "pinyin": "cūn yě pǐ fū",
            "meaning": "乡野间的普通男子，比喻身份卑微的百姓，多作自谦之辞。",
            "example": "他总说自己只是村野匹夫，却做成了大事业。"
        },
        2056: {
            "pinyin": "cún ér bù lùn",
            "meaning": "把材料记录下来而暂不加评论，多指保留争议问题以待再议。",
            "example": "对这些史料，先存而不论，以免妄下结论。"
        },
        2057: {
            "pinyin": "cún wáng ān wēi",
            "meaning": "关乎生存或灭亡、安宁或危险，形容形势极其重大严峻。",
            "example": "此战关系全局存亡安危，容不得半点疏忽。"
        },
        2058: {
            "pinyin": "cún wáng jì jué",
            "meaning": "保存未亡者，使断绝的继续下去，多指保护存活者、继承中断的宗族或文化。",
            "example": "修复古籍，是为了文化的存亡继绝。"
        },
        2059: {
            "pinyin": "cún wáng jué xù",
            "meaning": "生存与灭亡、断绝与延续，形容处在极其关键的存续关头。",
            "example": "在物种保护上，人类正面临存亡绝续的抉择。"
        },
        2060: {
            "pinyin": "cún wáng wèi bǔ",
            "meaning": "生死存亡尚不可预料，形容局势危急而结果难以判断。",
            "example": "战事吃紧，城中百姓存亡未卜。"
        },
        2061: {
            "pinyin": "cún xīn yǎng xìng",
            "meaning": "存养本心、修养性情，多指通过修身以保养德性。",
            "example": "他晚年潜心经典，只求存心养性。"
        },
        2062: {
            "pinyin": "cùn bù bù lí",
            "meaning": "一小步都不离开，形容时刻跟随或关系十分亲密。",
            "example": "护士寸步不离地守在病人身边。"
        },
        2063: {
            "pinyin": "cùn bù bù ràng",
            "meaning": "一点点地方也不肯相让，形容坚持立场、毫不退让。",
            "example": "在原则问题上，他寸步不让。"
        },
        2064: {
            "pinyin": "cùn bù nán xíng",
            "meaning": "连迈出一小步都很困难，比喻处境艰难或遭遇极大阻碍。",
            "example": "在重重限制之下，改革举措一时寸步难行。"
        },
        2065: {
            "pinyin": "cùn bù qiān lǐ",
            "meaning": "一步之间可达千里，比喻谋划得当、起点虽小却有极大发展。亦形容目光远大。",
            "example": "这次布局看似微小，却是寸步千里的长远之计。"
        },
        2066: {
            "pinyin": "cùn cǎo bù liú",
            "meaning": "连一寸草都不留下，形容破坏极为严重或扫荡彻底。",
            "example": "侵略者烧杀抢掠，所到之处寸草不留。"
        },
        2067: {
            "pinyin": "cùn cǎo bù shēng",
            "meaning": "连一寸草都长不出来，形容环境恶劣或破坏严重。",
            "example": "长期的过度开采，使这里几乎寸草不生。"
        },
        2068: {
            "pinyin": "cùn cǎo chūn huī",
            "meaning": "出自“谁言寸草心，报得三春晖”，比喻子女难以报答父母的深恩。",
            "example": "再多的付出，在父母恩情面前也只是寸草春晖。"
        },
        2069: {
            "pinyin": "cùn dì chǐ tiān",
            "meaning": "地窄如寸、天低如尺，形容空间狭小，活动范围很小。",
            "example": "在这寸地尺天的斗室里，他完成了巨著。"
        },
        2070: {
            "pinyin": "cùn jìn chǐ tuì",
            "meaning": "进一寸却退一尺，比喻一味退让、步步后退。",
            "example": "对无理要求若寸进尺退，只会助长对方气焰。"
        },
        2071: {
            "pinyin": "cùn lì bì dé",
            "meaning": "一丁点儿利益也要得到，形容极端贪婪或过于计较小利。",
            "example": "做生意若只知寸利必得，终难赢得口碑。"
        },
        2072: {
            "pinyin": "cùn liáng zhū chēng",
            "meaning": "用寸来量、用铢来称，比喻斤斤计较、繁琐苛刻地计算。",
            "example": "他对下属功过寸量铢称，弄得人心惶惶。"
        },
        2073: {
            "pinyin": "cùn mù cén lóu",
            "meaning": "一寸长的木头和高楼相比，比喻基准不同就无法比较，也形容差距悬殊。",
            "example": "拿初学者和大师相比，无异于寸木岑楼。"
        },
        2074: {
            "pinyin": "cùn nán chǐ nǚ",
            "meaning": "小男孩、小女孩，多指年幼的子女。",
            "example": "他告老还乡，只带着一双寸男尺女。"
        },
        2075: {
            "pinyin": "cùn sī bàn sù",
            "meaning": "一寸丝、一半粒谷，形容财物极少，也比喻丝毫的恩惠或利益。",
            "example": "他从不贪图别人寸丝半粟的好处。"
        },
        2076: {
            "pinyin": "cùn sī bù guà",
            "meaning": "身上连一寸丝线都没有，形容赤身裸体；也指一无所有。",
            "example": "古画中婴儿多是寸丝不挂的形象。"
        },
        2077: {
            "pinyin": "cùn tián chǐ zhái",
            "meaning": "极小的田地和宅院，形容家产微薄或土地狭小。",
            "example": "他只留下一点寸田尺宅，却留下了好名声。"
        },
        2078: {
            "pinyin": "cùn tiě shā rén",
            "meaning": "一小块铁也可以杀人，比喻力量虽小却足以造成重大后果。",
            "example": "这些谣言看似无形，却是可以寸铁杀人的利器。"
        },
        2079: {
            "pinyin": "cùn tiě zài shǒu",
            "meaning": "手中握有小小的武器，比喻虽力量不大却足以自保或反击。",
            "example": "面对压力，只要心中有理，便如寸铁在手。"
        },
        2080: {
            "pinyin": "cùn tǔ bì zhēng",
            "meaning": "一寸土地也要争夺，形容保卫领土的决心极其坚定。",
            "example": "在主权问题上，他们寸土必争。"
        },
        2081: {
            "pinyin": "cùn tǔ bù ràng",
            "meaning": "一寸领土也不退让，形容坚决维护领土完整。",
            "example": "对外谈判中，他态度强硬，寸土不让。"
        },
        2082: {
            "pinyin": "cùn tǔ chǐ dì",
            "meaning": "极小的一块土地，形容土地弥足珍贵或空间狭窄。",
            "example": "在寸土尺地的老城区，要拓宽道路并不容易。"
        },
        2083: {
            "pinyin": "cùn xīn qiān gǔ",
            "meaning": "寸心：一片心意；千古：极长久的时间。比喻内心自知得失是非，也终能为后世所明鉴。",
            "example": "是非功过，唯有寸心千古自知。"
        },
        2084: {
            "pinyin": "cùn yīn chǐ bì",
            "meaning": "一寸光阴和一尺美玉，相比之下光阴更为宝贵，劝人珍惜时间。",
            "example": "古人常以寸阴尺璧相喻，提醒后学惜时。"
        },
        2085: {
            "pinyin": "cùn yīn ruò suì",
            "meaning": "一寸光阴好像一年那样宝贵，形容时间极其可贵。",
            "example": "备考期间，他深感寸阴若岁。"
        },
        2086: {
            "pinyin": "cùn yīn shì xī",
            "meaning": "每一寸时光都应珍惜，形容时间非常宝贵。",
            "example": "少年当知寸阴是惜，不可虚度年华。"
        },
        2087: {
            "pinyin": "cùn zhǐ cè yuān",
            "meaning": "用一寸长的手指去探测深渊，比喻学识浅薄却妄图探究深奥道理。",
            "example": "若不系统学习，便妄议大道，无异于寸指测渊。"
        },
        2088: {
            "pinyin": "cùn yǒu suǒ cháng",
            "meaning": "就连一寸长的东西也有它的长处，比喻事物各有所长、人无全无是处。",
            "example": "用人所长，要看到每个人寸有所长的一面。"
        },
        2089: {
            "pinyin": "cuō tuó rì yuè",
            "meaning": "白白消磨光阴，形容虚度时日。",
            "example": "年轻时若只知玩乐，难免蹉跎日月。"
        },
        2090: {
            "pinyin": "cuō tuó suì yuè",
            "meaning": "虚度年华，白白浪费宝贵的岁月。",
            "example": "他幡然悔悟，不愿再蹉跎岁月。"
        },
        2091: {
            "pinyin": "cuō tuó zì wù",
            "meaning": "因虚度年华而耽误了自己的人生。",
            "example": "若沉迷享乐，终将蹉跎自误。"
        },
        2092: {
            "pinyin": "cuō shǒu dùn jiǎo",
            "meaning": "一边搓手一边顿脚，形容焦急懊恼的样子。",
            "example": "看着机会擦肩而过，他急得搓手顿脚。"
        },
        2093: {
            "pinyin": "cuō tǔ fén xiāng",
            "meaning": "抓一把土当香焚烧，比喻以极其简陋的供品表达虔诚之心。",
            "example": "山民撮土焚香，祈求风调雨顺。"
        },
        2094: {
            "pinyin": "cuō yán rù huǒ",
            "meaning": "把盐撒入火中，比喻在矛盾或怒气上再加刺激，使之更为激烈。",
            "example": "在双方争执时说风凉话，无异于撮盐入火。"
        },
        2095: {
            "pinyin": "cuò huǒ jī xīn",
            "meaning": "把火放在柴堆旁，比喻隐患极大、危险随时可能爆发。",
            "example": "若任由矛盾激化，无异于厝火积薪。"
        },
        2096: {
            "pinyin": "cuò shǒu bù jí",
            "meaning": "事情突然发生，来不及处理或应付。",
            "example": "事故来得太快，让人一时措手不及。"
        },
        2097: {
            "pinyin": "cuò zhì yù rú",
            "meaning": "安排处理事情十分从容，形容办事不慌不乱、应付裕如。",
            "example": "面对复杂局面，他仍能措置裕如。"
        },
        2098: {
            "pinyin": "cuò cǎi lòu jīn",
            "meaning": "色彩交错、雕刻精美，比喻文章辞藻华丽或装饰精致。",
            "example": "这篇骈文错彩镂金，极尽华美之能事。"
        },
        2099: {
            "pinyin": "cuò luò bù qí",
            "meaning": "高低参差、不很整齐，形容排列不齐或分布无规则。",
            "example": "远处的房屋错落不齐，却别有一番风味。"
        },
        2100: {
            "pinyin": "cuò luò yǒu zhì",
            "meaning": "参差不齐却富有情趣，形容布置有层次、有情调。",
            "example": "庭院中花木错落有致，颇见匠心。"
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

    print(f"已为 2001–2100 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
