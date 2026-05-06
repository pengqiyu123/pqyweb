import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 为 1001–1100 条成语添加拼音、释义和例句
    enrich = {
        # TODO: 填充 1001–1100 号成语的详细信息
        1001: {
            "pinyin": "bù jīng zhī tán",
            "meaning": "荒诞不经、没有根据的话。",
            "example": "这些只是茶余饭后的不经之谈，不能当真。"
        },
        1002: {
            "pinyin": "bù jìng ér zǒu",
            "meaning": "消息不用宣传就迅速传播开来。",
            "example": "他的好事很快不胫而走，传遍了整个小镇。"
        },
        1003: {
            "pinyin": "bù jiù jì wǎng",
            "meaning": "不再追究过去的过错。",
            "example": "既然知错能改，就让我们不咎既往，重新开始。"
        },
        1004: {
            "pinyin": "bù jū xiǎo jié",
            "meaning": "不拘泥于生活或待人接物中的细小节目。",
            "example": "他待人真诚，不拘小节，很受大家欢迎。"
        },
        1005: {
            "pinyin": "bù jū yī gé",
            "meaning": "不局限于一种规格或方式，多指用人或创作不拘常规。",
            "example": "学校在选拔人才时不拘一格，给了许多特长生机会。"
        },
        1006: {
            "pinyin": "bù jué rú lǚ",
            "meaning": "像细线一样延续不绝，比喻局势危急或力量微弱难支。",
            "example": "守军补给不畅，形势已是不绝如缕。"
        },
        1007: {
            "pinyin": "bù jué yú ěr",
            "meaning": "声音不断传入耳中。",
            "example": "山间鸟鸣不绝于耳，格外悦人心弦。"
        },
        1008: {
            "pinyin": "bù jué jì yǎng",
            "meaning": "技艺在身，情不自禁地想要施展。",
            "example": "看到台上的表演，他也不觉技痒，想上去露一手。"
        },
        1009: {
            "pinyin": "bù kān zhī lùn",
            "meaning": "极为精当、不可磨灭的言论。",
            "example": "这篇文章观点深刻，可谓不刊之论。"
        },
        1010: {
            "pinyin": "bù kān huí shǒu",
            "meaning": "过去的情景惨痛，不忍回忆。",
            "example": "那段战乱岁月令人不堪回首。"
        },
        1011: {
            "pinyin": "bù kān qí yōu",
            "meaning": "忧虑沉重，难以承受。",
            "example": "国事艰难，让有志之士不堪其忧。"
        },
        1012: {
            "pinyin": "bù kān rù ěr",
            "meaning": "难以听下去，多指言语粗鄙下流。",
            "example": "他在众人面前说出那番话，实在不堪入耳。"
        },
        1013: {
            "pinyin": "bù kān rù mù",
            "meaning": "难以入目，多指景象污秽或情景惨烈。",
            "example": "灾后的现场满目疮痍，真是不堪入目。"
        },
        1014: {
            "pinyin": "bù kān shè xiǎng",
            "meaning": "后果严重到不能想象。",
            "example": "如果继续忽视安全隐患，后果将不堪设想。"
        },
        1015: {
            "pinyin": "bù kān yán zhuàng",
            "meaning": "悲惨或尴尬得难以用语言形容。",
            "example": "现场一片混乱，情形不堪言状。"
        },
        1016: {
            "pinyin": "bù kān yī jī",
            "meaning": "经不起一次打击，形容力量极其薄弱。",
            "example": "对方防线脆弱不堪，一攻即破，不堪一击。"
        },
        1017: {
            "pinyin": "bù kān zào jiù",
            "meaning": "缺乏资质、难以培养成才。",
            "example": "他懒散成性，实在不堪造就。"
        },
        1018: {
            "pinyin": "bù kàn sēng miàn kàn fó miàn",
            "meaning": "不看僧面也要看佛面，比喻看在与之有关的另一个人的情分上予以照顾。",
            "example": "看在你师父的面子上，我就不再追究了，不看僧面看佛面。"
        },
        1019: {
            "pinyin": "bù kàng bù bēi",
            "meaning": "既不高傲也不自卑，形容态度平和得体。",
            "example": "他待人不亢不卑，很有分寸。"
        },
        1020: {
            "pinyin": "bù kě dòng yáo",
            "meaning": "坚定稳固，不能被动摇。",
            "example": "我们对理想的追求不可动摇。"
        },
        1021: {
            "pinyin": "bù kě duān ní",
            "meaning": "无法推测头绪和端倪，形容情况深奥难测。",
            "example": "案件扑朔迷离，一时不可端倪。"
        },
        1022: {
            "pinyin": "bù kě duō dé",
            "meaning": "十分难得，不易得到。",
            "example": "这样难逢的机遇实在不可多得。"
        },
        1023: {
            "pinyin": "bù kě gào rén",
            "meaning": "不能告诉别人，多指见不得人的秘密。",
            "example": "他心里有些不可告人的打算。"
        },
        1024: {
            "pinyin": "bù kě jiào xùn",
            "meaning": "不能用教训使其改正，形容极难教导。",
            "example": "他桀骜不驯，几乎到了不可教训的地步。"
        },
        1025: {
            "pinyin": "bù kě jiū jié",
            "meaning": "事情已经过去或太复杂，无法一一追究。",
            "example": "当年的细节如今已不可究诘。"
        },
        1026: {
            "pinyin": "bù kě jiù yào",
            "meaning": "病重到无法医治，比喻事情坏到无法挽回。",
            "example": "若任其发展下去，恐怕就不可救药了。"
        },
        1027: {
            "pinyin": "bù kě kāi jiāo",
            "meaning": "事情纠缠得难以摆脱或结束。",
            "example": "两人吵得不可开交，引来围观。"
        },
        1028: {
            "pinyin": "bù kě kuí duó",
            "meaning": "不能揣度、难以预测。",
            "example": "风云变幻，局势不可揆度。"
        },
        1029: {
            "pinyin": "bù kě lǐ yù",
            "meaning": "不能用常理来开导或理解，形容顽固或荒谬。",
            "example": "他一意孤行，简直不可理喻。"
        },
        1030: {
            "pinyin": "bù kě míng zhuàng",
            "meaning": "难以用语言形容。",
            "example": "那种激动的心情真是不可名状。"
        },
        1031: {
            "pinyin": "bù kě mó miè",
            "meaning": "不能磨灭，多指功绩或印象永远存在。",
            "example": "先烈的功勋不可磨灭。"
        },
        1032: {
            "pinyin": "bù kě piān fèi",
            "meaning": "不可以偏废一方，强调两方面都要兼顾。",
            "example": "教学中知识与能力不可偏废。"
        },
        1033: {
            "pinyin": "bù kě qǐ jí",
            "meaning": "不能企及，形容差距极大。",
            "example": "在艺术造诣上，他的成就令人不可企及。"
        },
        1034: {
            "pinyin": "bù kě shèng shǔ",
            "meaning": "多得数不过来。",
            "example": "夜空中的繁星不可胜数。"
        },
        1035: {
            "pinyin": "bù kě shèng yán",
            "meaning": "多得说不完，形容情况或事例非常多。",
            "example": "这类事例不可胜言，此处仅举一二。"
        },
        1036: {
            "pinyin": "bù kě shōu shí",
            "meaning": "局面乱到难以收拾。",
            "example": "若不及时制止，事态将不可收拾。"
        },
        1037: {
            "pinyin": "bù kě sī yì",
            "meaning": "常理难以想象和理解，形容非常奇特或深奥。",
            "example": "宇宙之大，真是不可思议。"
        },
        1038: {
            "pinyin": "bù kě tóng rì ér yǔ",
            "meaning": "不能放在同一天来说，比喻差距很大。",
            "example": "现在的生活水平和从前不可同日而语。"
        },
        1039: {
            "pinyin": "bù kě xiàn liàng",
            "meaning": "前途或成就无法限量，形容发展空间极大。",
            "example": "这位年轻人前途不可限量。"
        },
        1040: {
            "pinyin": "bù kě xiàng ěr",
            "meaning": "不能靠近，形容气味难闻或气势骇人。",
            "example": "那坛臭豆腐味道浓烈，真是不可向迩。"
        },
        1041: {
            "pinyin": "bù kě yán xuān",
            "meaning": "不能用言语表达出来。",
            "example": "那一刻他内心的感动实在不可言宣。"
        },
        1042: {
            "pinyin": "bù kě yán yù",
            "meaning": "难以用语言形容。",
            "example": "大自然的鬼斧神工，真是不可言喻。"
        },
        1043: {
            "pinyin": "bù kě yán zhuàng",
            "meaning": "同“不可名状”，难以用言语描述。",
            "example": "离别时那种滋味，实在不可言状。"
        },
        1044: {
            "pinyin": "bù kě yī shì",
            "meaning": "自以为了不起，不可一世。",
            "example": "他仗着有点成绩就不可一世，迟早要吃亏。"
        },
        1045: {
            "pinyin": "bù kě yí yì",
            "meaning": "不可改变或转移，多指立场坚定。",
            "example": "他为人正直，操守不可移易。"
        },
        1046: {
            "pinyin": "bù kě yú yuè",
            "meaning": "不能逾越，多指纪律或界限严明。",
            "example": "法律底线不可逾越。"
        },
        1047: {
            "pinyin": "bù kě zào cì",
            "meaning": "做事不能轻率急躁。",
            "example": "面对复杂局面，决策尤不可造次。"
        },
        1048: {
            "pinyin": "bù kě zhōng rì",
            "meaning": "一天都难以打发下去，形容内心极度不安或恐惧。",
            "example": "身陷疑案之中，他几乎不可终日。"
        },
        1049: {
            "pinyin": "bù kě zhuō mō",
            "meaning": "难以猜测或捉摸。",
            "example": "他的脾气阴晴不定，实在不可捉摸。"
        },
        1050: {
            "pinyin": "bù kuì bù zuò",
            "meaning": "行为对得起自己的良心，不感到惭愧。",
            "example": "一切问心无愧，便可不愧不作。"
        },
        1051: {
            "pinyin": "bù kuì wū lòu",
            "meaning": "在无人看见的地方也问心无愧。",
            "example": "真正的君子即使独处也不欺暗室、不愧屋漏。"
        },
        1052: {
            "pinyin": "bù láng bù xiù",
            "meaning": "既不英俊也不出众，比喻平平常常、无甚出色。",
            "example": "他相貌不扬，不郎不秀，但为人可靠。"
        },
        1053: {
            "pinyin": "bù láng bù yǒu",
            "meaning": "既不是好庄稼，也不是好草，形容人品平庸或不成才。",
            "example": "这种不稂不莠的态度，很难有所成就。"
        },
        1054: {
            "pinyin": "bù láo ér huò",
            "meaning": "自己不劳动却取得收获，比喻不劳而获。",
            "example": "总想不劳而获，终究站不稳脚跟。"
        },
        1055: {
            "pinyin": "bù lì wén zì",
            "meaning": "不立文字记载，多指以心传心或口授，不写成文字。",
            "example": "禅宗讲究不立文字，以心印心。"
        },
        1056: {
            "pinyin": "bù liǎo liǎo zhī",
            "meaning": "事情不了了结，没有下文。",
            "example": "这件事后来竟不了了之。"
        },
        1057: {
            "pinyin": "bù liè fāng tóu",
            "meaning": "形容人长相或举止粗鲁，不文雅。",
            "example": "他相貌粗犷，有些不劣方头的味道。"
        },
        1058: {
            "pinyin": "bù lìn cì jiào",
            "meaning": "表示虚心，希望对方不吝赐教。",
            "example": "对其中不当之处，还望诸位不吝赐教。"
        },
        1059: {
            "pinyin": "bù lìn zhǐ jiào",
            "meaning": "同“不吝赐教”，恳请对方多多指点。",
            "example": "我初来乍到，请大家不吝指教。"
        },
        1060: {
            "pinyin": "bù lìn zhū yù",
            "meaning": "不吝惜珍贵的话语，比喻恳请对方多提宝贵意见。",
            "example": "还望各位不吝珠玉，提出宝贵意见。"
        },
        1061: {
            "pinyin": "bù liú yú dì",
            "meaning": "做事不留下回旋余地，形容处理问题非常绝决。",
            "example": "谈判桌上他句句紧逼，几乎不留余地。"
        },
        1062: {
            "pinyin": "bù lù fēng máng",
            "meaning": "不显露自己的才华或锐气。",
            "example": "他做事一向低调，不露锋芒。"
        },
        1063: {
            "pinyin": "bù lù guī jiǎo",
            "meaning": "不显露才华或本领。",
            "example": "他虽有真才实学，却从不露圭角。"
        },
        1064: {
            "pinyin": "bù lù shēng sè",
            "meaning": "不露出声色变化，形容镇定沉着。",
            "example": "听到坏消息时，他仍不露声色，继续指挥工作。"
        },
        1065: {
            "pinyin": "bù lún bù lèi",
            "meaning": "既不合于这一类，也不合于那一类，形容事物古怪或不合常规。",
            "example": "这套装扮不伦不类，看着很别扭。"
        },
        1066: {
            "pinyin": "bù luò kē jiù",
            "meaning": "不落入旧有的窠臼，比喻有独创性，不因循守旧。",
            "example": "这篇文章立意新颖，不落窠臼。"
        },
        1067: {
            "pinyin": "bù màn bù zhī",
            "meaning": "形容说话或写文章不枝蔓拖沓，结构简洁有力。",
            "example": "他的发言简明扼要，不蔓不枝。"
        },
        1068: {
            "pinyin": "bù máo zhī dì",
            "meaning": "连草木都难以生长的地方，比喻极其贫瘠荒凉之地。",
            "example": "这里曾是一片不毛之地，如今却变成良田。"
        },
        1069: {
            "pinyin": "bù míng bù bái",
            "meaning": "事情的来龙去脉不清楚。",
            "example": "他莫名其妙被批评，心里很是不明不白。"
        },
        1070: {
            "pinyin": "bù míng yī qián",
            "meaning": "穷得身上一文钱都没有。",
            "example": "他创业之初不名一钱，全凭双手打拼。"
        },
        1071: {
            "pinyin": "bù móu ér hé",
            "meaning": "事先没有商量却说法或行动一致。",
            "example": "大家的看法不谋而合，都赞成这个方案。"
        },
        1072: {
            "pinyin": "bù mù zhī dì",
            "meaning": "没有人饲养的地方，引申为荒无人烟之地。",
            "example": "古代边塞多为不牧之地，环境十分恶劣。"
        },
        1073: {
            "pinyin": "bù néng zàn yī cí",
            "meaning": "好得令人无可挑剔，连一句赞美的话都嫌不足以形容。",
            "example": "他的演出精湛绝伦，真是不能赞一辞。"
        },
        1074: {
            "pinyin": "bù néng zì bá",
            "meaning": "自己不能把自己拉出来，比喻陷入困境而难以自拔。",
            "example": "他沉迷赌博，已经不能自拔。"
        },
        1075: {
            "pinyin": "bù néng zì yǐ",
            "meaning": "感情激动得不能控制自己。",
            "example": "听到噩耗，他悲痛万分，不能自已。"
        },
        1076: {
            "pinyin": "bù niàn jiù è",
            "meaning": "不记念旧日的仇怨过错。",
            "example": "他宽宏大量，对过去的矛盾一概不念旧恶。"
        },
        1077: {
            "pinyin": "bù níng wéi shì",
            "meaning": "不仅如此，而且如此，用于加强语气。",
            "example": "他不仅通晓诗文，不宁唯是，还精于书画。"
        },
        1078: {
            "pinyin": "bù pà guān, zhǐ pà guǎn",
            "meaning": "不怕当官的，只怕直接管自己的人，形容基层管理的重要。",
            "example": "俗话说不怕官，只怕管，说明日常管理更关键。"
        },
        1079: {
            "pinyin": "bù piān bù dǎng",
            "meaning": "不偏袒任何一方，也不结党营私。",
            "example": "他处事公正，不偏不党，深得大家信服。"
        },
        1080: {
            "pinyin": "bù piān bù yǐ",
            "meaning": "态度中立，不偏向任何一方。",
            "example": "做裁判必须不偏不倚，秉公断事。"
        },
        1081: {
            "pinyin": "bù píng zé míng",
            "meaning": "心中有不平就要发出声音，指对不合理的事自然而然会表示不满。",
            "example": "面对不公正的待遇，人们总会不平则鸣。"
        },
        1082: {
            "pinyin": "bù pò bù lì",
            "meaning": "旧的不打破，新的就不能建立。",
            "example": "改革往往要不破不立，冲破旧体制的束缚。"
        },
        1083: {
            "pinyin": "bù qī àn shì",
            "meaning": "在无人看见的暗室中也不欺骗，形容品行端正。",
            "example": "真正的君子不欺暗室，光明磊落。"
        },
        1084: {
            "pinyin": "bù qī ér rán",
            "meaning": "事先没有约定却自然而然地如此。",
            "example": "听到这个消息，人群中不期而然地响起掌声。"
        },
        1085: {
            "pinyin": "bù qī ér yù",
            "meaning": "事先没有约定却碰巧遇见。",
            "example": "在异国他乡和老同学不期而遇，格外惊喜。"
        },
        1086: {
            "pinyin": "bù qī xiū gǔ",
            "meaning": "不必拘泥于古代成法。",
            "example": "治国理政不能不期修古，一味复古。"
        },
        1087: {
            "pinyin": "bù qī rán ér rán",
            "meaning": "没有料想到却自然而然地这样。",
            "example": "他起初并不打算参赛，不期然而然成了主力。"
        },
        1088: {
            "pinyin": "bù qì cǎo mèi",
            "meaning": "不嫌弃地位卑微、出身寒微的人。",
            "example": "伯乐不弃草昧，愿意提携年轻后辈。"
        },
        1089: {
            "pinyin": "bù qín èr máo",
            "meaning": "打仗不俘虏鬓发花白的老人，比喻用兵仁慈。",
            "example": "他主张不擒二毛，以示宽大为怀。"
        },
        1090: {
            "pinyin": "bù qíng zhī qǐng",
            "meaning": "有点勉强或难以启齿的请求，多作自谦之辞。",
            "example": "我有一事相托，实属不情之请，还望见谅。"
        },
        1091: {
            "pinyin": "bù qiú shèn jiě",
            "meaning": "不要求十分透彻地理解，多指读书领会大意即可。",
            "example": "读这类文章可不求甚解，抓住主旨就好。"
        },
        1092: {
            "pinyin": "bù qiú wén dá",
            "meaning": "不求在社会上有名声地位。",
            "example": "他安于淡泊，不求闻达于诸侯。"
        },
        1093: {
            "pinyin": "bù qiú yǒu gōng, dàn qiú wú guò",
            "meaning": "不追求大功劳，只希望没有过失。",
            "example": "他做事向来谨慎，不求有功，但求无过。"
        },
        1094: {
            "pinyin": "bù qū bù náo",
            "meaning": "在压力和打击面前不屈服、不退缩。",
            "example": "面对困难，他始终不屈不挠。"
        },
        1095: {
            "pinyin": "bù rěn zú dú",
            "meaning": "文章内容过于悲惨或凄凉，令人读不下去。",
            "example": "那段战乱记述实在不忍卒读。"
        },
        1096: {
            "pinyin": "bù rì bù yuè",
            "meaning": "不以日月计算，比喻时间不会太久。",
            "example": "工程进展顺利，不日不月即可完工。"
        },
        1097: {
            "pinyin": "bù róng zhì biàn",
            "meaning": "事实明显，不容许再辩解。",
            "example": "证据确凿，此事已不容置辩。"
        },
        1098: {
            "pinyin": "bù róng zhì huì",
            "meaning": "不容插嘴或发表意见。",
            "example": "他话说得太满，让人不容置喙。"
        },
        1099: {
            "pinyin": "bù róng zhì yí",
            "meaning": "不容许有任何怀疑。",
            "example": "他的清白是不容置疑的。"
        },
        1100: {
            "pinyin": "bù rú guī qù",
            "meaning": "还不如回家去，表示对处境失望或不满。",
            "example": "若工作处处受阻，他不禁感叹不如归去。"
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

    print(f"已为 1001–1100 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
