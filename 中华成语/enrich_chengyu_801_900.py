import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 为 801–900 条成语添加拼音、释义和例句
    enrich = {
        # TODO: 填充 801–900 号成语的详细信息
        801: {
            "pinyin": "bīng wēi jiàng guǎ",
            "meaning": "兵力单薄、将领寥寥，形容一方兵少势弱。",
            "example": "敌军众多，我军兵微将寡，只能据险而守。"
        },
        802: {
            "pinyin": "bīng wú cháng shì",
            "meaning": "用兵的态势没有固定模式，要因时因势而变。",
            "example": "兵无常势，善战者总能随机应变。"
        },
        803: {
            "pinyin": "bīng xíng guǐ dào",
            "meaning": "用兵要采用诡秘多变的策略，出其不意制胜。",
            "example": "孙子提倡兵行诡道，以奇取胜。"
        },
        804: {
            "pinyin": "bīng zài qí jǐng",
            "meaning": "兵刃已临颈项，比喻危险迫在眉睫。",
            "example": "若再不撤军，形势就要兵在其颈了。"
        },
        805: {
            "pinyin": "bǐng qì níng shén",
            "meaning": "抑制呼吸，集中精神，形容十分专注或紧张。",
            "example": "大家屏气凝神，等待裁判宣布结果。"
        },
        806: {
            "pinyin": "bǐng qì liǎn xī",
            "meaning": "屏住呼吸，收敛气息，形容格外专注或紧张。",
            "example": "观众屏气敛息，看着最后一球的落点。"
        },
        807: {
            "pinyin": "bǐng shēng xī qì",
            "meaning": "压低声音，不敢大声出气，形容极为小心谨慎或害怕。",
            "example": "一进病房，大家都屏声息气，生怕惊动病人。"
        },
        808: {
            "pinyin": "bǐng bǐ zhí shū",
            "meaning": "执笔如实记载，不加掩饰，形容记述真实、公正。",
            "example": "史官秉笔直书，将当时的是非功过一一记下。"
        },
        809: {
            "pinyin": "bǐng gōng bàn lǐ",
            "meaning": "秉持公心处理事务。",
            "example": "他向来秉公办理，从不徇私情。"
        },
        810: {
            "pinyin": "bǐng gōng wú sī",
            "meaning": "一切按公道行事，没有一点私心。",
            "example": "只有真正秉公无私，才能让群众心服口服。"
        },
        811: {
            "pinyin": "bǐng yào zhí běn",
            "meaning": "抓住事物的要点和根本，不为枝节所扰。",
            "example": "治学要秉要执本，先把基础问题弄清楚。"
        },
        812: {
            "pinyin": "bǐng zhú dài dàn",
            "meaning": "点着蜡烛等待天亮，形容通宵不眠地工作或商议。",
            "example": "为定下改革方案，他们几夜秉烛待旦。"
        },
        813: {
            "pinyin": "bǐng zhú yè yóu",
            "meaning": "点着蜡烛在夜间游赏，比喻及时行乐或珍惜光阴。",
            "example": "同窗久别重逢，便相约秉烛夜游，畅叙旧情。"
        },
        814: {
            "pinyin": "bǐng zhú yè yóu",
            "meaning": "与“秉烛夜游”同，指在夜间行乐，也比喻及时行乐。",
            "example": "诗中感叹人生苦短，不如炳烛夜游。"
        },
        815: {
            "pinyin": "bǐng xìng nán yí",
            "meaning": "人的本性难以改变。",
            "example": "他为人急躁，多年难改，真是禀性难移。"
        },
        816: {
            "pinyin": "bìng bìng wāi wāi",
            "meaning": "形容人身体虚弱、多病无力的样子。",
            "example": "他小时候病病歪歪，常年往医院跑。"
        },
        817: {
            "pinyin": "bìng cóng kǒu rù",
            "meaning": "疾病多由饮食不慎而引起，也比喻祸患往往从言语或入口处产生。",
            "example": "医生再三叮嘱，病从口入，一定要注意饮食卫生。"
        },
        818: {
            "pinyin": "bìng gǔ zhī lí",
            "meaning": "形容人病得非常消瘦，瘦得只剩皮包骨。",
            "example": "他长期卧病在床，已经病骨支离。"
        },
        819: {
            "pinyin": "bìng jí luàn tóu yī",
            "meaning": "病情危急时胡乱求医，比喻情急之下乱想办法。",
            "example": "投资不能像病急乱投医那样盲目跟风。"
        },
        820: {
            "pinyin": "bìng mín gǔ guó",
            "meaning": "使百姓多病，使国家受毒害，比喻残害百姓、祸国殃民。",
            "example": "贪官污吏盘剥百姓，简直是病民蛊国。"
        },
        821: {
            "pinyin": "bìng mó chán shēn",
            "meaning": "好像疾病的魔鬼缠绕在身上，形容疾病缠身、久治不愈。",
            "example": "他多年病魔缠身，但始终乐观面对生活。"
        },
        822: {
            "pinyin": "bìng rù gāo huāng",
            "meaning": "病势已经深入要害部位，难以医治，比喻事情严重到难以挽回的地步。",
            "example": "贪污腐败之风若任其发展，势必病入膏肓。"
        },
        823: {
            "pinyin": "bìng rù gǔ suǐ",
            "meaning": "病势深入骨髓，比喻祸害极深或仇恨极深。",
            "example": "这种陋习在当地已经病入骨髓，不易根除。"
        },
        824: {
            "pinyin": "bìng dì fú róng",
            "meaning": "两朵荷花同生一蒂，比喻夫妻恩爱或兄弟友好。",
            "example": "画中的并蒂芙蓉象征着新人百年好合。"
        },
        825: {
            "pinyin": "bìng jià qí qū",
            "meaning": "并排驾车、齐头并进，比喻彼此地位或能力相当，不分高下。",
            "example": "这两家企业在行业内并驾齐驱，相互竞争。"
        },
        826: {
            "pinyin": "bìng rì ér shí",
            "meaning": "把两天的口粮合在一起吃，形容生活极其困苦。",
            "example": "战乱年代，百姓往往只能并日而食，勉强度日。"
        },
        827: {
            "pinyin": "bìng wéi yī tán",
            "meaning": "把不同的事物混在一起谈论，多指不该相提并论而却混为一谈。",
            "example": "学术讨论应有区分，不能把不同问题并为一谈。"
        },
        828: {
            "pinyin": "bìng xíng bù bèi",
            "meaning": "可以同时并行而互不抵触，指几种做法或观点可以共存。",
            "example": "传统文化与现代科技并行不悖，相辅相成。"
        },
        829: {
            "pinyin": "bāo chuáng jí fū",
            "meaning": "从床褥剥到肌肤，比喻侵害由浅入深，祸及本人。",
            "example": "若对腐败问题听之任之，终会剥床及肤，自食其果。"
        },
        830: {
            "pinyin": "bāo fū zhī tòng",
            "meaning": "像被剥去皮肤那样的疼痛，比喻极其惨痛的痛苦。",
            "example": "白发送黑发，对父母来说无疑是剥肤之痛。"
        },
        831: {
            "pinyin": "bō kāng mí mù",
            "meaning": "扬起谷壳迷住眼睛，比喻伤人害己的行为。",
            "example": "做人不可播糠眯目，只顾一时之利反害了自己。"
        },
        832: {
            "pinyin": "bō cǎo xún shé",
            "meaning": "拨动草丛去找蛇，比喻故意寻衅惹事，也比喻查探隐情。",
            "example": "他几番追问，无异于拨草寻蛇，让人心生警惕。"
        },
        833: {
            "pinyin": "bō luàn fǎn zhèng",
            "meaning": "拨除混乱的局面，恢复正常的秩序。",
            "example": "新政上台后，大力拨乱反正，社会秩序逐渐好转。"
        },
        834: {
            "pinyin": "bō yún liáo yǔ",
            "meaning": "原多用于描写男女欢会之事，后也用来形容挑动情欲或风月场景。",
            "example": "古典小说中常用拨云撩雨来描写儿女私情。"
        },
        835: {
            "pinyin": "bō yún jiàn rì",
            "meaning": "乌云拨开，太阳重现，比喻经历困境之后出现转机。",
            "example": "改革措施落实后，企业终于拨云见日，走出低谷。"
        },
        836: {
            "pinyin": "bō guāng lín lín",
            "meaning": "水面被波光照耀得闪闪发亮的样子。",
            "example": "夕阳下的湖面波光粼粼，景色十分迷人。"
        },
        837: {
            "pinyin": "bō jué yún guǐ",
            "meaning": "波浪诡谲、云彩怪异，比喻事物变化莫测或阴谋诡计多端。",
            "example": "局势波谲云诡，谁也不敢轻易下结论。"
        },
        838: {
            "pinyin": "bō lán lǎo chéng",
            "meaning": "历经风浪而显得老练成熟，形容人阅历深、处事沉稳。",
            "example": "多年打拼让他波澜老成，遇事沉着冷静。"
        },
        839: {
            "pinyin": "bō lán zhuàng kuò",
            "meaning": "波涛起伏、气势宏大，比喻场面或气势雄伟壮观。",
            "example": "这部长篇小说气象宏阔，可谓波澜壮阔。"
        },
        840: {
            "pinyin": "bō tāo xiōng yǒng",
            "meaning": "波浪翻滚、汹涌澎湃，比喻气势或声势非常浩大。",
            "example": "暴风雨来临时，大海波涛汹涌，惊心动魄。"
        },
        841: {
            "pinyin": "bó rán biàn sè",
            "meaning": "神色突然大变，多指因震惊或愤怒而脸色骤变。",
            "example": "听到这个消息，他勃然变色，半天说不出话来。"
        },
        842: {
            "pinyin": "bó rán dà nù",
            "meaning": "突然大发雷霆，形容人一时之间暴怒。",
            "example": "得知有人欺负孩子，他勃然大怒，当场质问对方。"
        },
        843: {
            "pinyin": "bó rán fèn lì",
            "meaning": "情绪激昂而奋发勉励，形容突然振作、努力进取的样子。",
            "example": "失败并未击倒他，反而让他勃然奋励，更加刻苦。"
        },
        844: {
            "pinyin": "bó cǎi zhòng cháng",
            "meaning": "广泛采纳众人的长处和优点。",
            "example": "团队管理要博采众长，善于听取各方面意见。"
        },
        845: {
            "pinyin": "bó dà jīng shēn",
            "meaning": "学识广博，精义深微，多用来形容学问或理论体系。",
            "example": "中国传统文化博大精深，值得一生钻研。"
        },
        846: {
            "pinyin": "bó ér bù jīng",
            "meaning": "知识面虽广却不精通，泛泛而学。",
            "example": "学习不能只求博而不精，要在某一方面深耕。"
        },
        847: {
            "pinyin": "bó ér guǎ yào",
            "meaning": "知识广博却对要点掌握不多，缺乏重点。",
            "example": "阅读若不分主次，容易博而寡要，抓不住核心。"
        },
        848: {
            "pinyin": "bó gǔ tōng jīn",
            "meaning": "通晓古代和现代的事情，形容学识渊博。",
            "example": "他博古通今，谈起历史来如数家珍。"
        },
        849: {
            "pinyin": "bó lǎn qún shū",
            "meaning": "广泛阅览各类书籍，形容读书极多。",
            "example": "要写好论文，离不开博览群书的积累。"
        },
        850: {
            "pinyin": "bó qià duō wén",
            "meaning": "学识广博而见闻丰富。",
            "example": "这位老先生博洽多闻，是大家敬重的学者。"
        },
        851: {
            "pinyin": "bó shī jì zhòng",
            "meaning": "广施恩惠，救济众人。",
            "example": "他热心公益，乐于助人，可谓博施济众。"
        },
        852: {
            "pinyin": "bó shí duō tōng",
            "meaning": "学识广、通晓的事情多。",
            "example": "老师博识多通，总能从不同角度启发学生。"
        },
        853: {
            "pinyin": "bó shì mǎi lǘ",
            "meaning": "比喻说话或写文章绕圈子，不切中要害。",
            "example": "文章开头铺陈太多，简直像博士买驴，只闻其名不见其形。"
        },
        854: {
            "pinyin": "bó shuò féi tú",
            "meaning": "肥壮的牛羊，形容牲畜肥美或物产丰富。",
            "example": "这一带水草丰茂，牛羊博硕肥腯。"
        },
        855: {
            "pinyin": "bó tōng jīng jí",
            "meaning": "通晓经典和史籍，形容学问渊博。",
            "example": "他自幼酷爱读书，长大后博通经籍。"
        },
        856: {
            "pinyin": "bó wén yuē lǐ",
            "meaning": "学识要广博，行为要合乎礼法，是古人治学做人的原则。",
            "example": "老师常勉励我们要博文约礼，修身立德。"
        },
        857: {
            "pinyin": "bó wén biàn yán",
            "meaning": "见闻广博、善于言辩。",
            "example": "他博闻辩言，在辩论场上游刃有余。"
        },
        858: {
            "pinyin": "bó wén qiáng jì",
            "meaning": "知识渊博、记忆力强。",
            "example": "这位学者博闻强记，许多典故信手拈来。"
        },
        859: {
            "pinyin": "bó wén qiáng zhì",
            "meaning": "见闻广博、记忆力强，多指学问深厚的人。",
            "example": "古人推崇博闻强识，以备不时之需。"
        },
        860: {
            "pinyin": "bó wù qià wén",
            "meaning": "通晓万物而见闻丰富。",
            "example": "要做博物洽闻之士，必须终身学习。"
        },
        861: {
            "pinyin": "bó xué duō cái",
            "meaning": "学识渊博，才能多方面。",
            "example": "他博学多才，在多个领域都有建树。"
        },
        862: {
            "pinyin": "bó xué duō wén",
            "meaning": "学识广博，见闻很多。",
            "example": "要在学术上有所成就，离不开博学多闻的积累。"
        },
        863: {
            "pinyin": "bó niú zhī méng",
            "meaning": "拍打牛身上的虻虫，比喻只注意消除小害而不顾大的祸患。",
            "example": "只在细节上斤斤计较，无异于搏牛之虻，忽略了更大的风险。"
        },
        864: {
            "pinyin": "bó hán zhòng rén",
            "meaning": "微微的寒意就使人感到刺骨，形容天气转凉、寒气侵人。",
            "example": "入秋后薄寒中人，出门还是得添件外套。"
        },
        865: {
            "pinyin": "bó jì zài shēn",
            "meaning": "身上只具备一点浅薄的技能。",
            "example": "他自知不过薄技在身，所以格外珍惜这份工作。"
        },
        866: {
            "pinyin": "bó mìng jiā rén",
            "meaning": "命运不好的美女，多指红颜薄命的女子。",
            "example": "她才貌双全，却命途多舛，真是让人感叹薄命佳人。"
        },
        867: {
            "pinyin": "bó wù xì gù",
            "meaning": "轻微细小的事物或过失。",
            "example": "这些薄物细故不必计较，还是把精力放在大事上。"
        },
        868: {
            "pinyin": "bó dào wú ér",
            "meaning": "比喻有德之人却没有子嗣，或用来感叹贤者不遇。",
            "example": "古人常以伯道无儿来感叹贤者命途多舛。"
        },
        869: {
            "pinyin": "bó gē jì wǔ",
            "meaning": "兄长唱歌、弟弟起舞，形容兄弟友爱或歌舞升平的欢乐场面。",
            "example": "节日里家人团聚，伯歌季舞，其乐融融。"
        },
        870: {
            "pinyin": "bó lè xiàng mǎ",
            "meaning": "伯乐善于相马，比喻善于识别和推荐人才的人。",
            "example": "他善于发现和培养新人，被同事称为当代伯乐相马。"
        },
        871: {
            "pinyin": "bó xūn zhòng chí",
            "meaning": "伯吹埙、仲吹篪，两种古代乐器合奏，比喻兄弟和好或配合默契。",
            "example": "兄弟俩合作无间，真有伯埙仲篪之和。"
        },
        872: {
            "pinyin": "bó yù zhī fēi",
            "meaning": "伯玉能够认识自己的过错，比喻知错能改、有自省之心。",
            "example": "青年人能像伯玉知非一样自省，才会不断进步。"
        },
        873: {
            "pinyin": "bó zhòng zhī jiān",
            "meaning": "高低、优劣相差不多。",
            "example": "这两支球队实力在伯仲之间，比赛格外精彩。"
        },
        874: {
            "pinyin": "bǒ biē qiān lǐ",
            "meaning": "即使跛脚的鳖也能走到千里之外，比喻只要坚持不懈，再弱小也能成功。",
            "example": "只要持之以恒，跛鳖千里，终能实现目标。"
        },
        875: {
            "pinyin": "bò jī fēn lǐ",
            "meaning": "像剥开肌肉、分清纹理那样细致，形容分析事理极为精细。",
            "example": "这篇评论把问题剖析得擘肌分理、入木三分。"
        },
        876: {
            "pinyin": "bū táo zhī chén",
            "meaning": "犯罪逃亡在外而未归的臣子，引申为有罪在身而逃匿不归的人。",
            "example": "他犯事后远走他乡，成了别人笔下的逋逃之臣。"
        },
        877: {
            "pinyin": "bǔ fēng zhuō yǐng",
            "meaning": "追逐风和影子，比喻言行没有根据、虚幻不实。",
            "example": "没有证据就乱下结论，无异于捕风捉影。"
        },
        878: {
            "pinyin": "bǔ yè bǔ zhòu",
            "meaning": "白天黑夜都在占卜，形容日夜忙碌地筹划或忧虑。",
            "example": "项目临近截止日期，他卜夜卜昼地反复推敲方案。"
        },
        879: {
            "pinyin": "bǔ zhòu bǔ yè",
            "meaning": "与“卜夜卜昼”同，指日夜不停地占卜，也比喻整日忧心忡忡。",
            "example": "为了这次考试，他卜昼卜夜地复习，生怕遗漏知识点。"
        },
        880: {
            "pinyin": "bǔ guò shí yí",
            "meaning": "弥补过失，拾补遗漏，形容事后补救错误和缺漏。",
            "example": "我们要及时补过拾遗，避免同样的错误再次发生。"
        },
        881: {
            "pinyin": "bǔ jū xià lòu",
            "meaning": "填补裂缝和漏洞，比喻弥补缺失、补救过失。",
            "example": "制度上存在的问题要及时补苴罅漏，不能听之任之。"
        },
        882: {
            "pinyin": "bǔ piān jiù bì",
            "meaning": "纠正偏差，挽救弊端。",
            "example": "这次改革正是为了补偏救弊，使政策更加完善。"
        },
        883: {
            "pinyin": "bǔ quē dēng qíng",
            "meaning": "像修补宫墙缺口、点亮灯檠一样，比喻匡正政治、整饬法度。",
            "example": "贤臣辅佐君王，所作所为无非补阙灯檠。"
        },
        884: {
            "pinyin": "bǔ quē shí yí",
            "meaning": "弥补疏漏和缺失，多指在工作或文章中补充遗漏之处。",
            "example": "这篇报告还有不少地方需要补阙拾遗，才能提交。"
        },
        885: {
            "pinyin": "bǔ tiān yù rì",
            "meaning": "补天又洗日，比喻功业宏大，能挽回极大的损失或危局。",
            "example": "若此计成功，几可补天浴日，扭转乾坤。"
        },
        886: {
            "pinyin": "bǔ tiān zhù dì",
            "meaning": "把天补好、把地支撑住，比喻挽救危局、支撑大局的重大作为。",
            "example": "国家危难之际，需要有人挺身而出补天柱地。"
        },
        887: {
            "pinyin": "bù ān qí shì",
            "meaning": "女子结婚后对丈夫的家庭不安分守礼，比喻不能安守本分。",
            "example": "他常在外惹是生非，简直有些不安其室。"
        },
        888: {
            "pinyin": "bù ān yú shì",
            "meaning": "同“ 不安其室 ”，指对现有的家庭或环境不安心。",
            "example": "他总想着外出闯荡，对目前的生活多少有些不安于室。"
        },
        889: {
            "pinyin": "bù ān yú wèi",
            "meaning": "对自己所处的位置不安心，常想变动或另谋出路。",
            "example": "身为干部应牢记职责，不可整日不安于位。"
        },
        890: {
            "pinyin": "bù bá zhī zhì",
            "meaning": "像树木扎根一样牢不可拔的志向，形容意志坚定。",
            "example": "他立下不拔之志，要把科研事业坚持到底。"
        },
        891: {
            "pinyin": "bù bái zhī yuān",
            "meaning": "没有得到澄清和昭雪的冤屈。",
            "example": "那桩公案多年未决，成了当事人的不白之冤。"
        },
        892: {
            "pinyin": "bù bēi bù kàng",
            "meaning": "既不自卑，也不傲慢，形容待人处事态度平和得体。",
            "example": "面对上级和下属，他始终不卑不亢，十分稳重。"
        },
        893: {
            "pinyin": "bù bì fǔ yuè",
            "meaning": "不畏惧斧钺之刑，比喻不怕严厉的惩罚或威胁。",
            "example": "他直言进谏，不避斧钺，只为社稷安危。"
        },
        894: {
            "pinyin": "bù biàn shū mài",
            "meaning": "连豆子和麦子都分不清，比喻极其无知或不识常识。",
            "example": "书读得太少，竟至不辨菽麦，难以胜任此职。"
        },
        895: {
            "pinyin": "bù biàn zhēn wěi",
            "meaning": "不能分辨真假。",
            "example": "网络信息繁杂，若不加辨别，容易不辨真伪而受骗。"
        },
        896: {
            "pinyin": "bù chā háo fà",
            "meaning": "一点一毫都不差，形容非常精确。",
            "example": "他按照图纸施工，尺寸把握得不差毫发。"
        },
        897: {
            "pinyin": "bù chā háo lí",
            "meaning": "相差极微小，几乎没有差别。",
            "example": "双方方案在成本上不差毫厘，需要从质量上来权衡。"
        },
        898: {
            "pinyin": "bù chā lěi shǔ",
            "meaning": "一点点像成堆的黍米那样微小的差异都没有，比喻丝毫不差。",
            "example": "账目核对后上下相符，不差累黍。"
        },
        899: {
            "pinyin": "bù chá bù fàn",
            "meaning": "既不想喝茶也不想吃饭，形容心事重重或身心不适。",
            "example": "自从出事以后，他整日愁眉不展，不茶不饭。"
        },
        900: {
            "pinyin": "bù chén zhī xīn",
            "meaning": "不愿做臣子之心，比喻不甘屈居人下或怀有不臣服的野心。",
            "example": "若有人心怀不臣之心，必成社稷大患。"
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

    print(f"已为 801–900 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
