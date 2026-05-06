import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 将 3801–3900 号成语的详细信息补充到 enrich 字典中
    enrich = {
        3801: {
            "pinyin": "fēng huán wù bìn",
            "meaning": "形容女子发髻如风吹云绕、鬓发如雾般轻柔，也形容头发蓬松飘逸的美态。",
            "example": "古画中的仕女风鬟雾鬓，姿态娴雅动人。"
        },
        3802: {
            "pinyin": "fēng huán yǔ bìn",
            "meaning": "形容女子鬓发如被风雨吹拂般轻盈飘洒，多用来描写女子秀丽的风姿。",
            "example": "她披衣立在廊下，风鬟雨鬓，更显几分柔情。"
        },
        3803: {
            "pinyin": "fēng jǐng bù shū",
            "meaning": "景色并没有什么改变，多用来感叹人事变迁、物是人非。",
            "example": "旧地重游，只觉风景不殊，人情已改。"
        },
        3804: {
            "pinyin": "fēng juǎn cán yún",
            "meaning": "本指狂风卷尽残云，后多比喻事物被迅速一扫而光，或饭菜被很快吃光。",
            "example": "一桌菜刚端上来，就被大家风卷残云般吃个精光。"
        },
        3805: {
            "pinyin": "fēng kǒu làng jiān",
            "meaning": "风头最劲处、浪头最高处，比喻矛盾冲突最激烈或舆论关注的中心位置。",
            "example": "事件曝光后，他一下子被推到了风口浪尖。"
        },
        3806: {
            "pinyin": "fēng liú cái zǐ",
            "meaning": "既有才华又风度潇洒的男子。",
            "example": "他年轻时是远近闻名的风流才子。"
        },
        3807: {
            "pinyin": "fēng liú rén wù",
            "meaning": "才情出众、品貌不凡的人物，多指在某个时代颇有影响和魅力的人。",
            "example": "屈原是楚国历史上的第一流风流人物。"
        },
        3808: {
            "pinyin": "fēng liú rú yǎ",
            "meaning": "既潇洒风流又文雅有礼，形容学识修养和气质都很出众。",
            "example": "这位老先生谈吐不凡，举止风流儒雅。"
        },
        3809: {
            "pinyin": "fēng liú tì tǎng",
            "meaning": "形容举止潇洒大方、风度不凡的样子。",
            "example": "他一身长衫缓步而来，风流倜傥，引人侧目。"
        },
        3810: {
            "pinyin": "fēng liú xiāo sǎ",
            "meaning": "形容人神情洒脱、气度不凡。",
            "example": "青年时的他风流潇洒，是许多人心中的偶像。"
        },
        3811: {
            "pinyin": "fēng liú yún sàn",
            "meaning": "风散云飞，比喻昔日的情爱、交游等关系消散无存。",
            "example": "当年的酒伴如今风流云散，各奔前程。"
        },
        3812: {
            "pinyin": "fēng liú yùn shì",
            "meaning": "指有关男女情爱的传闻或故事，多带暧昧意味。",
            "example": "这些风流韵事，早已成了茶余饭后的谈资。"
        },
        3813: {
            "pinyin": "fēng liú zuì guò",
            "meaning": "指沉迷酒色、风流放荡的过失，多用作自谦或调侃之词。",
            "example": "年轻时不免有些风流罪过，如今回想亦觉可笑。"
        },
        3814: {
            "pinyin": "fēng mǎ niú bù xiāng jí",
            "meaning": "出自《左传》，比喻事物彼此之间毫无关系或差异极大。",
            "example": "你说的那件事，跟我们讨论的主题风马牛不相及。"
        },
        3815: {
            "pinyin": "fēng mǐ yī shí",
            "meaning": "像风一样席卷、一时之间广为流行，形容事物非常盛行。",
            "example": "这种说法曾在网络上风靡一时。"
        },
        3816: {
            "pinyin": "fēng mù hán bēi",
            "meaning": "树被风吹而发出悲声，比喻父母去世，子女悲痛欲绝。",
            "example": "自从父亲去世，他每闻风木含悲，倍感孤单。"
        },
        3817: {
            "pinyin": "fēng píng bō xī",
            "meaning": "风息浪止，比喻纠纷或风波平息下来。",
            "example": "经过多方调解，这场矛盾终于风平波息。"
        },
        3818: {
            "pinyin": "fēng píng làng jìng",
            "meaning": "风平浪静，形容没有风浪，比喻局势平稳安定。",
            "example": "雨过天晴，江面风平浪静。"
        },
        3819: {
            "pinyin": "fēng qǐ shuǐ yǒng",
            "meaning": "风起水涌，形容声势浩大，事态迅猛发展。",
            "example": "改革政策一出台，社会反响风起水涌。"
        },
        3820: {
            "pinyin": "fēng qǐ yún yǒng",
            "meaning": "像风云涌动般迅速聚集，形容事物蓬勃兴起、气势磅礴。",
            "example": "创新创业之风在年轻人中风起云涌。"
        },
        3821: {
            "pinyin": "fēng qǐ yún zhēng",
            "meaning": "风云并起、蒸腾上升，形容局势迅速发展或群情激昂。",
            "example": "新技术的出现，使整个行业风起云蒸。"
        },
        3822: {
            "pinyin": "fēng qián cán zhú",
            "meaning": "风前的残烛，形容人衰老多病、行将就木的状态。",
            "example": "他自谦一把风前残烛，只盼再做点有益之事。"
        },
        3823: {
            "pinyin": "fēng qián yuè xià",
            "meaning": "微风吹拂、明月当空，多用来形容幽会或谈心的浪漫环境。",
            "example": "年轻时他们常在风前月下促膝长谈。"
        },
        3824: {
            "pinyin": "fēng qiáng zhèn mǎ",
            "meaning": "风中帆樯、阵前战马，形容战斗场面或军容十分壮观。",
            "example": "史书对当年风樯阵马的场景多有描写。"
        },
        3825: {
            "pinyin": "fēng qīng bì jué",
            "meaning": "政风清明、弊端消除，形容政治环境廉洁，社会风气良好。",
            "example": "只有不断反腐，才能真正达到风清弊绝。"
        },
        3826: {
            "pinyin": "fēng qīng yuè jiǎo",
            "meaning": "清风明月，多形容夜色清朗、环境幽静宜人。",
            "example": "小院里风清月皎，几位老友把酒闲谈。"
        },
        3827: {
            "pinyin": "fēng qīng yuè lǎng",
            "meaning": "微风清爽、月色明朗，形容夜晚的好天气。",
            "example": "在这风清月朗的夜晚，他写下了动人的诗句。"
        },
        3828: {
            "pinyin": "fēng qíng yuè zhài",
            "meaning": "风月情债，比喻男女之间难以了结的感情纠葛。",
            "example": "旧日的风情月债，总是在梦中隐约浮现。"
        },
        3829: {
            "pinyin": "fēng qù héng shēng",
            "meaning": "处处洋溢着幽默风趣，形容谈话或文章十分有趣。",
            "example": "他的演讲风趣横生，听众笑声不断。"
        },
        3830: {
            "pinyin": "fēng shēng hè lì, cǎo mù jiē bīng",
            "meaning": "风声鹤唳、草木皆兵，比喻人在惊恐之中疑神疑鬼、极度紧张。",
            "example": "兵败之后，士卒们风声鹤唳，草木皆兵。"
        },
        3831: {
            "pinyin": "fēng tiáo yǔ shùn",
            "meaning": "风调雨顺，形容风雨适时、农业丰收，也比喻社会安定。",
            "example": "但愿年年风调雨顺、五谷丰登。"
        },
        3832: {
            "pinyin": "fēng tǔ rén qíng",
            "meaning": "一个地方特有的自然环境和生活风俗。",
            "example": "旅行最大的乐趣之一，就是体会当地的风土人情。"
        },
        3833: {
            "pinyin": "fēng xiāo yǔ huì",
            "meaning": "风声萧瑟、雨色昏暗，形容天气阴冷凄清，也比喻处境凄凉。",
            "example": "在这风潇雨晦的夜里，他独自赶路。"
        },
        3834: {
            "pinyin": "fēng xìn nián huá",
            "meaning": "指青春年华如风信般易逝，也形容青春岁月的绚丽多变。",
            "example": "回想那段风信年华，总是充满诗意与憧憬。"
        },
        3835: {
            "pinyin": "fēng xíng cǎo yǎn",
            "meaning": "风一吹来，草就倒伏，比喻上行下效或政令教化迅速见效。",
            "example": "若为官者以身作则，风行草偃，自然民心归附。"
        },
        3836: {
            "pinyin": "fēng xíng shuǐ shàng",
            "meaning": "风在水面行走，比喻事物传播迅速、影响明显。",
            "example": "他的作品一经发表，便如风行水上，传遍全国。"
        },
        3837: {
            "pinyin": "fēng xíng yī shí",
            "meaning": "在一个时期里非常流行。",
            "example": "这种音乐风格曾经风行一时。"
        },
        3838: {
            "pinyin": "fēng xuán diàn chè",
            "meaning": "像旋风、闪电一样迅猛，形容速度极快。",
            "example": "救护车在公路上风旋电掣般驶过。"
        },
        3839: {
            "pinyin": "fēng xuě jiāo jiā",
            "meaning": "风雪同时袭来，形容天气恶劣，也比喻环境十分艰难。",
            "example": "他们在风雪交加的高原上坚持巡逻。"
        },
        3840: {
            "pinyin": "fēng yán cù yǔ",
            "meaning": "夹杂着酸溜溜意味的闲言碎语，多指挑拨离间或诽谤的话。",
            "example": "不要轻信那些风言醋语。"
        },
        3841: {
            "pinyin": "fēng yán fēng yǔ",
            "meaning": "随风飘散的议论，比喻没有根据的流言蜚语。",
            "example": "面对种种风言风语，他始终坦然以对。"
        },
        3842: {
            "pinyin": "fēng yǐng fū yǎn",
            "meaning": "风影摇曳、若有若无，比喻说话做事含糊其辞、不甚明确。",
            "example": "他回答得风影敷衍，让人难以捉摸真实想法."
        },
        3843: {
            "pinyin": "fēng yǔ bù cè",
            "meaning": "风雨变化难以预测，比喻事态多变、前途未卜。",
            "example": "当前局势风雨不测，更要保持冷静。"
        },
        3844: {
            "pinyin": "fēng yǔ bù gǎi",
            "meaning": "风雨再大也不改变，比喻意志坚定、坚持不懈。",
            "example": "多年来他风雨不改地坚持义务献血。"
        },
        3845: {
            "pinyin": "fēng yǔ bù tòu",
            "meaning": "连风雨都透不进去，形容建筑或防守十分严密。",
            "example": "这座城墙修得风雨不透、固若金汤。"
        },
        3846: {
            "pinyin": "fēng yǔ duì chuáng",
            "meaning": "朋友久别重逢，同榻对床、共听风雨，比喻知己相聚谈心。",
            "example": "多年老友重逢，一宿风雨对床，话不完的往事。"
        },
        3847: {
            "pinyin": "fēng yǔ jiāo jiā",
            "meaning": "风和雨一齐到来，形容天气恶劣，也比喻多种困难叠加。",
            "example": "在风雨交加的夜晚，他们仍坚守岗位。"
        },
        3848: {
            "pinyin": "fēng yǔ piāo yáo",
            "meaning": "在风雨中摇曳飘荡，比喻局势动荡、前途未卜。",
            "example": "那几年国家政局风雨飘摇。"
        },
        3849: {
            "pinyin": "fēng yǔ qī qī",
            "meaning": "风雨凄冷，形容环境萧瑟、心情悲凉。",
            "example": "他独自走在风雨凄凄的街头。"
        },
        3850: {
            "pinyin": "fēng yǔ rú huì",
            "meaning": "风雨如同黄昏般阴暗，比喻国家或社会处境黑暗动荡。",
            "example": "在那风雨如晦的年代，许多人仍坚守信仰。"
        },
        3851: {
            "pinyin": "fēng yǔ rú pán",
            "meaning": "风雨如同磐石般猛烈持久，形容风雨之大，也比喻形势严峻。",
            "example": "他们冒着风雨如磐的恶劣天气抢修大堤。"
        },
        3852: {
            "pinyin": "fēng yǔ tóng zhōu",
            "meaning": "在风雨中同坐一条船，比喻共同经历患难、同甘共苦。",
            "example": "我们是风雨同舟的战友。"
        },
        3853: {
            "pinyin": "fēng yǔ wú zǔ",
            "meaning": "无论刮风下雨都不会受阻，形容做事意志坚决、从不间断。",
            "example": "乡村义诊团队风雨无阻地坚持下乡。"
        },
        3854: {
            "pinyin": "fēng yǔ xiāo tiáo",
            "meaning": "风雨凄冷、景象萧条，也比喻经济衰落或人心不振。",
            "example": "战乱过后，城池一片风雨萧条。"
        },
        3855: {
            "pinyin": "fēng yún biàn huàn",
            "meaning": "风云变化无常，比喻局势或世事瞬息万变。",
            "example": "在风云变幻的时代，更需要坚定的信念。"
        },
        3856: {
            "pinyin": "fēng yún biàn tài",
            "meaning": "风云时起时落、变化莫测，形容形势险恶多变。",
            "example": "股市风云变态，投资需格外谨慎。"
        },
        3857: {
            "pinyin": "fēng yún jì huì",
            "meaning": "风云际会，喻英雄豪杰在动荡时代相会建功。",
            "example": "乱世之中，正是风云际会、建功立业的时机。"
        },
        3858: {
            "pinyin": "fēng yún rén wù",
            "meaning": "在风云变幻的时代中颇有影响的人物，多指英雄豪杰或重要人物。",
            "example": "他是那个年代著名的风云人物。"
        },
        3859: {
            "pinyin": "fēng yún tū biàn",
            "meaning": "风云突然变化，比喻局势骤然发生重大变化。",
            "example": "一纸公文下达，市场格局风云突变。"
        },
        3860: {
            "pinyin": "fēng yún yuè lù",
            "meaning": "风云月露，多指自然景物，也比喻风花雪月、儿女情长之事。",
            "example": "他早已把那些风云月露的往事看淡了。"
        },
        3861: {
            "pinyin": "fēng yún zhī zhì",
            "meaning": "如风云般壮阔的志向，形容胸怀远大、抱负不凡。",
            "example": "少年自当怀有风云之志，不负好时光。"
        },
        3862: {
            "pinyin": "fēng zhì yǔ mù",
            "meaning": "在风中梳栉、在雨中沐浴，比喻长期在外奔波劳苦。",
            "example": "边防战士年复一年风栉雨沐，守护着祖国边疆。"
        },
        3863: {
            "pinyin": "fēng zhōng bǐng zhú",
            "meaning": "在风中点烛，形容处境危险、难以维持，也比喻生命垂危。",
            "example": "这项事业若无人支持，无异于风中秉烛。"
        },
        3864: {
            "pinyin": "fēng zhōng zhī zhú",
            "meaning": "风中的蜡烛，比喻随时可能熄灭的生命或事业。",
            "example": "老人自喻风中之烛，更加珍惜当下。"
        },
        3865: {
            "pinyin": "fēng zhú cán nián",
            "meaning": "晚年如风中残烛，形容人年老体衰、行将就木。",
            "example": "他虽至风烛残年，仍关心国家大事。"
        },
        3866: {
            "pinyin": "fēng zhú zhī nián",
            "meaning": "晚景像风中之烛，形容人到了十分衰老的年纪。",
            "example": "在风烛之年得到亲人陪伴，是莫大的安慰。"
        },
        3867: {
            "pinyin": "féng chǎng zuò xì",
            "meaning": "赶上场合便演一出戏，比喻权且应付或不很认真的态度。",
            "example": "他不过是逢场作戏，别太当真。"
        },
        3868: {
            "pinyin": "féng jūn zhī è",
            "meaning": "遇到君主的恶念而迎合它，比喻助长别人的坏主意。",
            "example": "身为臣子若逢君之恶，必招来祸患。"
        },
        3869: {
            "pinyin": "féng rén shuō xiàng",
            "meaning": "见到人就替别人说好话，比喻到处为人说情、荐举他人。",
            "example": "他为朋友四处逢人说项，终于帮忙争取到机会。"
        },
        3870: {
            "pinyin": "féng shān kāi lù",
            "meaning": "遇山就开路，形容排除万难、勇往直前。",
            "example": "面对困难，我们要逢山开路，遇水架桥。"
        },
        3871: {
            "pinyin": "féng shí yù jié",
            "meaning": "遇到节日时令，后来也指逢年过节或适逢好时机。",
            "example": "逢时遇节，他总记得给长辈送去问候。"
        },
        3872: {
            "pinyin": "féng xiōng huà jí",
            "meaning": "遇到凶险能化为吉祥，比喻逢凶化吉、转危为安。",
            "example": "多亏众人相助，这次事故才得以逢凶化吉。"
        },
        3873: {
            "pinyin": "fěng yī quàn bǎi",
            "meaning": "讽刺一个人可以劝诫很多人，比喻以个别为例警告大众。",
            "example": "这篇文章通过一个反面人物讽一劝百。"
        },
        3874: {
            "pinyin": "fèng gōng bù ē",
            "meaning": "奉公守法而不阿附权贵，形容为官清正，不徇私情。",
            "example": "他一生奉公不阿，深得百姓信赖。"
        },
        3875: {
            "pinyin": "fèng gōng shǒu fǎ",
            "meaning": "恪守公事、遵守法律，形容作风正派、严于律己。",
            "example": "司法人员更应奉公守法，不徇私情。"
        },
        3876: {
            "pinyin": "fèng gōng zhèng jǐ",
            "meaning": "办事公正、修身律己，形容为官者严守操守。",
            "example": "为政之要，在于奉公正己。"
        },
        3877: {
            "pinyin": "fèng lìng chéng jiào",
            "meaning": "恭敬地接受命令与教诲，形容态度恭顺。",
            "example": "学生们对师长之言，当奉令承教。"
        },
        3878: {
            "pinyin": "fèng mìng wéi jǐn",
            "meaning": "奉行命令唯恐不慎，形容对上命极端谨慎、顺从。",
            "example": "军中纪律严明，士兵奉命唯谨。"
        },
        3879: {
            "pinyin": "fèng ruò shén míng",
            "meaning": "把某人或某事当作神明般崇拜，形容极端迷信或崇敬。",
            "example": "部分粉丝对偶像奉若神明。"
        },
        3880: {
            "pinyin": "fèng tiān chéng yùn",
            "meaning": "奉天命而承受帝运，古代皇帝诏书常用语。",
            "example": "诏书开头往往写着奉天承运，皇帝诏曰。"
        },
        3881: {
            "pinyin": "fèng tóu shǔ cuàn",
            "meaning": "像老鼠一样抱着头乱窜，形容人惊慌逃窜的样子。",
            "example": "敌军溃败，如丧家之犬奉头鼠窜。"
        },
        3882: {
            "pinyin": "fèng wéi guī niè",
            "meaning": "把某种言论或制度当作准则，形容极力尊崇并加以效法。",
            "example": "他把老师的教诲奉为圭臬，一生谨记。"
        },
        3883: {
            "pinyin": "fèng wéi kǎi mó",
            "meaning": "把某人当作楷模，极力学习效法。",
            "example": "许多青年把这位科学家奉为楷模。"
        },
        3884: {
            "pinyin": "fèng wéi zhì bǎo",
            "meaning": "当作极其珍贵的宝物，形容十分珍视。",
            "example": "这封亲笔信被他奉为至宝，妥善收藏。"
        },
        3885: {
            "pinyin": "fèng xíng gù shì",
            "meaning": "依照旧例办事，形容拘泥成规、缺乏创新。",
            "example": "他办事一味奉行故事，缺少变通。"
        },
        3886: {
            "pinyin": "fèng yáng rén fēng",
            "meaning": "宣扬别人的仁德之风，形容大加赞颂、推崇。",
            "example": "史书对这位清官多有奉扬仁风的记载。"
        },
        3887: {
            "pinyin": "fèng guān xiá pèi",
            "meaning": "凤冠霞帔，古代新娘礼服的华美装束，常用来指传统婚礼。",
            "example": "她身着凤冠霞帔，在亲友祝福中出嫁。"
        },
        3888: {
            "pinyin": "fèng huáng lái yí",
            "meaning": "凤凰飞来自我仪容，古代比喻贤才来朝或吉祥的征兆。",
            "example": "贤士云集，如凤凰来仪。"
        },
        3889: {
            "pinyin": "fèng huáng yú fēi",
            "meaning": "比喻夫妻恩爱和谐，或比喻才德相当的两人相得益彰。",
            "example": "这对伉俪琴瑟和鸣，堪称凤凰于飞。"
        },
        3890: {
            "pinyin": "fèng huáng zài nú",
            "meaning": "凤凰被关在笼中，比喻贤才受困、不得志。",
            "example": "他怀才不遇，如同凤凰在笯。"
        },
        3891: {
            "pinyin": "fèng máo jì měi",
            "meaning": "像凤毛般珍贵、美好，比喻子孙能继承先辈美德。",
            "example": "后辈若能凤毛济美，先人足慰。"
        },
        3892: {
            "pinyin": "fèng máo lín jiǎo",
            "meaning": "凤的羽毛、麟的角，比喻非常难得、极其珍贵的人或事物。",
            "example": "这样的天才可谓凤毛麟角。"
        },
        3893: {
            "pinyin": "fèng mí luán hé",
            "meaning": "形容乐声和鸣婉转，也比喻夫妻和美、歌舞华丽。",
            "example": "乐队合奏时，音色宛如凤靡鸾吪。"
        },
        3894: {
            "pinyin": "fèng míng zhāo yáng",
            "meaning": "凤凰在朝阳中鸣叫，比喻贤人出仕、太平兴盛的景象。",
            "example": "史书常以凤鸣朝阳来形容圣君贤臣相遇。"
        },
        3895: {
            "pinyin": "fèng xiāo tóng cháo",
            "meaning": "凤凰与枭鸟共处一巢，比喻贤人与恶人混杂在一起。",
            "example": "他不愿与小人同流合污，哪堪凤枭同巢。"
        },
        3896: {
            "pinyin": "fó kǒu shé xīn",
            "meaning": "嘴里说的是佛，心里却像蛇一样狠毒，形容口蜜腹剑、居心险恶。",
            "example": "他表面慈悲，实则佛口蛇心。"
        },
        3897: {
            "pinyin": "fó shì jīn zhuāng, rén shì yī zhuāng",
            "meaning": "佛要金身装饰，人要衣服装饰，比喻外表装饰对形象的重要性。",
            "example": "常言道佛是金妆，人是衣妆，仪表也很关键。"
        },
        3898: {
            "pinyin": "fó tóu jiā huì",
            "meaning": "在佛像头上抹上污秽，比喻对崇高事物的玷污或亵渎。",
            "example": "歪曲先贤原意，无异于佛头加秽。"
        },
        3899: {
            "pinyin": "fó tóu zhuó fèn",
            "meaning": "在佛头上涂抹粪便，比喻对神圣事物的极大亵渎。",
            "example": "捏造圣贤丑闻如同佛头着粪，令人不齿。"
        },
        3900: {
            "pinyin": "fó yǎn xiāng kàn",
            "meaning": "以佛的慈悲之眼来看待一切，形容宽容、慈和的态度。",
            "example": "他总是佛眼相看，对人多一分宽厚。"
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

    print(f"已为 3801–3900 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
