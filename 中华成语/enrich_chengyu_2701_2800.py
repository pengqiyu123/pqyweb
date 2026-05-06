import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    enrich = {
        2701: {
            "pinyin": "dī méi shùn yǎn",
            "meaning": "形容神情恭顺、驯服讨好。",
            "example": "面对严厉的上司，他总是一副低眉顺眼的样子。"
        },
        2702: {
            "pinyin": "dī méi zhé yāo",
            "meaning": "形容屈身逢迎、阿谀奉承的姿态。",
            "example": "他宁死也不肯为权贵低眉折腰。"
        },
        2703: {
            "pinyin": "dī sān xià sì",
            "meaning": "形容态度卑下、曲意逢迎。",
            "example": "为了那点好处，他在别人面前低三下四。"
        },
        2704: {
            "pinyin": "dī shēng xià qì",
            "meaning": "形容说话语气极为谦卑、恭顺。",
            "example": "他低声下气地向老师认错。"
        },
        2705: {
            "pinyin": "dī shǒu xià xīn",
            "meaning": "形容十分谦卑恭顺的样子。",
            "example": "在长辈面前，他总是低首下心，不敢造次。"
        },
        2706: {
            "pinyin": "dī yín qiǎn chàng",
            "meaning": "形容轻声吟咏或小声歌唱。",
            "example": "她独自坐在窗前，低吟浅唱一首老歌。"
        },
        2707: {
            "pinyin": "dí kài tóng chóu",
            "meaning": "大家对敌人都怀着同样的愤怒，团结一致对敌。",
            "example": "面对外来侵略，全国人民敌忾同仇。"
        },
        2708: {
            "pinyin": "dí gù gēng xīn",
            "meaning": "清除旧的事物，换上新的事物。",
            "example": "这次制度改革，正是一次涤故更新的机会。"
        },
        2709: {
            "pinyin": "dí xiá dàng huì",
            "meaning": "清除缺点和污秽，比喻肃清弊端。",
            "example": "反腐行动旨在涤瑕荡秽，重塑政府形象。"
        },
        2710: {
            "pinyin": "dǐ bèi è hóu",
            "meaning": "顶着背、掐住喉咙，比喻逼迫得很紧或斗争激烈。",
            "example": "两军相持，几乎到了抵背扼喉的地步。"
        },
        2711: {
            "pinyin": "dǐ sǐ màn shēng",
            "meaning": "形容竭尽思虑、千方百计地谋求脱身或达到目的。",
            "example": "为了完成任务，他抵死谩生地想办法。"
        },
        2712: {
            "pinyin": "dǐ xiá dǎo xì",
            "meaning": "专抓别人的缺点和漏洞加以攻击。",
            "example": "与其抵瑕蹈隙，不如多看他人的长处。"
        },
        2713: {
            "pinyin": "dǐ zhǎng ér tán",
            "meaning": "拍掌交谈，形容谈得高兴、畅快。",
            "example": "几位老友重逢，抵掌而谈到深夜。"
        },
        2714: {
            "pinyin": "dǐ zú ér mián",
            "meaning": "脚对着脚睡觉，形容关系亲密或住宿条件简陋。",
            "example": "学生时代我们常挤在一张床上，抵足而眠。"
        },
        2715: {
            "pinyin": "dǐ bīng lì wǔ",
            "meaning": "砥砺兵器、整训队伍，指整顿军队、厉兵秣马。",
            "example": "将军命令全军砥兵砺伍，准备出征。"
        },
        2716: {
            "pinyin": "dǐ jié fèng gōng",
            "meaning": "砥砺品节，奉公守法，形容忠诚廉洁。",
            "example": "他一生砥节奉公，从不以权谋私。"
        },
        2717: {
            "pinyin": "dǐ lì fēng jié",
            "meaning": "磨砺气节和操守。",
            "example": "艰苦的环境反而砥砺风节，使他更加坚强。"
        },
        2718: {
            "pinyin": "dǐ lì zhuó mó",
            "meaning": "磨砺琢磨，比喻不断锻炼、修养自己或研究学问。",
            "example": "只有在实践中砥砺琢磨，才能真正成长。"
        },
        2719: {
            "pinyin": "dǐ xíng lì míng",
            "meaning": "砥砺德行，以此立下名声。",
            "example": "读书人当以砥行立名，不可沽名钓誉。"
        },
        2720: {
            "pinyin": "dǐ xíng mó míng",
            "meaning": "通过修养品行而取得名声。",
            "example": "先贤多以砥行磨名，为后人所景仰。"
        },
        2721: {
            "pinyin": "dǐ zhù zhōng liú",
            "meaning": "黄河中流的砥柱石，比喻在动荡局势中起支柱作用的力量或人物。",
            "example": "在国家危难时刻，总要有人做砥柱中流。"
        },
        2722: {
            "pinyin": "dì bēng shān cuī",
            "meaning": "地裂山崩，形容声势巨大或灾变剧烈。",
            "example": "爆炸声如地崩山摧，震撼人心。"
        },
        2723: {
            "pinyin": "dì chè tiān bēng",
            "meaning": "大地裂开、天空塌下，比喻灾难巨大。",
            "example": "战火连绵，百姓犹如身处地坼天崩之中。"
        },
        2724: {
            "pinyin": "dì chǒu dé qí",
            "meaning": "地位门第相当，德行也相配，多用于婚姻双方相称。",
            "example": "两家可谓地丑德齐，婚事很快就定下来了。"
        },
        2725: {
            "pinyin": "dì dà wù bó",
            "meaning": "土地广大，物产丰富。",
            "example": "我国地大物博，资源极为丰富。"
        },
        2726: {
            "pinyin": "dì dòng shān yáo",
            "meaning": "地震山摇，比喻声势浩大或震撼。",
            "example": "礼炮齐鸣，真有地动山摇之势。"
        },
        2727: {
            "pinyin": "dì guǎng rén xī",
            "meaning": "地方广大而人口稀少。",
            "example": "这里地广人稀，适合发展牧业。"
        },
        2728: {
            "pinyin": "dì jiǎo tiān yá",
            "meaning": "地的尽头、天的边际，形容相距极远之处。",
            "example": "他远在地角天涯，却仍惦记着故乡。"
        },
        2729: {
            "pinyin": "dì jiǔ tiān cháng",
            "meaning": "像天地一样长久，常用来形容感情深厚。",
            "example": "他希望这份友谊地久天长。"
        },
        2730: {
            "pinyin": "dì kuàng rén xī",
            "meaning": "地方辽阔而人烟稀少。",
            "example": "北方草原地旷人稀，风景壮阔。"
        },
        2731: {
            "pinyin": "dì lǎo tiān huāng",
            "meaning": "形容时间极久或爱情誓言永恒。",
            "example": "他对她发誓要相守到地老天荒。"
        },
        2732: {
            "pinyin": "dì lì rén hé",
            "meaning": "占据有利地势，又得到人心。",
            "example": "凭借地利人和，这家企业发展迅速。"
        },
        2733: {
            "pinyin": "dì píng tiān chéng",
            "meaning": "大地平坦，天空自然形成，比喻天下太平、局势安定。",
            "example": "经过多年治理，这里终于地平天成、百姓安居。"
        },
        2734: {
            "pinyin": "dì shàng tiān guān",
            "meaning": "指地上的高官显贵，如同天上的神官，比喻权势显赫的人。",
            "example": "他家世显赫，几乎成了地上天官。"
        },
        2735: {
            "pinyin": "dì xià xiū wén",
            "meaning": "原指阴间治文书，比喻死后仍有文名，或讥讽只顾空谈文章。",
            "example": "他若再不务实，只怕要去地下修文了。"
        },
        2736: {
            "pinyin": "dì yù biàn xiàng",
            "meaning": "地狱的各种景象，比喻现实环境极其黑暗、残酷。",
            "example": "战乱中的城市几乎成了地狱变相。"
        },
        2737: {
            "pinyin": "dì zhǔ zhī yì",
            "meaning": "主人应尽的招待客人的情谊。",
            "example": "既然来了，就让我尽一尽地主之谊吧。"
        },
        2738: {
            "pinyin": "dì wáng jiāng xiàng",
            "meaning": "皇帝、诸侯、将军和宰相，一般指统治阶层。",
            "example": "历史书多记载帝王将相的事迹。"
        },
        2739: {
            "pinyin": "diān dǎo hēi bái",
            "meaning": "把黑说成白，把白说成黑，歪曲事实。",
            "example": "他在会上颠倒黑白，令人愤怒。"
        },
        2740: {
            "pinyin": "diān dǎo qián kūn",
            "meaning": "形容把局势完全扭转过来。",
            "example": "这一战足以颠倒乾坤，改变历史进程。"
        },
        2741: {
            "pinyin": "diān dǎo shì fēi",
            "meaning": "把对的说成错的，把错的说成对的。",
            "example": "我们不能容忍有人颠倒是非。"
        },
        2742: {
            "pinyin": "diān dǎo yī shang",
            "meaning": "衣服穿反了，比喻慌乱失措或颠倒错乱。",
            "example": "他急得连衣服都颠倒衣裳地穿上就冲出门去。"
        },
        2743: {
            "pinyin": "diān dǎo yīn yáng",
            "meaning": "把阴阳颠倒，比喻把根本原则弄乱或秩序大乱。",
            "example": "若任其胡作非为，势必颠倒阴阳。"
        },
        2744: {
            "pinyin": "diān lái dǎo qù",
            "meaning": "一再翻来覆去，比喻反复考虑或多次重复。",
            "example": "这件事他在心里颠来倒去地想着。"
        },
        2745: {
            "pinyin": "diān luán dǎo fèng",
            "meaning": "原形容欢爱缠绵，多用来指男女间亲昵之态。",
            "example": "小说中对男女主角颠鸾倒凤的描写略显夸张。"
        },
        2746: {
            "pinyin": "diān máo zhǒng zhǒng",
            "meaning": "颠毛指头发，种种指短少，形容年老头发稀少，比喻衰老。",
            "example": "他自叹颠毛种种，已不复当年英姿。"
        },
        2747: {
            "pinyin": "diān pèi liú lí",
            "meaning": "形容生活困顿，四处流亡。",
            "example": "战争让无数家庭颠沛流离。"
        },
        2748: {
            "pinyin": "diān pū bù pò",
            "meaning": "比喻理论或道理非常坚固，怎么打击也不能破坏。",
            "example": "这个真理已经被历史证明是颠扑不破的。"
        },
        2749: {
            "pinyin": "diān qián dǎo kūn",
            "meaning": "与“颠倒乾坤”同义，形容把局势完全扭转。",
            "example": "他妄想以一己之力颠乾倒坤。"
        },
        2750: {
            "pinyin": "diān sān dǎo sì",
            "meaning": "说话或做事错乱，没有条理。",
            "example": "他紧张得说话颠三倒四。"
        },
        2751: {
            "pinyin": "diān jīn bō liǎng",
            "meaning": "比喻过分计较利害得失。",
            "example": "合作要坦诚相待，别总掂斤播两。"
        },
        2752: {
            "pinyin": "diǎn qī yù zǐ",
            "meaning": "抵押妻子、卖掉儿女，形容极端贫困。",
            "example": "古时饥荒之年，百姓被迫典妻鬻子，以求糊口。"
        },
        2753: {
            "pinyin": "diǎn zhāng wén wù",
            "meaning": "典籍制度和有历史价值的器物总称。",
            "example": "这座博物馆珍藏着大量典章文物。"
        },
        2754: {
            "pinyin": "diǎn jīn chéng tiě",
            "meaning": "把金变成铁，比喻把好事办坏，反起负面作用。",
            "example": "他一向办事粗心，经他手常是点金成铁。"
        },
        2755: {
            "pinyin": "diǎn tiě chéng jīn",
            "meaning": "把铁变成金，比喻极高的本领，能化腐朽为神奇。",
            "example": "在大师笔下，平凡的素材也能点铁成金。"
        },
        2756: {
            "pinyin": "diǎn jīn fá shù",
            "meaning": "指再高明的手段也难以奏效，或比喻资金、资源枯竭。",
            "example": "公司资金链紧张，即便高手来也点金乏术。"
        },
        2757: {
            "pinyin": "diǎn jīng zhī bǐ",
            "meaning": "关键的一笔，使内容更加生动传神。",
            "example": "这句话是全文的点睛之笔。"
        },
        2758: {
            "pinyin": "diǎn shí chéng jīn",
            "meaning": "把石头变成金子，比喻非常高超的改造能力。",
            "example": "在他的指导下，这个团队仿佛点石成金。"
        },
        2759: {
            "pinyin": "diǎn tóu hā yāo",
            "meaning": "形容卑躬屈膝、逢迎讨好。",
            "example": "他在领导面前点头哈腰，令人看了很不舒服。"
        },
        2760: {
            "pinyin": "diàn guāng shí huǒ",
            "meaning": "比喻极其迅速、短暂。",
            "example": "事情发生得电光石火，几乎来不及反应。"
        },
        2761: {
            "pinyin": "diàn guāng zhāo lù",
            "meaning": "像闪电和晨露一样短暂，比喻事物转瞬即逝。",
            "example": "名利不过是电光朝露，转眼成空。"
        },
        2762: {
            "pinyin": "diàn shǎn léi míng",
            "meaning": "雷雨时电光闪耀、雷声隆隆。",
            "example": "夜空中电闪雷鸣，暴雨随之而来。"
        },
        2763: {
            "pinyin": "diàn wēi zhī yù",
            "meaning": "临近危险的境地。",
            "example": "若不及时调整，公司就要陷入阽危之域。"
        },
        2764: {
            "pinyin": "diàn wén rú shuǐ",
            "meaning": "形容竹席纹理细密如水波。",
            "example": "夏夜躺在簟纹如水的竹席上，十分凉爽。"
        },
        2765: {
            "pinyin": "diāo chán mǎn zuò",
            "meaning": "比喻美女很多，满席皆佳人。",
            "example": "宴会上貂蝉满座，宾客大饱眼福。"
        },
        2766: {
            "pinyin": "diāo qiú huàn jiǔ",
            "meaning": "把珍贵的貂皮袍子换酒喝，形容豪放不羁或不惜重财。",
            "example": "他性情豪爽，常有貂裘换酒之举。"
        },
        2767: {
            "pinyin": "diāo chóng xiǎo jì",
            "meaning": "比喻微不足道的小技巧，多为自谦之词。",
            "example": "我不过略懂皮毛，只是雕虫小技。"
        },
        2768: {
            "pinyin": "diāo gān zhuó shèn",
            "meaning": "比喻刻画入微、用心良苦，多形容文学创作。",
            "example": "这部巨著是作者雕肝琢肾多年之作。"
        },
        2769: {
            "pinyin": "diāo hān lòu gé",
            "meaning": "雕刻蚶蛤，比喻文辞雕琢过甚。",
            "example": "文章切忌雕蚶镂蛤，反而失去真味。"
        },
        2770: {
            "pinyin": "diāo lán yù qì",
            "meaning": "雕刻的栏杆、玉石的台阶，形容建筑华丽。",
            "example": "皇宫内处处雕阑玉砌，金碧辉煌。"
        },
        2771: {
            "pinyin": "diāo liáng huà dòng",
            "meaning": "房梁雕刻、栋梁上绘画，形容建筑装饰华丽。",
            "example": "这座古寺雕梁画栋，气势非凡。"
        },
        2772: {
            "pinyin": "diāo xīn yàn zhǎo",
            "meaning": "形容心肠狠毒、手段残酷。",
            "example": "他为达目的不择手段，简直是雕心雁爪。"
        },
        2773: {
            "pinyin": "diāo yù shuāng lián",
            "meaning": "精雕细琢的双句对联，比喻工整华美的对联作品。",
            "example": "门口悬着一副雕玉双联，引人驻足。"
        },
        2774: {
            "pinyin": "diāo zhāng lòu jù",
            "meaning": "过分雕琢文章辞句。",
            "example": "写作要自然真切，不必处处雕章镂句。"
        },
        2775: {
            "pinyin": "diāo dǒu sēn yán",
            "meaning": "形容军营戒备森严。",
            "example": "边关夜里刁斗森严，一片肃杀之气。"
        },
        2776: {
            "pinyin": "diāo huá jiān zhà",
            "meaning": "形容为人狡猾奸诈。",
            "example": "他为人刁滑奸诈，绝不可轻信。"
        },
        2777: {
            "pinyin": "diāo tiān jué dì",
            "meaning": "形容非常凶狠，敢做坏事；也形容极度顽劣。",
            "example": "这帮匪徒刁天决地，无恶不作。"
        },
        2778: {
            "pinyin": "diāo zuān gǔ guài",
            "meaning": "形容性格、言行怪异难以对付。",
            "example": "这位顾客脾气刁钻古怪，很难伺候。"
        },
        2779: {
            "pinyin": "diāo zuān kè bó",
            "meaning": "形容待人苛刻尖酸。",
            "example": "他对下属总是刁钻刻薄，大家都怕他。"
        },
        2780: {
            "pinyin": "diào míng gū yù",
            "meaning": "谋求名声、出卖名誉，比喻追逐虚名。",
            "example": "真正做学问的人，不屑于钓名沽誉。"
        },
        2781: {
            "pinyin": "diào míng qī shì",
            "meaning": "为了名声而欺骗世人。",
            "example": "这种钓名欺世的伎俩终究会被识破。"
        },
        2782: {
            "pinyin": "diào yóu zhī dì",
            "meaning": "适合游玩垂钓的地方。",
            "example": "这片湖光山色，可谓钓游之地。"
        },
        2783: {
            "pinyin": "diào bīng qiǎn jiàng",
            "meaning": "调动兵力、派遣将领，泛指调配人力、部署安排。",
            "example": "他在公司里调兵遣将，安排各部门协同作战。"
        },
        2784: {
            "pinyin": "diào hǔ lí shān",
            "meaning": "引诱对方离开有利地形，以便各个击破。",
            "example": "他们设计了一计调虎离山，引敌人出城。"
        },
        2785: {
            "pinyin": "diào bì bù gù",
            "meaning": "甩开手臂，不再回头，形容态度坚决、毫不顾惜。",
            "example": "既然下定决心，就掉臂不顾地走下去。"
        },
        2786: {
            "pinyin": "diào sān cùn shé",
            "meaning": "运用口才游说别人。",
            "example": "他最会掉三寸舌，说得大家连连点头。"
        },
        2787: {
            "pinyin": "diào shé gǔ chún",
            "meaning": "舌唇并用，喋喋不休地说。",
            "example": "他在台上掉舌鼓唇，说个没完。"
        },
        2788: {
            "pinyin": "diào shū dài",
            "meaning": "卖弄学问，引经据典过多。",
            "example": "聊天时别总掉书袋，会让人觉得做作。"
        },
        2789: {
            "pinyin": "diào tóu shǔ cuàn",
            "meaning": "形容慌忙逃跑的样子。",
            "example": "一见警察，他们立刻掉头鼠窜。"
        },
        2790: {
            "pinyin": "diào yǐ qīng xīn",
            "meaning": "形容把事情看得太轻，不够重视。",
            "example": "对安全问题绝不能掉以轻心。"
        },
        2791: {
            "pinyin": "diào ěr láng dāng",
            "meaning": "形容举止散漫、不负责任。",
            "example": "他做事总是吊尔郎当，让人不放心。"
        },
        2792: {
            "pinyin": "diào gǔ shāng jīn",
            "meaning": "怀念古人、感伤今事。",
            "example": "读史可以吊古伤今，反思现实。"
        },
        2793: {
            "pinyin": "diào gǔ xún yōu",
            "meaning": "访问古迹、寻求幽胜之处。",
            "example": "他们结伴出游，专门去山中吊古寻幽。"
        },
        2794: {
            "pinyin": "diào mín fá zuì",
            "meaning": "慰问百姓，讨伐有罪之人。",
            "example": "这支义军打着吊民伐罪的旗号起兵。"
        },
        2795: {
            "pinyin": "diào sǐ wèn jí",
            "meaning": "吊念死者，问候病人，形容对百姓十分关怀。",
            "example": "清官常亲自下乡，吊死问疾，体察民情。"
        },
        2796: {
            "pinyin": "dié chuáng jià wū",
            "meaning": "床上再搭床、屋上再架屋，比喻重复累赘、无谓叠加。",
            "example": "这项制度设计过于复杂，简直是迭床架屋。"
        },
        2797: {
            "pinyin": "dié dié bù xiū",
            "meaning": "形容说话没完没了。",
            "example": "他对同一件事喋喋不休，让人心烦。"
        },
        2798: {
            "pinyin": "dié chuáng jià wū",
            "meaning": "与“迭床架屋”同义，也比喻重复繁琐。",
            "example": "文件审批层级太多，实在是叠床架屋。"
        },
        2799: {
            "pinyin": "dié fěn fēng huáng",
            "meaning": "比喻花卉的绚丽色彩，也形容女子浓妆艳抹。",
            "example": "春园里蝶粉蜂黄，一片繁华景象。"
        },
        2800: {
            "pinyin": "dīng gōng záo jǐng",
            "meaning": "比喻替人做事反而得罪人或吃亏。",
            "example": "这事你若贸然插手，只怕成了丁公凿井。"
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

    print(f"已为 2701–2800 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
