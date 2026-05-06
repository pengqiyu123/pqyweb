import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 为前 100 条成语添加拼音、释义和例句
    enrich = {
        1: {
            "pinyin": "āi āi fù mǔ",
            "meaning": "出自《诗经》，形容父母抚养子女的艰辛劳苦和深切恩情。",
            "example": "读到\"哀哀父母\"这句诗，更让人体会父母的不易。"
        },
        2: {
            "pinyin": "āi āi yù jué",
            "meaning": "形容极度悲伤，悲痛到了几乎要断绝的地步。",
            "example": "亲人离世的消息传来，她悲痛得哀哀欲绝。"
        },
        3: {
            "pinyin": "āi bīng bì shèng",
            "meaning": "指处于困境、怀着悲愤之情的军队更能同仇敌忾，因而容易取胜。",
            "example": "在不被看好的情况下，这支\"哀兵必胜\"的队伍竟然夺得了冠军。"
        },
        4: {
            "pinyin": "āi ér bù shāng",
            "meaning": "感情真挚哀婉，但不过分悲伤哀怨，多用来评价文艺作品的情调。",
            "example": "这篇文章写得哀而不伤，读来令人感动却不至于压抑。"
        },
        5: {
            "pinyin": "āi gǎn tiān dì",
            "meaning": "悲痛之情深切动人，连天地都为之感动。",
            "example": "烈士的事迹哀感天地，让人无不为之落泪。"
        },
        6: {
            "pinyin": "āi gǎn wán yàn",
            "meaning": "感人至深，连性情顽劣或艳丽轻浮的人也会被感动。",
            "example": "这段故事真是哀感顽艳，使听者无不动容。"
        },
        7: {
            "pinyin": "āi gǎn zhōng nián",
            "meaning": "形容中年人感慨人生多舛、身世飘零而产生的悲凉情绪。",
            "example": "旧友重逢，各自经历坎坷，不免有几分哀感中年的滋味。"
        },
        8: {
            "pinyin": "āi gào bīn fú",
            "meaning": "以悲痛哀告的方式使来宾臣服或信服，多形容哀恳劝说。",
            "example": "他以国家危亡相告，可谓哀告宾服，言辞恳切动人心。"
        },
        9: {
            "pinyin": "āi hóng biàn yě",
            "meaning": "比喻到处都是流离失所、悲惨呼号的人民。",
            "example": "战乱之中，村庄被毁，哀鸿遍野，令人揪心。"
        },
        10: {
            "pinyin": "āi huǐ gǔ lì",
            "meaning": "形容极度悲哀、瘦弱憔悴，瘦得只剩皮包骨。",
            "example": "他为父亲守孝多年，竟然消瘦得哀毁骨立。"
        },
        11: {
            "pinyin": "āi lí zhēng shí",
            "meaning": "传说中以蒸熟的梨慰问仇人，形容以德报怨的行为。",
            "example": "他在矛盾化解后还主动帮忙，真有几分哀梨蒸食的味道。"
        },
        12: {
            "pinyin": "āi mò dà yú xīn sǐ",
            "meaning": "没有什么悲哀比内心死寂更严重，形容精神上极度绝望。",
            "example": "经历多次打击之后，他已是哀莫大于心死，不愿再作任何努力。"
        },
        13: {
            "pinyin": "āi sī háo zhú",
            "meaning": "指哀怨的丝弦声与管竹声，比喻凄婉动人的音乐。",
            "example": "曲调悠长，如同哀丝豪竹，让人沉浸在忧伤的氛围中。"
        },
        14: {
            "pinyin": "āi sī rú cháo",
            "meaning": "悲伤的思绪像潮水一样汹涌而来。",
            "example": "每到深夜，他对故乡的哀思如潮，难以入眠。"
        },
        15: {
            "pinyin": "āi tiān jiào dì",
            "meaning": "仰天呼号、伏地号哭，形容极度悲痛和呼天抢地的样子。",
            "example": "听到噩耗，她忍不住哀天叫地，哭成了泪人。"
        },
        16: {
            "pinyin": "āi tòng yù jué",
            "meaning": "形容悲痛到了极点，几乎要昏绝过去。",
            "example": "亲人突然离世，让他悲恸得哀痛欲绝。"
        },
        17: {
            "pinyin": "āi shēng tàn qì",
            "meaning": "不停地叹气，表示心情忧愁、烦闷或不满。",
            "example": "最近工作压力大，他总是唉声叹气。"
        },
        18: {
            "pinyin": "ái fēng jī fèng",
            "meaning": "在风里来回穿梭缝补，形容生活艰辛、奔波劳碌。",
            "example": "为了维持生计，她每日挨风缉缝，十分辛苦。"
        },
        19: {
            "pinyin": "ái jiā ái hù",
            "meaning": "挨家挨户，一家一户地逐个拜访或通知。",
            "example": "志愿者挨家挨户地发放防疫宣传单。"
        },
        20: {
            "pinyin": "ái jiān bìng zú",
            "meaning": "肩挨着肩、脚靠着脚，形容人群拥挤。",
            "example": "节日期间广场上人山人海，挨肩并足。"
        },
        21: {
            "pinyin": "ái jiān cā bǎng",
            "meaning": "肩挨着肩、胳膊擦着胳膊，形容人多拥挤或关系亲密。",
            "example": "地铁高峰时车厢里的人挨肩擦膀，几乎动弹不得。"
        },
        22: {
            "pinyin": "ái jiān cā bèi",
            "meaning": "肩挨着肩、背擦着背，形容人多或关系密切。",
            "example": "山道狭窄，游客们挨肩擦背地缓慢前行。"
        },
        23: {
            "pinyin": "ái jiān cā liǎn",
            "meaning": "肩碰着肩、脸贴着脸，形容挤得非常厉害。",
            "example": "演唱会现场挤得挨肩擦脸，气氛却异常热烈。"
        },
        24: {
            "pinyin": "ái jiān dā bèi",
            "meaning": "肩靠着肩、背挨着背，多形容亲密无间或人多拥挤。",
            "example": "小时候我们挨肩搭背地走在放学路上，充满笑声。"
        },
        25: {
            "pinyin": "ái mén zhú hù",
            "meaning": "挨家挨户，一户一户地去，含有逐一经过之意。",
            "example": "工作人员挨门逐户地登记住户信息。"
        },
        26: {
            "pinyin": "ái sān dǐng wǔ",
            "meaning": "形容人多、相互挤压，也可形容事情接连不断。",
            "example": "顾客挨三顶五地涌进店里，把小店挤得满满当当。"
        },
        27: {
            "pinyin": "ái shān sāi hǎi",
            "meaning": "像山一样叠起、像海一样拥挤，形容人多或东西极多。",
            "example": "节庆广场上人群挨山塞海，热闹非凡。"
        },
        28: {
            "pinyin": "ǎi rán kě qīn",
            "meaning": "神态和蔼可亲，使人容易亲近。",
            "example": "老师总是笑容可掬，显得蔼然可亲。"
        },
        29: {
            "pinyin": "ǎi rán rén zhě",
            "meaning": "形容一个人态度温和、具有仁者风范。",
            "example": "他待人宽厚，举止从容，真像一位蔼然仁者。"
        },
        30: {
            "pinyin": "ǎi rén kàn chǎng",
            "meaning": "比喻能力不足的人反而被推到显眼的位置去主持事情。",
            "example": "让毫无经验的人来负责大项目，无异于矮人看场。"
        },
        31: {
            "pinyin": "ǎi zi kàn xì",
            "meaning": "比喻眼界受限，看问题不全面。",
            "example": "只凭片面信息下结论，无异于矮子看戏。"
        },
        32: {
            "pinyin": "ài kǒu shí xiū",
            "meaning": "因害羞而不好开口说话。",
            "example": "他碍口识羞，有话总是吞吞吐吐。"
        },
        33: {
            "pinyin": "ài shǒu ài jiǎo",
            "meaning": "形容行动受阻、不方便或有所顾虑而放不开手脚。",
            "example": "规则太多，大家做事难免碍手碍脚。"
        },
        34: {
            "pinyin": "ài bié lí kǔ",
            "meaning": "佛教语，指亲人、爱侣分别的痛苦。",
            "example": "长期异地让他们饱受爱别离苦。"
        },
        35: {
            "pinyin": "ài bó ér qíng bù zhuān",
            "meaning": "爱得很广，却感情不专一。",
            "example": "他待人热情却难以专一，有几分爱博而情不专的意味。"
        },
        36: {
            "pinyin": "ài bù rěn shì",
            "meaning": "非常喜爱，以至于舍不得放下或离开。",
            "example": "这本小说他看得爱不忍释，一口气读完。"
        },
        37: {
            "pinyin": "ài bù shì shǒu",
            "meaning": "非常喜爱，拿在手里舍不得放下。",
            "example": "孩子对新玩具爱不释手。"
        },
        38: {
            "pinyin": "ài cái rú kě",
            "meaning": "爱惜人才就像口渴想喝水一样迫切。",
            "example": "这家公司对技术人才爱才如渴，提供了优厚的待遇。"
        },
        39: {
            "pinyin": "ài cái ruò kě",
            "meaning": "同\"爱才如渴\"，形容十分爱惜和渴求人才。",
            "example": "明君爱才若渴，广揽天下贤士。"
        },
        40: {
            "pinyin": "ài cái rú mìng",
            "meaning": "爱财如同爱生命，形容极其贪财。",
            "example": "他一向爱财如命，连小账也要算得清清楚楚。"
        },
        41: {
            "pinyin": "ài guó rú jiā",
            "meaning": "把国家当作自己的家一样热爱。",
            "example": "真正的爱国者总是爱国如家，愿意为之奉献。"
        },
        42: {
            "pinyin": "ài hè shī zhòng",
            "meaning": "因偏爱少数而失去大多数，比喻因偏私而失人心。",
            "example": "领导若过度偏袒一人，容易爱鹤失众。"
        },
        43: {
            "pinyin": "ài lǐ cún yáng",
            "meaning": "出自古代典故，为了保全礼义而不惜牺牲实物。",
            "example": "他宁可损失一些利益，也要守住原则，可谓爱礼存羊。"
        },
        44: {
            "pinyin": "ài máo fǎn qiú",
            "meaning": "只爱惜皮毛而弃掉皮裘，比喻舍本逐末或不知轻重。",
            "example": "在大是大非面前斤斤计较小利，无异于爱毛反裘。"
        },
        45: {
            "pinyin": "ài mín rú zǐ",
            "meaning": "把百姓当作自己的子女一样疼爱。",
            "example": "这位县令政绩斐然，待民爱民如子。"
        },
        46: {
            "pinyin": "ài mò néng zhù",
            "meaning": "虽然同情却没有能力帮助。",
            "example": "看到他的处境，大家都感到爱莫能助。"
        },
        47: {
            "pinyin": "ài qián rú mìng",
            "meaning": "把钱看得像生命一样重要，极其吝啬贪财。",
            "example": "他一向爱钱如命，很少主动请客。"
        },
        48: {
            "pinyin": "ài rén hào shì",
            "meaning": "喜爱贤人并乐于结交，推崇有才德的人。",
            "example": "这位长者爱人好士，门下常有俊彦来访。"
        },
        49: {
            "pinyin": "ài rén lì wù",
            "meaning": "爱护他人并使万物受益，形容胸怀仁爱。",
            "example": "古代仁政讲究爱人利物，关注百姓与自然的和谐。"
        },
        50: {
            "pinyin": "ài rén yǐ dé",
            "meaning": "用德行去爱护、对待他人。",
            "example": "为人处世若能爱人以德，自然能赢得尊敬。"
        },
        51: {
            "pinyin": "ài rì xī lì",
            "meaning": "爱惜光阴和精力，不肯轻易浪费。",
            "example": "他一向爱日惜力，把时间都用在学习上。"
        },
        52: {
            "pinyin": "ài rú jǐ chū",
            "meaning": "像对自己一样去爱护别人。",
            "example": "他待同事真诚宽厚，可谓爱如己出。"
        },
        53: {
            "pinyin": "ài rú zhēn bǎo",
            "meaning": "把人或事物看得像珍宝一样珍爱。",
            "example": "奶奶对孙子爱如珍宝，事事都亲自照料。"
        },
        54: {
            "pinyin": "ài sù hào gǔ",
            "meaning": "喜爱朴素，爱好古代文化或器物。",
            "example": "他向来爱素好古，家里收藏了不少古玩字画。"
        },
        55: {
            "pinyin": "ài wū jí wū",
            "meaning": "因为爱一个人而连带爱屋顶上的乌鸦，比喻爱屋及人。",
            "example": "她喜欢这座城市，多半是因为爱屋及乌。"
        },
        56: {
            "pinyin": "ài xī yǔ máo",
            "meaning": "比喻爱惜自己的名誉或形象。",
            "example": "他一向爱惜羽毛，从不做有损声誉的事。"
        },
        57: {
            "pinyin": "ài zēng fēn míng",
            "meaning": "爱与恨界限分明，态度十分鲜明。",
            "example": "他为人正直，向来爱憎分明。"
        },
        58: {
            "pinyin": "ài zhī yù qí shēng, wù zhī yù qí sǐ",
            "meaning": "喜欢一个人就希望他活着，不喜欢就希望他死，形容爱憎极端强烈。",
            "example": "对角色的态度不应爱之欲其生，恶之欲其死，而要理性客观。"
        },
        59: {
            "pinyin": "ài mèi bù míng",
            "meaning": "态度或关系模糊不清，难以分辨。",
            "example": "他和对方暧昧不明的关系，引起了很多猜测。"
        },
        60: {
            "pinyin": "ài mèi zhī qíng",
            "meaning": "模糊不清、若隐若现的感情，多指男女之间含糊的情愫。",
            "example": "小说中两人之间的暧昧之情写得含蓄而细腻。"
        },
        61: {
            "pinyin": "ān ān wěn wěn",
            "meaning": "形容十分平稳、安定，没有波折。",
            "example": "他只想安安稳稳地过日子。"
        },
        62: {
            "pinyin": "ān bāng dìng guó",
            "meaning": "使国家安定、局势平稳。",
            "example": "这项改革对安邦定国具有深远意义。"
        },
        63: {
            "pinyin": "ān bāng zhì guó",
            "meaning": "使国家安定、治理好国家。",
            "example": "历代君王都在思考如何安邦治国。"
        },
        64: {
            "pinyin": "ān bù wàng wēi",
            "meaning": "在安定时不忘记可能到来的危难。",
            "example": "企业在顺境中也要安不忘危，提前做好风险预案。"
        },
        65: {
            "pinyin": "ān bù dāng chē",
            "meaning": "慢步当作乘车，比喻从容而不急躁。",
            "example": "散步回家，正好安步当车，顺便放松心情。"
        },
        66: {
            "pinyin": "ān cháng chǔ shùn",
            "meaning": "处在安定的环境中顺应事物发展，不求改变。",
            "example": "他性格温和，习惯安常处顺的生活。"
        },
        67: {
            "pinyin": "ān cháng shǒu fèn",
            "meaning": "安于现状，守住本分，不越规矩。",
            "example": "老人一生安常守分，从不逾矩。"
        },
        68: {
            "pinyin": "ān cháng shǒu gù",
            "meaning": "安于旧有的习惯与成规，不愿改变。",
            "example": "如果一味安常守故，就很难有创新发展。"
        },
        69: {
            "pinyin": "ān chē pú lún",
            "meaning": "古代给年老或有功之臣乘坐的安车软轮，象征优待与礼遇。",
            "example": "他功成身退，朝廷以安车蒲轮相送。"
        },
        70: {
            "pinyin": "ān dǔ lè yè",
            "meaning": "百姓安居守业，生活安定快乐。",
            "example": "社会安定，人民才能安堵乐业。"
        },
        71: {
            "pinyin": "ān dǔ rú gù",
            "meaning": "局势安定，像从前一样安稳。",
            "example": "战乱平息后，城市逐渐安堵如故。"
        },
        72: {
            "pinyin": "ān fèn shǒu jǐ",
            "meaning": "安于自己应有的地位与本分，严守分寸。",
            "example": "他一向安分守己，从不做出格的事。"
        },
        73: {
            "pinyin": "ān fèn zhī zú",
            "meaning": "满足于本分，不贪多求快。",
            "example": "学会安分知足，才能内心平和。"
        },
        74: {
            "pinyin": "ān fù xù pín",
            "meaning": "安抚富人、体恤穷人，形容施政得当。",
            "example": "这项政策既安富恤贫，又兼顾长远发展。"
        },
        75: {
            "pinyin": "ān fù zūn róng",
            "meaning": "生活优裕、地位尊贵。",
            "example": "他出身安富尊荣，却依然勤奋好学。"
        },
        76: {
            "pinyin": "ān guó níng jiā",
            "meaning": "国家安定，家庭安宁。",
            "example": "只有安国宁家，人民才能过上好日子。"
        },
        77: {
            "pinyin": "ān hún dìng pò",
            "meaning": "使惊魂不定的人平静下来。",
            "example": "老师的安慰话语，如同安魂定魄的良药。"
        },
        78: {
            "pinyin": "ān jiā lì yè",
            "meaning": "安定家庭，建立事业。",
            "example": "他来到新城市，从头开始安家立业。"
        },
        79: {
            "pinyin": "ān jiā luò hù",
            "meaning": "在一个地方安定下来，登记成户。",
            "example": "他们终于在这座城市安家落户。"
        },
        80: {
            "pinyin": "ān jū lè yè",
            "meaning": "形容安定地居住，愉快地工作。",
            "example": "社会和谐，百姓才能安居乐业。"
        },
        81: {
            "pinyin": "ān lǎo huái shào",
            "meaning": "安养老人，关怀年少，形容对老少都给予照顾。",
            "example": "一个有温度的社会，应做到安老怀少。"
        },
        82: {
            "pinyin": "ān lè wō",
            "meaning": "指舒适安逸的住所。",
            "example": "他在这座小城找到了属于自己的安乐窝。"
        },
        83: {
            "pinyin": "ān liáng chú bào",
            "meaning": "安抚善良的人，清除残暴的人。",
            "example": "古代明君主张安良除暴，赢得百姓拥护。"
        },
        84: {
            "pinyin": "ān méi dài yǎn",
            "meaning": "形容神态安详、眉目舒展。",
            "example": "他面带微笑，神情安眉带眼，看上去很温和。"
        },
        85: {
            "pinyin": "ān mín gào shì",
            "meaning": "为安抚百姓而发布的告示、公告。",
            "example": "政府及时发布安民告示，稳定了人心。"
        },
        86: {
            "pinyin": "ān nèi rǎng wài",
            "meaning": "安定内部，抵御外患。",
            "example": "要想国家长治久安，必须安内攘外。"
        },
        87: {
            "pinyin": "ān pín lè dào",
            "meaning": "安于清贫，以践行道义为乐。",
            "example": "他虽生活简朴，却安贫乐道。"
        },
        88: {
            "pinyin": "ān pín lè jiàn",
            "meaning": "安于贫贱，并以此自得其乐。",
            "example": "他们夫妻二人安贫乐贱，相互扶持。"
        },
        89: {
            "pinyin": "ān rán rú gù",
            "meaning": "安然自若，像从前一样没有变化。",
            "example": "面对流言，他依旧安然如故，专心做事。"
        },
        90: {
            "pinyin": "ān rán wú shì",
            "meaning": "安然自在，仿佛没有发生什么事情。",
            "example": "别人都在忙碌，他却安然无事地喝茶聊天。"
        },
        91: {
            "pinyin": "ān rán wú yàng",
            "meaning": "安稳平静，没有受到损害或病痛。",
            "example": "台风过去后，村庄依旧安然无恙。"
        },
        92: {
            "pinyin": "ān rěn wú qīn",
            "meaning": "残忍到对亲人也毫不顾惜。",
            "example": "他为了利益不择手段，简直到了安忍无亲的地步。"
        },
        93: {
            "pinyin": "ān rú pán shí",
            "meaning": "像巨石一样稳固，形容非常牢靠安稳。",
            "example": "他们之间的友谊安如磐石。"
        },
        94: {
            "pinyin": "ān rú tài shān",
            "meaning": "像泰山一样稳固，形容极其安稳牢靠。",
            "example": "在父母的支持下，他心里安如泰山。"
        },
        95: {
            "pinyin": "ān shēn lì mìng",
            "meaning": "在社会上站稳脚跟，确立自己的人生目标。",
            "example": "年轻人要努力学习本领，以求安身立命。"
        },
        96: {
            "pinyin": "ān shēn wéi lè",
            "meaning": "以自身安定为快乐，多指不求进取，只顾自保。",
            "example": "他只图安身为乐，对外界的变化漠不关心。"
        },
        97: {
            "pinyin": "ān shēn zhī chǔ",
            "meaning": "立身存活的去处。",
            "example": "这份工作是他在城市里的安身之处。"
        },
        98: {
            "pinyin": "ān shēn zhī dì",
            "meaning": "可以安身立足的地方。",
            "example": "多年漂泊后，他终于找到了安身之地。"
        },
        99: {
            "pinyin": "ān shí chǔ shùn",
            "meaning": "在适当的时候顺应环境而行。",
            "example": "做人要懂得安时处顺，不必强求难成之事。"
        },
        100: {
            "pinyin": "ān shì lì chǔ",
            "meaning": "使居室安定，有利于居住，多指安居之所。",
            "example": "这套房子位置合适，又安室利处，全家都很满意。"
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

    print(f"已为前 100 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
