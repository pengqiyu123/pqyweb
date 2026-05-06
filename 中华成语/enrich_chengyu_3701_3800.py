import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 将 3701–3800 号成语的详细信息补充到 enrich 字典中
    enrich = {
        3701: {
            "pinyin": "fēn shēn wú shù",
            "meaning": "形容事情太多，一个人根本忙不过来，好像分出好几个身子也不够用。",
            "example": "眼看项目扎堆上线，他简直分身无术。"
        },
        3702: {
            "pinyin": "fēn shǒu yào jīn",
            "meaning": "分别镇守重要关口，比喻把骨干力量布置在关键岗位上。",
            "example": "几位老同志分守要津，把好单位的关键环节。"
        },
        3703: {
            "pinyin": "fēn tíng kàng lǐ",
            "meaning": "站在庭院两侧彼此行礼，原形容礼节周到，后多指平起平坐、不相逊色。",
            "example": "这两家企业如今已能与国外巨头分庭抗礼。"
        },
        3704: {
            "pinyin": "fēn wén bù míng",
            "meaning": "连一分钱都没有，形容极端贫穷。",
            "example": "他刚毕业时分文不名，全靠朋友接济。"
        },
        3705: {
            "pinyin": "fēn wén bù qǔ",
            "meaning": "一分钱都不拿，形容为人清廉或极有骨气。",
            "example": "面对贿赂，他分文不取，严词拒绝。"
        },
        3706: {
            "pinyin": "fēn wén bù zhí",
            "meaning": "连一分钱的价值都没有，形容毫无价值或极端鄙视。",
            "example": "这种违反原则的胜利，在他看来分文不值。"
        },
        3707: {
            "pinyin": "fēn wǒ bēi gēng",
            "meaning": "把自己的一杯肉羹分给别人，比喻与人分享利益或分一杯羹。",
            "example": "新产业起步，他也想在其中分我杯羹。"
        },
        3708: {
            "pinyin": "fēn xiāng mài lǚ",
            "meaning": "分卖香火钱和鞋履，比喻在利益分配中过分计较，各行其是。",
            "example": "若各自分香卖履，只顾小账，不利于整体发展。"
        },
        3709: {
            "pinyin": "fēn xíng tóng qì",
            "meaning": "分体却同源之气，比喻同族同气、关系极为密切。",
            "example": "兄弟本是分形同气，不该为一点小利反目。"
        },
        3710: {
            "pinyin": "fēn fēn rǎng rǎng",
            "meaning": "形容人来人往、声音嘈杂的样子。",
            "example": "广场上人声鼎沸，纷纷攘攘直到深夜。"
        },
        3711: {
            "pinyin": "fēn fēn yáng yáng",
            "meaning": "形容雪花、花瓣、纸屑等纷纷飘落的样子，也形容众多纷乱的景象。",
            "example": "大雪纷纷扬扬地下了一整夜。"
        },
        3712: {
            "pinyin": "fēn hóng hài lǜ",
            "meaning": "红绿交错、色彩纷繁，形容景物绚丽迷离。",
            "example": "园中花木纷红骇绿，令人目不暇接。"
        },
        3713: {
            "pinyin": "fēn luàn rú má",
            "meaning": "混乱得像一团麻线，形容局面极其纷乱无序。",
            "example": "没有统一规划，管理自然纷乱如麻。"
        },
        3714: {
            "pinyin": "fēn yún zá tà",
            "meaning": "事情众多而杂乱，议论纷繁、头绪复杂。",
            "example": "会上意见纷纭杂沓，需要有人归纳梳理。"
        },
        3715: {
            "pinyin": "fēn zhì tà lái",
            "meaning": "形容人或事物不断地接连而来。",
            "example": "节日期间游客纷至沓来，古城一片热闹。"
        },
        3716: {
            "pinyin": "fēn fāng fù yù",
            "meaning": "香气浓郁四溢，形容花草或环境香气馥郁。",
            "example": "花园里芬芳馥郁，令人心旷神怡。"
        },
        3717: {
            "pinyin": "fén gāo jì guǐ",
            "meaning": "点灯熬油、连夜工作，比喻勤奋用功不分昼夜。",
            "example": "备战高考时，他常常焚膏继晷苦读。"
        },
        3718: {
            "pinyin": "fén gǔ yáng huī",
            "meaning": "把骨头烧成灰撒向空中，比喻严厉惩处或痛恨之极。",
            "example": "叛国之罪，古人往往欲其焚骨扬灰。"
        },
        3719: {
            "pinyin": "fén lín ér liè",
            "meaning": "烧毁森林以便围猎，喻为一时之利而不顾长远后果。",
            "example": "只顾眼前收益而破坏环境，无异于焚林而猎。"
        },
        3720: {
            "pinyin": "fén lín ér tián, jié zé ér yú",
            "meaning": "烧林打猎、抽干水泽捕鱼，比喻只图眼前利益，不顾长远，最终自食其果。",
            "example": "粗放式开发资源，就像焚林而田，竭泽而渔。"
        },
        3721: {
            "pinyin": "fén qín zhǔ hè",
            "meaning": "烧琴煮鹤，比喻不解风雅，粗暴对待珍贵事物。",
            "example": "在古迹上乱刻乱画，无异于焚琴煮鹤。"
        },
        3722: {
            "pinyin": "fén shū kēng rú",
            "meaning": "焚烧典籍、活埋儒生，比喻残酷迫害文化与知识分子。",
            "example": "历史上的焚书坑儒给后世留下了惨痛教训。"
        },
        3723: {
            "pinyin": "fén xiāng lǐ bài",
            "meaning": "焚香行礼叩拜，多指宗教祭祀或礼佛活动。",
            "example": "新年时香客纷纷前来焚香礼拜。"
        },
        3724: {
            "pinyin": "fén zhōu pò fǔ",
            "meaning": "烧船砸釜，比喻下定决心、不留退路地去做一件事。",
            "example": "创业之初，他便有焚舟破釜的勇气。"
        },
        3725: {
            "pinyin": "fěn bái dài hēi",
            "meaning": "用粉饰白、用黛画黑，形容女子妆容精致，也可指景物色彩分明。",
            "example": "仕女画中粉白黛黑，线条细腻。"
        },
        3726: {
            "pinyin": "fěn bái dài lǜ",
            "meaning": "粉妆玉肤、黛眉点绿，形容环境或服饰色彩艳丽。",
            "example": "春山如黛，林木间粉白黛绿，美不胜收。"
        },
        3727: {
            "pinyin": "fěn miàn yóu tóu",
            "meaning": "脸上扑粉、头上油亮，形容过分修饰的庸脂俗粉。",
            "example": "他不喜欢浮华做派，更厌恶粉面油头的虚伪。"
        },
        3728: {
            "pinyin": "fěn mò dēng chǎng",
            "meaning": "涂粉抹墨登上舞台，比喻登上政治或舆论舞台，多带讽刺意味。",
            "example": "一些投机分子借机粉墨登场，博取眼球。"
        },
        3729: {
            "pinyin": "fěn shēn suì gǔ",
            "meaning": "身体粉碎、骨头折断，多用来形容不惜牺牲一切的决心，或罪大恶极该受严惩。",
            "example": "为报国恩，纵使粉身碎骨也在所不辞。"
        },
        3730: {
            "pinyin": "fěn shì tài píng",
            "meaning": "掩饰矛盾和危机，虚假地表现一片太平景象。",
            "example": "单凭粉饰太平的报表，并不能掩盖企业的隐患。"
        },
        3731: {
            "pinyin": "fěn zhuāng yù zhuó",
            "meaning": "粉饰如妆、玉石雕琢，比喻装饰得十分华美精致。",
            "example": "雪后山川如同粉妆玉琢，分外妖娆。"
        },
        3732: {
            "pinyin": "fèn nèi zhī shì",
            "meaning": "本分之内应当完成的事情。",
            "example": "照顾好客户是我们分内之事。"
        },
        3733: {
            "pinyin": "fèn wài yāo ráo",
            "meaning": "格外妩媚动人，多形容景色或姿态非常秀美。",
            "example": "春风拂过，桃李分外妖娆。"
        },
        3734: {
            "pinyin": "fèn rán zuò sè",
            "meaning": "因愤怒而变脸，形容大为恼火的样子。",
            "example": "听到有人诋毁同伴，他立刻忿然作色。"
        },
        3735: {
            "pinyin": "fèn bù yù shēng",
            "meaning": "愤怒到极点，几乎不想活下去，形容极端悲愤。",
            "example": "面对国破家亡，他一度愤不欲生。"
        },
        3736: {
            "pinyin": "fèn fèn bù píng",
            "meaning": "心中充满不平之气，表示强烈不满。",
            "example": "对不公的待遇，大家都愤愤不平。"
        },
        3737: {
            "pinyin": "fèn shì jí sú",
            "meaning": "对黑暗现实满怀愤恨，憎恶世俗庸俗之风。",
            "example": "许多思想家都曾愤世嫉俗，试图唤醒民众。"
        },
        3738: {
            "pinyin": "fèn bù gù shēn",
            "meaning": "在紧要关头顾不上个人安危，勇往直前。",
            "example": "救火时他奋不顾身冲进火场。"
        },
        3739: {
            "pinyin": "fèn fā dǎo lì",
            "meaning": "振作精神，奋起用力，形容意气奋发、行为积极。",
            "example": "青年人应奋发蹈厉，肩负时代使命。"
        },
        3740: {
            "pinyin": "fèn fā tú qiáng",
            "meaning": "振作精神，努力谋求强盛或进步。",
            "example": "面对差距，只能奋发图强。"
        },
        3741: {
            "pinyin": "fèn fā yǒu wéi",
            "meaning": "精神振奋，有所作为，形容进取有为的状态。",
            "example": "一批奋发有为的年轻干部走上了重要岗位。"
        },
        3742: {
            "pinyin": "fèn mèi ér qǐ",
            "meaning": "挥动衣袖而起身行动，形容情绪激动，下定决心。",
            "example": "听完报告，他奋袂而起，主动请缨。"
        },
        3743: {
            "pinyin": "fèn qǐ zhí zhuī",
            "meaning": "鼓起劲头紧紧追赶，力图赶上或超过。",
            "example": "落后地区正奋起直追，缩小差距。"
        },
        3744: {
            "pinyin": "fèn yǒng dāng xiān",
            "meaning": "奋勇争先，冲在最前面。",
            "example": "在抗灾一线，党员干部纷纷奋勇当先。"
        },
        3745: {
            "pinyin": "fèn tǔ bù rú",
            "meaning": "连泥土都不如，比喻极端轻贱某物或某人。",
            "example": "在他眼里，名利不过粪土不如。"
        },
        3746: {
            "pinyin": "fēng fù duō cǎi",
            "meaning": "内容或形式丰富多样、色彩斑斓。",
            "example": "校园生活丰富多采，给学生留下了美好回忆。"
        },
        3747: {
            "pinyin": "fēng gōng wěi jì",
            "meaning": "功劳大、业绩显著。",
            "example": "他在扶贫工作中立下丰功伟绩。"
        },
        3748: {
            "pinyin": "fēng hēng yù dà",
            "meaning": "出自《易经》，形容富足安乐、前景广大。",
            "example": "先贤所说丰亨豫大，正是太平盛世的写照。"
        },
        3749: {
            "pinyin": "fēng jīn duō lì",
            "meaning": "筋骨丰实、有力，形容人身材强健。",
            "example": "这些运动员个个丰筋多力。"
        },
        3750: {
            "pinyin": "fēng nián rěn suì",
            "meaning": "年成丰收，庄稼成熟，形容风调雨顺的好年景。",
            "example": "连续几年丰年稔岁，村民的日子越过越好。"
        },
        3751: {
            "pinyin": "fēng nián yù huāng nián gǔ",
            "meaning": "好年景时粮食如玉般珍贵，荒年时一粒谷也难得，比喻世事无常，要居安思危。",
            "example": "长辈常以丰年玉荒年谷相劝，要我们节约粮食。"
        },
        3752: {
            "pinyin": "fēng qǔ kè yǔ",
            "meaning": "苛刻地搜刮百姓财物，贪多而不顾民生。",
            "example": "暴政丰取刻与，终致民怨沸腾。"
        },
        3753: {
            "pinyin": "fēng shén chuò yuē",
            "meaning": "神采丰盈、举止优雅，形容女子体态轻盈、气质高雅。",
            "example": "她举止端庄，丰神绰约。"
        },
        3754: {
            "pinyin": "fēng shén yì cǎi",
            "meaning": "风采非凡，神情焕发。",
            "example": "这位老艺术家虽已年迈，仍丰神异彩。"
        },
        3755: {
            "pinyin": "fēng yī zú shí",
            "meaning": "衣食充足、生活富裕。",
            "example": "改革开放让千家万户丰衣足食。"
        },
        3756: {
            "pinyin": "fēng guān xǔ yuàn",
            "meaning": "用官职和允诺作为诱饵，多指以利益收买人心。",
            "example": "他靠封官许愿来笼络人心。"
        },
        3757: {
            "pinyin": "fēng hú è mò",
            "meaning": "封胡林、遏末水，本指守边要地，后比喻防守外患。",
            "example": "古代边将被寄望封胡遏末，保境安民。"
        },
        3758: {
            "pinyin": "fēng qī yìn zǐ",
            "meaning": "因功受封，妻子得封号、子孙享荫泽，形容功成名就、光耀门楣。",
            "example": "古人立下战功，往往可以封妻荫子。"
        },
        3759: {
            "pinyin": "fēng shǐ cháng shé",
            "meaning": "像大猪和长蛇一样残暴贪婪，比喻残酷贪暴的人。",
            "example": "史书中多有封豕长蛇般的权臣。"
        },
        3760: {
            "pinyin": "fēng fěi zhī cǎi",
            "meaning": "采摘葑菜和菲菜，比喻不计小恶，重在察其大节。",
            "example": "对一时的过失不必穷追不舍，当念葑菲之采。"
        },
        3761: {
            "pinyin": "fēng huí lù zhuǎn",
            "meaning": "山峰回环、道路曲折，比喻事情出现转机或形势好转。",
            "example": "谈判一度陷入僵局，但很快峰回路转。"
        },
        3762: {
            "pinyin": "fēng gǔ bù xī",
            "meaning": "烽烟与战鼓从不停歇，形容战事频仍、局势紧张。",
            "example": "边关烽鼓不息，消息不断传来。"
        },
        3763: {
            "pinyin": "fēng huǒ lián nián",
            "meaning": "战火连年不断，形容长期处于战争状态。",
            "example": "那片土地曾烽火连年，民不聊生。"
        },
        3764: {
            "pinyin": "fēng huǒ lián tiān",
            "meaning": "战火整天燃烧，形容战争极为频繁激烈。",
            "example": "敌军进犯时，边疆烽火连天。"
        },
        3765: {
            "pinyin": "fēng huǒ sì qǐ",
            "meaning": "到处燃起战火，形容各地纷纷爆发战争或动乱。",
            "example": "内乱爆发后，全国烽火四起。"
        },
        3766: {
            "pinyin": "fēng chài yǒu dú",
            "meaning": "蜜蜂与蝎子都有毒，比喻小人伺机害人。",
            "example": "身边若多蜂虿有毒之徒，行事务必谨慎。"
        },
        3767: {
            "pinyin": "fēng chài zuò yú huái xiù",
            "meaning": "毒蜂毒蝎藏在衣袖之间，比喻祸患潜伏在身边。",
            "example": "若不防微杜渐，小人之害犹如蜂虿作于怀袖。"
        },
        3768: {
            "pinyin": "fēng mù chái shēng",
            "meaning": "眼睛像蜂眼、声音似豺嚎，形容人相貌声音阴毒可憎。",
            "example": "传说中的恶吏蜂目豺声，令人闻风丧胆。"
        },
        3769: {
            "pinyin": "fēng tún yǐ jù",
            "meaning": "像蜂群与蚁群那样聚集，形容人众多而拥挤。",
            "example": "市集上商贩蜂屯蚁聚，十分热闹。"
        },
        3770: {
            "pinyin": "fēng yōng ér lái",
            "meaning": "像蜂群一样涌来，形容人群大量而迅速地聚拢。",
            "example": "消息一出，顾客蜂拥而来。"
        },
        3771: {
            "pinyin": "fēng bù kě dāng",
            "meaning": "兵锋锐利无比，难以抵挡，形容来势汹汹、锐不可当。",
            "example": "这支新军士气高昂，其锋不可当。"
        },
        3772: {
            "pinyin": "fēng fā yùn liú",
            "meaning": "文笔锋利而韵味流转，形容文章或书法遒劲有致。",
            "example": "他的行书锋发韵流，颇有大家风范。"
        },
        3773: {
            "pinyin": "fēng máng bī rén",
            "meaning": "锋芒太过显露，使人难以接近或感到压力。",
            "example": "他说话过于尖刻，锋芒逼人。"
        },
        3774: {
            "pinyin": "fēng máng bì lù",
            "meaning": "锐气、才华完全显露出来，多含褒义或中性。",
            "example": "年轻作者在这部作品中锋芒毕露。"
        },
        3775: {
            "pinyin": "fēng máng bù lù",
            "meaning": "有才华却不轻易显露，形容内敛持重。",
            "example": "他一向锋芒不露，但关键时刻总能脱颖而出。"
        },
        3776: {
            "pinyin": "fēng máng suǒ xiàng",
            "meaning": "锋利之处所指向的地方，比喻进攻或努力的目标。",
            "example": "改革的锋芒所向，是顽固的旧观念。"
        },
        3777: {
            "pinyin": "fēng bù míng tiáo",
            "meaning": "风吹树木而枝条不动，形容风平气和或政治清明。",
            "example": "此地风不鸣条，百姓安居乐业。"
        },
        3778: {
            "pinyin": "fēng cān lù sù",
            "meaning": "以风为餐、以露为宿，形容旅途艰辛或长期在外奔波。",
            "example": "巡逻队在边境风餐露宿，守护一方平安。"
        },
        3779: {
            "pinyin": "fēng chè léi xíng",
            "meaning": "像风被拉扯、雷电行走一样迅疾，形容速度极快。",
            "example": "救援车风掣雷行赶往现场。"
        },
        3780: {
            "pinyin": "fēng chén lù lù",
            "meaning": "尘土仆仆、忙忙碌碌，形容奔波劳碌的样子。",
            "example": "他为生计风尘碌碌，难得休息。"
        },
        3781: {
            "pinyin": "fēng chén pú pú",
            "meaning": "满身风尘，形容旅途劳顿或奔波不息。",
            "example": "他风尘仆仆地赶回家乡。"
        },
        3782: {
            "pinyin": "fēng chén zhī biàn",
            "meaning": "战乱或局势动荡的变化，形容时局纷乱。",
            "example": "在风尘之变中，许多家庭被迫流离失所。"
        },
        3783: {
            "pinyin": "fēng chí diàn chè",
            "meaning": "像风驰电掣般迅速，形容速度极快。",
            "example": "高铁在大地上风驰电掣。"
        },
        3784: {
            "pinyin": "fēng chuī cǎo dòng",
            "meaning": "风一吹草就摇动，比喻情况稍有变化就引起警觉或波动。",
            "example": "局势紧张之时，风吹草动都会引发猜疑。"
        },
        3785: {
            "pinyin": "fēng chuī làng dǎ",
            "meaning": "风吹浪打，形容环境恶劣或经受种种磨难。",
            "example": "这艘小船在风吹浪打中艰难前行。"
        },
        3786: {
            "pinyin": "fēng chuī yǔ dǎ",
            "meaning": "风雨交加地冲击，形容遭受多种打击和磨难。",
            "example": "这座老房子经受住了多年风吹雨打。"
        },
        3787: {
            "pinyin": "fēng cóng hǔ, yún cóng lóng",
            "meaning": "风随老虎而起，云随蛟龙而行，比喻英雄豪杰自有相应的气势和追随者。",
            "example": "真正的领袖往往风从虎，云从龙。"
        },
        3788: {
            "pinyin": "fēng dāo shuāng jiàn",
            "meaning": "像风中的刀、霜中的剑一样寒冷刺骨，比喻恶劣的环境或尖刻的言辞。",
            "example": "他在风刀霜剑般的岁月里依然坚守信念。"
        },
        3789: {
            "pinyin": "fēng dù piān piān",
            "meaning": "形容举止洒脱、风度翩然的样子。",
            "example": "那位青年风度翩翩，颇得长者喜爱。"
        },
        3790: {
            "pinyin": "fēng fēng huǒ huǒ",
            "meaning": "形容人性格急躁、行动匆忙，或场面热闹喧嚣。",
            "example": "他做事风风火火，却也效率极高。"
        },
        3791: {
            "pinyin": "fēng guāng yǐ nǐ",
            "meaning": "景色柔美多姿，十分迷人。",
            "example": "湖畔风光旖旎，是著名的旅游胜地。"
        },
        3792: {
            "pinyin": "fēng fēng yǔ yǔ",
            "meaning": "像风雨一样来来往往，比喻经历多次波折，也形容舆论争论不断。",
            "example": "他的人生一路风风雨雨，却始终不改初心。"
        },
        3793: {
            "pinyin": "fēng gāo fàng huǒ, yuè hēi shā rén",
            "meaning": "形容时机险恶，容易滋生罪恶行为，也比喻坏人趁机作乱。",
            "example": "夜深人静，正是风高放火，月黑杀人的时候。"
        },
        3794: {
            "pinyin": "fēng gǔ qiào jùn",
            "meaning": "风骨高峻，形容气节刚毅、品格高洁。",
            "example": "这位诗人风骨峭峻，一生不肯低头。"
        },
        3795: {
            "pinyin": "fēng hé rì lì",
            "meaning": "微风和煦、阳光明丽，形容天气晴好。",
            "example": "今日风和日丽，正适合出游。"
        },
        3796: {
            "pinyin": "fēng hé rì nuǎn",
            "meaning": "风和气暖，形容春日宜人的气候。",
            "example": "三月江南风和日暖，百花盛开。"
        },
        3797: {
            "pinyin": "fēng hǔ yún lóng",
            "meaning": "风如虎、云如龙，比喻气势宏大，英雄辈出。",
            "example": "乱世之中，常见风虎云龙之象。"
        },
        3798: {
            "pinyin": "fēng huā xuě yuè",
            "meaning": "风、花、雪、月，多指男女之间的情爱或风雅的游乐生活。",
            "example": "他年轻时也曾沉迷风花雪月。"
        },
        3799: {
            "pinyin": "fēng huá jué dài",
            "meaning": "风采才华冠绝当代，形容人极其出众。",
            "example": "这位女词人可谓风华绝代。"
        },
        3800: {
            "pinyin": "fēng huá zhèng mào",
            "meaning": "正值风采焕发的青春年华，多指青年意气风发之时。",
            "example": "在风华正茂的年纪，他选择投身科研一线。"
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

    print(f"已为 3701–3800 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
