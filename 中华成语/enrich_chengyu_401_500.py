import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 为 401–500 条成语添加拼音、释义和例句
    enrich = {
        401: {
            "pinyin": "bǎi bān fèng cheng",
            "meaning": "用尽一切方式恭维奉承。",
            "example": "面对上司，他百般奉承，只求得到赏识。"
        },
        402: {
            "pinyin": "bǎi bì cóng shēng",
            "meaning": "各种弊端一齐产生、层出不穷。",
            "example": "监管不严，导致行业内百弊丛生。"
        },
        403: {
            "pinyin": "bǎi bù shī yī",
            "meaning": "百次中几乎没有一次失误，形容准确率极高。",
            "example": "他的计算几乎百不失一，非常可靠。"
        },
        404: {
            "pinyin": "bǎi bù yī cún",
            "meaning": "百件事中几乎没有一件幸存，多形容损失惨重。",
            "example": "一场洪水下来，庄稼百不一存。"
        },
        405: {
            "pinyin": "bǎi chǐ gān tóu, gèng jìn yī bù",
            "meaning": "比喻在已有成绩的基础上继续努力，更进一步。",
            "example": "学习已经很好了，还要百尺竿头，更进一步。"
        },
        406: {
            "pinyin": "bǎi chuān guī hǎi",
            "meaning": "众多河流都流入大海，比喻事物终归有个总的归宿。",
            "example": "各方意见最终会百川归海，形成共识。"
        },
        407: {
            "pinyin": "bǎi cí mò biàn",
            "meaning": "讲上一百句也不能辩白清楚，形容百口莫辩的处境。",
            "example": "流言四起，让他百辞莫辩。"
        },
        408: {
            "pinyin": "bǎi dài guò kè",
            "meaning": "一代又一代都是过客，比喻人生短暂、世事无常。",
            "example": "古今人物皆是百代过客。"
        },
        409: {
            "pinyin": "bǎi dài wén zōng",
            "meaning": "历代文学的宗师，指影响极大的文学家。",
            "example": "杜甫被尊为百代文宗。"
        },
        410: {
            "pinyin": "bǎi dú bù yàn",
            "meaning": "形容文章或书籍非常精彩，反复阅读也不感到厌倦。",
            "example": "这本名著让人百读不厌。"
        },
        411: {
            "pinyin": "bǎi dǔ jiē zuò",
            "meaning": "到处筑墙建屋，形容大兴土木、建设繁忙。",
            "example": "新城建设时，真是百堵皆作。"
        },
        412: {
            "pinyin": "bǎi duān dài jǔ",
            "meaning": "许多事情都等待兴办，形容任务繁多。",
            "example": "战后重建百端待举，需要长期努力。"
        },
        413: {
            "pinyin": "bǎi fā bǎi zhòng",
            "meaning": "射箭或打击百发百中，比喻做事十分得手。",
            "example": "他在靶场上百发百中。"
        },
        414: {
            "pinyin": "bǎi fèi dài jǔ",
            "meaning": "各种荒废的事业都等待兴办。",
            "example": "新政府上台时，百废待举。"
        },
        415: {
            "pinyin": "bǎi fèi jù xīng",
            "meaning": "各项荒废的事业重新兴办起来。",
            "example": "改革后，工业农业百废俱兴。"
        },
        416: {
            "pinyin": "bǎi gǎn jiāo jí",
            "meaning": "各种感慨交织在一起，形容感受复杂强烈。",
            "example": "重返故乡，他不禁百感交集。"
        },
        417: {
            "pinyin": "bǎi huā qí fàng",
            "meaning": "百花一起开放，比喻各种事物自由发展、竞相出现。",
            "example": "文艺创作要百花齐放、百家争鸣。"
        },
        418: {
            "pinyin": "bǎi huā shēng rì",
            "meaning": "传说中百花的生日，多指农历二月十二日。",
            "example": "民间在百花生日这天有踏青赏花的习俗。"
        },
        419: {
            "pinyin": "bǎi huì qiān pā",
            "meaning": "各种花卉争奇斗艳，比喻事物丰富多彩。",
            "example": "园中百卉千葩，景色迷人。"
        },
        420: {
            "pinyin": "bǎi jiā zhēng míng",
            "meaning": "诸子百家争相发表言论，比喻学术思想自由争鸣。",
            "example": "学术界应提倡百家争鸣。"
        },
        421: {
            "pinyin": "bǎi jǔ bǎi quán",
            "meaning": "每一次举动都完全成功。",
            "example": "如果事前准备充分，就有望百举百全。"
        },
        422: {
            "pinyin": "bǎi kǒng qiān chuāng",
            "meaning": "比喻创伤极多或弊病极严重。",
            "example": "战争让这座城市百孔千疮。"
        },
        423: {
            "pinyin": "bǎi kǒu mò biàn",
            "meaning": "许多人一起辩解也无法说清，形容受冤深重。",
            "example": "谣言四起，他一时百口莫辩。"
        },
        424: {
            "pinyin": "bǎi lǐ tiāo yī",
            "meaning": "从一百人中挑选一个，形容十分出众。",
            "example": "她的条件真是百里挑一。"
        },
        425: {
            "pinyin": "bǎi liàn chéng gāng",
            "meaning": "钢铁经过多次锻炼才成材，比喻人经多磨练而意志坚定。",
            "example": "革命者在斗争中百炼成钢。"
        },
        426: {
            "pinyin": "bǎi liǎo qiān dāng",
            "meaning": "做了很多却没有效果，或事情多而忙不过来。",
            "example": "他整日奔波，仍觉得百了千当。"
        },
        427: {
            "pinyin": "bǎi líng bǎi lì",
            "meaning": "形容人聪明伶俐、反应敏捷。",
            "example": "这个孩子说话做事都百伶百俐。"
        },
        428: {
            "pinyin": "bǎi líng méi shòu",
            "meaning": "长寿而健康，常用作祝寿用语。",
            "example": "祝老人家百龄眉寿，福如东海。"
        },
        429: {
            "pinyin": "bǎi nián bù yù",
            "meaning": "很多年难得遇到一次，形容极为罕见。",
            "example": "这样的洪水真是百年不遇。"
        },
        430: {
            "pinyin": "bǎi nián dà jì",
            "meaning": "关系长远的大计划。",
            "example": "教育是关系民族未来的百年大计。"
        },
        431: {
            "pinyin": "bǎi nián nán yù",
            "meaning": "同“百年不遇”，形容极其难得。",
            "example": "这次机遇可以说是百年难遇。"
        },
        432: {
            "pinyin": "bǎi nián shù rén",
            "meaning": "比喻培养人才是一项长远的工作。",
            "example": "教育工作百年树人，贵在坚持。"
        },
        433: {
            "pinyin": "bǎi nián xié lǎo",
            "meaning": "夫妻共同生活到老。",
            "example": "愿新人琴瑟和鸣，百年偕老。"
        },
        434: {
            "pinyin": "bǎi nián zhī bǐng",
            "meaning": "长时期掌握大权的柄，借指重权。",
            "example": "他一度握有百年之柄，权势显赫。"
        },
        435: {
            "pinyin": "bǎi nián zhī hǎo",
            "meaning": "多指夫妻婚姻长久美满。",
            "example": "两人结为连理，自此百年之好。"
        },
        436: {
            "pinyin": "bǎi nián zhī hòu",
            "meaning": "人死之后的委婉说法。",
            "example": "他早早安排好百年之后的后事。"
        },
        437: {
            "pinyin": "bǎi niàn jiē huī",
            "meaning": "一切念头都灰心丧气，形容极度失望。",
            "example": "连遭打击，他几乎百念皆灰。"
        },
        438: {
            "pinyin": "bǎi niǎo cháo fèng",
            "meaning": "百鸟朝拜凤凰，比喻众人归附贤明的首领。",
            "example": "这位德高望重的老人有如百鸟朝凤般受人敬仰。"
        },
        439: {
            "pinyin": "bǎi qiǎo qiān qióng",
            "meaning": "再多的巧计也掩盖不了穷困，形容小聪明无济于事。",
            "example": "空有机巧而缺乏实力，只能百巧千穷。"
        },
        440: {
            "pinyin": "bǎi shé zhī shēng",
            "meaning": "众多声音杂乱地同时发出，比喻议论纷纷。",
            "example": "会场上百舌之声，不易统一意见。"
        },
        441: {
            "pinyin": "bǎi shè zhòng jiǎn",
            "meaning": "路途遥远而负担沉重，比喻任重道远。",
            "example": "教育改革百舍重茧，需要耐心推进。"
        },
        442: {
            "pinyin": "bǎi shēn hé shú",
            "meaning": "拿一百个生命来赎罪也不够，形容罪行极重。",
            "example": "这样的恶行百身何赎。"
        },
        443: {
            "pinyin": "bǎi shēn mò shú",
            "meaning": "百条性命也不足以赎罪。",
            "example": "他认为对方的背叛简直百身莫赎。"
        },
        444: {
            "pinyin": "bǎi shì bù mó",
            "meaning": "经历百世也不会消磨，形容功绩或事物长存不朽。",
            "example": "这些文化遗产可谓百世不磨。"
        },
        445: {
            "pinyin": "bǎi shì shī",
            "meaning": "历代都可以作师表的人。",
            "example": "孔子被尊为百世师。"
        },
        446: {
            "pinyin": "bǎi shòu shuài wǔ",
            "meaning": "百兽跟随起舞，比喻天下万物响应号召。",
            "example": "圣王在上，百兽率舞。"
        },
        447: {
            "pinyin": "bǎi sī bù jiě",
            "meaning": "反复思考也想不明白。",
            "example": "这个问题让他百思不解。"
        },
        448: {
            "pinyin": "bǎi suì qiān qiū",
            "meaning": "形容岁月长久，多用作祝福长寿之辞。",
            "example": "祝老人家福寿绵长，百岁千秋。"
        },
        449: {
            "pinyin": "bǎi wàn mǎi zhái, qiān wàn mǎi lín",
            "meaning": "买房要看邻居，比喻好邻居非常重要。",
            "example": "俗话说百万买宅，千万买邻。"
        },
        450: {
            "pinyin": "bǎi wàn xióng shī",
            "meaning": "人数众多、声势浩大的军队。",
            "example": "百万雄师过大江，气势磅礴。"
        },
        451: {
            "pinyin": "bǎi wén bù rú yī jiàn",
            "meaning": "听到一百次不如亲眼见一次。",
            "example": "风景再怎么描写也不如亲临其境，真是百闻不如一见。"
        },
        452: {
            "pinyin": "bǎi wú jìn jì",
            "meaning": "什么都不忌讳。",
            "example": "过年期间大家说话行事百无禁忌。"
        },
        453: {
            "pinyin": "bǎi wú liáo lài",
            "meaning": "十分无聊，没有事情可做。",
            "example": "假期在家百无聊赖，只好看书打发时间。"
        },
        454: {
            "pinyin": "bǎi wú yī néng",
            "meaning": "什么本事都没有。",
            "example": "他自嘲百无一能，只会埋头苦干。"
        },
        455: {
            "pinyin": "bǎi wú yī shī",
            "meaning": "十分可靠，没有一点差错。",
            "example": "周密的计划让行动几乎百无一失。"
        },
        456: {
            "pinyin": "bǎi wú yī shì",
            "meaning": "没有一件是对的，形容错误很多。",
            "example": "这份草案几乎百无一是，需要重写。"
        },
        457: {
            "pinyin": "bǎi wú yī yòng",
            "meaning": "一点用处都没有。",
            "example": "空有学历却不会做事，难免被说百无一用。"
        },
        458: {
            "pinyin": "bǎi xīng bù rú yī yuè",
            "meaning": "许多星星不如一轮明月，比喻众多弱者抵不过一个强者。",
            "example": "在这个领域，百星不如一月的情形很常见。"
        },
        459: {
            "pinyin": "bǎi yè xiāo tiáo",
            "meaning": "各行各业都很萧条冷清。",
            "example": "经济危机时，城市一度百业萧条。"
        },
        460: {
            "pinyin": "bǎi yī bǎi shùn",
            "meaning": "对别人言行完全顺从。",
            "example": "她对孩子百依百顺，反而助长了娇气。"
        },
        461: {
            "pinyin": "bǎi yī bǎi suí",
            "meaning": "同“百依百顺”，事事依从别人。",
            "example": "对原则问题不能百衣百随。"
        },
        462: {
            "pinyin": "bǎi zhàn bǎi shèng",
            "meaning": "打很多次仗都能取胜，比喻屡战屡胜。",
            "example": "他带兵作战百战百胜。"
        },
        463: {
            "pinyin": "bǎi zhàn bù dài",
            "meaning": "多次作战都没有危险，形容常胜不败。",
            "example": "若能做到知己知彼，自可百战不殆。"
        },
        464: {
            "pinyin": "bǎi zhé bù huí",
            "meaning": "遭受再多挫折也不退缩。",
            "example": "他对理想百折不回，令人敬佩。"
        },
        465: {
            "pinyin": "bǎi zhé bù náo",
            "meaning": "屡遭挫折而意志不动摇。",
            "example": "创业必须有百折不挠的精神。"
        },
        466: {
            "pinyin": "bǎi zú zhī chóng, sǐ ér bù jiāng",
            "meaning": "比喻旧势力根基深，即使受挫也难以立即消亡。",
            "example": "陈旧观念如百足之虫，死而不僵。"
        },
        467: {
            "pinyin": "bǎi xiù què jīn",
            "meaning": "挥袖推开黄金，比喻不贪财物。",
            "example": "他对贿赂摆袖却金，十分清正。"
        },
        468: {
            "pinyin": "bài dé rǔ xíng",
            "meaning": "败坏道德，辱没品行。",
            "example": "这种行为实在是败德辱行。"
        },
        469: {
            "pinyin": "bài gǔ zhī pí",
            "meaning": "比喻失势后再也不能恢复原状的人或事。",
            "example": "他一朝失势，仿佛败鼓之皮。"
        },
        470: {
            "pinyin": "bài jūn zhī jiàng",
            "meaning": "打败仗的将领，多用来自谦。",
            "example": "在老将军面前，他自称败军之将，不敢班门弄斧。"
        },
        471: {
            "pinyin": "bài lín cán jiǎ",
            "meaning": "失败后残存的鳞甲，比喻失败者零星的残余力量。",
            "example": "叛军只剩一些败鳞残甲。"
        },
        472: {
            "pinyin": "bài liǔ cán huā",
            "meaning": "被摧残的柳树和花朵，比喻被糟蹋的女子或事物。",
            "example": "战乱过后，村庄一片败柳残花。"
        },
        473: {
            "pinyin": "bài dǎo yuán mén",
            "meaning": "到对方营帐前下拜求和或求教。",
            "example": "他不耻下问，亲自拜倒辕门讨教。"
        },
        474: {
            "pinyin": "bài ēn sī shì",
            "meaning": "在私室中拜谢恩德，多形容关系密切的私相授受。",
            "example": "收受贿赂还拜恩私室，实在可耻。"
        },
        475: {
            "pinyin": "bài jiàng fēng hóu",
            "meaning": "授予将帅爵位，形容战功显赫、受到重用。",
            "example": "他建功立业，终于被拜将封侯。"
        },
        476: {
            "pinyin": "bài guān yě shǐ",
            "meaning": "记录民间轶事的书籍。",
            "example": "这本书多属稗官野史，不可尽信。"
        },
        477: {
            "pinyin": "bān bó lù lí",
            "meaning": "色彩斑驳、光彩陆离，形容色彩繁杂美丽。",
            "example": "夕阳映照下，墙面斑驳陆离。"
        },
        478: {
            "pinyin": "bān jīng dào gù",
            "meaning": "铺席于路旁与老友叙旧，形容久别重逢的亲切。",
            "example": "多年未见的同窗在路边班荆道故。"
        },
        479: {
            "pinyin": "bān mén nòng fǔ",
            "meaning": "在鲁班门前舞弄斧头，比喻在行家面前卖弄本事。",
            "example": "在你面前谈木工，我这是班门弄斧了。"
        },
        480: {
            "pinyin": "bān shī huí cháo",
            "meaning": "出征的军队胜利后回到朝廷。",
            "example": "将军班师回朝，百姓夹道欢迎。"
        },
        481: {
            "pinyin": "bān chún dì shé",
            "meaning": "搬弄嘴皮，挑拨是非。",
            "example": "少在背后搬唇递舌，影响团结。"
        },
        482: {
            "pinyin": "bān jīn bō liǎng",
            "meaning": "斤两必分得很细，比喻计较得失非常斤斤。",
            "example": "与这样的人合作，他总是搬斤播两。"
        },
        483: {
            "pinyin": "bān nòng shì fēi",
            "meaning": "说长道短、挑拨是非。",
            "example": "喜欢搬弄是非的人终会被人疏远。"
        },
        484: {
            "pinyin": "bān shí zá jiǎo",
            "meaning": "搬石头砸自己的脚，比喻自作自受。",
            "example": "他拒绝合作，结果搬石砸脚，错失良机。"
        },
        485: {
            "pinyin": "bǎn shàng zǒu wán",
            "meaning": "像丸在斜坡上滚下，比喻事情发展很快、不可收拾。",
            "example": "事态一旦失控，就如阪上走丸。"
        },
        486: {
            "pinyin": "bǎn shàng dīng dīng",
            "meaning": "像钉在板上一样牢固，比喻事情已经定局。",
            "example": "合同签下，事情算是板上钉钉了。"
        },
        487: {
            "pinyin": "bǎn bǎn liù shí sì",
            "meaning": "形容刻板、拘泥于成规。",
            "example": "做事不要总是版版六十四，要学会变通。"
        },
        488: {
            "pinyin": "bàn bì jiāng shān",
            "meaning": "比喻国家或事业的一半领土或成果。",
            "example": "他凭一己之力打下半壁江山。"
        },
        489: {
            "pinyin": "bàn bù lún yǔ",
            "meaning": "指读半部《论语》就能治国，后多用来自谦学识不多。",
            "example": "他自称不过半部论语，却极有见地。"
        },
        490: {
            "pinyin": "bàn chóu bù nà",
            "meaning": "一点筹码也拿不出，比喻毫无办法。",
            "example": "面对这些专业问题，他半筹不纳。"
        },
        491: {
            "pinyin": "bàn jiān bù jiè",
            "meaning": "界限模糊、不清楚。",
            "example": "这两者之间半间不界，很难分得太清。"
        },
        492: {
            "pinyin": "bàn jié rù tǔ",
            "meaning": "形容年纪已老，离死不远。",
            "example": "他自叹半截入土，却仍每天工作。"
        },
        493: {
            "pinyin": "bàn jīn bā liǎng",
            "meaning": "彼此不相上下，实力差不多。",
            "example": "这两支队伍水平半斤八两。"
        },
        494: {
            "pinyin": "bàn lù chū jiā",
            "meaning": "中途改行从事某种职业或学业。",
            "example": "他原学工程，后来半路出家学了音乐。"
        },
        495: {
            "pinyin": "bàn miàn zhī jiāo",
            "meaning": "只见过一次面的人，交情不深。",
            "example": "我们不过半面之交，却让我深爱难忘。"
        },
        496: {
            "pinyin": "bàn miàn zhī jiù",
            "meaning": "曾经见过一次的旧相识。",
            "example": "多年之后重逢当年的半面之旧，别有感慨。"
        },
        497: {
            "pinyin": "bàn qīng bàn huáng",
            "meaning": "一半青一半黄，比喻事物尚未成熟或发展到中间状态。",
            "example": "田里的庄稼半青半黄，正值抽穗。"
        },
        498: {
            "pinyin": "bàn shēn bù suí",
            "meaning": "身体一半失去知觉，指严重瘫痪。",
            "example": "他因病落下半身不遂的后遗症。"
        },
        499: {
            "pinyin": "bàn sǐ bù huó",
            "meaning": "形容病重或死气沉沉的样子。",
            "example": "他整天半死不活，没有精神。"
        },
        500: {
            "pinyin": "bàn tú ér fèi",
            "meaning": "事情做到一半就放弃。",
            "example": "做事要有恒心，不能半途而废。"
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

    print(f"已为 401–500 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
