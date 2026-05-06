import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 为 301–400 条成语添加拼音、释义和例句
    enrich = {
        301: {
            "pinyin": "bā jiǔ bù lí shí",
            "meaning": "形容事物与实际情况很接近，大体相符。",
            "example": "根据经验估算的结果和实测值八九不离十。"
        },
        302: {
            "pinyin": "bā miàn jiàn guāng",
            "meaning": "比喻到处攀附、讨好别人，或指四处受人欢迎。",
            "example": "他处事圆滑，在单位里八面见光。"
        },
        303: {
            "pinyin": "bā miàn líng lóng",
            "meaning": "形容待人处事周到圆滑，各方面都应付得很得体。",
            "example": "她性格外向，说话做事八面玲珑。"
        },
        304: {
            "pinyin": "bā miàn wēi fēng",
            "meaning": "形容气势盛大，威风凛凛，令人敬畏。",
            "example": "将军披挂上阵，真有八面威风之势。"
        },
        305: {
            "pinyin": "bā miàn yíng chè",
            "meaning": "四面八方都晶莹透彻，比喻光明磊落、毫无污点。",
            "example": "他为人清白，如玉一般八面莹澈。"
        },
        306: {
            "pinyin": "bā miàn yuán tōng",
            "meaning": "各个方面都应付得很周到圆滑。",
            "example": "做生意的人往往八面圆通，善于沟通。"
        },
        307: {
            "pinyin": "bā miàn zhāng luo",
            "meaning": "到处张罗、照应，形容非常忙碌。",
            "example": "婚礼当天他忙得八面张罗。"
        },
        308: {
            "pinyin": "bā xiān guò hǎi, gè xiǎn shén tōng",
            "meaning": "比喻各有各的本领和办法，各自施展才能。",
            "example": "解决这个难题，大家可以八仙过海，各显神通。"
        },
        309: {
            "pinyin": "bā yīn dié zòu",
            "meaning": "八种乐器轮番奏响，形容音乐演奏和谐优美。",
            "example": "乐团演出时八音迭奏，场面十分壮观。"
        },
        310: {
            "pinyin": "bā zhēn yù shí",
            "meaning": "各种珍贵的美味食物，形容丰盛的筵席。",
            "example": "宴会上八珍玉食，十分奢华。"
        },
        311: {
            "pinyin": "bā zì dǎ kāi",
            "meaning": "比喻事情已经有眉目或婚事已有合适对象。",
            "example": "工作还没开始，项目的八字倒是先打开了。"
        },
        312: {
            "pinyin": "bā zì méi yī piě",
            "meaning": "比喻事情还没有任何眉目。",
            "example": "这件事目前八字没一撇，先别着急。"
        },
        313: {
            "pinyin": "bā gāo wàng shàng",
            "meaning": "巴结地位高的人，向上攀附。",
            "example": "他老是巴高望上，喜欢巴结上司。"
        },
        314: {
            "pinyin": "bā qián suàn hòu",
            "meaning": "事前事后都反复打算、盘算。",
            "example": "为了这次投资，他巴前算后，思量了很久。"
        },
        315: {
            "pinyin": "bā sān lǎn sì",
            "meaning": "东张西望，心思不专一。",
            "example": "上课的时候不要巴三览四，要专心听讲。"
        },
        316: {
            "pinyin": "bā shān shǔ shuǐ",
            "meaning": "指巴蜀一带的高山和江水，也形容山川险要秀丽。",
            "example": "他们沿着巴山蜀水一路旅行，欣赏美景。"
        },
        317: {
            "pinyin": "bā shān yè yǔ",
            "meaning": "出自诗句，形容他乡夜雨中思念家乡的情景。",
            "example": "每逢秋雨，他总会想起诗中的巴山夜雨。"
        },
        318: {
            "pinyin": "bā tóu tàn nǎo",
            "meaning": "探头探脑，形容鬼鬼祟祟的样子。",
            "example": "他在门口巴头探脑，看起来很可疑。"
        },
        319: {
            "pinyin": "bá běn sāi yuán",
            "meaning": "拔掉树本、堵住水源，比喻从根本上加以破坏。",
            "example": "只重眼前利益而不顾长远，无异于拔本塞源。"
        },
        320: {
            "pinyin": "bá cuì chū qún",
            "meaning": "才能特别优秀，超出众人。",
            "example": "在众多选手中，她的表现拔萃出群。"
        },
        321: {
            "pinyin": "bá dāo xiāng zhù",
            "meaning": "拔刀相助，形容见义勇为，帮助有难的人。",
            "example": "他路见不平，立刻拔刀相助。"
        },
        322: {
            "pinyin": "bá dì yáo shān",
            "meaning": "形容力量非常大，可以撼动山岳。",
            "example": "战士们士气高昂，仿佛有拔地摇山之力。"
        },
        323: {
            "pinyin": "bá dì yǐ tiān",
            "meaning": "山峰拔地而起，直插云天，形容山势高峻。",
            "example": "远处群峰拔地倚天，气势雄伟。"
        },
        324: {
            "pinyin": "bá dīng chōu xiè",
            "meaning": "比喻抽走关键人物或要害部分，影响全局。",
            "example": "贸然调走骨干，无异于拔丁抽楔。"
        },
        325: {
            "pinyin": "bá kuí dàn zǎo",
            "meaning": "比喻做事不顾本末，处置不当。",
            "example": "只图眼前痛快而不顾后果，简直是拔葵啖枣。"
        },
        326: {
            "pinyin": "bá kuí qù zhī",
            "meaning": "指劳民伤财或扰乱民生的做法，出自劝谏之辞。",
            "example": "苛捐杂税无异于拔葵去织，增加百姓负担。"
        },
        327: {
            "pinyin": "bá lái bào wǎng",
            "meaning": "来往奔走，互相应酬。",
            "example": "节日期间邻里之间拔来报往，其乐融融。"
        },
        328: {
            "pinyin": "bá le luó bo dì pí kuān",
            "meaning": "比喻失去一个人或事物后空出很大地方。",
            "example": "他一走，办公室好像拔了萝卜地皮宽。"
        },
        329: {
            "pinyin": "bá máo lián rú",
            "meaning": "比喻选拔一个人会牵连到一群人。",
            "example": "提拔一个骨干往往会拔茅连茹，带动一批人。"
        },
        330: {
            "pinyin": "bá miáo zhù zhǎng",
            "meaning": "揠苗助长，比喻违反规律、急于求成反而坏事。",
            "example": "学习要循序渐进，不能拔苗助长。"
        },
        331: {
            "pinyin": "bá shí dé wǔ",
            "meaning": "本想得到十成却只得到五成，比喻不尽人意。",
            "example": "计划执行不力，结果拔十得五。"
        },
        332: {
            "pinyin": "bá shān chāo hǎi",
            "meaning": "形容力量巨大，可以翻山越海。",
            "example": "在困难面前，他有一种拔山超海的气概。"
        },
        333: {
            "pinyin": "bá shān gài shì",
            "meaning": "形容力量或气势极其雄壮，盖世无双。",
            "example": "项羽力能扛鼎，号称拔山盖世。"
        },
        334: {
            "pinyin": "bá shān gāng dǐng",
            "meaning": "形容力大无穷，可以举起极重之物。",
            "example": "古书中常写英雄拔山扛鼎的壮举。"
        },
        335: {
            "pinyin": "bá shù xún gēn",
            "meaning": "拔掉树木寻找根部，比喻追究事物的根源。",
            "example": "要解决问题，还得拔树寻根，从源头抓起。"
        },
        336: {
            "pinyin": "bá xī zhuó xiàng",
            "meaning": "比喻选拔杰出的贤才。",
            "example": "朝廷四处拔犀擢象，延揽人才。"
        },
        337: {
            "pinyin": "bá xīn lǐng yì",
            "meaning": "标新立异，提出新奇独特的见解。",
            "example": "这篇论文在观点上拔新领异，很有创见。"
        },
        338: {
            "pinyin": "bá zhái shàng shēng",
            "meaning": "连屋带人一起升天，比喻全家得到升迁或福泽。",
            "example": "古人传说修行成仙时可以拔宅上升。"
        },
        339: {
            "pinyin": "bá zhì yì zhì",
            "meaning": "换掉旧旗帜，树立新旗帜，比喻政权或立场的改变。",
            "example": "那次政变之后，他们拔帜易帜，另立新号。"
        },
        340: {
            "pinyin": "bá hù zì zì",
            "meaning": "蛮横跋扈，为所欲为。",
            "example": "他仗势跋扈自恣，终究不得人心。"
        },
        341: {
            "pinyin": "bá qián zhì hòu",
            "meaning": "向前走时跌倒，向后退也跌倒，比喻处境困难，进退两难。",
            "example": "面对复杂局势，他感到跋前踬后。"
        },
        342: {
            "pinyin": "bá shān shè shuǐ",
            "meaning": "翻山越岭，涉过江河，形容旅途艰辛。",
            "example": "多年来他跋山涉水，为乡村教育奔走。"
        },
        343: {
            "pinyin": "bǎ bì rù lín",
            "meaning": "挽着胳膊走进树林，比喻亲密结交。",
            "example": "他们把臂入林，畅谈理想。"
        },
        344: {
            "pinyin": "bǎ chí bù dìng",
            "meaning": "拿不定主意，犹豫不决。",
            "example": "面对多个选择，他一时把持不定。"
        },
        345: {
            "pinyin": "bǎ fàn jiào jī",
            "meaning": "明明吃饱了却喊饿，比喻故意叫苦。",
            "example": "有些人明明日子不错，却总把饭叫饥。"
        },
        346: {
            "pinyin": "bǎ sù chí zhāi",
            "meaning": "吃素、持斋，指虔诚修行或表示庄重。",
            "example": "他为了祈福，特地把素持斋。"
        },
        347: {
            "pinyin": "bǎ wán wú yàn",
            "meaning": "把玩欣赏，永不厌倦。",
            "example": "这件古玩精致雅致，令人把玩无厌。"
        },
        348: {
            "pinyin": "bà chù bǎi jiā",
            "meaning": "指独尊一家学说而罢黜其他学派。",
            "example": "历史上的罢黜百家、独尊儒术影响深远。"
        },
        349: {
            "pinyin": "bà líng zuì wèi",
            "meaning": "典出故事，指酒后失礼或意外遭遇。",
            "example": "他一时豪饮，差点演成霸陵醉尉的笑话。"
        },
        350: {
            "pinyin": "bà wáng bié jī",
            "meaning": "霸王与爱妾诀别的故事，比喻生离死别的悲壮场面。",
            "example": "这出戏演的是霸王别姬，情节凄美动人。"
        },
        351: {
            "pinyin": "bà wáng fēng yuè",
            "meaning": "借指英雄儿女的儿女情长与风流韵事。",
            "example": "小说中既写战场，也写霸王风月。"
        },
        352: {
            "pinyin": "bái bì qīng yíng",
            "meaning": "洁白的玉璧上落着苍蝇，比喻在好人身边出现小人。",
            "example": "他身边的拍马者如同白璧青蝇。"
        },
        353: {
            "pinyin": "bái bì wéi xiá",
            "meaning": "美玉上有细小瑕疵，比喻人或事物大体很好但有小缺点。",
            "example": "这份方案只是白璧微瑕，总体还是很优秀。"
        },
        354: {
            "pinyin": "bái bì wú xiá",
            "meaning": "洁白的玉璧没有一点瑕疵，比喻人品或事物完美无缺。",
            "example": "在大家心中，他几乎是白璧无瑕的榜样。"
        },
        355: {
            "pinyin": "bái dīng sú kè",
            "meaning": "指平民百姓或文化浅薄的俗人。",
            "example": "那会儿他只是个白丁俗客，并不显眼。"
        },
        356: {
            "pinyin": "bái fà cāng yán",
            "meaning": "头发花白、脸色苍老，形容年老。",
            "example": "几年不见，他已是白发苍颜。"
        },
        357: {
            "pinyin": "bái fà hóng yán",
            "meaning": "头发花白，脸色却红润，形容老当益壮。",
            "example": "老太太白发红颜，精神矍铄。"
        },
        358: {
            "pinyin": "bái fà qiān zhàng",
            "meaning": "形容愁思深重，似乎连头发都长了千丈。",
            "example": "忧愁太多，让人有白发千丈之感。"
        },
        359: {
            "pinyin": "bái fà qīng shān",
            "meaning": "白发配青衫，形容老年仍怀壮志或处境落魄。",
            "example": "他白发青衫，仍奔走于理想之路。"
        },
        360: {
            "pinyin": "bái fàn qīng chú",
            "meaning": "指粗茶淡饭的清苦生活。",
            "example": "即使白饭青刍，他也甘之如饴。"
        },
        361: {
            "pinyin": "bái guī zhī diàn",
            "meaning": "洁白玉圭上微小的污点，比喻美中不足的小缺陷。",
            "example": "这点小错误不过是白圭之玷。"
        },
        362: {
            "pinyin": "bái hēi fēn míng",
            "meaning": "是非、善恶分得很清楚。",
            "example": "他做事向来白黑分明，从不偏袒。"
        },
        363: {
            "pinyin": "bái hóng guàn rì",
            "meaning": "白色的彩虹横贯日中，古人视为不祥之兆。",
            "example": "史书记载，战前曾出现白虹贯日的天象。"
        },
        364: {
            "pinyin": "bái huá zhī yuàn",
            "meaning": "出自《诗经》，比喻女子遭弃的怨情。",
            "example": "她境遇坎坷，有几分白华之怨的意味。"
        },
        365: {
            "pinyin": "bái jū guò xì",
            "meaning": "白色骏马奔驰过细小缝隙，比喻光阴飞逝。",
            "example": "岁月如白驹过隙，转眼已多年。"
        },
        366: {
            "pinyin": "bái jū kōng gǔ",
            "meaning": "好马闲置在空谷，比喻贤才不得重用。",
            "example": "这位学者长期白驹空谷，难以施展才华。"
        },
        367: {
            "pinyin": "bái là míng jīng",
            "meaning": "指刻苦攻读经书，直到蜡尽灯残。",
            "example": "他青年时白蜡明经，寒窗苦读。"
        },
        368: {
            "pinyin": "bái lóng yú fú",
            "meaning": "龙穿上鱼的衣服，比喻隐居或伪装身份的人。",
            "example": "名士微服私访，宛如白龙鱼服。"
        },
        369: {
            "pinyin": "bái máo huáng yuè",
            "meaning": "古代军中仪仗，借指兵权或征伐。",
            "example": "他再披白旄黄钺，率军出征。"
        },
        370: {
            "pinyin": "bái méi chì yǎn",
            "meaning": "眉毛白、眼圈红，形容愤怒的样子。",
            "example": "他被冤枉得白眉赤眼，大声辩解。"
        },
        371: {
            "pinyin": "bái miàn shū shēng",
            "meaning": "形容年轻书生面孔白净，经验不足。",
            "example": "他只是个白面书生，却有远大抱负。"
        },
        372: {
            "pinyin": "bái rì jiàn guǐ",
            "meaning": "大白天见到鬼，比喻荒诞离奇或根本不可能的事。",
            "example": "这种说法简直是白日见鬼。"
        },
        373: {
            "pinyin": "bái rì shēng tiān",
            "meaning": "白日飞升成仙，比喻一举成名或飞黄腾达。",
            "example": "他夺冠那一刻，仿佛白日升天。"
        },
        374: {
            "pinyin": "bái rì yī xiù",
            "meaning": "白天穿着绣花衣服，比喻炫耀荣耀于不当之处。",
            "example": "在灾区炫富，如同白日衣绣，极不合适。"
        },
        375: {
            "pinyin": "bái rì zuò mèng",
            "meaning": "形容根本不现实的幻想。",
            "example": "不努力却想成功，只是白日做梦。"
        },
        376: {
            "pinyin": "bái shān hēi shuǐ",
            "meaning": "指东北一带的山川，也泛指北方边远地区。",
            "example": "他远赴白山黑水支教多年。"
        },
        377: {
            "pinyin": "bái shǒu qǐ jiā",
            "meaning": "空手起家，凭自己的双手建立事业。",
            "example": "他从小摊做起，白手起家成了企业家。"
        },
        378: {
            "pinyin": "bái shǒu běi miàn",
            "meaning": "年老时向北面事人，比喻晚年不得志。",
            "example": "他不愿白首北面，更加努力打拼。"
        },
        379: {
            "pinyin": "bái shǒu kōng guī",
            "meaning": "白了头却空手而归，比喻一生劳而无成。",
            "example": "若虚度年华，难免白首空归。"
        },
        380: {
            "pinyin": "bái shǒu qióng jīng",
            "meaning": "到老仍苦读经书，形容治学刻苦。",
            "example": "他白首穷经，一生钻研学问。"
        },
        381: {
            "pinyin": "bái shǒu xiāng zhī",
            "meaning": "终身相知相交的朋友。",
            "example": "他们是白首相知的老友。"
        },
        382: {
            "pinyin": "bái shǒu zhī xīn",
            "meaning": "到老不变的忠心或情意。",
            "example": "她对白首之心的承诺始终未变。"
        },
        383: {
            "pinyin": "bái shuǐ jiàn xīn",
            "meaning": "用清澈的水照见人心，比喻心地清白。",
            "example": "他行事光明磊落，可谓白水鉴心。"
        },
        384: {
            "pinyin": "bái tóu rú xīn",
            "meaning": "虽然白了头，却像新相识一样疏远，形容朋友感情变淡。",
            "example": "多年不见，他们竟有几分白头如新的生疏。"
        },
        385: {
            "pinyin": "bái tóu xiāng shǒu",
            "meaning": "夫妻相守到老。",
            "example": "老人俩白头相守，令人羡慕。"
        },
        386: {
            "pinyin": "bái tóu xié lǎo",
            "meaning": "夫妻共同生活到白头，形容婚姻美满长久。",
            "example": "祝你们新婚快乐，白头偕老。"
        },
        387: {
            "pinyin": "bái wǎng hēi lái",
            "meaning": "把黑说成白，把白说成黑，颠倒是非。",
            "example": "他在众人面前白往黑来，令人愤怒。"
        },
        388: {
            "pinyin": "bái wū hán mén",
            "meaning": "简陋的房屋、寒门子弟。",
            "example": "他出身白屋寒门，却靠努力改变了命运."
        },
        389: {
            "pinyin": "bái xuě ái ái",
            "meaning": "形容积雪非常厚，连绵不绝。",
            "example": "山顶白雪皑皑，景色壮丽。"
        },
        390: {
            "pinyin": "bái yǎn xiāng kàn",
            "meaning": "用白眼看人，形容轻视或厌恶。",
            "example": "他一听到这个名字就白眼相看。"
        },
        391: {
            "pinyin": "bái yī gōng qīng",
            "meaning": "没有官职却有公卿的声望和地位。",
            "example": "这位学者虽非官员，却是白衣公卿。"
        },
        392: {
            "pinyin": "bái yī qīng xiàng",
            "meaning": "没有官职却有卿相的名望和才能。",
            "example": "他学识渊博，人称白衣卿相。"
        },
        393: {
            "pinyin": "bái yī xiù shì",
            "meaning": "身着白衣的秀才，比喻未得官职的读书人。",
            "example": "年轻时他只是白衣秀士，却胸怀大志。"
        },
        394: {
            "pinyin": "bái yú rù zhōu",
            "meaning": "白鱼跳入船中，古人视为祥瑞之兆。",
            "example": "史书上记载，有年河中白鱼入舟，被视作好征兆。"
        },
        395: {
            "pinyin": "bái yún cāng gǒu",
            "meaning": "白云变成苍狗，比喻世事变幻无常。",
            "example": "几十年过去，世事白云苍狗。"
        },
        396: {
            "pinyin": "bái yún gū fēi",
            "meaning": "孤云在天空飘飞，常用以表现孤寂或飘零。",
            "example": "远山之上白云孤飞，景色清寂。"
        },
        397: {
            "pinyin": "bái yún qīn shě",
            "meaning": "白云环绕着亲人住处，比喻对故乡和亲人的思念。",
            "example": "他常梦见白云亲舍，心中满是乡愁。"
        },
        398: {
            "pinyin": "bái zhǐ hēi zì",
            "meaning": "白纸上写着黑字，比喻证据确凿，不容否认。",
            "example": "合同白纸黑字写得清清楚楚。"
        },
        399: {
            "pinyin": "bǎi bān diāo nán",
            "meaning": "用尽各种手段百般刁难。",
            "example": "他在审批时百般刁难，让人十分为难。"
        },
        400: {
            "pinyin": "bǎi bù chuān yáng",
            "meaning": "在百步之外射中杨树的叶子，形容射箭或枪法极准，也比喻技术高超。",
            "example": "射击队员个个百步穿杨，弹无虚发。"
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

    print(f"已为 301–400 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
