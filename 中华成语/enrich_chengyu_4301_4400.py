import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 将 4301–4400 号成语的详细信息补充到 enrich 字典中
    enrich = {
        4301: {
            "pinyin": "fèi fèi tāng tāng",
            "meaning": "形容水流沸腾奔涌的样子，多用于描写江河泉源。",
            "example": "山涧泉眼处，清流沸沸汤汤，自石隙间奔涌而出。"
        },
        4302: {
            "pinyin": "fèi tiān zhèn dì",
            "meaning": "形容声音极其喧腾震撼，仿佛要把天地都震动起来。",
            "example": "礼堂内掌声与欢呼声沸天震地。"
        },
        4303: {
            "pinyin": "fèi cái láo mín",
            "meaning": "耗费大量财力，使百姓劳苦，常用来批评弊政。",
            "example": "若一味营造土木，只会费财劳民。"
        },
        4304: {
            "pinyin": "fēn bié mén hù",
            "meaning": "划分门户、各立宗派，多指人为制造派别、门户之见。",
            "example": "学术讨论贵在求同存异，切不可过分分别门户。"
        },
        4305: {
            "pinyin": "fēn chāi pī fèng",
            "meaning": "比喻夫妻离散或被迫分离。",
            "example": "战乱之中，不知多少人家分钗劈凤，各自天涯。"
        },
        4306: {
            "pinyin": "fēn chuáng tóng mèng",
            "meaning": "分床而睡却做着同样的梦，比喻虽暂时分离，情意仍然相通。",
            "example": "远隔两地，多年仍常分床同梦，彼此牵挂。"
        },
        4307: {
            "pinyin": "fēn ér zhì zhī",
            "meaning": "把整体分割成若干部分来加以统治，多指统治者离间、分化以便控制的策略。",
            "example": "殖民者惯用分而治之的手段瓦解民族团结。"
        },
        4308: {
            "pinyin": "fēn fáng jiǎn kǒu",
            "meaning": "旧时荒年为减轻口粮负担，让部分家人外出谋生或逃荒。",
            "example": "他少年时家境困顿，只得分房减口，被送往他乡。"
        },
        4309: {
            "pinyin": "fēn gān tóng kǔ",
            "meaning": "同享甘甜、共担苦难，形容关系亲密、同甘共苦。",
            "example": "夫妻能分甘同苦，方能共度风雨人生。"
        },
        4310: {
            "pinyin": "fēn gōng hé zuò",
            "meaning": "按照分工各尽其职，又相互配合完成工作。",
            "example": "团队只有分工合作得当，项目才能顺利推进。"
        },
        4311: {
            "pinyin": "fēn háo bù chā",
            "meaning": "连一丝一毫都没有差错，形容极为准确。",
            "example": "他对账细致入微，结果与报表分毫不差。"
        },
        4312: {
            "pinyin": "fēn háo bù qǔ",
            "meaning": "连一丝一毫也不取，形容极其廉洁。",
            "example": "他为官多年，公私分明，分毫不取。"
        },
        4313: {
            "pinyin": "fēn háo bù zhí",
            "meaning": "连一丝一毫的价值都没有，形容极其微不足道。",
            "example": "在浩瀚宇宙面前，个人的得失实在分毫不值。"
        },
        4314: {
            "pinyin": "fēn háo wú shuǎng",
            "meaning": "毫厘之间都没有差错，形容非常准确、严密。",
            "example": "这次测量数据分毫无爽，可作精确依据。"
        },
        4315: {
            "pinyin": "fēn huā fú liǔ",
            "meaning": "拨弄花枝、拂动杨柳，多形容春日漫步花间或轻佻调情的举止。",
            "example": "他闲来无事，只在街头分花拂柳、吟诗作对。"
        },
        4316: {
            "pinyin": "fēn wén wèi qǔ",
            "meaning": "一个钱也没有收取，形容分文不取的清廉或慷慨。",
            "example": "这次救援全凭义务，众人分文未取。"
        },
        4317: {
            "pinyin": "fēn xiāo dá shǔ",
            "meaning": "从半夜一直到天亮，形容时间之久或通宵不眠。",
            "example": "他们分宵达曙地商量方案，终于拿出可行之策。"
        },
        4318: {
            "pinyin": "fēn xié pò jìng",
            "meaning": "分鞋、破镜，比喻夫妻决裂分离。",
            "example": "一场误会竟使多年恩爱终成分鞋破镜。"
        },
        4319: {
            "pinyin": "fēn xīn guà fù",
            "meaning": "心思牵挂在肚里，比喻十分忧虑、放心不下。",
            "example": "孩子远行在外，做父母的难免分心挂腹。"
        },
        4320: {
            "pinyin": "fēn xīng bō liǎng",
            "meaning": "分星拨两，比喻分析得极为细致明白。",
            "example": "他把案情分星拨两地剖析清楚。"
        },
        4321: {
            "pinyin": "fēn xīng bò liǎng",
            "meaning": "比喻分辨事理十分精细明白。",
            "example": "这份报告对各项数据分星擘两，一目了然。"
        },
        4322: {
            "pinyin": "fēn xīng pī liǎng",
            "meaning": "与“分星擘两”义近，比喻分析得极其细致。",
            "example": "他把案件证据分星劈两，层层推理。"
        },
        4323: {
            "pinyin": "fēn xíng gòng qì",
            "meaning": "形容父母与子女同出一体、关系密切；亦泛指同源一体。",
            "example": "父子本为分形共气，理当互相体谅。"
        },
        4324: {
            "pinyin": "fēn xíng lián qì",
            "meaning": "与“分形同气”同，指骨肉至亲，一体相连。",
            "example": "兄弟本是分形连气，却为利反目，令人叹息。"
        },
        4325: {
            "pinyin": "fēn yān xī chǎn",
            "meaning": "同“分家析产”，指分家而分别财产。",
            "example": "父母过世后，兄弟几人只得分烟析产，各自度日。"
        },
        4326: {
            "pinyin": "fēn yān xī shēng",
            "meaning": "指兄弟分家，各自成户；亦指分散家业。",
            "example": "旧时人多口杂，往往不得不分烟析生。"
        },
        4327: {
            "pinyin": "fēn zhāng xī jù",
            "meaning": "把文章分段析句，逐一加以解释说明。",
            "example": "老师带领学生分章析句，体会文意。"
        },
        4328: {
            "pinyin": "fēn fēn bù yī",
            "meaning": "众说纷纭，意见不一致。",
            "example": "此事众人看法纷纷不一，一时难下定论。"
        },
        4329: {
            "pinyin": "fēn fēn jí jí",
            "meaning": "众多议论杂乱喧嚷的样子。",
            "example": "街头围观的人纷纷籍籍，议论不休。"
        },
        4330: {
            "pinyin": "fēn fēn rǎo rǎo",
            "meaning": "形容纷乱嘈杂的状态。",
            "example": "会场里一时纷纷扰扰，秩序大乱。"
        },
        4331: {
            "pinyin": "fēn fēn yáng yáng",
            "meaning": "形容雪花或花瓣等细小物片纷乱飘扬。",
            "example": "大雪纷纷洋洋，转眼间银装素裹。"
        },
        4332: {
            "pinyin": "fēn fēn yōng yōng",
            "meaning": "形容人群杂沓拥挤的样子。",
            "example": "广场上人流纷纷拥拥，热闹非凡。"
        },
        4333: {
            "pinyin": "fēn zhì tà lái",
            "meaning": "形容人或事物接连不断地到来。",
            "example": "贺电贺信纷至踏来，令人备受鼓舞。"
        },
        4334: {
            "pinyin": "fén cháo dàng xué",
            "meaning": "烧毁鸟巢、荡平洞穴，比喻彻底摧毁敌巢或祸根。",
            "example": "要想息乱，必须焚巢荡穴，一扫余党。"
        },
        4335: {
            "pinyin": "fén cháo dǎo xué",
            "meaning": "烧毁鸟巢，捣毁兽穴，比喻彻底剿灭敌人老巢。",
            "example": "官军进山焚巢捣穴，土匪无处藏身。"
        },
        4336: {
            "pinyin": "fén diǎn kēng rú",
            "meaning": "焚毁典籍、坑杀儒生，比喻残酷摧残文化与知识分子。",
            "example": "历史上的焚典坑儒给文化带来巨大损失。"
        },
        4337: {
            "pinyin": "fén fú pò xǐ",
            "meaning": "焚烧信符、破坏玉玺，比喻决心断绝旧约或旧制。",
            "example": "新政一出，旧时制度悉皆焚符破玺。"
        },
        4338: {
            "pinyin": "fēn huā yuē liǔ",
            "meaning": "在花间杨柳下幽会，多指男女约会游春。",
            "example": "古人常于春日分花约柳，吟诗作对。"
        },
        4339: {
            "pinyin": "fēn jiā xī chǎn",
            "meaning": "指分家并分割家产，各自过活。",
            "example": "兄弟情谊尚在，虽已分家析产，仍常相往来。"
        },
        4340: {
            "pinyin": "fēn jīn bō liǎng",
            "meaning": "比喻斤斤计较，过于琐碎较真。",
            "example": "做人不必事事分斤拨两，适当退让反能和气生财。"
        },
        4341: {
            "pinyin": "fēn jīn bāi liǎng",
            "meaning": "比喻极其精细地计算或计较。",
            "example": "做学问要严谨分金掰两，生活中却不可太刻薄。"
        },
        4342: {
            "pinyin": "fēn jìn hé jī",
            "meaning": "部队分别向两翼或多路推进，同时协同攻击。",
            "example": "大军分进合击，迅速突破敌军防线。"
        },
        4343: {
            "pinyin": "fēn jiǔ bì hé, hé jiǔ bì fēn",
            "meaning": "指事物由合而分、由分而合，是一种循环变化的规律。",
            "example": "历史兴亡，正应了分久必合，合久必分之理。"
        },
        4344: {
            "pinyin": "fēn láo fù gōng",
            "meaning": "各分担劳苦，奔赴建功立业。",
            "example": "同事们分劳赴功，使项目提前完成。"
        },
        4345: {
            "pinyin": "fēn lí háo sī",
            "meaning": "极细微的数量，比喻事物极小或差别细微。",
            "example": "他对乐曲节奏的掌握可谓分厘毫丝不差。"
        },
        4346: {
            "pinyin": "fēn máo cì tǔ",
            "meaning": "古代分封诸侯的一种仪式，表示授予土封。",
            "example": "先王分茅赐土，以建藩屏。"
        },
        4347: {
            "pinyin": "fēn máo liè tǔ",
            "meaning": "分封诸侯，划分疆土。",
            "example": "自古天子分茅列土，以诸侯共治天下。"
        },
        4348: {
            "pinyin": "fēn máo xī tǔ",
            "meaning": "同“分茅赐土”，指封授土地、建立诸侯。",
            "example": "他战功卓著，被王室分茅锡土，封为列侯。"
        },
        4349: {
            "pinyin": "fēn máo zuò tǔ",
            "meaning": "古代分封诸侯、赐以祭地之土。",
            "example": "列国君臣分茅胙土，各守一方。"
        },
        4350: {
            "pinyin": "fēn péng yǐn lèi",
            "meaning": "按朋党和类别结成集团，多带贬义。",
            "example": "用人若任由分朋引类，必致党同伐异。"
        },
        4351: {
            "pinyin": "fēn pín zhèn qióng",
            "meaning": "拿出财物周济贫苦、振救穷困。",
            "example": "年终他捐资分贫振穷，颇得好评。"
        },
        4352: {
            "pinyin": "fēn qíng pò ài",
            "meaning": "割舍情爱，断绝旧情。",
            "example": "既已分情破爱，便各自珍重前程。"
        },
        4353: {
            "pinyin": "fēn sān bié liǎng",
            "meaning": "形容分得很细，也指分分合合的反复。",
            "example": "账目被他分三别两地理得井然有序。"
        },
        4354: {
            "pinyin": "fēn shēn jiǎn kǒu",
            "meaning": "同“分房减口”，指为减轻家中口粮而让部分人外出谋生。",
            "example": "祖父年轻时因灾年不得不分身减口，外出做工。"
        },
        4355: {
            "pinyin": "fēn sī xī lǚ",
            "meaning": "像把丝线一缕缕分开，形容分析得非常细致。",
            "example": "他对这段历史分丝析缕，考证详明。"
        },
        4356: {
            "pinyin": "fēn tiáo xī lǐ",
            "meaning": "按条分出，细细分析道理。",
            "example": "老师分条析理，把复杂问题讲得通俗易懂。"
        },
        4357: {
            "pinyin": "fēn tíng kàng lǐ",
            "meaning": "夫妻在庭堂中并立行礼，比喻夫妇相敬如宾。",
            "example": "新人拜堂成亲时分庭伉礼，亲友齐贺。"
        },
        4358: {
            "pinyin": "fēn wén bù zhí",
            "meaning": "连一文钱的价值都没有，形容极其微贱。",
            "example": "那旧物早已分文不值，只剩些回忆。"
        },
        4359: {
            "pinyin": "fén kū shí dàn",
            "meaning": "烧柴吃淡饭，形容生活清苦俭朴。",
            "example": "他甘于焚枯食淡，只求潜心著述。"
        },
        4360: {
            "pinyin": "fén lín ér shòu",
            "meaning": "烧林打猎，比喻竭泽而渔，只图一时之利而损害长远根基。",
            "example": "过度开发资源，无异于焚林而狩。"
        },
        4361: {
            "pinyin": "fén lín ér tián",
            "meaning": "烧毁树林以猎取野兽，比喻只顾眼前利益，不计长远后果。",
            "example": "若为一时之利而焚林而田，终将自食其果。"
        },
        4362: {
            "pinyin": "fén lín ér tián",
            "meaning": "同“焚林而田”，比喻取之不留余地。",
            "example": "经营之道贵在长久，岂可焚林而畋。"
        },
        4363: {
            "pinyin": "fén lín jié zé",
            "meaning": "烧林捕兽、抽干水泽捕鱼，比喻只图眼前利益而破坏根本。",
            "example": "这种开发方式无异于焚林竭泽。"
        },
        4364: {
            "pinyin": "fén qín yù hè",
            "meaning": "把琴当柴烧、把鹤拿去卖，比喻糟蹋美好的事物。",
            "example": "粗俗之人强评名画，真是焚琴鬻鹤。"
        },
        4365: {
            "pinyin": "fén shī yáng huī",
            "meaning": "焚烧尸体、扬弃骨灰，形容极端仇视。",
            "example": "百姓痛恨乱臣贼子，恨不得焚尸扬灰。"
        },
        4366: {
            "pinyin": "fén sǒu ér tián",
            "meaning": "烧毁林薮以打猎，比喻只顾眼前利益，不顾长远。",
            "example": "企业若只知焚薮而田，终究难以长久。"
        },
        4367: {
            "pinyin": "fén xiāng dǐng lǐ",
            "meaning": "焚香礼拜，多用来形容极其虔诚的崇敬态度。",
            "example": "香客们焚香顶礼，祈求风调雨顺。"
        },
        4368: {
            "pinyin": "fén xiāng mó bài",
            "meaning": "烧香跪拜，形容极度崇拜或盲目膜拜。",
            "example": "对偶像不必焚香膜拜，当理性看待。"
        },
        4369: {
            "pinyin": "fén xiāng sǎo dì",
            "meaning": "焚香、扫地以自洁，多形容清幽恬淡的隐居生活。",
            "example": "他隐居山林，不过焚香扫地、读书写字而已。"
        },
        4370: {
            "pinyin": "fěn bái mò hēi",
            "meaning": "以白粉敷面、黑黛画眉，形容女子妆饰艳丽。",
            "example": "那女子粉白墨黑，远远望去宛若画中人。"
        },
        4371: {
            "pinyin": "fěn gǔ juān qū",
            "meaning": "粉身碎骨，捐出身躯，比喻献身赴死。",
            "example": "将士们誓言粉骨捐躯，保家卫国。"
        },
        4372: {
            "pinyin": "fěn gǔ mí qū",
            "meaning": "同“粉身碎骨”，形容为报恩或成大义而不惜牺牲生命。",
            "example": "他宁肯粉骨糜躯，也不肯屈服。"
        },
        4373: {
            "pinyin": "fěn gǔ mí shēn",
            "meaning": "犹言粉身碎骨，形容牺牲极为惨烈。",
            "example": "烈士粉骨糜身，只为换来山河无恙。"
        },
        4374: {
            "pinyin": "fěn gǔ suì shēn",
            "meaning": "身躯粉碎，比喻牺牲生命也在所不惜。",
            "example": "若能救民于水火，纵然粉骨碎身亦无悔。"
        },
        4375: {
            "pinyin": "fěn miàn zhū chún",
            "meaning": "白嫩的脸庞、红润的嘴唇，多形容容貌俊美。",
            "example": "那少年粉面朱唇，风采不凡。"
        },
        4376: {
            "pinyin": "fěn shēn huī gǔ",
            "meaning": "粉碎身躯、化为灰骨，比喻为某种理想献出全部生命。",
            "example": "他立誓纵然粉身灰骨，也要守护此城。"
        },
        4377: {
            "pinyin": "fěn zhuāng yù qì",
            "meaning": "用白粉装饰、以白玉砌成，比喻雪后银装素裹的景象。",
            "example": "一夜大雪，山川粉妆玉砌，美不胜收。"
        },
        4378: {
            "pinyin": "fēng cǎo cháng lín",
            "meaning": "茂盛的草木与高林，亦借指隐居之地。",
            "example": "他早有投迹丰草长林之志。"
        },
        4379: {
            "pinyin": "fēng dù piān piān",
            "meaning": "风采气度洒脱文雅，形容仪态不凡。",
            "example": "那书生丰度翩翩，令人一见难忘。"
        },
        4380: {
            "pinyin": "fēng fù duō cǎi",
            "meaning": "内容丰富、形式多样。",
            "example": "晚会节目丰富多彩，老少皆宜。"
        },
        4381: {
            "pinyin": "fēng gōng hòu lì",
            "meaning": "伟大的功绩和丰厚的利益或惠泽。",
            "example": "这项改革对国家实为丰功厚利。"
        },
        4382: {
            "pinyin": "fēng gōng mào dé",
            "meaning": "丰盛的功绩与美好的德行。",
            "example": "先贤丰功茂德，后人无不景仰。"
        },
        4383: {
            "pinyin": "fēng gōng shèng liè",
            "meaning": "伟大的功业和显著的功勋。",
            "example": "他在抗战中所立丰功盛烈，青史可鉴。"
        },
        4384: {
            "pinyin": "fēng gōng shuò dé",
            "meaning": "巨大的功勋和隆盛的德泽。",
            "example": "这位老将丰功硕德，堪称一代楷模。"
        },
        4385: {
            "pinyin": "fēng gōng yì dé",
            "meaning": "卓著的功绩和高尚的品德。",
            "example": "他以丰功懿德享誉乡里。"
        },
        4386: {
            "pinyin": "fēng jī ruò gǔ",
            "meaning": "肌肤丰润、骨格柔弱，形容女子体态丰腴而娇嫩。",
            "example": "画中仕女丰肌弱骨，姿态生动。"
        },
        4387: {
            "pinyin": "fēng jī xiù gǔ",
            "meaning": "形容女子或花木肌理丰润、体态秀美。",
            "example": "她丰肌秀骨，举止端庄。"
        },
        4388: {
            "pinyin": "fēng qiáng qiāo xià",
            "meaning": "墙虽高大而地基峻峭，比喻根基不牢。",
            "example": "若企业管理不善，纵有丰墙硗下之势，终难长久。"
        },
        4389: {
            "pinyin": "fēng qiáng qiào zhǐ",
            "meaning": "墙高基陡，喻根基不稳。",
            "example": "制度若失民心，不过是丰墙峭阯而已。"
        },
        4390: {
            "pinyin": "fēng qiáng qiào zhǐ",
            "meaning": "同“丰墙峭阯”，形容外表雄伟而基础不牢。",
            "example": "这番繁华恐成丰墙峭址，一触即塌。"
        },
        4391: {
            "pinyin": "fēng wū bù jiā",
            "meaning": "比喻深自隐藏，不肯出仕，亦可指富贵显宦之家。",
            "example": "他本可出山为官，却偏要丰屋蔀家。"
        },
        4392: {
            "pinyin": "fēng wū shēng zāi",
            "meaning": "屋宇宏大反而滋生灾祸，比喻奢侈易致祸患。",
            "example": "古人常言丰屋生灾，提醒人不可过度奢华。"
        },
        4393: {
            "pinyin": "fēng wū yán zāi",
            "meaning": "房屋高大而招来灾祸，比喻财多位高易生祸端。",
            "example": "他不信丰屋延灾之说，终因贪恋权势而败。"
        },
        4394: {
            "pinyin": "fēng wū zhī guò",
            "meaning": "指因居所过于高大豪华而招来祸患，应当引以为戒。",
            "example": "古籍多以丰屋之过警世，劝人知足守节。"
        },
        4395: {
            "pinyin": "fēng wū zhī huò",
            "meaning": "居室过于宏大华丽所带来的祸患，比喻奢华易致灾祸。",
            "example": "他最终应了丰屋之祸之谶，家道中落。"
        },
        4396: {
            "pinyin": "fēng chuī mǎ ěr",
            "meaning": "比喻对别人的话毫不在意，当作耳边风。",
            "example": "我苦口婆心劝他，他却当风吹马耳。"
        },
        4397: {
            "pinyin": "fēng chuī rì shài",
            "meaning": "狂风吹、烈日晒，形容毫无遮蔽的辛劳环境。",
            "example": "农人风吹日晒，一年到头不曾闲歇。"
        },
        4398: {
            "pinyin": "fēng chuī yún sàn",
            "meaning": "比喻事情、恩怨等随时间消散无踪。",
            "example": "往日是非，早已风吹云散。"
        },
        4399: {
            "pinyin": "fēng fēng yùn yùn",
            "meaning": "形容姿态韵致优美，或声音悠长婉转。",
            "example": "他弹起琴来，音调风风韵韵，引人沉醉。"
        },
        4400: {
            "pinyin": "fēng guāng yuè jì",
            "meaning": "雨过天晴、月色清朗的景象，比喻胸襟开阔、品格高洁。",
            "example": "他待人坦荡，如风光月霁。"
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

    print(f"已为 4301–4400 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
