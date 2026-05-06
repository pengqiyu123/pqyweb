import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    enrich = {
        2801: {
            "pinyin": "dīng shì dīng, mǎo shì mǎo",
            "meaning": "比喻界限分明、态度认真，一丝不苟，不能含糊混淆。",
            "example": "在账目问题上，他向来是丁是丁，卯是卯，从不马虎。"
        },
        2802: {
            "pinyin": "dīng yī mǎo èr",
            "meaning": "比喻条理分明、分得很清楚，也形容办事认真谨慎。",
            "example": "文件分类要做到丁一卯二，方便日后查找。"
        },
        2803: {
            "pinyin": "dīng yī què èr",
            "meaning": "犹言丁一卯二，形容分辨清楚、不含糊。",
            "example": "合同条款必须写得丁一确二，避免产生歧义。"
        },
        2804: {
            "pinyin": "dīng shì dīng, mǎo shì mǎo",
            "meaning": "形容说话、办事极其认真，一点也不含糊。",
            "example": "他做项目向来是钉是钉，铆是铆，团队都很放心。"
        },
        2805: {
            "pinyin": "dīng zuǐ tiě shé",
            "meaning": "形容说话尖刻、舌头厉害。",
            "example": "她一张钉嘴铁舌，说起人来毫不留情。"
        },
        2806: {
            "pinyin": "dǐng lǐ mó bài",
            "meaning": "原指佛教最隆重的礼拜仪式，后泛指十分崇敬、膜拜。",
            "example": "粉丝们对偶像顶礼膜拜，几乎到了疯狂的程度。"
        },
        2807: {
            "pinyin": "dǐng tiān lì dì",
            "meaning": "形容形象高大，气概雄伟，也形容人格坚强正直。",
            "example": "在灾难面前，总有人顶天立地地站出来。"
        },
        2808: {
            "pinyin": "dǐng zhēn xù má",
            "meaning": "用顶针接续麻线，比喻继续前人的事业，环环相接、不断前进。",
            "example": "几代科学家顶针续麻，才有今天的成就。"
        },
        2809: {
            "pinyin": "dǐng chēng yǒu ěr",
            "meaning": "鼎和铛都有耳，比喻某事影响很大，几乎人人皆知。",
            "example": "这件丑闻早已鼎铛有耳，他还想瞒得住吗？"
        },
        2810: {
            "pinyin": "dǐng chēng yù shí",
            "meaning": "视宝鼎如炊具，视美玉如顽石，形容生活极端奢侈、挥霍无度。",
            "example": "宫中鼎铛玉石，金块珠砾，奢华到了极点。"
        },
        2811: {
            "pinyin": "dǐng dǐng dà míng",
            "meaning": "形容名气很大，人人都知道。",
            "example": "他是业界鼎鼎大名的专家。"
        },
        2812: {
            "pinyin": "dǐng huò dāo jù",
            "meaning": "鼎镬、刀锯都是古代酷刑用具，比喻极其严酷的刑罚或环境。",
            "example": "为了理想，就算是鼎镬刀锯他也毫不畏惧。"
        },
        2813: {
            "pinyin": "dǐng huò rú yí",
            "meaning": "把严刑看得像糖一样，形容视死如归、毫不畏惧。",
            "example": "为了真理，先贤们把鼎镬如饴，宁死不屈。"
        },
        2814: {
            "pinyin": "dǐng xīn gé gù",
            "meaning": "革除旧的，创立新的，多指政治、制度等方面的改革。",
            "example": "这次改革旨在鼎新革故，解决多年积累的问题。"
        },
        2815: {
            "pinyin": "dǐng yú mù yàn",
            "meaning": "宛如鼎中游鱼、幕上燕巢，比喻处境极其危险，随时可能灭亡。",
            "example": "敌军四面合围，他们已是鼎鱼幕燕。"
        },
        2816: {
            "pinyin": "dǐng zú ér sān",
            "meaning": "三足鼎立，比喻三方面对峙而又相互制衡的局面。",
            "example": "经过几番争夺，市场上形成了鼎足而三的格局。"
        },
        2817: {
            "pinyin": "dǐng zú sān fēn",
            "meaning": "同“鼎足而三”，比喻三方分立、势均力敌。",
            "example": "各大公司鼎足三分，竞争十分激烈。"
        },
        2818: {
            "pinyin": "dǐng zú zhī shì",
            "meaning": "像鼎的三足那样分立的形势，比喻三方分立互相牵制的局面。",
            "example": "一旦形成鼎足之势，再想独占就难了。"
        },
        2819: {
            "pinyin": "dìng guó ān bāng",
            "meaning": "使国家安定、邦国太平，多形容安定天下的大功绩。",
            "example": "他一生戎马，立下定国安邦的功劳。"
        },
        2820: {
            "pinyin": "dìng qīng fú wēi",
            "meaning": "扶危济困、稳定倾危的局势。",
            "example": "在公司最困难的时候，是他出手定倾扶危。"
        },
        2821: {
            "pinyin": "dìng yú yī zūn",
            "meaning": "确定为唯一的最高权威，形容独断专行或不容分说的地位。",
            "example": "学术研究不应定于一尊，而要允许不同声音。"
        },
        2822: {
            "pinyin": "diū kuī xiè jiǎ",
            "meaning": "扔掉头盔，卸下铠甲，形容打败仗后狼狈逃窜的样子。",
            "example": "敌军被我军击溃，只得丢盔卸甲而逃。"
        },
        2823: {
            "pinyin": "diū sān là sì",
            "meaning": "形容做事马虎，记忆力差，常常忘东忘西。",
            "example": "他办事总是丢三落四，让人不放心。"
        },
        2824: {
            "pinyin": "diū xià pá ér nòng sào zhou",
            "meaning": "扔下耙子去拿扫帚，比喻事情还没做完就去干别的，忙乱无序。",
            "example": "工作要按部就班，不能老是丢下耙儿弄扫帚。"
        },
        2825: {
            "pinyin": "diū zú bǎo jū",
            "meaning": "在棋局中舍弃卒子以保战车，比喻牺牲小的利益以保全大的利益。",
            "example": "在谈判中适当丢卒保车，反而能争取更多空间。"
        },
        2826: {
            "pinyin": "dōng bēn xī zǒu",
            "meaning": "到处奔走，多方奔忙。",
            "example": "为了这次筹款，他东奔西走忙了大半年。"
        },
        2827: {
            "pinyin": "dōng chuāng shì fā",
            "meaning": "比喻阴谋、秘密的事情被揭露。",
            "example": "事情终于东窗事发，他受到了应有的惩罚。"
        },
        2828: {
            "pinyin": "dōng chuáng kuài xù",
            "meaning": "原指东床择婿的故事，后多指称心如意的女婿。",
            "example": "女儿找了个东床快婿，父母十分满意。"
        },
        2829: {
            "pinyin": "dōng chuáng tǎn fú",
            "meaning": "出自“东床坦腹”，形容女婿坦率自然、落落大方。",
            "example": "他在岳父家东床坦腹，一点也不拘谨。"
        },
        2830: {
            "pinyin": "dōng dǎo xī wāi",
            "meaning": "形容站立或摆放不稳，东倒西歪；也形容不端正、不整齐。",
            "example": "地震过后，屋里的家具全都东倒西歪。"
        },
        2831: {
            "pinyin": "dōng dào zhī yì",
            "meaning": "主人对客人的情谊、礼遇之道。",
            "example": "这次招待略尽东道之谊，还望不要嫌简陋。"
        },
        2832: {
            "pinyin": "dōng dào zhǔ",
            "meaning": "指主人、款待他人的一方。",
            "example": "作为东道主，他把行程安排得井井有条。"
        },
        2833: {
            "pinyin": "dōng fāng qiān qí",
            "meaning": "原指女子的如意郎君，后也形容仪容俊美的青年男子。",
            "example": "在她心中，他就是那位东方千骑。"
        },
        2834: {
            "pinyin": "dōng fēng chuī mǎ ěr",
            "meaning": "像春风吹在马耳边一样，比喻听不进劝告。",
            "example": "父母的话在他那里不过是东风吹马耳。"
        },
        2835: {
            "pinyin": "dōng fēng hào dàng",
            "meaning": "形容东风盛大、气势浩荡，多借指革命或进步的力量强大。",
            "example": "改革的东风浩荡，给这座城市带来新气象。"
        },
        2836: {
            "pinyin": "dōng fēng huà yǔ",
            "meaning": "比喻良好的教育或影响像春风化雨般滋润人心。",
            "example": "老师的教诲如东风化雨，伴随他一生。"
        },
        2837: {
            "pinyin": "dōng fēng rén miàn",
            "meaning": "出自“东风人面”，多用来形容春日重逢的喜悦或美好的景象。",
            "example": "十年之后再相见，依旧是东风人面。"
        },
        2838: {
            "pinyin": "dōng fēng yā dǎo xī fēng",
            "meaning": "比喻一种力量压倒另一种力量，多指好的一方战胜坏的一方。",
            "example": "正气终将东风压倒西风。"
        },
        2839: {
            "pinyin": "dōng fú xī dǎo",
            "meaning": "扶住这边，倒了那边，比喻顾此失彼，难以兼顾。",
            "example": "资金有限，只能东扶西倒地维持几个项目。"
        },
        2840: {
            "pinyin": "dōng guān xù shǐ",
            "meaning": "指撰写史书或续写历史记载。",
            "example": "他自比东观续史之人，一生致力于地方史编纂。"
        },
        2841: {
            "pinyin": "dōng guō xiān shēng",
            "meaning": "出自“东郭先生与狼”的故事，比喻不分善恶、一味同情坏人的人。",
            "example": "对待骗子可不能当东郭先生。"
        },
        2842: {
            "pinyin": "dōng hǎi lāo zhēn",
            "meaning": "到东海去捞一根针，比喻极难办成的事。",
            "example": "想在茫茫人海中找到他，无异于东海捞针。"
        },
        2843: {
            "pinyin": "dōng hǎi yáng chén",
            "meaning": "东海里扬起尘土，形容声势浩大或变化巨大。",
            "example": "这场风暴好似东海扬尘，惊天动地。"
        },
        2844: {
            "pinyin": "dōng jiàn nán jīn",
            "meaning": "原指东南的竹箭和西南的金石，后比喻珍贵的人才。",
            "example": "这里人才济济，可谓东箭南金。"
        },
        2845: {
            "pinyin": "dōng láo xī yàn",
            "meaning": "伯劳东飞，燕子西飞，比喻情侣或朋友离别，各奔东西。",
            "example": "毕业之后，同学们东劳西燕，再难常聚。"
        },
        2846: {
            "pinyin": "dōng lā xī chě",
            "meaning": "一会儿拉东一会儿扯西，比喻说话或做事没有中心，漫无边际。",
            "example": "开会要抓重点，别总东拉西扯。"
        },
        2847: {
            "pinyin": "dōng lín xī zhǎo",
            "meaning": "比喻零碎的材料或片断的事物，不能反映整体。",
            "example": "这份材料只是东鳞西爪，还需系统整理。"
        },
        2848: {
            "pinyin": "dōng nán bàn bì",
            "meaning": "指长江中下游及其以东、以南的半边江山。",
            "example": "他戍守边关，被称为守住东南半壁的名将。"
        },
        2849: {
            "pinyin": "dōng nán què fēi",
            "meaning": "比喻亲人、恋人分离，各自飞散。",
            "example": "战乱使无数家庭东南雀飞，骨肉分离。"
        },
        2850: {
            "pinyin": "dōng nù xī yuàn",
            "meaning": "一会儿向东生气，一会儿向西埋怨，形容情绪无常或到处抱怨。",
            "example": "他整天东怒西怨，谁都不满意。"
        },
        2851: {
            "pinyin": "dōng pǎo xī diān",
            "meaning": "到处奔跑、颠簸，形容奔走忙碌。",
            "example": "为了项目顺利推进，他东跑西颠地联络各方。"
        },
        2852: {
            "pinyin": "dōng qiáng chù zǐ",
            "meaning": "指闺中少女，多用来称赞女子端庄洁身自好。",
            "example": "她自小被视为东墙处子，出嫁时人人称羡。"
        },
        2853: {
            "pinyin": "dōng shān gāo wò",
            "meaning": "指隐居东山，高枕而卧，比喻退隐不仕。",
            "example": "功成身退，东山高卧，也是另一种人生选择。"
        },
        2854: {
            "pinyin": "dōng shān zài qǐ",
            "meaning": "比喻失势之后重新恢复地位或东山再起。",
            "example": "经过多年沉淀，他终于东山再起。"
        },
        2855: {
            "pinyin": "dōng shī xiào pín",
            "meaning": "比喻盲目模仿别人，结果适得其反。",
            "example": "品牌推广不能简单照搬，否则容易东施效颦。"
        },
        2856: {
            "pinyin": "dōng shí xī sù",
            "meaning": "东边吃饭，西边住宿，形容漂泊不定或生活辛劳。",
            "example": "他在外打工，东食西宿，十分辛苦。"
        },
        2857: {
            "pinyin": "dōng tú xī mǒ",
            "meaning": "到处乱涂乱抹，比喻做事没有章法或弄得一团糟。",
            "example": "孩子把墙上东涂西抹，弄得家里乱七八糟。"
        },
        2858: {
            "pinyin": "dōng tù xī wū",
            "meaning": "指日月东升西落，也比喻光阴流逝。",
            "example": "东兔西乌，转眼又是一年。"
        },
        2859: {
            "pinyin": "dōng xī nán běi",
            "meaning": "东、南、西、北四个方向，常用来形容到处、各个方面。",
            "example": "他为了找资料，东西南北到处跑。"
        },
        2860: {
            "pinyin": "dōng yáo xī bǎi",
            "meaning": "来回摇摆，形容走路不稳或态度不坚定。",
            "example": "小船在浪里东摇西摆，让人站不稳。"
        },
        2861: {
            "pinyin": "dōng yě bā rén",
            "meaning": "本为周代的歌手乐官名，后多用以指平民歌者或民间艺人。",
            "example": "这首民歌出自东野巴人之口，流传甚广。"
        },
        2862: {
            "pinyin": "dōng yú yǐ shì, sāng yú fēi wǎn",
            "meaning": "东隅的日光已经逝去，桑榆的日光却还不算晚，比喻晚年或后期仍有可为。",
            "example": "他中年改行，东隅已逝，桑榆非晚，终于干出了名堂。"
        },
        2863: {
            "pinyin": "dōng zhāng xī wàng",
            "meaning": "向东向西东张西望，形容心神不定或东看西看。",
            "example": "新来的同学在教室里东张西望，显得有些紧张。"
        },
        2864: {
            "pinyin": "dōng zhēng xī tǎo",
            "meaning": "向东征战，向西讨伐，形容东征西讨、四处用兵。",
            "example": "多年东征西讨，他终于平定了边疆。"
        },
        2865: {
            "pinyin": "dōng zǒu xī gù",
            "meaning": "向东走又向西看，比喻心态犹豫不决或顾前顾后。",
            "example": "做决定不能总是东走西顾，机会稍纵即逝。"
        },
        2866: {
            "pinyin": "dōng hán bào bīng, xià rè wò huǒ",
            "meaning": "冬天抱冰、夏天握火，形容刻苦自勉、磨炼意志。",
            "example": "他训练自己可谓冬寒抱冰，夏热握火，非常刻苦。"
        },
        2867: {
            "pinyin": "dōng hōng xiān shēng",
            "meaning": "指学识浅陋、见识迂腐的读书人，多含讥讽之意。",
            "example": "鲁迅笔下常讽刺那些不问世事的冬烘先生。"
        },
        2868: {
            "pinyin": "dōng qiú xià gě",
            "meaning": "裘是皮衣，葛是葛布衣裳，泛指美好的衣服。",
            "example": "他从小家境殷实，穿的都是冬裘夏葛。"
        },
        2869: {
            "pinyin": "dōng rì kě ài",
            "meaning": "像冬天的太阳一样令人感到温暖，比喻为人温和可亲。",
            "example": "这位老教师脾气温和，真可谓冬日可爱。"
        },
        2870: {
            "pinyin": "dōng rì xià yún",
            "meaning": "冬天的太阳，夏天的云层，比喻态度温和可亲、令人愿意接近。",
            "example": "他的处事风格如冬日夏云，让同事倍感温暖。"
        },
        2871: {
            "pinyin": "dōng shàn xià lú",
            "meaning": "冬天送扇子，夏天送火炉，比喻不合时宜或毫无用处的东西。",
            "example": "你现在提这个建议，简直是冬扇夏炉。"
        },
        2872: {
            "pinyin": "dōng wēn xià qìng",
            "meaning": "冬天让父母温暖，夏天让父母凉爽，形容奉养父母无微不至，也泛指冬暖夏凉。",
            "example": "他侍奉父母冬温夏凊，邻里都很称赞。"
        },
        2873: {
            "pinyin": "dǒng hú zhí bǐ",
            "meaning": "指史官据实直书，秉笔公正不阿。",
            "example": "媒体要做当代的董狐直笔，真实记录社会。"
        },
        2874: {
            "pinyin": "dòng bù shī shí",
            "meaning": "行动不失时机，形容做事合乎时宜、把握分寸。",
            "example": "他处事动不失时，很少出错。"
        },
        2875: {
            "pinyin": "dòng jìng yǒu cháng",
            "meaning": "动与静都有一定的法则，形容行动合乎规范、有章可循。",
            "example": "军营生活动静有常，纪律十分严格。"
        },
        2876: {
            "pinyin": "dòng pò jīng xīn",
            "meaning": "形容场面或经历十分惊险，使人心神大为震撼。",
            "example": "那次地震的场景真是动魄惊心。"
        },
        2877: {
            "pinyin": "dòng rén xīn pò",
            "meaning": "形容作品、事迹等非常感人，深深打动人的心灵。",
            "example": "这部纪录片动人心魄，让人潸然泪下。"
        },
        2878: {
            "pinyin": "dòng rén xīn xián",
            "meaning": "像拨动心弦一样，使人深受感动或产生强烈共鸣。",
            "example": "她清亮的歌声动人心弦，全场静静聆听。"
        },
        2879: {
            "pinyin": "dòng rú tuō tù",
            "meaning": "形容行动迅速敏捷，好像奔跑的兔子。",
            "example": "特警队员个个动如脱兔，动作利落。"
        },
        2880: {
            "pinyin": "dòng xīn chù mù",
            "meaning": "看到触目惊心的事物而内心震动，形容景象极其惨烈或触目惊心。",
            "example": "灾后的画面令人动心怵目。"
        },
        2881: {
            "pinyin": "dòng xīn hài mù",
            "meaning": "看到可怕景象而心惊目骇，形容非常恐怖震撼。",
            "example": "山洪暴发的情景真叫人动心骇目。"
        },
        2882: {
            "pinyin": "dòng xīn rěn xìng",
            "meaning": "出自古训，指在艰难困苦中磨炼心志，增长才干。",
            "example": "他经历多年动心忍性，终于有所成就。"
        },
        2883: {
            "pinyin": "dòng zhé dé jiù",
            "meaning": "一有所动辄就招致责备，形容处境艰难、容易被指责。",
            "example": "在那种高压环境下，稍有差错便动辄得咎。"
        },
        2884: {
            "pinyin": "dòng zhī yǐ qíng",
            "meaning": "用情感来打动别人，多指以真诚的态度感化他人。",
            "example": "教育孩子贵在动之以情，晓之以理。"
        },
        2885: {
            "pinyin": "dòng liáng zhī cái",
            "meaning": "比喻能担当重任的人才。",
            "example": "这些年轻人将来都是国家的栋梁之材。"
        },
        2886: {
            "pinyin": "dòng zhé cuī bēng",
            "meaning": "栋梁折断，椽子崩塌，比喻国家或团体的支柱人物相继丧失。",
            "example": "短短几年内几位老专家先后离世，真有栋折榱崩之感。"
        },
        2887: {
            "pinyin": "dòng chá qiū háo",
            "meaning": "观察入微，连鸟兽的秋毫之末都看得清，比喻目光敏锐。",
            "example": "审计人员洞察秋毫，很快发现了账目的问题。"
        },
        2888: {
            "pinyin": "dòng chá yī qiè",
            "meaning": "对一切情况都观察得很清楚。",
            "example": "他对企业的运行状况洞察一切。"
        },
        2889: {
            "pinyin": "dòng chá qí jiān",
            "meaning": "洞悉其中的奸诈或阴谋。",
            "example": "经过仔细调查，警方已经洞察其奸。"
        },
        2890: {
            "pinyin": "dòng chè shì lǐ",
            "meaning": "通达透彻地了解事物的道理。",
            "example": "只有洞彻事理，才能作出正确决策。"
        },
        2891: {
            "pinyin": "dòng fáng huā zhú",
            "meaning": "指新婚洞房中的花烛之夜，多用来祝贺新婚。",
            "example": "亲友们齐来祝贺他们洞房花烛。"
        },
        2892: {
            "pinyin": "dòng jiàn zhèng jié",
            "meaning": "洞见病灶所在，比喻看清问题的关键。",
            "example": "他一针见血，洞见症结所在。"
        },
        2893: {
            "pinyin": "dòng jiàn fèi xīng",
            "meaning": "洞察兴衰成败的原因。",
            "example": "读史可以洞鉴废兴，吸取前人的教训。"
        },
        2894: {
            "pinyin": "dòng ruò guān huǒ",
            "meaning": "好像近距离看火一样清楚，比喻观察事物十分透彻明白。",
            "example": "在老工程师眼里，这些故障简直是洞若观火。"
        },
        2895: {
            "pinyin": "dòng tiān fú dì",
            "meaning": "指景色优美、适宜修身养性的地方。",
            "example": "这处山谷仿佛洞天福地，远离尘嚣。"
        },
        2896: {
            "pinyin": "dòng yōu zhú wēi",
            "meaning": "洞察幽深之处，照见细微之处，形容观察入微。",
            "example": "他对社会问题的分析可谓洞幽烛微。"
        },
        2897: {
            "pinyin": "dòng zhú qí jiān",
            "meaning": "像灯烛一样照见奸邪，比喻看穿别人的诡计阴谋。",
            "example": "老检察官早已洞烛其奸，不会被花言巧语蒙蔽。"
        },
        2898: {
            "pinyin": "dòng jiě bīng shì",
            "meaning": "像冰冻融化一样，比喻困难、误会或障碍完全消除。",
            "example": "经过坦诚交流，双方的误会终于冻解冰释。"
        },
        2899: {
            "pinyin": "dòng yí xū hè",
            "meaning": "虚张声势，使人疑惧不安。",
            "example": "对方只是在恫疑虚喝，你不用太紧张。"
        },
        2900: {
            "pinyin": "dōu dǔ lián cháng",
            "meaning": "兜：包括。包括肚子连同肠子，比喻全部东西一起处理。",
            "example": "仓库里过期物品只好兜肚连肠地清理掉。"
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

    print(f"已为 2801–2900 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
