import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 将 4501–4600 号成语的详细信息补充到 enrich 字典中
    enrich = {
        4501: {
            "pinyin": "gān qīng dǐ shì",
            "meaning": "干卿何事的缩略语，意为与你何干、关你什么事，多用于表示不满或拒绝干预。",
            "example": "这是我的私事，干卿底事。"
        },
        4502: {
            "pinyin": "gān xiāo líng yún",
            "meaning": "干：冲、直上；霄：云霄。直上云霄，凌空冲云，比喻志向远大或声势极盛。",
            "example": "少年豪情干霄凌云，立志有所作为。"
        },
        4503: {
            "pinyin": "gān yún bì rì",
            "meaning": "云气高耸遮蔽日光，比喻树木高大繁茂，或气势盛大惊人。",
            "example": "密林干云蔽日，行人须点灯而行。"
        },
        4504: {
            "pinyin": "gān tóu rì jìn",
            "meaning": "竿头：竿子的顶端；日进：天天前进。比喻学业、修养等不断进步。",
            "example": "只要持之以恒，必能竿头日进。"
        },
        4505: {
            "pinyin": "gān tóu zhí shàng",
            "meaning": "好像顺着竿子一直往上爬，比喻地位、成绩等迅速上升。",
            "example": "他仕途顺利，几年间官阶竿头直上。"
        },
        4506: {
            "pinyin": "gān cháng cùn duàn",
            "meaning": "肝肠好像一寸寸断开，形容极度悲痛。",
            "example": "噩耗传来，令家人肝肠寸断。"
        },
        4507: {
            "pinyin": "gān dǎn chǔ yuè",
            "meaning": "肝胆：比喻内心；楚越：相距遥远的两地。比喻情谊疏远，如肝胆分隔、相去万里。",
            "example": "昔日至交，如今却成肝胆楚越，令人唏嘘。"
        },
        4508: {
            "pinyin": "gān dǎn guò rén",
            "meaning": "肝胆：指勇气、气魄。形容非常勇敢，气概超过常人。",
            "example": "他临危不惧，真是肝胆过人。"
        },
        4509: {
            "pinyin": "gān dǎn xiāng zhào",
            "meaning": "肝胆相照：以赤诚之心相见。形容彼此坦诚相待，忠诚相助。",
            "example": "多年的战友情，使他们肝胆相照。"
        },
        4510: {
            "pinyin": "gān dǎn yù suì",
            "meaning": "肝胆好像要碎裂一样，形容极度悲痛或愤懑。",
            "example": "目睹惨状，无不肝胆欲碎。"
        },
        4511: {
            "pinyin": "gān nǎo tú dì",
            "meaning": "肝和脑洒在地上，形容牺牲惨烈，亦用以表示竭尽忠诚、不惜牺牲生命。",
            "example": "愿为国事肝脑涂地，在所不惜。"
        },
        4512: {
            "pinyin": "gān xīn ruò liè",
            "meaning": "肝和心仿佛都裂开了，形容极度伤心悲痛。",
            "example": "闻此噩耗，他只觉肝心若裂。"
        },
        4513: {
            "pinyin": "gān bài xià fēng",
            "meaning": "甘心失败，处于下风，多指自认不如对方。",
            "example": "论学问，我自愧不如，只好甘败下风。"
        },
        4514: {
            "pinyin": "gān guā kǔ dì",
            "meaning": "甘甜的瓜却有苦蒂，比喻事物好坏相伴，不可能十全十美。",
            "example": "世事如甘瓜苦蒂，总难尽如人意。"
        },
        4515: {
            "pinyin": "gān jū rén hòu",
            "meaning": "甘心居于人后，不与人争先，多形容为人谦逊或缺乏进取心。",
            "example": "他从不争功，宁肯甘居人后。"
        },
        4516: {
            "pinyin": "gān kǔ yǔ gòng",
            "meaning": "甘甜与苦难共同承担，比喻同甘共苦、患难与共。",
            "example": "夫妻二人甘苦与共，携手度过难关。"
        },
        4517: {
            "pinyin": "gān pín lè dào",
            "meaning": "安于贫穷，以坚持道义为乐。",
            "example": "他淡泊名利，甘贫乐道，一生著述不辍。"
        },
        4518: {
            "pinyin": "gān sǐ rú yí",
            "meaning": "为正义事业甘愿牺牲生命，觉得像吃饴糖一样甘甜。",
            "example": "革命先烈甘死如饴，才有今日太平。"
        },
        4519: {
            "pinyin": "gān táng yí ài",
            "meaning": "源自召伯甘棠的典故，指官吏施政仁爱，离任后仍为百姓怀念。",
            "example": "父母官清正爱民，自会留下甘棠遗爱。"
        },
        4520: {
            "pinyin": "gān xīn míng mù",
            "meaning": "心愿已了，闭目而死，形容死时无憾。",
            "example": "见子女各有成就，他方才甘心瞑目。"
        },
        4521: {
            "pinyin": "gān xīn qíng yuàn",
            "meaning": "心里情愿，毫无勉强。",
            "example": "为了孩子再辛苦，我也甘心情愿。"
        },
        4522: {
            "pinyin": "gān xīn shǒu jí",
            "meaning": "出自《诗经·卫风·伯兮》，指即使思念到头痛也心甘情愿，形容对所思之人极其痴情。",
            "example": "她对远行的丈夫朝思夜想，简直是甘心首疾。"
        },
        4523: {
            "pinyin": "gān yán měi yǔ",
            "meaning": "甜蜜动听、用来讨好奉承人的话。",
            "example": "他嘴上一套甘言美语，实则难以信任。"
        },
        4524: {
            "pinyin": "gān yǔ suí chē",
            "meaning": "车到哪里，甘霖就下到哪里，比喻德政所至，恩泽普被。",
            "example": "新任刺史清廉仁政，百姓称其政如甘雨随车。"
        },
        4525: {
            "pinyin": "gān zhī rú yí",
            "meaning": "把艰难痛苦看得像甜食一样，形容甘愿承受艰辛。",
            "example": "为理想而吃苦，他视之甘之如饴。"
        },
        4526: {
            "pinyin": "gǎn jìn shā jué",
            "meaning": "赶尽并杀绝，比喻把敌人或对方彻底消灭干净。",
            "example": "对付盗匪不可心软，否则难以赶尽杀绝。"
        },
        4527: {
            "pinyin": "gǎn làng tóu",
            "meaning": "比喻抓住时机，乘着形势的浪头前进，也指赶时髦、凑热闹。",
            "example": "他总爱赶浪头，什么新潮都要试一试。"
        },
        4528: {
            "pinyin": "gǎn yā zi shàng jià",
            "meaning": "把鸭子赶到架子上，比喻强迫人去做力所不及的事。",
            "example": "让一个新人独当大任，无异于赶鸭子上架。"
        },
        4529: {
            "pinyin": "gǎn ēn dài dé",
            "meaning": "感激别人的恩德，心怀深厚谢意。",
            "example": "受人相助，当感恩戴德，铭记在心。"
        },
        4530: {
            "pinyin": "gǎn ēn tú bào",
            "meaning": "心怀感恩而图报答别人的恩德。",
            "example": "他始终想着感恩图报，不负师长栽培。"
        },
        4531: {
            "pinyin": "gǎn jī tì líng",
            "meaning": "因感激而涕泪纵横，形容非常感动。",
            "example": "听完这番话，老人不禁感激涕零。"
        },
        4532: {
            "pinyin": "gǎn jīn huái xī",
            "meaning": "由眼前事物触景生情，既感慨现在，又怀念过去。",
            "example": "登临古城楼，他不由感今怀昔。"
        },
        4533: {
            "pinyin": "gǎn jiù zhī āi",
            "meaning": "感念旧人旧事而发出的哀叹，表示怀旧之情。",
            "example": "故地重游，勾起他无限感旧之哀。"
        },
        4534: {
            "pinyin": "gǎn kǎi wàn duān",
            "meaning": "感慨之事多得难以尽述，形容感触极多。",
            "example": "目睹世事变迁，他心中感慨万端。"
        },
        4535: {
            "pinyin": "gǎn kǎi wàn qiān",
            "meaning": "感慨之情极多，形容思绪纷繁、感触很深。",
            "example": "读到此处，不禁令人感慨万千。"
        },
        4536: {
            "pinyin": "gǎn kǎi xì zhī",
            "meaning": "对某事物怀有强烈感慨，情意系念不忘。",
            "example": "他对故国山河感慨系之，终身难忘。"
        },
        4537: {
            "pinyin": "gǎn qíng yòng shì",
            "meaning": "不从理智和原则出发，而凭个人情绪办事。",
            "example": "处理公事切忌感情用事。"
        },
        4538: {
            "pinyin": "gǎn rén fèi fǔ",
            "meaning": "形容言语或文章极能打动人心。",
            "example": "这封家书朴实真挚，感人肺腑。"
        },
        4539: {
            "pinyin": "gǎn tiān dòng dì",
            "meaning": "形容感情真挚、义行伟大，连天地都为之感动。",
            "example": "他们救死扶伤的事迹，真可谓感天动地。"
        },
        4540: {
            "pinyin": "gǎn tóng shēn shòu",
            "meaning": "比喻对别人的遭遇感同身历，好像自己亲身经历一样。",
            "example": "听完受灾群众的讲述，大家无不感同身受。"
        },
        4541: {
            "pinyin": "gǎn yù wàng shēn",
            "meaning": "因感激知遇之恩而不惜牺牲生命。",
            "example": "他受国士之遇，自是感遇忘身。"
        },
        4542: {
            "pinyin": "gǎn bù chéng mìng",
            "meaning": "怎敢不接受你的命令或意见，多为谦辞。",
            "example": "既蒙厚爱，晚生敢不承命。"
        },
        4543: {
            "pinyin": "gǎn nù ér bù gǎn yán",
            "meaning": "心里敢于愤怒，却不敢说出来，形容在强权压制下有气难言。",
            "example": "众人敢怒而不敢言，只得暗自摇头。"
        },
        4544: {
            "pinyin": "gǎn nù gǎn yán",
            "meaning": "既敢愤怒也敢直言，形容性格刚直，不畏权势。",
            "example": "他一向刚直不阿，凡不平事皆敢怒敢言。"
        },
        4545: {
            "pinyin": "gǎn zuò gǎn dāng",
            "meaning": "敢于做事，也敢承担后果，形容责任心强。",
            "example": "出了差错，他主动揽下责任，真是敢作敢当。"
        },
        4546: {
            "pinyin": "gàn fù zhī gǔ",
            "meaning": "语出《易·蛊》，“干父之蛊，有子，考无咎”，指继承并完成父辈未竟的事业。",
            "example": "他立志干父之蛊，重振家声。"
        },
        4547: {
            "pinyin": "gāng bì zì yòng",
            "meaning": "性情刚强，固执己见，不肯采纳他人意见。",
            "example": "为政者若刚愎自用，必致贻误大事。"
        },
        4548: {
            "pinyin": "gāng cháng jí è",
            "meaning": "性情刚直，痛恨邪恶。",
            "example": "他素来刚肠嫉恶，绝不与奸佞同流合污。"
        },
        4549: {
            "pinyin": "gāng róu xiāng jì",
            "meaning": "刚强与柔和互相配合或调剂。",
            "example": "处事当刚柔相济，方能进退自如。"
        },
        4550: {
            "pinyin": "gāng yì mù nè",
            "meaning": "刚强有毅力而少言木讷，多形容质朴的君子之风。",
            "example": "他为人刚毅木讷，却极讲信义。"
        },
        4551: {
            "pinyin": "gāng zhí bù ē",
            "meaning": "刚直正派，不阿谀奉承权贵。",
            "example": "此人一向刚直不阿，深得百姓敬重。"
        },
        4552: {
            "pinyin": "gāng zhōng róu wài",
            "meaning": "内心刚强而外表柔和。",
            "example": "她看似温婉，其实刚中柔外，极有主见。"
        },
        4553: {
            "pinyin": "gāng jǔ mù zhāng",
            "meaning": "提起纲领，细目自然张列，比喻抓住关键，其他问题就容易解决。",
            "example": "只要把制度建设抓好，便可纲举目张。"
        },
        4554: {
            "pinyin": "gāng jīn tiě gǔ",
            "meaning": "像钢筋铁骨一样坚硬，比喻体魄强健或意志十分坚定。",
            "example": "长年苦练，使他练就钢筋铁骨之身。"
        },
        4555: {
            "pinyin": "gāo àn shēn gǔ",
            "meaning": "高高的河岸、深深的山谷，形容地势险要，也比喻世事变迁。",
            "example": "江山几度更替，早已高岸深谷，人事全非。"
        },
        4556: {
            "pinyin": "gāo ào zì dà",
            "meaning": "极其骄傲，自以为了不起。",
            "example": "他高傲自大，终究难以服众。"
        },
        4557: {
            "pinyin": "gāo bù chéng dī bù jiù",
            "meaning": "高的职位够不上，低的工作又不肯做，形容好高骛远、不切实际。",
            "example": "求职若一味高不成低不就，只会错失良机。"
        },
        4558: {
            "pinyin": "gāo bù kě pān",
            "meaning": "高得无法攀登，比喻地位尊贵或条件过高，难以企及。",
            "example": "他在业界声望极高，几乎令人高不可攀。"
        },
        4559: {
            "pinyin": "gāo bù yún qú",
            "meaning": "高高地行走在通天的大道上，比喻位居高官显爵或科举及第。",
            "example": "他一举成名，自此高步云衢。"
        },
        4560: {
            "pinyin": "gāo cái jié zú",
            "meaning": "既有高才又脚程敏捷，比喻才智出众、行动迅速的人。",
            "example": "这些高材捷足的青年，很快就在行业中脱颖而出。"
        },
        4561: {
            "pinyin": "gāo cái jí zú",
            "meaning": "才智出众、行动敏捷的人。",
            "example": "在同辈中，他算得上高材疾足。"
        },
        4562: {
            "pinyin": "gāo chàng rù yún",
            "meaning": "歌声嘹亮高亢，仿佛直入云霄，也比喻极力称颂。",
            "example": "台上高唱入云，掌声经久不息。"
        },
        4563: {
            "pinyin": "gāo chē sì mǎ",
            "meaning": "高大的车子配以四马，形容显赫的车乘和尊贵的身份。",
            "example": "他昔日高车驷马出入宫门，今已风流云散。"
        },
        4564: {
            "pinyin": "gāo chéng shēn chí",
            "meaning": "城墙高峻、护城池深广，比喻防守坚固。",
            "example": "此城高城深池，易守难攻。"
        },
        4565: {
            "pinyin": "gāo chū yì chóu",
            "meaning": "比别人高出一等或略胜一筹。",
            "example": "在同类作品中，这部小说明显高出一筹。"
        },
        4566: {
            "pinyin": "gāo dǎo yuǎn jǔ",
            "meaning": "超然隐退，远离尘俗，多用来形容隐居避世。",
            "example": "战乱之际，不少文人高蹈远举，隐居山林。"
        },
        4567: {
            "pinyin": "gāo fēi yuǎn jǔ",
            "meaning": "飞得很高，飞得很远，比喻远走高飞或前程远大。",
            "example": "他决意高飞远举，到海外闯荡。"
        },
        4568: {
            "pinyin": "gāo fēng liàng jié",
            "meaning": "高尚的品德和坚贞的节操。",
            "example": "先贤高风亮节，后人无不景仰。"
        },
        4569: {
            "pinyin": "gāo gāo zài shàng",
            "meaning": "位置或地位极高，也形容态度上居高临下、脱离群众。",
            "example": "领导干部切忌高高在上，不接地气。"
        },
        4570: {
            "pinyin": "gāo gē měng jìn",
            "meaning": "边唱边奋勇前进，比喻情绪高昂、迅猛推进。",
            "example": "在改革的大道上，人们高歌猛进。"
        },
        4571: {
            "pinyin": "gāo guān hòu lù",
            "meaning": "尊贵的官职和优厚的俸禄。",
            "example": "他并不贪图高官厚禄，只求问心无愧。"
        },
        4572: {
            "pinyin": "gāo guān bó dài",
            "meaning": "高冠阔带，指古代士大夫的服饰，借指读书人或做官的人。",
            "example": "堂上皆是高冠博带的名士。"
        },
        4573: {
            "pinyin": "gāo guān xiǎn jué",
            "meaning": "显赫的官职爵位。",
            "example": "他位居高官显爵，却仍不忘百姓冷暖。"
        },
        4574: {
            "pinyin": "gāo jié qīng fēng",
            "meaning": "高尚的节操和清廉的作风。",
            "example": "这位清官高节清风，为世人称道。"
        },
        4575: {
            "pinyin": "gāo mén dà hù",
            "meaning": "门第高贵、家业宏大的家庭。",
            "example": "他出身高门大户，却性情平和。"
        },
        4576: {
            "pinyin": "gāo míng dà xìng",
            "meaning": "声名显赫的家族或姓氏。",
            "example": "此地多高名大姓，世代簪缨。"
        },
        4577: {
            "pinyin": "gāo nì dà tán",
            "meaning": "仰首高视而侃侃而谈，形容议论高超不凡或气概昂扬。",
            "example": "几位学者高睨大谈，纵论天下形势。"
        },
        4578: {
            "pinyin": "gāo péng mǎn zuò",
            "meaning": "座位上坐满了贵宾、好友，形容宾客众多而且尊贵。",
            "example": "喜宴之上，高朋满座，其乐融融。"
        },
        4579: {
            "pinyin": "gāo qíng yuǎn zhì",
            "meaning": "情趣高雅，志向远大。",
            "example": "他高情远致，不屑于流俗交往。"
        },
        4580: {
            "pinyin": "gāo rén yǎ shì",
            "meaning": "品格高尚、风度雅致的人。",
            "example": "席间多是高人雅士，谈笑皆成佳话。"
        },
        4581: {
            "pinyin": "gāo rén yì chóu",
            "meaning": "比别人高明一等或略胜一筹。",
            "example": "论棋艺，他总是高人一筹。"
        },
        4582: {
            "pinyin": "gāo rén yī děng",
            "meaning": "地位、才干或成绩比别人高出一等。",
            "example": "她在专业领域可谓高人一等。"
        },
        4583: {
            "pinyin": "gāo shān jǐng xíng",
            "meaning": "比喻崇高的德行，值得效法。",
            "example": "先贤之德，真可谓高山景行。"
        },
        4584: {
            "pinyin": "gāo shān liú shuǐ",
            "meaning": "原指琴曲名，后比喻知音难遇或高妙的艺术境界。",
            "example": "若无知音，再妙的曲子也难成高山流水。"
        },
        4585: {
            "pinyin": "gāo shān yǎng zhǐ",
            "meaning": "像仰望高山那样敬仰卓越的德行。",
            "example": "读其行谊，只觉高山仰止。"
        },
        4586: {
            "pinyin": "gāo shēn mò cè",
            "meaning": "高深得无法推测，形容事物或道理非常奥妙难懂。",
            "example": "这门学问非专心钻研，实在高深莫测。"
        },
        4587: {
            "pinyin": "gāo shì hài sú",
            "meaning": "品行或言论远远超出流俗，因而使世人惊异。",
            "example": "他的见解高世骇俗，却也发人深省。"
        },
        4588: {
            "pinyin": "gāo shì kuò bù",
            "meaning": "抬头阔步，形容趾高气扬的样子。",
            "example": "他高视阔步，毫不把旁人放在眼里。"
        },
        4589: {
            "pinyin": "gāo sǒng rù yún",
            "meaning": "高高耸立，直入云霄。",
            "example": "群峰高耸入云，气象万千。"
        },
        4590: {
            "pinyin": "gāo tái guì shǒu",
            "meaning": "多作求情用语，请人网开一面、从宽处理。",
            "example": "此事皆我之过，还望诸位高抬贵手。"
        },
        4591: {
            "pinyin": "gāo tán hóng lùn",
            "meaning": "议论高明，论述宏大。",
            "example": "几位学者高谈弘论，气氛热烈。"
        },
        4592: {
            "pinyin": "gāo tán kuò lùn",
            "meaning": "说话时夸夸其谈、议论甚多，多含贬义。",
            "example": "空有高谈阔论，若无实干终成空话。"
        },
        4593: {
            "pinyin": "gāo tán xióng biàn",
            "meaning": "纵论时事，口若悬河，形容善于言辞、辩才出众。",
            "example": "他在会上高谈雄辩，令人叹服。"
        },
        4594: {
            "pinyin": "gāo wèi hòu lù",
            "meaning": "高的职位和优厚的俸禄。",
            "example": "他轻视高位厚禄，只愿潜心学问。"
        },
        4595: {
            "pinyin": "gāo wén diǎn cè",
            "meaning": "重要的文书诏令或典籍，也泛指高妙的文章著作。",
            "example": "先贤高文典册，至今仍被反复研读。"
        },
        4596: {
            "pinyin": "gāo wò dōng shān",
            "meaning": "典出谢安高卧东山，后指隐居不仕或暂避世务。",
            "example": "他暂且高卧东山，以待时机再出。"
        },
        4597: {
            "pinyin": "gāo wū jiàn líng",
            "meaning": "从高屋往下倒水，比喻所向披靡、居高临下掌握全局。",
            "example": "此役我军居上游之势，如高屋建瓴。"
        },
        4598: {
            "pinyin": "gāo xià zài xīn",
            "meaning": "高低、优劣怎样，自己心里清楚。",
            "example": "作品好坏如何，作者自当高下在心。"
        },
        4599: {
            "pinyin": "gāo xiáng yuǎn yǐn",
            "meaning": "飞得很高而远远飞去，比喻远遁他乡或超然远引。",
            "example": "战乱将起，他高翔远引，隐居海上。"
        },
        4600: {
            "pinyin": "gāo xuán qín jìng",
            "meaning": "传说秦国有能照见善恶的明镜，后以高悬秦镜比喻执法公正、鉴察严明。",
            "example": "为官者当高悬秦镜，明辨是非。"
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

    print(f"已为 4501–4600 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
