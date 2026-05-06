import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 为 601–700 条成语添加拼音、释义和例句
    enrich = {
        601: {
            "pinyin": "bèi cháng jiān kǔ",
            "meaning": "经历过各种艰难困苦。",
            "example": "创业多年，他早已备尝艰苦。"
        },
        602: {
            "pinyin": "bèi cháng xīn kǔ",
            "meaning": "饱受辛劳和困苦。",
            "example": "为了这个项目，团队成员备尝辛苦。"
        },
        603: {
            "pinyin": "bèi duō lì fēn",
            "meaning": "准备很多力量分散使用，比喻分散精力去做许多事情。",
            "example": "他事务太多，备多力分，难免顾此失彼。"
        },
        604: {
            "pinyin": "bèi wèi chōng shù",
            "meaning": "只是占个位置，用来充数，没有真才实学。",
            "example": "他不愿在岗位上只是备位充数。"
        },
        605: {
            "pinyin": "bèi běn qū mò",
            "meaning": "舍弃根本而追求末节，比喻抛弃主要的而追求次要的。",
            "example": "只重盈利忽视质量，是典型的背本趋末。"
        },
        606: {
            "pinyin": "bèi chéng jiè yī",
            "meaning": "背城借一战，指背靠城池，下最后决心打一仗。",
            "example": "军队在此背城借一，誓死抵抗。"
        },
        607: {
            "pinyin": "bèi chéng yī zhàn",
            "meaning": "同“背城借一”，背水一战的意思。",
            "example": "面对强敌，他们只能背城一战。"
        },
        608: {
            "pinyin": "bèi dào ér chí",
            "meaning": "走的路和正确方向相反，比喻行动和目的相违背。",
            "example": "若一味追求形式，就会与教育初衷背道而驰。"
        },
        609: {
            "pinyin": "bèi ēn wàng yì",
            "meaning": "忘掉别人的恩德，背弃情义。",
            "example": "他不念旧情，实在是背恩忘义。"
        },
        610: {
            "pinyin": "bèi jǐng lí xiāng",
            "meaning": "离开家乡，到外地生活。",
            "example": "他年少时就背井离乡，到外地闯荡。"
        },
        611: {
            "pinyin": "bèi méng bài yuē",
            "meaning": "背弃盟约和契约。",
            "example": "凡是背盟败约之举，都要受到谴责。"
        },
        612: {
            "pinyin": "bèi shān qǐ lóu",
            "meaning": "背靠着山建房，比喻借重外力来发展。",
            "example": "这处宅院背山起楼，风景极佳。"
        },
        613: {
            "pinyin": "bèi shuǐ yī zhàn",
            "meaning": "背靠河水进行决战，比喻下定决心作最后一搏。",
            "example": "球队在决赛中只能背水一战。"
        },
        614: {
            "pinyin": "bèi xìn qì yì",
            "meaning": "背弃信用和情义。",
            "example": "在金钱面前，他选择背信弃义。"
        },
        615: {
            "pinyin": "bèi què zhū gōng",
            "meaning": "珍珠铺就的宫殿，形容极其华丽的宫室。",
            "example": "传说海底有贝阙珠宫，金碧辉煌。"
        },
        616: {
            "pinyin": "bēn yì jué chén",
            "meaning": "奔跑迅疾，尘土都被抛在后面，比喻速度极快或成绩遥遥领先。",
            "example": "他在赛场上奔逸绝尘，无人能及。"
        },
        617: {
            "pinyin": "bēn zǒu hū háo",
            "meaning": "奔走呼喊，形容为某件事四处奔波呼吁。",
            "example": "志愿者们为救灾募捐奔走呼号。"
        },
        618: {
            "pinyin": "bēn zǒu xiāng gào",
            "meaning": "奔走相互告知，形容消息传播迅速。",
            "example": "好消息一出，乡亲们奔走相告。"
        },
        619: {
            "pinyin": "bēn zǒu zuān yíng",
            "meaning": "为谋取私利到处奔走钻营。",
            "example": "他整日奔走钻营，只为升官发财。"
        },
        620: {
            "pinyin": "běn lái miàn mù",
            "meaning": "事物原来的样子或真实面目。",
            "example": "经过调查，事情的本来面目终于揭示出来。"
        },
        621: {
            "pinyin": "běn mò dào zhì",
            "meaning": "本末颠倒，把主要的和次要的弄反。",
            "example": "学习只重分数不重能力，是本末倒置。"
        },
        622: {
            "pinyin": "běn tóng mò yì",
            "meaning": "本质相同而末节不同。",
            "example": "这些方案本同末异，关键在执行。"
        },
        623: {
            "pinyin": "běn xiàng bì lù",
            "meaning": "真实的面目完全显露出来。",
            "example": "随着调查深入，某些腐败分子的本相毕露。"
        },
        624: {
            "pinyin": "běn xiǎo lì wēi",
            "meaning": "本钱很小，利润很微薄。",
            "example": "小摊生意本小利微，却也养家糊口。"
        },
        625: {
            "pinyin": "běn xìng nán yí",
            "meaning": "人的本性难以改变。",
            "example": "他虽努力克制，仍时常急躁，本性难移。"
        },
        626: {
            "pinyin": "bèn niǎo xiān fēi",
            "meaning": "笨鸟先飞，比喻能力不足的人先下功夫，以弥补不足。",
            "example": "我资质平平，只能像笨鸟先飞那样多下功夫。"
        },
        627: {
            "pinyin": "bèn zuǐ zhuō shé",
            "meaning": "嘴笨、口才差。",
            "example": "他虽然笨嘴拙舌，却很讲信用。"
        },
        628: {
            "pinyin": "bī shàng liáng shān",
            "meaning": "被迫上梁山，比喻被逼造反或走上极端道路。",
            "example": "他不是好斗之人，也是被逼上梁山。"
        },
        629: {
            "pinyin": "bí xī rú léi",
            "meaning": "呼吸声像雷声一样大，形容睡觉打鼾很响。",
            "example": "他睡着后鼻息如雷，把室友都吵醒了。"
        },
        630: {
            "pinyin": "bǐ bǎo mò hān",
            "meaning": "下笔酣畅，墨色饱满，形容写字作画极为得意。",
            "example": "书法家挥毫泼墨，真是笔饱墨酣。"
        },
        631: {
            "pinyin": "bǐ dà rú chuán",
            "meaning": "形容文笔雄健有力，也指重要的文稿。",
            "example": "他年轻时就能写出笔大如椽的文章。"
        },
        632: {
            "pinyin": "bǐ gēng yàn tián",
            "meaning": "以笔墨为耕，以砚台为田，比喻勤奋写作。",
            "example": "作家终日笔耕砚田，作品不断问世。"
        },
        633: {
            "pinyin": "bǐ mò guān sī",
            "meaning": "通过文字争论的是非曲直，比喻文字上的纠纷。",
            "example": "两家公司因广告语产生了一场笔墨官司。"
        },
        634: {
            "pinyin": "bǐ sǎo qiān jūn",
            "meaning": "一挥笔就能摧毁千军，比喻文笔犀利、气势雄壮。",
            "example": "他的评论文章真可谓笔扫千军。"
        },
        635: {
            "pinyin": "bǐ xià chāo shēng",
            "meaning": "落笔就能使人脱离罪责，比喻掌握生杀予夺的大权。",
            "example": "在古代，有些权臣一言九鼎，笔下超生。"
        },
        636: {
            "pinyin": "bǐ xià shēng huā",
            "meaning": "形容文笔生动优美，如同在纸上开花。",
            "example": "她写景如画，真是笔下生花。"
        },
        637: {
            "pinyin": "bǐ zǒu lóng shé",
            "meaning": "形容书法笔势有力，如龙蛇飞动。",
            "example": "他的草书笔走龙蛇，极有气势。"
        },
        638: {
            "pinyin": "bǐ zhū mò fá",
            "meaning": "用文章笔墨进行讨伐，形容舆论的批判力量。",
            "example": "记者用犀利文笔对腐败现象笔诛墨伐。"
        },
        639: {
            "pinyin": "bǐ zhòu zuò yè",
            "meaning": "把白天当夜晚用，比喻日夜操劳。",
            "example": "工人们俾昼作夜，加紧赶工。"
        },
        640: {
            "pinyin": "bǐ chàng bù jīng",
            "meaning": "手执匕首和祭酒也不惊惶，形容在危险面前沉着镇定。",
            "example": "他在危机中仍匕鬯不惊，从容应对。"
        },
        641: {
            "pinyin": "bǐ bǐ jiē shì",
            "meaning": "到处都是，形容极为常见。",
            "example": "身边的好例子比比皆是，要善于学习。"
        },
        642: {
            "pinyin": "bǐ jiān bìng qǐ",
            "meaning": "众多的人或事物同时并肩兴起。",
            "example": "新兴企业在这座城市比肩并起。"
        },
        643: {
            "pinyin": "bǐ jiān ér lì",
            "meaning": "肩挨着肩地站立，形容人多拥挤或团结一致。",
            "example": "队伍中的士兵比肩而立，整齐有序。"
        },
        644: {
            "pinyin": "bǐ jiān jì zhǒng",
            "meaning": "肩挨肩、脚跟擦着脚跟，形容人很多、非常拥挤。",
            "example": "节日期间，街上行人比肩继踵。"
        },
        645: {
            "pinyin": "bǐ jiān qí shēng",
            "meaning": "肩并肩地一起发声，比喻众人一起响应。",
            "example": "群众比肩齐声，高喊口号。"
        },
        646: {
            "pinyin": "bǐ lèi cóng shì",
            "meaning": "按照同类事物类比来处理事情。",
            "example": "研究时要善于比类从事，举一反三。"
        },
        647: {
            "pinyin": "bǐ shàng bù zú, bǐ xià yǒu yú",
            "meaning": "同比自己强的相比就不够，看比自己弱的就有余，劝人知足常乐。",
            "example": "做人要学会比上不足，比下有余。"
        },
        648: {
            "pinyin": "bǐ wū kě fēng",
            "meaning": "家家户户都可以用来表彰，形容道德风尚极好。",
            "example": "当时社会民风淳朴，几乎比屋可封。"
        },
        649: {
            "pinyin": "bǐ wù cǐ zhì",
            "meaning": "借事物来表达自己的心志。",
            "example": "诗人常借景抒情，比物此志。"
        },
        650: {
            "pinyin": "bǐ yì lián zhī",
            "meaning": "比喻夫妻恩爱，永不分离。",
            "example": "他们伉俪情深，如同比翼连枝。"
        },
        651: {
            "pinyin": "bǐ yì qí fēi",
            "meaning": "比翼鸟成双齐飞，比喻夫妻或情侣情深意笃。",
            "example": "新人携手走上红毯，仿佛比翼齐飞。"
        },
        652: {
            "pinyin": "bǐ yì shuāng fēi",
            "meaning": "同“比翼齐飞”，多形容感情深厚。",
            "example": "他们恩爱有加，终身比翼双飞。"
        },
        653: {
            "pinyin": "bǐ chàng cǐ hè",
            "meaning": "这边作歌，那边附和，比喻互相呼应。",
            "example": "两位诗人彼倡此和，唱和不绝。"
        },
        654: {
            "pinyin": "bǐ jié wǒ yíng",
            "meaning": "对方亏损而我方充盈，比喻敌弱我强。",
            "example": "若能节约资源，便可彼竭我盈。"
        },
        655: {
            "pinyin": "bǐ yī shí, cǐ yī shí",
            "meaning": "那是一个时候，这是一个时候，形容情况已发生变化。",
            "example": "如今形势早非当年，真是彼一时，此一时。"
        },
        656: {
            "pinyin": "bǐ zhòng wǒ guǎ",
            "meaning": "对方人多而我方人少。",
            "example": "在敌众我寡的情况下，只能固守待援。"
        },
        657: {
            "pinyin": "bǐ lìn fù méng",
            "meaning": "原已克服的吝啬之心又重新滋生。",
            "example": "他本想大方些，不料鄙吝复萌。"
        },
        658: {
            "pinyin": "bǐ yú bù xiè",
            "meaning": "觉得不值得去做，表示轻视。",
            "example": "这种小利他向来鄙于不屑。"
        },
        659: {
            "pinyin": "bì bù náo běi",
            "meaning": "坚决不向北方退缩，形容毫不退让。",
            "example": "面对压力，他立誓必不挠北。"
        },
        660: {
            "pinyin": "bì gōng bì jìng",
            "meaning": "十分恭敬而不怠慢。",
            "example": "他对长辈一向必恭必敬。"
        },
        661: {
            "pinyin": "bì lǐ chí lí",
            "meaning": "本为佛经用语，后用来形容心神不定、疑虑重重。",
            "example": "他听闻此事，难免必里迟离。"
        },
        662: {
            "pinyin": "bì yóu zhī lù",
            "meaning": "一定要经过的道路，比喻必不可少的途径。",
            "example": "提高素质是走向成功的必由之路。"
        },
        663: {
            "pinyin": "bì zhēng zhī dì",
            "meaning": "双方一定要争夺的要地。",
            "example": "这座关隘历来是兵家必争之地。"
        },
        664: {
            "pinyin": "bì guān què sǎo",
            "meaning": "关起门来打扫庭院，比喻闭门自修或拒客谢访。",
            "example": "他近来闭关却扫，专心著书。"
        },
        665: {
            "pinyin": "bì guān suǒ guó",
            "meaning": "封闭关口，与世隔绝的政策。",
            "example": "近代的闭关锁国使国家错失发展机遇。"
        },
        666: {
            "pinyin": "bì guān zì shǒu",
            "meaning": "关起门来自己防守，不与外界交往。",
            "example": "企业若一味闭关自守，就会被时代淘汰。"
        },
        667: {
            "pinyin": "bì hù dú shū",
            "meaning": "关上门在家读书，形容专心学习。",
            "example": "他闭户读书数年，学问大有长进。"
        },
        668: {
            "pinyin": "bì kǒu bù yán",
            "meaning": "紧闭嘴巴，一句话也不说。",
            "example": "他对这件事闭口不言。"
        },
        669: {
            "pinyin": "bì kǒu cáng shé",
            "meaning": "闭住嘴巴，把舌头藏起来，比喻默不作声。",
            "example": "他平日多言，今天却闭口藏舌。"
        },
        670: {
            "pinyin": "bì mén gēng",
            "meaning": "吃闭门羹，比喻被人拒之门外。",
            "example": "他多次上门，却总是吃闭门羹。"
        },
        671: {
            "pinyin": "bì mén hān gē",
            "meaning": "关起门来纵情歌唱，多形容自得其乐。",
            "example": "他常独自在家闭门酣歌。"
        },
        672: {
            "pinyin": "bì mén mì jù",
            "meaning": "关起门来反复推敲句子，形容用心写作。",
            "example": "诗人闭门觅句，只为写出传世佳作。"
        },
        673: {
            "pinyin": "bì mén què sǎo",
            "meaning": "同“闭关却扫”，也指隐居读书或谢绝往来。",
            "example": "他近几年闭门却扫，很少露面。"
        },
        674: {
            "pinyin": "bì mén sī guò",
            "meaning": "关起门来反省自己的过错。",
            "example": "犯错之后，他被要求闭门思过。"
        },
        675: {
            "pinyin": "bì mén tóu xiá",
            "meaning": "关闭大门，将车辖投入门内，表示谢客。",
            "example": "他因病闭门投辖，不再应酬宾客。"
        },
        676: {
            "pinyin": "bì mén zào chē",
            "meaning": "关起门来造车，比喻不了解实际情况，主观办事。",
            "example": "制定政策不能闭门造车，要深入基层。"
        },
        677: {
            "pinyin": "bì mù sāi tīng",
            "meaning": "闭上眼睛，堵住耳朵，比喻对外界情况一概不问。",
            "example": "对问题闭目塞听，只会错失良机。"
        },
        678: {
            "pinyin": "bì sāi yǎn jīng zhuō má què",
            "meaning": "蒙住眼睛抓麻雀，比喻盲目行动。",
            "example": "不做调查就下结论，无异于闭塞眼睛捉麻雀。"
        },
        679: {
            "pinyin": "bì yuè xiū huā",
            "meaning": "月亮躲藏、花儿羞惭，比喻女子容貌极为美丽。",
            "example": "她貌若天仙，真有闭月羞花之姿。"
        },
        680: {
            "pinyin": "bì gōng bì jìng",
            "meaning": "十分恭敬，多形容态度极其庄重。",
            "example": "他向老师行礼时毕恭毕敬。"
        },
        681: {
            "pinyin": "bì qí gōng yú yī yì",
            "meaning": "把全部力量用在一件事情上，一举完成。",
            "example": "这次改革要毕其功于一役，不能半途而废。"
        },
        682: {
            "pinyin": "bì gǔ sàng tún",
            "meaning": "敲破鼓丢掉猪，原指礼物微薄，后多用作谦辞。",
            "example": "这点薄礼，不过敝鼓丧豚，请勿见笑。"
        },
        683: {
            "pinyin": "bì zhǒu qiān jīn",
            "meaning": "自家破扫帚也当成千金之宝，比喻对自己东西的偏爱。",
            "example": "他对旧物情有独钟，可谓敝帚千金。"
        },
        684: {
            "pinyin": "bì zhǒu zì zhēn",
            "meaning": "破扫帚也自己珍惜，比喻对自己的事物特别爱护。",
            "example": "这书虽然旧了，他仍敝帚自珍。"
        },
        685: {
            "pinyin": "bì lù lán lǚ",
            "meaning": "披荆斩棘、跋山涉水，形容创业的艰辛。",
            "example": "先辈们筚路蓝缕，才有今天的成就。"
        },
        686: {
            "pinyin": "bì mén guī dòu",
            "meaning": "简陋的门和小窗，比喻家境贫寒。",
            "example": "他出身筚门闺窦，却自强不息。"
        },
        687: {
            "pinyin": "bì chē léi mǎ",
            "meaning": "破车瘦马，形容行装简陋或境况艰苦。",
            "example": "他们驾着弊车羸马，踏上漫长旅途。"
        },
        688: {
            "pinyin": "bì jué fēng qīng",
            "meaning": "弊端消除，风气清明。",
            "example": "经过整顿，官场渐有弊绝风清之象。"
        },
        689: {
            "pinyin": "bì hǎi qīng tiān",
            "meaning": "碧蓝的海水和青天，比喻环境优美或前途光明。",
            "example": "站在海边，只见碧海青天，一片澄明。"
        },
        690: {
            "pinyin": "bì luò huáng quán",
            "meaning": "天上人间的遥远距离，比喻相隔极远或生死悬殊。",
            "example": "他们自此天各一方，如同碧落黄泉。"
        },
        691: {
            "pinyin": "bì xuè dān xīn",
            "meaning": "碧绿的血、赤红的心，比喻忠诚的爱国之心。",
            "example": "革命烈士以碧血丹心谱写历史。"
        },
        692: {
            "pinyin": "bì lǐ ròu shēng",
            "meaning": "大腿内侧长出肥肉，比喻久不出战而养尊处优。",
            "example": "他自感髀里肉生，难以再上战场。"
        },
        693: {
            "pinyin": "bì ròu fù shēng",
            "meaning": "同“髀里肉生”，形容久处安逸而荒废志气。",
            "example": "长久闲居，让他有了髀肉复生的惭愧。"
        },
        694: {
            "pinyin": "bì zuò fū rén",
            "meaning": "婢女做了夫人，比喻地位突然显赫起来。",
            "example": "他从小职员到高管，宛如婢作夫人。"
        },
        695: {
            "pinyin": "bì zhòng yán gān",
            "meaning": "礼物丰厚、言语甜蜜，比喻用重礼和花言巧语去拉拢别人。",
            "example": "面对币重言甘的游说，他仍然不为所动。"
        },
        696: {
            "pinyin": "bì cōng sāi míng",
            "meaning": "蒙蔽听觉，遮塞视线，比喻被欲望或偏见蒙蔽。",
            "example": "若被私心蔽聪塞明，就难以公正判断。"
        },
        697: {
            "pinyin": "bì rì gān yún",
            "meaning": "遮住太阳直插云霄，形容声势浩大或树木高大。",
            "example": "城中高楼林立，几乎蔽日干云。"
        },
        698: {
            "pinyin": "bì ér bù tán",
            "meaning": "有意回避某个话题而不去谈论。",
            "example": "提到自己的失误时，他总是避而不谈。"
        },
        699: {
            "pinyin": "bì hài jiù lì",
            "meaning": "避开害处，追求好处。",
            "example": "做决策要趋利避害，而不是避害就利。"
        },
        700: {
            "pinyin": "bì huò jiù fú",
            "meaning": "躲开灾祸，走向幸福。",
            "example": "他及时调整方向，总算避祸就福。"
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

    print(f"已为 601–700 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
