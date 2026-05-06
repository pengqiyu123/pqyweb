import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 将 3601–3700 号成语的详细信息补充到 enrich 字典中
    enrich = {
        3601: {
            "pinyin": "fáng wēi lǜ yuǎn",
            "meaning": "在事情还处于细微苗头时就加以防范，并从长远角度加以考虑，以免酿成大祸。",
            "example": "治国理政当防微虑远，不能只顾眼前利益。"
        },
        3602: {
            "pinyin": "fáng yì rú chéng",
            "meaning": "对别人的居心动机提高警惕，防备之心像城墙一样牢固，形容十分谨慎小心。",
            "example": "与人交往既要坦诚，也要防意如城，不可全无戒备。"
        },
        3603: {
            "pinyin": "fáng gōng hài néng",
            "meaning": "妨碍别人的功劳，损害别人的才能，多指出于嫉妒而打压贤能之人。",
            "example": "用人若妨功害能，只会让真正的人才心灰意冷。"
        },
        3604: {
            "pinyin": "fàng cháng xiàn diào dà yú",
            "meaning": "比喻做事时先作较大投入或暂时忍受损失，以便日后获得更大的利益。",
            "example": "前期让利只是放长线钓大鱼的策略。"
        },
        3605: {
            "pinyin": "fàng dàng bù jī",
            "meaning": "行为放纵，不受礼法约束，性情轻狂不羁。",
            "example": "年轻时他放荡不羁，后来才渐渐收敛。"
        },
        3606: {
            "pinyin": "fàng diāo sā pō",
            "meaning": "故意耍赖、无理取闹，仗势欺人。",
            "example": "他们在人群中放刁撒泼，严重扰乱了秩序。"
        },
        3607: {
            "pinyin": "fàng fàn liú chuò",
            "meaning": "吃饭喝汤毫无节制，声音粗豪，形容豪放不拘小节的吃喝样子。",
            "example": "一群壮汉围桌而坐，放饭流歠，好不痛快。"
        },
        3608: {
            "pinyin": "fàng gē zòng jiǔ",
            "meaning": "放声高歌，纵情饮酒，形容豪放畅快的生活情景。",
            "example": "古人常在月下放歌纵酒，寄托胸中豪情。"
        },
        3609: {
            "pinyin": "fàng hǔ guī shān",
            "meaning": "把老虎放回山林，比喻放回恶人或敌人，让其有机会再度为害。",
            "example": "对屡教不改的恶徒若轻易放过，无异于放虎归山。"
        },
        3610: {
            "pinyin": "fàng hǔ zì wèi",
            "meaning": "放出老虎作为自己的护卫，比喻倚仗强暴之人或恶势力来保护自己，终有反噬之患。",
            "example": "依附黑恶势力谋利，不过是放虎自卫，后患无穷。"
        },
        3611: {
            "pinyin": "fàng làng xíng hái",
            "meaning": "形骸：肢体、形迹。形容行为不受礼法拘束，放纵不羁。",
            "example": "他性情疏阔，常被人说是放浪形骸。"
        },
        3612: {
            "pinyin": "fàng niú guī mǎ",
            "meaning": "把战马役牛放回原处，多用来比喻战争结束，军队解甲归田。",
            "example": "烽烟既息，百姓得以放牛归马、安居乐业。"
        },
        3613: {
            "pinyin": "fàng pì xié chǐ",
            "meaning": "放纵、邪僻、奢侈，形容为非作歹、纵欲无度的行为。",
            "example": "统治者若放辟邪侈，终将失去民心。"
        },
        3614: {
            "pinyin": "fàng rèn zì liú",
            "meaning": "听任事物自然发展，不加约束或引导，多含贬义。",
            "example": "对子女教育切不可放任自流。"
        },
        3615: {
            "pinyin": "fàng xià tú dāo, lì dì chéng fó",
            "meaning": "比喻只要立刻改恶从善，就可以成为好人。",
            "example": "哪怕他曾误入歧途，只要悔过自新，也能放下屠刀，立地成佛。"
        },
        3616: {
            "pinyin": "fàng yán qiǎn cí",
            "meaning": "放：毫无顾忌；遣：运用。说话用词毫无拘束，直率而不加修饰。",
            "example": "他向来放言遣辞，想到什么就说什么。"
        },
        3617: {
            "pinyin": "fàng zhī sì hǎi ér jiē zhǔn",
            "meaning": "把某个道理放到世界任何地方都适用，形容真理具有普遍性。",
            "example": "诚实守信的原则放之四海而皆准。"
        },
        3618: {
            "pinyin": "fàng zòng chí dàng",
            "meaning": "行为放纵散漫，毫无约束。",
            "example": "长期放纵驰荡的生活最终让他一事无成。"
        },
        3619: {
            "pinyin": "fēi cháng zhī móu",
            "meaning": "在非常时期采取的非常之计，也指高明而特别的谋略。",
            "example": "要扭转困局，必须有非常之谋。"
        },
        3620: {
            "pinyin": "fēi chí zhōng wù",
            "meaning": "不是池塘里平常的东西，比喻有大才大志，将来必有大作为的人。",
            "example": "这孩子聪慧过人，绝非池中物。"
        },
        3621: {
            "pinyin": "fēi cǐ jí bǐ",
            "meaning": "不是这个就是那个，二者必取其一，形容非此即彼、不能兼得。",
            "example": "在原则问题上，态度应当鲜明，非此即彼。"
        },
        3622: {
            "pinyin": "fēi fèn zhī cái",
            "meaning": "指本分之外不应得的财物，多指不义之财。",
            "example": "他从不贪图非分之财，行事光明磊落。"
        },
        3623: {
            "pinyin": "fēi fèn zhī xiǎng",
            "meaning": "超出本分、地位之外的奢望或妄念。",
            "example": "与其生非分之想，不如脚踏实地做好当下。"
        },
        3624: {
            "pinyin": "fēi lǘ fēi mǎ",
            "meaning": "既不像驴又不像马，比喻事物不伦不类，界限不清。",
            "example": "这篇文章文体杂糅，颇有非驴非马之感。"
        },
        3625: {
            "pinyin": "fēi qīn fēi gù",
            "meaning": "既非亲属又非旧交，比喻彼此关系疏远。",
            "example": "他不过是我非亲非故的同乡，谈不上多熟。"
        },
        3626: {
            "pinyin": "fēi tóng ér xì",
            "meaning": "不是小孩子的游戏，比喻事情严肃认真，不容儿戏。",
            "example": "安全生产非同儿戏，丝毫马虎不得。"
        },
        3627: {
            "pinyin": "fēi tóng xiǎo kě",
            "meaning": "事情重大，不可以等闲视之。",
            "example": "这起事故影响深远，实在非同小可。"
        },
        3628: {
            "pinyin": "fēi wǒ zú lèi",
            "meaning": "不属于我们的族类，后多指立场、信仰等根本不同的一类人。",
            "example": "若总是以非我族类的眼光看人，难免偏狭。"
        },
        3629: {
            "pinyin": "fēi xī shì jīn",
            "meaning": "不再是从前的样子，指今昔大不相同。",
            "example": "旧城改造后已非昔是今，让人有些恍惚。"
        },
        3630: {
            "pinyin": "fēi yì rén rèn",
            "meaning": "并非别人的责任，多用来表示这是自己分内该做的事。",
            "example": "守护家园非异人任，而是我们每个人的义务。"
        },
        3631: {
            "pinyin": "fēi yì xiāng gān",
            "meaning": "本非有意，却彼此牵连发生关系，多指意料之外的牵扯。",
            "example": "这桩旧案竟与他非意相干，实在出人意料。"
        },
        3632: {
            "pinyin": "fēi duǎn liú cháng",
            "meaning": "散布、传递别人的短处和流言，比喻造谣生事。",
            "example": "职场中最忌蜚短流长，应当以事实为据。"
        },
        3633: {
            "pinyin": "fēi chú wǎn sù",
            "meaning": "急速运送草料粮食支援前线，比喻迅速支援、供给。",
            "example": "灾情发生后，各地物资飞刍挽粟般运来。"
        },
        3634: {
            "pinyin": "fēi duǎn liú cháng",
            "meaning": "同“蜚短流长”，指到处散布毫无根据的流言蜚语。",
            "example": "网络空间更要杜绝飞短流长，维护清朗环境。"
        },
        3635: {
            "pinyin": "fēi dùn míng gāo",
            "meaning": "远走高飞、隐遁起来以示高洁，形容避世自守名节。",
            "example": "乱世之中，有人选择飞遁鸣高，不与权贵同流。"
        },
        3636: {
            "pinyin": "fēi é fù huǒ",
            "meaning": "飞蛾往火上扑，比喻明知危险却偏要冒险送死或投身其中。",
            "example": "他明知那是圈套，却仍如飞蛾赴火一般闯了进去。"
        },
        3637: {
            "pinyin": "fēi é tóu huǒ",
            "meaning": "与“飞蛾赴火”相近，比喻自取灭亡或自投罗网。",
            "example": "面对高利骗局，盲目跟风无异于飞蛾投火。"
        },
        3638: {
            "pinyin": "fēi gé liú dān",
            "meaning": "高阁连廊，彩绘丹漆流光溢彩，形容楼阁建筑壮丽辉煌。",
            "example": "宫殿飞阁流丹，气势宏伟。"
        },
        3639: {
            "pinyin": "fēi hóng yìn xuě",
            "meaning": "大雁飞过在雪地留下的印迹，比喻事物经过后留下可寻的痕迹，亦形容书法飘逸。",
            "example": "他的字势若飞鸿印雪，洒脱自然。"
        },
        3640: {
            "pinyin": "fēi huáng téng dá",
            "meaning": "像神兽飞黄一样腾空而起，比喻飞速升迁、发迹得志。",
            "example": "他凭借机遇与实力飞黄腾达。"
        },
        3641: {
            "pinyin": "fēi lái hèng huò",
            "meaning": "突如其来的意外灾祸。",
            "example": "一场车祸的飞来横祸打破了原本平静的生活。"
        },
        3642: {
            "pinyin": "fēi niǎo jīng shé",
            "meaning": "鸟被惊起、蛇被惊走，比喻文字笔势飞动; 也形容惊慌逃避的情景。",
            "example": "这幅字用笔飞鸟惊蛇，极富动感。"
        },
        3643: {
            "pinyin": "fēi niǎo yī rén",
            "meaning": "飞鸟亲近依附在人身旁，比喻性情温和、令人亲近。",
            "example": "这位老者和蔼可亲，院中的飞鸟依人。"
        },
        3644: {
            "pinyin": "fēi péng suí fēng",
            "meaning": "飞蓬随风飘荡，比喻身世飘零或行踪无定。",
            "example": "多年在外奔波，他只觉一生如飞蓬随风。"
        },
        3645: {
            "pinyin": "fēi qín zǒu shòu",
            "meaning": "天上飞的鸟、地上走的兽，泛指各种飞禽走兽。",
            "example": "山林间飞禽走兽出没其间，生机盎然。"
        },
        3646: {
            "pinyin": "fēi shā zǒu lì",
            "meaning": "风吹沙土、石子乱飞，形容风势猛烈。",
            "example": "大风呼啸，沙尘漫天，真是飞沙走砾。"
        },
        3647: {
            "pinyin": "fēi shā zǒu shí",
            "meaning": "沙石被风卷起飞舞，形容风势极大、环境恶劣。",
            "example": "戈壁滩常有飞沙走石的天气。"
        },
        3648: {
            "pinyin": "fēi shēng téng shí",
            "meaning": "名声飞扬而事实也足以证明，形容名实相符、声望很高。",
            "example": "这位老艺术家早已飞声腾实，广受敬重。"
        },
        3649: {
            "pinyin": "fēi xióng rù mèng",
            "meaning": "古代以飞熊入梦为生贵子、得贤臣的祥兆。",
            "example": "史书记载，周文王曾飞熊入梦，象征将得贤才辅佐。"
        },
        3650: {
            "pinyin": "fēi yán zǒu bì",
            "meaning": "轻功高妙，可以飞上屋檐、踏壁而行，比喻身手矫健或武艺高强。",
            "example": "武侠小说中常写豪侠飞檐走壁，出入如风。"
        },
        3651: {
            "pinyin": "fēi yáng bá hù",
            "meaning": "形容气焰嚣张、专横跋扈。",
            "example": "他因一时得势而飞扬跋扈，终致众叛亲离。"
        },
        3652: {
            "pinyin": "fēi yīng zǒu gǒu",
            "meaning": "使鹰捕鸟、驱狗追兽，形容贵族豪门的游猎生活。",
            "example": "他整日飞鹰走狗，荒废了学业。"
        },
        3653: {
            "pinyin": "fēi yún chè diàn",
            "meaning": "像云飞、电掣一样迅疾，形容速度极快。",
            "example": "高铁飞云掣电般掠过原野。"
        },
        3654: {
            "pinyin": "fēi zāi hèng huò",
            "meaning": "意外降临的灾祸。",
            "example": "谁也没想到这一连串飞灾横祸会接踵而至。"
        },
        3655: {
            "pinyin": "fēi zhēn zǒu xiàn",
            "meaning": "针飞线走，形容女工做针线活的娴熟敏捷。",
            "example": "母亲飞针走线，一会儿就缝好了一件衣裳。"
        },
        3656: {
            "pinyin": "fěi fěi yì yì",
            "meaning": "出自《诗经》，形容仪容庄重、恭敬谨慎的样子。",
            "example": "队伍行进时匪匪翼翼，军容严整。"
        },
        3657: {
            "pinyin": "féi dùn míng gāo",
            "meaning": "肥遁：优游避世。指退隐不仕以保全名节。",
            "example": "他不愿同流合污，选择肥遁鸣高。"
        },
        3658: {
            "pinyin": "féi mǎ qīng qiú",
            "meaning": "肥壮的马、轻暖的皮衣，形容生活豪华优裕。",
            "example": "达官贵人多骑肥马轻裘，出入显赫。"
        },
        3659: {
            "pinyin": "féi tóu dà ěr",
            "meaning": "头大耳肥，形容人富态或庸碌。",
            "example": "画中人物肥头大耳，颇具讽刺意味。"
        },
        3660: {
            "pinyin": "fěi bàng zhī mù",
            "meaning": "古代朝廷设置的让百姓书写意见、直言诽谤的木柱，比喻广开言路、纳谏之举。",
            "example": "若能立下诽谤之木，多听逆耳之言，方能改过自新。"
        },
        3661: {
            "pinyin": "fěi yù zài sú",
            "meaning": "毁谤和称誉都出自民间，比喻人的声望、口碑取决于百姓评价。",
            "example": "为官者当知诽誉在俗，真正的考验在民心。"
        },
        3662: {
            "pinyin": "fěi rán chéng zhāng",
            "meaning": "文章文采斐然，结构成章，比喻言辞、事理井然有序。",
            "example": "他的演讲斐然成章，条理分明。"
        },
        3663: {
            "pinyin": "fěi shí fěi xí",
            "meaning": "不是像石头和席子那样容易改变，比喻志向或约定坚定不移。",
            "example": "他对学术理想矢志不渝，可谓匪石匪席。"
        },
        3664: {
            "pinyin": "fěi yí fěi huì",
            "meaning": "既不粗野也不薄情，形容人品温厚、行为合礼。",
            "example": "他待人匪夷匪惠，既有原则又不失温和。"
        },
        3665: {
            "pinyin": "fěi yí suǒ sī",
            "meaning": "不是一般人所能想到的，形容事物非常奇特或离奇。",
            "example": "这起案件的手法真是匪夷所思。"
        },
        3666: {
            "pinyin": "fěi yī zhāo xī",
            "meaning": "并非一朝一夕，比喻形成某种局面经历了较长时间。",
            "example": "问题的积累匪伊朝夕，解决也需要耐心。"
        },
        3667: {
            "pinyin": "fěi shí bó yī",
            "meaning": "饭食菲薄、衣着单薄，形容生活清贫或克己节俭。",
            "example": "他宁愿菲食薄衣，也要资助贫困学生。"
        },
        3668: {
            "pinyin": "fèi fēi qí zhǔ",
            "meaning": "像狗那样乱叫却不知该对谁叫，比喻攻击、指责对象搞错，或仆从不忠。",
            "example": "不分青红皂白地指责好人，无异于吠非其主。"
        },
        3669: {
            "pinyin": "fèi xíng fèi shēng",
            "meaning": "对着形状乱叫、跟着声音乱叫，比喻人不辨是非、随声附和。",
            "example": "对于舆论热点要冷静分析，切勿吠形吠声。"
        },
        3670: {
            "pinyin": "fèi yǐng fèi shēng",
            "meaning": "对影子和声音乱叫，比喻捕风捉影地攻击别人。",
            "example": "一些评论只是吠影吠声，经不起推敲。"
        },
        3671: {
            "pinyin": "fèi huà lián piān",
            "meaning": "废话一篇接一篇，形容说话空洞冗长、没有实质内容。",
            "example": "报告若是废话连篇，只会让人失去耐心。"
        },
        3672: {
            "pinyin": "fèi qǐn wàng shí",
            "meaning": "顾不得睡觉和吃饭，形容十分用功或工作极其努力。",
            "example": "科研人员为攻克难题废寝忘食。"
        },
        3673: {
            "pinyin": "fèi rán ér fǎn",
            "meaning": "兴致全无地返回，形容失望而归。",
            "example": "展会规模不如预期，他只得废然而返。"
        },
        3674: {
            "pinyin": "fèi shū ér tàn",
            "meaning": "放下书本发出感叹，形容读书有感或触动很深。",
            "example": "读到悲壮处，他不禁废书而叹。"
        },
        3675: {
            "pinyin": "fèi wén rèn wǔ",
            "meaning": "废弃文教而任用武力，形容只尚武力、不重文化。",
            "example": "一个社会若废文任武，终究难免粗鄙。"
        },
        3676: {
            "pinyin": "fèi fǔ zhī yán",
            "meaning": "出自肺腑的真心话，多指真诚恳切的劝告。",
            "example": "老师的肺腑之言，他一直铭记在心。"
        },
        3677: {
            "pinyin": "fèi shí fēng qīng",
            "meaning": "敢于进谏、直陈利害，使政治风气清明。",
            "example": "只有鼓励肺石风清，才能形成良好的从政环境。"
        },
        3678: {
            "pinyin": "fèi fǎn yíng tiān",
            "meaning": "像沸水翻腾、声音充满天空，形容喧闹纷乱到极点。",
            "example": "球场上加油声沸反盈天。"
        },
        3679: {
            "pinyin": "fèi fèi yáng yáng",
            "meaning": "像沸水一样翻滚扬溅，形容议论纷纷、声势浩大。",
            "example": "这件事在网上闹得沸沸扬扬。"
        },
        3680: {
            "pinyin": "fèi lì láo xīn",
            "meaning": "既耗费力气又劳神费心，形容付出的辛劳很多。",
            "example": "这次筹备工作着实费力劳心。"
        },
        3681: {
            "pinyin": "fèi jìn xīn jī",
            "meaning": "用尽心思和计谋，形容绞尽脑汁想办法。",
            "example": "为了挽回损失，他费尽心机。"
        },
        3682: {
            "pinyin": "fēn bēng lí xī",
            "meaning": "四处崩溃、分裂瓦解，形容国家或集团严重分裂。",
            "example": "内患外敌并起，政权终于分崩离析。"
        },
        3683: {
            "pinyin": "fēn bié bù jū",
            "meaning": "分开居住，各在一处。",
            "example": "兄弟长大后分别部居，各自成家立业。"
        },
        3684: {
            "pinyin": "fēn chāi duàn dài",
            "meaning": "折断同心的头钗、扯断相赠的衣带，比喻恋人或夫妻被迫分离。",
            "example": "乱世之中，不知多少佳人经历分钗断带之苦。"
        },
        3685: {
            "pinyin": "fēn chāi pò jìng",
            "meaning": "分拆头钗、打碎圆镜，比喻夫妻、恋人离散。",
            "example": "战乱使无数家庭分钗破镜，天各一方。"
        },
        3686: {
            "pinyin": "fēn cùn zhī mò",
            "meaning": "事情最细微末节的部分。",
            "example": "他连分寸之末也要计较得一清二楚。"
        },
        3687: {
            "pinyin": "fēn dào yáng biāo",
            "meaning": "各走各的道路，骑马扬鞭而去，比喻目标不同，各奔前程。",
            "example": "理念不合的伙伴终究会分道扬镳。"
        },
        3688: {
            "pinyin": "fēn fēng pī liú",
            "meaning": "船行极快，仿佛把风分开、水劈开，形容速度飞快。",
            "example": "快艇分风劈流，在江面疾驰。"
        },
        3689: {
            "pinyin": "fēn gān gòng kǔ",
            "meaning": "共同分享甘甜，也一起承受苦难，形容患难与共的深厚情谊。",
            "example": "多年的分甘共苦，让他们结下了深厚友谊。"
        },
        3690: {
            "pinyin": "fēn gān jué shǎo",
            "meaning": "与人分享甘甜的情况极少，比喻只想独享好处。",
            "example": "若只顾自己享乐、分甘绝少，终究不得人心。"
        },
        3691: {
            "pinyin": "fēn háo bù shuǎng",
            "meaning": "连一丝一毫都不差错，形容极其准确。",
            "example": "他对细节的把握可谓分毫不爽。"
        },
        3692: {
            "pinyin": "fēn háo xī lí",
            "meaning": "把很细微的差别都加以分析，形容区分得极为精细。",
            "example": "做学问要能分毫析厘，不能含糊其辞。"
        },
        3693: {
            "pinyin": "fēn huà wǎ jiě",
            "meaning": "先分裂，再瓦解，形容使敌对力量逐渐分散、解体。",
            "example": "他们通过政策感化，实现了对敌军的分化瓦解。"
        },
        3694: {
            "pinyin": "fēn jīn bāi liǎng",
            "meaning": "把一斤再掰成两半来算，比喻过分计较、斤斤计较。",
            "example": "做朋友不必分斤掰两，太计较只会伤感情。"
        },
        3695: {
            "pinyin": "fēn jū yì cuàn",
            "meaning": "住处分开、炉灶各异，比喻家庭成员分家另过。",
            "example": "兄弟们因琐事分居异爨，令人唏嘘。"
        },
        3696: {
            "pinyin": "fēn lù yáng biāo",
            "meaning": "在岔路口各自扬鞭而去，比喻分手走各自的人生道路。",
            "example": "毕业后同学们分路扬镳，天各一方。"
        },
        3697: {
            "pinyin": "fēn máo liè tǔ",
            "meaning": "按葱茅分封诸侯、裂土建国，形容把土地分给属下。",
            "example": "古代帝王往往分茅裂土，以巩固统治。"
        },
        3698: {
            "pinyin": "fēn mén bié hù",
            "meaning": "按种类或派别各立门户，形容分化成许多小团体。",
            "example": "学术界不宜过度分门别户，影响交流。"
        },
        3699: {
            "pinyin": "fēn mén bié lèi",
            "meaning": "按门类区别归纳，形容分类细致有序。",
            "example": "图书馆将资料分门别类，便于查找。"
        },
        3700: {
            "pinyin": "fēn miǎo bì zhēng",
            "meaning": "连一分一秒都力求抓紧，形容非常珍惜时间。",
            "example": "备考阶段他分秒必争，努力提升自己。"
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

    print(f"已为 3601–3700 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
