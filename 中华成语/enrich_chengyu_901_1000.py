import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 为 901–1000 条成语添加拼音、释义和例句
    enrich = {
        # TODO: 填充 901–1000 号成语的详细信息
        901: {
            "pinyin": "bù chéng qì",
            "meaning": "不能成才做器，比喻人成不了有用的人。",
            "example": "他若再这样游手好闲，将来恐怕不成器。"
        },
        902: {
            "pinyin": "bù chéng sān wǎ",
            "meaning": "连三片瓦都凑不成，形容房屋极其破败，亦比喻事情一团糟。",
            "example": "这处老宅早已不成三瓦，早该翻修了。"
        },
        903: {
            "pinyin": "bù chéng tǐ tǒng",
            "meaning": "不合礼法规矩，没有应有的体统和样子。",
            "example": "他在会上大吵大闹，实在不成体统。"
        },
        904: {
            "pinyin": "bù chěng zhī tú",
            "meaning": "指泄愤生事的坏人，多为心怀不满而胡作非为之徒。",
            "example": "这些不逞之徒到处闹事，影响了社会秩序。"
        },
        905: {
            "pinyin": "bù chī yān huǒ shí",
            "meaning": "不吃人间烟火，比喻超凡脱俗，不食人间烟火的神仙或人物。",
            "example": "画中的仙子仿佛不吃烟火食，飘然若仙。"
        },
        906: {
            "pinyin": "bù chī bù lóng",
            "meaning": "不痴也不聋，原意指过分聪明反不利家庭和睦，常与“不过家翁”连用。",
            "example": "俗话说不痴不聋，不作家翁，提醒人凡事别过于计较。"
        },
        907: {
            "pinyin": "bù chǐ xià wèn",
            "meaning": "不以向地位或学问比自己低的人请教为可耻，形容虚心好学。",
            "example": "真正有学问的人从来不耻下问。"
        },
        908: {
            "pinyin": "bù chǐ yú rén",
            "meaning": "为人所不齿，被众人鄙视。",
            "example": "他背信弃义的行为，早已不齿于人。"
        },
        909: {
            "pinyin": "bù chǐ zuì hòu",
            "meaning": "不以得名次在最后为可耻，强调重在尽力而为。",
            "example": "比赛中要拼尽全力，不耻最后。"
        },
        910: {
            "pinyin": "bù chì tiān yuān",
            "meaning": "相差就像天空和深渊那样遥远，比喻差别极大。",
            "example": "两人的实力相比，不啻天渊。"
        },
        911: {
            "pinyin": "bù chǒu bù cǎi",
            "meaning": "既不正眼看，也不理睬，形容冷淡和轻视。",
            "example": "他说了半天，对方却不瞅不睬。"
        },
        912: {
            "pinyin": "bù chū suǒ liào",
            "meaning": "事态的发展如同事先预料的一样。",
            "example": "结果不出所料，他又一次取得了第一名。"
        },
        913: {
            "pinyin": "bù chuǎi mào mèi",
            "meaning": "自谦之词，指自己没有揣摩周到，却冒昧行事或说话。",
            "example": "不揣冒昧，特来请教，还望多多指正。"
        },
        914: {
            "pinyin": "bù cí ér bié",
            "meaning": "没有打招呼就离开，指不告而别。",
            "example": "他悄悄收拾行李，不辞而别。"
        },
        915: {
            "pinyin": "bù cí láo kǔ",
            "meaning": "不推辞辛劳和苦楚，形容任劳任怨。",
            "example": "为了集体利益，他总是不辞劳苦，冲在前面。"
        },
        916: {
            "pinyin": "bù cì zhī qiān",
            "meaning": "不按通常品级次第升迁，指破格提拔。",
            "example": "他贡献突出，被破格擢升，不次之迁。"
        },
        917: {
            "pinyin": "bù cún jiè dì",
            "meaning": "心中没有一点隔阂和嫌隙。",
            "example": "既然把话说开了，双方都不存芥蒂了。"
        },
        918: {
            "pinyin": "bù dǎ bù chéng xiāng shí",
            "meaning": "不打架就成不了朋友，形容先有矛盾后又和好的关系。",
            "example": "他们小时候时常打架，长大后反而成了好朋友，真是“不打不成相识”。"
        },
        919: {
            "pinyin": "bù dǎ zì zhāo",
            "meaning": "不用拷打就自己招认，比喻事情不攻自破。",
            "example": "证据摆在面前，他只好不打自招。"
        },
        920: {
            "pinyin": "bù dài shī guī",
            "meaning": "不必用蓍草和龟甲占卜就可以知道，比喻事情显而易见。",
            "example": "这次改革利大于弊，不待蓍龟就能判断。"
        },
        921: {
            "pinyin": "bù dāng rén zǐ",
            "meaning": "旧时表示自己罪过极重或歉疚很深的自责之语。",
            "example": "若有半点虚言，情愿不当人子。"
        },
        922: {
            "pinyin": "bù dào huáng hé xīn bù sǐ",
            "meaning": "不到黄河边上心不死，比喻不到绝路不回头。",
            "example": "他一意孤行，真是不到黄河心不死。"
        },
        923: {
            "pinyin": "bù dé ér zhī",
            "meaning": "没法知道。",
            "example": "事情的真相究竟如何，目前还不得而知。"
        },
        924: {
            "pinyin": "bù dé qí suǒ",
            "meaning": "没有得到适当的安顿或位置。",
            "example": "人才若得不到合理安排，就会不得其所。"
        },
        925: {
            "pinyin": "bù dé rén xīn",
            "meaning": "得不到群众的拥护和支持。",
            "example": "这项苛刻的政策显然不得人心。"
        },
        926: {
            "pinyin": "bù dé shàn zhōng",
            "meaning": "不能有好的结局或下场。",
            "example": "作恶多端的人终究不得善终。"
        },
        927: {
            "pinyin": "bù dé yào lǐng",
            "meaning": "抓不住要点和关键。",
            "example": "他读书只看表面，难免不得要领。"
        },
        928: {
            "pinyin": "bù dé yǐ ér wéi zhī",
            "meaning": "出于无奈才这样做，迫不得已。",
            "example": "他签下这份协议也属不得已而为之。"
        },
        929: {
            "pinyin": "bù dēng dà yǎ zhī táng",
            "meaning": "作品格调不高，不能进入正式、高雅的场合。",
            "example": "这种段子只供茶余饭后解闷，不登大雅之堂。"
        },
        930: {
            "pinyin": "bù dòng shēng sè",
            "meaning": "面不改色、声音平静，形容沉着镇定。",
            "example": "他在危急关头仍不动声色，指挥若定。"
        },
        931: {
            "pinyin": "bù è ér yán",
            "meaning": "没有凶恶的神色却很严肃威严。",
            "example": "这位老者不恶而严，让人自觉收敛。"
        },
        932: {
            "pinyin": "bù èr fǎ mén",
            "meaning": "唯一正确的方法或门径。",
            "example": "勤学苦练是不二法门，别无捷径。"
        },
        933: {
            "pinyin": "bù fá qí rén",
            "meaning": "具有某种特征的人并不少见。",
            "example": "乐于助人的好同事在我们单位不乏其人。"
        },
        934: {
            "pinyin": "bù fá xiān lì",
            "meaning": "这样的事在以前就有不少例子。",
            "example": "类似做法在历史上不乏先例。"
        },
        935: {
            "pinyin": "bù fǎ cháng kě",
            "meaning": "不拘泥于成法，可以因时因事而变通。",
            "example": "治国用兵，不可拘泥一格，须不法常可。"
        },
        936: {
            "pinyin": "bù fǎ gǔ bù xiū jīn",
            "meaning": "既不效法古人，又不整治今世，比喻两边都做不好。",
            "example": "一味否定传统又不思进取，无异于不法古不修今。"
        },
        937: {
            "pinyin": "bù fěi bù fā",
            "meaning": "学生若不到想说却说不出的程度，就不要去启发他，出自孔子教学思想。",
            "example": "老师遵循不悱不发的原则，鼓励学生主动思考。"
        },
        938: {
            "pinyin": "bù fèi jiāng hé",
            "meaning": "像江河那样永不废绝，比喻作品或事业流传久远。",
            "example": "他的诗文影响深远，可谓不废江河。"
        },
        939: {
            "pinyin": "bù fèi chuī huī zhī lì",
            "meaning": "连吹一口气的力气都不用，比喻毫不费力。",
            "example": "对他来说，解决这个小问题不费吹灰之力。"
        },
        940: {
            "pinyin": "bù fēn bǐ cǐ",
            "meaning": "不分你我，形容关系亲密或态度公正。",
            "example": "老朋友之间谈钱也不必太计较，不分彼此。"
        },
        941: {
            "pinyin": "bù fēn xuān zhì",
            "meaning": "不分高低轻重，比喻对事物不加区别对待。",
            "example": "评价作品不能不分轩轾，一味一刀切。"
        },
        942: {
            "pinyin": "bù fēn zào bái",
            "meaning": "不分黑白，比喻不分是非曲直。",
            "example": "处理问题要公正，不能不分皂白乱下结论。"
        },
        943: {
            "pinyin": "bù fēn qīng hóng zào bái",
            "meaning": "不分青红皂白，比喻不问情由就加以责备或处理。",
            "example": "家长教育孩子不能不分青红皂白，一味责骂。"
        },
        944: {
            "pinyin": "bù fēn zhěn yù",
            "meaning": "不分界限和范围，比喻不分彼此或不讲界别。",
            "example": "在公共事务上，应各方协作，不分畛域。"
        },
        945: {
            "pinyin": "bù fèn bù qǐ",
            "meaning": "学生不到自己感到愤懑想说却说不出的程度就不启发，是孔子提出的教学原则。",
            "example": "老师讲究不愤不启，引导学生主动思考。"
        },
        946: {
            "pinyin": "bù fēng bù shā",
            "meaning": "祭祀时祭品不奢华也不简陋，比喻做事适中有度。",
            "example": "待客之道贵在不丰不杀，恰到好处即可。"
        },
        947: {
            "pinyin": "bù fú shāo mái",
            "meaning": "死者不肯顺服烧埋，比喻冤情未申，死者难以瞑目。",
            "example": "此案疑点重重，仿佛不伏烧埋一般。"
        },
        948: {
            "pinyin": "bù fú shuǐ tǔ",
            "meaning": "身体不适应当地的水土气候。",
            "example": "他初到高原，多少有些不服水土。"
        },
        949: {
            "pinyin": "bù fù zhòng wàng",
            "meaning": "不辜负大家的期望。",
            "example": "他在关键时刻挺身而出，果然不负众望。"
        },
        950: {
            "pinyin": "bù gǎi qí lè",
            "meaning": "环境变了也不改变自己的志趣和乐趣。",
            "example": "即使生活清贫，他仍不改其乐，潜心读书。"
        },
        951: {
            "pinyin": "bù gān cí fú",
            "meaning": "不甘心处在雌伏的位置，比喻不愿意屈居人下或沉寂无闻。",
            "example": "他年轻气盛，不甘雌伏，总想一展抱负。"
        },
        952: {
            "pinyin": "bù gān hòu rén",
            "meaning": "不甘心落在别人后面，形容争强好胜的态度。",
            "example": "他学习刻苦，不甘后人，每次考试都名列前茅。"
        },
        953: {
            "pinyin": "bù gān jì mò",
            "meaning": "不愿意清静寂寞，多指主动寻求表现或参与。",
            "example": "他向来不甘寂寞，总要找点事情做。"
        },
        954: {
            "pinyin": "bù gān shì ruò",
            "meaning": "不愿意表现得比对方弱。",
            "example": "对手连连加码，我方也不甘示弱。"
        },
        955: {
            "pinyin": "bù gān bù gà",
            "meaning": "形容处境或姿态既不自然又不舒服，显得尴尬。",
            "example": "他站在台上不知说什么好，显得不尴不尬。"
        },
        956: {
            "pinyin": "bù gǎn gào láo",
            "meaning": "不敢说自己辛劳，表示谦逊。",
            "example": "这些都是分内之事，我不敢告劳。"
        },
        957: {
            "pinyin": "bù gǎn gǒu tóng",
            "meaning": "不敢轻易赞同，多用于婉言表示不同意。",
            "example": "对这个看法，我不敢苟同。"
        },
        958: {
            "pinyin": "bù gǎn lüè měi",
            "meaning": "不敢把功劳据为己有。",
            "example": "这次获奖是团队的功劳，我不敢掠美。"
        },
        959: {
            "pinyin": "bù gǎn páng wù",
            "meaning": "不敢分心做别的事，比喻专心致志。",
            "example": "任务紧急，他不敢旁骛，全力以赴。"
        },
        960: {
            "pinyin": "bù gǎn wèn jīn",
            "meaning": "不敢探问情况，比喻不敢过问或介入某事。",
            "example": "那段往事他讳莫如深，旁人也不敢问津。"
        },
        961: {
            "pinyin": "bù gǎn yuè léi chí yī bù",
            "meaning": "连雷池一步都不敢跨过去，比喻不敢逾越界限或规矩。",
            "example": "在纪律面前，人人都不敢越雷池一步。"
        },
        962: {
            "pinyin": "bù gēn zhī lùn",
            "meaning": "没有根据的言论。",
            "example": "这种指责纯属不根之论，不值一驳。"
        },
        963: {
            "pinyin": "bù gōng zì pò",
            "meaning": "不用去攻打就自己瓦解，比喻言论或计划站不住脚，自然被否定。",
            "example": "这个谎言经不起推敲，很快就不攻自破。"
        },
        964: {
            "pinyin": "bù gòng dài tiān",
            "meaning": "不能同处一个天地，比喻仇恨极深。",
            "example": "杀父之仇，不共戴天。"
        },
        965: {
            "pinyin": "bù gǒu yán xiào",
            "meaning": "不随便说笑，形容人庄重严肃。",
            "example": "他为人一向不苟言笑，在单位很有威信。"
        },
        966: {
            "pinyin": "bù gǔ bù jīn",
            "meaning": "既不像古代又不像现代，形容式样或做法不伦不类。",
            "example": "这栋楼的设计不古不今，看上去颇为别扭。"
        },
        967: {
            "pinyin": "bù guān jǐn yào",
            "meaning": "关系不大，不太重要。",
            "example": "这些都是不关紧要的小事，先把主问题解决。"
        },
        968: {
            "pinyin": "bù guān tòng yǎng",
            "meaning": "同自己的痛痒无关，比喻事不关己。",
            "example": "公共问题不能总当成不关痛痒的事情。"
        },
        969: {
            "pinyin": "bù guǎn bù gù",
            "meaning": "什么都不管，也不顾及后果。",
            "example": "他一气之下不管不顾地摔门而去。"
        },
        970: {
            "pinyin": "bù guǎn sān qī èr shí yī",
            "meaning": "不问三七二十一，比喻不顾情由和后果，鲁莽行事。",
            "example": "他不管三七二十一，先把事情顶了下来。"
        },
        971: {
            "pinyin": "bù guǐ zhī tú",
            "meaning": "不守法纪的人，多指图谋不轨之辈。",
            "example": "这伙不轨之徒终被警方一网打尽。"
        },
        972: {
            "pinyin": "bù guò ěr ěr",
            "meaning": "不过如此而已，表示很平常、不值得夸耀。",
            "example": "这点成绩算不得什么，不过尔尔。"
        },
        973: {
            "pinyin": "bù hán ér lì",
            "meaning": "天气并不寒冷却冷得发抖，比喻非常恐惧。",
            "example": "想到那场灾难，至今回忆起来仍不寒而栗。"
        },
        974: {
            "pinyin": "bù hé shí yí",
            "meaning": "与当时的风尚或需要不相适合。",
            "example": "这种老套的做法早已不合时宜。"
        },
        975: {
            "pinyin": "bù hēng bù hā",
            "meaning": "既不出声赞成也不出声反对，形容沉默不语。",
            "example": "问到他的意见时，他只是笑笑，不哼不哈。"
        },
        976: {
            "pinyin": "bù huān ér sàn",
            "meaning": "聚会或会谈在不愉快的气氛中结束。",
            "example": "两国谈判因分歧过大而不欢而散。"
        },
        977: {
            "pinyin": "bù huì zhī mén",
            "meaning": "允许人们直言无讳地进谏的门庭。",
            "example": "古代明君多开不讳之门，广纳谏言。"
        },
        978: {
            "pinyin": "bù huò zhī nián",
            "meaning": "指四十岁，出自孔子“ 四十而不惑 ”。",
            "example": "到了不惑之年，他的人生目标更加清晰。"
        },
        979: {
            "pinyin": "bù jī zhī cái",
            "meaning": "性情不受拘束而有才华的人。",
            "example": "他是个不羁之才，需要宽松的环境发挥所长。"
        },
        980: {
            "pinyin": "bù jī zhī mín",
            "meaning": "不受约束的民众，多指桀骜不驯之民。",
            "example": "若治理不当，恐使百姓成为不羁之民。"
        },
        981: {
            "pinyin": "bù jí zhī fǎ",
            "meaning": "法律不能追溯既往之人或既成之事。",
            "example": "制定新规时要考虑不及之法的原则。"
        },
        982: {
            "pinyin": "bù jí bù lí",
            "meaning": "既不贴近也不远离，比喻态度持中，不亲不疏。",
            "example": "他与同事相处不即不离，保持着合适的距离。"
        },
        983: {
            "pinyin": "bù jí zhī wù",
            "meaning": "并不紧迫的事务。",
            "example": "可以先处理要紧的事，不急之务往后放一放。"
        },
        984: {
            "pinyin": "bù jí bù xú",
            "meaning": "不快不慢，形容节奏适中、从容稳重。",
            "example": "他讲课不疾不徐，条理清晰。"
        },
        985: {
            "pinyin": "bù jì qí shù",
            "meaning": "多得数不清。",
            "example": "天上的星星不计其数。"
        },
        986: {
            "pinyin": "bù jiǎ sī suǒ",
            "meaning": "不用费心思考，立即做出反应。",
            "example": "他不假思索地答应了下来。"
        },
        987: {
            "pinyin": "bù jià bù sè",
            "meaning": "既不播种也不收获，比喻只坐享其成，不劳而获。",
            "example": "他一向游手好闲，想不稼不穑却有好日子过。"
        },
        988: {
            "pinyin": "bù jiàn guān cái bù luò lèi",
            "meaning": "不到看见棺材不流泪，比喻不到最后关头不肯回头。",
            "example": "他一再劝告朋友，却是不见棺材不落泪。"
        },
        989: {
            "pinyin": "bù jiàn jīng zhuàn",
            "meaning": "经书传记中没有记载，比喻事情来历不明或少见。",
            "example": "这种说法在典籍中不见经传，难以采信。"
        },
        990: {
            "pinyin": "bù jiàn tiān rì",
            "meaning": "见不到天日，比喻处境黑暗或遭受严酷压迫。",
            "example": "囚犯多年不见天日，身心备受折磨。"
        },
        991: {
            "pinyin": "bù jiāo bù zào",
            "meaning": "既不骄傲也不急躁，形容态度谦逊稳重。",
            "example": "成绩面前要不骄不躁，继续努力。"
        },
        992: {
            "pinyin": "bù jiào ér shā",
            "meaning": "不先进行教育就加以惩罚，多用来批评苛政。",
            "example": "古人认为不教而杀是暴政。"
        },
        993: {
            "pinyin": "bù jiào ér zhū",
            "meaning": "不加教化就施以刑罚，同“不教而杀”。",
            "example": "治理社会不能不教而诛，只重处罚不重教化。"
        },
        994: {
            "pinyin": "bù jiào zhī jiào",
            "meaning": "一种不着痕迹的教育方式，通过环境和潜移默化起作用。",
            "example": "家庭氛围本身就是一种不教之教。"
        },
        995: {
            "pinyin": "bù jiě zhī yuán",
            "meaning": "难以分开的缘分，多指人与人之间深厚的感情联系。",
            "example": "他们自相识起便结下不解之缘。"
        },
        996: {
            "pinyin": "bù jīn bù gǔ",
            "meaning": "既不像今也不像古，形容式样怪异或不伦不类。",
            "example": "这件衣服款式不今不古，穿出去有些怪。"
        },
        997: {
            "pinyin": "bù jīn bù fá",
            "meaning": "既不自夸也不贬低自己，形容谦逊而不张扬。",
            "example": "他向来不矜不伐，却深得同事尊敬。"
        },
        998: {
            "pinyin": "bù jìn rén qíng",
            "meaning": "不合乎人之常情，显得过于冷酷或刻板。",
            "example": "对方的做法过于生硬，难免让人觉得不近人情。"
        },
        999: {
            "pinyin": "bù jìn zé tuì",
            "meaning": "不前进就会后退，比喻形势不允许停滞。",
            "example": "在激烈竞争中，企业若不进则退。"
        },
        1000: {
            "pinyin": "bù jīng yī shì, bù zhǎng yī zhì",
            "meaning": "不经历一件事情，就增长不了一分见识。",
            "example": "人生许多道理，都是不经一事，不长一智才懂得的。"
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

    print(f"已为 901–1000 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
