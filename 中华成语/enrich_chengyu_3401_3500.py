import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 将 3401–3500 号成语的详细信息补充到 enrich 字典中
    enrich = {
        3401: {
            "pinyin": "ā shì qǔ róng",
            "meaning": "迎合世俗风尚以求容身或取悦他人，多含贬义。",
            "example": "他为人处世一味阿世取容，渐渐失去了原则。"
        },
        3402: {
            "pinyin": "ē yì qǔ róng",
            "meaning": "曲意逢迎，以讨好他人来取得欢心。",
            "example": "在是非问题上绝不能阿意取容，否则只会助长歪风。"
        },
        3403: {
            "pinyin": "ē jīn niào yín",
            "meaning": "形容极其奢侈豪华的排场或生活。",
            "example": "古时某些权贵纵情声色，铺张到屙金溺银的地步。"
        },
        3404: {
            "pinyin": "é yǐ chuán é",
            "meaning": "用错误的说法去传播错误的消息，使谣言一再扩散。",
            "example": "网络上传言切勿讹以传讹，应当核实后再转发。"
        },
        3405: {
            "pinyin": "é yǐ zī é",
            "meaning": "以讹传讹，越传错误越多，使谣言愈演愈烈。",
            "example": "若任由讹以滋讹，最终只会扰乱人心。"
        },
        3406: {
            "pinyin": "é é tāng tāng",
            "meaning": "峨峨形容高耸雄伟，汤汤形容水势浩大，多用来形容山川形势壮阔。",
            "example": "这里山势峨峨汤汤，气象万千。"
        },
        3407: {
            "pinyin": "é é yáng yáng",
            "meaning": "形容高大雄伟、气势盛大。",
            "example": "宫阙峨峨洋洋，显示出帝都的宏伟气度。"
        },
        3408: {
            "pinyin": "é hú zhī huì",
            "meaning": "指宋代著名文人集会之事，后多用来泛指文人雅集。",
            "example": "这次学术研讨会堪比当年的鹅湖之会，群贤毕至。"
        },
        3409: {
            "pinyin": "é wáng zé rǔ",
            "meaning": "比喻选择精细、要求严格。",
            "example": "他在选材上如鹅王择乳般挑剔，只为保证作品质量。"
        },
        3410: {
            "pinyin": "é méi qín shǒu",
            "meaning": "蛾眉细长，螓首秀美，形容女子容貌娟秀动人。",
            "example": "画中女子蛾眉螓首，神情婉约。"
        },
        3411: {
            "pinyin": "é cù xīn tòng",
            "meaning": "额头紧皱、心中疼痛，形容忧愁悲痛之极。",
            "example": "望着灾区的景象，他不禁额蹙心痛，难以言表。"
        },
        3412: {
            "pinyin": "é shǒu chēng sòng",
            "meaning": "以手按额以示尊敬赞颂，形容十分钦佩或感激。",
            "example": "人们对这位好官额手称颂，口碑极佳。"
        },
        3413: {
            "pinyin": "é shǒu xiāng qìng",
            "meaning": "举手按额，彼此庆贺，形容因好消息而非常高兴。",
            "example": "听到孩子被录取的消息，一家人额手相庆。"
        },
        3414: {
            "pinyin": "é shǒu chēng qìng",
            "meaning": "举手按额表示庆贺，和“额手相庆”意义相近。",
            "example": "改革见到成效，百姓无不额首称庆。"
        },
        3415: {
            "pinyin": "é wài zhǔ shì",
            "meaning": "指不在正式名义上的主持者，或额外掌管实权的人。",
            "example": "表面上是他在当家，其实另有额外主事。"
        },
        3416: {
            "pinyin": "è jīn kòng yàn",
            "meaning": "揪住衣襟、掐住咽喉，比喻扼守要害，使对方难以脱身。",
            "example": "这座关隘扼襟控咽，是南北交通的咽喉所在。"
        },
        3417: {
            "pinyin": "è kàng fǔ bèi",
            "meaning": "掐住咽喉、抚拍脊背，比喻控制要害、掌握生杀大权。",
            "example": "一旦被人扼亢拊背，便只能任人摆布。"
        },
        3418: {
            "pinyin": "è wàn dǐ zhǎng",
            "meaning": "捶腕击掌，形容极度懊恼或激动。",
            "example": "看着计划功亏一篑，他只能扼腕抵掌，追悔莫及。"
        },
        3419: {
            "pinyin": "è wàn tàn xī",
            "meaning": "捶腕叹息，形容非常懊悔、痛惜或愤慨。",
            "example": "想起当年的错误决定，他不时扼腕叹息。"
        },
        3420: {
            "pinyin": "è chén wú rǎn",
            "meaning": "不为世俗尘垢所染，比喻品行高洁，不沾染污浊。",
            "example": "他身居闹市而恶尘无染，始终坚守原则。"
        },
        3421: {
            "pinyin": "è guàn yǐ yíng",
            "meaning": "形容罪恶已经累积到极点，与“恶贯满盈”相近。",
            "example": "此人罪行累累，早已恶贯已盈。"
        },
        3422: {
            "pinyin": "è jì zhāo zhuó",
            "meaning": "恶迹：坏行为；昭着：明显显著。指坏事做得很多，恶名远扬。",
            "example": "这伙人恶迹昭着，早成百姓深恶痛绝的对象。"
        },
        3423: {
            "pinyin": "è jí yíng zhǐ",
            "meaning": "坏事登记之多，手指数也数不过来，比喻罪恶累累。",
            "example": "贪官们恶籍盈指，怎能轻易饶恕。"
        },
        3424: {
            "pinyin": "è yán lì sè",
            "meaning": "说话语气粗暴、神色凶恶。",
            "example": "他总是恶言厉色，对下属毫不留情。"
        },
        3425: {
            "pinyin": "è yán lì cí",
            "meaning": "詈：骂。指恶毒的言辞和严厉的神色。",
            "example": "面对别人的过失，可以指出，但不必用恶言詈辞。"
        },
        3426: {
            "pinyin": "è yī fěi shí",
            "meaning": "粗劣的衣服和简薄的食物，形容生活清贫或刻苦朴素。",
            "example": "他宁甘恶衣菲食，也要把钱省下来做公益。"
        },
        3427: {
            "pinyin": "è yī shū shí",
            "meaning": "粗陋的衣服和蔬菜为食，形容节俭朴素的生活。",
            "example": "祖父一生恶衣蔬食，却乐于助人。"
        },
        3428: {
            "pinyin": "è yì zhòng shāng",
            "meaning": "出于恶意去诋毁、伤害他人名誉或感情。",
            "example": "在背后恶意中伤同事，不但缺德，也会毁了自己。"
        },
        3429: {
            "pinyin": "è zhí chǒu zhèng",
            "meaning": "说坏话丑化正直的人，或憎恶正直而袒护奸邪。",
            "example": "为一己私利而恶直丑正，终会失去众人的信任。"
        },
        3430: {
            "pinyin": "è piǎo zài dào",
            "meaning": "饿死的人的尸体满路都是，形容灾荒极为严重。",
            "example": "古籍中记载，当年饿莩载道，景象凄惨。"
        },
        3431: {
            "pinyin": "ēn tóng shān yuè",
            "meaning": "恩德像高山大岳一样深重。",
            "example": "师长待他恩同山岳，他一直铭记在心。"
        },
        3432: {
            "pinyin": "ēn wēi bìng yòng",
            "meaning": "恩惠与威严并行使用。",
            "example": "治理地方要恩威并用，既关爱百姓又严明法纪。"
        },
        3433: {
            "pinyin": "ér nǚ qīn jiā",
            "meaning": "儿女双方成为亲家，或指两家因婚姻而结成的亲戚关系。",
            "example": "两家本就来往密切，如今更成了儿女亲家。"
        },
        3434: {
            "pinyin": "ér nǚ zhī qíng",
            "meaning": "指男女之间的情爱，或对子女的感情。",
            "example": "他性情柔软，常被儿女之情所牵绊。"
        },
        3435: {
            "pinyin": "ér jīn ér hòu",
            "meaning": "从现在起直到以后，表示时间上的转折与延续。",
            "example": "而今而后，他决心痛改前非。"
        },
        3436: {
            "pinyin": "ěr rǔ zhī jiāo",
            "meaning": "你我相称为“尔”“汝”，形容彼此关系极为亲密。",
            "example": "两人自小青梅竹马，是典型的尔汝之交。"
        },
        3437: {
            "pinyin": "ěr bào shén",
            "meaning": "传说中专门在耳边报告消息的神，后多比喻秘密通风报信的人。",
            "example": "多亏耳报神通风，他才及时躲过那场灾祸。"
        },
        3438: {
            "pinyin": "ěr shùn zhī nián",
            "meaning": "指六十岁，出自《论语》“六十而耳顺”。",
            "example": "步入耳顺之年，他看问题愈发通达平和。"
        },
        3439: {
            "pinyin": "ěr bìn sī mó",
            "meaning": "同“耳鬓厮磨”，形容夫妻或亲密之人朝夕相处、感情亲密。",
            "example": "年轻时夫妻耳鬓厮磨，相互扶持。"
        },
        3440: {
            "pinyin": "è hǔ tūn yáng",
            "meaning": "像饿虎吞食羊一样，比喻动作凶猛或大肆吞并。",
            "example": "这支部队攻城如饿虎吞羊，所向披靡。"
        },
        3441: {
            "pinyin": "è piǎo biàn yě",
            "meaning": "饿死的人的尸体遍布原野，形容饥荒极为严重。",
            "example": "战乱年代，田地荒芜，甚至出现饿殍遍野的惨景。"
        },
        3442: {
            "pinyin": "è piǎo zǎi dào",
            "meaning": "饿死的人的尸体满路都是，形容灾荒严重、百姓极端困苦。",
            "example": "史籍中记载，当时饿殍载道，民不聊生。"
        },
        3443: {
            "pinyin": "è piǎo zhěn jiè",
            "meaning": "饿死的尸体相枕而眠、层层叠叠，形容饥荒或战乱极其惨烈。",
            "example": "那一年的饥荒几近饿殍枕藉，令人不忍卒读。"
        },
        3444: {
            "pinyin": "è jiàn fáng méng",
            "meaning": "在坏事刚刚萌芽、逐渐发展时就加以遏制。",
            "example": "对腐败现象要遏渐防萌，防止小错演变成大案。"
        },
        3445: {
            "pinyin": "è mì bā yīn",
            "meaning": "遏密八音，本指调和乐音，使之不淫不乱。后亦比喻约束声色享乐。",
            "example": "古人主张遏密八音，以防奢靡之风。"
        },
        3446: {
            "pinyin": "è yún rào liáng",
            "meaning": "形容歌声高妙动听，能穿云而绕梁不绝。",
            "example": "她一曲清唱，真有遏云绕梁之感。"
        },
        3447: {
            "pinyin": "è è hún hún",
            "meaning": "形容神志昏沉、愚钝无知的样子。",
            "example": "他少年时噩噩浑浑，并未显出什么才华。"
        },
        3448: {
            "pinyin": "è yú yǎn lèi",
            "meaning": "鳄鱼流泪是假装悲伤，比喻虚伪的眼泪。",
            "example": "他在镜头前的痛哭被讥为鳄鱼眼泪。"
        },
        3449: {
            "pinyin": "ēn bù fàng zhài",
            "meaning": "施恩不计回报，借贷却必收还，比喻处理恩与利应加以区分。",
            "example": "古训云恩不放债，既是提醒人要分清情义与账目。"
        },
        3450: {
            "pinyin": "ēn duàn yì jué",
            "meaning": "恩情断绝，义分尽弃，形容关系彻底破裂。",
            "example": "经过这件事，两人可谓恩断义绝，再无往来。"
        },
        3451: {
            "pinyin": "èr xīn sān yì",
            "meaning": "形容意志不坚定，犹豫不决，拿不定主意。",
            "example": "做大事若总是二心三意，终究难有成就。"
        },
        3452: {
            "pinyin": "èr zhě bù kě dé jiān",
            "meaning": "两个选择不能同时得到，比喻在两者之间必须作出取舍。",
            "example": "在事业和安逸之间，往往二者不可得兼。"
        },
        3453: {
            "pinyin": "ěr bìn sī mó",
            "meaning": "同“耳鬓厮磨”，形容亲密的人朝夕相处、形影不离。",
            "example": "儿时他们耳鬓撕磨，一同长大。"
        },
        3454: {
            "pinyin": "ěr mǎn bí mǎn",
            "meaning": "形容听得、闻得太多而感到厌烦，也形容骄傲自满的神情。",
            "example": "这些虚伪的恭维话早已叫人耳满鼻满。"
        },
        3455: {
            "pinyin": "ěr mù bì sè",
            "meaning": "耳朵和眼睛都像被堵住一样，比喻消息闭塞、见闻不广。",
            "example": "若长期脱离群众，难免耳目闭塞。"
        },
        3456: {
            "pinyin": "ěr mù zhòng duō",
            "meaning": "指替人侦察、通风报信的人很多，消息灵通。",
            "example": "他在各地耳目众多，消息十分灵通。"
        },
        3457: {
            "pinyin": "ěr páng fēng",
            "meaning": "从耳旁吹过的风，比喻听了不放在心上的话。",
            "example": "别人再三提醒，他都当耳旁风。"
        },
        3458: {
            "pinyin": "ěr shí zhī lùn",
            "meaning": "只凭耳朵听来的议论，没有经过考察，多指不可靠的说法。",
            "example": "这种耳食之论，不足为据。"
        },
        3459: {
            "pinyin": "ěr shí zhī yán",
            "meaning": "只听信别人传来的话，没有亲自求证的言语。",
            "example": "对重要决策不能根据耳食之言草率行事。"
        },
        3460: {
            "pinyin": "ěr shì mù shí",
            "meaning": "用耳朵去看、用眼睛去吃，比喻颠倒常理或见闻错乱。",
            "example": "若不分是非，便如耳视目食，一切皆乱。"
        },
        3461: {
            "pinyin": "ěr wén bù rú miàn jiàn",
            "meaning": "听说不如亲眼见到，比喻实地观察更为可靠。",
            "example": "这些风景真是耳闻不如面见，亲临其境才知其壮丽。"
        },
        3462: {
            "pinyin": "ěr ān yuǎn zhì",
            "meaning": "近处安定，则远方的人也会前来归附。",
            "example": "只有真正做到迩安远至，才能赢得四方民心。"
        },
        3463: {
            "pinyin": "èr fǒu zhōng huò",
            "meaning": "缶与钟都是量器，弄不清两者容量的差别，比喻连普通的是非道理都分辨不清。",
            "example": "对这样浅显的道理尚且二缶钟惑，又谈何治国理政。"
        },
        3464: {
            "pinyin": "èr fǒu zhōng huò",
            "meaning": "同“二缶钟惑”，比喻是非不明、判断混乱。",
            "example": "他对是非轻重竟至二缶锺惑，让人担忧。"
        },
        3465: {
            "pinyin": "èr huà bù shuō",
            "meaning": "一点儿多余的话都不说，形容态度干脆、立即行动。",
            "example": "他当即答应下来，二话不说就开始准备。"
        },
        3466: {
            "pinyin": "èr mǎn sān píng",
            "meaning": "旧时写字占格的术语，引申为做事讲究分寸、分配适当。",
            "example": "这几幅字布局得当，真有二满三平之妙。"
        },
        3467: {
            "pinyin": "èr sān jūn zǐ",
            "meaning": "指寥寥数位品行高尚的君子。",
            "example": "他身边常有二三君子相伴，切磋砥砺。"
        },
        3468: {
            "pinyin": "èr tóng yī mǎ",
            "meaning": "两个童子共乘一马，多用来形容旅伴相随或师友相从。",
            "example": "书中写道二童一马，随先生走村串户教书。"
        },
        3469: {
            "pinyin": "è hǔ qín yáng",
            "meaning": "像饿虎擒捉羊一样，形容出击凶猛、迅速。",
            "example": "精锐部队对敌军如饿虎擒羊，很快取得胜利。"
        },
        3470: {
            "pinyin": "fā cè jué kē",
            "meaning": "发下策问、决断科第，指举行科举考试取士。",
            "example": "古时寒门学子多寄望于发策决科，改变命运。"
        },
        3471: {
            "pinyin": "fā fán qǐ lì",
            "meaning": "从大体上加以阐发，订立条理规范。",
            "example": "这部著作对相关制度发凡起例，影响深远。"
        },
        3472: {
            "pinyin": "fā fèn tú qiáng",
            "meaning": "下定决心，努力谋求强盛或进步。",
            "example": "面对落后局面，全体员工唯有发愤图强。"
        },
        3473: {
            "pinyin": "fā fèn wàng shí",
            "meaning": "因努力用功而忘记吃饭，形容用功极勤。",
            "example": "备考期间他发愤忘食，只为不负多年心愿。"
        },
        3474: {
            "pinyin": "fā hào shī lìng",
            "meaning": "发出号令，布置命令。",
            "example": "将军在阵前发号施令，调度全军。"
        },
        3475: {
            "pinyin": "fā jiān tì fú",
            "meaning": "揭发奸邪、搜罗隐匿的罪犯。",
            "example": "监察机关肩负发奸擿伏之责，维护社会公正。"
        },
        3476: {
            "pinyin": "fā lóng zhèn kuì",
            "meaning": "使聋者也能听见、昏聩者也被震醒，比喻言论极有震撼力，能唤醒麻木的人。",
            "example": "那篇文章可谓发聋振聩，一针见血指出了现实问题。"
        },
        3477: {
            "pinyin": "fā méng jiě huò",
            "meaning": "启发蒙昧，解除疑惑，多形容老师的教导作用。",
            "example": "良师一席话，足以发蒙解惑。"
        },
        3478: {
            "pinyin": "fā méng zhèn kuì",
            "meaning": "启发蒙昧、振动昏聩，与“发聋振聩”义近。",
            "example": "这些扎实的调查报告，对决策者有发蒙振聩之功。"
        },
        3479: {
            "pinyin": "fā méng zhèn luò",
            "meaning": "启发蒙昧，使人震动警醒。",
            "example": "读史可以发蒙振落，使人明白盛衰之理。"
        },
        3480: {
            "pinyin": "fā rén shēn sī",
            "meaning": "使人受到触动而深切思考。",
            "example": "影片中的情节发人深思，令人久久不能平静。"
        },
        3481: {
            "pinyin": "fā rén shēn xǐng",
            "meaning": "使人深刻醒悟，多指具有教育意义的言行或作品。",
            "example": "这些案例发人深省，为大家敲响了警钟。"
        },
        3482: {
            "pinyin": "fā táng zhī qǐng",
            "meaning": "原指劝请君王发放棠邑粮食赈济饥民，后多指请求赈济。",
            "example": "灾情告急，他上书朝廷，提出发棠之请。"
        },
        3483: {
            "pinyin": "fā xíng xīn shì",
            "meaning": "硎：磨刀石；新试：初次试用。比喻新人初露锋芒或新作首次问世。",
            "example": "这位青年画家的新作不过发硎新试，却已颇受好评。"
        },
        3484: {
            "pinyin": "fā yán yíng tíng",
            "meaning": "发言之声充满庭院，形容众人议论热烈，或贤才云集各抒己见。",
            "example": "会上发言盈庭，大家畅所欲言。"
        },
        3485: {
            "pinyin": "fā yáng chuō lì",
            "meaning": "踔厉：振奋有力。形容精神振奋、气概昂扬。",
            "example": "青年人当发扬踔厉，承担时代使命。"
        },
        3486: {
            "pinyin": "fā yáng dǎo lì",
            "meaning": "振奋精神，奋发有为。与“发扬踔厉”义近。",
            "example": "他以振兴家乡为己任，处处发扬蹈厉。"
        },
        3487: {
            "pinyin": "fā yáng guāng dà",
            "meaning": "使好的事物更加显著、广大。",
            "example": "要把优良传统发扬光大，而不是丢弃。"
        },
        3488: {
            "pinyin": "fā zōng zhǐ shì",
            "meaning": "发：发出；综：踪，踪迹。发现猎物踪迹并指示猎犬追逐，比喻在幕后指挥、操纵。",
            "example": "表面看是他出面，其实另有高人发综指示。"
        },
        3489: {
            "pinyin": "fā zhèng shī rén",
            "meaning": "施行政令、推行仁政。",
            "example": "古代明君多能发政施仁，安抚百姓。"
        },
        3490: {
            "pinyin": "fá bù dāng zuì",
            "meaning": "刑罚与罪行不相当，多指处罚过重或不公正。",
            "example": "法律应当公正，绝不可罚不当罪。"
        },
        3491: {
            "pinyin": "fá bù zé zhòng",
            "meaning": "不责罚众人，指对普遍存在的错误不宜过于苛责。",
            "example": "古人有罚不责众之说，提醒我们区分主流与个别。"
        },
        3492: {
            "pinyin": "fá yī quàn bǎi",
            "meaning": "惩罚一个人以警戒许多人。",
            "example": "对典型案例要罚一劝百，形成震慑。"
        },
        3493: {
            "pinyin": "fá gōng jīn néng",
            "meaning": "夸耀功劳，炫示才能，含贬义。",
            "example": "他屡屡伐功矜能，招致同僚反感。"
        },
        3494: {
            "pinyin": "fá máo xǐ suǐ",
            "meaning": "比喻完全改变旧习，从根本上加以改造。",
            "example": "这场思想教育运动，意在伐毛洗髓，革除积弊。"
        },
        3495: {
            "pinyin": "fá xìng zhī fǔ",
            "meaning": "比喻损害人的天性或本性之事物，多用于批判过度约束。",
            "example": "教育不宜成为伐性之斧，否则会扼杀孩子的创造力。"
        },
        3496: {
            "pinyin": "fǎ bù ē guì",
            "meaning": "法律不偏袒权贵，强调法律面前人人平等。",
            "example": "真正的法治社会必须法不阿贵。"
        },
        3497: {
            "pinyin": "fǎ bù xùn qíng",
            "meaning": "法律不依徇私情，强调执法应当公正无私。",
            "example": "法不徇情，任何人触犯法律都要受到制裁。"
        },
        3498: {
            "pinyin": "fǎ hǎi wú biān",
            "meaning": "佛法或法律的力量广大无边。",
            "example": "他常说法海无边，劝人多行善事。"
        },
        3499: {
            "pinyin": "fǎ jiā bì shì",
            "meaning": "拂通“弼”。法家：明法度的大臣；拂士：辅弼之士，指能匡正时弊的贤臣良士。",
            "example": "国家要长治久安，离不开法家拂士的辅佐。"
        },
        3500: {
            "pinyin": "fǎ lì wú biān",
            "meaning": "佛法或神力无限广大，多用作对宗教力量的赞叹。",
            "example": "传说中菩萨法力无边，普度众生。"
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

    print(f"已为 3401–3500 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
