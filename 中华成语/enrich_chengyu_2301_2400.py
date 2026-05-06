import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    enrich = {
        2301: {
            "pinyin": "dǎ bào bù píng",
            "meaning": "为受欺压的人打抱不平，主持公道。",
            "example": "他见同事被冤枉，立刻站出来打抱不平。"
        },
        2302: {
            "pinyin": "dǎ cǎo jīng shé",
            "meaning": "打草惊动了藏在草里的蛇，比喻做事不慎重，惊动对方，使其有所防备。",
            "example": "行动之前千万保密，免得打草惊蛇。"
        },
        2303: {
            "pinyin": "dǎ chéng yí piàn",
            "meaning": "融洽相处，混成一体，没有隔阂。",
            "example": "新同学很快和大家打成一片。"
        },
        2304: {
            "pinyin": "dǎ de huǒ rè",
            "meaning": "形容关系十分密切或争斗得非常激烈。",
            "example": "两人越聊越投机，很快就打得火热。"
        },
        2305: {
            "pinyin": "dǎ fèng lāo lóng",
            "meaning": "凤、龙比喻杰出人才，指到处寻找、网罗难得的人才。",
            "example": "这所名校四处打凤捞龙，延揽青年才俊。"
        },
        2306: {
            "pinyin": "dǎ fù jì pín",
            "meaning": "打击富人，救济穷人。多用来形容某些平均主义或革命措施。",
            "example": "那时曾倡言打富济贫，以求社会公平。"
        },
        2307: {
            "pinyin": "dǎ gōng zuò yī",
            "meaning": "双手抱拳、作揖行礼，是一种旧式的见面礼节。",
            "example": "老先生笑眯眯地向众人打躬作揖。"
        },
        2308: {
            "pinyin": "dǎ gǒu kàn zhǔ",
            "meaning": "打狗要看主人，比喻对待下属或晚辈时要顾及其背后靠山。",
            "example": "你若真要责怪他，也得打狗看主。"
        },
        2309: {
            "pinyin": "dǎ jiā jié shè",
            "meaning": "成群结队地抢劫人家财物。",
            "example": "那伙强盗专在荒郊打家劫舍。"
        },
        2310: {
            "pinyin": "dǎ kāi tiān chuāng shuō liàng huà",
            "meaning": "比喻把隐讳的事情公开讲明。",
            "example": "既然大家心里都有数，不如打开天窗说亮话。"
        },
        2311: {
            "pinyin": "dǎ luò shuǐ gǒu",
            "meaning": "痛打落水的狗，比喻乘人危难时进一步打击。",
            "example": "对已经认错的人就别再打落水狗了。"
        },
        2312: {
            "pinyin": "dǎ mǎ hu yǎn",
            "meaning": "故意装糊涂，敷衍了事。",
            "example": "这份报告不能再打马虎眼，必须认真修改。"
        },
        2313: {
            "pinyin": "dǎ mèn hú lu",
            "meaning": "说话含糊其词，使人猜不透。",
            "example": "问起工作进度，他只是打闷葫芦。"
        },
        2314: {
            "pinyin": "dǎ pò shā guō wèn dào dǐ",
            "meaning": "比喻追问事情的根底，非弄清不可。",
            "example": "这次审计要打破沙锅问到底，不能有任何疏漏。"
        },
        2315: {
            "pinyin": "dǎ qíng mà qiào",
            "meaning": "男女之间说笑打闹、表示亲昵。",
            "example": "年轻情侣在街角打情骂俏。"
        },
        2316: {
            "pinyin": "dǎ shé dǎ qī cùn",
            "meaning": "打蛇要打在七寸处，比喻做事抓住关键。",
            "example": "谈判要找住对方的软肋，犹如打蛇打七寸。"
        },
        2317: {
            "pinyin": "dǎ tiě chèn rè",
            "meaning": "趁铁烧红时锤打，比喻做事要抓紧时机。",
            "example": "项目刚起步，正该打铁趁热，把基础打牢。"
        },
        2318: {
            "pinyin": "dǎ tuì táng gǔ",
            "meaning": "原指官吏在堂上敲鼓、表示请求辞职，后多指临阵退缩。",
            "example": "关键时刻可不能打退堂鼓。"
        },
        2319: {
            "pinyin": "dǎ yā jīng yuān yāng",
            "meaning": "打鸭子吓惊了鸳鸯，比喻做事连累到无关的人。",
            "example": "他本想批评一人，结果打鸭惊鸳鸯，把大家都得罪了。"
        },
        2320: {
            "pinyin": "dǎ yā zi shàng jià",
            "meaning": "把鸭子硬往架子上放，比喻强人所难。",
            "example": "要他在众人面前演讲，无异于打鸭子上架。"
        },
        2321: {
            "pinyin": "dǎ yá fàn zuǐ",
            "meaning": "说顶撞或不合时宜的话。",
            "example": "他一时嘴快，打牙犯嘴惹恼了老板。"
        },
        2322: {
            "pinyin": "dǎ yá pèi zuǐ",
            "meaning": "多嘴多舌，爱插话评论。",
            "example": "这事与你无关，就别打牙配嘴了。"
        },
        2323: {
            "pinyin": "dǎ zhǒng liǎn chōng pàng zi",
            "meaning": "把脸打肿充胖子，比喻勉强充阔或逞能。",
            "example": "与其打肿脸充胖子，不如量力而行。"
        },
        2324: {
            "pinyin": "dà bài kuī shū",
            "meaning": "指败得厉害，损失很大。",
            "example": "这一仗他们大败亏输，只得班师回朝。"
        },
        2325: {
            "pinyin": "dà běn dà zōng",
            "meaning": "本：根本；宗：主旨。指事物最根本、最重要的部分。",
            "example": "办教育以育人为大本大宗，切忌本末倒置。"
        },
        2326: {
            "pinyin": "dà bǐ rú chuán",
            "meaning": "笔大如椽木，形容笔力雄健或文章气势宏大。",
            "example": "史家以大笔如椽写尽王朝兴替。"
        },
        2327: {
            "pinyin": "dà biàn bù yán",
            "meaning": "大辩者不必多言，形容真正有理的人反而不善于辩论。",
            "example": "他处事低调，大辩不言，却最得人心。"
        },
        2328: {
            "pinyin": "dà biàn ruò nè",
            "meaning": "最善于辩论的人反而显得迟钝，形容大智若愚的风度。",
            "example": "那位长者大辩若讷，从不与人争口舌。"
        },
        2329: {
            "pinyin": "dà bù liú xīng",
            "meaning": "形容步伐大、走路快，多比喻大踏步前进。",
            "example": "队伍大步流星地赶往灾区。"
        },
        2330: {
            "pinyin": "dà cái pán pán",
            "meaning": "槃槃：盛大、宏大。形容人有很大的才干。",
            "example": "他真是大才槃槃，可惜生不逢时。"
        },
        2331: {
            "pinyin": "dà cái xiǎo yòng",
            "meaning": "用人不当，让有大才干的人去做小事情。",
            "example": "让他只做这些杂务，未免大材小用。"
        },
        2332: {
            "pinyin": "dà chē yǐ zài",
            "meaning": "大车可载重物，比喻有人能胜大任。",
            "example": "这位主将大车以载，可托付重任。"
        },
        2333: {
            "pinyin": "dà chè dà wù",
            "meaning": "彻：通晓；悟：领会。形容彻底觉悟，完全明白。",
            "example": "经过这番波折，他终于大彻大悟。"
        },
        2334: {
            "pinyin": "dà chè dà wù",
            "meaning": "与“大彻大悟”同义，形容彻底明白、觉悟。",
            "example": "一夜思索之后，他似乎大澈大悟。"
        },
        2335: {
            "pinyin": "dà chù luò mò",
            "meaning": "落墨：落笔。原指写画要在主要部分下功夫，比喻做事抓住大处、关键处着手。",
            "example": "改革必须大处落墨，解决体制上的问题。"
        },
        2336: {
            "pinyin": "dà chù zhuó mò",
            "meaning": "指在主要部分用力描写，比喻做事要立足全局、从大处着眼。",
            "example": "写文章要大处着墨，小处精雕。"
        },
        2337: {
            "pinyin": "dà chù zhuó yǎn",
            "meaning": "从大的方面观察、思考问题，抓住主要矛盾。",
            "example": "领导干部要学会大处着眼，小处着手。"
        },
        2338: {
            "pinyin": "dà chuī dà léi",
            "meaning": "形容说话或做事声势很大。多含夸张之意。",
            "example": "方案还没影儿，他倒先大吹大擂起来。"
        },
        2339: {
            "pinyin": "dà chuī fǎ luó",
            "meaning": "比喻夸大其词，到处宣扬。",
            "example": "广告词不能一味大吹法螺，否则适得其反。"
        },
        2340: {
            "pinyin": "dà chún xiǎo cī",
            "meaning": "醇：纯正；疵：毛病。大体纯正而略有小缺点。",
            "example": "这篇文章大醇小疵，总体还是很精彩的。"
        },
        2341: {
            "pinyin": "dà cí dà bēi",
            "meaning": "极大的慈悲，多形容佛、菩萨或极富怜悯之心的人。",
            "example": "观音菩萨大慈大悲，普度众生。"
        },
        2342: {
            "pinyin": "dà cuò tè cuò",
            "meaning": "极大的错误，完全错误。",
            "example": "把责任推给基层，是大错特错的做法。"
        },
        2343: {
            "pinyin": "dà dǎ chū shǒu",
            "meaning": "大规模地相互殴打，多指多人参与的斗殴。",
            "example": "双方一言不合，就大打出手。"
        },
        2344: {
            "pinyin": "dà dà luò luò",
            "meaning": "形容人举止洒脱大方，或形容人不拘小节。",
            "example": "她性格大大落落，很少计较小事。"
        },
        2345: {
            "pinyin": "dà dāo kuò fǔ",
            "meaning": "比喻作风坚决果断，大规模地改革、整顿。",
            "example": "这次机构改革要大刀阔斧，不能畏首畏尾。"
        },
        2346: {
            "pinyin": "dà dé rén xīn",
            "meaning": "做事合乎民意，因而深得人心。",
            "example": "新政策切合实际，自然大得人心。"
        },
        2347: {
            "pinyin": "dà dí dāng qián",
            "meaning": "强大的敌人就在眼前，形容形势十分紧急。",
            "example": "如今大敌当前，更要同心协力。"
        },
        2348: {
            "pinyin": "dà dì huí chūn",
            "meaning": "大地恢复生机，形容春回人间、万物复苏的景象。",
            "example": "冰雪消融，大地回春，一派生机。"
        },
        2349: {
            "pinyin": "dà dòng gān gē",
            "meaning": "大动刀兵，比喻兴师动众、挑起战争或大规模冲突。",
            "example": "这点小事不必大动干戈。"
        },
        2350: {
            "pinyin": "dà dù bāo róng",
            "meaning": "气度宏大，能容人之短，受人之过。",
            "example": "领导者应有大度包容之心，善纳不同意见。"
        },
        2351: {
            "pinyin": "dà ér huà zhī",
            "meaning": "做事粗疏，不求深入细致。也可指对小节不拘泥。",
            "example": "他向来大而化之，不太计较生活细节。"
        },
        2352: {
            "pinyin": "dà ér wú dāng",
            "meaning": "大而不合用，形容不切实际或不相称。",
            "example": "这套制度看似完备，其实行之大而无当。"
        },
        2353: {
            "pinyin": "dà fà cí bēi",
            "meaning": "大发慈悲，大施恩惠（多含戏谑）。",
            "example": "老师今日大发慈悲，竟然不留作业。"
        },
        2354: {
            "pinyin": "dà fà léi tíng",
            "meaning": "比喻大发怒气，严厉训斥。",
            "example": "得知有人弄虚作假，校长当场大发雷霆。"
        },
        2355: {
            "pinyin": "dà fǎ xiǎo lián",
            "meaning": "旧指大臣守法，小吏廉洁，比喻各尽其职、上下守正。",
            "example": "若能做到大法小廉，政风自然清明。"
        },
        2356: {
            "pinyin": "dà fāng zhī jiā",
            "meaning": "学识渊博、见识高明的人家或主人。",
            "example": "他出入多是大方之家，眼界渐渐开阔。"
        },
        2357: {
            "pinyin": "dà fàng bēi shēng",
            "meaning": "放声大哭，发出悲凄的哭声。",
            "example": "噩耗传来，亲属们大放悲声。"
        },
        2358: {
            "pinyin": "dà fàng jué cí",
            "meaning": "放肆发表言论，多指说话夸大其词或信口开河。",
            "example": "他在会上大放厥词，毫无依据。"
        },
        2359: {
            "pinyin": "dà fēng dà làng",
            "meaning": "形容险恶的环境或巨大的考验。",
            "example": "他经历过大风大浪，心态早已十分沉稳。"
        },
        2360: {
            "pinyin": "dà fù pián pián",
            "meaning": "形容肚子很大，多指中年发福的男子。",
            "example": "他大腹便便，走起路来气喘吁吁。"
        },
        2361: {
            "pinyin": "dà gōng gào chéng",
            "meaning": "大工作已经完成。",
            "example": "桥梁顺利竣工，这项民生工程终于大功告成。"
        },
        2362: {
            "pinyin": "dà gōng wú sī",
            "meaning": "一心为公，没有私心。",
            "example": "他为人处世大公无私，深受大家信服。"
        },
        2363: {
            "pinyin": "dà hǎi lāo zhēn",
            "meaning": "在大海里捞一根针，比喻极难找到。",
            "example": "不留任何线索，要再找到他简直是大海捞针。"
        },
        2364: {
            "pinyin": "dà hán suǒ qiú",
            "meaning": "等到寒冬才去找皮袍，比喻平时不作准备，事到临头才手忙脚乱。",
            "example": "学习不能像大寒索裘，临考才着急。"
        },
        2365: {
            "pinyin": "dà hán xì rù",
            "meaning": "原指文章包罗宏大而又深入细微，形容文辞博大精深。",
            "example": "他的论著大含细入，读来收获颇丰。"
        },
        2366: {
            "pinyin": "dà hàn wàng yún ní",
            "meaning": "大旱之时盼望云霓出现，比喻殷切期盼救援或好消息。",
            "example": "久旱的庄稼盼雨如大旱望云霓。"
        },
        2367: {
            "pinyin": "dà hàn yún ní",
            "meaning": "与“大旱望云霓”同义，形容对解救的强烈期盼。",
            "example": "百姓对减税政策可谓大旱云霓。"
        },
        2368: {
            "pinyin": "dà háng dà shì",
            "meaning": "指商品的一般市场价格。",
            "example": "这价钱不过是大行大市，你不必嫌贵。"
        },
        2369: {
            "pinyin": "dà hǎo hé shān",
            "meaning": "辽阔美好的国土山河。",
            "example": "我们要共同守护这片大好河山。"
        },
        2370: {
            "pinyin": "dà huò quán shèng",
            "meaning": "在大战或比赛中取得全面胜利。",
            "example": "经过顽强拼搏，我军终于大获全胜。"
        },
        2371: {
            "pinyin": "dà huò bù jiě",
            "meaning": "疑惑很大，难以理解。",
            "example": "对他的突然辞职，大家都大惑不解。"
        },
        2372: {
            "pinyin": "dà jí dà lì",
            "meaning": "非常吉祥顺利，多用作祝颂语。",
            "example": "新年祝你大吉大利，心想事成。"
        },
        2373: {
            "pinyin": "dà jì xiǎo yòng",
            "meaning": "把重大计划用在小事情上，比喻人尽其才而用非其处。",
            "example": "让他长期处理琐务，无异于大计小用。"
        },
        2374: {
            "pinyin": "dà jiā fēng fàn",
            "meaning": "大家：德高望重的人。指有名望人物所表现出的气度和风范。",
            "example": "他的为人处世颇具大家风范。"
        },
        2375: {
            "pinyin": "dà jiā guī xiù",
            "meaning": "指出身名门、受过良好教育的女子。",
            "example": "她自小涵养极佳，真是典型的大家闺秀。"
        },
        2376: {
            "pinyin": "dà jiāng dōng qù",
            "meaning": "江水向东流去，比喻时间流逝或历史潮流不可逆转，也常借指苏轼词句。",
            "example": "人生如大江东去，转瞬已是暮年。"
        },
        2377: {
            "pinyin": "dà jiāng nán běi",
            "meaning": "长江以南以北，泛指广大的区域。",
            "example": "他的足迹遍及大江南北。"
        },
        2378: {
            "pinyin": "dà jiē xiǎo xiàng",
            "meaning": "城市里的大街小巷，到处、各个角落。",
            "example": "这首歌很快传遍大街小巷。"
        },
        2379: {
            "pinyin": "dà jié bù duó",
            "meaning": "在生死关头仍不改变自己的节操和志向。",
            "example": "先贤临难不苟，大节不夺。"
        },
        2380: {
            "pinyin": "dà jīng shī sè",
            "meaning": "非常吃惊，吓得脸色都变了。",
            "example": "听到这个消息，他不禁大惊失色。"
        },
        2381: {
            "pinyin": "dà jīng xiǎo guài",
            "meaning": "遇到平常事情也大惊小怪，形容见识少或胆小。",
            "example": "这点风浪就吓成这样，未免太大惊小怪了。"
        },
        2382: {
            "pinyin": "dà kāi dà hé",
            "meaning": "原指音乐气势雄浑开阔，后也形容文章、局面等气势宏大。",
            "example": "这部交响曲大开大合，气势恢宏。"
        },
        2383: {
            "pinyin": "dà kāi yǎn jiè",
            "meaning": "见到平常不容易见到的事物，增长见识。",
            "example": "这次展览真是让我大开眼界。"
        },
        2384: {
            "pinyin": "dà kuài wén zhāng",
            "meaning": "大篇精彩的文章，也借指宏大的著作。",
            "example": "这部史书可谓一代大块文章。"
        },
        2385: {
            "pinyin": "dà kuài rén xīn",
            "meaning": "指坏人受到惩罚或问题得到解决，使大家非常痛快。",
            "example": "这次严惩腐败分子，着实大快人心。"
        },
        2386: {
            "pinyin": "dà làng táo shā",
            "meaning": "大浪翻涌淘洗沙石，比喻在激烈斗争中淘汰坏的，留下精华。",
            "example": "时代如大浪淘沙，终会留下真正的金子。"
        },
        2387: {
            "pinyin": "dà lù zhuī lún",
            "meaning": "大辂：华美的大车；椎轮：原始的实心车轮。比喻事物由简到繁、由粗到精的发展过程，也用来称赞开创性的事物。",
            "example": "他在这一领域的工作，有如大辂椎轮之功。"
        },
        2388: {
            "pinyin": "dà mèng chū xǐng",
            "meaning": "好像从大梦中刚刚醒来，比喻从长期迷惘中突然觉悟。",
            "example": "经历这件事，他仿佛大梦初醒。"
        },
        2389: {
            "pinyin": "dà míng dǐng dǐng",
            "meaning": "形容名声很大，人人皆知。",
            "example": "这位科学家在业内大名鼎鼎。"
        },
        2390: {
            "pinyin": "dà míng fǎ dù",
            "meaning": "指完备而清明的法律制度，有时也特指某朝的成文法度。",
            "example": "古代典籍中多有关于大明法度的记载。"
        },
        2391: {
            "pinyin": "dà miù bù rán",
            "meaning": "非常荒谬，完全不是那回事。",
            "example": "把失败全怪在员工身上，实在大谬不然。"
        },
        2392: {
            "pinyin": "dà mú dà yàng",
            "meaning": "形容态度傲慢、目中无人的样子，也指大大方方、不拘小节。",
            "example": "他走路一副大模大样的样子，引人侧目。"
        },
        2393: {
            "pinyin": "dà mò yǔ jīng",
            "meaning": "莫：没有谁；京：大。大得无人能比，形容首屈一指、无与伦比。",
            "example": "此山巍峨雄伟，真可谓大莫与京。"
        },
        2394: {
            "pinyin": "dà móu bù móu",
            "meaning": "具有远大谋略的人表面上好像不善谋划，形容大智若愚的气度。",
            "example": "他行事看似散漫，其实大谋不谋。"
        },
        2395: {
            "pinyin": "dà nàn bù sǐ",
            "meaning": "在极大的灾难中幸存下来。",
            "example": "他在那次地震中大难不死，更懂得珍惜生命。"
        },
        2396: {
            "pinyin": "dà nàn lín tóu",
            "meaning": "巨大的灾难降临到头上。",
            "example": "他破产之后，真正体会到大难临头各自飞。"
        },
        2397: {
            "pinyin": "dà nì bù dào",
            "meaning": "罪行极大，悖逆天理人道。",
            "example": "屠杀无辜百姓，简直是大逆不道。"
        },
        2398: {
            "pinyin": "dà qì páng bó",
            "meaning": "气势宏大磅礴，形容场面或气概极为壮阔。",
            "example": "这幅山水画大气磅礴，令人震撼。"
        },
        2399: {
            "pinyin": "dà qì wǎn chéng",
            "meaning": "大器需要较长时间才能铸成，比喻成就大事业的人往往成名较晚。",
            "example": "他四十岁才崭露头角，真是大器晚成。"
        },
        2400: {
            "pinyin": "dà qiān shì jiè",
            "meaning": "佛教语，指包括无数世界在内的广大宇宙，也泛指极为浩瀚的世界。",
            "example": "在这大千世界中，每个人都只是微小的一粒尘埃。"
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

    print(f"已为 2301–2400 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
