import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 将 4001–4100 号成语的详细信息补充到 enrich 字典中
    enrich = {
        4001: {
            "pinyin": "fù zhī yī jù",
            "meaning": "把东西一把火烧掉，比喻彻底毁掉或抛弃。",
            "example": "多年心血顷刻付之一炬，令人扼腕。"
        },
        4002: {
            "pinyin": "fù zhī yī tàn",
            "meaning": "对无法挽回的事情只好叹息一下，表示惋惜而无可奈何。",
            "example": "对那些错失的良机，也只能付之一叹。"
        },
        4003: {
            "pinyin": "fù zhī yī xiào",
            "meaning": "用一笑来对待，表示毫不在意或认为不值一提。",
            "example": "面对流言蜚语，他一概付之一笑。"
        },
        4004: {
            "pinyin": "fù zhū dōng liú",
            "meaning": "像流水向东流去一样不可挽回，比喻希望、努力等全部落空。",
            "example": "项目被迫叫停，多年投入几乎付诸东流。"
        },
        4005: {
            "pinyin": "fù zhū hóng qiáo",
            "meaning": "典出古人托书于洪乔而被焚毁的故事，比喻书信文稿被烧毁或计划落空。",
            "example": "那封遗稿竟被误作废纸，付诸洪乔。"
        },
        4006: {
            "pinyin": "fù dé gū ēn",
            "meaning": "做出有负德行、辜负恩情的事，形容恩将仇报、不念旧情。",
            "example": "对如此照顾过自己的人，他断不可负德辜恩。"
        },
        4007: {
            "pinyin": "fù ēn mèi liáng",
            "meaning": "辜负别人的恩德、泯灭自己的良心，形容忘恩负义。",
            "example": "忘记师长栽培之恩，无异于负恩昧良。"
        },
        4008: {
            "pinyin": "fù jīng qǐng zuì",
            "meaning": "背着荆条上门请罪，出自廉颇负荆请罪的典故，比喻主动承认错误、诚恳道歉。",
            "example": "他意识到自己错怪了朋友，特地登门负荆请罪。"
        },
        4009: {
            "pinyin": "fù lǎo xié yòu",
            "meaning": "扶着老人、携带幼儿，多形容一家老小同行，或战乱中百姓扶老携幼逃难的情景。",
            "example": "灾后逃难的人们扶老携幼，场面十分凄凉。"
        },
        4010: {
            "pinyin": "fù nú qián qū",
            "meaning": "以劣马在前作引导，比喻自谦甘作先驱或以微薄之力为大家开路。",
            "example": "此事愿我负驽前驱，先去探路。"
        },
        4011: {
            "pinyin": "fù qì dòu hěn",
            "meaning": "凭着一口怨气去争斗狠拼，形容因意气用事而与人争斗。",
            "example": "他年轻时常为小事负气斗狠，闹出不少矛盾。"
        },
        4012: {
            "pinyin": "fù qì zhàng yì",
            "meaning": "凭着一腔怒气去打抱不平，形容性情刚烈、因义而出头。",
            "example": "他为同事负气仗义，却也常因此得罪人。"
        },
        4013: {
            "pinyin": "fù qū hán yuān",
            "meaning": "背负着委屈、心中含有冤屈，形容长期得不到申诉的郁结。",
            "example": "多年来他负屈含冤，却始终没有机会辩白。"
        },
        4014: {
            "pinyin": "fù qū xián yuān",
            "meaning": "肩负屈辱、心怀冤屈，含义与“负屈含冤”相近。",
            "example": "历史上不少清官一度负屈衔冤。"
        },
        4015: {
            "pinyin": "fù xīn wéi yuàn",
            "meaning": "负心违背誓愿，形容对感情或承诺不忠实。",
            "example": "他轻易许下承诺，又转身负心违愿。"
        },
        4016: {
            "pinyin": "fù xīn jiù huǒ",
            "meaning": "背着柴薪去救火，比喻办法错误，非但不能解决问题，反而使之更严重。",
            "example": "只顾刺激消费而忽视风险管理，无异于负薪救火。"
        },
        4017: {
            "pinyin": "fù xīn zhī yōu",
            "meaning": "像背着柴薪走在火边一样的忧虑，比喻隐伏着难以解除的大祸患。",
            "example": "若监管缺位，金融体系难免有负薪之忧。"
        },
        4018: {
            "pinyin": "fù yú wán kàng",
            "meaning": "据守险要之地而顽强抵抗，形容在绝境中仍不肯投降。",
            "example": "守军负隅顽抗，誓死不退。"
        },
        4019: {
            "pinyin": "fù zhòng zhì yuǎn",
            "meaning": "肩负重任才能走得更远，比喻担当重责以成就长远事业。",
            "example": "青年一代应当勇于负重致远。"
        },
        4020: {
            "pinyin": "fù ěr dī yán",
            "meaning": "把嘴贴近耳朵低声说话，形容窃窃私语或偷偷叮嘱。",
            "example": "两人附耳低言，不知在商量什么。"
        },
        4021: {
            "pinyin": "fù fū luò máo",
            "meaning": "原形容箭术高妙，箭矢贴着皮肤掠过，仅射落毛发，后比喻赋闲无事或游手好闲。",
            "example": "他整日无所事事，简直是附肤落毛般的消磨光阴。"
        },
        4022: {
            "pinyin": "fù jì míng zhāng",
            "meaning": "依附有声望的人而使自己的名声显著。",
            "example": "他不过是附骥名彰，真正有本事的另有其人。"
        },
        4023: {
            "pinyin": "fù jì pān hóng",
            "meaning": "攀附骏马与鸿鹄，比喻依附他人以求成名或飞黄腾达。",
            "example": "与其一味附骥攀鸿，不如脚踏实地提升自己。"
        },
        4024: {
            "pinyin": "fù shàng wǎng xià",
            "meaning": "附和君上而欺骗臣下，比喻对上巴结、对下蒙骗。",
            "example": "这种附上罔下的官吏最招人痛恨。"
        },
        4025: {
            "pinyin": "fù yōng fēng yǎ",
            "meaning": "本无真才实学却勉强参加文酒清谈，假装风雅有文化。",
            "example": "他对艺术一知半解，却爱附庸风雅。"
        },
        4026: {
            "pinyin": "fù zhuì xuán yóu",
            "meaning": "像身上的赘肉和悬着的疣一样，比喻多余而累赘的事物。",
            "example": "这些重复机构简直是附赘悬疣，亟待精简。"
        },
        4027: {
            "pinyin": "fù dǎo qián zhé",
            "meaning": "再次踏上从前车轮走过的道路，比喻重犯旧错。",
            "example": "若忽视安全隐患，只会复蹈前辙。"
        },
        4028: {
            "pinyin": "fù jiù rú chū",
            "meaning": "恢复到最初的样子，形容损坏或变化后的事物又回复原状。",
            "example": "古建筑经过修缮，已复旧如初。"
        },
        4029: {
            "pinyin": "fù tāng dǎo huǒ",
            "meaning": "赴汤和蹈火，比喻不避艰险，奋不顾身。",
            "example": "为救灾群众，他愿意赴汤蹈火。"
        },
        4030: {
            "pinyin": "fù xiǎn rú yí",
            "meaning": "把非常危险的事看得像平地一样平常，形容临危不惧、勇往直前。",
            "example": "战士们赴险如夷，毫不退缩。"
        },
        4031: {
            "pinyin": "fù cí zǐ xiào",
            "meaning": "父亲慈爱、儿女孝顺，形容家庭关系融洽。",
            "example": "这家人父慈子孝，街坊们都十分羡慕。"
        },
        4032: {
            "pinyin": "fù mǔ ēn qín",
            "meaning": "父母养育子女既有深恩又极其勤劳，形容父母对子女含辛茹苦的付出。",
            "example": "想到父母恩勤，他更不敢懈怠。"
        },
        4033: {
            "pinyin": "fù mǔ zhī bāng",
            "meaning": "父母居住的国家或故乡，多指自己出生长大的地方。",
            "example": "远离父母之邦多年，他十分思念家乡。"
        },
        4034: {
            "pinyin": "fù wéi zǐ yǐn",
            "meaning": "父亲为儿子隐瞒过错，出自《论语》，强调亲情超过法理。",
            "example": "古语有云父为子隐，子为父隐，乃人情之常。"
        },
        4035: {
            "pinyin": "fù yán zǐ xiào",
            "meaning": "父亲严厉、子女孝顺，形容家庭有严教却仍相亲相爱。",
            "example": "他自幼家教甚严，可谓父严子孝。"
        },
        4036: {
            "pinyin": "fù guì bī rén",
            "meaning": "富贵之势压迫别人，形容仗势凌人或富贵令人侧目。",
            "example": "他一身珠光宝气，真有几分富贵逼人的气派。"
        },
        4037: {
            "pinyin": "fù guì bù néng yín",
            "meaning": "出自《孟子》，指一个人即使身处富贵也不能使其放纵为恶，形容品格高尚。",
            "example": "他为人刚正，真可谓富贵不能淫。"
        },
        4038: {
            "pinyin": "fù guì fú yún",
            "meaning": "把荣华富贵看得像浮云一样轻淡，形容不慕名利。",
            "example": "在他心里，富贵浮云，只有学术最重要。"
        },
        4039: {
            "pinyin": "fù guì jiāo rén",
            "meaning": "仗着富贵而对人骄横无礼，也指富贵本身足以令人敬畏。",
            "example": "有人一朝得势便富贵骄人。"
        },
        4040: {
            "pinyin": "fù guì róng huá",
            "meaning": "富裕的生活和显赫的地位，泛指荣华富贵。",
            "example": "他看透了富贵荣华，只求平淡安稳。"
        },
        4041: {
            "pinyin": "fù guó ān mín",
            "meaning": "使国家富足、百姓安乐，形容施政得当、社会安定。",
            "example": "历代贤相皆以富国安民为己任。"
        },
        4042: {
            "pinyin": "fù guó qiáng bīng",
            "meaning": "使国家富裕、军队强大，形容国力日益增强。",
            "example": "改革数十年，使得富国强兵的目标逐步实现。"
        },
        4043: {
            "pinyin": "fù kě dí guó",
            "meaning": "财富多得足以跟一个国家相比，形容极为富有。",
            "example": "这位财阀富可敌国，却行事低调。"
        },
        4044: {
            "pinyin": "fù lì táng huáng",
            "meaning": "华丽富贵、气势堂皇，多形容建筑或陈设。",
            "example": "宫殿内部富丽堂皇，金碧辉煌。"
        },
        4045: {
            "pinyin": "fù liè táo bái",
            "meaning": "财富可与古代巨富陶朱公和白圭相匹敌，形容极其富有。",
            "example": "商贾累世经营，富埒陶白。"
        },
        4046: {
            "pinyin": "fù miàn bǎi chéng",
            "meaning": "本指南面称王、统辖百城，后比喻藏书极为丰富。",
            "example": "他家中藏书富面百城，令人叹服。"
        },
        4047: {
            "pinyin": "fù zài zhī zú",
            "meaning": "认为懂得满足就是最大的富有，形容知足常乐的心态。",
            "example": "他一向主张富在知足，不与人攀比。"
        },
        4048: {
            "pinyin": "fù jī zhī lì",
            "meaning": "连捆绑一只鸡的力气都没有，形容体力非常弱小。",
            "example": "他自谦不过缚鸡之力。"
        },
        4049: {
            "pinyin": "fù bèi shòu dí",
            "meaning": "前后都遭到敌人的攻击，形容处境十分艰难。",
            "example": "部队在山谷中腹背受敌，被迫突围。"
        },
        4050: {
            "pinyin": "fù bèi zhī máo",
            "meaning": "背上和腹部的毛，比喻无足轻重的事物。",
            "example": "与国家大事相比，这点损失不过腹背之毛。"
        },
        4051: {
            "pinyin": "fù fěi xīn bàng",
            "meaning": "心里暗暗诽谤埋怨别人。",
            "example": "他嘴上不说，心里却腹诽心谤。"
        },
        4052: {
            "pinyin": "fù xīn xiāng zhào",
            "meaning": "彼此心意相通、互相理解。",
            "example": "多年的战友情让他们腹心相照。"
        },
        4053: {
            "pinyin": "fù xīn zhī jí",
            "meaning": "比喻关乎国家存亡或个人安危的严重问题，也指根深蒂固的病症。",
            "example": "腐败问题已成腹心之疾，非下猛药不可。"
        },
        4054: {
            "pinyin": "fù yǒu lín jiǎ",
            "meaning": "腹中似藏鳞甲，比喻心机深沉、为人阴险。",
            "example": "他城府极深，真有几分腹有鳞甲之态。"
        },
        4055: {
            "pinyin": "fù zǎi wǔ chē",
            "meaning": "肚里好像装着五车书，比喻学识渊博。",
            "example": "这位学者腹载五车，谈吐间旁征博引。"
        },
        4056: {
            "pinyin": "fù zhōng bīng jiǎ",
            "meaning": "肚子里有兵有甲，比喻胸中自有谋略和主张。",
            "example": "他胸有成竹，真可谓腹中兵甲。"
        },
        4057: {
            "pinyin": "fù cháo wú wán luǎn",
            "meaning": "鸟巢覆灭，蛋也没有一个完整的，比喻整体毁坏后个体难以幸免。",
            "example": "局势一旦全面失控，覆巢无完卵。"
        },
        4058: {
            "pinyin": "fù chē zhī guǐ",
            "meaning": "车子翻覆的轨迹，比喻前人的失败经验教训。",
            "example": "前车之覆，后人当以覆车之轨为戒。"
        },
        4059: {
            "pinyin": "fù chē zhī jiàn",
            "meaning": "翻车的教训，比喻值得引以为鉴的失败事例。",
            "example": "这些失败案例都是覆车之鉴。"
        },
        4060: {
            "pinyin": "fù chē zhī jiè",
            "meaning": "翻车的警戒，比喻可资戒惧的前车之覆。",
            "example": "历史上的教训应当成为覆车之戒。"
        },
        4061: {
            "pinyin": "fù dì fān tiān",
            "meaning": "形容变化或斗争的声势极大，如同把大地翻转、天空倒覆。",
            "example": "一场革新运动在全国掀起覆地翻天之势。"
        },
        4062: {
            "pinyin": "fù hǎi yí shān",
            "meaning": "把海水翻覆、山岳移动，比喻力量巨大、变化极其惊人。",
            "example": "科技的发展在短短几十年里已是覆海移山。"
        },
        4063: {
            "pinyin": "fù pén zhī yuān",
            "meaning": "像倒扣的盆子一样蒙在头上的冤屈，比喻极深而难以申雪的冤情。",
            "example": "这桩旧案一直是一宗覆盆之冤。"
        },
        4064: {
            "pinyin": "fù shuǐ nán shōu",
            "meaning": "倒出去的水难以收回，比喻事情一旦做出就难以挽回。",
            "example": "话已出口，覆水难收，只能尽力弥补。"
        },
        4065: {
            "pinyin": "fù wáng wú rì",
            "meaning": "覆灭灭亡之日已经不远，形容局势岌岌可危。",
            "example": "内忧外患之下，这个政权早已覆亡无日。"
        },
        4066: {
            "pinyin": "fù yǔ fān yún",
            "meaning": "一会儿下雨、一会儿翻卷乌云，比喻人反复无常或局势变化莫测。",
            "example": "他在两派之间覆雨翻云，难以信任。"
        },
        4067: {
            "pinyin": "fù zhōu zhī jiè",
            "meaning": "船覆的教训，比喻沉痛的前车之鉴。",
            "example": "金融危机应成为后来者的覆舟之戒。"
        },
        4068: {
            "pinyin": "fù shé shì shǒu, zhuàng shì jiě wàn",
            "meaning": "被毒蛇咬住手时，壮士宁可断腕求生，比喻为保全大局而坚决舍弃局部。",
            "example": "面对严重亏损业务，只能蝮蛇螫手，壮士解腕。"
        },
        4069: {
            "pinyin": "fù gū bó xī",
            "meaning": "婆婆与儿媳闹不和，形容家庭内部的妇女争吵。",
            "example": "老屋里常有妇姑勃谿之声。"
        },
        4070: {
            "pinyin": "fù rén zhī rén",
            "meaning": "借指妇人心地过于仁软，不忍施以刑罚，比喻缺乏应有的果断。",
            "example": "治乱世不能妇人之仁。"
        },
        4071: {
            "pinyin": "fù rú jiē zhī",
            "meaning": "妇女和儿童都知道，形容人所共知、极其明显。",
            "example": "这个道理妇孺皆知，却总有人偏要违背。"
        },
        4072: {
            "pinyin": "shǔ hòu xīng gū",
            "meaning": "典出诗句“曙后一星孤”，后用以指人死后只留下一个孤女。",
            "example": "战乱之后，只剩她一人，真是曙后星孤。"
        },
        4073: {
            "pinyin": "wú kě jiù yào",
            "meaning": "病重到药也救不了，比喻坏到无可挽回的地步。",
            "example": "一味纵容腐败，最终必至无可救药。"
        },
        4074: {
            "pinyin": "fā nù chuān guàn",
            "meaning": "怒发上冲把帽子顶穿，形容极度愤怒。",
            "example": "听闻此事，他几乎要发怒穿冠。"
        },
        4075: {
            "pinyin": "fā yǒng chōng guàn",
            "meaning": "怒发直竖、跃然而起，把帽子顶起，形容愤怒到极点。",
            "example": "众人被这番话激得发踊冲冠。"
        },
        4076: {
            "pinyin": "fā zhí chuān guàn",
            "meaning": "头发竖直而把帽子顶穿，形容怒极或惊愕之状。",
            "example": "闻此噩耗，士兵无不发植穿冠。"
        },
        4077: {
            "pinyin": "fā cái zhì fù",
            "meaning": "赚到钱财并逐渐富裕起来，多用于号召或目标。",
            "example": "乡亲们靠特色农业发财经富。"
        },
        4078: {
            "pinyin": "fā fèn tú qiáng",
            "meaning": "振作精神、立志图强，形容下定决心努力进取。",
            "example": "面对落后局面，他暗下决心发奋图强。"
        },
        4079: {
            "pinyin": "fā hūn zhāng dì shí yī",
            "meaning": "戏称发昏到第十一章，形容昏头昏脑的状态。",
            "example": "被他这一通解释，大家都听得发昏章第十一。"
        },
        4080: {
            "pinyin": "fā jiā zhì fù",
            "meaning": "创立家业并获得富裕生活，多指通过劳动和经营致富。",
            "example": "乡村要想发家致富，离不开教育和技术。"
        },
        4081: {
            "pinyin": "fā kē dǎ hùn",
            "meaning": "说笑话、打趣逗乐，多用于戏曲或相声等表演中。",
            "example": "他擅长发科打诨，经常把观众逗得前仰后合。"
        },
        4082: {
            "pinyin": "fā méng jiě fù",
            "meaning": "启发蒙昧、解除束缚，比喻启迪心智、开阔眼界。",
            "example": "这本书对青年读者颇有发蒙解缚之功。"
        },
        4083: {
            "pinyin": "fā nù chōng guàn",
            "meaning": "怒气冲天，头发竖起把帽子顶起，形容极度愤怒。",
            "example": "听到侵略者暴行，人们无不发怒冲冠。"
        },
        4084: {
            "pinyin": "fā shàng chōng guàn",
            "meaning": "头发向上冲起把帽子顶起，形容愤怒到极点。",
            "example": "他被冤枉得发上冲冠。"
        },
        4085: {
            "pinyin": "fā shàng zhǐ guàn",
            "meaning": "头发竖起直指帽子，形容极度愤怒或激动。",
            "example": "这番话说得他几乎发上指冠。"
        },
        4086: {
            "pinyin": "fā wū qiú lí",
            "meaning": "拆屋捉狸，比喻因小失大，处理事情方法过于激烈。",
            "example": "为了一点小错就全面否定，是发屋求狸的做法。"
        },
        4087: {
            "pinyin": "fā xiàn bù lìng",
            "meaning": "发布法令、颁布命令，形容宣布政令。",
            "example": "新朝发宪布令，整顿吏治。"
        },
        4088: {
            "pinyin": "fā yǐn tī fú",
            "meaning": "揭露隐蔽的坏人坏事，形容吏治严明。",
            "example": "清官发隐擿伏，肃清了一方邪气。"
        },
        4089: {
            "pinyin": "fā zōng zhǐ shǐ",
            "meaning": "追寻线索并指使行动，多指幕后主使。",
            "example": "真正发踪指使的人还未被抓获。"
        },
        4090: {
            "pinyin": "fā zōng zhǐ shì",
            "meaning": "发出踪迹、指明方向，比喻揭示线索。",
            "example": "这几条证据足以发踪指示真凶。"
        },
        4091: {
            "pinyin": "fā zòng zhǐ shǐ",
            "meaning": "放纵部下并加以指使，多指背后操纵他人做坏事。",
            "example": "幕后主脑发纵指使，多次挑起事端。"
        },
        4092: {
            "pinyin": "fā zòng zhǐ shì",
            "meaning": "放纵与指示，形容纵容某种行为并暗中指点。",
            "example": "有人在背后发纵指示，煽动闹事。"
        },
        4093: {
            "pinyin": "fá bīng zhī jiā",
            "meaning": "古代贵族冬天仍食冰的家庭，比喻生活讲究、出身高贵。",
            "example": "他出自伐冰之家，自幼衣食无忧。"
        },
        4094: {
            "pinyin": "fá máo huàn suǐ",
            "meaning": "削皮去毛、换骨移髓，比喻彻底改造、脱胎换骨。",
            "example": "只要痛下决心改革，机构也能伐毛换髓。"
        },
        4095: {
            "pinyin": "fá yì dǎng tóng",
            "meaning": "打击不同派别而拉拢同党，形容政治上排斥异己、结党营私。",
            "example": "他一味伐异党同，最终失尽人心。"
        },
        4096: {
            "pinyin": "fá zuì diào mín",
            "meaning": "讨伐罪人、抚恤百姓，形容出兵有正当理由并关心民生。",
            "example": "古代一些讨伐行动自称伐罪吊民。"
        },
        4097: {
            "pinyin": "fá zuì diào rén",
            "meaning": "讨伐罪人、安抚百姓，与“伐罪吊民”义近。",
            "example": "这次出兵号称伐罪吊人。"
        },
        4098: {
            "pinyin": "fǎ bù chuán liù ěr",
            "meaning": "机密的道理或口诀不向六只耳朵以上的人传授，形容秘不外传。",
            "example": "师父一再叮嘱，此术法不传六耳。"
        },
        4099: {
            "pinyin": "fǎ chū duō mén",
            "meaning": "法规命令由多个部门同时发布，形容制度混乱、标准不一。",
            "example": "若管理权过于分散，必致法出多门。"
        },
        4100: {
            "pinyin": "fán shū kēng rú",
            "meaning": "同“焚书坑儒”，指焚烧典籍、坑杀儒生的暴行。",
            "example": "历史上燔书阬儒的教训发人深省。"
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

    print(f"已为 4001–4100 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
