import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 为 201–300 条成语添加拼音、释义和例句
    enrich = {
        201: {
            "pinyin": "ǎi shēng tàn qì",
            "meaning": "发出叹息声，表示忧愁、烦闷或不满。",
            "example": "最近压力太大，他总是在那儿嗳声叹气。"
        },
        202: {
            "pinyin": "ǎi rén guān chǎng",
            "meaning": "比喻能力不足的人却站在显眼位置上指手画脚。",
            "example": "让一个外行来主导项目，简直是矮人观场。"
        },
        203: {
            "pinyin": "ǎi rén kàn xì",
            "meaning": "比喻眼界受限，看问题不全面。",
            "example": "只根据片面信息判断事情，无异于矮人看戏。"
        },
        204: {
            "pinyin": "ǎi zi guān chǎng",
            "meaning": "同“矮人观场”，比喻见识浅陋的人却居高位。",
            "example": "如果让矮子观场，难免误判形势。"
        },
        205: {
            "pinyin": "ài cái rú mìng",
            "meaning": "把人才看得像生命一样宝贵，极其爱惜人才。",
            "example": "这位领导一向爱才如命，广纳贤才。"
        },
        206: {
            "pinyin": "ài fù xián pín",
            "meaning": "喜欢富有的人而嫌弃贫穷的人。",
            "example": "只会爱富嫌贫的人，很难赢得真正的友谊。"
        },
        207: {
            "pinyin": "ài mò zhī zhù",
            "meaning": "心里同情却没有办法帮助。",
            "example": "看到他的遭遇，大家都感到爱莫之助。"
        },
        208: {
            "pinyin": "ài shēng wù sǐ",
            "meaning": "贪恋生存、害怕死亡。",
            "example": "战士不能爱生恶死，关键时刻要敢于牺牲。"
        },
        209: {
            "pinyin": "ài zé jiā zhū xī, è zé zhuì zhū yuān",
            "meaning": "形容爱憎极不平衡，对人偏爱或偏恶到了极端。",
            "example": "作为父母不能爱则加诸膝，恶则坠诸渊，要一视同仁。"
        },
        210: {
            "pinyin": "ài zhī yù qí shēng",
            "meaning": "喜欢一个人就希望他活着，形容爱得深切。",
            "example": "对孩子的感情，总是爱之欲其生。"
        },
        211: {
            "pinyin": "ài nán cóng mìng",
            "meaning": "难以照对方的意思去做，只好婉言拒绝。",
            "example": "这件事实在办不到，只能说一句碍难从命。"
        },
        212: {
            "pinyin": "ài zú ài shǒu",
            "meaning": "同“碍手碍脚”，形容受到很多限制，行动不便。",
            "example": "规矩太多，大家做事难免碍足碍手。"
        },
        213: {
            "pinyin": "ān cháng lǚ shùn",
            "meaning": "处于安定环境，循规蹈矩地顺着习俗行事。",
            "example": "他性格保守，一向安常履顺。"
        },
        214: {
            "pinyin": "ān cháng xí gù",
            "meaning": "安于现状，习惯旧有风俗。",
            "example": "如果大家都安常习故，改革就难以推进。"
        },
        215: {
            "pinyin": "ān fèn shǒu yǐ",
            "meaning": "安守本分，遵守自己该做的事（“已”为“己”的异写）。",
            "example": "他一生为人老实，安分守已。"
        },
        216: {
            "pinyin": "ān fèn shǒu jǐ",
            "meaning": "同“安分守己”，安守本分，不越规矩。",
            "example": "老人一家人安份守己，日子虽清苦却很踏实。"
        },
        217: {
            "pinyin": "ān fù xù qióng",
            "meaning": "安抚富人，体恤穷人，施政公正。",
            "example": "这套政策既能安富恤穷，又能促进发展。"
        },
        218: {
            "pinyin": "ān gù zhòng qiān",
            "meaning": "因留恋故土而不愿轻易迁移。",
            "example": "老人安故重迁，不愿离开乡下老屋。"
        },
        219: {
            "pinyin": "ān guó fù mín",
            "meaning": "使国家安定，使百姓富足。",
            "example": "历代仁政都以安国富民为目标。"
        },
        220: {
            "pinyin": "ān jiā lè yè",
            "meaning": "家庭安定，事业安稳。",
            "example": "只要社会太平，人人就能安家乐业。"
        },
        221: {
            "pinyin": "ān pín shǒu dào",
            "meaning": "安于贫穷，坚守道义。",
            "example": "他宁可安贫守道，也不肯违心谋利。"
        },
        222: {
            "pinyin": "ān rú pán shí",
            "meaning": "像盘中的大石一样稳固，比喻非常稳定牢靠。",
            "example": "在家人的支持下，他的心境安如盘石。"
        },
        223: {
            "pinyin": "ān rú tài shān",
            "meaning": "像泰山一样稳重、安定。",
            "example": "无论外界如何变化，他始终安如太山。"
        },
        224: {
            "pinyin": "ān ruò tài shān",
            "meaning": "同“安如泰山”，比喻极其稳固。",
            "example": "在科学依据的支撑下，我们的判断安若泰山。"
        },
        225: {
            "pinyin": "ān shēn lè yè",
            "meaning": "生活安定，工作安稳。",
            "example": "经过多年打拼，他终于安身乐业。"
        },
        226: {
            "pinyin": "ān shén dìng pò",
            "meaning": "安定精神，使惊恐的心平静下来。",
            "example": "医生几句话就像安神定魄的良药。"
        },
        227: {
            "pinyin": "ān shēng fú yè",
            "meaning": "安定生活，从事本业。",
            "example": "战乱结束，百姓又能安生服业。"
        },
        228: {
            "pinyin": "ān shēng lè yè",
            "meaning": "安定生活，愉快工作。",
            "example": "社会稳定，大家安生乐业。"
        },
        229: {
            "pinyin": "ān tǔ lè yè",
            "meaning": "安居故土，乐于从事本业。",
            "example": "政策改善后，农民得以安土乐业。"
        },
        230: {
            "pinyin": "ān tǔ zhòng jiù",
            "meaning": "留恋故土，重视旧有环境。",
            "example": "许多老人安土重旧，不愿搬到新小区。"
        },
        231: {
            "pinyin": "ān bù lí mǎ bèi, jiǎ bù lí jiāng shēn",
            "meaning": "鞍不离马背，甲不离将身，形容时刻准备战斗。",
            "example": "边防军人常年鞍不离马背，甲不离将身。"
        },
        232: {
            "pinyin": "ān mǎ láo juàn",
            "meaning": "长途奔波，骑马赶路而十分劳累。",
            "example": "他们一日奔波千里，早已鞍马劳倦。"
        },
        233: {
            "pinyin": "ān mǎ láo shén",
            "meaning": "奔波劳累，身心俱疲。",
            "example": "多日出差，使他鞍马劳神。"
        },
        234: {
            "pinyin": "àn gǔ zhī biàn",
            "meaning": "山谷和河岸都改变了，比喻世事巨变。",
            "example": "几十年过去，这里早已岸谷之变。"
        },
        235: {
            "pinyin": "àn rán dào mào",
            "meaning": "装出一本正经、道貌岸然的样子。",
            "example": "他当众岸然道貌，私下却另有打算。"
        },
        236: {
            "pinyin": "àn bīng bù jǔ",
            "meaning": "按住军队不出动，比喻暂不行动。",
            "example": "他选择按兵不举，静观形势发展。"
        },
        237: {
            "pinyin": "àn bīng shù jiǎ",
            "meaning": "收拾武器，停止战争。",
            "example": "两国议和后，双方按兵束甲。"
        },
        238: {
            "pinyin": "àn bù jiù bān",
            "meaning": "按照一定步骤、次序行事。",
            "example": "工程建设必须按步就班地推进。"
        },
        239: {
            "pinyin": "àn dàn wú guāng",
            "meaning": "颜色暗淡，没有光泽。",
            "example": "多年风吹日晒，使墙面黯淡无光。"
        },
        240: {
            "pinyin": "àn huì xiāo chén",
            "meaning": "心情抑郁消沉，显得暗淡无光。",
            "example": "接连失败让他一度黯晦消沉。"
        },
        241: {
            "pinyin": "àn rán shén shāng",
            "meaning": "神情黯淡，内心悲伤。",
            "example": "听到噩耗，他不禁黯然神伤。"
        },
        242: {
            "pinyin": "àn rán wú sè",
            "meaning": "神情黯淡，没有生气。",
            "example": "病中的他面容憔悴，黯然无色。"
        },
        243: {
            "pinyin": "áng áng zì ruò",
            "meaning": "神态昂扬，自信从容。",
            "example": "青年选手昂昂自若地走上赛场。"
        },
        244: {
            "pinyin": "áng rán zhí rù",
            "meaning": "昂首大步直入，形容气势雄健。",
            "example": "将军昂然直入营门，士气大振。"
        },
        245: {
            "pinyin": "áng rán zì ruò",
            "meaning": "昂首挺胸，神情自若。",
            "example": "面对质疑，他依旧昂然自若。"
        },
        246: {
            "pinyin": "áng tóu kuò bù",
            "meaning": "抬头大步行走，形容气概豪迈。",
            "example": "学生们昂头阔步走进操场。"
        },
        247: {
            "pinyin": "áng tóu tiān wài",
            "meaning": "抬头仰望天空，比喻志向远大。",
            "example": "年轻人应当昂头天外，胸怀天下。"
        },
        248: {
            "pinyin": "áng tóu tǐng xiōng",
            "meaning": "抬头挺胸，形容自信从容。",
            "example": "他昂头挺胸走进面试场。"
        },
        249: {
            "pinyin": "áng xiāo sǒng hè",
            "meaning": "高耸入云，形容山势高峻。",
            "example": "远处群峰昂霄耸壑，景色壮丽。"
        },
        250: {
            "pinyin": "áo shì qīng wù",
            "meaning": "同“傲世轻物”，看不起世人和事物。",
            "example": "他一向敖世轻物，难以与人相处。"
        },
        251: {
            "pinyin": "áo bù kě cháng",
            "meaning": "同“傲不可长”，骄傲之气不可滋长。",
            "example": "古人早就提醒我们敖不可长。"
        },
        252: {
            "pinyin": "áo xiáng zì dé",
            "meaning": "自由飞翔，心情自得。",
            "example": "鸟儿在天空遨翔自得。"
        },
        253: {
            "pinyin": "áo kū shòu dàn",
            "meaning": "在艰苦清淡的生活中忍受折磨。",
            "example": "他年轻时在山村熬枯受淡，坚持教书。"
        },
        254: {
            "pinyin": "áo qīng shǒu tán",
            "meaning": "在清苦寡淡的环境中坚守操守（“谈”为“淡”的异写）。",
            "example": "这些老先生一生熬清守谈，淡泊名利。"
        },
        255: {
            "pinyin": "áo qīng shòu dàn",
            "meaning": "忍受清苦淡泊的生活。",
            "example": "为了理想，他甘愿熬清受淡。"
        },
        256: {
            "pinyin": "áo yóu fèi huǒ",
            "meaning": "比喻耗费财力、人力。",
            "example": "这场豪华宴会实在是熬油费火。"
        },
        257: {
            "pinyin": "áo yá jí qū",
            "meaning": "文辞艰涩难懂。",
            "example": "这篇文章用词聱牙佶屈，不易理解。"
        },
        258: {
            "pinyin": "ào yuán yǒu líng",
            "meaning": "暗中得到有力的支援。",
            "example": "他关键时刻奥援有灵，终于转危为安。"
        },
        259: {
            "pinyin": "àn dǔ rú gù",
            "meaning": "局势安定如故。",
            "example": "骚乱平息后，城市很快按堵如故。"
        },
        260: {
            "pinyin": "àn tú suǒ jùn",
            "meaning": "按照图样寻找好马，比喻拘泥成法办事。",
            "example": "做研究不能只按图索骏，要勇于创新。"
        },
        261: {
            "pinyin": "àn bīng shù jiǎ",
            "meaning": "同“按兵束甲”，收拾兵器停止作战。",
            "example": "如今边境安宁，可以案兵束甲。"
        },
        262: {
            "pinyin": "àn dú zhī láo",
            "meaning": "文书工作带来的劳累。",
            "example": "整天处理文件，让人颇感案牍之劳。"
        },
        263: {
            "pinyin": "àn jiǎ xiū bīng",
            "meaning": "同“按甲休兵”，停止战争，休养士卒。",
            "example": "国家太平，便可案甲休兵。"
        },
        264: {
            "pinyin": "àn jiàn chēn mù",
            "meaning": "按剑怒目而视，形容愤怒的神情。",
            "example": "他被冤枉时几乎要案剑瞋目。"
        },
        265: {
            "pinyin": "àn wú liú dú",
            "meaning": "桌案上没有积压的文书，形容办事及时。",
            "example": "科室工作井井有条，几乎案无留牍。"
        },
        266: {
            "pinyin": "àn chuí dǎ rén",
            "meaning": "暗中殴打别人，比喻暗中加害。",
            "example": "做人要光明磊落，不能暗锤打人。"
        },
        267: {
            "pinyin": "àn dòu míng zhēng",
            "meaning": "暗中斗争，表面上公开争执。",
            "example": "两派之间暗斗明争已久。"
        },
        268: {
            "pinyin": "àn dù chén cāng",
            "meaning": "暗中采用别的手段，比喻暗中进行活动。",
            "example": "他表面退让，实则暗度陈仓。"
        },
        269: {
            "pinyin": "àn dù jīn zhēn",
            "meaning": "暗中传递信息或指点，比喻秘密相助。",
            "example": "关键时刻有人暗度金针，提醒了他。"
        },
        270: {
            "pinyin": "àn jiàn míng qiāng",
            "meaning": "指暗地和明处的攻击。",
            "example": "工作中既要防暗箭明枪，也要防流言蜚语。"
        },
        271: {
            "pinyin": "àn jiàn zhòng rén",
            "meaning": "被暗箭射中，比喻暗中遭人陷害。",
            "example": "他在官场上屡次暗箭中人。"
        },
        272: {
            "pinyin": "àn lǜ xī hóng",
            "meaning": "暗绿与淡红交织，形容幽雅的景色。",
            "example": "庭院里花木扶疏，暗绿稀红，别有情致。"
        },
        273: {
            "pinyin": "àn shì sī xīn",
            "meaning": "在暗中怀有私心。",
            "example": "做官若暗室私心，终会败露。"
        },
        274: {
            "pinyin": "àn shì wū lòu",
            "meaning": "黑屋漏雨，比喻处境艰难或心中有愧。",
            "example": "想到暗室屋漏的往事，他十分不安。"
        },
        275: {
            "pinyin": "áo yá jǐ kǒu",
            "meaning": "言语艰涩难懂。",
            "example": "这段话聱牙戟口，让人摸不着头脑。"
        },
        276: {
            "pinyin": "áo yá jí qǔ",
            "meaning": "同“聱牙诘屈”，形容文辞晦涩难懂。",
            "example": "他的报告写得聱牙诘曲，不够明了。"
        },
        277: {
            "pinyin": "áo yá jí qū",
            "meaning": "文辞艰涩曲折。",
            "example": "古书语言聱牙诘屈，初学者难以读懂。"
        },
        278: {
            "pinyin": "áo fèn lóng chóu",
            "meaning": "形容极度愤懑忧愁。",
            "example": "他满腔抱负无处施展，不免鳌愤龙愁。"
        },
        279: {
            "pinyin": "áo lǐ duó zūn",
            "meaning": "在众人之中夺取首位。",
            "example": "他凭实力在比赛中鳌里夺尊。"
        },
        280: {
            "pinyin": "áo míng biē yìng",
            "meaning": "鳌鸣鳖应，比喻互相呼应或相互酬答。",
            "example": "台上台下鳌鸣鳖应，气氛热烈。"
        },
        281: {
            "pinyin": "áo tóu dú zhàn",
            "meaning": "独占鳌头，比喻占据首位。",
            "example": "他在考试中鳌头独占。"
        },
        282: {
            "pinyin": "áo zhì jīng qū",
            "meaning": "形容气势宏大，像巨鳌与鲸鱼翻腾。",
            "example": "海上风浪仿佛鳌掷鲸呿，惊心动魄。"
        },
        283: {
            "pinyin": "áo zhì jīng tūn",
            "meaning": "形容气势吞吐山河。",
            "example": "大江奔流，如同鳌掷鲸吞。"
        },
        284: {
            "pinyin": "ān tǔ zhòng jū",
            "meaning": "安于故土，不愿远离家乡。",
            "example": "老人安土重居，不肯搬到城市。"
        },
        285: {
            "pinyin": "ān xīn lè yè",
            "meaning": "心情安定，乐于从事自己的事业。",
            "example": "他在新单位安心乐业，很少抱怨。"
        },
        286: {
            "pinyin": "ān xīn lè yì",
            "meaning": "内心安宁愉悦。",
            "example": "完成任务后，他觉得安心乐意。"
        },
        287: {
            "pinyin": "ān xīn luò yì",
            "meaning": "心情踏实，意愿满足。",
            "example": "事情妥善解决，大家都安心落意。"
        },
        288: {
            "pinyin": "ān yíng xià zhài",
            "meaning": "同“安营扎寨”，扎下营地。",
            "example": "部队在山脚安营下寨，准备休整。"
        },
        289: {
            "pinyin": "ān yú pán shí",
            "meaning": "安如盘石，极其稳固。",
            "example": "他们的合作关系安于盘石。"
        },
        290: {
            "pinyin": "ào màn wú lǐ",
            "meaning": "态度傲慢，不讲礼貌。",
            "example": "他对顾客傲慢无礼，影响极坏。"
        },
        291: {
            "pinyin": "ào nì yī qiè",
            "meaning": "轻视一切人和事。",
            "example": "他年少得志，渐有傲睨一切之态。"
        },
        292: {
            "pinyin": "ào rán tǐng lì",
            "meaning": "昂然挺立，毫不屈服。",
            "example": "大树在风中傲然挺立。"
        },
        293: {
            "pinyin": "cāng bái wú lì",
            "meaning": "颜色苍白，没有力量。",
            "example": "他病得脸色苍白无力。"
        },
        294: {
            "pinyin": "bā bǎi gū hán",
            "meaning": "指许多贫寒的读书人。",
            "example": "当年书院里八百孤寒寄望于科举。"
        },
        295: {
            "pinyin": "bā bài zhī jiāo",
            "meaning": "以八拜礼结成的盟交，指结义兄弟之交。",
            "example": "他们自小就是八拜之交。"
        },
        296: {
            "pinyin": "bā dǒu zhī cái",
            "meaning": "形容才华出众。",
            "example": "他文采斐然，人称八斗之才。"
        },
        297: {
            "pinyin": "bā fāng hū yìng",
            "meaning": "各方面互相响应、支持。",
            "example": "活动发起后，很快得到八方呼应。"
        },
        298: {
            "pinyin": "bā gōng shān shàng, cǎo mù jiē bīng",
            "meaning": "形容极度紧张时草木皆被看作敌兵。",
            "example": "他紧张得如临大敌，简直八公山上，草木皆兵。"
        },
        299: {
            "pinyin": "bā huāng zhī wài",
            "meaning": "极遥远的地方。",
            "example": "传说他游历至八荒之外。"
        },
        300: {
            "pinyin": "bā jiē jiǔ mò",
            "meaning": "城中的大街小巷。",
            "example": "节日期间，八街九陌到处张灯结彩。"
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

    print(f"已为 201–300 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
