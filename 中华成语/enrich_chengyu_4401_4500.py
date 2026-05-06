import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 将 4401–4500 号成语的详细信息补充到 enrich 字典中
    enrich = {
        # TODO: 填写 4401–4500 号成语的 pinyin、meaning、example
        4401: {
            "pinyin": "fēng hé jìn qǐ",
            "meaning": "比喻顺应天心民意，得到天助，情势大为好转。",
            "example": "若能施政得当，自有风禾尽起之时。"
        },
        4402: {
            "pinyin": "fēng hé rì měi",
            "meaning": "微风和畅，阳光明丽，形容天气晴朗宜人。",
            "example": "在这样风和日美的早晨出游最是惬意。"
        },
        4403: {
            "pinyin": "fēng hé rì xuān",
            "meaning": "微风和畅，阳光温暖，形容春日暖和的天气。",
            "example": "郊外风和日暄，正宜踏青赏春。"
        },
        4404: {
            "pinyin": "fēng huā xuě yè",
            "meaning": "原指旧时诗文中常写的风、花、雪、月等景物，后多比喻堆砌辞藻而内容空洞的作品。",
            "example": "他已不满足于写些风花雪夜的篇章。"
        },
        4405: {
            "pinyin": "fēng huí diàn jī",
            "meaning": "形容来去迅疾，像旋风回转、闪电激射一般。",
            "example": "骑兵突进如风回电激，令人目不暇接。"
        },
        4406: {
            "pinyin": "fēng jī diàn fēi",
            "meaning": "形容声势猛厉，行动迅疾如狂风激荡、电光飞驰。",
            "example": "大军南下，鼓角风激电飞。"
        },
        4407: {
            "pinyin": "fēng jī diàn hài",
            "meaning": "形容来势汹汹、威势极猛。",
            "example": "山洪风激电骇，一泻千里。"
        },
        4408: {
            "pinyin": "fēng jí làng gāo",
            "meaning": "形容风浪很大。",
            "example": "渔民冒着风急浪高出海打鱼。"
        },
        4409: {
            "pinyin": "fēng jǔ yún fēi",
            "meaning": "凭借风云飞腾而上，比喻乘时得势、迅速升迁。",
            "example": "这几年他风举云飞，仕途一片光明。"
        },
        4410: {
            "pinyin": "fēng jǔ yún yáo",
            "meaning": "凭借风云飞腾而上，亦比喻飞黄腾达。",
            "example": "少年胸怀大志，只待一日风举云摇。"
        },
        4411: {
            "pinyin": "fēng jué yún guǐ",
            "meaning": "形容风云怪诞多变，比喻局势诡谲莫测。",
            "example": "时局风谲云诡，更需保持清醒头脑。"
        },
        4412: {
            "pinyin": "fēng léi huǒ pào",
            "meaning": "形容脾气急躁，言行猛烈。",
            "example": "他一向说话风雷火炮，毫不遮掩。"
        },
        4413: {
            "pinyin": "fēng léi zhī biàn",
            "meaning": "指风雷交作等灾异之象，古人多视为上天示警。",
            "example": "史书屡记风雷之变，以警示当政者。"
        },
        4414: {
            "pinyin": "fēng liú diē dàng",
            "meaning": "形容气度洒脱不羁，风采潇洒。",
            "example": "他谈笑自若，举止风流跌宕。"
        },
        4415: {
            "pinyin": "fēng zī chuò yuē",
            "meaning": "形容女子风度姿态柔美动人。",
            "example": "新娘风姿绰约，一出场便惊艳全场。"
        },
        4416: {
            "pinyin": "fēng dāo guà jiàn",
            "meaning": "比喻结束武斗或竞技生涯，不再出场拼杀。亦泛指退出某种事业。",
            "example": "连夺数届冠军之后，他选择封刀挂剑，退居幕后。"
        },
        4417: {
            "pinyin": "fēng guān xǔ yuán",
            "meaning": "封赏官职并许以报酬，今多指以名利地位笼络他人。",
            "example": "他不愿因封官许原而违背原则。"
        },
        4418: {
            "pinyin": "fēng hú jié mò",
            "meaning": "封、胡、羯、末本为谢氏兄弟的小名，后用以称赞他人兄弟子侄皆为优秀之才。",
            "example": "这几位青年才俊，真可谓封胡羯末。"
        },
        4419: {
            "pinyin": "fēng jǐ shǒu cán",
            "meaning": "指固步自封、抱残守缺，形容思想保守，不思革新。",
            "example": "在飞速发展的时代，企业若封己守残，终将被淘汰。"
        },
        4420: {
            "pinyin": "fēng jīn guà yìn",
            "meaning": "指不受赏金，挂印辞官，比喻辞去官职或要职。",
            "example": "他毅然封金挂印，只为守住内心的操守。"
        },
        4421: {
            "pinyin": "fēng xī xiū shé",
            "meaning": "比喻贪婪残暴、侵略成性的势力或人物，同“封豕长蛇”。",
            "example": "此辈封豨修蛇，终将为民所弃。"
        },
        4422: {
            "pinyin": "fēng huǒ xiāng lián",
            "meaning": "形容烽火台报警的烟火相继不绝，比喻战事频仍、战火不断。",
            "example": "边关多年烽火相连，百姓饱受战乱之苦。"
        },
        4423: {
            "pinyin": "fēng dí yú shēng",
            "meaning": "锋：刀锋；镝：箭镞。指从刀箭下逃生，形容历经战乱而幸存。",
            "example": "他在前线锋镝余生，更知和平可贵。"
        },
        4424: {
            "pinyin": "fēng máng bì lù",
            "meaning": "锐气与才华全都显露出来，多形容人喜欢表现自己。",
            "example": "年轻人锋铓毕露，也难免得罪人。"
        },
        4425: {
            "pinyin": "fēng chū quán liú",
            "meaning": "像群蜂倾巢，如泉水涌流，形容事物一时纷纷出现。",
            "example": "那段时间各家新书蜂出泉流，目不暇接。"
        },
        4426: {
            "pinyin": "fēng fáng yǐ xué",
            "meaning": "蜂房：蜂巢。比喻所占据的地方狭小，或各据一隅的局面。",
            "example": "昔日诸侯蜂房蚁穴，割据一方。"
        },
        4427: {
            "pinyin": "fēng fù yún jí",
            "meaning": "比喻人群像蜂拥、如云集聚，四处赶来。",
            "example": "消息传出后，报名者蜂附云集。"
        },
        4428: {
            "pinyin": "fēng hé shǐ tū",
            "meaning": "像蜂群聚合、猪群横冲直撞，形容人群杂乱蜂拥、横冲直闯。",
            "example": "暴民蜂合豕突，所到之处满目疮痍。"
        },
        4429: {
            "pinyin": "fēng hé yǐ jù",
            "meaning": "形容人众像蜂蚁般拥挤聚集在一起。",
            "example": "广场上游人蜂合蚁聚，十分热闹。"
        },
        4430: {
            "pinyin": "fēng kē yǐ xué",
            "meaning": "蜂窠：蜂巢。比喻占据的地方极为狭小，也用以轻蔑偏安一隅的势力。",
            "example": "与其谋那蜂窠蚁穴之利，不如着眼四方。"
        },
        4431: {
            "pinyin": "fēng kuáng dié luàn",
            "meaning": "像蜂蝶般纷飞杂乱，多形容因美色引来众多追随或形容心神被勾起而纷乱。",
            "example": "她一笑之间，引得少年们蜂狂蝶乱。"
        },
        4432: {
            "pinyin": "fēng méi dié shǐ",
            "meaning": "指花间飞舞的蜂蝶，比喻为男女之间居间撮合或传递书信的人。",
            "example": "这桩婚事还得靠几位蜂媒蝶使多费些心。"
        },
        4433: {
            "pinyin": "féng huān dàn jiá",
            "meaning": "指怀才不遇的人弹剑长叹，比喻有才华者渴望得到赏识。",
            "example": "他屡试不第，自觉如冯驩弹铗。"
        },
        4434: {
            "pinyin": "féng shēng dàn jiá",
            "meaning": "同“冯驩弹铗”，指有才华而久不得志的人渴望被任用。",
            "example": "这些隐居山林的文士，个个是冯生弹铗之才。"
        },
        4435: {
            "pinyin": "féng táng bái shǒu",
            "meaning": "汉朝冯唐白首仍不得施展抱负，比喻生不逢时或年老志未酬。",
            "example": "他自叹冯唐白首，壮志难酬。"
        },
        4436: {
            "pinyin": "féng táng tóu bái",
            "meaning": "指冯唐年老头白仍不得重用，感叹身世坎坷、报国无门。",
            "example": "多少志士成了冯唐头白之人。"
        },
        4437: {
            "pinyin": "féng táng yǐ lǎo",
            "meaning": "同“冯唐易老”，感叹年华易逝，壮志未酬。",
            "example": "时光如梭，叹我冯唐已老。"
        },
        4438: {
            "pinyin": "féng táng yì lǎo",
            "meaning": "出自冯唐身历三朝而老才被荐举的典故，比喻生不逢时或年老难以有所作为。",
            "example": "他常以冯唐易老自喻，惜未遇明主。"
        },
        4439: {
            "pinyin": "féng chǎng gān mù",
            "meaning": "比喻遇到场合才凑个热闹的人，亦指偶尔随俗应酬。",
            "example": "他平日清静，不喜喧嚣，今日也算逢场竿木了一回。"
        },
        4440: {
            "pinyin": "féng chǎng yóu xì",
            "meaning": "犹言逢场作戏，指偶尔凑凑热闹或随俗应酬。",
            "example": "他原本无意久留，只是逢场游戏而已。"
        },
        4441: {
            "pinyin": "féng chǎng zuò lè",
            "meaning": "犹言逢场作戏，遇到机会便及时行乐，带有随俗凑热闹之意。",
            "example": "他向来自律，此番也不过是逢场作乐而已。"
        },
        4442: {
            "pinyin": "féng chǎng zuò qù",
            "meaning": "犹言逢场作戏，指偶尔随俗应酬、凑凑热闹。",
            "example": "这回他不过逢场作趣，并非真心沉迷其中。"
        },
        4443: {
            "pinyin": "féng è dǎo fēi",
            "meaning": "逢迎坏人，助长恶行。",
            "example": "为官若逢恶导非，必遗害一方。"
        },
        4444: {
            "pinyin": "féng jī gòu huì",
            "meaning": "遭逢良机，把握住机会。",
            "example": "他善于逢机遘会，从不轻易错失时机。"
        },
        4445: {
            "pinyin": "féng jī lì duàn",
            "meaning": "犹言当机立断，在机会来临时果断作出决定。",
            "example": "关键时刻他能逢机立断，转危为安。"
        },
        4446: {
            "pinyin": "féng jí dīng chén",
            "meaning": "指遇上好时运。",
            "example": "他少年得志，可谓逢吉丁辰。"
        },
        4447: {
            "pinyin": "féng shān kāi dào",
            "meaning": "形容不畏艰险，在前开路，常与“遇水叠桥”连用。",
            "example": "先锋队逢山开道、遇水架桥，行军极为迅速。"
        },
        4448: {
            "pinyin": "féng yī qiǎn dài",
            "meaning": "宽袖大带为古代儒者的服饰，借指儒者。",
            "example": "堂上缝衣浅带，多是饱学之士。"
        },
        4449: {
            "pinyin": "fěng dé sòng gōng",
            "meaning": "讽诵德行，颂扬功业，指赞美、称颂功德。",
            "example": "史臣秉笔，讽德诵功，以示后人。"
        },
        4450: {
            "pinyin": "fèng suǐ lóng gān",
            "meaning": "与“龙肝凤髓”同，形容极其珍奇名贵的美味佳肴。",
            "example": "纵然是凤髓龙肝，他也无心下箸。"
        },
        4451: {
            "pinyin": "fèng tàn hǔ shì",
            "meaning": "形容谈吐文雅、器宇轩昂，文武兼备。",
            "example": "那少年凤叹虎视，不似等闲人物。"
        },
        4452: {
            "pinyin": "fèng wǔ lóng fēi",
            "meaning": "形容书法笔势有力而灵动舒展。",
            "example": "此碑字画凤舞龙飞，气势非凡。"
        },
        4453: {
            "pinyin": "fèng wǔ lóng pán",
            "meaning": "凤凰飞舞，蛟龙盘曲，比喻相配得当、姿态雄丽。",
            "example": "两人郎才女貌，真是凤舞龙蟠的一对。"
        },
        4454: {
            "pinyin": "fèng wǔ luán gē",
            "meaning": "形容歌舞优美动人，亦指仙乐妙舞。",
            "example": "殿上笙歌鼎沸，真个是凤舞鸾歌的盛景。"
        },
        4455: {
            "pinyin": "fèng xiāo lóng guǎn",
            "meaning": "指笙箫一类管乐器的吹奏声。",
            "example": "夜深宫中凤箫龙管，回荡不绝。"
        },
        4456: {
            "pinyin": "fèng xiāo luán guǎn",
            "meaning": "笙箫之类的吹奏乐声。",
            "example": "曲罢人未散，只余凤箫鸾管在耳畔回响。"
        },
        4457: {
            "pinyin": "fèng xié luán hé",
            "meaning": "比喻夫妻和睦、情意融洽，亦指众人和衷共济。",
            "example": "新人珠联璧合，自当凤协鸾和。"
        },
        4458: {
            "pinyin": "fèng yí shòu wǔ",
            "meaning": "形容圣贤德化极大，连凤凰来仪、百兽起舞，比喻教化感人至深。",
            "example": "吏治清平，礼乐兴盛，几近凤仪兽舞之世。"
        },
        4459: {
            "pinyin": "fèng yì lóng qí",
            "meaning": "凤凰的胸脯、龙的颈鬣，比喻骏马雄奇健美。",
            "example": "这匹骏马真有凤臆龙鬐之姿。"
        },
        4460: {
            "pinyin": "fèng yín luán chuī",
            "meaning": "形容乐声和美悠扬，如凤凰吟唱、鸾鸟吹奏一般。",
            "example": "堂上传来笙歌管弦，恍若凤吟鸾吹。"
        },
        4461: {
            "pinyin": "fēng qīng yún jìng",
            "meaning": "微风轻拂、浮云淡薄，形容天气晴朗、天空澄净。",
            "example": "春日郊外风轻云净，最宜踏青远眺。"
        },
        4462: {
            "pinyin": "fēng qīng yuè bái",
            "meaning": "微风清凉、月色皎洁，形容夜景幽美宜人。",
            "example": "这般风清月白的夜里，他独自徘徊江畔。"
        },
        4463: {
            "pinyin": "fēng qīng yuè míng",
            "meaning": "微风清凉，月光明朗，形容夜色清幽明净。",
            "example": "夏夜风清月明，一片蛙声此起彼伏。"
        },
        4464: {
            "pinyin": "fēng qíng yuè sī",
            "meaning": "指男女间缠绵的情思，多与月夜景色相连。",
            "example": "词中句句风情月思，写尽离人相思。"
        },
        4465: {
            "pinyin": "fēng qíng yuè yì",
            "meaning": "指男女相互爱恋的情意，同“风情月思”。",
            "example": "她一颦一笑皆含风情月意。"
        },
        4466: {
            "pinyin": "fēng qū diàn jī",
            "meaning": "形容来势迅猛，如狂风驱赶、闪电击发。",
            "example": "大军风驱电击般突入敌阵。"
        },
        4467: {
            "pinyin": "fēng qū diàn sǎo",
            "meaning": "形容行动迅速猛烈，如暴风骤起、电光扫荡。",
            "example": "清剿行动风驱电扫，一举平定匪患。"
        },
        4468: {
            "pinyin": "fēng shēng hè lì",
            "meaning": "听到风声和鹤鸣都疑为敌军追兵，形容极度惊恐、多疑自扰。",
            "example": "战败之后，他稍闻异响便风声鹤唳。"
        },
        4469: {
            "pinyin": "fēng shuāng yǔ xuě",
            "meaning": "本指自然界的风霜雨雪，比喻种种艰难困苦的历练。",
            "example": "他历经风霜雨雪，性格愈发坚韧。"
        },
        4470: {
            "pinyin": "gǎi bù gǎi yù",
            "meaning": "原指死者身份改变而安葬礼制也随之变更，后亦指改变制度或改朝换代。",
            "example": "自古每逢改步改玉，百姓多受其累。"
        },
        4471: {
            "pinyin": "gǎi cāo yì jié",
            "meaning": "改变原来的操守和节操，多指放弃应守的气节，亦可指弃恶从善。",
            "example": "他誓不改操易节，宁作孤臣。"
        },
        4472: {
            "pinyin": "gǎi cháo huàn dài",
            "meaning": "旧王朝被推翻，由新的政权取而代之，亦泛指时代发生巨大变革。",
            "example": "几经改朝换代，这座古城依旧巍然。"
        },
        4473: {
            "pinyin": "gǎi è xiàng shàn",
            "meaning": "不再作恶，走向善良正直的道路。",
            "example": "他决心改恶向善，重新开始人生。"
        },
        4474: {
            "pinyin": "gǎi è xíng shàn",
            "meaning": "改掉恶行而去做善事。",
            "example": "只要肯改恶行善，仍可赢得众人尊重。"
        },
        4475: {
            "pinyin": "gǎi guò bù lìn",
            "meaning": "吝：吝惜。指改正错误态度坚决，不犹豫、不保留。",
            "example": "君子行事，当能改过不吝，从善如流。"
        },
        4476: {
            "pinyin": "gǎi guò qiān shàn",
            "meaning": "改正错误，转而行善，指去恶就善。",
            "example": "他虽曾误入歧途，终能改过迁善。"
        },
        4477: {
            "pinyin": "gǎi guò zì xīn",
            "meaning": "改正过错，自觉重新做人。",
            "example": "法律也给愿意改过自新的人留有机会。"
        },
        4478: {
            "pinyin": "gǎi huàn jiā mén",
            "meaning": "提高家庭门第、社会地位，亦指改换门庭。",
            "example": "他立志读书求仕，只望有日改换家门。"
        },
        4479: {
            "pinyin": "gǎi míng huàn xìng",
            "meaning": "改变原来的姓名，多为隐瞒身分或避祸。",
            "example": "战乱之中，他被迫改名换姓以保全性命。"
        },
        4480: {
            "pinyin": "gǎi róng yì mào",
            "meaning": "改变神情容貌，多指态度突然转变。",
            "example": "听到此言，他不由得改容易貌，沉吟不语。"
        },
        4481: {
            "pinyin": "gǎi shì chéng fēi",
            "meaning": "把正确的说成错误，颠倒是非。",
            "example": "若任人改是成非，社会公义必受损害。"
        },
        4482: {
            "pinyin": "gǎi sú qiān fēng",
            "meaning": "改变旧有风俗习气，移风易俗。",
            "example": "要改俗迁风，还须教化与制度并行。"
        },
        4483: {
            "pinyin": "gǎi tiān huàn dì",
            "meaning": "比喻彻底改变原有面貌，多指社会或自然的重大变革。",
            "example": "短短几十年，这里已经改天换地。"
        },
        4484: {
            "pinyin": "gǎi tóu huàn miàn",
            "meaning": "多指只在形式或外表上作些变动，而实质并未改变。",
            "example": "若只是改头换面而不触及根本，难以取信于民。"
        },
        4485: {
            "pinyin": "gǎi tóu huàn wěi",
            "meaning": "只在开头结尾上作改动，实质内容仍旧。",
            "example": "这篇文章不过改头换尾，观点毫无新意。"
        },
        4486: {
            "pinyin": "gǎi xián gēng zhāng",
            "meaning": "本指更换琴弦以调和音律，后比喻改革制度或变更方针、办法。",
            "example": "企业必须改弦更张，方能适应新形势。"
        },
        4487: {
            "pinyin": "gǎi xián yì zhé",
            "meaning": "琴换弦、车改道，比喻改变原来的方向、计划或做法。",
            "example": "看到弊端丛生，他主张及时改弦易辙。"
        },
        4488: {
            "pinyin": "gǎi xié guī zhèng",
            "meaning": "从邪路回到正道上来，不再做坏事。",
            "example": "他终于幡然醒悟，决心改邪归正。"
        },
        4489: {
            "pinyin": "gǎi yuán yì zhé",
            "meaning": "改变车辕方向、改走别路，比喻改变原有态度和做法。",
            "example": "若此策难行，不妨改辕易辙，另谋出路。"
        },
        4490: {
            "pinyin": "gài bù yóu jǐ",
            "meaning": "指事情出于上命或外力，自己难以作主。",
            "example": "此来奉命行事，实乃盖不由己。"
        },
        4491: {
            "pinyin": "gài guān lùn dìng",
            "meaning": "指一个人的功过是非要到死后方能作出最后评价。",
            "example": "英雄功罪，尚待将来盖棺论定。"
        },
        4492: {
            "pinyin": "gài shì wú shuāng",
            "meaning": "才能或武艺当代第一，独一无二。",
            "example": "他以剑术盖世无双而闻名天下。"
        },
        4493: {
            "pinyin": "gài shì yīng xióng",
            "meaning": "形容超越当世群雄的杰出英雄人物。",
            "example": "这位将军真是盖世英雄，战功彪炳。"
        },
        4494: {
            "pinyin": "gài shì zhī cái",
            "meaning": "形容超出当代、无与伦比的卓越才能。",
            "example": "他才华横溢，堪称盖世之才。"
        },
        4495: {
            "pinyin": "gài mò néng wài",
            "meaning": "一概不能例外，指都在所说范围之内。",
            "example": "规律所在，古今中外概莫能外。"
        },
        4496: {
            "pinyin": "gān chái liè huǒ",
            "meaning": "比喻感情或情绪十分炽烈，一触即发。",
            "example": "两队球员早已如干柴烈火，比赛气氛紧张。"
        },
        4497: {
            "pinyin": "gān chéng zhī jiàng",
            "meaning": "干城：盾牌和城墙，比喻捍卫者。指保卫国家的栋梁大将。",
            "example": "他戎马一生，可谓国家的干城之将。"
        },
        4498: {
            "pinyin": "gān jiāng mò yé",
            "meaning": "干将、莫邪皆古代名剑，借指锋利的宝剑或卓越的人才。",
            "example": "此剑锋利非常，不减干将莫邪。"
        },
        4499: {
            "pinyin": "gān jìng lì luò",
            "meaning": "形容干脆利索，没有拖泥带水；或指整洁有条理。",
            "example": "他办事一向干净利落，令人放心。"
        },
        4500: {
            "pinyin": "gān míng cǎi yù",
            "meaning": "以不正当手段猎取名誉。",
            "example": "为官者若一味干名采誉，终将失去民心。"
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

    print(f"已为 4401–4500 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
