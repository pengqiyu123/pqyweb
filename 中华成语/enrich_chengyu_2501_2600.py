import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    enrich = {
        2501: {
            "pinyin": "dān fèng cháo yáng",
            "meaning": "比喻贤才遇上英明的君主或良好的时代。",
            "example": "青年学者得以在重要科研平台一展所学，真有丹凤朝阳之感。"
        },
        2502: {
            "pinyin": "dān qīng bù yú",
            "meaning": "丹、青都是不易褪色的颜料，比喻节操、信念始终不变。",
            "example": "他对公益事业的投入丹青不渝，几十年如一日。"
        },
        2503: {
            "pinyin": "dān shū tiě qì",
            "meaning": "用丹笔书写、以铁为契的文书，古代表示功勋与信用永不更改的凭据。",
            "example": "祖上的丹书铁契早已散佚，只在族谱中留下只言片语。"
        },
        2504: {
            "pinyin": "dān shū tiě quàn",
            "meaning": "皇帝赐给功臣的免死金牌，借指对功劳的最高褒奖或永保荣宠的凭据。",
            "example": "他虽无丹书铁券，却以实干赢得众人尊敬。"
        },
        2505: {
            "pinyin": "dān xīn bì xuè",
            "meaning": "丹心与碧血，比喻赤诚的忠心和为正义事业流的鲜血。",
            "example": "先烈们以丹心碧血换来了今天的和平生活。"
        },
        2506: {
            "pinyin": "dān xīn rú gù",
            "meaning": "忠心一如从前，始终不变。",
            "example": "他对家乡建设丹心如故，从未因身居异地而疏远。"
        },
        2507: {
            "pinyin": "dān yíng kè jué",
            "meaning": "楹：柱子；桷：椽子。柱子涂成红色，椽子雕刻花纹，形容建筑华美精巧。",
            "example": "古殿丹楹刻桷，金碧辉煌，令人叹为观止。"
        },
        2508: {
            "pinyin": "dān zhī suǒ cáng zhě chì",
            "meaning": "丹所浸润的东西都会变红，比喻环境和朋友对人的深远影响，交友必须谨慎择人。",
            "example": "古人云丹之所藏者赤，择友之道，岂可不慎。"
        },
        2509: {
            "pinyin": "dǎn cū qì zhuàng",
            "meaning": "胆量粗大而气势凶猛，多形容人蛮横无畏。",
            "example": "他仗着人多势众，行事一向胆粗气壮。"
        },
        2510: {
            "pinyin": "dǎn dà bāo tiān",
            "meaning": "胆大得连天都敢包下来，比喻胆量极大，常含鲁莽之意。",
            "example": "不研究行情就盲目投资，未免胆大包天。"
        },
        2511: {
            "pinyin": "dǎn dà rú dǒu",
            "meaning": "胆子大得像斗一样，形容非常大胆。",
            "example": "他胆大如斗，竟敢独自夜探古墓。"
        },
        2512: {
            "pinyin": "dǎn dà wàng wéi",
            "meaning": "胆子很大，行为放肆，不顾后果。",
            "example": "若是胆大妄为触犯法律，终要付出代价。"
        },
        2513: {
            "pinyin": "dǎn dà xīn xiǎo",
            "meaning": "做事胆子很大，但心思细密谨慎。",
            "example": "这类高危救援，需要胆大心小、反应敏捷的人。"
        },
        2514: {
            "pinyin": "dǎn dà xīn cū",
            "meaning": "有胆量却粗心大意，考虑不周。",
            "example": "他胆大心粗，签合同时总是不看细节。"
        },
        2515: {
            "pinyin": "dǎn dà xīn xì",
            "meaning": "既有胆量又细心周到。",
            "example": "外科医生必须胆大心细，方能完成高难度手术。"
        },
        2516: {
            "pinyin": "dǎn liè hún fēi",
            "meaning": "吓得胆都裂了、魂都飞了，形容极度惊恐。",
            "example": "突如其来的山体滑坡让村民胆裂魂飞。"
        },
        2517: {
            "pinyin": "dǎn pò xīn hán",
            "meaning": "吓得胆破心寒，形容非常害怕、心惊胆战。",
            "example": "亲历那场车祸后，他每次坐车仍觉胆破心寒。"
        },
        2518: {
            "pinyin": "dǎn xiǎo pà shì",
            "meaning": "胆子小，怕惹是非，不敢担当。",
            "example": "关键时刻若人人胆小怕事，事情就办不成。"
        },
        2519: {
            "pinyin": "dǎn xiǎo rú shǔ",
            "meaning": "胆小得像老鼠一样，形容极端胆怯。",
            "example": "他在台上胆小如鼠，一句话都说不出来。"
        },
        2520: {
            "pinyin": "dǎn zhàn xīn hán",
            "meaning": "吓得发抖、心里发冷，形容十分害怕。",
            "example": "听到山洪暴发的消息，村民无不胆战心寒。"
        },
        2521: {
            "pinyin": "dǎn zhàn xīn jīng",
            "meaning": "胆子发抖，心里吃惊，形容极度惊恐不安。",
            "example": "飞机遭遇强烈气流时，乘客们无不胆战心惊。"
        },
        2522: {
            "pinyin": "dàn jìn liáng jué",
            "meaning": "子弹打光、粮食吃尽，形容陷入孤立无援、极端困难的境地。",
            "example": "守军弹尽粮绝，只得选择突围。"
        },
        2523: {
            "pinyin": "dàn jìn yuán jué",
            "meaning": "子弹用尽，援军断绝，形容处境异常危急。",
            "example": "一旦前线弹尽援绝，后果不堪设想。"
        },
        2524: {
            "pinyin": "dàn wán zhī dì",
            "meaning": "像弹丸那样小的一块地方，比喻国家、地区疆域狭小。",
            "example": "这个岛国虽是弹丸之地，却经济发达。"
        },
        2525: {
            "pinyin": "dàn wú xū fā",
            "meaning": "射出的子弹没有一发虚耗，形容射击技术极高，也比喻做事准确无误。",
            "example": "狙击手弹无虚发，一举瓦解了敌方火力点。"
        },
        2526: {
            "pinyin": "dàn bó míng zhì",
            "meaning": "性情恬淡，不追逐名利，以此保持志向高洁。",
            "example": "他向往淡泊明志的生活，不愿卷入名利场。"
        },
        2527: {
            "pinyin": "dàn ér bù yàn",
            "meaning": "味道虽淡却不使人厌烦，也比喻文风朴素却耐人寻味。",
            "example": "这篇小品文淡而不厌，读来颇觉亲切。"
        },
        2528: {
            "pinyin": "dàn ér wú wèi",
            "meaning": "味道清淡甚至寡淡无味，比喻事物平淡乏味、缺乏特色。",
            "example": "如果缺乏细节描写，人物形象就会显得淡而无味。"
        },
        2529: {
            "pinyin": "dàn rán chǔ zhī",
            "meaning": "以平静、冷静的态度对待事物，不大惊小怪。",
            "example": "面对流言蜚语，他选择淡然处之。"
        },
        2530: {
            "pinyin": "dàn rán zhì zhī",
            "meaning": "冷淡地放在一边，不予理会。",
            "example": "他对一切与学术无关的应酬都淡然置之。"
        },
        2531: {
            "pinyin": "dàn rǔ nóng mǒ",
            "meaning": "原为“淡妆浓抹”之讹写，形容素雅与浓丽两种不同的装饰风格。",
            "example": "湖光山色，晴时淡汝浓抹，雨时烟波浩渺，各有情致。"
        },
        2532: {
            "pinyin": "dàn hè qiān lǐ",
            "meaning": "惮赫：威震。威势震动千里，形容声威极盛。",
            "example": "其军威惮赫千里，令敌军不敢轻举妄动。"
        },
        2533: {
            "pinyin": "dàn dàn ér fá",
            "meaning": "一再进攻或责难，形容反复不断地攻击。",
            "example": "他对腐败现象旦旦而伐，从未松口。"
        },
        2534: {
            "pinyin": "dàn xī zhī jiān",
            "meaning": "在早晨和傍晚之间，比喻时间非常短暂。",
            "example": "局势在旦夕之间就发生了逆转。"
        },
        2535: {
            "pinyin": "dàn xī zhī wēi",
            "meaning": "危险就在早晚之间，比喻情势岌岌可危。",
            "example": "若不及时疏散群众，堤坝失守只是旦夕之危。"
        },
        2536: {
            "pinyin": "dàn zhǒng mù chéng",
            "meaning": "早晨播种，傍晚就长成，比喻事情成功过于迅速，常含不切实际之意。",
            "example": "若想旦种暮成，而不踏实投入，终究难有收获。"
        },
        2537: {
            "pinyin": "dàn yǐ zhòng lì",
            "meaning": "用重利引诱别人。",
            "example": "有人试图啖以重利，让他出卖原则，被他严词拒绝。"
        },
        2538: {
            "pinyin": "dàn shuǐ jiāo qíng",
            "meaning": "友情清澈如水，不掺杂功利得失。",
            "example": "与其酒肉朋友，不如几位淡水交情的知己。"
        },
        2539: {
            "pinyin": "dàn bó guǎ yù",
            "meaning": "澹泊：恬淡；寡欲：少欲。形容心境恬淡，不贪图名利与享乐。",
            "example": "他选择澹泊寡欲的生活方式，把主要精力都用在创作上。"
        },
        2540: {
            "pinyin": "dàn bó míng zhì, níng jìng zhì yuǎn",
            "meaning": "只有恬淡寡欲才能明确志向，只有心境宁静才能成就远大目标。",
            "example": "诸葛亮在诫子书中提出澹泊明志，宁静致远，被后世奉为座右铭。"
        },
        2541: {
            "pinyin": "dāng chǎng chū cǎi",
            "meaning": "在现场表现出色、大放光彩。",
            "example": "他在答辩会上当场出彩，评委们纷纷点头称赞。"
        },
        2542: {
            "pinyin": "dāng duàn bù duàn",
            "meaning": "在必须下决心时优柔寡断，反贻后患。",
            "example": "对违规行为当断不断，只会酿成更大的问题。"
        },
        2543: {
            "pinyin": "dāng xíng chū sè",
            "meaning": "在本行业、本专业中表现特别突出。",
            "example": "他在法律界当行出色，屡屡承办重大案件。"
        },
        2544: {
            "pinyin": "dāng ěr biān fēng",
            "meaning": "把别人的话当成风吹过耳旁，比喻丝毫不在意。",
            "example": "老师的忠告他全当耳边风，结果吃了大亏。"
        },
        2545: {
            "pinyin": "dāng fēng bǐng zhú",
            "meaning": "迎着风举着蜡烛，比喻身处极其危险的境地。",
            "example": "在缺乏监管的深山黑矿作业，无异于当风秉烛。"
        },
        2546: {
            "pinyin": "dāng jī lì duàn",
            "meaning": "在紧要关头立刻作出果断决定。",
            "example": "面对突发险情，他当机立断，组织人员紧急撤离。"
        },
        2547: {
            "pinyin": "dāng jú zhě mí, páng guān zhě qīng",
            "meaning": "当事人往往被纠缠其中而看不清问题，旁观者反而看得清楚。",
            "example": "所谓当局者迷，旁观者清，多听外界意见往往有益。"
        },
        2548: {
            "pinyin": "dāng lì zhī nián",
            "meaning": "指男子三十岁前后，应当自立成家立业的年龄。",
            "example": "到了当立之年，他终于找到了自己的发展方向。"
        },
        2549: {
            "pinyin": "dāng mén dǐ hù",
            "meaning": "指撑持门户、主持家务。",
            "example": "父母年迈，家中琐事多由大姐当门抵户。"
        },
        2550: {
            "pinyin": "dāng miàn luó, duì miàn gǔ",
            "meaning": "像锣鼓相对敲打，比喻当面直接商量、对质或争论。",
            "example": "有意见就当面锣，对面鼓地说清楚，别背后议论。"
        },
        2551: {
            "pinyin": "dāng miàn shū xīn bèi miàn xiào",
            "meaning": "当面装出真心，背后却暗中讥笑，比喻表里不一、两面三刀。",
            "example": "与其当面输心背面笑，不如坦诚相待。"
        },
        2552: {
            "pinyin": "dāng rén bú ràng",
            "meaning": "遇到合乎道义的事情主动承担责任，不推让给别人。",
            "example": "在维护集体利益的问题上，应当仁不让。"
        },
        2553: {
            "pinyin": "dāng shì wú shuāng",
            "meaning": "当代社会中没有第二个可与之相比的人，形容极为杰出。",
            "example": "他在该领域的贡献可谓当世无双。"
        },
        2554: {
            "pinyin": "dāng tóu bàng hè",
            "meaning": "从头上打下一棒喝醒，比喻当头的严厉警告或提醒。",
            "example": "导师的一番直言不讳，如当头棒喝，让他重新审视自己。"
        },
        2555: {
            "pinyin": "dāng tóu duì miàn",
            "meaning": "面对面，正对着。多形容态度直接。",
            "example": "有问题不妨当头对面地谈一谈。"
        },
        2556: {
            "pinyin": "dāng tóu yī bàng",
            "meaning": "迎头一记棒打，比喻突然受到严厉斥责或打击。",
            "example": "方案刚讲完就遭领导当头一棒，他只好回去重想。"
        },
        2557: {
            "pinyin": "dāng wù zhī jí",
            "meaning": "当前必须立刻处理的紧要任务。",
            "example": "解决就业问题是当前的当务之急。"
        },
        2558: {
            "pinyin": "dāng zhī wú kuì",
            "meaning": "担当得起某种称号或荣誉，毫不惭愧。",
            "example": "他对事业的投入与成就，当之无愧被称为行业楷模。"
        },
        2559: {
            "pinyin": "dāng zhī yǒu kuì",
            "meaning": "自觉愧对于某种名分或期望。",
            "example": "面对师长的期待，他坦言当之有愧。"
        },
        2560: {
            "pinyin": "dāng zhóu chǔ zhōng",
            "meaning": "当：掌管；轴：要职；处中：在中央。指身居中枢要职、掌握大权。",
            "example": "他当轴处中多年，对国家经济政策影响甚大。"
        },
        2561: {
            "pinyin": "dāng zhuó bù zhuó",
            "meaning": "该做的事不做，不该做的事却去做，形容处理事务颠倒失当。",
            "example": "若在改革中当着不着，只会错失良机。"
        },
        2562: {
            "pinyin": "dǎng chái wéi nüè",
            "meaning": "把豺狼之类的恶人结为同党，一起扰乱祸害百姓。",
            "example": "他结交权奸，党豺为虐，终究不得善终。"
        },
        2563: {
            "pinyin": "dǎng tóng fá yì",
            "meaning": "同党的人互相帮助，对立者则加以打击，形容结党营私。",
            "example": "用人若只讲亲疏、党同伐异，势必损害公信力。"
        },
        2564: {
            "pinyin": "dǎng yán zhí shēng",
            "meaning": "公正正直的言论和坦率无畏的声音。",
            "example": "在种种溢美之词中，更需要几句谠言直声。"
        },
        2565: {
            "pinyin": "dàng jiǎn yú xián",
            "meaning": "荡、逾：超越；检、闲：法度、规矩。形容行为放荡，不守礼法，越出应有的界限。",
            "example": "若任由少数人荡检逾闲，必将影响整个团队的风气。"
        },
        2566: {
            "pinyin": "dàng qì huí cháng",
            "meaning": "气势激荡，回旋不已，形容文章、音乐等极有感染力，使人内心激动不已。",
            "example": "这部史诗般的小说真可谓荡气回肠。"
        },
        2567: {
            "pinyin": "dàng rán wú cún",
            "meaning": "荡然：完全消失。形容事物彻底消失、一点不剩。",
            "example": "洪水过后，沿河村庄荡然无存。"
        },
        2568: {
            "pinyin": "dàng xī lí jū",
            "meaning": "家园破败、亲人流离，彼此分散各处居住。",
            "example": "战乱使千家万户荡析离居，民不聊生。"
        },
        2569: {
            "pinyin": "dāo gēng huǒ nòu",
            "meaning": "指原始的刀耕火烧式农业生产方式。",
            "example": "祖辈们靠刀耕火耨在这片山地顽强生存。"
        },
        2570: {
            "pinyin": "dāo gēng huǒ zhòng",
            "meaning": "与“刀耕火耨”同义，指原始的农耕方式。",
            "example": "那时生产力低下，只能刀耕火种，收成极不稳定."
        },
        2571: {
            "pinyin": "dāo guāng jiàn yǐng",
            "meaning": "刀的寒光与剑的影子，形容搏斗激烈或气氛紧张。",
            "example": "影片中的决斗场面刀光剑影，扣人心弦。"
        },
        2572: {
            "pinyin": "dāo guò zhú jiě",
            "meaning": "刀一砍下去竹子立刻分开，比喻事情处理得干脆利落、毫不拖泥带水。",
            "example": "这类纠纷要刀过竹解，不能一拖再拖。"
        },
        2573: {
            "pinyin": "dāo jù dǐng huò",
            "meaning": "刀、锯、鼎、镬都是古代酷刑刑具，借指种种严酷的刑罚。",
            "example": "古时叛逆者往往要受刀锯鼎镬之刑。"
        },
        2574: {
            "pinyin": "dāo jù fǔ yuè",
            "meaning": "刀、锯、斧、钺皆为古代刑具，比喻残酷的刑罚或暴虐统治。",
            "example": "暴君以刀锯斧钺恐吓臣民，终致众叛亲离。"
        },
        2575: {
            "pinyin": "dāo qiāng jiàn jǐ",
            "meaning": "刀、枪、剑、戟等各种冷兵器的总称，多用以形容战场景象或武备森严。",
            "example": "城头刀枪剑戟森然，在阳光下闪着寒光。"
        },
        2576: {
            "pinyin": "dāo shān huǒ hǎi",
            "meaning": "比喻极其艰险、困难的环境，也指各种严酷的考验。",
            "example": "即使前路是刀山火海，他也要救出被困群众。"
        },
        2577: {
            "pinyin": "dāo shān jiàn shù",
            "meaning": "刀山与剑树，比喻极其危险、艰难的境地。",
            "example": "为了理想，他不惧刀山剑树。"
        },
        2578: {
            "pinyin": "dāo tóu tiǎn mì",
            "meaning": "在刀尖上舔蜂蜜，比喻贪图眼前小利而不顾严重后果。",
            "example": "靠高利贷维持生活，无异于刀头舔蜜。"
        },
        2579: {
            "pinyin": "dǎo cháng xí gù",
            "meaning": "一味沿袭过去的常规做法，缺乏创新。",
            "example": "办教育不能只是蹈常袭故，更要顺应时代发展。"
        },
        2580: {
            "pinyin": "dǎo jié sǐ yì",
            "meaning": "坚守节操，为了正义和信念宁可牺牲生命。",
            "example": "许多仁人志士蹈节死义，才换来国家的独立。"
        },
        2581: {
            "pinyin": "dǎo lì fèn fā",
            "meaning": "振作精神，奋发努力。",
            "example": "失败之后，他反而蹈厉奋发，更加刻苦训练。"
        },
        2582: {
            "pinyin": "dǎo lì zhī zhì",
            "meaning": "奋勉自励的志向和决心。",
            "example": "少年时立下蹈厉之志，后来果真有所成就。"
        },
        2583: {
            "pinyin": "dǎo qí fù zhé",
            "meaning": "重蹈别人翻车的老路，比喻不吸取教训，再犯前人错误。",
            "example": "若不反思历史，就难免蹈其覆辙。"
        },
        2584: {
            "pinyin": "dǎo rén jiù zhé",
            "meaning": "重蹈他人旧日的失败之路。",
            "example": "他一味模仿前人，结果只是在蹈人旧辙。"
        },
        2585: {
            "pinyin": "dǎo xí fù zhé",
            "meaning": "沿袭陈规旧习，重犯过去的错误。",
            "example": "若改革只流于形式，反而成了蹈袭覆辙。"
        },
        2586: {
            "pinyin": "dǎo shòu jiāo hán",
            "meaning": "本指贾岛、孟郊诗歌清冷瘦硬的风格，后用来形容诗文意境清峭冷峻。",
            "example": "他的绝句多为岛瘦郊寒之作，别具一格。"
        },
        2587: {
            "pinyin": "dǎo fèng diān luán",
            "meaning": "本比喻事物次序颠倒，旧小说中多用作男女交欢的隐语。",
            "example": "这类描写倒凤颠鸾的段落，多半出自话本小说。"
        },
        2588: {
            "pinyin": "dǎo guān luò pèi",
            "meaning": "脱下帽子、摘去佩饰，本指摆脱仕宦礼服，多用以形容放达不拘或辞官归隐。",
            "example": "他早已看淡功名，倒冠落佩，寄情山水。"
        },
        2589: {
            "pinyin": "dǎo gē xiè jiǎ",
            "meaning": "放下兵器和铠甲，比喻停止作战或投降，也可指放弃旧立场。",
            "example": "叛军见大势已去，只得倒戈卸甲，缴械投降。"
        },
        2590: {
            "pinyin": "dǎo hǎi fān jiāng",
            "meaning": "把海水、江水都翻转起来，比喻力量巨大或声势非常浩大。",
            "example": "台风来临前，大海早已倒海翻江般翻涌不息。"
        },
        2591: {
            "pinyin": "dǎo sān diān sì",
            "meaning": "次序颠倒、杂乱无章。",
            "example": "他做事总是倒三颠四，让人不放心。"
        },
        2592: {
            "pinyin": "dǎo shān qīng hǎi",
            "meaning": "能推倒高山、倾覆大海，比喻力量极大或气势极盛。",
            "example": "革命洪流有倒山倾海之势，任何阻力都无法阻挡。"
        },
        2593: {
            "pinyin": "dào míng àn shì",
            "meaning": "在昏暗的世道里窃取名声，比喻以虚假手段在混乱环境中骗取名誉。",
            "example": "他不过是借机盗名暗世的投机分子，并无真才实学。"
        },
        2594: {
            "pinyin": "dào míng qī shì",
            "meaning": "欺骗世人、窃取名誉。",
            "example": "学术界容不得欺世盗名之辈。"
        },
        2595: {
            "pinyin": "dào yì yǒu dào",
            "meaning": "即使是盗贼也有一定的行规，比喻某些人虽不正派，却也有所不为。",
            "example": "连盗亦有道的小偷，都鄙视这种出卖同伴的行为。"
        },
        2596: {
            "pinyin": "dào zēng zhǔ rén",
            "meaning": "贼人最憎恨主人，比喻做坏事的人往往仇视正直之人。",
            "example": "他处处与廉洁干部作对，正应了盗憎主人的古语。"
        },
        2597: {
            "pinyin": "dào zhí zhī wù",
            "meaning": "盗跖：传说中的大盗。指盗贼所得之物，比喻不义之财。",
            "example": "这种靠行贿得来的利益，不过是盗跖之物，终究守不住。"
        },
        2598: {
            "pinyin": "dào zhōng yǎn ěr",
            "meaning": "偷钟时捂住自己的耳朵，以为别人也听不见，比喻自欺欺人。",
            "example": "篡改数据只求蒙混过关，无异于盗钟掩耳。"
        },
        2599: {
            "pinyin": "dào xīn shī tú",
            "meaning": "悼：悲痛；图：谋划。因过于悲痛而失去主张，不知如何是好。",
            "example": "噩耗传来，众人一时悼心失图，不知该如何面对。"
        },
        2600: {
            "pinyin": "dào bàng zhī zhù",
            "meaning": "路旁筑室，比喻必定无法成功的事情。",
            "example": "若不尊重科学规律，一切规划都只是道傍之筑。"
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

    print(f"已为 2501–2600 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
