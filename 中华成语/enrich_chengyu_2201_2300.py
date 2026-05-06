import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    enrich = {
        2201: {
            "pinyin": "cái bó zhì qiǎn",
            "meaning": "才智薄弱、见识浅陋，多用作自谦之辞。",
            "example": "我自知才薄智浅，只能略陈管见。"
        },
        2202: {
            "pinyin": "cái bó zhì shuāi",
            "meaning": "才能薄弱、体质衰弱，多为自谦或自伤之语。",
            "example": "他笑言自己材薄质衰，不堪重任。"
        },
        2203: {
            "pinyin": "cái dé jiān bèi",
            "meaning": "才能与德行都很完备。",
            "example": "这位学者可谓材德兼备，深受后辈敬重。"
        },
        2204: {
            "pinyin": "cái jù zhì dà",
            "meaning": "才能出众而志向宏大。",
            "example": "少年时的他就已材剧志大，胸怀天下。"
        },
        2205: {
            "pinyin": "cái mào xíng jié",
            "meaning": "才能茂盛、品行高洁。",
            "example": "祖父一生材茂行洁，为乡里所称道。"
        },
        2206: {
            "pinyin": "cái mào xíng xié",
            "meaning": "与“材茂行洁”同义，形容才高行洁。",
            "example": "史书中多有材茂行絜的贤臣名士。"
        },
        2207: {
            "pinyin": "cái qīng dé bó",
            "meaning": "才能浅、德行薄，多作自谦之语。",
            "example": "他屡屡表示自己材轻德薄，不敢当此美誉。"
        },
        2208: {
            "pinyin": "cái shì liàn bīng",
            "meaning": "指勇敢的士卒、精锐的兵马。",
            "example": "只要选出几队材士练兵，足以守住险关。"
        },
        2209: {
            "pinyin": "cái shū zhì dà",
            "meaning": "才能疏浅而志向很大，多含自讽之意。",
            "example": "空有一腔热血，却终究材疏志大，难成大事。"
        },
        2210: {
            "pinyin": "cái xióng dé mào",
            "meaning": "才能雄厚、德行茂盛。",
            "example": "历代名相多是材雄德茂之士。"
        },
        2211: {
            "pinyin": "cái xiǔ xíng huì",
            "meaning": "才能衰朽、品行污秽，形容人德才极差。",
            "example": "此人材朽行秽，却仍窃据高位。"
        },
        2212: {
            "pinyin": "cái yōu gàn jì",
            "meaning": "才能优异，又善于办事，极有干才。",
            "example": "他在几次危机中表现出材优干济的一面。"
        },
        2213: {
            "pinyin": "cái bù lòu bái",
            "meaning": "钱财不可显露于外，比喻要谨慎，不要炫富。",
            "example": "做生意的人更应牢记财不露白之理。"
        },
        2214: {
            "pinyin": "cān luán yù hè",
            "meaning": "驾着鸾鸟与仙鹤，比喻飞升成仙，亦用作人死的婉辞。",
            "example": "诗中写道他骖鸾驭鹤而去，寄托了无尽哀思。"
        },
        2215: {
            "pinyin": "cān fēng sì xiá",
            "meaning": "驾风驾霞，形容行走迅疾或仙人往来。",
            "example": "神话故事里的神仙总是骖风驷霞，来去如电。"
        },
        2216: {
            "pinyin": "cān fēng niè xuě",
            "meaning": "吃风啮雪，形容在外漂泊受冻、生活极其艰辛。",
            "example": "戍边将士餐风啮雪，只为守护一方安宁。"
        },
        2217: {
            "pinyin": "cān fēng rú xuě",
            "meaning": "以风代食、以雪充饥，形容在外备受饥寒之苦。",
            "example": "他年轻时餐风茹雪，四处奔波谋生。"
        },
        2218: {
            "pinyin": "cān fēng sù cǎo",
            "meaning": "以风为食、睡卧草间，形容旅途艰辛或生活清苦。",
            "example": "探险队一路餐风宿草，只为完成科考任务。"
        },
        2219: {
            "pinyin": "cān fēng sù lù",
            "meaning": "以风为食、卧宿露地，形容行旅辛苦、居无定所。",
            "example": "流亡之民餐风宿露，情状令人酸楚。"
        },
        2220: {
            "pinyin": "cān fēng sù shuǐ",
            "meaning": "以风为食、栖宿水边，形容行程艰难困苦。",
            "example": "他们沿江赶路，几日来都是餐风宿水。"
        },
        2221: {
            "pinyin": "cān fēng sù yǔ",
            "meaning": "风里吃、雨中宿，形容长途跋涉的辛劳。",
            "example": "红军战士餐风宿雨，仍咬牙翻越雪山草地。"
        },
        2222: {
            "pinyin": "cān fēng yàn lù",
            "meaning": "以风为食、咽露充饥，形容修道者或旅人生活清苦。",
            "example": "古时高士多在山林餐风咽露，不问世事。"
        },
        2223: {
            "pinyin": "cān fēng yǐn lù",
            "meaning": "以风为食，以露为饮，常形容隐士或神仙的生活。",
            "example": "传说中的仙人餐风饮露，与世相隔。"
        },
        2224: {
            "pinyin": "cān pā yǐn lù",
            "meaning": "吃花朵、饮露水，比喻高洁超逸的生活。",
            "example": "诗人笔下的仙子餐葩饮露，不食人间烟火。"
        },
        2225: {
            "pinyin": "cān sōng dàn bǎi",
            "meaning": "吃松子、啖柏实，形容隐居山林、生活简朴。",
            "example": "古代许多高士终身餐松啖柏，以清修自守。"
        },
        2226: {
            "pinyin": "cān sōng yǐn jiàn",
            "meaning": "吃松子、饮山涧之水，形容寄身山林、淡泊自甘。",
            "example": "他向往那种餐松饮涧的隐逸生活。"
        },
        2227: {
            "pinyin": "cān xiá shù xiè",
            "meaning": "餐霞光、漱夜露，比喻神仙般清虚高洁的生活。",
            "example": "画中的仙人餐霞漱瀣，飘然出尘。"
        },
        2228: {
            "pinyin": "cān xiá xī lù",
            "meaning": "吸食朝霞、饮露为生，比喻超尘脱俗的境界。",
            "example": "古书每言真人餐霞吸露，以示道行高深。"
        },
        2229: {
            "pinyin": "cān xiá yǐn jǐng",
            "meaning": "以彩霞为食、以日光为饮，比喻仙人或高士的生活。",
            "example": "诗句写他餐霞饮景，出入云端之间。"
        },
        2230: {
            "pinyin": "cān xiá yǐn xiè",
            "meaning": "吃霞饮露，形容清虚自守或神仙生活。",
            "example": "道人终日餐霞饮瀣，不问人间荣辱。"
        },
        2231: {
            "pinyin": "cān xiá yǐn yè",
            "meaning": "以霞为食、饮玉液，比喻神仙生活或超然物外的境界。",
            "example": "传说中他隐居深山，餐霞饮液，寿与天齐。"
        },
        2232: {
            "pinyin": "cān yún wò shí",
            "meaning": "餐云卧石，形容山林隐居、生活清苦。",
            "example": "这位高僧甘于餐云卧石，一心修行。"
        },
        2233: {
            "pinyin": "cán biān liè jiǎn",
            "meaning": "残缺的书编与竹简，比喻残存的文献资料。",
            "example": "考古人员从残编裂简中梳理出一段历史。"
        },
        2234: {
            "pinyin": "cán piān duàn jiǎn",
            "meaning": "残缺的篇章和断裂的竹简，比喻零散的古籍文献。",
            "example": "这些残篇断简对研究先秦史极有价值。"
        },
        2235: {
            "pinyin": "cán tāng shèng fàn",
            "meaning": "吃剩的汤和多余的饭，比喻无足轻重或不被重视的东西。",
            "example": "他只分到些残汤剩饭，却仍默默付出。"
        },
        2236: {
            "pinyin": "cán zhāng duàn jiǎn",
            "meaning": "残缺的章节和断裂的竹简，比喻散佚不全的典籍。",
            "example": "学者们从残章断简中缀合出完整的文献体系。"
        },
        2237: {
            "pinyin": "cán cóng niǎo dào",
            "meaning": "蜀地古道，险峻如鸟行，比喻道路异常艰险。",
            "example": "古人形容蜀道为蚕丛鸟道，可见其崎岖难行。"
        },
        2238: {
            "pinyin": "cǎn bù rěn yán",
            "meaning": "悲惨得让人不忍说起。",
            "example": "战后的景象实在惨不忍言。"
        },
        2239: {
            "pinyin": "cǎn dàn jīng yíng",
            "meaning": "处境清苦却竭力经营，多形容创业或办事业的艰难。",
            "example": "他靠一间小铺惨澹经营，终于闯出名堂。"
        },
        2240: {
            "pinyin": "cǎn lǜ chóu hóng",
            "meaning": "本指衣饰颜色，后多形容因愁苦而看繁华景物也觉凄凉。",
            "example": "失恋之后，她只觉春色如旧，却是惨绿愁红。"
        },
        2241: {
            "pinyin": "cǎn lǜ nián huá",
            "meaning": "指忧愁惆怅的青春年华。",
            "example": "他在日记中多次感叹自己这段惨绿年华。"
        },
        2242: {
            "pinyin": "cǎn rán bù lè",
            "meaning": "神情凄惨而不快乐。",
            "example": "老人自从妻子去世后，终日惨然不乐。"
        },
        2243: {
            "pinyin": "cǎn wú rén lǐ",
            "meaning": "残暴狠毒，全无人情道理。",
            "example": "那场屠杀行为简直是惨无人理。"
        },
        2244: {
            "pinyin": "cǎn wú tiān rì",
            "meaning": "悲惨到好像没有天日，形容极端黑暗残酷的处境。",
            "example": "在敌人的牢狱中，他度过了一段惨无天日的岁月。"
        },
        2245: {
            "pinyin": "cǎn yǔ suān fēng",
            "meaning": "凄冷的雨、刺骨的风，比喻环境恶劣或境遇悲凉。",
            "example": "他独自走在惨雨酸风的街头，倍感凄清。"
        },
        2246: {
            "pinyin": "càn rán yī xīn",
            "meaning": "焕然一新，形容面貌完全改变，显得光彩夺目。",
            "example": "翻修后的老街灿然一新，吸引了许多游客。"
        },
        2247: {
            "pinyin": "càn rán kě guān",
            "meaning": "光彩照人，值得一看。",
            "example": "新展开幕，作品众多，真是灿然可观。"
        },
        2248: {
            "pinyin": "cāng huáng wú cuò",
            "meaning": "匆忙慌乱，不知如何应付。",
            "example": "突遭变故，他一时间仓皇无措。"
        },
        2249: {
            "pinyin": "cāng hǎi yī lín",
            "meaning": "广大海洋中的一片鱼鳞，比喻极其渺小的一部分。",
            "example": "这些资料不过是沧海一鳞，仍需继续搜集。"
        },
        2250: {
            "pinyin": "cāng láng lǎo rén",
            "meaning": "古代隐士自号，后泛指隐居山林、不慕荣利的人。",
            "example": "他自称沧浪老人，以示不问功名。"
        },
        2251: {
            "pinyin": "cǎo yǎn fēng cóng",
            "meaning": "草随风倒，比喻下属顺从上意，风行草偃。",
            "example": "只要政策得当，自会草偃风从。"
        },
        2252: {
            "pinyin": "cǎo yǎn fēng xíng",
            "meaning": "像草随风而倒，形容政令一出，众人立即响应。",
            "example": "新规一经发布，便草偃风行。"
        },
        2253: {
            "pinyin": "cǎo yī mù shí",
            "meaning": "衣以草编，食以树木果实，形容生活极为清苦简朴。",
            "example": "先民在荒山野岭草衣木食，艰难谋生。"
        },
        2254: {
            "pinyin": "cè dá zhī xīn",
            "meaning": "怜悯别人的悲苦之心，指恻隐之心。",
            "example": "正是怀着恻怛之心，他创办了这所慈善学校。"
        },
        2255: {
            "pinyin": "cè mǎ fēi yú",
            "meaning": "驱策骏马、飞驰车舆，形容车马行驶迅疾。",
            "example": "使者昼夜策马飞舆，赶赴前线传递军令。"
        },
        2256: {
            "pinyin": "cè míng jiù liè",
            "meaning": "题名册上、就列班行，指取得功名、跻身仕途。",
            "example": "他高中进士，终于策名就列。"
        },
        2257: {
            "pinyin": "cè míng wěi zhì",
            "meaning": "题名投效，委身听命，多指归附新主或投靠强者。",
            "example": "乱世之中，不少人选择策名委质，以求自保。"
        },
        2258: {
            "pinyin": "cè nú lì dùn",
            "meaning": "鞭策劣马、磨砺钝器，比喻勉励劣弱、奋发自强。",
            "example": "他常以策驽砺钝自勉，从不轻言放弃。"
        },
        2259: {
            "pinyin": "cè wán mó dùn",
            "meaning": "鞭策顽钝之材，比喻努力学习、磨炼才能。",
            "example": "只要肯策顽磨钝，愚钝之人也能有所成就。"
        },
        2260: {
            "pinyin": "chá chá ér míng",
            "meaning": "在细枝末节上过分用心，自以为明察。",
            "example": "为政者若只在小事上察察而明，反易失大道。"
        },
        2261: {
            "pinyin": "chá yán guān xíng",
            "meaning": "观察人的言语和行为，以了解其真实情况。",
            "example": "用人之道在于察言观行，而非只听一面之词。"
        },
        2262: {
            "pinyin": "chá yán guān sè",
            "meaning": "从对方面色表情中观察其心意。",
            "example": "他惯会察颜观色，总能揣摩上司心思。"
        },
        2263: {
            "pinyin": "chā ruò háo lí, miù yǐ qiān lǐ",
            "meaning": "差别看似只有毫厘，却会造成千里之谬，比喻开头一点差错，结果会造成巨大偏差。",
            "example": "科研数据若有偏差若毫厘，结论便可能谬以千里。"
        },
        2264: {
            "pinyin": "chā yǐ háo lí, miù yǐ qiān lǐ",
            "meaning": "在极细小的地方出差错，会导致极大的失误。",
            "example": "初始设定若差以毫厘，后续结果难免谬以千里。"
        },
        2265: {
            "pinyin": "chā zhī háo lí, shī zhī qiān lǐ",
            "meaning": "开始相差极微，结果却会失之千里，比喻小小差错会造成巨大后果。",
            "example": "航道校准必须精确，否则便会差之毫厘，失之千里。"
        },
        2266: {
            "pinyin": "chāi dōng qiáng bǔ xī qiáng",
            "meaning": "拆掉东墙去修补西墙，比喻顾此失彼、临时应付。",
            "example": "企业若只会拆东墙补西墙，终究难以根本扭亏。"
        },
        2267: {
            "pinyin": "chāi pái dào zì",
            "meaning": "把一个字拆开说成一句话的文字游戏。",
            "example": "他们酒席间拆牌道字，猜得不亦乐乎。"
        },
        2268: {
            "pinyin": "chāi xī bǔ dōng",
            "meaning": "拆掉西边补东边，比喻临时挪用，不能从根本上解决问题。",
            "example": "频繁借新还旧，只是拆西补东的权宜之计。"
        },
        2269: {
            "pinyin": "chái huǐ miè xìng",
            "meaning": "因居父母丧过度悲痛而骨瘦如柴，几乎伤及性命。",
            "example": "他守孝时几近柴毁灭性，感动了乡里众人。"
        },
        2270: {
            "pinyin": "chái lì bù ē",
            "meaning": "像直立的柴薪一样不屈曲，比喻为人正直，不阿附权贵。",
            "example": "他处事向来柴立不阿，从不随波逐流。"
        },
        2271: {
            "pinyin": "chái mǐ yóu yán",
            "meaning": "柴火、米粮、油盐等日常生活必需品，比喻平淡琐碎的家常生活。",
            "example": "婚姻终究要回到柴米油盐的现实里。"
        },
        2272: {
            "pinyin": "chái tiān gǎi wù",
            "meaning": "烧柴祭天、改变礼制，比喻改朝换代。",
            "example": "历史上的每一次柴天改物，都伴随着社会巨变。"
        },
        2273: {
            "pinyin": "chái tiān gǎi yù",
            "meaning": "烧柴祭天、改换佩玉，比喻改朝换代。",
            "example": "文中以柴天改玉暗指政权更迭。"
        },
        2274: {
            "pinyin": "chái hú zhī xīn",
            "meaning": "像豺狐一样的心肠，形容阴险残忍的本性。",
            "example": "这伙人豺狐之心昭然若揭。"
        },
        2275: {
            "pinyin": "chái hǔ sì nüè",
            "meaning": "像豺虎一样肆意残害，形容极端残暴。",
            "example": "侵略军在此地豺虎肆虐，民不聊生。"
        },
        2276: {
            "pinyin": "chái láng dāng lù",
            "meaning": "豺狼横在路上，比喻坏人当权用事。",
            "example": "若任由豺狼当路，百姓必将再次受苦。"
        },
        2277: {
            "pinyin": "chái láng dāng tú",
            "meaning": "与“豺狼当路”同义，比喻恶人当权。",
            "example": "那时豺狼当涂，忠良多遭陷害。"
        },
        2278: {
            "pinyin": "chái láng héng dào",
            "meaning": "豺狼横行道路之间，比喻强暴者横行天下。",
            "example": "战乱年代，豺狼横道，行人惶惶不安。"
        },
        2279: {
            "pinyin": "chái láng hǔ bào",
            "meaning": "豺狼、老虎、豹子，比喻残暴凶狠的人。",
            "example": "这些土匪简直是豺狼虎豹，人人谈之色变。"
        },
        2280: {
            "pinyin": "chái láng yě xīn",
            "meaning": "像豺狼一样的野心，比喻贪婪狠毒的欲望。",
            "example": "侵略者怀着豺狼野心，绝不会善罢甘休。"
        },
        2281: {
            "pinyin": "chān qián luò hòu",
            "meaning": "有人抢前有人落后，形容队列不整齐、秩序混乱。",
            "example": "排队购票时切不可搀前落后。"
        },
        2282: {
            "pinyin": "chān háng duó shì",
            "meaning": "跨行抢生意，比喻越权夺职或插手他人事务。",
            "example": "本是他分内之事，你却来搀行夺市，难免招人反感。"
        },
        2283: {
            "pinyin": "chán kǒu shuò jīn",
            "meaning": "讒言之口连金石都能熔化，比喻流言蜚语具有极大破坏力。",
            "example": "若不加辨别，谗口铄金，贤者也难免蒙冤。"
        },
        2284: {
            "pinyin": "chán yán nìng yǔ",
            "meaning": "谗毁的话和阿谀的话，泛指不实的毁誉之辞。",
            "example": "他从不轻信谗言佞语，总要反复求证。"
        },
        2285: {
            "pinyin": "chán shì diāo lóng",
            "meaning": "形容文章精美，足以流传后世。",
            "example": "这部著作被誉为禅世雕龙，影响深远。"
        },
        2286: {
            "pinyin": "chán xù zhān ní",
            "meaning": "比喻清净的禅心被尘世烦恼所染。",
            "example": "他本欲出家，却终为俗缘所缚，不免禅絮沾泥。"
        },
        2287: {
            "pinyin": "chán jiā bù qīng",
            "meaning": "缠绕夹杂在一起，难以分清头绪。",
            "example": "这桩旧案牵涉多人，早已缠夹不清。"
        },
        2288: {
            "pinyin": "chán mián chuáng rù",
            "meaning": "长期卧病在床，亦指沉溺于男女之事。",
            "example": "他因病缠绵床褥，经年不出。"
        },
        2289: {
            "pinyin": "chǎn yú qǔ róng",
            "meaning": "以谄媚阿谀来取悦于人，多指巴结有权势者。",
            "example": "他一味谄谀取容，早已失去同僚的尊重。"
        },
        2290: {
            "pinyin": "chǎn yáng guāng dà",
            "meaning": "充分阐发并使之发扬光大。",
            "example": "这本书旨在阐扬光大中华优秀传统文化。"
        },
        2291: {
            "pinyin": "chǎn yōu jué wēi",
            "meaning": "阐明幽深道理，发掘精微之处。",
            "example": "这篇论文对相关理论多有阐幽抉微之功。"
        },
        2292: {
            "pinyin": "chǎn yōu míng wēi",
            "meaning": "使幽深隐微的道理显露出来。",
            "example": "名家的讲解往往能阐幽明微，使人茅塞顿开。"
        },
        2293: {
            "pinyin": "chāng tíng lǚ shí",
            "meaning": "寄食于昌亭亭长，比喻寄人篱下、依人而食。",
            "example": "他早年在亲戚家昌亭旅食，境况颇为凄凉。"
        },
        2294: {
            "pinyin": "dá guān guì rén",
            "meaning": "地位显要的官员和尊贵的人物。",
            "example": "宴会上宾客多是达官贵人。"
        },
        2295: {
            "pinyin": "dá guān xiǎn huàn",
            "meaning": "显贵的高官。",
            "example": "他虽然位列达官显宦，却仍保持俭朴作风。"
        },
        2296: {
            "pinyin": "dá guān zhī mìng",
            "meaning": "高官通达人情世故，懂得安于天命，多用来自我安慰。",
            "example": "他自谓达官知命，晚年看得颇为淡然。"
        },
        2297: {
            "pinyin": "dá quán zhī biàn",
            "meaning": "善于权衡利害，懂得因时制宜地变通。",
            "example": "治国之道贵在达权知变，不可墨守成规。"
        },
        2298: {
            "pinyin": "dá rén zhī mìng",
            "meaning": "通达人理的人明白命运的不可勉强，出自《论语》。",
            "example": "他以达人知命自勉，对得失不再过分计较。"
        },
        2299: {
            "pinyin": "dá rán shī sè",
            "meaning": "因惊恐而脸色骤变。",
            "example": "听闻噩耗，他不由得怛然失色。"
        },
        2300: {
            "pinyin": "dá fēi suǒ wèn",
            "meaning": "回答的内容与人所问不相符合。",
            "example": "记者提问十分具体，他却总是答非所问。"
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

    print(f"已为 2201–2300 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
