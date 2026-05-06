import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 为 101–200 条成语添加拼音、释义和例句
    enrich = {
        101: {
            "pinyin": "ān shì rú cháng",
            "meaning": "安稳舒适，和往常一样。",
            "example": "节后工作逐渐恢复安适如常。"
        },
        102: {
            "pinyin": "ān tǔ zhòng qiān",
            "meaning": "留恋故土，不愿轻易迁移。",
            "example": "老人安土重迁，不想离开老家。"
        },
        103: {
            "pinyin": "ān wēi xiāng yì",
            "meaning": "安宁与危险互相转化、交替出现。",
            "example": "世事多变，安危相易，须居安思危。"
        },
        104: {
            "pinyin": "ān wēi yǔ gòng",
            "meaning": "共同面对安全和危难，患难与共。",
            "example": "真正的朋友会与你安危与共。"
        },
        105: {
            "pinyin": "ān xián zì dé",
            "meaning": "安适悠闲，自我满足。",
            "example": "退休后他在乡下过得安闲自得。"
        },
        106: {
            "pinyin": "ān xián zì zài",
            "meaning": "安逸悠闲，自然自在。",
            "example": "周末在家看看书，十分安闲自在。"
        },
        107: {
            "pinyin": "ān xīn dìng zhì",
            "meaning": "安心下来，坚定志向。",
            "example": "只有安心定志，才能学有所成。"
        },
        108: {
            "pinyin": "ān yíng zhá zhài",
            "meaning": "安置营地，扎下营寨。",
            "example": "部队在河边安营扎寨，准备休整。"
        },
        109: {
            "pinyin": "ān yú gù sú, nì yú jiù wén",
            "meaning": "安于旧俗，沉溺旧见，不愿接受新事物。",
            "example": "如果总是安于故俗，溺于旧闻，就难有进步。"
        },
        110: {
            "pinyin": "ān yú xiàn zhuàng",
            "meaning": "满足于现在的状况，不求改变。",
            "example": "年轻人不应安于现状，要勇于突破。"
        },
        111: {
            "pinyin": "ān yú yī yú",
            "meaning": "安守一隅，比喻目光狭隘，只顾小范围。",
            "example": "做学问不能安于一隅，要放眼天下。"
        },
        112: {
            "pinyin": "ān zhái zhèng lù",
            "meaning": "安守家宅，走正道行事。",
            "example": "父母希望子女安宅正路，不走歪门邪道。"
        },
        113: {
            "pinyin": "ān zhěn ér wò",
            "meaning": "枕稳而卧，睡得安稳。",
            "example": "一切安排妥当，他终于可以安枕而卧。"
        },
        114: {
            "pinyin": "ān zhī ruò mìng",
            "meaning": "像对待命运一样安然接受。",
            "example": "既然事实已定，也只好安之若命。"
        },
        115: {
            "pinyin": "ān zhī ruò sù",
            "meaning": "把异常情况当作平常对待，毫不在意。",
            "example": "面对误解，他安之若素，继续做好本职工作。"
        },
        116: {
            "pinyin": "ān zuò dài bì",
            "meaning": "坐着等待灭亡，比喻不作努力坐以待毙。",
            "example": "遇到困难不能安坐待毙，要主动想办法。"
        },
        117: {
            "pinyin": "ān bù lí mǎ, jiǎ bù lí shēn",
            "meaning": "随时披甲上马，形容时刻准备作战。",
            "example": "边防将士鞍不离马，甲不离身。"
        },
        118: {
            "pinyin": "ān mǎ láo dùn",
            "meaning": "长途奔波，骑马赶路而十分劳累。",
            "example": "一路鞍马劳顿，他们终于抵达目的地。"
        },
        119: {
            "pinyin": "ān mǎ láo kùn",
            "meaning": "形容旅途奔波，十分疲惫。",
            "example": "他鞍马劳困，却仍坚持完成任务。"
        },
        120: {
            "pinyin": "ān mǎ zhī láo",
            "meaning": "鞍马奔走之劳，多指征战或奔波辛苦。",
            "example": "这些年他奔走四方，颇费鞍马之劳。"
        },
        121: {
            "pinyin": "ān qián mǎ hòu",
            "meaning": "在马前马后服侍，形容随侍左右、忙前忙后。",
            "example": "他常在老板鞍前马后，处理各种杂事。"
        },
        122: {
            "pinyin": "àn dú láo xíng",
            "meaning": "文书工作劳累形体，形容案牍繁多、工作辛苦。",
            "example": "科室事务繁杂，他每日案牍劳形。"
        },
        123: {
            "pinyin": "àn bīng bù dòng",
            "meaning": "按住军队不调动，比喻按兵不发，静观其变。",
            "example": "他暂时按兵不动，等待最佳时机出手。"
        },
        124: {
            "pinyin": "àn bù jiù bān",
            "meaning": "按照一定步骤和次序行事。",
            "example": "项目推进要按部就班，不能一味求快。"
        },
        125: {
            "pinyin": "àn jiǎ qǐn bīng",
            "meaning": "脱下铠甲，让士兵休息，表示停止战争。",
            "example": "战事平定后，朝廷下令按甲寝兵。"
        },
        126: {
            "pinyin": "àn jiǎ xiū bīng",
            "meaning": "收起甲兵，休整军队。",
            "example": "边境安宁，可以按甲休兵养民生息。"
        },
        127: {
            "pinyin": "àn míng zé shí",
            "meaning": "根据名义或职名去考核其实绩。",
            "example": "选人用人应按名责实，看重实际能力。"
        },
        128: {
            "pinyin": "àn nà bù zhù",
            "meaning": "无法抑制情绪或冲动。",
            "example": "听到这个好消息，他按捺不住激动的心情。"
        },
        129: {
            "pinyin": "àn pèi xú xíng",
            "meaning": "拉着马缰缓缓前行，比喻从容不迫。",
            "example": "他们按辔徐行，欣赏沿途风景。"
        },
        130: {
            "pinyin": "àn tú suǒ jì",
            "meaning": "按照图本寻找好马，比喻按线索、凭经验办事。",
            "example": "学习不能死记硬背按图索骥，要灵活运用。"
        },
        131: {
            "pinyin": "àn xíng zì yì",
            "meaning": "克制自己的行为和欲望。",
            "example": "面对诱惑，他能按行自抑，不逾规矩。"
        },
        132: {
            "pinyin": "àn rán shāng shén",
            "meaning": "神情黯淡，忧伤不乐。",
            "example": "听到噩耗，他不禁黯然伤神。"
        },
        133: {
            "pinyin": "àn rán shī sè",
            "meaning": "神情黯淡，失去光彩。",
            "example": "与高手一比，他原本得意的作品顿时黯然失色。"
        },
        134: {
            "pinyin": "àn rán xiāo hún",
            "meaning": "极度哀伤，像灵魂都要消散。",
            "example": "离别之夜，他独自黯然销魂。"
        },
        135: {
            "pinyin": "àn dàn wú guāng",
            "meaning": "颜色暗淡，没有光泽。",
            "example": "久经风雨，墙上的油漆已经暗淡无光。"
        },
        136: {
            "pinyin": "àn dù chén cāng",
            "meaning": "表面上走一条路，暗地里另有行动，比喻暗中进行活动。",
            "example": "他明修栈道，暗渡陈仓，最终取得主动。"
        },
        137: {
            "pinyin": "àn jiàn nán fáng",
            "meaning": "暗中的冷箭难以防备，比喻暗算难以提防。",
            "example": "职场中最怕暗箭难防的流言中伤。"
        },
        138: {
            "pinyin": "àn jiàn shāng rén",
            "meaning": "指暗中伤害别人。",
            "example": "光明正大竞争，不要搞暗箭伤人。"
        },
        139: {
            "pinyin": "àn mèi zhī shì",
            "meaning": "见不得光的勾当或事情。",
            "example": "这种暗昧之事一旦曝光，必然遭人唾弃。"
        },
        140: {
            "pinyin": "àn qì àn nǎo",
            "meaning": "心中郁闷恼怒，却不明说。",
            "example": "他对这件事颇为不满，心里暗气暗恼。"
        },
        141: {
            "pinyin": "àn ruò wú duàn",
            "meaning": "性情软弱，缺乏主见。",
            "example": "为人处事若暗弱无断，很难令人信服。"
        },
        142: {
            "pinyin": "àn shì bù qī",
            "meaning": "在无人看见的地方也不做亏心事。",
            "example": "他一向严于律己，做到暗室不欺。"
        },
        143: {
            "pinyin": "àn shì féng dēng",
            "meaning": "在黑暗的屋子里遇到灯，比喻在困境中遇到希望。",
            "example": "贵人相助，对他来说如同暗室逢灯。"
        },
        144: {
            "pinyin": "àn shì kuī xīn",
            "meaning": "在暗中做亏心事。",
            "example": "做人切不可暗室亏心，自欺欺人。"
        },
        145: {
            "pinyin": "àn shì qī xīn",
            "meaning": "在无人处做见不得人的事，欺骗自己的良心。",
            "example": "即使没有人知道，也别暗室欺心。"
        },
        146: {
            "pinyin": "àn shì qiú wù",
            "meaning": "在黑暗的屋里寻找东西，比喻摸不着门径。",
            "example": "不懂方法，学习就像暗室求物。"
        },
        147: {
            "pinyin": "àn sòng qiū bō",
            "meaning": "暗中递送眼色，比喻偷偷传情或示意。",
            "example": "剧中两人频频暗送秋波，引得观众会心一笑。"
        },
        148: {
            "pinyin": "àn wú tiān rì",
            "meaning": "黑暗得看不见天日，比喻社会黑暗或境况极端悲惨。",
            "example": "旧社会多少人生活在暗无天日之中。"
        },
        149: {
            "pinyin": "àn xiāng shū yǐng",
            "meaning": "幽暗的香气与稀疏的影子，多用来形容梅花。",
            "example": "词人用\"暗香疏影\"写尽梅花风姿。"
        },
        150: {
            "pinyin": "àn zhōng mō suǒ",
            "meaning": "比喻在没有经验或线索的情况下摸索前进。",
            "example": "刚开始做项目时，他也是在暗中摸索。"
        },
        151: {
            "pinyin": "áng cáng qī chǐ",
            "meaning": "身材高大挺拔。",
            "example": "那位将军昂藏七尺，气宇轩昂。"
        },
        152: {
            "pinyin": "áng rán zì dé",
            "meaning": "神态高昂，自我满足。",
            "example": "比赛获胜后，他显得昂然自得。"
        },
        153: {
            "pinyin": "áng shǒu kuò bù",
            "meaning": "抬头大步行走，形容气概豪迈、自信。",
            "example": "青年们昂首阔步走进新时代。"
        },
        154: {
            "pinyin": "áng shǒu shēn méi",
            "meaning": "抬头伸眉，形容得意自豪的神态。",
            "example": "任务完成得好，他终于可以昂首伸眉了。"
        },
        155: {
            "pinyin": "áng shǒu tiān wài",
            "meaning": "昂首向天，比喻志向远大。",
            "example": "年轻人应当昂首天外，胸怀理想。"
        },
        156: {
            "pinyin": "áng shǒu tǐng xiōng",
            "meaning": "抬头挺胸，形容自信、精神饱满。",
            "example": "他昂首挺胸走上讲台，毫不怯场。"
        },
        157: {
            "pinyin": "áng shǒu wàng tiān",
            "meaning": "抬头望天，形容愤慨或沉思的样子。",
            "example": "他仰面长叹，昂首望天良久。"
        },
        158: {
            "pinyin": "àng yú xiāng jī",
            "meaning": "盎与盂互相撞击，比喻争执不休或声音杂乱。",
            "example": "双方争论得如盎盂相击，难分高下。"
        },
        159: {
            "pinyin": "àng yú xiāng qiāo",
            "meaning": "盎与盂互相敲击，比喻纷争不休或声音杂乱。",
            "example": "会场上议论纷纷，仿佛盎盂相敲。"
        },
        160: {
            "pinyin": "áo áo dài bǔ",
            "meaning": "形容小儿饥饿时张口待哺的样子，比喻急切盼望救济。",
            "example": "灾区群众嗷嗷待哺，需要及时救援。"
        },
        161: {
            "pinyin": "áo cháng guā dǔ",
            "meaning": "形容饥饿难忍或思念焦急。",
            "example": "等了半天饭还没上，他早已熬肠刮肚。"
        },
        162: {
            "pinyin": "áo gēng shǒu yè",
            "meaning": "熬长夜守更点，形容连夜工作或值班。",
            "example": "医生为救病人熬更守夜。"
        },
        163: {
            "pinyin": "áo jiāng xiā cù",
            "meaning": "比喻心中酸楚烦闷。",
            "example": "想到往事，他不禁熬姜呷醋，十分难受。"
        },
        164: {
            "pinyin": "áo qīng shǒu dàn",
            "meaning": "在清苦淡泊中坚守操守。",
            "example": "他一生熬清守淡，远离名利。"
        },
        165: {
            "pinyin": "áo xīn fèi lì",
            "meaning": "耗费心思与力气。",
            "example": "这本书是作者熬心费力写成的。"
        },
        166: {
            "pinyin": "ào bù kě cháng",
            "meaning": "骄傲自满的情绪不可以滋长。",
            "example": "取得成绩后更要警惕傲不可长。"
        },
        167: {
            "pinyin": "ào gǔ lín lín",
            "meaning": "形容骨气高傲、坚贞不屈。",
            "example": "他一身傲骨嶙嶙，绝不向恶势力低头。"
        },
        168: {
            "pinyin": "ào màn bù xùn",
            "meaning": "傲慢无礼，不肯顺从。",
            "example": "他为人傲慢不逊，很难与人合作。"
        },
        169: {
            "pinyin": "ào màn shǎo lǐ",
            "meaning": "骄傲自大，很少讲礼貌。",
            "example": "对长辈傲慢少礼是很不合适的。"
        },
        170: {
            "pinyin": "ào nì dé zhì",
            "meaning": "得志后目空一切，态度傲慢。",
            "example": "他稍有成绩便傲睨得志，令人反感。"
        },
        171: {
            "pinyin": "ào nì wàn wù",
            "meaning": "目空一切，轻视众人。",
            "example": "做人不可傲睨万物，应懂得尊重他人。"
        },
        172: {
            "pinyin": "ào nì yī shì",
            "meaning": "轻视当世所有的人。",
            "example": "他才华出众，却不该傲睨一世。"
        },
        173: {
            "pinyin": "ào nì zì ruò",
            "meaning": "傲慢地斜视，神情自若。",
            "example": "他对众人不屑一顾，神态傲睨自若。"
        },
        174: {
            "pinyin": "ào rán yì lì",
            "meaning": "昂然挺立，不可动摇。",
            "example": "松树在风雪中傲然屹立。"
        },
        175: {
            "pinyin": "ào shì qīng wù",
            "meaning": "看不起世人和事物。",
            "example": "他自命不凡，常有傲世轻物之态。"
        },
        176: {
            "pinyin": "ào shuāng dòu xuě",
            "meaning": "不畏霜雪侵袭，形容品格高洁坚贞。",
            "example": "梅花傲霜斗雪，迎寒绽放。"
        },
        177: {
            "pinyin": "ào tóu ào nǎo",
            "meaning": "形容神情傲慢、自以为是。",
            "example": "他一副傲头傲脑的样子，让人难以亲近。"
        },
        178: {
            "pinyin": "ào xián màn shì",
            "meaning": "轻视贤者，有才之士。",
            "example": "统治者若傲贤慢士，必招致贤才远离。"
        },
        179: {
            "pinyin": "ào xuě líng shuāng",
            "meaning": "在雪中凌霜而立，形容品格高洁不屈。",
            "example": "翠竹傲雪凌霜，四季常青。"
        },
        180: {
            "pinyin": "ào xuě qī shuāng",
            "meaning": "在雪中欺压霜寒，比喻不畏严寒艰苦。",
            "example": "这些小树傲雪欺霜，在风雪中挺立。"
        },
        181: {
            "pinyin": "ào miào wú qióng",
            "meaning": "精深奇妙，没有穷尽。",
            "example": "中国文化奥妙无穷，值得细细体会。"
        },
        182: {
            "pinyin": "ào huǐ wú jí",
            "meaning": "后悔也来不及了。",
            "example": "事前不多加思量，事后懊悔无及。"
        },
        183: {
            "pinyin": "ē bí dì yù",
            "meaning": "佛教语，极其痛苦的地狱。",
            "example": "小说中描写的战场如同阿鼻地狱。"
        },
        184: {
            "pinyin": "ā gǒu ā māo",
            "meaning": "泛指无名小辈或普通人。",
            "example": "这些阿狗阿猫也敢妄加评论。"
        },
        185: {
            "pinyin": "ā gū ā wēng",
            "meaning": "泛指姑姑、翁翁等长辈。",
            "example": "过年时，家中阿姑阿翁都回来团聚。"
        },
        186: {
            "pinyin": "ā jiā ā wēng",
            "meaning": "泛指家中的长辈。",
            "example": "村里阿家阿翁都来参加喜宴。"
        },
        187: {
            "pinyin": "ā jiāo jīn wū",
            "meaning": "出自典故，为所宠爱的人建金屋相待。",
            "example": "他为了心爱的妻子，几乎要阿娇金屋般地宠爱。"
        },
        188: {
            "pinyin": "ā māo ā gǒu",
            "meaning": "与\"阿狗阿猫\"同，指无足轻重的小人物。",
            "example": "这种场合岂是阿猫阿狗能随便进来的。"
        },
        189: {
            "pinyin": "ē pí dì yù",
            "meaning": "佛教语，极苦之地狱，与阿鼻地狱同义。",
            "example": "旧社会底层人民的生活好似阿毗地狱。"
        },
        190: {
            "pinyin": "ā píng jué dǎo",
            "meaning": "形容被逗得大笑不止。",
            "example": "他的相声表演让观众阿平绝倒。"
        },
        191: {
            "pinyin": "āi hóng biàn dì",
            "meaning": "到处都是悲惨呼号的人民。",
            "example": "战乱使村庄哀鸿遍地，民不聊生。"
        },
        192: {
            "pinyin": "āi huǐ jí lì",
            "meaning": "形容因悲哀过度而身体极度消瘦。",
            "example": "多年守孝，他几乎哀毁瘠立。"
        },
        193: {
            "pinyin": "āi shēng tàn qì",
            "meaning": "不断叹息，表示忧愁烦闷。",
            "example": "他整天愁眉苦脸，哀声叹气。"
        },
        194: {
            "pinyin": "ái dòng shòu è",
            "meaning": "忍受寒冷和饥饿。",
            "example": "流浪汉在街头挨冻受饿，十分可怜。"
        },
        195: {
            "pinyin": "ái jiān dié bèi",
            "meaning": "肩挨肩、背靠背，形容人多拥挤。",
            "example": "节日里广场上人群挨肩迭背。"
        },
        196: {
            "pinyin": "ái jiān dié bèi",
            "meaning": "同\"挨肩迭背\"，形容人挤得很紧。",
            "example": "车厢里挤得挨肩叠背。"
        },
        197: {
            "pinyin": "ái mén ái hù",
            "meaning": "挨家挨户，一户一户地。",
            "example": "工作人员挨门挨户做问卷调查。"
        },
        198: {
            "pinyin": "ái fēng jī fèng",
            "meaning": "在风中来回缝补，比喻生活艰辛。",
            "example": "她靠街边裁缝摊谋生，整日捱风缉缝。"
        },
        199: {
            "pinyin": "ái sān dǐng sì",
            "meaning": "形容人多拥挤或事情接连不断。",
            "example": "顾客捱三顶四地进店，把店里挤得满满当当。"
        },
        200: {
            "pinyin": "ái sān dǐng wǔ",
            "meaning": "形容时间紧、事情多或人群拥挤。",
            "example": "他这几天事务繁忙，真是捱三顶五。"
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

    print(f"已为 101–200 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
