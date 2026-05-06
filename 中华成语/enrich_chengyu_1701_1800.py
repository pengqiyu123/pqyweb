import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    enrich = {
        1701: {
            "pinyin": "chì bì áo bīng",
            "meaning": "指三国时赤壁大战时的激烈战斗，后也泛指经过一场异常激烈残酷的大战。",
            "example": "在那场市场竞争的赤壁鏖兵之后，他的公司终于脱颖而出。"
        },
        1702: {
            "pinyin": "chì bó shàng zhèn",
            "meaning": "赤膊：光着上身；阵：战场。原指不穿盔甲就上阵打仗，比喻不加掩饰、毫无准备地亲自出面做某事。",
            "example": "这类复杂谈判绝不能赤膊上阵，必须事先充分调研。"
        },
        1703: {
            "pinyin": "chì chéng xiāng dài",
            "meaning": "赤诚：极真诚、忠诚。以至诚之心对待别人。",
            "example": "多年合作下来，他始终对伙伴赤诚相待。"
        },
        1704: {
            "pinyin": "chì dǎn zhōng xīn",
            "meaning": "赤胆：赤诚之心。形容对国家、事业等极其忠诚。",
            "example": "他以一腔赤胆忠心投身边防事业数十年。"
        },
        1705: {
            "pinyin": "chì dì qiān lǐ",
            "meaning": "赤：光秃、空无。形容天灾或战乱后大片土地寸草不生、一片荒凉。",
            "example": "连年旱灾，使这一带赤地千里，民不聊生。"
        },
        1706: {
            "pinyin": "chì kǒu dú shé",
            "meaning": "形容说话尖酸刻薄、言语恶毒，出口伤人。",
            "example": "与人相处要和气，切莫赤口毒舌伤人自尊。"
        },
        1707: {
            "pinyin": "chì shéng xì zú",
            "meaning": "相传月下老人以红绳系住男女的脚，使之结为夫妇，比喻婚姻姻缘是天注定的。",
            "example": "两人相识相爱，仿佛早被赤绳系足。"
        },
        1708: {
            "pinyin": "chì pín rú xǐ",
            "meaning": "赤贫：极度贫穷；如洗：好像被洗净一样。形容穷得一无所有。",
            "example": "他年轻时赤贫如洗，全凭刻苦奋斗才有今日成就。"
        },
        1709: {
            "pinyin": "chì shēn lù tǐ",
            "meaning": "指光着身子，衣不蔽体，也指全身裸露、一丝不挂。",
            "example": "古人以赤身露体示众为极大的羞辱。"
        },
        1710: {
            "pinyin": "chì shé shāo chéng",
            "meaning": "赤舌：比喻恶毒的言辞。比喻谗言或恶言可以造成极大的祸害。",
            "example": "流言蜚语若任其发展，往往有赤舌烧城之势。"
        },
        1711: {
            "pinyin": "chì shǒu kōng quán",
            "meaning": "赤手：空手。形容两手空空、手无兵器，比喻没有任何物质基础或依靠就去做事。",
            "example": "他当年赤手空拳闯天下，创业实属不易。"
        },
        1712: {
            "pinyin": "chì xiàn shén zhōu",
            "meaning": "中国的别称，多用来指中华大地。",
            "example": "诗人怀抱豪情，纵歌赤县神州。"
        },
        1713: {
            "pinyin": "chì xīn bào guó",
            "meaning": "赤心：纯真的忠心。指以至诚之心报效国家。",
            "example": "无数青年怀着赤心报国的理想奔赴边疆。"
        },
        1714: {
            "pinyin": "chì xīn xiāng dài",
            "meaning": "赤心：真诚的心。以真心诚意对待别人。",
            "example": "他们夫妻数十年相濡以沫，始终赤心相待。"
        },
        1715: {
            "pinyin": "chì zǐ zhī xīn",
            "meaning": "赤子：初生婴儿。比喻纯洁善良、不染世故的心地。",
            "example": "身居要职而不失赤子之心，实属难得。"
        },
        1716: {
            "pinyin": "chì zhà fēng yún",
            "meaning": "叱咤：怒喝。形容声势威猛，足以左右局势或轰动一时。",
            "example": "他年轻时也曾在商界叱咤风云。"
        },
        1717: {
            "pinyin": "chōng ěr bù wén",
            "meaning": "充：塞住。塞住耳朵不听，比喻故意不听别人的意见或对外界事物置若罔闻。",
            "example": "对群众的合理建议绝不能充耳不闻。"
        },
        1718: {
            "pinyin": "chōng lèi zhì jìn",
            "meaning": "充类：类推扩展；至尽：到极致。指就同类事理作充分推论，把道理引申到最精微周密的程度。",
            "example": "这篇文章从一个例子出发，层层推演，可谓充类至尽。"
        },
        1719: {
            "pinyin": "chōng lǘ zhī qìng",
            "meaning": "充闾：光大门第。指能使门第兴盛的喜庆事，多用于祝贺生子或家族昌盛。",
            "example": "新添贵子，自是满门充闾之庆。"
        },
        1720: {
            "pinyin": "chōng fēng xiàn zhèn",
            "meaning": "陷：攻入敌阵。指勇往直前冲向敌人阵地，形容作战勇猛，也比喻在艰巨任务中冲在最前面。",
            "example": "关键时刻，总要有人站出来冲锋陷阵。"
        },
        1721: {
            "pinyin": "chōng hūn tóu nǎo",
            "meaning": "形容感情冲动或胜利得意，使人失去冷静判断。",
            "example": "取得一点成绩也不能被胜利冲昏头脑。"
        },
        1722: {
            "pinyin": "chōng kǒu ér chū",
            "meaning": "话语未经思考就从口中说出，形容一时冲动、脱口而出。",
            "example": "他一时激动，责备的话就冲口而出。"
        },
        1723: {
            "pinyin": "chóng bì shǔ gān",
            "meaning": "本指微小的虫臂、鼠肝，比喻极其微贱、不足挂齿的事物，多用作自谦。",
            "example": "晚辈所献不过虫臂鼠肝，聊表心意而已。"
        },
        1724: {
            "pinyin": "chóng shā yuán hè",
            "meaning": "旧比喻战死沙场的将士，也泛指死于战乱的人。",
            "example": "烽烟散尽，那些虫沙猿鹤却永远留在史册之中。"
        },
        1725: {
            "pinyin": "chóng yú zhī xué",
            "meaning": "指过于琐碎细微的考据之学，多用作自谦或批评。",
            "example": "他自谓不过虫鱼之学，不敢与诸君高论相提并论。"
        },
        1726: {
            "pinyin": "chóng lùn hóng yì",
            "meaning": "崇：高；闳：宏大。形容议论高明深远、气度宏大。",
            "example": "会上诸专家崇论闳议，各抒己见。"
        },
        1727: {
            "pinyin": "chóng shān jùn lǐng",
            "meaning": "形容高大险峻、连绵起伏的山岭。",
            "example": "我们翻越崇山峻岭，终于到达山那边的小村庄。"
        },
        1728: {
            "pinyin": "chóng dǎo fù zhé",
            "meaning": "覆辙：翻过车留下的车辙，比喻失败的教训。指重犯前人的错误。",
            "example": "改革要汲取历史教训，切勿重蹈覆辙。"
        },
        1729: {
            "pinyin": "chóng jiàn tiān rì",
            "meaning": "重新见到天日，比喻摆脱黑暗困境或重获自由光明。",
            "example": "案件平反后，他终于重见天日。"
        },
        1730: {
            "pinyin": "chóng dǔ tiān rì",
            "meaning": "再次得见光明，形容从艰难或黑暗中重新获得新生。",
            "example": "经历多年坎坷，他的事业总算重睹天日。"
        },
        1731: {
            "pinyin": "chóng guī dié jǔ",
            "meaning": "规、矩：画圆画方的工具。比喻法度、规矩十分周密严谨。",
            "example": "这一制度设计可谓重规迭矩，几无疏漏。"
        },
        1732: {
            "pinyin": "chóng luán dié zhàng",
            "meaning": "形容山峦重叠、峰峦起伏的壮丽景象。",
            "example": "远处重峦叠嶂，在云雾间若隐若现。"
        },
        1733: {
            "pinyin": "chóng mén jī tuò",
            "meaning": "柝：打更用的木梆。设立重重门户，夜间敲梆巡更，比喻戒备森严。",
            "example": "城池外重门击柝，守备极其严密。"
        },
        1734: {
            "pinyin": "chóng shēng fù mǔ",
            "meaning": "比喻有救命大恩或恩情极深的人，多指救命恩人。",
            "example": "是您在危难时伸手相救，对我而言简直是重生父母。"
        },
        1735: {
            "pinyin": "chóng wēn jiù mèng",
            "meaning": "重新温习从前的经历，比喻再度实现昔日的理想或重拾旧日美好回忆。",
            "example": "多年后重游故地，不禁有重温旧梦之感。"
        },
        1736: {
            "pinyin": "chóng xī lěi qià",
            "meaning": "熙：光明；洽：融洽。形容国家连世升平、政局清明。",
            "example": "在先贤励精图治之下，方有今日重熙累洽之盛世。"
        },
        1737: {
            "pinyin": "chóng yán dié zhàng",
            "meaning": "山岩重叠如屏障一样，形容山势险峻、层峦叠嶂。",
            "example": "这里重岩叠障，向来是兵家必争之地。"
        },
        1738: {
            "pinyin": "chóng zhěng qí gǔ",
            "meaning": "比喻在遭受挫折后，重新整顿队伍、鼓舞士气，再度出发。",
            "example": "短暂休整之后，球队重整旗鼓，再度踏上赛场。"
        },
        1739: {
            "pinyin": "chóng zú ér lì, cè mù ér shì",
            "meaning": "重足：两脚并拢不敢移动；侧目：斜着眼看。形容既恐惧又愤恨而不敢言的神态。",
            "example": "在高压统治下，百姓只得重足而立，侧目而视。"
        },
        1740: {
            "pinyin": "chǒng rǔ bù jīng",
            "meaning": "宠：荣耀；辱：屈辱。受宠或遭辱都不惊慌失措，形容内心安定，不以外物喜忧。",
            "example": "修身之人应宠辱不惊，自守本心。"
        },
        1741: {
            "pinyin": "chǒng rǔ jiē wàng",
            "meaning": "宠：荣耀；辱：屈辱。把荣辱得失都置之度外，不放在心上。",
            "example": "他淡泊名利，早已宠辱皆忘。"
        },
        1742: {
            "pinyin": "chǒng rǔ ruò jīng",
            "meaning": "出自《老子》，原意是把受宠与受辱都看作一件值得警惕的大事，后也形容心存戒惧、谨慎处世。",
            "example": "为官者当宠辱若惊，方能慎终如始。"
        },
        1743: {
            "pinyin": "chōu chōu dā dā",
            "meaning": "形容抽噎啜泣、断断续续的哭泣声。",
            "example": "她坐在床沿上抽抽搭搭地哭个不停。"
        },
        1744: {
            "pinyin": "chōu dāo duàn shuǐ",
            "meaning": "用刀去砍流水。比喻企图用错误的方法解决问题，结果徒劳无功，多用以形容愁思难解。",
            "example": "李白诗云：抽刀断水水更流，正道尽愁难消之意。"
        },
        1745: {
            "pinyin": "chōu jīn bá gǔ",
            "meaning": "抽筋拔骨，比喻极其严厉地折磨或压榨，也形容训练、劳动的强度极大。",
            "example": "旧社会苛捐杂税几乎要把百姓抽筋拔骨。"
        },
        1746: {
            "pinyin": "chōu sī bō jiǎn",
            "meaning": "像抽丝、剥茧一样，一层层理出头绪，比喻分析事物条理清晰、由浅入深。",
            "example": "侦查人员抽丝剥茧，最终还原了案件真相。"
        },
        1747: {
            "pinyin": "chōu xīn zhǐ fèi",
            "meaning": "抽去柴薪使水不再沸腾，比喻从根本上解决问题或消除祸患。",
            "example": "治理污染不能只治河面垃圾，还要抽薪止沸，控制源头排污。"
        },
        1748: {
            "pinyin": "chóu chú bù qián",
            "meaning": "踌躇：犹豫不决。形容拿不定主意而迟疑不前。",
            "example": "机会稍纵即逝，切莫踌躇不前。"
        },
        1749: {
            "pinyin": "chóu chú mǎn zhì",
            "meaning": "形容心满意足、得意洋洋的神情。",
            "example": "听到评委的赞扬，他不禁踌躇满志。"
        },
        1750: {
            "pinyin": "chóu rén guǎng zhòng",
            "meaning": "在许多人的场合，当众之中。",
            "example": "稠人广众之下，他依然从容不迫地发表演讲。"
        },
        1751: {
            "pinyin": "chóu rén guǎng zuò",
            "meaning": "指在许多人的座位之中，当着众人的面。",
            "example": "稠人广座之下，切记言行得体。"
        },
        1752: {
            "pinyin": "chóu rén xiāng jiàn, fèn wài yǎn hóng",
            "meaning": "仇敌相见，格外眼红。形容仇恨极深，一见面就怒火中烧。",
            "example": "两家积怨已久，仇人相见，分外眼红。"
        },
        1753: {
            "pinyin": "chóu cháng bǎi jié",
            "meaning": "愁绪像肠子打了上百个结一样，形容内心极度忧愁郁结。",
            "example": "国事家事压在心头，真是愁肠百结。"
        },
        1754: {
            "pinyin": "chóu cháng cùn duàn",
            "meaning": "形容忧愁悲痛到了极点，仿佛愁肠一寸一寸断裂。",
            "example": "噩耗传来，她只觉愁肠寸断。"
        },
        1755: {
            "pinyin": "chóu cháng jiǔ huí",
            "meaning": "比喻内心愁绪回环往复，难以排遣。",
            "example": "深夜难眠，只觉愁肠九回。"
        },
        1756: {
            "pinyin": "chóu duō yè cháng",
            "meaning": "忧愁多的人往往觉得夜晚特别漫长。",
            "example": "愁多夜长，他常常辗转反侧到天明。"
        },
        1757: {
            "pinyin": "chóu méi bù zhǎn",
            "meaning": "皱着眉头，愁容满面，形容极为忧愁不乐。",
            "example": "这些天他总是愁眉不展，显然心事重重。"
        },
        1758: {
            "pinyin": "chóu méi kǔ liǎn",
            "meaning": "愁眉苦脸，形容忧愁苦闷的神情。",
            "example": "不要整日愁眉苦脸，试着乐观一点。"
        },
        1759: {
            "pinyin": "chóu méi lèi yǎn",
            "meaning": "愁眉紧锁、双眼含泪，形容极度忧伤的神态。",
            "example": "她愁眉泪眼地诉说着这些年的委屈。"
        },
        1760: {
            "pinyin": "chóu méi suǒ yǎn",
            "meaning": "眉头紧锁、目光忧郁，形容愁苦不安的样子。",
            "example": "听到裁员消息，许多人立刻愁眉锁眼。"
        },
        1761: {
            "pinyin": "chóu méi tí zhuāng",
            "meaning": "愁眉：细而曲折的眉形；啼妆：故意在眼下作出泪痕的妆饰。形容女子带愁态的妖娆妆束。",
            "example": "台上的旦角愁眉啼妆，一举一动都牵动着观众的心。"
        },
        1762: {
            "pinyin": "chóu yún cǎn wù",
            "meaning": "形容阴沉晦暗的景象，多比喻令人愁闷压抑的局面。",
            "example": "战争阴影之下，大地一派愁云惨雾。"
        },
        1763: {
            "pinyin": "chǒu lèi è wù",
            "meaning": "指品行恶劣的一伙坏人、坏东西。",
            "example": "这些丑类恶物终究会受到法律的严惩。"
        },
        1764: {
            "pinyin": "chǒu shēng yuǎn bō",
            "meaning": "丑：不光彩；声：名声。坏名声传播得很远，形容名声极坏。",
            "example": "他贪赃枉法的事早已丑声远播。"
        },
        1765: {
            "pinyin": "chǒu tài bǎi chū",
            "meaning": "各种丑恶的姿态轮番出现，形容丑态层出不穷。",
            "example": "他一喝醉就丑态百出，旁人都替他难堪。"
        },
        1766: {
            "pinyin": "chòu bù kě dāng",
            "meaning": "臭得让人难以忍受，也比喻名声极坏。",
            "example": "这条排污沟早已臭不可当，却一直无人整治。"
        },
        1767: {
            "pinyin": "chòu bù kě wén",
            "meaning": "臭得使人受不了，比喻名声极坏、令人深恶痛绝。",
            "example": "那些借公益之名行敛财之实的人早已臭不可闻。"
        },
        1768: {
            "pinyin": "chòu míng yuǎn yáng",
            "meaning": "坏名声传播得很远，形容极端恶劣的名声。",
            "example": "他一系列丑闻曝光后，臭名远扬。"
        },
        1769: {
            "pinyin": "chòu míng zhāo zhù",
            "meaning": "臭名：坏名声；昭著：显著、显而易见。指坏名声非常明显、众所共知。",
            "example": "那个贪官在当地早已臭名昭著。"
        },
        1770: {
            "pinyin": "chòu ròu lái yíng",
            "meaning": "腐臭的肉招来苍蝇，比喻自身品行有问题，才会招致坏人的围拢和利用。",
            "example": "身正不怕影子斜，若行迹可疑，自会臭肉来蝇。"
        },
        1771: {
            "pinyin": "chū chū máo lú",
            "meaning": "茅庐：草屋。原指诸葛亮刚出山，今多比喻刚离开家庭或学校走上社会，缺乏经验。",
            "example": "我不过是初出茅庐的新人工程师，还有许多要向前辈学习。"
        },
        1772: {
            "pinyin": "chū fā fú róng",
            "meaning": "像刚刚开放的荷花一样，形容女子姿容清新秀丽，也形容文笔、艺术清新脱俗。",
            "example": "她年纪轻轻，气质如初发芙蓉，让人眼前一亮。"
        },
        1773: {
            "pinyin": "chū lù fēng máng",
            "meaning": "锋芒：锐气、本领。初次显露出才华或本领。",
            "example": "这位新人在比赛中初露锋芒，很有发展潜力。"
        },
        1774: {
            "pinyin": "chū shēng niú dú bù pà hǔ",
            "meaning": "比喻年轻人阅历浅、不知厉害，因此无所畏惧。",
            "example": "他初生牛犊不怕虎，单枪匹马闯进了竞争最激烈的行业。"
        },
        1775: {
            "pinyin": "chū xiě huáng tíng",
            "meaning": "《黄庭经》为小楷名帖，初写黄庭被视为书法恰到好处。后比喻做事或行文恰到好处。",
            "example": "这篇文章分寸拿捏极佳，可谓初写黄庭。"
        },
        1776: {
            "pinyin": "chū lì yōng cái",
            "meaning": "樗栎：不成材的树木。比喻平庸无用之才，多用作自谦。",
            "example": "我不过樗栎庸材，所言仅供参考。"
        },
        1777: {
            "pinyin": "chū chén bù rǎn",
            "meaning": "出尘：超脱尘世；不染：不受污染。比喻身处污浊环境仍能保持高洁品格。",
            "example": "他为人淡泊名利，可谓出尘不染。"
        },
        1778: {
            "pinyin": "chū ěr fǎn ěr",
            "meaning": "尔：你。对人发出承诺却又翻悔，反复无常。",
            "example": "做事要讲信用，不能出尔反尔。"
        },
        1779: {
            "pinyin": "chū fán rù shèng",
            "meaning": "凡：平凡；胜：胜境、妙境。指超越平凡，进入高妙境界，形容造诣精深。",
            "example": "这幅画意境高远，已然出凡入胜。"
        },
        1780: {
            "pinyin": "chū gǔ qiān qiáo",
            "meaning": "谷：山谷；乔：高树。比喻地位由卑微迁升到显要，或环境大为改善。",
            "example": "他从普通工人做到厂长，可谓出谷迁乔。"
        },
        1781: {
            "pinyin": "chū guāi lù chǒu",
            "meaning": "乖：不合常理；露丑：丢人现眼。形容言行荒唐，显出丑态。",
            "example": "他酒后失态，在宴席上出乖露丑。"
        },
        1782: {
            "pinyin": "chū hé diǎn jì",
            "meaning": "诘问有何经典可据，比喻言论没有根据，是无稽之谈。",
            "example": "你这番说法出何典记，最好拿出切实证据来。"
        },
        1783: {
            "pinyin": "chū jiàng rù xiàng",
            "meaning": "出任将帅或宰相，比喻做大官、居高位。",
            "example": "他少年立志，誓要将来出将入相、报效国家。"
        },
        1784: {
            "pinyin": "chū kǒu chéng zhāng",
            "meaning": "说出的话就像成篇文章一样完美，形容文思敏捷、口才出众。",
            "example": "老教授出口成章，同学们听得如醉如痴。"
        },
        1785: {
            "pinyin": "chū kǒu rù ěr",
            "meaning": "话只在你我之间流转，不为外人所知。",
            "example": "此话仅当出口入耳，切勿对外宣扬。"
        },
        1786: {
            "pinyin": "chū kǒu shāng rén",
            "meaning": "话一出口就伤害别人，形容说话尖刻、不顾他人感受。",
            "example": "即使生气，也不要随便出口伤人。"
        },
        1787: {
            "pinyin": "chū lèi bá cuì",
            "meaning": "拔：超出；类：同类；萃：聚集。形容品德、才能远远超过同类。",
            "example": "他在数学方面的天赋确实出类拔萃。"
        },
        1788: {
            "pinyin": "chū mò wú cháng",
            "meaning": "忽而出现，忽而隐没，行动无固定规律，使人难以捉摸。",
            "example": "这伙山匪出没无常，给当地百姓带来极大困扰。"
        },
        1789: {
            "pinyin": "chū móu huà cè",
            "meaning": "谋：谋划；画：筹划。替人出主意、定策略。",
            "example": "几十年来，他一直为企业出谋画策，贡献良多。"
        },
        1790: {
            "pinyin": "chū qí bù yì",
            "meaning": "趁对方没有防备，出其意料地采取行动。",
            "example": "要想制胜，必须攻其无备，出其不意。"
        },
        1791: {
            "pinyin": "chū qí zhì shèng",
            "meaning": "发奇兵或用奇计制服对手，比喻用非常规手段取得胜利。",
            "example": "这次战术调整可谓出奇制胜，对手完全没有准备。"
        },
        1792: {
            "pinyin": "chū rén tóu dì",
            "meaning": "原意是让人高出一头，后指超出一般人之上，形容成绩突出或才德出众。",
            "example": "他读书刻苦，终在同届同学中出人头地。"
        },
        1793: {
            "pinyin": "chū rén yì biǎo",
            "meaning": "表：外。出乎人们意料之外，形容情况或言论十分新奇。",
            "example": "这部作品构思精巧，结局更是出人意表。"
        },
        1794: {
            "pinyin": "chū rù rén zuì",
            "meaning": "指司法裁判失当，把有罪判为无罪，或把无罪判为有罪。",
            "example": "古代律例对官吏故意出入人罪有严厉惩处。"
        },
        1795: {
            "pinyin": "chū shān quán shuǐ",
            "meaning": "本指山中清泉出山后渐趋浑浊，后多用以比喻人一旦涉世或出仕容易失去原有的清白。",
            "example": "有人在官场渐渐迷失自我，真是出山泉水不再清。"
        },
        1796: {
            "pinyin": "chū shén rù huà",
            "meaning": "形容技艺、文章等达到极其高妙的境界。",
            "example": "老画家笔下的山水已臻出神入化之境。"
        },
        1797: {
            "pinyin": "chū shēng rù sǐ",
            "meaning": "原指人从出生到死亡的过程，后多形容历经生死考验、冒着生命危险。",
            "example": "他跟随部队南征北战，出生入死数十载。"
        },
        1798: {
            "pinyin": "chū shī bù lì",
            "meaning": "师：军队。出征或事情一开始就遭遇挫折和不顺。",
            "example": "这次行动出师不利，但并不影响整体战略布局。"
        },
        1799: {
            "pinyin": "chū shì chāo fán",
            "meaning": "超出尘世凡俗，形容品格或境界高妙脱俗。",
            "example": "他诗风清峻，有出世超凡之致。"
        },
        1800: {
            "pinyin": "chū shǒu dé lú",
            "meaning": "卢：古代博戏中一掷皆黑的最胜点。比喻一出手便获得大胜或开局顺利。",
            "example": "项目一上线便广受欢迎，可谓出手得卢。"
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

    print(f"已为 1701–1800 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
