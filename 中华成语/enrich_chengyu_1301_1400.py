import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    enrich = {
        1301: {
            "pinyin": "cái gāo yì guǎng",
            "meaning": "才华高超，胸怀宏大，思想见识十分开阔。",
            "example": "他自幼好学，长大后才高意广，著作颇丰。"
        },
        1302: {
            "pinyin": "cái gāo yùn jiǎn",
            "meaning": "才华出众却一生多舛，命运坎坷。",
            "example": "许多古代文人都是才高运蹇，怀才不遇。"
        },
        1303: {
            "pinyin": "cái huá chāo zhòng",
            "meaning": "才华超过一般人，极为出众。",
            "example": "她在音乐方面才华超众，屡获大奖。"
        },
        1304: {
            "pinyin": "cái jiān wén wǔ",
            "meaning": "既有文才，又通武艺，文武双全。",
            "example": "这位将领才兼文武，深得君王器重。"
        },
        1305: {
            "pinyin": "cái mào shuāng quán",
            "meaning": "又有才学，又有美貌。",
            "example": "她聪慧端庄，可谓才貌双全。"
        },
        1306: {
            "pinyin": "cái qì guò rén",
            "meaning": "才情和气度都胜过常人。",
            "example": "他谈吐不凡，才气过人。"
        },
        1307: {
            "pinyin": "cái qì wú shuāng",
            "meaning": "才情天下少有，独一无二。",
            "example": "这位诗人放眼当世，才气无双。"
        },
        1308: {
            "pinyin": "cái shí guò rén",
            "meaning": "才学与见识都超过一般人。",
            "example": "他在史学上的造诣可谓才识过人。"
        },
        1309: {
            "pinyin": "cái shū xué qiǎn",
            "meaning": "才学疏浅，学问不深。",
            "example": "我不过才疏学浅，不敢在行家面前班门弄斧。"
        },
        1310: {
            "pinyin": "cái shū yì guǎng",
            "meaning": "才学不高却胸怀广大，多用作自谦之辞。",
            "example": "他常自称才疏意广，仍愿为后辈指点迷津。"
        },
        1311: {
            "pinyin": "cái shū zhì dà",
            "meaning": "才学有限而志向很大，多含自谦或讽刺意味。",
            "example": "他常说自己才疏志大，还需要不断学习。"
        },
        1312: {
            "pinyin": "cái wàng gāo yǎ",
            "meaning": "才学和名望都很高，气度优雅。",
            "example": "这位老先生德高望重，真是才望高雅。"
        },
        1313: {
            "pinyin": "cái zǐ jiā rén",
            "meaning": "有才华的男子和美貌的女子，常用来指般配的情侣。",
            "example": "二人郎才女貌，被称作才子佳人。"
        },
        1314: {
            "pinyin": "cái dà nán yòng",
            "meaning": "才能太大反而难以施展，多指不被环境或制度所容。",
            "example": "这位谋士怀才不遇，可谓材大难用。"
        },
        1315: {
            "pinyin": "cái gāo zhī shēn",
            "meaning": "才能高超，学问见识深厚。",
            "example": "他在哲学领域材高知深，著述颇丰。"
        },
        1316: {
            "pinyin": "cái néng jiān bèi",
            "meaning": "各种才能和技能都具备，十分全面。",
            "example": "要胜任这份工作，需要材能兼备的人才。"
        },
        1317: {
            "pinyin": "cái yùn hēng tōng",
            "meaning": "财运顺利、通达，赚钱较为容易。",
            "example": "近几年他生意兴隆，财运亨通。"
        },
        1318: {
            "pinyin": "cǎi jí fēng fěi",
            "meaning": "出自《论语》，指采摘萝卜芥菜一类低贱之物也不嫌弃，比喻不因人或物卑贱而加以轻视。",
            "example": "真正的贤主会采及葑菲，不弃寒门之士。"
        },
        1319: {
            "pinyin": "cǎi lán zèng yào",
            "meaning": "采兰赠药，比喻赠人清香或有益之物，亦指以佳言良方相赠。",
            "example": "老师常以嘉言善行相勉，如同采兰赠药。"
        },
        1320: {
            "pinyin": "cǎi xīn zhī yōu",
            "meaning": "因砍柴取火而担忧，比喻对隐伏的祸患有所担心。",
            "example": "他对制度上的漏洞心怀采薪之忧，主张及早修补。"
        },
        1321: {
            "pinyin": "cǎi fèng suí yā",
            "meaning": "彩凤跟在乌鸦后面，比喻贤才误随小人或好人混在坏人之中。",
            "example": "他若一味结交不学无术之徒，便成了彩凤随鸦。"
        },
        1322: {
            "pinyin": "cǎi yī yú qīn",
            "meaning": "穿彩衣以娱亲人，出自“老莱子”的故事，比喻孝顺父母、逗父母欢心。",
            "example": "他处处为父母着想，可谓彩衣娱亲。"
        },
        1323: {
            "pinyin": "cǎi yún yì sàn",
            "meaning": "彩云容易消散，比喻美好的景象或情缘不易长久。",
            "example": "一段情事如彩云易散，终究没能长久。"
        },
        1324: {
            "pinyin": "cài shū zhī sè",
            "meaning": "菜蔬的颜色，比喻脸色枯槁、苍黄，多因饥饿或忧劳所致。",
            "example": "连日操劳，他面容消瘦，有了菜蔬之色。"
        },
        1325: {
            "pinyin": "cān fēng lù sù",
            "meaning": "以风为食、露中住宿，形容旅途或生活的艰辛漂泊。",
            "example": "他到处奔波，为生计餐风露宿。"
        },
        1326: {
            "pinyin": "cān fēng mù yǔ",
            "meaning": "迎着风、冒着雨前行，形容经受风吹雨打的艰辛生活。",
            "example": "多年来他在外奔走，餐风沐雨。"
        },
        1327: {
            "pinyin": "cān xīng zhuó fǔ",
            "meaning": "吃腥啄腐，比喻贪婪卑鄙、趋炎附势之辈。",
            "example": "那些餐腥啄腐的小人，只会在暗处中伤他人。"
        },
        1328: {
            "pinyin": "cān tòu jī guān",
            "meaning": "参透机括机关，比喻看穿事物的内情和关键所在。",
            "example": "他细细推敲案情，终究参透机关。"
        },
        1329: {
            "pinyin": "cán bào bù rén",
            "meaning": "残酷暴戾，对人毫无仁心。",
            "example": "这位暴君残暴不仁，百姓民不聊生。"
        },
        1330: {
            "pinyin": "cán bēi lěng zhì",
            "meaning": "宴席上剩下的杯酒和冷掉的肉，比喻被丢弃的残余事物或不被重视的人。",
            "example": "他不愿做别人眼中的残杯冷炙，选择重新出发。"
        },
        1331: {
            "pinyin": "cán biān duàn jiǎn",
            "meaning": "残缺不全的册子和简牍，比喻保存下来的零碎文献或资料。",
            "example": "这些史料虽是残编断简，却极具研究价值。"
        },
        1332: {
            "pinyin": "cán bīng bài jiàng",
            "meaning": "打了败仗后残存的兵士和将领，比喻失败的一方或败落的人。",
            "example": "战后营中只剩些残兵败将。"
        },
        1333: {
            "pinyin": "cán chá shèng fàn",
            "meaning": "剩下的茶和饭，比喻被遗弃的事物或不受重视的人。",
            "example": "他不甘心被当作残茶剩饭，决定另谋出路。"
        },
        1334: {
            "pinyin": "cán dōng là yuè",
            "meaning": "冬天将尽，腊月将过，形容一年中最寒冷、接近岁末的时节。",
            "example": "在残冬腊月里，乡村显得格外萧索。"
        },
        1335: {
            "pinyin": "cán gāo shèng fù",
            "meaning": "残存的膏脂和馥郁的香气，比喻前人遗留下来的成就或作品的余辉。",
            "example": "这部著作只是古人学问的残膏剩馥，却已令人叹服。"
        },
        1336: {
            "pinyin": "cán gēng lěng zhì",
            "meaning": "吃剩的羹汤和冷肉，比喻遭人抛弃的事物或人物。",
            "example": "他不愿在人家门下做残羹冷炙，宁可白手起家。"
        },
        1337: {
            "pinyin": "cán huā bài liǔ",
            "meaning": "凋谢的花、枯败的柳，比喻衰败的景象，亦指被侮辱、被蹂躏的妇女。",
            "example": "战乱之后，街巷冷落，如同残花败柳。"
        },
        1338: {
            "pinyin": "cán mín hài lǐ",
            "meaning": "残害百姓，败坏礼法道理。",
            "example": "暴政残民害理，终会招致天下共愤。"
        },
        1339: {
            "pinyin": "cán nián mù jǐng",
            "meaning": "晚年的景况，形容人已到了暮年。",
            "example": "他在残年暮景之时仍勤于著述。"
        },
        1340: {
            "pinyin": "cán nián yú lì",
            "meaning": "晚年所余下的精力，多为自谦之辞。",
            "example": "我这点残年余力，愿再为教育事业做些事情。"
        },
        1341: {
            "pinyin": "cán quē bù quán",
            "meaning": "有残损缺漏，不够完整。",
            "example": "这份资料保存已久，内容残缺不全。"
        },
        1342: {
            "pinyin": "cán shān shèng shuǐ",
            "meaning": "战乱或灾难后残存的山河，比喻破败后的景象。",
            "example": "多年战火，把这片土地折腾得只剩残山剩水。"
        },
        1343: {
            "pinyin": "cán zhā yú niè",
            "meaning": "残留的渣滓和余孽，比喻坏势力的残余部分。",
            "example": "必须彻底清除这些残渣余孽。"
        },
        1344: {
            "pinyin": "cán jì xiè kuāng",
            "meaning": "比喻名实不符、牵强附会，两者互不相干。",
            "example": "这些空洞的口号和实际工作蚕绩蟹匡，毫不相应。"
        },
        1345: {
            "pinyin": "cán shí jīng tūn",
            "meaning": "像蚕一样一点点吞食，像鲸一样一口吞尽，比喻先局部侵吞，继而全部占有。",
            "example": "他先暗中收购股权，后又蚕食鲸吞整个公司。"
        },
        1346: {
            "pinyin": "cán tóu yàn wěi",
            "meaning": "书法上形容起笔圆浑如蚕头，收笔轻捷如燕尾，后也用来形容字体俊逸。",
            "example": "这幅字用笔蚕头燕尾，极见功力。"
        },
        1347: {
            "pinyin": "cán fú qǐ hè",
            "meaning": "像鸭子仰头学鹤那样，形容因自己不如别人而感到惭愧。",
            "example": "与名家作品相比，他深感惭凫企鹤。"
        },
        1348: {
            "pinyin": "cǎn bù rěn dǔ",
            "meaning": "悲惨得叫人不忍心看。",
            "example": "灾后现场一片废墟，实在惨不忍睹。"
        },
        1349: {
            "pinyin": "cǎn bù rěn wén",
            "meaning": "事情悲惨得叫人不忍心听闻。",
            "example": "关于难民营的报道，真是惨不忍闻。"
        },
        1350: {
            "pinyin": "cǎn dàn jīng yíng",
            "meaning": "在艰难困苦的环境中辛勤经营，多指事业创建不易。",
            "example": "这家公司是他惨淡经营多年才有的规模。"
        },
        1351: {
            "pinyin": "cǎn jué rén huán",
            "meaning": "残酷悲惨到了人世间难以容忍的地步。",
            "example": "那场屠杀真是惨绝人寰，令人发指。"
        },
        1352: {
            "pinyin": "cǎn lǜ shào nián",
            "meaning": "指身着淡绿色衣服的美貌少年，后多指风度翩翩的青年男子。",
            "example": "他年少俊秀，正是一位惨绿少年。"
        },
        1353: {
            "pinyin": "cǎn wú rén dào",
            "meaning": "残忍到了没有人性、没有道理的地步。",
            "example": "这伙人手段毒辣，简直惨无人道。"
        },
        1354: {
            "pinyin": "càn làn huī huáng",
            "meaning": "光彩耀眼，极其辉煌灿烂。",
            "example": "夜空中焰火齐放，场面灿烂辉煌。"
        },
        1355: {
            "pinyin": "càn ruò fán xīng",
            "meaning": "像满天繁星一样灿烂，形容数量多而光彩夺目。",
            "example": "山城夜灯灿若繁星，美不胜收。"
        },
        1356: {
            "pinyin": "càn huā zhī lùn",
            "meaning": "像盛开的花一样绚丽的言辞，比喻言谈文辞华丽动人。",
            "example": "他辩才无碍，发言可谓粲花之论。"
        },
        1357: {
            "pinyin": "cāng cù zhī jì",
            "meaning": "匆忙仓促之时。",
            "example": "在仓卒之际，他依旧沉着冷静。"
        },
        1358: {
            "pinyin": "cāng cù zhǔ rén",
            "meaning": "在匆忙中暂时应付局面的人，多指临时主持事务的人。",
            "example": "他只是仓卒主人，许多事情还不熟悉。"
        },
        1359: {
            "pinyin": "cāng huáng chū táo",
            "meaning": "慌慌张张地逃跑。",
            "example": "敌军被突袭后仓皇出逃。"
        },
        1360: {
            "pinyin": "cāng huáng shī cuò",
            "meaning": "惊慌失措，不知所措。",
            "example": "突遇地震，人群一时仓皇失措。"
        },
        1361: {
            "pinyin": "cāng hǎi héng liú",
            "meaning": "大海横向奔流，比喻政局动荡、世道混乱。",
            "example": "在沧海横流的时代，更见英雄本色。"
        },
        1362: {
            "pinyin": "cāng hǎi sāng tián",
            "meaning": "大海变成桑田，形容世事变迁巨大。",
            "example": "几十年间，这里早已沧海桑田。"
        },
        1363: {
            "pinyin": "cāng hǎi yī sù",
            "meaning": "沧海中的一粒谷粒，比喻渺小微不足道。",
            "example": "个人的力量在时代面前不过沧海一粟。"
        },
        1364: {
            "pinyin": "cāng hǎi yí zhū",
            "meaning": "大海里遗失的珍珠，比喻埋没的人才或被遗忘的珍贵事物。",
            "example": "这位画家生前寂寂无名，实乃沧海遗珠。"
        },
        1365: {
            "pinyin": "cāng cuì yù dī",
            "meaning": "形容树木等绿得仿佛要滴下水来，十分青翠。",
            "example": "雨后山林苍翠欲滴，生机盎然。"
        },
        1366: {
            "pinyin": "cāng huáng fān fù",
            "meaning": "局势仓促多变，反复无常。",
            "example": "战事发展苍黄翻复，令人难以预料。"
        },
        1367: {
            "pinyin": "cāng shēng tú tàn",
            "meaning": "老百姓像被涂在炭火上一样，形容民众处境极其悲惨。",
            "example": "战乱连年，苍生涂炭。"
        },
        1368: {
            "pinyin": "cāng sōng cuì bǎi",
            "meaning": "青苍的松树和翠绿的柏树，常用来比喻坚贞不屈的品格。",
            "example": "山上苍松翠柏，四季常青。"
        },
        1369: {
            "pinyin": "cāng yán bái fà",
            "meaning": "面色苍老、头发花白，形容年老的容貌。",
            "example": "那位苍颜白发的老人依旧精神矍铄。"
        },
        1370: {
            "pinyin": "cāng yíng jiàn xuè",
            "meaning": "苍蝇一见血就飞来，比喻坏人专门趁机落井下石或从祸患中捞好处。",
            "example": "有人一听到他出事，立刻苍蝇见血般前来诋毁。"
        },
        1371: {
            "pinyin": "cáng gōng pēng gǒu",
            "meaning": "打完猎就把弓收藏、猎狗烹煮，比喻事情成功后就抛弃曾出过力的人。",
            "example": "他担心功成之后会被藏弓烹狗，所以格外谨慎。"
        },
        1372: {
            "pinyin": "cáng gòu nà wū",
            "meaning": "藏垢纳污，比喻包容、容纳各种缺点，也指包庇坏人。",
            "example": "这座古城历来藏垢纳污，也汇聚了各色人物。"
        },
        1373: {
            "pinyin": "cáng lóng wò hǔ",
            "meaning": "隐藏着龙和卧着虎，比喻潜藏着未被发现的人才。",
            "example": "这所小镇学校实为藏龙卧虎之地。"
        },
        1374: {
            "pinyin": "cáng nù sù yuàn",
            "meaning": "把怒气和仇怨藏在心里。",
            "example": "他表面平静，其实心中藏怒宿怨。"
        },
        1375: {
            "pinyin": "cáng qì dài shí",
            "meaning": "隐藏才器，等待时机。",
            "example": "他暂隐锋芒，宁愿藏器待时。"
        },
        1376: {
            "pinyin": "cáng qiǎo yú zhuō",
            "meaning": "把聪明才智隐藏在质朴笨拙的外表之下。",
            "example": "他处事低调，常以藏巧于拙示人。"
        },
        1377: {
            "pinyin": "cáng tóu lù wěi",
            "meaning": "藏住了头却露出尾巴，比喻想要隐瞒却仍然暴露。",
            "example": "他解释得前后矛盾，难免藏头露尾。"
        },
        1378: {
            "pinyin": "cáng wū nà gòu",
            "meaning": "同“藏垢纳污”，亦指包容污秽或包庇坏人。",
            "example": "若对恶行一味藏污纳垢，只会助长歪风。"
        },
        1379: {
            "pinyin": "cáng xíng nì yǐng",
            "meaning": "连形体和影子都隐藏起来，形容隐藏得极其周密。",
            "example": "他行踪诡秘，几乎藏形匿影。"
        },
        1380: {
            "pinyin": "cáng zhī míng shān, chuán zhī qí rén",
            "meaning": "把典籍藏在名山，传给合适的人，表示珍重文献，期待后人继承。",
            "example": "这些手稿当可藏之名山，传之其人。"
        },
        1381: {
            "pinyin": "cáng zōng niè jì",
            "meaning": "隐藏踪迹，悄悄行动。",
            "example": "他一路藏踪蹑迹，避免被人发现。"
        },
        1382: {
            "pinyin": "cāo dāo bì gē",
            "meaning": "拿起刀就一定能割，形容技艺娴熟，做事必有成效。",
            "example": "老匠人操作机器如操刀必割，干净利落。"
        },
        1383: {
            "pinyin": "cāo dāo shāng jǐn",
            "meaning": "不善用刀却去割锦，反而损坏了锦，比喻外行胡乱干预而坏事。",
            "example": "对专业工作不懂装懂，只会操刀伤锦。"
        },
        1384: {
            "pinyin": "cāo hàn chéng zhāng",
            "meaning": "挥笔成章，形容文思敏捷，下笔成文。",
            "example": "他操翰成章，不多时便写完演讲稿。"
        },
        1385: {
            "pinyin": "cāo qí jì yíng",
            "meaning": "运用奇特的计谋以取得胜利。",
            "example": "在商战中，他善于操奇计赢，屡屡得手。"
        },
        1386: {
            "pinyin": "cāo zhī guò jí",
            "meaning": "做事过于急躁，缺乏耐心。",
            "example": "改革不能操之过急，要循序渐进。"
        },
        1387: {
            "pinyin": "cāo zòng zì rú",
            "meaning": "操纵得心应手，十分自如。",
            "example": "多年经验让他对这套系统操纵自如。"
        },
        1388: {
            "pinyin": "cǎo cǎo liǎo shì",
            "meaning": "事情做得很草率，敷衍了事。",
            "example": "这份报告不能草草了事，必须认真修改。"
        },
        1389: {
            "pinyin": "cǎo cǎo shōu bīng",
            "meaning": "军队匆忙撤退，比喻事情尚未妥善处理就仓促结束。",
            "example": "会议尚未达成共识便草草收兵，难免留下隐患。"
        },
        1390: {
            "pinyin": "cǎo chuàng wèi jiù",
            "meaning": "事业刚刚起步，尚未完成。",
            "example": "公司如今仍是草创未就，需要大家齐心努力。"
        },
        1391: {
            "pinyin": "cǎo jiān qiú huó",
            "meaning": "在艰难环境中勉强求生。",
            "example": "战乱年月，他只得草间求活。"
        },
        1392: {
            "pinyin": "cǎo jiān rén mìng",
            "meaning": "把人命看得像草一样贱，形容极端蔑视生命。",
            "example": "那个暴君草菅人命，终于遭到推翻。"
        },
        1393: {
            "pinyin": "cǎo mǎn líng yǔ",
            "meaning": "监狱里长满了草，形容社会清平、罪犯很少。",
            "example": "国泰民安之时，往往是草满囹圄。"
        },
        1394: {
            "pinyin": "cǎo mǎng yīng xióng",
            "meaning": "出身草野而有作为的英雄人物。",
            "example": "这位草莽英雄虽无名望，却深得民心。"
        },
        1395: {
            "pinyin": "cǎo mù jiē bīng",
            "meaning": "把草木都当成敌兵，形容人在惊恐时疑神疑鬼。",
            "example": "失败之后，他一度草木皆兵。"
        },
        1396: {
            "pinyin": "cǎo mù jù xiǔ",
            "meaning": "草木都已腐朽，比喻时间久远或事物衰败。",
            "example": "古城荒废多年，早已草木俱朽。"
        },
        1397: {
            "pinyin": "cǎo mù zhī wēi",
            "meaning": "连草木都感受到威势，形容声威极大。",
            "example": "他的军威之盛，几乎草木知威。"
        },
        1398: {
            "pinyin": "cǎo lú sān gù",
            "meaning": "即“三顾草庐”，比喻诚心求贤、礼遇人才。",
            "example": "他多次登门相请，可谓草庐三顾。"
        },
        1399: {
            "pinyin": "cǎo shuài cóng shì",
            "meaning": "做事情鲁莽、草率。",
            "example": "关系到安全的问题决不能草率从事。"
        },
        1400: {
            "pinyin": "cǎo shuài shōu bīng",
            "meaning": "匆忙结束战斗或活动，比喻事情半途而废。",
            "example": "项目忽然被叫停，算是草率收兵了。"
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

    print(f"已为 1301–1400 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
