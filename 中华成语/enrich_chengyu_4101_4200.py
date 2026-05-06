import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 将 4101–4200 号成语的详细信息补充到 enrich 字典中
    enrich = {
        4101: {
            "pinyin": "fán shū kēng rú",
            "meaning": "焚毁典籍、坑杀儒生，比喻残酷摧残文化与知识分子。",
            "example": "历史上燔书坑儒的教训，至今仍令人警醒。"
        },
        4102: {
            "pinyin": "fán huá sǔn zhī",
            "meaning": "繁盛的花朵反而损伤枝干，比喻文采过于华丽会损害文章内容。",
            "example": "写论文要注意简洁明晰，切莫繁华损枝。"
        },
        4103: {
            "pinyin": "fán róng xīng wàng",
            "meaning": "形容事业、经济或城镇等十分繁荣兴盛。",
            "example": "改革开放以后，这座小城逐渐繁荣兴旺起来。"
        },
        4104: {
            "pinyin": "fán xíng zhòng fù",
            "meaning": "刑罚繁多而苛重、赋税沉重，形容苛政酷法。",
            "example": "若一味繁刑重赋，只会激起民怨。"
        },
        4105: {
            "pinyin": "fán zhēng bó yǐn",
            "meaning": "引用多方面的资料作为证明，形容论证时广泛取材。",
            "example": "这篇论文繁征博引，显示了作者扎实的学养。"
        },
        4106: {
            "pinyin": "fǎn bǔ zhī sī",
            "meaning": "幼鸟长大反过来喂养母鸟，比喻子女奉养父母、报答养育之恩。",
            "example": "赡养老人，是每个子女的反哺之私。"
        },
        4107: {
            "pinyin": "fǎn fēng miè huǒ",
            "meaning": "比喻施行德政、教化感人，连风火等灾害仿佛都能止息。",
            "example": "他在任期间勤政爱民，有反风灭火之效。"
        },
        4108: {
            "pinyin": "fǎn fù tuī qiāo",
            "meaning": "一再反复地推敲琢磨，多指对文字或方案仔细斟酌。",
            "example": "这段文字他反复推敲多次，方才定稿。"
        },
        4109: {
            "pinyin": "fǎn fù wú cháng",
            "meaning": "反反复复、变化不定，形容态度或局势极不稳定。",
            "example": "他做事反覆无常，难以让人信赖。"
        },
        4110: {
            "pinyin": "fǎn gōng dǎo suàn",
            "meaning": "对压迫剥削进行反击，重新清算旧账，多用于政治、经济语境。",
            "example": "解放后，贫苦农民掀起了反攻倒算的运动。"
        },
        4111: {
            "pinyin": "fǎn gōng zì zé",
            "meaning": "回过头来责备和反省自己，形容能自我检讨。",
            "example": "出现问题时，应先反躬自责，而不是一味怪别人。"
        },
        4112: {
            "pinyin": "fǎn jiāo pò mǎn",
            "meaning": "抑制骄矜、破除自满，形容保持谦虚谨慎的态度。",
            "example": "在成绩面前更要反骄破满，继续努力。"
        },
        4113: {
            "pinyin": "fǎn jīng hé dào",
            "meaning": "表面上似乎违反经典，其实符合大道理，多指创新而不失根本。",
            "example": "这部作品形式上反经合道，却极具时代精神。"
        },
        4114: {
            "pinyin": "fǎn jīng hé yì",
            "meaning": "貌似背离经常之道，实则合乎义理，多指不拘成规而合情合理。",
            "example": "他此举虽有违常规，却也反经合义。"
        },
        4115: {
            "pinyin": "fǎn pǔ guī zhēn",
            "meaning": "由雕琢复归朴素，由虚华回到真淳，常用来形容艺术风格或人生境界。",
            "example": "历经繁华之后，他的人生观渐渐反朴归真。"
        },
        4116: {
            "pinyin": "fǎn pǔ huán chún",
            "meaning": "由矫饰回到淳厚质朴，含义与“反朴归真”相近。",
            "example": "近年的文学创作多有反朴还淳的倾向。"
        },
        4117: {
            "pinyin": "fǎn qiú fù xīn",
            "meaning": "反穿皮袄、背负柴薪，比喻贫穷劳苦，也比喻愚昧不知本末。",
            "example": "若只顾眼前小利而损害根本，无异于反裘负薪。"
        },
        4118: {
            "pinyin": "fǎn qiú shāng pí",
            "meaning": "皮衣反穿毛在里，皮必受损，比喻愚昧不知本末，顾此失彼。",
            "example": "只图一时便宜，结果反裘伤皮。"
        },
        4119: {
            "pinyin": "fǎn shēn zì wèn",
            "meaning": "回过头来审视、询问自己，形容严于自省。",
            "example": "他每晚都会反身自问，检点一日言行。"
        },
        4120: {
            "pinyin": "fǎn xū rù hún",
            "meaning": "诗文由清虚而入浑成之境，亦可比喻人浑厚无华或浑浑噩噩。",
            "example": "这组诗境界高远，可谓返虚入浑。"
        },
        4121: {
            "pinyin": "fǎn zhào huí guāng",
            "meaning": "亦作“回光返照”，比喻人临死前的短暂清醒，或事物灭亡前的短暂兴旺。",
            "example": "这种表面的繁荣，不过是返照回光而已。"
        },
        4122: {
            "pinyin": "fàn ér wù jiào",
            "meaning": "别人触犯自己也不去计较，形容度量宽宏。",
            "example": "做人当能犯而勿校，不必事事斤斤计较。"
        },
        4123: {
            "pinyin": "fàn yán zhí jiàn",
            "meaning": "说出可能触怒君主的话而直率进谏。",
            "example": "朝中仍需有人敢于犯言直谏。"
        },
        4124: {
            "pinyin": "fàn yán kǔ jiàn",
            "meaning": "不顾得罪对方，以严厉的话语苦口相劝。",
            "example": "老师屡屡犯颜苦谏，只盼他早日醒悟。"
        },
        4125: {
            "pinyin": "fàn fàn zhī tán",
            "meaning": "浮泛空洞、不切实际的言谈。",
            "example": "会议要讲实际问题，切忌泛泛之谈。"
        },
        4126: {
            "pinyin": "fàn hào mó cāng",
            "meaning": "形容文章气象博大高远，如同泛海摩天。",
            "example": "此篇议论宏肆，真有泛浩摩苍之势。"
        },
        4127: {
            "pinyin": "fàn yīng qǔ dāng",
            "meaning": "广泛应对而无不恰当，形容处事得体周全。",
            "example": "胸中义理明白，自能泛应曲当。"
        },
        4128: {
            "pinyin": "fàn zhái fú jiā",
            "meaning": "以船为家，在水上往来漂泊。",
            "example": "昔日他泛宅浮家，浪迹江湖。"
        },
        4129: {
            "pinyin": "fàn lái kāi kǒu",
            "meaning": "饭送到嘴边才肯张口，比喻极端懒惰、坐享其成。",
            "example": "做人不能只知饭来开口，衣来伸手。"
        },
        4130: {
            "pinyin": "fàn lái zhāng kǒu",
            "meaning": "与“饭来开口”同，形容生活过于安逸、坐享其成。",
            "example": "他自幼娇生惯养，习惯饭来张口。"
        },
        4131: {
            "pinyin": "fàn lì rú shū",
            "meaning": "吃粗糙的米饭、蔬菜，形容生活清苦俭朴。",
            "example": "他们在山村饭粝茹蔬，却毫无怨言。"
        },
        4132: {
            "pinyin": "fàn náng jiǔ wèng",
            "meaning": "只会吃饭喝酒，毫无本领，比喻庸碌无用之人。",
            "example": "若做官只知享乐，便成饭囊酒瓮。"
        },
        4133: {
            "pinyin": "fàn náng jiǔ wèng",
            "meaning": "同“饭囊酒瓮”，比喻只会吃喝、不干正事的废物。",
            "example": "朝中岂容这等饭囊酒甕久居其位。"
        },
        4134: {
            "pinyin": "fàn niú tú gǒu",
            "meaning": "给牛喂食、宰杀狗，比喻从事卑贱职业或低下事务。",
            "example": "他虽曾饭牛屠狗，却心怀壮志。"
        },
        4135: {
            "pinyin": "fàn shū yǐn shuǐ",
            "meaning": "吃粗蔬、喝清水，形容生活简朴清苦。",
            "example": "纵使饭蔬饮水，他也不改其志。"
        },
        4136: {
            "pinyin": "fàn shuǐ mó shān",
            "meaning": "比喻仿效他人、依样画葫芦。",
            "example": "写文章切不可一味范水模山。"
        },
        4137: {
            "pinyin": "fáng huàn yú wèi rán",
            "meaning": "在灾祸尚未发生之前就加以防备。",
            "example": "安全工作重在防患于未然。"
        },
        4138: {
            "pinyin": "fáng huò yú wèi rán",
            "meaning": "在祸患尚未发生时加以预防。",
            "example": "治国理政，当思防祸于未然。"
        },
        4139: {
            "pinyin": "fáng méng dù jiàn",
            "meaning": "在坏事刚刚萌芽时就堵塞祸端。",
            "example": "对苗头性问题必须防萌杜渐。"
        },
        4140: {
            "pinyin": "fáng wēi dù xìn",
            "meaning": "在坏事尚处微小、隐蔽阶段时就加以防止。",
            "example": "对腐败问题要防微杜衅于未然。"
        },
        4141: {
            "pinyin": "fáng xīn shè xíng",
            "meaning": "防止杂念、约束行为，注意检点言行。",
            "example": "修身之道，在于防心摄行。"
        },
        4142: {
            "pinyin": "fáng yá è méng",
            "meaning": "在祸患刚刚萌芽时就予以遏制。",
            "example": "对邪风歪气要及早防芽遏萌。"
        },
        4143: {
            "pinyin": "fáng móu dù duàn",
            "meaning": "指房玄龄多谋、杜如晦善断，比喻能人合作、相得益彰。",
            "example": "两位负责人可谓房谋杜断，配合默契。"
        },
        4144: {
            "pinyin": "fáng yú chēng wěi",
            "meaning": "鲂鱼尾巴赤红，比喻忧劳国事或劳苦过度的形象。",
            "example": "他为公事奔走操劳，真有鲂鱼赪尾之状。"
        },
        4145: {
            "pinyin": "fǎng pín wèn kǔ",
            "meaning": "走访贫苦群众，询问疾苦。",
            "example": "干部要常下乡访贫问苦。"
        },
        4146: {
            "pinyin": "fǎng qīn wèn yǒu",
            "meaning": "探望亲戚、朋友，表示关切问候。",
            "example": "逢年过节他总要访亲问友。"
        },
        4147: {
            "pinyin": "fàng pì yín chǐ",
            "meaning": "行为放纵，发展到荒淫奢侈的地步。",
            "example": "亡国之君多因放辟淫侈而失民心。"
        },
        4148: {
            "pinyin": "fàng dá bù jī",
            "meaning": "性情洒脱，不受拘束。",
            "example": "他为人放达不羁，颇有侠客风度。"
        },
        4149: {
            "pinyin": "fàng dàn bù jī",
            "meaning": "言行狂放，不受约束。",
            "example": "这位诗人素以放诞不羁著称。"
        },
        4150: {
            "pinyin": "fàng dàn bù jū",
            "meaning": "行事放纵，不受礼法拘束。",
            "example": "他年轻时性情放诞不拘。"
        },
        4151: {
            "pinyin": "fàng dàn fēng liú",
            "meaning": "行为放荡而又自命风流。",
            "example": "他自诩放诞风流，其实难登大雅之堂。"
        },
        4152: {
            "pinyin": "fàng dàng xíng hái",
            "meaning": "不拘形迹礼法，举止放浪不羁。",
            "example": "文人多有放荡形骸的一面。"
        },
        4153: {
            "pinyin": "fàng diāo bǎ làn",
            "meaning": "刁难勒索、胡作非为。",
            "example": "少数人仗势放刁把滥，群众深恶痛绝。"
        },
        4154: {
            "pinyin": "fàng yīng zhú quǎn",
            "meaning": "放出鹰犬追逐猎物，泛指出猎打围。",
            "example": "贵族们终日放鹰逐犬，荒废正事。"
        },
        4155: {
            "pinyin": "fàng yú rù hǎi",
            "meaning": "把鱼放回大海，比喻彻底解脱或任其自由发展。",
            "example": "他毅然辞官归隐，犹如放鱼入海。"
        },
        4156: {
            "pinyin": "fàng zhū sì hǎi ér jiē zhǔn",
            "meaning": "到处推行都适用，比喻具有普遍适用性的真理或标准。",
            "example": "这个原则放诸四海而皆准。"
        },
        4157: {
            "pinyin": "fàng zòng bù jī",
            "meaning": "行为放纵，不受约束。",
            "example": "他少年时放纵不羁，屡惹祸端。"
        },
        4158: {
            "pinyin": "fàng zòng bù jū",
            "meaning": "放任自己，不受礼法拘束。",
            "example": "若一味放纵不拘，终将自食其果。"
        },
        4159: {
            "pinyin": "fēi jiàng shù jī",
            "meaning": "原指名将李广命运多舛，后泛指才能出众而遭遇不佳。",
            "example": "他屡遭挫折，真有飞将数奇之感。"
        },
        4160: {
            "pinyin": "fēi cāng zǒu huáng",
            "meaning": "苍鹰飞翔、黄狗奔跑，指出猎打围的场景。",
            "example": "贵族们纵马原野，飞苍走黄，不知黎民疾苦。"
        },
        4161: {
            "pinyin": "fēi chú wǎn lì",
            "meaning": "同“飞芻挽粟”，形容急速运送粮草。",
            "example": "后方日夜飞刍挽粒，支援前线。"
        },
        4162: {
            "pinyin": "fēi chú wǎn liáng",
            "meaning": "迅速运送草料和粮食，多形容军需运输的紧急。",
            "example": "诸郡飞刍挽粮，以解前线之急。"
        },
        4163: {
            "pinyin": "fēi chú zhuǎn xiǎng",
            "meaning": "急速运送饷粮，支援前线。",
            "example": "各地飞刍转饷，保证了大军粮草无忧。"
        },
        4164: {
            "pinyin": "fēi dùn lí sú",
            "meaning": "隐遁远离尘俗，过超脱世俗的生活。",
            "example": "他一心向往山林飞遁离俗的日子。"
        },
        4165: {
            "pinyin": "fēi é fù yàn",
            "meaning": "飞蛾投向火焰，比喻自取灭亡或甘冒生命危险。",
            "example": "明知前路凶险，他却如飞蛾赴焰般义无反顾。"
        },
        4166: {
            "pinyin": "fēi é fù zhú",
            "meaning": "飞蛾投向灯烛，比喻明知危险却偏要往上撞。",
            "example": "对于赌博，他简直是飞蛾赴烛。"
        },
        4167: {
            "pinyin": "fēi é pū huǒ",
            "meaning": "比喻自投罗网、自取灭亡。",
            "example": "铤而走险者，无异于飞蛾扑火。"
        },
        4168: {
            "pinyin": "fēi gōng xiàn jiǎ",
            "meaning": "频频传杯、开怀畅饮。",
            "example": "席间宾主飞觥献斝，其乐融融。"
        },
        4169: {
            "pinyin": "fēi gōng zǒu jiǎ",
            "meaning": "与“飞觥献斝”义近，形容酒宴上频繁传杯。",
            "example": "堂上笙歌鼎沸，飞觥走斝不绝。"
        },
        4170: {
            "pinyin": "fēi hóng tà xuě",
            "meaning": "大雁踏过雪地，比喻往事遗留的痕迹。",
            "example": "故人旧事，如飞鸿踏雪，虽淡却难忘。"
        },
        4171: {
            "pinyin": "fēi hóng xuě zhǎo",
            "meaning": "同“雪泥鸿爪”，比喻往事遗留下来的痕迹。",
            "example": "那几封书信，不过人生中的飞鸿雪爪。"
        },
        4172: {
            "pinyin": "fēi huáng téng tà",
            "meaning": "本形容骏马奔腾，后多比喻官职、地位迅速上升。",
            "example": "他一朝飞黄腾踏，令人侧目。"
        },
        4173: {
            "pinyin": "fǎ chū yī mén",
            "meaning": "法律出自同一门径，比喻法令统一、前后一致。",
            "example": "治理国家，当求法出一门，杜绝各行其是。"
        },
        4174: {
            "pinyin": "fǎ jiǔ shén zhēn",
            "meaning": "神奇高明的针炙医术。",
            "example": "老中医法灸神针，妙手回春。"
        },
        4175: {
            "pinyin": "fǎ mài zhǔn shéng",
            "meaning": "比喻可资遵循的法则、标准。",
            "example": "这些经典著作，实为后学之法脉准绳。"
        },
        4176: {
            "pinyin": "fǎ wú èr mén",
            "meaning": "法律没有两样的门径，比喻法令统一，不可因人而异。",
            "example": "依法治国，贵在法无二门。"
        },
        4177: {
            "pinyin": "fǎ wú kě dài",
            "meaning": "依法不可宽恕，形容罪行严重。",
            "example": "此辈罪大恶极，实属法无可贷。"
        },
        4178: {
            "pinyin": "fān kē dǎo jiù",
            "meaning": "打破旧有格式或成法，另出新意。",
            "example": "这篇文章番窠倒臼，颇具创意。"
        },
        4179: {
            "pinyin": "fān lái fù qù",
            "meaning": "指动作或事情反复多次。",
            "example": "他番来覆去地思量这个问题。"
        },
        4180: {
            "pinyin": "fān rán huǐ wù",
            "meaning": "态度突然转变而深刻悔悟。",
            "example": "几经挫折，他终于幡然悔悟。"
        },
        4181: {
            "pinyin": "fān cháng jiǎo dù",
            "meaning": "形容内心极度思念或非常不安。",
            "example": "他一夜翻肠搅肚，难以入眠。"
        },
        4182: {
            "pinyin": "fān huáng dǎo zào",
            "meaning": "颠倒黑白、混淆是非。",
            "example": "谣言往往翻黄倒皂，迷惑人心。"
        },
        4183: {
            "pinyin": "fān huáng dǎo zào",
            "meaning": "同“翻黄倒皂”，比喻颠倒是非、混淆黑白。",
            "example": "他惯于翻黄倒皂，为自己开脱。"
        },
        4184: {
            "pinyin": "fān jiāng jiǎo hǎi",
            "meaning": "形容水势浩大，亦比喻力量或声势极其壮大，或形容闹得很凶。",
            "example": "会场上争论激烈，几乎要翻江搅海。"
        },
        4185: {
            "pinyin": "fān shǒu yún fù shǒu yǔ",
            "meaning": "一翻手为云，一覆手成雨，比喻反复无常或任意操纵局势。",
            "example": "他在商场上翻手云覆手雨，手段颇为老辣。"
        },
        4186: {
            "pinyin": "fān tiān zuò dì",
            "meaning": "形容闹得很凶，局势被搅得天翻地覆。",
            "example": "几家媒体炒作此事，几乎翻天作地。"
        },
        4187: {
            "pinyin": "fán cái qiǎn shí",
            "meaning": "自谦才能平庸、见识肤浅。",
            "example": "我不过凡才浅识，尚望诸位多多指教。"
        },
        4188: {
            "pinyin": "fán ǒu jìn qì",
            "meaning": "多用作自谦，指平凡浅近的才识或人物。",
            "example": "以我凡偶近器之见，不足为训。"
        },
        4189: {
            "pinyin": "fán tāi ròu yǎn",
            "meaning": "指凡人的肉眼，看不出高深玄妙之理。",
            "example": "此景在凡胎肉眼看来，不过寻常山水。"
        },
        4190: {
            "pinyin": "fán tāi zhuó tǐ",
            "meaning": "指凡人的浊重肉身，多用作自谦。",
            "example": "自叹凡胎浊体，怎敢妄论仙道。"
        },
        4191: {
            "pinyin": "fán wén rù lǐ",
            "meaning": "繁琐多余的礼节或文书手续。",
            "example": "这些烦文缛礼早该精简。"
        },
        4192: {
            "pinyin": "fǎn tīng nèi shì",
            "meaning": "反听外界、内视自身，既能听取意见又能反省自我。",
            "example": "为政者当善于反听内视，广纳谏言。"
        },
        4193: {
            "pinyin": "fǎn tīng shōu shì",
            "meaning": "收敛耳目、反求诸己，比喻不为外物所惑，专注内省。",
            "example": "学道之人需反听收视，以静养心。"
        },
        4194: {
            "pinyin": "fǎn zhèng bō luàn",
            "meaning": "整顿混乱局面，使之恢复正常秩序。",
            "example": "新政上台，以反正拨乱为己任。"
        },
        4195: {
            "pinyin": "fǎn zhèng huán chún",
            "meaning": "复归于朴实淳厚，同“反朴还淳”。",
            "example": "社会风尚当反正还淳，摒弃浮华。"
        },
        4196: {
            "pinyin": "fǎn liǎn wú qíng",
            "meaning": "翻脸变为无情，形容态度骤变，不顾旧情。",
            "example": "一旦牵涉利益，他立刻反脸无情。"
        },
        4197: {
            "pinyin": "fǎn běn cháo yuán",
            "meaning": "返回根本本源，多用以形容修养达到本真境界。",
            "example": "修行在于返本朝元，复其本性。"
        },
        4198: {
            "pinyin": "fǎn běn huán yuán",
            "meaning": "同“返本还源”，指返回本原、恢复本来面目。",
            "example": "儒释道皆言返本还元之旨。"
        },
        4199: {
            "pinyin": "fǎn běn huán yuán",
            "meaning": "本、原：根本、本源。指返回本原状态或根源所在。",
            "example": "他主张文化应返本还源，从经典中汲取营养。"
        },
        4200: {
            "pinyin": "fǎn guān nèi shì",
            "meaning": "回过头来观照内心，指自我反省。",
            "example": "遇事多些返观内视，方能少犯错误。"
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

    print(f"已为 4101–4200 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
