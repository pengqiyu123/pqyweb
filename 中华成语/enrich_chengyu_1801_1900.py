import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    enrich = {
        1801: {
            "pinyin": "chū shuǐ fú róng",
            "meaning": "芙蓉：荷花。刚露出水面的荷花。比喻诗文清新不俗，也形容女子容貌清秀艳丽。",
            "example": "她一身素衣立在湖畔，真有出水芙蓉之姿。"
        },
        1802: {
            "pinyin": "chū tóu lù miàn",
            "meaning": "在公众场合露出头脸，比喻公开出面或显露身份。",
            "example": "这种事不用你出头露面，我去协调就行了。"
        },
        1803: {
            "pinyin": "chū tóu zhī rì",
            "meaning": "出头：摆脱困境。指从压抑、困厄的处境中摆脱出来的日子。",
            "example": "他始终相信，总有一天会有自己出头之日。"
        },
        1804: {
            "pinyin": "chū yán bù xùn",
            "meaning": "逊：谦逊、有礼。形容说话粗暴无礼，不知收敛。",
            "example": "说话要有分寸，切莫随便出言不逊。"
        },
        1805: {
            "pinyin": "chū yán chéng zhāng",
            "meaning": "说出的话就像成篇文章一样有条理、有文采，形容才思敏捷、口才好。",
            "example": "他从小博览群书，讲话常常出言成章。"
        },
        1806: {
            "pinyin": "chū yán wú zhuàng",
            "meaning": "说话放肆、没有礼貌。",
            "example": "他年轻气盛，难免有时出言无状。"
        },
        1807: {
            "pinyin": "chū yán yǒu zhāng",
            "meaning": "说话有条理、有法度。",
            "example": "这位发言人出言有章，态度沉稳。"
        },
        1808: {
            "pinyin": "chū yǐ gōng xīn",
            "meaning": "指考虑问题、处理事务以公共利益为出发点，不徇私情。",
            "example": "只要大家出以公心，很多矛盾都能化解。"
        },
        1809: {
            "pinyin": "chú bào ān liáng",
            "meaning": "铲除强暴势力，安抚善良的人民。",
            "example": "他立志从警，希望能为民除暴安良。"
        },
        1810: {
            "pinyin": "chú cán qù huì",
            "meaning": "残：残暴；秽：污秽，比喻恶势力。清除残暴腐朽的势力或不良风气。",
            "example": "只有坚决除残去秽，社会风气才能日渐清明。"
        },
        1811: {
            "pinyin": "chú è wù jìn",
            "meaning": "务：务求、一定要。铲除邪恶势力必须彻底，不留祸根。",
            "example": "打击黑恶势力要除恶务尽，不能心慈手软。"
        },
        1812: {
            "pinyin": "chú jiān gé bì",
            "meaning": "革：革除；弊：弊端。铲除奸邪之徒，革除各种弊端。",
            "example": "新一轮改革重在除奸革弊、重塑风气。"
        },
        1813: {
            "pinyin": "chú jiù bù xīn",
            "meaning": "除去旧事物，布置新的事物，形容推陈出新、改革更新。",
            "example": "制度建设要除旧布新，不能一味因循守旧。"
        },
        1814: {
            "pinyin": "chú jiù gēng xīn",
            "meaning": "去除旧的，更新为新的，多指改朝换代或制度、观念的更新。",
            "example": "社会转型期往往伴随着除旧更新的阵痛。"
        },
        1815: {
            "pinyin": "chú xié chéng è",
            "meaning": "惩：惩治。铲除邪气恶行，并加以惩治。",
            "example": "司法机关肩负着除邪惩恶、匡扶正义的责任。"
        },
        1816: {
            "pinyin": "chú qiáng fú ruò",
            "meaning": "锄：铲除；强：强暴者；扶：扶助。铲除强暴，扶助弱小。",
            "example": "他笔下的英雄多是行侠仗义、锄强扶弱之士。"
        },
        1817: {
            "pinyin": "chú ráo zhī jiàn",
            "meaning": "刍荛：割草砍柴的人，比喻平民百姓。指普通人的肤浅见解，多作自谦之辞。",
            "example": "我不过刍荛之见，尚望诸公不吝指教。"
        },
        1818: {
            "pinyin": "chǔ cái jìn yòng",
            "meaning": "楚国的人才被晋国任用，比喻人才不为本国或原来的单位所用，却被别处重用。",
            "example": "如果轻易放走这位骨干，难免将来楚材晋用。"
        },
        1819: {
            "pinyin": "chǔ chǔ kě lián",
            "meaning": "形容姿态娇弱可爱，也形容境遇凄楚、令人怜惜。",
            "example": "雨中的小女孩楚楚可怜，让人心生怜惜。"
        },
        1820: {
            "pinyin": "chǔ gōng chǔ dé",
            "meaning": "弓是楚国的，拾得者也是楚人，比喻本国的损失由本国自己补偿，得失相抵。",
            "example": "内部资源调剂，不过是楚弓楚得而已。"
        },
        1821: {
            "pinyin": "chǔ guān qín lóu",
            "meaning": "原指楚地的棺木、秦地的歌楼，后多泛指歌舞场所、妓院之类的欢场。",
            "example": "他年轻时流连楚棺秦楼，虚掷了大好年华。"
        },
        1822: {
            "pinyin": "chǔ jiè hàn hé",
            "meaning": "楚地与汉地以河为界，后多用来泛指两国或两地之间的分界。",
            "example": "两军隔河对峙，各守楚界汉河之线。"
        },
        1823: {
            "pinyin": "chǔ mèng yún yǔ",
            "meaning": "本指楚襄王梦神女于巫山的故事，后多用以指男女间云雨之情或虚幻的情缘。",
            "example": "那些楚梦云雨不过过眼云烟，不足为凭。"
        },
        1824: {
            "pinyin": "chǔ qiú duì qì",
            "meaning": "原指战国时楚国战俘相对而哭的典故，比喻同遭困境的人相对悲泣。",
            "example": "失业工人聚在一起，难免有楚囚对泣之叹。"
        },
        1825: {
            "pinyin": "chǔ wěi wú tóu",
            "meaning": "古豫章一带在楚地下游、吴地上游，如首尾相接，后用以泛指长江中下游一带地区。",
            "example": "他多年奔走于楚尾吴头之间，经商闯荡。"
        },
        1826: {
            "pinyin": "chǔ yāo xiān xì",
            "meaning": "形容女子腰身柔细、体态轻盈。",
            "example": "古画中的仕女个个楚腰纤细、衣袂飘飘。"
        },
        1827: {
            "pinyin": "chǔ jiù zhī jiāo",
            "meaning": "杵臼：舂米的木杵和石臼。比喻平民百姓之间的交情，形容友谊质朴深厚。",
            "example": "他们虽是杵臼之交，却能生死相托。"
        },
        1828: {
            "pinyin": "chǔ rùn ér yǔ",
            "meaning": "础：柱子下的石基。基石潮湿预示将要下雨，比喻从细微征兆可以预料事物的发展。",
            "example": "市场上的种种变化，正是础润而雨的先兆。"
        },
        1829: {
            "pinyin": "chǔ gāo lín shēn",
            "meaning": "处在高处、临近深渊，比喻境地极其险恶。",
            "example": "公司资金链紧张，如今已是处高临深，不可不慎。"
        },
        1830: {
            "pinyin": "chǔ táng yàn què",
            "meaning": "堂上本应是人君、贤士，竟栖息着燕雀，比喻地位不称或小人盘踞高位。",
            "example": "若任用庸人掌权，无异于处堂燕雀。"
        },
        1831: {
            "pinyin": "chǔ xīn jī lǜ",
            "meaning": "指长时间地处处用心、积蓄谋划，多用于形容别有用心或阴谋算计。",
            "example": "他早已处心积虑，策划这场收购。"
        },
        1832: {
            "pinyin": "chǔ zhī tài rán",
            "meaning": "指面对复杂情况时神情安然自若，毫不慌张。",
            "example": "面对突发状况，他仍能处之泰然、从容应对。"
        },
        1833: {
            "pinyin": "chù mù jīng xīn",
            "meaning": "看见某种景象而内心震惊不安，多形容场面惨烈或情况严重。",
            "example": "灾区一片废墟，真是怵目惊心。"
        },
        1834: {
            "pinyin": "chù jī biàn fā",
            "meaning": "机：弓弩上的发箭器。原指一触机制便会发射，比喻一有机会就立刻发动或爆发。",
            "example": "在这种触机便发的局势下，更要谨言慎行。"
        },
        1835: {
            "pinyin": "chù jǐng shēng qíng",
            "meaning": "因看到某种景物而触动感情，联想到往事。",
            "example": "故乡的老树总让他触景生情，想起童年时光。"
        },
        1836: {
            "pinyin": "chù lèi páng tōng",
            "meaning": "触类：由一类事物推及同类；旁通：旁及他物。指掌握了一类事物的规律后，就能推知同类事物的道理。",
            "example": "学习要善于触类旁通，而不能死记硬背。"
        },
        1837: {
            "pinyin": "chù mù jiē shì",
            "meaning": "目光所及之处到处都是某种景象。",
            "example": "昔日荒山，如今绿树成荫，触目皆是生机。"
        },
        1838: {
            "pinyin": "chù mù jīng xīn",
            "meaning": "所见情景使人内心震惊、多为惨烈、恐怖的场面。",
            "example": "事故现场惨不忍睹，真叫人触目惊心。"
        },
        1839: {
            "pinyin": "chù mù rú gù",
            "meaning": "所见到的一切仍和从前一样，毫无变化。",
            "example": "多年后重回母校，礼堂操场依旧，触目如故。"
        },
        1840: {
            "pinyin": "chù mù tòng xīn",
            "meaning": "恸：极度悲伤。看到眼前景象而引起内心强烈悲痛。",
            "example": "看到河道被严重污染，他不禁触目恸心。"
        },
        1841: {
            "pinyin": "chù mù xīng tàn",
            "meaning": "因眼前景象而感慨叹息，多形容局面凄凉、破败。",
            "example": "这座曾经繁华的古城，如今让人触目兴叹。"
        },
        1842: {
            "pinyin": "chù wù xīng huái",
            "meaning": "受到眼前事物的触动而引发某种情感或联想。",
            "example": "他常在黄昏散步，触物兴怀，思绪万千。"
        },
        1843: {
            "pinyin": "chuǎi hé féng yíng",
            "meaning": "揣：揣测。指揣摩、迎合他人特别是权贵的心意以谋求私利。",
            "example": "真正的读书人不屑于揣合逢迎、阿谀奉承。"
        },
        1844: {
            "pinyin": "chuān liú bù xī",
            "meaning": "像河水那样不断地流动，形容行人、车马等往来不绝或事物持续不断。",
            "example": "假日期间，景区游客川流不息。"
        },
        1845: {
            "pinyin": "chuān yōng bì kuì",
            "meaning": "壅：堵塞；溃：决口。堵塞河道必然会决堤，比喻办事要因势利导，否则会酿成大祸。",
            "example": "若一味压制舆论，终有川壅必溃之虞。"
        },
        1846: {
            "pinyin": "chuān bì yǐn guāng",
            "meaning": "穿：凿通；引：引进。凿通墙壁引进邻家灯光读书，比喻家贫而勤学不辍。",
            "example": "匡衡穿壁引光的故事，激励了无数寒门子弟。"
        },
        1847: {
            "pinyin": "chuān fáng rù hù",
            "meaning": "穿：穿过。穿房越屋、闯入人家，比喻行为猥琐、偷偷摸摸地出入。",
            "example": "这些小偷专门在夜间穿房入户行窃。"
        },
        1848: {
            "pinyin": "chuān jǐng dé rén",
            "meaning": "穿井：凿井。本指凿井时意外得到人才，后比喻因事得人或意外收获。",
            "example": "这次招聘原只想补一个岗位，没想到却穿井得人。"
        },
        1849: {
            "pinyin": "chuān yú zhī dào",
            "meaning": "穿窬：攀墙钻洞。指翻墙越户、出入人家行窃的小偷。",
            "example": "古时法律对穿窬之盗多有严厉处罚。"
        },
        1850: {
            "pinyin": "chuān yún liè shí",
            "meaning": "歌曲或声音高亢嘹亮，有如穿云裂石；也形容声势非常宏大。",
            "example": "将军一声怒吼，犹如穿云裂石，震撼全军。"
        },
        1851: {
            "pinyin": "chuān zhēn yǐn xiàn",
            "meaning": "穿针引线，比喻从中牵线搭桥、介绍撮合。",
            "example": "这桩合作多亏他在中间穿针引线。"
        },
        1852: {
            "pinyin": "chuān záo fù huì",
            "meaning": "穿凿：牵强解释；附会：勉强拉到一起。指生拉硬扯、牵强附会地解释或联系。",
            "example": "做学问贵在求实，不可穿凿附会。"
        },
        1853: {
            "pinyin": "chuán dào shòu yè",
            "meaning": "语出韩愈《师说》，指教师传授道理、教授学业。",
            "example": "三尺讲台之上，老师辛勤传道受业。"
        },
        1854: {
            "pinyin": "chuán shén ā dǔ",
            "meaning": "阿堵，指钱。形容刻画或描写人物形象极其传神生动。",
            "example": "这幅仕女画可谓传神阿堵，栩栩如生。"
        },
        1855: {
            "pinyin": "chuán sòng yī shí",
            "meaning": "在一段时间内到处传诵、广为称道。",
            "example": "他的那篇演讲曾传诵一时。"
        },
        1856: {
            "pinyin": "chuán wéi xiào bǐng",
            "meaning": "被人当作笑料来谈论。",
            "example": "这种粗心的错误足以传为笑柄。"
        },
        1857: {
            "pinyin": "chuán wén yì cí",
            "meaning": "传闻：传言、流言；异辞：不同的说法。指关于某事的传闻说法互相矛盾。",
            "example": "此事传闻异辞，真假难辨。"
        },
        1858: {
            "pinyin": "chuán xí ér dìng",
            "meaning": "檄：檄文。指向各处发出檄文，敌方或地方势力即行归附平定。",
            "example": "当年他声望极高，几乎传檄而定一方局势。"
        },
        1859: {
            "pinyin": "chuán zōng jiē dài",
            "meaning": "传续宗族血脉、使后代不断。",
            "example": "在传统观念里，传宗接代是天经地义的事。"
        },
        1860: {
            "pinyin": "chuán dào jiāng xīn bǔ lòu chí",
            "meaning": "比喻事情发展到紧要关头才想办法挽救，为时已晚。",
            "example": "安全隐患不能等到船到江心补漏迟时才重视。"
        },
        1861: {
            "pinyin": "chuán duō bù ài lù",
            "meaning": "船只虽多，却并不妨碍通行，比喻事情繁多而不相冲突。",
            "example": "合理安排时间，做多件事也可船多不碍路。"
        },
        1862: {
            "pinyin": "chuǎn é bǎi chū",
            "meaning": "舛讹：错误。形容错误非常多。",
            "example": "这份资料舛讹百出，必须重新整理。"
        },
        1863: {
            "pinyin": "chuǎn xī zhī jiān",
            "meaning": "喘气的片刻之间，比喻时间极为短暂。",
            "example": "他在喘息之间便做出了决定。"
        },
        1864: {
            "pinyin": "chuàn qīn fǎng yǒu",
            "meaning": "挨家挨户地走亲戚、访朋友。",
            "example": "春节期间大家忙着串亲访友，联络感情。"
        },
        1865: {
            "pinyin": "chuàn tōng yī qì",
            "meaning": "形容相互勾结、沆瀣一气。",
            "example": "那些人串通一气，企图操纵市场。"
        },
        1866: {
            "pinyin": "chuāng jù tòng shēn",
            "meaning": "创：创伤。伤口很重、痛楚很深，比喻遭受的打击极大。",
            "example": "这场战争给当地人民带来了创巨痛深的灾难。"
        },
        1867: {
            "pinyin": "chuāng yí mǎn mù",
            "meaning": "疮痍：创伤。放眼望去到处都是创伤，比喻经受战乱或灾荒后的惨状。",
            "example": "多年的冲突后，这片土地疮痍满目。"
        },
        1868: {
            "pinyin": "chuāng míng jī jìng",
            "meaning": "几：小桌。形容室内窗明几净、整洁明亮。",
            "example": "她把房间收拾得窗明几净、井井有条。"
        },
        1869: {
            "pinyin": "chuáng xià niú dòu",
            "meaning": "听到床下微小的声音，却误以为牛在争斗，形容体衰耳聪、神经过敏。",
            "example": "老人夜里一点动静都觉床下牛斗，大家只好轻手轻脚。"
        },
        1870: {
            "pinyin": "chuáng zǐ zhī sī",
            "meaning": "床笫：床铺。指夫妻之间的隐私之事。",
            "example": "这些乃人家床笫之私，不宜对外宣扬。"
        },
        1871: {
            "pinyin": "chuáng shàng ān chuáng",
            "meaning": "比喻多此一举、重复无谓的事情。",
            "example": "此举无异于床上安床，既费力又无益。"
        },
        1872: {
            "pinyin": "chuáng tóu jīn jìn",
            "meaning": "床头的钱财花光了，比喻经济拮据、入不敷出。",
            "example": "生意连年亏损，早已是床头金尽。"
        },
        1873: {
            "pinyin": "chuǎng dàng jiāng hú",
            "meaning": "在社会上四处闯荡谋生，多指在江湖间行走。",
            "example": "他年轻时独自闯荡江湖，见过不少世面。"
        },
        1874: {
            "pinyin": "chuàng yè chuí tǒng",
            "meaning": "创业并把基业传给后代。",
            "example": "先辈们创业垂统，才有家族今天的规模。"
        },
        1875: {
            "pinyin": "chuàng yè wéi jiān",
            "meaning": "创建事业非常不易、过程艰难。",
            "example": "他深知创业维艰，对公司基础建设格外重视。"
        },
        1876: {
            "pinyin": "chuàng dì hū tiān",
            "meaning": "悲伤到极点，对着大地呼号、向上天呼喊。形容极度哀痛。",
            "example": "亲人离世，他不禁怆地呼天。"
        },
        1877: {
            "pinyin": "chuī jīn zhuàn yù",
            "meaning": "炊：做饭；馔：饭食。形容饮食极其奢侈丰盛。",
            "example": "昔日王侯炊金馔玉，如今也提倡节俭。"
        },
        1878: {
            "pinyin": "chuī shā chéng fàn",
            "meaning": "用沙子煮成饭，比喻条件根本不具备却勉强去做，必然不会成功。",
            "example": "没有前期调研就贸然上马项目，无异于炊沙成饭。"
        },
        1879: {
            "pinyin": "chuī chún chàng hǒu",
            "meaning": "形容喧嚷吆喝、大声叫喊的样子。",
            "example": "集市上小贩们吹唇唱吼，招徕顾客。"
        },
        1880: {
            "pinyin": "chuī dà fǎ luó",
            "meaning": "比喻大肆宣扬、极力鼓吹。",
            "example": "广告把这款产品吹大法螺，说得近乎完美。"
        },
        1881: {
            "pinyin": "chuī jiǎo lián yíng",
            "meaning": "军营里号角相继吹响，形容军容严整或战事紧张。",
            "example": "黄昏时分，山谷中吹角连营，杀声震天。"
        },
        1882: {
            "pinyin": "chuī kāng jiàn mǐ",
            "meaning": "把谷粒吹去皮糠即可见到白米，比喻事情非常明显、一看便知。",
            "example": "账目是否清楚，一查便是，犹如吹糠见米。"
        },
        1883: {
            "pinyin": "chuī huī zhī lì",
            "meaning": "像吹一吹灰尘那样轻而易举的力量，比喻事情极易办到。",
            "example": "对他来说，这点任务不过是吹灰之力。"
        },
        1884: {
            "pinyin": "chuī máo lì rèn",
            "meaning": "吹毛使之挺立于利刃之上，比喻十分锋利，也指过于苛刻地挑毛病。",
            "example": "这份合同的条款几乎到吹毛利刃的程度。"
        },
        1885: {
            "pinyin": "chuī máo qiú cī",
            "meaning": "吹起毫毛来寻找细小的瑕疵，比喻过分挑剔、苛求。",
            "example": "与其吹毛求疵，不如多给些建设性的意见。"
        },
        1886: {
            "pinyin": "chuī qì shèng lán",
            "meaning": "气息芬芳胜过兰花，比喻女子吐气如兰，谈吐文雅。",
            "example": "她说话轻声细语，真有吹气胜兰之感。"
        },
        1887: {
            "pinyin": "chuī tán dé pò",
            "meaning": "形容事物脆弱不堪，一吹一弹就会破裂。",
            "example": "如此脆弱的友谊，简直吹弹得破。"
        },
        1888: {
            "pinyin": "chuī tán gē wǔ",
            "meaning": "边奏乐器边歌舞，形容歌舞升平、场面热闹。",
            "example": "殿内吹弹歌舞，一派盛世气象。"
        },
        1889: {
            "pinyin": "chuī xiāo qǐ shí",
            "meaning": "以吹箫卖艺乞讨糊口，形容生活贫困、以技求食。",
            "example": "他年轻时曾在街头吹箫乞食，备尝艰辛。"
        },
        1890: {
            "pinyin": "chuī yǐng lòu chén",
            "meaning": "吹影子、雕尘土，比喻技艺或工夫精细入微，几乎不可察觉。",
            "example": "这位雕刻大师的手艺简直到了吹影镂尘的境界。"
        },
        1891: {
            "pinyin": "chuī zhòu yī chí chūn shuǐ",
            "meaning": "形容稍加挑拨就引起一番波澜，多用来形容感情或局势的微妙。",
            "example": "他随口一句玩笑，竟吹皱一池春水。"
        },
        1892: {
            "pinyin": "zhuī niú xiǎng shì",
            "meaning": "杀牛置酒款待士卒，形容犒赏士兵或宾客盛情。",
            "example": "主公椎牛飨士，以谢将士之功。"
        },
        1893: {
            "pinyin": "zhuī xīn qì xuè",
            "meaning": "悲痛到极点，如同心被捶击、泪尽而出血，形容极度悲伤。",
            "example": "噩耗传来，家属无不椎心泣血。"
        },
        1894: {
            "pinyin": "chuí fàn bǎi shì",
            "meaning": "垂：流传；范：榜样。指留下可以作为典范的事迹，流传后世。",
            "example": "他的高风亮节足以垂范百世。"
        },
        1895: {
            "pinyin": "chuí gǒng ér zhì",
            "meaning": "垂衣拱手而天下自安，形容统治者无为而治、政局安定。",
            "example": "国政清明，君主得以垂拱而治。"
        },
        1896: {
            "pinyin": "chuí lián tīng zhèng",
            "meaning": "垂帘而坐、听群臣奏事，多指皇太后、皇后临朝处理政务。",
            "example": "她一度垂帘听政，左右朝局十余年。"
        },
        1897: {
            "pinyin": "chuí míng qīng shǐ",
            "meaning": "留下好名声在史册上，形容功业或品德为后世所称道。",
            "example": "为官一任，造福一方，方能垂名青史。"
        },
        1898: {
            "pinyin": "chuí mù zhī nián",
            "meaning": "指临近老年或人生晚年阶段。",
            "example": "他在垂暮之年仍笔耕不辍。"
        },
        1899: {
            "pinyin": "chuí shǒu ér dé",
            "meaning": "垂下双手就能得到，比喻事情极易成功或东西容易取得。",
            "example": "只要稍加努力，这个小目标简直垂手而得。"
        },
        1900: {
            "pinyin": "chuí shǒu kě dé",
            "meaning": "轻而易举就可以得到。",
            "example": "过去难以想象的生活，如今已是垂手可得。"
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

    print(f"已为 1801–1900 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
