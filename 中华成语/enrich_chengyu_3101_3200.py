import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 将 3101–3200 号成语的详细信息补充到 enrich 字典中
    enrich = {
        3101: {
            "pinyin": "dāi rú mù jī",
            "meaning": "像木鸡一样呆住不动，形容十分惊愕或发愣的样子。",
            "example": "听到这个噩耗，他一时呆如木鸡，说不出话来。"
        },
        3102: {
            "pinyin": "dāi sì mù jī",
            "meaning": "同“呆如木鸡”，形容惊讶发愣、失去反应能力。",
            "example": "突如其来的变故，把在场的人都惊得呆似木鸡。"
        },
        3103: {
            "pinyin": "dèng shā tài lì",
            "meaning": "澄清沙石，淘汰杂质，比喻去粗取精、去伪存真。",
            "example": "治学当澄沙汰砾，只取真正有价值的资料。"
        },
        3104: {
            "pinyin": "dān jiàn qiǎn wén",
            "meaning": "见识单薄，学问肤浅。",
            "example": "我不过是单见浅闻，不敢对这个问题妄加评论。"
        },
        3105: {
            "pinyin": "dān jié dú lì",
            "meaning": "单：孤单；孑：孤立。形容孤身一人、独自存在或行动。",
            "example": "在异乡打拼多年，他始终单孑独立，习惯了一个人的生活。"
        },
        3106: {
            "pinyin": "dān qiāng dú mǎ",
            "meaning": "带一杆枪、骑一匹马，形容单独行动、没有帮手。",
            "example": "创业初期，他几乎是单枪独马扛下了所有事务。"
        },
        3107: {
            "pinyin": "dān sī bù xiàn",
            "meaning": "一根丝线成不了线，比喻单凭一人之力难成大事。",
            "example": "单丝不线，单木不林，团队合作远比个人英雄主义重要。"
        },
        3108: {
            "pinyin": "dān wén gū zhèng",
            "meaning": "只有一条文献或一份证据，比喻根据不足，不足以取信。",
            "example": "史料不过单文孤证，还需要更多旁证才能下结论。"
        },
        3109: {
            "pinyin": "dān yōu jí cuì",
            "meaning": "极尽忧虑辛劳之苦。单，通“殚”，竭尽之意。",
            "example": "他为这个项目单忧极瘁，几个月来几乎没睡过一个安稳觉。"
        },
        3110: {
            "pinyin": "dá guān guì yào",
            "meaning": "达官：高官；贵要：显贵要人。指地位高、权势重的大官显贵。",
            "example": "这次庆典上达官贵要云集，场面极为隆重。"
        },
        3111: {
            "pinyin": "dá guān yào rén",
            "meaning": "显赫的官员和要人。",
            "example": "会场内外守卫森严，多有达官要人出入其间。"
        },
        3112: {
            "pinyin": "dá quán tōng biàn",
            "meaning": "善于权衡利害，通晓变通之道，处理问题灵活而不拘泥。",
            "example": "面对复杂局势，他总能达权通变，找到折中方案。"
        },
        3113: {
            "pinyin": "dá shì tōng rén",
            "meaning": "通达事理、见识高明的人。",
            "example": "他为人豁达，是个难得的达士通人。"
        },
        3114: {
            "pinyin": "dǎ biān gǔ",
            "meaning": "在旁边敲鼓助兴，比喻从旁帮腔、帮忙说话或做辅助工作。",
            "example": "谈判还是你来主谈，我在一旁打边鼓就好。"
        },
        3115: {
            "pinyin": "dǎ cǎo shé jīng",
            "meaning": "敲打草丛，惊动了里面的蛇，比喻做事不谨慎，惊动对方。",
            "example": "行动之前一定要保密，千万别打草蛇惊。"
        },
        3116: {
            "pinyin": "dǎ fèng láo lóng",
            "meaning": "凤、龙：比喻才德高超的人或强有力的对手。比喻设法降服、制服强敌。",
            "example": "这一计正是为他量身打造，可谓打凤牢龙之策。"
        },
        3117: {
            "pinyin": "dǎ gōng zuò yī",
            "meaning": "作揖行礼，形容低声下气、过分恭敬的样子。",
            "example": "他见到上司总是打恭作揖，唯恐失了礼数。"
        },
        3118: {
            "pinyin": "dǎ gǒng zuò yī",
            "meaning": "打躬作揖，频频行礼，形容谦卑讨好的态度。",
            "example": "为了求情，他在厅上打拱作揖，不住赔罪。"
        },
        3119: {
            "pinyin": "dǎ gǔn sā pō",
            "meaning": "在地上打滚、撒泼，形容无理取闹或极度耍赖的样子。",
            "example": "孩子在地上打滚撒泼，只因为没买到想要的玩具。"
        },
        3120: {
            "pinyin": "dǎ hǔ láo lóng",
            "meaning": "捉拿猛虎、关住蛟龙，比喻制服强悍的对手或处理棘手的大事。",
            "example": "这支特遣队肩负打虎牢龙的任务，责任重大。"
        },
        3121: {
            "pinyin": "dǎ hùn chā kē",
            "meaning": "打诨、插科：戏曲中调笑逗乐的表演。比喻说笑话、装滑稽来逗人发笑。",
            "example": "他说话总爱打诨插科，活跃气氛。"
        },
        3122: {
            "pinyin": "dǎ jī bào fù",
            "meaning": "对别人加以攻击和报复，多指出于私心的打击。",
            "example": "用权力去打击报复下属，是绝对不被允许的。"
        },
        3123: {
            "pinyin": "dǎ jī mà gǒu",
            "meaning": "打鸡又骂狗，形容迁怒无辜或乱发脾气。",
            "example": "他工作不顺心，回家就打鸡骂狗，弄得全家气氛紧张。"
        },
        3124: {
            "pinyin": "dǎ jiā jié dào",
            "meaning": "打家劫舍、拦路抢劫，形容成群结伙进行抢掠活动。",
            "example": "这伙人专在深山里打家截道，危害一方百姓。"
        },
        3125: {
            "pinyin": "dǎ jiā jié shè",
            "meaning": "闯进人家抢劫财物，和“打家截道”意义相近。",
            "example": "官府雷厉风行，终于把那帮打家截舍的匪徒一网打尽。"
        },
        3126: {
            "pinyin": "dǎ jiē mà xiàng",
            "meaning": "在街头巷尾打打骂骂，形容吵闹喧嚣、不讲体面。",
            "example": "夫妻俩为小事打街骂巷，邻里都为之侧目。"
        },
        3127: {
            "pinyin": "dà fā yì lùn",
            "meaning": "对某事议论纷纷、大肆评论。",
            "example": "新政一出台，各界人士纷纷大发议论。"
        },
        3128: {
            "pinyin": "dà fàng jué cí",
            "meaning": "厥辞：浮夸的言辞。形容大发议论或说话夸张、不切实际。",
            "example": "他在会上大放厥辞，却拿不出任何可行方案。"
        },
        3129: {
            "pinyin": "dà gōng gào chéng",
            "meaning": "大的工程宣告完成。比喻重大的事业顺利结束。",
            "example": "历时数年的水利工程终于大工告成。"
        },
        3130: {
            "pinyin": "dà gōng bì chéng",
            "meaning": "巨大的功业已经完成。",
            "example": "等到大功毕成之日，大家都能松一口气。"
        },
        3131: {
            "pinyin": "dà hǎn dà jiào",
            "meaning": "又喊又叫，形容声音大而吵闹。",
            "example": "孩子们在院子里大喊大叫，玩得不亦乐乎。"
        },
        3132: {
            "pinyin": "dà hàn wàng yún",
            "meaning": "大旱之时仰望天边云彩，形容在困境中迫切盼望转机或援助。",
            "example": "资金迟迟不到位，让团队如大旱望云般焦急。"
        },
        3133: {
            "pinyin": "dà hóng dà lǜ",
            "meaning": "颜色非常鲜艳的红和绿，多用来形容色彩俗艳或不协调。",
            "example": "屋里装饰得大红大绿，看上去颇为扎眼。"
        },
        3134: {
            "pinyin": "dà hóng dà zǐ",
            "meaning": "比喻非常红火、走红，受人追捧。",
            "example": "这部电视剧播出后，主演一时间大红大紫。"
        },
        3135: {
            "pinyin": "dà hū xiǎo hè",
            "meaning": "大声呼喊、小声喝骂，形容吆喝声不断、喧哗吵闹。",
            "example": "集市上商贩大呼小喝，叫卖声此起彼伏。"
        },
        3136: {
            "pinyin": "dà hū xiǎo jiào",
            "meaning": "又大叫又小喊，形容吵闹不休。",
            "example": "楼上的装修声大呼小叫，让人难以入睡。"
        },
        3137: {
            "pinyin": "dà jiàn mí liú",
            "meaning": "指病势恶化、性命垂危的阶段。",
            "example": "老人病势已是大渐弥留，家人都守在床前。"
        },
        3138: {
            "pinyin": "dà jiàng yùn jīn",
            "meaning": "大匠：技艺高超的工匠；运斤：挥动斧子。比喻技艺高超、运用自如。",
            "example": "他修改文稿时如大匠运斤，寥寥数笔便令文气大增。"
        },
        3139: {
            "pinyin": "dà jīng dà fǎ",
            "meaning": "重要的经典与法度，比喻根本的大道理和制度规范。",
            "example": "治国理政须循大经大法，不可任性而为。"
        },
        3140: {
            "pinyin": "dà kāi fāng biàn zhī mén",
            "meaning": "大大敞开方便之门，形容给予极大的便利与照顾。",
            "example": "有关部门为企业大开方便之门，加快审批流程。"
        },
        3141: {
            "pinyin": "dà kuài duǒ yí",
            "meaning": "朵颐：动腮颊，形容吃东西。大块朵颐指尽情大吃，吃得很香。",
            "example": "一桌美味佳肴摆上来，大家都大块朵颐，十分尽兴。"
        },
        3142: {
            "pinyin": "dà lù zhuī lún",
            "meaning": "大辂由原始的椎轮演变而来，比喻事物由粗陋到精致、逐步发展完善。",
            "example": "科学技术的发展也是从大路椎轮到精密仪器的过程。"
        },
        3143: {
            "pinyin": "dà mǎ jīn dāo",
            "meaning": "原指军中披甲执刀的威武气象，后多形容说话做事豪迈不拘小节。",
            "example": "他办事大马金刀，向来不喜欢拖泥带水。"
        },
        3144: {
            "pinyin": "dà yǎ jūn zǐ",
            "meaning": "品德高雅的君子，多指有修养、有气度的人。",
            "example": "他处事从容不迫，谦和有礼，可谓大雅君子。"
        },
        3145: {
            "pinyin": "dà yǎ zhī táng",
            "meaning": "能容纳高雅艺术和正大文章的场所，比喻庄重、高雅的环境。",
            "example": "这部作品足以登堂入室，步入大雅之堂。"
        },
        3146: {
            "pinyin": "dà yǎn wàng xiǎo yǎn",
            "meaning": "你看我、我看你，一时不知如何是好。",
            "example": "突如其来的提问让他们大眼望小眼，谁也答不上来。"
        },
        3147: {
            "pinyin": "dà yāo xiǎo hè",
            "meaning": "大声吆喝，小声喝骂，形容叫嚷声不断。",
            "example": "这条老街商贩众多，整日大吆小喝十分热闹。"
        },
        3148: {
            "pinyin": "dà yīn xī shēng",
            "meaning": "出自《老子》：“大音希声”。指真正伟大的声响反而无声，常用来比喻最高境界的艺术不事张扬。",
            "example": "这幅作品意在言外，可谓大音希声。"
        },
        3149: {
            "pinyin": "dà yǒng ruò qiè",
            "meaning": "真正的大勇反而像胆怯一样，不轻易逞强。",
            "example": "他沉稳内敛，大勇若怯，从不逞一时之勇。"
        },
        3150: {
            "pinyin": "dà yǒu jiàn dì",
            "meaning": "见解很深、很有道理。",
            "example": "这篇评论立意新颖，大有见地。"
        },
        3151: {
            "pinyin": "dà yǒu jìng tíng",
            "meaning": "迳庭：差别很大。形容两者之间相差悬殊。",
            "example": "他说的和事实大有迳庭，根本对不上。"
        },
        3152: {
            "pinyin": "dà yǒu wén zhāng",
            "meaning": "大有文章，比喻其中含有很多门道或隐情。",
            "example": "这份合同条款繁多，只怕大有文章，需要仔细审阅。"
        },
        3153: {
            "pinyin": "dà yǔ pāng tuó",
            "meaning": "形容雨下得很大、很急。",
            "example": "突然大雨滂沱，街上的行人四处躲避。"
        },
        3154: {
            "pinyin": "dà yǔ qīng pén",
            "meaning": "雨下得像用盆倒下来一样，形容雨势很大。",
            "example": "大雨倾盆而下，城市一时间积水严重。"
        },
        3155: {
            "pinyin": "dà yǔ rú zhù",
            "meaning": "雨下得像注水一样，形容雨势非常大。",
            "example": "山里忽然大雨如注，山路变得十分泥泞。"
        },
        3156: {
            "pinyin": "dà yǔ zhì shuǐ",
            "meaning": "指传说中大禹治理洪水的事迹，比喻治理大患、建功立业。",
            "example": "他常以大禹治水的故事勉励自己要不畏艰难。"
        },
        3157: {
            "pinyin": "dà zhǎn hóng tú",
            "meaning": "大展宏大的蓝图，比喻充分施展远大的抱负。",
            "example": "新公司成立，他准备在这片领域大展宏图。"
        },
        3158: {
            "pinyin": "dà zhí ruò qū",
            "meaning": "出自《老子》：“大直若屈”。指真正正直的人表面上反而像曲折一样。",
            "example": "他为人低调含蓄，可谓大直若诎。"
        },
        3159: {
            "pinyin": "dà zhí ruò qū",
            "meaning": "同“大直若诎”，比喻真正的正直并不外露锋芒。",
            "example": "在复杂的人事关系中，坚持原则的人往往大直若屈。"
        },
        3160: {
            "pinyin": "dà zhì dà yǒng",
            "meaning": "既有大智慧，又具大勇气。",
            "example": "要完成这项改革，需要领导层大智大勇。"
        },
        3161: {
            "pinyin": "dà zhì rú yú",
            "meaning": "真正有大智慧的人表面上好像很愚笨。",
            "example": "他平日寡言少语，大智如愚，其实胸有成竹。"
        },
        3162: {
            "pinyin": "dà zuò wén zhāng",
            "meaning": "在某事上大肆渲染或大作文章，多含贬义。",
            "example": "媒体不必在这件小事上大做文章，以免引起不必要的恐慌。"
        },
        3163: {
            "pinyin": "dú wǔ qióng bīng",
            "meaning": "黩武：好战；穷兵：极力用兵。指好战成性，滥用兵力。",
            "example": "历史上许多黩武穷兵的统治者，最终都落得亡国下场。"
        },
        3164: {
            "pinyin": "dā dā sā sā",
            "meaning": "形容眼皮下垂、无精打采的样子。",
            "example": "他熬夜之后精神不济，走路都搭搭撒撒的。"
        },
        3165: {
            "pinyin": "dá dì zhī gēn",
            "meaning": "指根底清楚明白，比喻情况了解得很透彻。",
            "example": "这位老乡对当地人情世故可谓达地知根。"
        },
        3166: {
            "pinyin": "dá guān zhī mìng",
            "meaning": "达观：看得开；知命：明白命运的安排。形容对世事看得开、能安于命。",
            "example": "经历风雨之后，他愈加达观知命，不再计较一时得失。"
        },
        3167: {
            "pinyin": "dǎ pò cháng guī",
            "meaning": "打破原有的常规做法，形容敢于创新、不拘泥于旧习。",
            "example": "这次活动打破常规，采用了全新的线上形式。"
        },
        3168: {
            "pinyin": "dǎ pò mí guān",
            "meaning": "打破心中的迷惑关口，比喻消除思想上的迷惘。",
            "example": "听了那番忠告，他终于打破迷关，看清了前路。"
        },
        3169: {
            "pinyin": "dǎ pò shā guō wèn dào dǐ",
            "meaning": "比喻追问事情的根底，非弄个水落石出不可。",
            "example": "他做事一向认真，总要打破砂锅问到底才放心。"
        },
        3170: {
            "pinyin": "dǎ qíng mà qù",
            "meaning": "一边打情骂俏、一边说笑打趣，多形容男女之间亲昵调笑。",
            "example": "两个人在角落里打情骂趣，旁人只好装作没看见。"
        },
        3171: {
            "pinyin": "dǎ qíng mài xiào",
            "meaning": "用卖弄风情、嬉笑取悦的方式讨好他人，多含贬义。",
            "example": "她在酒席上打情卖笑，让人颇感尴尬。"
        },
        3172: {
            "pinyin": "dǎ rén mà gǒu",
            "meaning": "又打人又骂狗，形容脾气暴躁、动辄打骂。",
            "example": "他喝醉后动辄打人骂狗，邻里都很头疼。"
        },
        3173: {
            "pinyin": "dǎ rù lěng gōng",
            "meaning": "原指后妃失宠被冷落在冷宫中，后多比喻受到冷遇或被弃用。",
            "example": "这个老项目早已被打入冷宫，没人愿意再提起。"
        },
        3174: {
            "pinyin": "dǎ sǐ hǔ",
            "meaning": "比喻抨击已失势的人，或趁对方无力反抗时大加攻击。",
            "example": "风头过后再出来指责，不过是打死虎而已。"
        },
        3175: {
            "pinyin": "dǎ sǐ lǎo hǔ",
            "meaning": "比喻打击已经倒台或失势的人。",
            "example": "事情过去多年，有些人却喜欢出来打死老虎，博取掌声。"
        },
        3176: {
            "pinyin": "dǎ xiǎo suàn pán",
            "meaning": "打得是自己的小算盘，比喻只顾眼前和个人的小利。",
            "example": "合作若各自打小算盘，项目很难做成。"
        },
        3177: {
            "pinyin": "dǎ yā jīng yuān",
            "meaning": "打鸭子却惊动了鸳鸯，比喻打甲惊乙，或牵连无辜之人。",
            "example": "处理问题要分清对象，别一不小心打鸭惊鸳。"
        },
        3178: {
            "pinyin": "dà bài kuī lún",
            "meaning": "形容遭到很大的失败和损失。",
            "example": "这次贸然扩张使公司大败亏轮，元气大伤。"
        },
        3179: {
            "pinyin": "dà cái cuī pán",
            "meaning": "指有大才干的人，与“大才盘盘”同义。",
            "example": "这些青年才俊皆是大才榱盘，将来必成栋梁。"
        },
        3180: {
            "pinyin": "dà cái cuī pán",
            "meaning": "同“大才榱盘”，形容才华横溢、器局宏大的人。",
            "example": "他学识渊博、胸怀宽广，可谓大才榱槃。"
        },
        3181: {
            "pinyin": "dà cái pán pán",
            "meaning": "槃槃：盛大、充盈的样子。指才干很大。",
            "example": "这支团队大才盘盘，足以承担国家级项目。"
        },
        3182: {
            "pinyin": "dà chī yī jīng",
            "meaning": "形容吃惊的程度很深。",
            "example": "听到这个决定，所有人都大吃一惊。"
        },
        3183: {
            "pinyin": "dà chuī dà dǎ",
            "meaning": "又吹又打，形容场面热闹或张扬铺排。",
            "example": "婚礼办得大吹大打，整个村子都听得见锣鼓声。"
        },
        3184: {
            "pinyin": "dà dà liē liē",
            "meaning": "形容性格粗枝大叶、做事随便不拘小节。",
            "example": "他为人虽然大大咧咧，却非常讲义气。"
        },
        3185: {
            "pinyin": "dà dǎn bāo shēn",
            "meaning": "胆量极大，形容非常大胆。",
            "example": "他竟敢独自夜探荒山，真是大胆包身。"
        },
        3186: {
            "pinyin": "dà dì chūn huí",
            "meaning": "大地恢复春意，形容万物复苏、生机勃勃的景象。",
            "example": "雪融冰消，大地春回，一派欣欣向荣。"
        },
        3187: {
            "pinyin": "dà dòng gān huǒ",
            "meaning": "形容非常生气，怒火中烧。",
            "example": "听闻有人造假，他气得大动肝火，当场发作。"
        },
        3188: {
            "pinyin": "dà dòng gōng guàn",
            "meaning": "形容公众群起而出、主持正义。",
            "example": "此事一经曝光，舆论大动公惯，纷纷声讨不法行为。"
        },
        3189: {
            "pinyin": "dà ēn dà dé",
            "meaning": "极大的恩情和德泽。",
            "example": "多年来蒙您照拂，大恩大德无以为报。"
        },
        3190: {
            "pinyin": "dà fā miù lùn",
            "meaning": "大肆发表荒谬的言论。",
            "example": "在不了解事实的情况下就大发谬论，只会误导他人。"
        },
        3191: {
            "pinyin": "dà mèng fāng xǐng",
            "meaning": "好像从长梦中刚刚醒来，比喻突然觉悟或看清真相。",
            "example": "经历这一番挫折，他如大梦方醒，重新审视自己的人生。"
        },
        3192: {
            "pinyin": "dà míng nán jū",
            "meaning": "名声太大，反而难以胜任或名不副实。",
            "example": "这职位要求极高，一般人只怕大名难居。"
        },
        3193: {
            "pinyin": "dà miù bù rán",
            "meaning": "大错特错，完全不是那回事。",
            "example": "若以为他只是贪图享乐，那就大缪不然了。"
        },
        3194: {
            "pinyin": "dà nì wú dào",
            "meaning": "罪大恶极，完全悖逆人伦和天道。",
            "example": "这伙人在战乱中烧杀抢掠，真是大逆无道。"
        },
        3195: {
            "pinyin": "dà qǐ dà luò",
            "meaning": "形容变化幅度极大，忽高忽低。",
            "example": "股市近期大起大落，投资需格外谨慎。"
        },
        3196: {
            "pinyin": "dà qǐng dà shòu",
            "meaning": "指受到十分优厚的款待或待遇。",
            "example": "他在东道主那里大请大受，吃住都极为讲究。"
        },
        3197: {
            "pinyin": "dà rén xiān shēng",
            "meaning": "对有身份或有学问者的敬称，有时也带讥讽意味。",
            "example": "大人先生既已远见卓识，何不拿出具体方案来？"
        },
        3198: {
            "pinyin": "dà shā fēng jǐng",
            "meaning": "严重破坏兴致和气氛。",
            "example": "他当众挑错，着实有些大杀风景。"
        },
        3199: {
            "pinyin": "dà shā fēng qù",
            "meaning": "大大扫了风趣，形容败坏兴致、令人扫兴。",
            "example": "本来大家谈得正高兴，他这一席话真是大煞风趣。"
        },
        3200: {
            "pinyin": "dà shù dǐ xià hǎo chéng liáng",
            "meaning": "比喻依附权势者可以得到庇护和好处。",
            "example": "他总想着靠关系，大树底下好乘凉，却从不肯脚踏实地。"
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

    print(f"已为 3101–3200 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
