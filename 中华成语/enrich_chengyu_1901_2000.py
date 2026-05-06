import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    enrich = {
        1901: {
            "pinyin": "chuí sǐ zhēng zhá",
            "meaning": "在临死之前做最后的挣扎，比喻在失败前作徒劳的抵抗。",
            "example": "敌军已被包围，只剩下垂死挣扎的余地。"
        },
        1902: {
            "pinyin": "chuí tóu sàng qì",
            "meaning": "低着头，叹着气，形容情绪低落、非常沮丧。",
            "example": "比赛失利后，他一直垂头丧气，不愿多说话。"
        },
        1903: {
            "pinyin": "chuí xián sān chǐ",
            "meaning": "形容看到美味的食物非常贪馋，口水直流。也比喻对某种事物十分眼热、极想得到。",
            "example": "橱窗里的甜点色香味俱全，看得人垂涎三尺。"
        },
        1904: {
            "pinyin": "chuí xián yù dī",
            "meaning": "口水快要流下来了，比喻非常贪馋或极其羡慕。",
            "example": "听他讲起环球旅行的见闻，大家都羡慕得垂涎欲滴。"
        },
        1905: {
            "pinyin": "chuí xiōng dùn zú",
            "meaning": "一会儿捶打胸口，一会儿跺脚，形容非常懊悔或极度悲痛。",
            "example": "要是当初多留个心眼，也不至于现在捶胸顿足。"
        },
        1906: {
            "pinyin": "chūn bīng hǔ wěi",
            "meaning": "踩在春天将融的薄冰和老虎尾巴上，比喻处境极其危险。",
            "example": "在金融市场上盲目冒险，无异于行走春冰虎尾。"
        },
        1907: {
            "pinyin": "chūn fēng dé yì",
            "meaning": "像春风吹拂一样得意舒畅，形容人顺心如意、意气风发。",
            "example": "升职之后，他整个人春风得意，干劲十足。"
        },
        1908: {
            "pinyin": "chūn fēng fēng rén",
            "meaning": "比喻像春风一样给人以温和的感化，多指文章、教化等对人的熏陶。",
            "example": "这本传记文字温润，如春风风人，令人深受感动。"
        },
        1909: {
            "pinyin": "chūn fēng hé qì",
            "meaning": "像春风那样和煦，形容态度温和可亲、气氛融洽。",
            "example": "老师总是春风和气地与学生交流，却又不失原则。"
        },
        1910: {
            "pinyin": "chūn fēng huà yǔ",
            "meaning": "像春风细雨那样润物无声，比喻良好的教育或恩德对人潜移默化的影响。",
            "example": "这位老校长多年来春风化雨，培养了无数人才。"
        },
        1911: {
            "pinyin": "chūn fēng mǎn miàn",
            "meaning": "好像春风吹拂着脸庞，形容人的神情和蔼、满脸喜悦。",
            "example": "听到项目成功的消息，他春风满面地走进办公室。"
        },
        1912: {
            "pinyin": "chūn fēng xià yǔ",
            "meaning": "春风与夏雨，比喻适时适度的教化与恩泽。",
            "example": "良师益友的指点，如同春风夏雨，让他受益匪浅。"
        },
        1913: {
            "pinyin": "chūn fēng yí dù",
            "meaning": "原指春夜一度风情，后多指短暂的男女欢会。",
            "example": "小说中那场春风一度，最终却换来一地伤心。"
        },
        1914: {
            "pinyin": "chūn fēng yí shuǐ",
            "meaning": "语出先秦典籍，形容春日和风拂面、沂水清澈的闲适景象，后多指恬淡安乐的生活。",
            "example": "退休后，他向往的正是那种春风沂水的田园日子。"
        },
        1915: {
            "pinyin": "chūn guāng lòu xiè",
            "meaning": "本指春日景色从缝隙中泄出，后多比喻男女私情泄露或隐秘感情流露。",
            "example": "两人眼神里的默契早已让春光漏泄。"
        },
        1916: {
            "pinyin": "chūn guāng míng mèi",
            "meaning": "形容春天阳光明媚、景色鲜艳动人。",
            "example": "在这春光明媚的周末，公园里到处是踏青的人群。"
        },
        1917: {
            "pinyin": "chūn hán liào qiào",
            "meaning": "料峭：微寒。形容初春乍暖还寒、带着寒意的天气。",
            "example": "清晨的风仍然春寒料峭，出门别忘了加件外套。"
        },
        1918: {
            "pinyin": "chūn hé jǐng míng",
            "meaning": "春天气候温和、景物明朗，形容万物复苏、风光秀丽的景象。",
            "example": "在这春和景明的时节，江面上白帆点点。"
        },
        1919: {
            "pinyin": "chūn huā qiū yuè",
            "meaning": "春天的花、秋天的月，泛指良辰美景，多与离愁别绪、伤感往事联系在一起。",
            "example": "在这般春花秋月的夜晚，他不免想起旧日恋人。"
        },
        1920: {
            "pinyin": "chūn huá qiū shí",
            "meaning": "春天开花，秋天结果，比喻事物发展的过程和结果，也指付出与收获。",
            "example": "教育工作要耐心耕耘，才能见到春华秋实的回报。"
        },
        1921: {
            "pinyin": "chūn huī cùn cǎo",
            "meaning": "出自“谁言寸草心，报得三春晖”，比喻子女难以报答父母深厚恩情。",
            "example": "那一声叮嘱，让他再次体会到春晖寸草之意。"
        },
        1922: {
            "pinyin": "chūn huí dà dì",
            "meaning": "春天回到大地，形容严冬过去、万物复苏，也比喻局势好转或重新焕发生机。",
            "example": "经济逐渐复苏，城市仿佛春回大地。"
        },
        1923: {
            "pinyin": "chūn lán qiū jú",
            "meaning": "春天的兰花、秋天的菊花，各有其美，比喻各有所长、各得其所。",
            "example": "每个孩子都有春兰秋菊般的优点，教育要因材施教。"
        },
        1924: {
            "pinyin": "chūn lù qiū shuāng",
            "meaning": "春天的露水、秋天的霜，多用来比喻时序变换或荣辱兴衰的交替。",
            "example": "世事如春露秋霜，盛衰更替不足为奇。"
        },
        1925: {
            "pinyin": "chūn mèng wú hén",
            "meaning": "如春日美梦般短暂而无痕，常用来形容一段感情或往事转瞬即逝。",
            "example": "回想那段时光，终究不过是春梦无痕。"
        },
        1926: {
            "pinyin": "chūn nuǎn huā kāi",
            "meaning": "春天气候温暖、百花盛开，常用来形容景色宜人或好时机的到来。",
            "example": "在这春暖花开的日子里，一切似乎都充满希望。"
        },
        1927: {
            "pinyin": "chūn pā lì zǎo",
            "meaning": "春葩、丽藻本指华美的花朵与水藻，比喻文辞华丽、文采斐然。",
            "example": "这篇文章辞藻瑰丽，可谓春葩丽藻。"
        },
        1928: {
            "pinyin": "chūn qiū bǐ fǎ",
            "meaning": "指像《春秋》那样寓褒贬于字里行间的写作手法，褒贬分明而含蓄。",
            "example": "这部史书多用春秋笔法，对人物评判极有分寸。"
        },
        1929: {
            "pinyin": "chūn qiū dǐng shèng",
            "meaning": "春秋：比喻年纪；鼎盛：最兴盛的时候。指人正处在精力最旺盛的壮年时期。",
            "example": "他正值春秋鼎盛，事业上大有可为。"
        },
        1930: {
            "pinyin": "chūn qiū wú yì zhàn",
            "meaning": "指春秋时期的战争多不合正义，后泛指以侵略、掠夺为目的的不义之战。",
            "example": "历史一再证明，春秋无义战，侵略终将失败。"
        },
        1931: {
            "pinyin": "chūn sè liáo rén",
            "meaning": "春天的景色撩拨人心，形容春景动人，也含有容易引发情思的意味。",
            "example": "江南三月春色撩人，游客流连忘返。"
        },
        1932: {
            "pinyin": "chūn sè mǎn yuán",
            "meaning": "整个庭园都充满了春天的景色，形容春意盎然、花木繁盛。",
            "example": "推窗远望，只见春色满园，绿意葱茏。"
        },
        1933: {
            "pinyin": "chūn shān rú xiào",
            "meaning": "春天的山色仿佛在微笑，形容春山秀丽明媚、生机盎然。",
            "example": "细雨初歇，远处春山如笑，景色宜人。"
        },
        1934: {
            "pinyin": "chūn shēn sì hǎi",
            "meaning": "春意浓极，如海之深广，形容春色正浓、景象繁盛。",
            "example": "一路花树相迎，只觉春深似海。"
        },
        1935: {
            "pinyin": "chūn shēng qiū shā",
            "meaning": "春天万物生长，秋天草木凋零，比喻自然界或社会事物盛衰消长的规律。",
            "example": "世间万事皆有春生秋杀的节律，不必过分执着。"
        },
        1936: {
            "pinyin": "chūn shēng xià zhǎng, qiū shōu dōng cáng",
            "meaning": "春天生发、夏天生长、秋天收获、冬天收藏，概括了一年四季的自然与生产规律。",
            "example": "农业生产要顺应春生夏长、秋收冬藏的节奏安排。"
        },
        1937: {
            "pinyin": "chūn shù mù yún",
            "meaning": "春天的树木、傍晚的云彩，多用来寄托对远方亲友的思念之情。",
            "example": "每逢春树暮云之时，他总会想起故乡的母亲。"
        },
        1938: {
            "pinyin": "chūn sòng xià xián",
            "meaning": "春天念书，夏天学琴，形容学生整年不停地学习，也指良好的教育环境。",
            "example": "古代书院讲求春诵夏弦，文武兼修。"
        },
        1939: {
            "pinyin": "chūn sǔn nù fà",
            "meaning": "春天的竹笋迅猛生长，形容新事物、新力量大量、迅速地涌现出来。",
            "example": "创业公司如春笋怒发般出现在这座城市。"
        },
        1940: {
            "pinyin": "chūn wā qiū chán",
            "meaning": "春天的青蛙、秋天的蝉，叫声喧闹，常比喻聒噪多言的人声或议论。",
            "example": "网络上众声喧哗，不免有些春蛙秋蝉之感。"
        },
        1941: {
            "pinyin": "chūn xiāo yí kè",
            "meaning": "出自“春宵一刻值千金”，形容春夜短暂而美好，常暗指良辰美景或爱情欢会。",
            "example": "在这春宵一刻的良夜里，古城灯火如昼。"
        },
        1942: {
            "pinyin": "chūn yì àng rán",
            "meaning": "春天的气息格外浓厚，形容到处洋溢着勃勃生机。",
            "example": "雨后公园春意盎然，游人络绎不绝。"
        },
        1943: {
            "pinyin": "chūn yì lán shān",
            "meaning": "春意将尽、景色衰减，常带有惆怅、伤感的情绪。",
            "example": "花事已过，庭院里一片春意阑珊。"
        },
        1944: {
            "pinyin": "chūn yǐn qiū shé",
            "meaning": "像春蚯蚓、秋游蛇那样蜿蜒盘曲，多用来形容书法笔画富有变化、姿态生动。",
            "example": "这幅行书笔势宛转，有春蚓秋蛇之妙。"
        },
        1945: {
            "pinyin": "chūn yǔ rú yóu",
            "meaning": "春天的雨像油一样珍贵，形容春雨对农作物生长十分重要。",
            "example": "久旱逢甘霖，乡亲们都说这场春雨如油。"
        },
        1946: {
            "pinyin": "chūn xuān bìng mào",
            "meaning": "椿象父亲，萱象母亲，比喻父母都健在且安康。",
            "example": "他最庆幸的是双亲尚在堂，真可谓椿萱并茂。"
        },
        1947: {
            "pinyin": "chún jiǔ fù rén",
            "meaning": "醇厚的美酒和美貌的女子，比喻容易使人沉迷的酒色享乐。",
            "example": "古人常以醇酒妇人为戒，提醒自己克制欲望。"
        },
        1948: {
            "pinyin": "chún jū kòu shí",
            "meaning": "像鹑鸟的窝一样狭小的住所、像雏鸟进食一样微薄的口粮，比喻居住简陋、生活困苦。",
            "example": "他在城里鹑居鷇食多年，只为守住一份理想。"
        },
        1949: {
            "pinyin": "chún yī bǎi jié",
            "meaning": "鹑衣：打满补丁的衣服；百结：多处打结。形容衣服破烂不堪、贫困潦倒的样子。",
            "example": "旧社会许多穷人常是鹑衣百结、食不果腹。"
        },
        1950: {
            "pinyin": "chún zhèng wú xié",
            "meaning": "纯洁正直，没有邪念或杂质，多用来形容品德或风气。",
            "example": "童年时代的友谊往往最为纯正无邪。"
        },
        1951: {
            "pinyin": "chún bù lí sāi",
            "meaning": "嘴唇不离脸颊，比喻说话不停，也形容关系十分亲近。",
            "example": "他一天到晚唇不离腮地絮叨个不停。"
        },
        1952: {
            "pinyin": "chún chǐ xiāng yī",
            "meaning": "嘴唇和牙齿互相依存，比喻关系密切、互相依赖。",
            "example": "两国历来唇齿相依，休戚与共。"
        },
        1953: {
            "pinyin": "chún chǐ zhī bāng",
            "meaning": "比喻彼此接近、互相依存的邻邦。",
            "example": "面对共同挑战，这两个唇齿之邦更应携手合作。"
        },
        1954: {
            "pinyin": "chún gān kǒu zào",
            "meaning": "嘴唇干裂、口中燥热，形容说话太多或极度焦急。",
            "example": "他为这件事四处奔走，劝说得唇干口燥。"
        },
        1955: {
            "pinyin": "chún hóng chǐ bái",
            "meaning": "嘴唇红润、牙齿洁白，形容容貌俊美。",
            "example": "那孩子唇红齿白，一看就很讨人喜欢。"
        },
        1956: {
            "pinyin": "chún jiāo shé bì",
            "meaning": "嘴唇焦干、舌头磨破，形容费尽口舌地劝说或辩论。",
            "example": "大家为这项改革唇焦舌敝，终于取得一致意见。"
        },
        1957: {
            "pinyin": "chún qiāng shé jiàn",
            "meaning": "嘴如枪、舌如剑，形容言辞锋利、争辩激烈。",
            "example": "两位辩手在台上唇枪舌剑，场面十分精彩。"
        },
        1958: {
            "pinyin": "chún wáng chǐ hán",
            "meaning": "嘴唇没有了，牙齿就会感到寒冷，比喻双方关系密切，一方遭难另一方也难以独善其身。",
            "example": "在区域合作中，各国早已是唇亡齿寒的命运共同体。"
        },
        1959: {
            "pinyin": "chún gēng lú kuài",
            "meaning": "莼菜羹和鲈鱼脍，比喻家乡的美味佳肴，引申为对故乡的怀念。",
            "example": "远在他乡，每逢佳节便倍增莼羹鲈脍之思。"
        },
        1960: {
            "pinyin": "chún lú zhī sī",
            "meaning": "指对故乡的思念之情，典出张翰思乡的故事。",
            "example": "游子客居海外，常有莼鲈之思。"
        },
        1961: {
            "pinyin": "chǔn chǔn yù dòng",
            "meaning": "像虫子蠕动般隐隐活动，形容暗中活动、准备行动。多含贬义。",
            "example": "一些不法分子在蠢蠢欲动，必须提前防范。"
        },
        1962: {
            "pinyin": "chuō jué zhī néng",
            "meaning": "踔绝：超绝。指超群出众的才能。",
            "example": "他在书法上的踔绝之能有目共睹。"
        },
        1963: {
            "pinyin": "chuō lì fēng fā",
            "meaning": "精神奋发，气概昂扬，形容斗志高昂、意气风发的样子。",
            "example": "青年人应当踔厉风发，勇于担当时代重任。"
        },
        1964: {
            "pinyin": "chuò shí tǔ bǔ",
            "meaning": "一边吃饭一边吐下口中的食物去接待宾客，形容忙于延揽贤才。",
            "example": "古代明君往往啜食吐哺，以礼相待贤士。"
        },
        1965: {
            "pinyin": "chuò shū yǐn shuǐ",
            "meaning": "吃豆子、喝清水，比喻生活清贫而能安之若素。",
            "example": "他们啜菽饮水，却始终保持读书人的气节。"
        },
        1966: {
            "pinyin": "chuò dá shāng cuì",
            "meaning": "惙怛：忧伤；伤悴：憔悴。形容极度忧愁悲伤、形容枯槁。",
            "example": "听闻噩耗，她不由惙怛伤悴、茶饭不思。"
        },
        1967: {
            "pinyin": "chuò chuò yǒu yú",
            "meaning": "形容数量、力量等非常充足，绰绰有余。",
            "example": "以他的实力，完成这点任务绰绰有余。"
        },
        1968: {
            "pinyin": "chuò yǒu yú yù",
            "meaning": "绰绰：宽裕；余裕：富余的空间或时间。形容从容不迫，十分宽裕。",
            "example": "面对突发状况，他仍显得绰有余裕。"
        },
        1969: {
            "pinyin": "chuò yuē duō zī",
            "meaning": "形容女子体态轻盈、风姿绰约。",
            "example": "古画中的仕女个个绰约多姿、顾盼生辉。"
        },
        1970: {
            "pinyin": "cí bēi wéi běn",
            "meaning": "以慈悲为根本出发点，多用于佛教语境，也泛指待人以仁爱为本。",
            "example": "这家慈善机构始终秉持慈悲为本的理念。"
        },
        1971: {
            "pinyin": "cí méi shàn mù",
            "meaning": "眉目和善，形容人的容貌慈祥可亲。",
            "example": "她一脸慈眉善目，很容易让人放下戒心。"
        },
        1972: {
            "pinyin": "cí míng wú shuāng",
            "meaning": "慈：仁慈；明：聪明。形容仁慈而聪明的品德举世无双。",
            "example": "史书称其为慈明无双的贤君。"
        },
        1973: {
            "pinyin": "cí wū fǎn bǔ",
            "meaning": "慈乌反哺，指乌鸦长大后反哺老母，比喻子女报答父母养育之恩。",
            "example": "孝顺父母，本是慈乌返哺般的天性。"
        },
        1974: {
            "pinyin": "cí bù dá yì",
            "meaning": "言辞不能充分表达思想感情，形容表达能力不足。",
            "example": "这份感激之情，真是辞不达意。"
        },
        1975: {
            "pinyin": "cí duō shòu shǎo",
            "meaning": "言辞多而所受甚少，形容花言巧语很多，真正给予的很少。",
            "example": "有的承诺不过是辞多受少的空话。"
        },
        1976: {
            "pinyin": "cí fù jū pín",
            "meaning": "言辞华丽却仍然贫困，形容空有文采而无实际成就。",
            "example": "若只会卖弄文采而不脚踏实地，终究不过辞富居贫。"
        },
        1977: {
            "pinyin": "cí yán yì zhèng",
            "meaning": "言辞严正有力，理由充足正当。",
            "example": "他在会上对歪风邪气进行了辞严义正的批评。"
        },
        1978: {
            "pinyin": "cí zūn jū bēi",
            "meaning": "自称时使用卑下的名分，表示谦逊。",
            "example": "古人写信多用辞尊居卑，以示自谦。"
        },
        1979: {
            "pinyin": "cí bù dǎi lǐ",
            "meaning": "言辞不能完全表达道理，形容辩说能力有限或理屈词穷。",
            "example": "面对对方有力的论证，他只觉词不逮理。"
        },
        1980: {
            "pinyin": "cí dùn yì xū",
            "meaning": "言辞迟钝、意思空虚，形容说话没有内容、缺乏说服力。",
            "example": "空洞的口号往往词钝意虚，难以打动人心。"
        },
        1981: {
            "pinyin": "cí qióng lǐ jí",
            "meaning": "话已经说尽、道理已经讲透，多用来表示再无可说。",
            "example": "此事利弊已分析到词穷理极，就看你如何选择了。"
        },
        1982: {
            "pinyin": "cí xióng wèi jué",
            "meaning": "胜负尚未决定，比喻事情的结果还难以预料。",
            "example": "比赛刚到中场，双方雌雄未决。"
        },
        1983: {
            "pinyin": "cǐ chàng bǐ hè",
            "meaning": "这一方唱，那一方和，比喻互相呼应，多含附和、迎合之意。",
            "example": "会议上一片此唱彼和的赞成声，缺少冷静思考。"
        },
        1984: {
            "pinyin": "cǐ dì wú yín sān bǎi liǎng",
            "meaning": "本想掩饰反而暴露，形容欲盖弥彰、自作聪明反而出丑。",
            "example": "他越是否认越像此地无银三百两。"
        },
        1985: {
            "pinyin": "cǐ fú bǐ qǐ",
            "meaning": "这儿伏下，那儿又起来，形容事物此消彼长、交替出现。",
            "example": "各种流行语此伏彼起，更新速度飞快。"
        },
        1986: {
            "pinyin": "cǐ hèn mián mián",
            "meaning": "这份怨恨或遗憾绵延不绝。",
            "example": "他叹道：‘此恨绵绵无绝期。’"
        },
        1987: {
            "pinyin": "cǐ qǐ bǐ fú",
            "meaning": "这里起来，那里落下，形容接连不断、此消彼长的情形。",
            "example": "山谷中犬吠声此起彼伏。"
        },
        1988: {
            "pinyin": "cǐ qǐ bǐ luò",
            "meaning": "这里响起、那里停落，形容声音交替不断。",
            "example": "乐声在大厅内此起彼落，气氛热烈。"
        },
        1989: {
            "pinyin": "cǐ yī shí, bǐ yī shí",
            "meaning": "这个时候和那个时候情况不同，比喻环境、条件变了，应作不同看待。",
            "example": "如今形势早已不同，当年之事此一时，彼一时。"
        },
        1990: {
            "pinyin": "cǐ zhōng sān mèi",
            "meaning": "三昧：要旨、奥妙。指其中的要领或精要之处。",
            "example": "多做几次，你自会体会此中三昧。"
        },
        1991: {
            "pinyin": "cì cì bù xiū",
            "meaning": "形容说话絮絮叨叨、喋喋不休，多带贬义。",
            "example": "他对别人的小错总是刺刺不休。"
        },
        1992: {
            "pinyin": "cì gǔ dú shū",
            "meaning": "用锥子刺大腿以免打瞌睡，形容刻苦读书。",
            "example": "古人刺股读书的精神值得后人学习。"
        },
        1993: {
            "pinyin": "cì gǔ xuán liáng",
            "meaning": "刺大腿、悬头于梁，比喻刻苦学习、自我鞭策。",
            "example": "少年时他以刺股悬梁自励，终成一代学者。"
        },
        1994: {
            "pinyin": "cì qiáng jí jiān",
            "meaning": "赐给人的围墙只到肩膀高，比喻表面施惠、实则无用。",
            "example": "这种对基层的‘支持’不过是赐墙及肩，难解实际困难。"
        },
        1995: {
            "pinyin": "cóng róng bù pò",
            "meaning": "神情镇定，从容不慌。",
            "example": "面对质疑，他从容不迫，逐条回应。"
        },
        1996: {
            "pinyin": "cóng róng jiù yì",
            "meaning": "态度镇静地走向就义之路，形容为正义事业献身时的无畏气概。",
            "example": "革命先烈从容就义的身影永远令人敬仰。"
        },
        1997: {
            "pinyin": "cóng cháng jì yì",
            "meaning": "从长远打算，慢慢商量，形容不急于作出决定。",
            "example": "这件事关系重大，还是从长计议为好。"
        },
        1998: {
            "pinyin": "cóng è shì bēng",
            "meaning": "顺从邪恶就会像山崩一样迅速毁灭，形容走上邪路极易堕落。",
            "example": "古人告诫我们从善如登，从恶是崩。"
        },
        1999: {
            "pinyin": "cóng jiàn rú liú",
            "meaning": "把别人的劝谏当作流水一样顺势接纳，形容虚心纳谏。",
            "example": "明君多能从谏如流，广开言路。"
        },
        2000: {
            "pinyin": "cóng jǐng jiù rén",
            "meaning": "跳入井中去救人，比喻不顾自身安危去解救别人。",
            "example": "消防员们义无反顾，从井救人，令人敬佩。"
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

    print(f"已为 1901–2000 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
