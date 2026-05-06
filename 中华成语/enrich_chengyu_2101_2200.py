import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    enrich = {
        2101: {
            "pinyin": "cuò rèn yán biāo",
            "meaning": "错把颜标当成颜真卿，形容见识浅陋、判断失误。",
            "example": "若不细加甄别，难免主司头脑太冬烘，错认颜标。"
        },
        2102: {
            "pinyin": "cuò zōng fù zá",
            "meaning": "交错综合而又复杂，形容事物头绪繁多、关系错杂。",
            "example": "现实问题往往错综复杂，不能简单下结论。"
        },
        2103: {
            "pinyin": "rù shèng chāo fán",
            "meaning": "进入圣人的境界，超越凡俗，形容学识或修养极为高超。",
            "example": "这部著作的影响可谓入圣超凡，历久弥新。"
        },
        2104: {
            "pinyin": "yǐ duàn tóu luǎn",
            "meaning": "碫：磨刀石。用磨刀石去砸鸡蛋，比喻以强攻弱，必胜无疑。",
            "example": "两队实力悬殊，此战简直是以碫投卵。"
        },
        2105: {
            "pinyin": "yǐ lǐ xiāng dài",
            "meaning": "用礼貌的方式对待别人，形容待人客气、恭敬。",
            "example": "无论对谁，他总是以礼相待，从不盛气凌人。"
        },
        2106: {
            "pinyin": "cí bù dá yì",
            "meaning": "言词不能完全表达出意思，形容表达能力不足或言不尽意。",
            "example": "这段经历太复杂，我一时词不达意。"
        },
        2107: {
            "pinyin": "cā quán mó zhǎng",
            "meaning": "搓拳头、摩手掌，形容跃跃欲试或兴奋期待的样子。",
            "example": "小伙子们听说要上场比赛，一个个擦拳磨掌。"
        },
        2108: {
            "pinyin": "cā quán mǒ zhǎng",
            "meaning": "同“擦拳磨掌”，形容激动兴奋、准备大干一场的样子。",
            "example": "大家对新项目颇有信心，早已擦拳抹掌。"
        },
        2109: {
            "pinyin": "cā zhǎng mó quán",
            "meaning": "同“擦拳磨掌”，形容蠢蠢欲动、热切期盼上阵。",
            "example": "队员们擦掌磨拳，只等裁判一声哨响。"
        },
        2110: {
            "pinyin": "cā zhī mǒ fěn",
            "meaning": "抹脂涂粉，形容浓妆艳抹。",
            "example": "她并不喜欢擦脂抹粉，更偏爱素面朝天。"
        },
        2111: {
            "pinyin": "cāi quán xíng lìng",
            "meaning": "猜拳行令，多指酒席间以划拳行令助兴。",
            "example": "酒过三巡，众人开始猜拳行令，笑声不断。"
        },
        2112: {
            "pinyin": "cái bì shí qiǎn",
            "meaning": "才学被掩、见识浅陋，形容才能有限、眼界不高。",
            "example": "我不过才蔽识浅，此事还得向前辈请教。"
        },
        2113: {
            "pinyin": "cái dà nán yòng",
            "meaning": "才能虽然很大，却难以被任用或发挥。",
            "example": "若环境闭塞，再有本事的人也会才大难用。"
        },
        2114: {
            "pinyin": "cái dà rú hǎi",
            "meaning": "才华像大海一样深广，形容才能极其出众。",
            "example": "他学识渊博，真有才大如海之感。"
        },
        2115: {
            "pinyin": "cái duǎn qì cū",
            "meaning": "才能短浅、性情粗率，形容人学识不丰又急躁。",
            "example": "他虽有热情，却略嫌才短气粗。"
        },
        2116: {
            "pinyin": "cái duō shí guǎ",
            "meaning": "才华虽多却见识浅薄，形容有才而少学，见地不高。",
            "example": "只会卖弄文采而不增长见闻，难免才多识寡。"
        },
        2117: {
            "pinyin": "cái gāo qī bù",
            "meaning": "才气很高，据说七步之内可成诗，形容才思敏捷。",
            "example": "他临场挥毫成章，真有才高七步之风。"
        },
        2118: {
            "pinyin": "cái gāo qì qīng",
            "meaning": "才华高超、气质清雅，形容人有才又气度高洁。",
            "example": "那位诗人自少便才高气清，不染俗尘。"
        },
        2119: {
            "pinyin": "cái guàn èr yǒu",
            "meaning": "二酉：古代藏书处名。形容学识渊博，通晓群籍。",
            "example": "他自诩才贯二酉，几乎无书不读。"
        },
        2120: {
            "pinyin": "cái guǎng fáng shēn",
            "meaning": "才能过于广博反而妨碍自身，指才多不免遭忌。",
            "example": "在权术纷争之中，往往才广妨身。"
        },
        2121: {
            "pinyin": "cái guò qū sòng",
            "meaning": "才华胜过屈原、宋玉，极言文才之高。",
            "example": "古人赞他辞章瑰丽，几乎才过屈宋。"
        },
        2122: {
            "pinyin": "cái huá gài shì",
            "meaning": "才华盖过当世所有的人，形容才气极其出众。",
            "example": "他以一己之力改变了行业格局，可谓才华盖世。"
        },
        2123: {
            "pinyin": "cái huá héng yì",
            "meaning": "才华横溢，形容才能极为丰富、表现突出。",
            "example": "她在舞台上的表现真是才华横溢。"
        },
        2124: {
            "pinyin": "cái kuā bā dǒu",
            "meaning": "自夸才学有八斗之多，形容非常自负或才华出众。",
            "example": "他一向才夸八斗，说话难免带着几分傲气。"
        },
        2125: {
            "pinyin": "cái mào jiān quán",
            "meaning": "才学与容貌都很出众。",
            "example": "她可谓才貌兼全，是众人眼中的焦点。"
        },
        2126: {
            "pinyin": "cái mào jù quán",
            "meaning": "才华和容貌都很完美，与“才貌兼全”同义。",
            "example": "古书常以才貌俱全来形容绝代佳人。"
        },
        2127: {
            "pinyin": "cái dà qì cū",
            "meaning": "财力雄厚而气焰嚣张，形容仗着有钱就蛮横无理。",
            "example": "他仗着财大气粗，对人说话颇不客气。"
        },
        2128: {
            "pinyin": "cái dān lì jié",
            "meaning": "钱财和力气都耗尽了，形容极端困乏窘迫。",
            "example": "战乱多年，百姓早已财殚力竭。"
        },
        2129: {
            "pinyin": "cái dān lì jìn",
            "meaning": "钱财用光、力气耗尽，形容极其困顿疲惫。",
            "example": "多年的官司让他财殚力尽，身心俱疲。"
        },
        2130: {
            "pinyin": "cái dān lì pū",
            "meaning": "钱财和体力都已经耗竭，义同“财殚力尽”。",
            "example": "企业连年亏损，老板几乎财殚力痡。"
        },
        2131: {
            "pinyin": "cái jié lì jìn",
            "meaning": "钱财耗尽、力气也用完，形容十分困乏窘迫。",
            "example": "这场救援行动使他们财竭力尽，却无怨无悔。"
        },
        2132: {
            "pinyin": "cái kuì lì chù",
            "meaning": "钱财匮乏、力量不足，形容财力和人力都很紧张。",
            "example": "若一味扩张，难免陷入财匮力绌的境地。"
        },
        2133: {
            "pinyin": "cān qián yǐ héng",
            "meaning": "立则见其在前，在车则见其倚衡，形容时刻谨记忠信笃敬，以之为行事准则。",
            "example": "为人处世当参前倚衡，不忘忠信笃敬四字。"
        },
        2134: {
            "pinyin": "cān tiān èr dì",
            "meaning": "参：通“叁”；贰：二。比喻颠倒是非、扰乱纲常，也用以形容罪行重大。",
            "example": "他妄图参天贰地，扰乱法度，终遭严惩。"
        },
        2135: {
            "pinyin": "cān tiān liǎng dì",
            "meaning": "同“参天贰地”，形容犯上作乱、颠覆纲常。",
            "example": "谋反之举实属参天两地的大罪。"
        },
        2136: {
            "pinyin": "cān wǔ cuò zòng",
            "meaning": "参差错落、相互交织，形容关系复杂、条理纷繁。",
            "example": "各方利益参伍错纵，需要耐心协调。"
        },
        2137: {
            "pinyin": "cēn cī bù yī",
            "meaning": "长短、高低或好坏不完全一致，形容参差不齐。",
            "example": "各地发展水平参差不一，需要分类施策。"
        },
        2138: {
            "pinyin": "cān wǔ cuò zōng",
            "meaning": "交错综合，形容情况复杂、多种因素交织。",
            "example": "历史进程往往是参伍错综的多重结果。"
        },
        2139: {
            "pinyin": "cái mí xīn qiào",
            "meaning": "被金钱迷住了心窍，形容极其贪财。",
            "example": "一旦财迷心窍，什么原则都可以抛到脑后。"
        },
        2140: {
            "pinyin": "cái cháng bǔ duǎn",
            "meaning": "剪去长处补在短处，比喻取长补短、弥补不足。",
            "example": "团队合作贵在裁长补短，互通有无。"
        },
        2141: {
            "pinyin": "cái hóng diǎn cuì",
            "meaning": "裁剪红绫、点缀翠羽，形容装饰华丽精致。",
            "example": "台上的戏服裁红点翠，极尽绚烂之能事。"
        },
        2142: {
            "pinyin": "cái xīn lòu shé",
            "meaning": "刻意雕琢语言，竭力劝说或辩论，形容费尽心思和口舌。",
            "example": "他为此事四处奔走，裁心镂舌，十分辛苦。"
        },
        2143: {
            "pinyin": "cái yuè lòu yún",
            "meaning": "裁剪明月、雕刻流云，比喻文辞华美或技艺精妙。",
            "example": "这篇词作意境高远，真有裁月镂云之妙。"
        },
        2144: {
            "pinyin": "cái yún jiǎn shuǐ",
            "meaning": "裁云剪水，形容文笔优美或舞姿轻盈。",
            "example": "舞者身姿宛若裁云剪水，令人目不转睛。"
        },
        2145: {
            "pinyin": "cǎi chuán bù zhuó",
            "meaning": "用大梁木而不加斧凿，比喻做事粗疏、不加修饰。",
            "example": "这篇报告如同采椽不斫，还需仔细推敲。"
        },
        2146: {
            "pinyin": "cǎi fēng wèn sú",
            "meaning": "采集民间歌谣、访问风俗，指调查民情、了解民意。",
            "example": "学者深入乡间采风问俗，记录下大量第一手资料。"
        },
        2147: {
            "pinyin": "cǎi fēng cǎi fěi",
            "meaning": "出自《诗经》，比喻择人要看根本，不可只顾末节。",
            "example": "选贤任能当如采葑采菲，不以下体。"
        },
        2148: {
            "pinyin": "cǎi fèng suí yā",
            "meaning": "凤凰却跟着乌鸦，形容贤者误随不肖、良材屈就下位。",
            "example": "若让栋梁之才长期采凤随鸦，实在可惜。"
        },
        2149: {
            "pinyin": "cǎi lán zèng sháo",
            "meaning": "以兰赠人、以芍药回赠，比喻以好意相互酬答。",
            "example": "他送来一篮水果，对方也采兰赠芍地回礼。"
        },
        2150: {
            "pinyin": "cǎi xīn zhī huàn",
            "meaning": "上山砍柴而引发的祸患，比喻隐伏的小事可能酿成大祸。",
            "example": "这点疏忽看似不起眼，却可能成为采薪之患。"
        },
        2151: {
            "pinyin": "cǎi xīn zhī jí",
            "meaning": "因砍柴而招致的疾病，比喻由细微处引发的严重后果。",
            "example": "他常以采薪之疾自警，不敢再轻忽健康。"
        },
        2152: {
            "pinyin": "cǎi bǐ shēng huā",
            "meaning": "笔端生出花来，形容文采极其华美。",
            "example": "名家三笔下去，仿佛彩笔生花。"
        },
        2153: {
            "pinyin": "cán gēng lěng fàn",
            "meaning": "吃剩的菜羹和冷饭，比喻待遇差、地位低或不受重视的事物。",
            "example": "他只分到些残羹冷饭，却仍兢兢业业。"
        },
        2154: {
            "pinyin": "cán guī duàn bì",
            "meaning": "残缺的圭璧，比喻残存的文物、典籍或美德。",
            "example": "这些散佚的手稿好比残圭断璧，弥足珍贵。"
        },
        2155: {
            "pinyin": "cán jūn bài jiàng",
            "meaning": "被打败的军队和将领，形容战败的一方。",
            "example": "这支队伍早已是残军败将，再无还手之力。"
        },
        2156: {
            "pinyin": "cán mín hài wù",
            "meaning": "残害百姓、生灵，形容暴政或战乱给人民带来的灾难。",
            "example": "任何残民害物的行为都必将被历史唾弃。"
        },
        2157: {
            "pinyin": "cán mín yǐ chěng",
            "meaning": "以残害百姓为逞能，形容暴君或酷吏仗势作恶。",
            "example": "专制者往往残民以逞，终成众矢之的。"
        },
        2158: {
            "pinyin": "cāng gǒu bái yī",
            "meaning": "把白衣比作苍狗，比喻世事变化无常。",
            "example": "世间荣辱如苍狗白衣，转眼即非。"
        },
        2159: {
            "pinyin": "cāng gǒu bái yún",
            "meaning": "白云变成苍狗，形容世事变幻无常。",
            "example": "几十年风云变幻，真有苍狗白云之感。"
        },
        2160: {
            "pinyin": "cāng huáng fān fù",
            "meaning": "仓促慌张地反复变化，形容局势动荡不安。",
            "example": "股市行情一日之间苍黄翻覆，令人捉摸不定。"
        },
        2161: {
            "pinyin": "cāng huáng fǎn fù",
            "meaning": "匆忙慌乱地反复折腾，形容做事急躁、变化频繁。",
            "example": "政策若朝令夕改，难免苍黄反复。"
        },
        2162: {
            "pinyin": "cāng rán rú jǐ",
            "meaning": "灰白的胡须像戟一样竖立，形容老者威严刚劲的仪态。",
            "example": "那老将军苍髯如戟，气势逼人。"
        },
        2163: {
            "pinyin": "cáng fēng liǎn è",
            "meaning": "收敛锋芒、隐藏刀刃，形容不轻易显露锋锐。",
            "example": "他向来藏锋敛锷，从不轻易出手争功。"
        },
        2164: {
            "pinyin": "cáng fēng liǎn ruì",
            "meaning": "收敛锋锐，形容隐藏才能或不显山露水。",
            "example": "真正高人多懂得藏锋敛锐，不与人争。"
        },
        2165: {
            "pinyin": "cáng fēng liǎn yǐng",
            "meaning": "收敛锋芒、隐藏才华。",
            "example": "他年轻时锋芒毕露，如今却学会了藏锋敛颖。"
        },
        2166: {
            "pinyin": "cáng tóu kàng nǎo",
            "meaning": "把头藏起、昂起脖子，形容心怀鬼胎、遮遮掩掩的样子。",
            "example": "他回答得闪烁其词，一副藏头亢脑的模样。"
        },
        2167: {
            "pinyin": "cáng zhī míng shān",
            "meaning": "把书藏在名山之中，形容珍视典籍，使之流传久远。",
            "example": "古人常言藏之名山，以保文献不绝。"
        },
        2168: {
            "pinyin": "cáng zhū míng shān",
            "meaning": "同“藏之名山”，指把著作珍藏于名山，以期久远流传。",
            "example": "他愿将此书藏诸名山，留待后人评说。"
        },
        2169: {
            "pinyin": "cáng zhū míng shān, chuán zhī qí rén",
            "meaning": "把书藏在名山，又传给合适的人，形容对典籍极其珍视。",
            "example": "许多学者的心愿，无非藏诸名山，传之其人而已。"
        },
        2170: {
            "pinyin": "cāo dāo zhì jǐn",
            "meaning": "本不善治锦却执刀裁制，比喻不称其任或外行指挥内行。",
            "example": "若让门外汉操刀制锦，只会误事。"
        },
        2171: {
            "pinyin": "cāo fǔ fá kē",
            "meaning": "拿斧头去砍斫斧柄，借以比喻从实际中学习做事的方法。",
            "example": "教育后辈要像操斧伐柯，从身边榜样学起。"
        },
        2172: {
            "pinyin": "cāo gē rù shì",
            "meaning": "持戈进入别人家中，比喻内部人相互攻击或叛乱。",
            "example": "他勾结外人，简直是操戈入室。"
        },
        2173: {
            "pinyin": "cāo gē tóng shì",
            "meaning": "同室操戈，相互攻伐，指内部纷争。",
            "example": "家族企业最忌操戈同室，自相残杀。"
        },
        2174: {
            "pinyin": "cāo gū rǎn hàn",
            "meaning": "执笔写作，形容从事文章创作。",
            "example": "他少年时便操觚染翰，立志做个作家。"
        },
        2175: {
            "pinyin": "cāo máo rù shì",
            "meaning": "拿着长矛闯入别人家中，比喻内部人互相攻伐。",
            "example": "若在公司中操矛入室，只会两败俱伤。"
        },
        2176: {
            "pinyin": "cāo qí zhú yíng",
            "meaning": "经营奇货以追求赢利，形容投机取巧、逐利心切。",
            "example": "他一味操奇逐赢，终在风险中栽了跟头."
        },
        2177: {
            "pinyin": "cāo róu mó zhì",
            "meaning": "反复揉治、琢磨，比喻精心锤炼文章或品德。",
            "example": "这篇作品经作者多次操揉磨治，方臻成熟。"
        },
        2178: {
            "pinyin": "cāo shēn xíng shì",
            "meaning": "谨慎持身，以礼行世，形容修身自重、行事谨严。",
            "example": "他一生操身行世，从不逾矩。"
        },
        2179: {
            "pinyin": "cāo yíng zhì qí",
            "meaning": "运用奇巧谋略而获得胜利，形容善于出奇制胜。",
            "example": "在商战中，他往往操赢致奇，出人意表。"
        },
        2180: {
            "pinyin": "cāo zhī guò cù",
            "meaning": "做事过于急切，形容操之过急、缺乏耐心。",
            "example": "改革需要稳步推进，万不可操之过蹙。"
        },
        2181: {
            "pinyin": "cāo zhī guò jī",
            "meaning": "做事过分激烈、急躁。",
            "example": "他处理问题往往操之过激，容易激化矛盾。"
        },
        2182: {
            "pinyin": "cāo zhī guò qiè",
            "meaning": "行事过于迫切、急于求成。",
            "example": "人才培养切忌操之过切，需要时间积累。"
        },
        2183: {
            "pinyin": "cáo shè zhī móu",
            "meaning": "曹社：古代诸侯会盟之地。指合谋叛乱或另立政权的图谋。",
            "example": "史书记载，当时曾有曹社之谋，幸而被及时平息。"
        },
        2184: {
            "pinyin": "cǎo chuán jiè jiàn",
            "meaning": "用草船借箭，比喻巧用天时地利人和，借助外力完成任务。",
            "example": "这次合作堪称一场巧妙的草船借箭。"
        },
        2185: {
            "pinyin": "cǎo fù cài cháng",
            "meaning": "肚里装的只是草、菜，形容人学识浅薄。",
            "example": "若不刻苦读书，终难摆脱草腹菜肠之讥。"
        },
        2186: {
            "pinyin": "cǎo jiè rén mìng",
            "meaning": "把人命看得像草一样轻贱，形容极其残暴。",
            "example": "那场战争对草芥人命的漠视令人痛心。"
        },
        2187: {
            "pinyin": "cǎo shuài jiāng shì",
            "meaning": "办事草率、敷衍了事。",
            "example": "这份报告明显草率将事，需要重写。"
        },
        2188: {
            "pinyin": "cǎo mǐ fēng xíng",
            "meaning": "草木因风而伏倒，形容风行一时、影响广泛。",
            "example": "新政策一经推出，便草靡风行。"
        },
        2189: {
            "pinyin": "cǎo mù xiāo shū",
            "meaning": "草木稀疏、萧条，形容景象冷落、荒凉。",
            "example": "旧城墙边草木萧疏，透出几分苍凉。"
        },
        2190: {
            "pinyin": "cǎo mù yú fū",
            "meaning": "把草木和愚夫并提，比喻识见浅陋之人。",
            "example": "他自谦不过草木愚夫，不敢妄议国是。"
        },
        2191: {
            "pinyin": "cǎo shé huī xiàn",
            "meaning": "像草丛中的蛇留下的灰线，比喻事情发展留下的隐约线索。",
            "example": "案件表面平静，却处处可见草蛇灰线。"
        },
        2192: {
            "pinyin": "cái mào liǎng quán",
            "meaning": "才华与容貌都很出众。",
            "example": "她不仅业务能力强，亦算才貌两全。"
        },
        2193: {
            "pinyin": "cái mào shuāng jué",
            "meaning": "才华与容貌都达到绝顶，形容极为出众。",
            "example": "小说中的女主角被描写成才貌双绝。"
        },
        2194: {
            "pinyin": "cái mò zhī sǒu",
            "meaning": "才与墨并聚之地，比喻文人荟萃或藏书之所。",
            "example": "这间书斋可谓才墨之薮，常聚集一批文人雅士。"
        },
        2195: {
            "pinyin": "cái qīng dé bó",
            "meaning": "才华高而德行薄弱，形容有才却缺少修养。",
            "example": "若只恃才傲物，终究难免才轻德薄之评。"
        },
        2196: {
            "pinyin": "cái shū dé bó",
            "meaning": "才学疏浅、德行又薄，常作自谦之辞。",
            "example": "我不过才疏德薄，哪敢当此重任。"
        },
        2197: {
            "pinyin": "cái shū jì zhuō",
            "meaning": "才学浅、计谋拙，常用作自谦语。",
            "example": "在座诸公皆是高贤，我不过才疏计拙。"
        },
        2198: {
            "pinyin": "cái xiù rén wēi",
            "meaning": "才华出众而地位低微。",
            "example": "他虽才秀人微，却默默为集体做了许多事。"
        },
        2199: {
            "pinyin": "cái xué jiān yōu",
            "meaning": "才华与学问都十分出众。",
            "example": "这位青年学者可谓才学兼优，前途无量。"
        },
        2200: {
            "pinyin": "cái zhàn bā dǒu",
            "meaning": "自比拥有八斗之才，形容才华横溢或极其自负。",
            "example": "若一味认为自己才占八斗，便难以继续成长。"
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

    print(f"已为 2101–2200 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
