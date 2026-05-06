import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 将 4201–4300 号成语的详细信息补充到 enrich 字典中
    enrich = {
        4201: {
            "pinyin": "fǎn guān nèi zhào",
            "meaning": "原为佛教语，指回过头来观照内心，后来多指自我反省。",
            "example": "每晚静坐片刻，返观内照一日言行，大有裨益。"
        },
        4202: {
            "pinyin": "fǎn lái fù qù",
            "meaning": "来来去去、反反复复，形容动作或事情多次重复。",
            "example": "他返来复去地斟酌这道题的解法。"
        },
        4203: {
            "pinyin": "fǎn lǎo guī tóng",
            "meaning": "本指衰老复还童稚，多用来形容衰老的人精神焕发，仿佛回到童年。",
            "example": "祖父练气功多年，步履轻健，几乎有返老归童之态。"
        },
        4204: {
            "pinyin": "fǎn pèi shōu fān",
            "meaning": "掉转马缰、收起船帆，比喻退归、引退。",
            "example": "功成身退，正是他此番返辔收帆的最好时机。"
        },
        4205: {
            "pinyin": "fǎn pú guī zhēn",
            "meaning": "由雕琢虚华回复到质朴真淳的本性或状态。",
            "example": "历经名利起伏之后，他渐悟当返璞归真。"
        },
        4206: {
            "pinyin": "fǎn pǔ guī zhēn",
            "meaning": "与“返璞归真”义近，指去除浮华，回到朴素真实的本来面目。",
            "example": "艺术创作到极处，往往又要返朴归真。"
        },
        4207: {
            "pinyin": "fǎn pǔ huán zhēn",
            "meaning": "由矫饰复归质朴真纯，多用来形容人品或艺术风格。",
            "example": "这部晚期作品风格平淡冲和，可谓返朴还真。"
        },
        4208: {
            "pinyin": "fǎn shì nèi zhào",
            "meaning": "回过头来反省观照自身，检查内心与言行。",
            "example": "学道之要，在于时时返视内照。"
        },
        4209: {
            "pinyin": "fǎn xié guī zhèng",
            "meaning": "抛弃邪恶道路，回到正道上来。",
            "example": "他最终痛改前非，返邪归正。"
        },
        4210: {
            "pinyin": "fàn fū sú zǐ",
            "meaning": "小商小贩和平常百姓，泛指社会下层普通人。",
            "example": "他常到市集间与贩夫俗子把酒闲谈。"
        },
        4211: {
            "pinyin": "fàn fū zào lì",
            "meaning": "小贩和皂隶，泛指社会地位低下的普通人。",
            "example": "此政若行，贩夫皁隶亦得其利。"
        },
        4212: {
            "pinyin": "fàn fū zào lì",
            "meaning": "同“贩夫皁隶”，指社会下层的百姓。",
            "example": "他出身贩夫皂隶，却胸怀天下。"
        },
        4213: {
            "pinyin": "fàn fū zōu zú",
            "meaning": "贩夫与驺卒，泛指地位卑微的平民百姓。",
            "example": "圣人之道，本为贩夫驺卒而设。"
        },
        4214: {
            "pinyin": "fàn guān yù jué",
            "meaning": "买卖官职爵位，指权势者贪赃卖官。",
            "example": "一旦贩官鬻爵之风盛行，必致朝纲败坏。"
        },
        4215: {
            "pinyin": "fàn jiàn mài guì",
            "meaning": "低价买进、高价卖出，以牟取暴利。",
            "example": "他投机倒把，专干贩贱卖贵的勾当。"
        },
        4216: {
            "pinyin": "fàn jiāo mǎi míng",
            "meaning": "通过广泛交往、奔走钻营来猎取名声。",
            "example": "真正的学问不在贩交买名，而在脚踏实地。"
        },
        4217: {
            "pinyin": "fàn cè bèi yè",
            "meaning": "指佛经。古时佛经多以梵文写在贝叶或经册上。",
            "example": "他潜心研读梵册贝叶，研求佛理。"
        },
        4218: {
            "pinyin": "fāng cān bìng lù",
            "meaning": "骖马并辔齐驱，比喻齐肩并进、地位相当。",
            "example": "两位青年才俊方骖并路，各擅胜场。"
        },
        4219: {
            "pinyin": "fāng lái wèi ài",
            "meaning": "恩泽或盛况刚刚来到，还没有停止，形容事物正在兴盛发展。",
            "example": "改革之利方来未艾，切莫半途而废。"
        },
        4220: {
            "pinyin": "fāng lǐng yuán guàn",
            "meaning": "方形衣领、圆形帽冠，泛指古代儒生的服饰，亦借指读书人。",
            "example": "堂上方领圆冠，济济多士。"
        },
        4221: {
            "pinyin": "fāng miàn dà ěr",
            "meaning": "方正的脸庞，大大的耳朵，旧时被认为是富贵之相。",
            "example": "他生得方面大耳，一派雍容气象。"
        },
        4222: {
            "pinyin": "fāng ruì huán záo",
            "meaning": "方形榫头难以嵌入圆形榫眼，比喻格格不入，不能相合。",
            "example": "性情迥异之人硬凑在一起，终究是方枘圜凿。"
        },
        4223: {
            "pinyin": "fāng táo pì lǐ",
            "meaning": "姿容可与桃李相比，形容容貌娇艳美丽。",
            "example": "她年少时方桃譬李，倾倒一时士子。"
        },
        4224: {
            "pinyin": "fāng tóu bù lǜ",
            "meaning": "形容性格倔强，固执己见，不合时宜。",
            "example": "他性情方头不律，劝说也听不进去。"
        },
        4225: {
            "pinyin": "fāng xīng wèi yǐ",
            "meaning": "事物正处在兴盛发展阶段，还没有停止。",
            "example": "科技创新方兴未已，新成果层出不穷。"
        },
        4226: {
            "pinyin": "fāng yán jǔ xíng",
            "meaning": "言谈举止方正合度，合乎规范。",
            "example": "他为人方言矩行，深得同僚敬重。"
        },
        4227: {
            "pinyin": "fāng yǐ lèi jù",
            "meaning": "同类事物自然聚在一起，比喻人或事物按性质分门别类。",
            "example": "所谓方以类聚，人以群分，交友尤当慎之。"
        },
        4228: {
            "pinyin": "fāng yuán kě shī",
            "meaning": "方也能用，圆也能用，比喻才艺多、用途广。",
            "example": "他学识渊博，方员可施，深得器重。"
        },
        4229: {
            "pinyin": "fāng zī wèi ài",
            "meaning": "形容事物正在发展，祸患或势头正日益增长，尚未止息。",
            "example": "弊政久不整顿，流弊方滋未艾。"
        },
        4230: {
            "pinyin": "fāng zú yuán lú",
            "meaning": "脚趾方正、头颅圆形，泛指芸芸众生。",
            "example": "茫茫宇宙之中，方足圆颅，不知凡几。"
        },
        4231: {
            "pinyin": "fáng huàn wèi méng",
            "meaning": "在祸患还没有萌芽之前就加以防备。",
            "example": "治国理政须防患未萌，不能坐失良机。"
        },
        4232: {
            "pinyin": "fàng hǔ yí huàn",
            "meaning": "放走老虎，留下祸患，比喻纵容恶人或隐患而留后患。",
            "example": "对腐败分子手软，无异于放虎遗患。"
        },
        4233: {
            "pinyin": "fàng huǒ shāo shān",
            "meaning": "字面指放火烧山，引申为做事不留余地，或煽风点火、挑拨离间。",
            "example": "他在旁边放火烧山，终于闹得两人决裂。"
        },
        4234: {
            "pinyin": "fàng làng bù jī",
            "meaning": "言行放纵，不受约束。",
            "example": "他生性放浪不羁，不愿受俗务羁绊。"
        },
        4235: {
            "pinyin": "fàng làng bù jū",
            "meaning": "放纵任性，不受礼法拘束，与“放浪不羁”义近。",
            "example": "她向来放浪不拘，行止洒脱。"
        },
        4236: {
            "pinyin": "fàng làng wú jī",
            "meaning": "放纵任性，不加检点，不受约束。",
            "example": "诗人多半放浪无羁，才情横溢。"
        },
        4237: {
            "pinyin": "fàng làng wú jū",
            "meaning": "放纵不受拘束，与“放浪不羁”同义。",
            "example": "他放浪无拘，游历四方。"
        },
        4238: {
            "pinyin": "fàng lěng jiàn",
            "meaning": "乘人不备暗中放箭，比喻背后中伤他人。",
            "example": "有话当面说，何必在背后放冷箭。"
        },
        4239: {
            "pinyin": "fàng lóng rù hǎi",
            "meaning": "把龙放入大海，比喻放走强敌，自留后患。",
            "example": "此举无异于放龙入海，将来恐难收拾。"
        },
        4240: {
            "pinyin": "fàng mǎ hòu pào",
            "meaning": "比喻事情已过才发议论或采取行动，已无补于事。",
            "example": "事先不提意见，如今再来放马后炮有何用处。"
        },
        4241: {
            "pinyin": "fàng mǎ huá yáng",
            "meaning": "指战事平定后不再用兵，比喻天下太平。",
            "example": "战乱平息，百姓盼望早日放马华阳。"
        },
        4242: {
            "pinyin": "fàng pì tiān fēng",
            "meaning": "比喻在旁助威，虽力量不大也能助长声势。",
            "example": "众人附和叫好，不过是放屁添风罢了。"
        },
        4243: {
            "pinyin": "fàng pì xié chǐ",
            "meaning": "行为荒淫放纵，邪僻奢侈。",
            "example": "人情足于财而无礼以节之，则易生放僻邪侈之风。"
        },
        4244: {
            "pinyin": "fàng pì yín yì",
            "meaning": "肆无忌惮地为非作歹，行为邪恶不正。",
            "example": "若纵容这班人放僻淫佚，必贻害一方。"
        },
        4245: {
            "pinyin": "fàng pō sā háo",
            "meaning": "形容举止粗野放纵，盛气凌人。",
            "example": "他仗势放泼撒豪，乡里人多避之不及。"
        },
        4246: {
            "pinyin": "fàng qíng qiū hè",
            "meaning": "纵情山水之间，不以世务为念。",
            "example": "谢公晚年多放情丘壑，淡于功名。"
        },
        4247: {
            "pinyin": "fàng xīn jiě tǐ",
            "meaning": "人心离散，组织瓦解。",
            "example": "赏罚不明，只会使属下放心解体。"
        },
        4248: {
            "pinyin": "fàng xīn tuō dǎn",
            "meaning": "心里十分踏实，有所倚仗而毫无顾虑。",
            "example": "有师长在旁指点，徒弟们自然放心托胆。"
        },
        4249: {
            "pinyin": "fàng yán gāo lùn",
            "meaning": "毫无顾忌地大发议论。",
            "example": "酒席间众人放言高论，各抒己见。"
        },
        4250: {
            "pinyin": "fàng yǎn shì jiè",
            "meaning": "放开眼界，纵观天下，不局限于狭小范围。",
            "example": "青年人要放眼世界，拓宽胸襟。"
        },
        4251: {
            "pinyin": "fàng yì sì zhì",
            "meaning": "纵情而行，任意施展志向，没有拘束。",
            "example": "登临远眺，不禁放意肆志，豪情满怀。"
        },
        4252: {
            "pinyin": "fēi liáng wǎn mò",
            "meaning": "同“飞芻挽粟”，形容急速运送粮草。",
            "example": "战事吃紧，各地飞粮挽秣，以供军需。"
        },
        4253: {
            "pinyin": "fēi liú duǎn cháng",
            "meaning": "散布谣言、闲话，中伤他人。",
            "example": "职场之中最忌飞流短长，伤人又害己。"
        },
        4254: {
            "pinyin": "fēi lóng chéng yún",
            "meaning": "飞龙乘云而上，比喻得势升腾，前途远大。",
            "example": "少年得志，宛若飞龙乘云。"
        },
        4255: {
            "pinyin": "fēi lóng zài tiān",
            "meaning": "源自《易经》，象征志得意满、地位显达。",
            "example": "他官运亨通，可谓飞龙在天。"
        },
        4256: {
            "pinyin": "fēi luán xiáng fèng",
            "meaning": "鸾凤飞翔，比喻夫妻恩爱或才艺出众的佳偶。",
            "example": "新人的才貌真如飞鸾翔凤，令人称羡。"
        },
        4257: {
            "pinyin": "fēi mǐ zhuǎn chú",
            "meaning": "比喻迅速运送粮草或物资。",
            "example": "后方飞米转刍，确保前线给养无虞。"
        },
        4258: {
            "pinyin": "fēi móu diào bàng",
            "meaning": "以流言蜚语阴谋中伤他人。",
            "example": "小人飞谋钓谤，妄图挑拨离间。"
        },
        4259: {
            "pinyin": "fēi móu jiàn bàng",
            "meaning": "同“飞谋钓谤”，指用谣言诋毁别人。",
            "example": "为官者当不畏飞谋荐谤，秉公而行。"
        },
        4260: {
            "pinyin": "fēi péng chéng fēng",
            "meaning": "蓬草随风飞转，比喻意志不定，随境遇而转变。",
            "example": "处世切莫如飞蓬乘风，缺乏主见。"
        },
        4261: {
            "pinyin": "fēi shā yáng lì",
            "meaning": "沙石被风卷起飞扬，形容风势十分强劲。",
            "example": "大漠深处狂风骤起，飞沙扬砾，行人难进。"
        },
        4262: {
            "pinyin": "fēi shā yáng lì",
            "meaning": "同“飞沙扬砾”，形容大风卷起沙石、声势骇人。",
            "example": "一阵飞砂扬砾，顿时天昏地暗。"
        },
        4263: {
            "pinyin": "fēi shā zhuǎn shí",
            "meaning": "沙土飞扬、石块滚动，形容风势狂暴。",
            "example": "山口狂风怒号，飞砂转石。"
        },
        4264: {
            "pinyin": "fēi shā zǒu shí",
            "meaning": "沙土飞扬、石块滚动，形容风力极大。",
            "example": "昨夜狂风大作，飞砂走石，屋瓦皆鸣。"
        },
        4265: {
            "pinyin": "fēi shāng zǒu jiǎ",
            "meaning": "与“飞觥走斝”同，形容宴饮时频频传杯、痛饮不已。",
            "example": "席间飞觞走斝，歌声笑语不绝于耳。"
        },
        4266: {
            "pinyin": "fēi shēng téng shí",
            "meaning": "飞腾而上，声名与实际成绩都迅速提高。",
            "example": "这几年他事业飞升腾实，令人称羡。"
        },
        4267: {
            "pinyin": "fēi shū zǒu xí",
            "meaning": "飞速传递文书檄文。",
            "example": "军情紧急，只得飞书走檄，调集诸路兵马。"
        },
        4268: {
            "pinyin": "fēi shuāng liù yuè",
            "meaning": "六月飞霜，比喻有冤情或冤狱。",
            "example": "此案若不昭雪，简直是飞霜六月。"
        },
        4269: {
            "pinyin": "fēi tǔ zhú hài",
            "meaning": "抛掷土丸以驱逐禽兽，引申为驱除祸患。",
            "example": "古人断竹续竹，飞土逐害，以护庄稼。"
        },
        4270: {
            "pinyin": "fēi tǔ zhú ròu",
            "meaning": "抛掷土丸驱逐禽兽，与“飞土逐害”同。",
            "example": "孩童在田间飞土逐肉，以防野兽伤人。"
        },
        4271: {
            "pinyin": "fēi wén rǎn hàn",
            "meaning": "挥笔疾书，文思泉涌。",
            "example": "他胸有成竹，下笔时真可谓飞文染翰。"
        },
        4272: {
            "pinyin": "fēi yán zǒu bì",
            "meaning": "旧小说中形容武艺高强，身法轻捷，能跃上屋檐、越过墙壁。",
            "example": "那侠客飞沿走壁，转瞬便不见了踪影。"
        },
        4273: {
            "pinyin": "fēi yán zǒu jǐ",
            "meaning": "同“飞檐走壁”，形容身手矫健、轻功高强。",
            "example": "他自夸飞檐走脊，夜入重门如履平地。"
        },
        4274: {
            "pinyin": "fēi yǎn chuán qíng",
            "meaning": "用眼神传递情意，多指男女之间暗送秋波。",
            "example": "两人隔座而坐，偶一飞眼传情，心意已然相通。"
        },
        4275: {
            "pinyin": "fēi yāng zǒu huò",
            "meaning": "意外从天而降的灾祸，同“飞来横祸”。",
            "example": "他无端卷入是非，实属飞殃走祸。"
        },
        4276: {
            "pinyin": "fēi yáng fú zào",
            "meaning": "举止轻浮急躁，不够沉稳。",
            "example": "做学问切忌飞扬浮躁，要踏踏实实。"
        },
        4277: {
            "pinyin": "fēi yīng bēn quǎn",
            "meaning": "放出鹰犬追捕猎物，指打猎。",
            "example": "贵族子弟终日飞鹰奔犬，不理政事。"
        },
        4278: {
            "pinyin": "fēi yīng zǒu mǎ",
            "meaning": "放鹰追捕、骑马奔驰，指打猎或纵情驰骋。",
            "example": "他虽年逾古稀，仍喜飞鹰走马。"
        },
        4279: {
            "pinyin": "fēi yīng zǒu quǎn",
            "meaning": "放出鹰和狗去追捕野兽，指打猎或骄奢游乐。",
            "example": "昔日权贵终日飞鹰走犬，荒废朝政。"
        },
        4280: {
            "pinyin": "fēi zhū jiàn yù",
            "meaning": "形容水珠飞溅，如同珠玉散落一般。",
            "example": "山涧瀑布飞珠溅玉，蔚为奇观。"
        },
        4281: {
            "pinyin": "fēi fèn zhī niàn",
            "meaning": "超出本分、不属分内的念头。",
            "example": "做人应安守本分，不可心存非分之念。"
        },
        4282: {
            "pinyin": "fēi tóng xún cháng",
            "meaning": "与平常不同，形容人或事物十分突出。",
            "example": "他的见解独到，实属非同寻常。"
        },
        4283: {
            "pinyin": "fēi wǎ bá mù",
            "meaning": "屋瓦被风掀起、树木被连根拔起，形容风力极大。",
            "example": "昨夜飓风蜚瓦拔木，村舍多有损毁。"
        },
        4284: {
            "pinyin": "fēi yīng téng mào",
            "meaning": "名声如英华飞扬，功业如草木茂盛，比喻声名事业日益兴盛。",
            "example": "他出道数年，已是蜚英腾茂，名实相副。"
        },
        4285: {
            "pinyin": "féi cháng mǎn nǎo",
            "meaning": "同“脑满肠肥”，形容不劳而食、养尊处优的人肥胖臃肿。",
            "example": "他终日无所事事，只把自己养得肥肠满脑。"
        },
        4286: {
            "pinyin": "féi dōng shòu nián",
            "meaning": "南宋吴地俗语，指冬至馈赠丰厚而年节反略显寒伧。",
            "example": "旧时江南有肥冬瘦年之说，冬至礼物远胜年节。"
        },
        4287: {
            "pinyin": "féi dùn míng gāo",
            "meaning": "肥：丰厚；遯：隐退；鸣高：标榜高节，指隐居而多有清名。",
            "example": "他功成之后肥遯鸣高，不再问世事。"
        },
        4288: {
            "pinyin": "féi gān qīng nuǎn",
            "meaning": "肥美的饮食、轻暖的衣物，泛指优裕安逸的生活。",
            "example": "古之君子仕进，并非为求一己之肥甘轻暖。"
        },
        4289: {
            "pinyin": "féi tóu dà miàn",
            "meaning": "形容人满脸肥肉、相貌肥胖，多含贬义。",
            "example": "他肥头大面，一副酒肉官模样。"
        },
        4290: {
            "pinyin": "féi tóu pàng ěr",
            "meaning": "形容人头脸肥胖、耳朵粗大。亦可指小孩肥胖可爱。",
            "example": "那孩童肥头胖耳，甚是讨喜。"
        },
        4291: {
            "pinyin": "féi yú dà ròu",
            "meaning": "肥美的鱼和大片的肉，形容饮食丰盛。",
            "example": "席上肥鱼大肉堆满一桌。"
        },
        4292: {
            "pinyin": "fěi cháo yī xī",
            "meaning": "不止一朝一夕，形容经历时间较长。",
            "example": "他勤学苦读，匪朝伊夕，终有所成。"
        },
        4293: {
            "pinyin": "fěi shí zhī xīn",
            "meaning": "比喻意志坚贞，不可动摇。",
            "example": "他以匪石之心守护誓言，从不食言。"
        },
        4294: {
            "pinyin": "fěi cè chán mián",
            "meaning": "心绪悲苦缠绵，难以排遣。",
            "example": "离别之后，他常觉悱恻缠绵，难以自解。"
        },
        4295: {
            "pinyin": "fěi rán xiàng fēng",
            "meaning": "众人闻风而纷纷归向，形容风气盛行、广受景仰。",
            "example": "他以德服人，士林斐然向风。"
        },
        4296: {
            "pinyin": "fěi rán xiàng fēng",
            "meaning": "同“斐然向风”，形容人们仰慕某种德行或风气而竞相归附。",
            "example": "儒学之盛，学子斐然乡风。"
        },
        4297: {
            "pinyin": "fèi qǐn wàng cān",
            "meaning": "顾不得睡觉，忘记吃饭，形容十分用功或专心。",
            "example": "他为备课常常废寝忘餐。"
        },
        4298: {
            "pinyin": "fèi rán ér fǎn",
            "meaning": "兴致全消、失望而回。",
            "example": "久候不见主事，只得废然而反。"
        },
        4299: {
            "pinyin": "fèi sī lì gōng",
            "meaning": "去除私心而维护公义。",
            "example": "为政者当能废私立公，不徇私情。"
        },
        4300: {
            "pinyin": "fèi fǎn lián tiān",
            "meaning": "形容人声喧嚣，如水沸般翻腾不息。",
            "example": "会场上人声鼎沸，沸反连天。"
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

    print(f"已为 4201–4300 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
