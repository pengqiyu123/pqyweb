import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 将 3501–3600 号成语的详细信息补充到 enrich 字典中
    enrich = {
        3501: {
            "pinyin": "fǎ lún cháng zhuǎn",
            "meaning": "佛教用语，比喻佛法常住世间、不断弘扬，也泛指正道常行不息。",
            "example": "寺院钟声悠长，仿佛在诉说法轮常转的真义。"
        },
        3502: {
            "pinyin": "fǎ wài shī rén",
            "meaning": "在法律许可之外施行仁政或从宽处理，多指在不违背大原则前提下变通。",
            "example": "对初犯且悔意诚恳者，可以酌情法外施仁。"
        },
        3503: {
            "pinyin": "fā duǎn xīn cháng",
            "meaning": "头发虽短而心志很长，比喻外表平凡却胸怀远大抱负。",
            "example": "他出身寒微，却发短心长，一心想改变家乡面貌。"
        },
        3504: {
            "pinyin": "fā tū chǐ huò",
            "meaning": "头发脱落、牙齿破损，形容年老体衰的样子。",
            "example": "老人发秃齿豁，却仍精神矍铄。"
        },
        3505: {
            "pinyin": "fā yǐn qiān jūn",
            "meaning": "一发而引动千钧之力，比喻事情牵动重大利害或影响极大。",
            "example": "这项调整可谓发引千钧，必须慎之又慎。"
        },
        3506: {
            "pinyin": "fā zhǐ zì liè",
            "meaning": "愤怒到极点，头发竖起、眼眶欲裂，形容非常愤怒。",
            "example": "听闻暴行，他不禁发指眦裂。"
        },
        3507: {
            "pinyin": "fān rán gǎi tú",
            "meaning": "幡然：忽然猛然。忽然改变道路，比喻痛下决心改换方向或志向。",
            "example": "经历挫折之后，他幡然改途，走上了科研之路。"
        },
        3508: {
            "pinyin": "fān fù wú cháng",
            "meaning": "反复无定，变化多端，形容言行或局势多变不稳。",
            "example": "他做事翻复无常，难以让人信任。"
        },
        3509: {
            "pinyin": "fān jiāng dǎo hǎi",
            "meaning": "把江海都掀翻，比喻力量或气势极其浩大，也形容心中激荡不平。",
            "example": "乐曲高潮处如翻江倒海，令人热血沸腾。"
        },
        3510: {
            "pinyin": "fān kōng chū qí",
            "meaning": "在空中翻腾变换而出奇兵，比喻用非常规手段出奇制胜。",
            "example": "关键时刻他翻空出奇，提出了别人想不到的方案。"
        },
        3511: {
            "pinyin": "fān lái fù qù",
            "meaning": "形容翻转反复，常指心中思绪或身体辗转难眠。",
            "example": "他在床上翻来覆去，就是睡不着。"
        },
        3512: {
            "pinyin": "fān rán gǎi jìn",
            "meaning": "幡然：猛然。猛然改进，多指态度、作风等突然向好的方向转变。",
            "example": "受到批评后，他翻然改进，工作认真多了。"
        },
        3513: {
            "pinyin": "fān rán gǎi tú",
            "meaning": "忽然改变谋划或方向，多指从错误道路上回头。",
            "example": "他幡然改图，不再一味逐利，而是投身公益。"
        },
        3514: {
            "pinyin": "fān rán huǐ wù",
            "meaning": "猛然醒悟，深感悔恨。",
            "example": "经历挫败之后，他翻然悔悟，懂得了团队的重要。"
        },
        3515: {
            "pinyin": "fān shān yuè lǐng",
            "meaning": "翻过山岭，越过高山，形容旅途辛苦或路程遥远。",
            "example": "救援队翻山越岭，终于抵达受灾村庄。"
        },
        3516: {
            "pinyin": "fān shǒu wéi yún, fù shǒu wéi yǔ",
            "meaning": "一翻手是云，再翻手是雨，比喻反复无常或操纵局势轻而易举。",
            "example": "他在商场上翻手为云，覆手为雨，手段老练。"
        },
        3517: {
            "pinyin": "fān tiān fù dì",
            "meaning": "形容变化极大或斗争、动作非常激烈。",
            "example": "短短几年，家乡已发生翻天覆地的变化。"
        },
        3518: {
            "pinyin": "fān xiāng dǎo guì",
            "meaning": "把箱子、柜子都翻倒过来找东西，形容翻找得很乱很彻底。",
            "example": "他为找那本旧相册，翻箱倒柜忙了半天。"
        },
        3519: {
            "pinyin": "fān xiāng dǎo qiè",
            "meaning": "与“翻箱倒柜”相近，形容把箱箱柜柜翻得乱七八糟。",
            "example": "孩子们翻箱倒箧，把屋子弄得一团糟。"
        },
        3520: {
            "pinyin": "fān yún fù yǔ",
            "meaning": "翻动云层、覆下大雨，比喻权势极大，兴风作浪。",
            "example": "他一人之言，足以翻云覆雨，左右局势。"
        },
        3521: {
            "pinyin": "fán yán suì cí",
            "meaning": "烦琐零碎的言辞，形容话多而不着要点。",
            "example": "开会发言宜言简意赅，切莫烦言碎辞。"
        },
        3522: {
            "pinyin": "fán huā sì jǐn",
            "meaning": "繁多的鲜花好像锦绣一般，形容景色绚丽多彩。",
            "example": "园中春色正好，繁花似锦，美不胜收。"
        },
        3523: {
            "pinyin": "fán róng chāng shèng",
            "meaning": "形容事业、国家等兴旺发达，蒸蒸日上。",
            "example": "经过多年建设，城市经济日益繁荣昌盛。"
        },
        3524: {
            "pinyin": "fán róng fù qiáng",
            "meaning": "形容国家既繁荣又富强。",
            "example": "人民共同的愿望是建设一个繁荣富强的祖国。"
        },
        3525: {
            "pinyin": "fán wén mò jié",
            "meaning": "指多余而琐碎的礼节和手续。",
            "example": "办事重实效，不必拘泥繁文末节。"
        },
        3526: {
            "pinyin": "fán wén rù jié",
            "meaning": "指过多而繁琐的礼仪、手续。",
            "example": "这些繁文缛节不仅浪费时间，也影响效率。"
        },
        3527: {
            "pinyin": "fán xián jí guǎn",
            "meaning": "弦乐、管乐声繁多急促，形容音乐场面热闹非凡。",
            "example": "堂内繁弦急管，歌舞升平。"
        },
        3528: {
            "pinyin": "fán zhī xì jié",
            "meaning": "枝叶繁多而细小，比喻事物错综复杂的细节。",
            "example": "写作时应抓住主线，不要陷入繁枝细节。"
        },
        3529: {
            "pinyin": "fán fū ròu yǎn",
            "meaning": "凡俗之人的肉眼，比喻见识浅陋。",
            "example": "在凡夫肉眼看来，他不过是个普通人。"
        },
        3530: {
            "pinyin": "fán fū sú zǐ",
            "meaning": "平庸的普通人，多带轻视之意。",
            "example": "他志向远大，不甘做凡夫俗子。"
        },
        3531: {
            "pinyin": "fán shì yù zé lì, bù yù zé fèi",
            "meaning": "凡事事先预作准备就能成功，不预先准备就会失败。",
            "example": "项目管理讲究凡事预则立，不预则废。"
        },
        3532: {
            "pinyin": "fán tāi zhuó gǔ",
            "meaning": "指凡俗污浊的肉体，比喻普通人本性平凡。",
            "example": "他自谦只是凡胎浊骨，却立志有所作为。"
        },
        3533: {
            "pinyin": "fán táo sú lǐ",
            "meaning": "平凡的桃李，比喻寻常之辈或平常的作品。",
            "example": "在大师的杰作面前，其它作品皆成凡桃俗李。"
        },
        3534: {
            "pinyin": "fǎn bài wéi shèng",
            "meaning": "从失败转为胜利。",
            "example": "凭借周密部署，他们最终反败为胜。"
        },
        3535: {
            "pinyin": "fǎn bǔ zhī qíng",
            "meaning": "幼鸟长大后反过来哺养母鸟，比喻子女报答父母养育之情。",
            "example": "照顾年迈父母，是儿女应尽的反哺之情。"
        },
        3536: {
            "pinyin": "fǎn chún xiāng jī",
            "meaning": "受到指责时回嘴讥讽，形容不服气而顶撞对方。",
            "example": "他一听批评就反唇相讥，很难沟通。"
        },
        3537: {
            "pinyin": "fǎn chún xiāng jī",
            "meaning": "同“反唇相讥”，指以言语顶撞、讥笑对方。",
            "example": "同事之间应心平气和，不必反唇相稽。"
        },
        3538: {
            "pinyin": "fǎn fù wú cháng",
            "meaning": "反复变化，没有定准，形容态度或局势多变。",
            "example": "他做事反复无常，让人难以信赖。"
        },
        3539: {
            "pinyin": "fǎn gē xiāng xiàng",
            "meaning": "掉转兵器来对付原来一方，比喻倒戈相向。",
            "example": "昔日盟友如今反戈相向，令人唏嘘。"
        },
        3540: {
            "pinyin": "fǎn gē yī jī",
            "meaning": "掉转兵器给对方突然一击，比喻在关键时刻反击对手。",
            "example": "他表面示弱，最后却反戈一击，出其不意。"
        },
        3541: {
            "pinyin": "fǎn gōng zì wèn",
            "meaning": "回过头来检点自身言行，反省自己是否有过错。",
            "example": "遇事多些反躬自问，少些指责别人，矛盾自然会少。"
        },
        3542: {
            "pinyin": "fǎn gōng zì xǐng",
            "meaning": "回头审视、反省自己的行为。",
            "example": "他习惯在每天睡前反躬自省，总结得失。"
        },
        3543: {
            "pinyin": "fǎn jiàn zhī jì",
            "meaning": "利用敌人的间谍反过来欺骗敌人，比喻反用对方的计谋。",
            "example": "他们巧妙运用反间之计，使敌军内部互相猜忌。"
        },
        3544: {
            "pinyin": "fǎn jīng xíng quán",
            "meaning": "不按常规经义行事而采用权宜之计，比喻在非常时期采取灵活办法。",
            "example": "非常时期需要反经行权，但也要守住底线。"
        },
        3545: {
            "pinyin": "fǎn kè wéi zhǔ",
            "meaning": "客人反而成为主人，比喻局势逆转或后来者居上。",
            "example": "原本请他来协助，没想到渐渐反客为主。"
        },
        3546: {
            "pinyin": "fǎn láo wéi yì",
            "meaning": "把辛劳变为安逸，比喻用智慧减轻劳动或改善处境。",
            "example": "科学技术的发展正是为了反劳为逸，提高效率。"
        },
        3547: {
            "pinyin": "fǎn lǎo huán tóng",
            "meaning": "由老复少，好像又回到童年，多形容精神焕发或返老还童的状态。",
            "example": "坚持锻炼让他精神愈发矍铄，几近反老还童。"
        },
        3548: {
            "pinyin": "fǎn miàn jiào yuán",
            "meaning": "以反面人物或事例作为教育的教材，警戒人们。",
            "example": "这些贪腐案件成了最生动的反面教员。"
        },
        3549: {
            "pinyin": "fǎn miàn wén zhāng",
            "meaning": "从反面入手写文章或说明道理，以衬托正面。",
            "example": "这篇评论运用反面文章的手法，更凸显出正义的重要。"
        },
        3550: {
            "pinyin": "fǎn miàn wú qíng",
            "meaning": "翻脸不认人，毫不留情。",
            "example": "一旦触犯底线，他立刻反面无情，绝不姑息。"
        },
        3551: {
            "pinyin": "fǎn mù chéng chóu",
            "meaning": "由和睦转为仇敌，形容朋友反目成仇。",
            "example": "他们因利益纠纷反目成仇，实在可惜。"
        },
        3552: {
            "pinyin": "fǎn pú guī zhēn",
            "meaning": "去除浮华装饰，回复到质朴纯真的本来状态。",
            "example": "这部作品风格质朴，有反璞归真之美。"
        },
        3553: {
            "pinyin": "fǎn qí dào ér xíng zhī",
            "meaning": "与通常的做法相反而行，比喻采取与对方相反的策略。",
            "example": "在价格战中，他反其道而行之，主打高品质路线。"
        },
        3554: {
            "pinyin": "fǎn qiú zhū jǐ",
            "meaning": "出了问题不先责怪别人，而是回过头来要求自己。",
            "example": "遇到矛盾先反求诸己，往往更容易找到解决之道。"
        },
        3555: {
            "pinyin": "fǎn qiú fù chú",
            "meaning": "穿皮袍反面、背着草料，比喻本末倒置或行事颠倒。",
            "example": "只重形式不重内容，无异于反裘负刍。"
        },
        3556: {
            "pinyin": "fǎn shǒu kě dé",
            "meaning": "伸手一翻就能得到，比喻事情极易办成。",
            "example": "这点小忙对他来说反手可得，却十分关键。"
        },
        3557: {
            "pinyin": "fǎn shuǐ bù shōu",
            "meaning": "水一旦泼出就不能再收回，比喻话说出或事做出后难以挽回。",
            "example": "言语如反水不收，说出口前务必三思。"
        },
        3558: {
            "pinyin": "fǎn yǎn bù shí",
            "meaning": "翻白眼装作不认识，形容故意装作不相识或态度冷漠。",
            "example": "曾经的好友如今反眼不识，只因一场误会。"
        },
        3559: {
            "pinyin": "fǎn zhì qí shēn",
            "meaning": "把本来要施加在别人身上的办法或力量反过来用在自己身上。",
            "example": "对他人的要求也要反治其身，自我约束。"
        },
        3560: {
            "pinyin": "fǎn běn huán yuán",
            "meaning": "返回事物本来的根源或状态。",
            "example": "这场改革的目标是反本还原，让制度回归本意。"
        },
        3561: {
            "pinyin": "fǎn bǔ zhī ēn",
            "meaning": "反哺的恩情，比喻子女报答父母的养育之恩。",
            "example": "赡养双亲，是为人子女报答返哺之恩的应尽之责。"
        },
        3562: {
            "pinyin": "fǎn lǎo huán tóng",
            "meaning": "同“反老还童”，形容精神焕发、老当益壮。",
            "example": "常锻炼的人到了晚年也能返老还童般精神矍铄。"
        },
        3563: {
            "pinyin": "fǎn pǔ huán chún",
            "meaning": "回到朴素、淳厚的状态。",
            "example": "艺术创作到极致，往往要返朴还淳。"
        },
        3564: {
            "pinyin": "fǎn wǒ chū fú",
            "meaning": "回到最初朴素的状态，比喻返归本真。",
            "example": "经历世事之后，他愈发想返我初服，过简单生活。"
        },
        3565: {
            "pinyin": "fàn fàn ér tán",
            "meaning": "泛泛地谈论，浮于表面，缺乏深入。",
            "example": "对复杂问题不能只是泛泛而谈。"
        },
        3566: {
            "pinyin": "fàn fàn zhī jiāo",
            "meaning": "交情不深的朋友。",
            "example": "他与我不过泛泛之交，无需掏心置腹。"
        },
        3567: {
            "pinyin": "fàn fàn zhī rén",
            "meaning": "平庸普通之人或不甚了解之人。",
            "example": "对泛泛之人不必过多计较。"
        },
        3568: {
            "pinyin": "fàn làn chéng zāi",
            "meaning": "比喻事物不受控制地扩展发展，最终造成严重祸害。",
            "example": "若任由污染泛滥成灾，后果不堪设想。"
        },
        3569: {
            "pinyin": "fàn píng fú gěng",
            "meaning": "像水上的浮萍与木梗一样随波逐流，比喻人生漂泊无依。",
            "example": "他在外多年飘零，宛如泛萍浮梗。"
        },
        3570: {
            "pinyin": "fàn kēng jiǔ náng",
            "meaning": "饭坑酒囊，比喻只知吃喝、无所作为的人。",
            "example": "一个干部若成了饭坑酒囊，必为人所不齿。"
        },
        3571: {
            "pinyin": "fàn náng yī jià",
            "meaning": "装饭的口袋、挂衣服的架子，比喻只会吃穿而无其他本事的人。",
            "example": "他常自嘲不过是个饭囊衣架，需要多充实自己。"
        },
        3572: {
            "pinyin": "fàn qiǔ rú cǎo",
            "meaning": "吃干粮、啃野草，形容行军或流亡生活的艰苦。",
            "example": "革命先烈饭糗茹草，仍不改初心。"
        },
        3573: {
            "pinyin": "fàn ér bù jiào",
            "meaning": "别人冒犯自己也不计较，多形容宽宏大量。",
            "example": "对无心之失，还是犯而不校为好。"
        },
        3574: {
            "pinyin": "fàn shàng zuò luàn",
            "meaning": "触犯长上，发动叛乱。",
            "example": "嗜权者往往犯上作乱，终遭失败。"
        },
        3575: {
            "pinyin": "fàn yán jí jiàn",
            "meaning": "不顾自身安危而直言极力进谏。",
            "example": "为国为民者，当有犯颜极谏的勇气。"
        },
        3576: {
            "pinyin": "fàn zhāng jī shǔ",
            "meaning": "指范式、张劭鸡黍之约，后用以称颂朋友之间守信重义的情谊。",
            "example": "他们交往多年，情若范张鸡黍。"
        },
        3577: {
            "pinyin": "fàn fū fàn fù",
            "meaning": "平常的男人和女人，比喻普通百姓。",
            "example": "政策的好坏，最终要由贩夫贩妇来检验。"
        },
        3578: {
            "pinyin": "fàn fū zǒu zú",
            "meaning": "小贩和步行的小卒，比喻社会底层的普通人。",
            "example": "他从小就是贩夫走卒出身，更懂得民间疾苦。"
        },
        3579: {
            "pinyin": "fāng biàn zhī mén",
            "meaning": "比喻使事情容易办到的途径或方法。",
            "example": "互联网为学习提供了方便之门。"
        },
        3580: {
            "pinyin": "fāng cùn bù luàn",
            "meaning": "方寸：心。心中镇定，没有慌乱。",
            "example": "面对突发状况，他仍能方寸不乱。"
        },
        3581: {
            "pinyin": "fāng cùn wàn zhòng",
            "meaning": "一方寸之间承载万钧重担，比喻心事重重或责任重大。",
            "example": "身负重任，他只觉方寸万重，不敢稍有懈怠。"
        },
        3582: {
            "pinyin": "fāng cùn yǐ luàn",
            "meaning": "心绪已经十分紊乱。",
            "example": "接连的打击让他方寸已乱。"
        },
        3583: {
            "pinyin": "fāng cùn zhī dì",
            "meaning": "很小的一块地方，比喻狭小空间或人的内心。",
            "example": "这方寸之地，承载着他全部的回忆。"
        },
        3584: {
            "pinyin": "fāng dǐ yuán gài",
            "meaning": "器物的底是方的而盖是圆的，比喻两者不相称或不协调。",
            "example": "若人才与职位不符，便是方底圆盖，难以相容。"
        },
        3585: {
            "pinyin": "fāng lǐng jǔ bù",
            "meaning": "方形衣领、方正规矩的步伐，形容读书人举止谨慎、仪表端正。",
            "example": "他方领矩步，一看便知是饱学之士。"
        },
        3586: {
            "pinyin": "fāng ruì yuán zào",
            "meaning": "方形的榫头、圆形的卯眼，比喻二者格格不入、难以配合。",
            "example": "若强行合作，只会方枘圆凿，彼此掣肘。"
        },
        3587: {
            "pinyin": "fāng tóu bù liè",
            "meaning": "方：正直；不劣：不逊色。形容人正直不凡，不亚于他人。",
            "example": "他为人方头不劣，在同辈中颇受敬重。"
        },
        3588: {
            "pinyin": "fāng wài zhī rén",
            "meaning": "指超脱世俗、出家修行或隐居山林的人。",
            "example": "他本是方外之人，却一时兴起下山游历。"
        },
        3589: {
            "pinyin": "fāng xīng wèi ài",
            "meaning": "事物正在兴盛发展，还没有停止。",
            "example": "全民健身正方兴未艾，各地设施不断完善。"
        },
        3590: {
            "pinyin": "fāng yǐ lèi jù, wù yǐ qún fēn",
            "meaning": "同类的人互相聚集，同类的物彼此归属，比喻物以类聚、人以群分。",
            "example": "所谓方以类聚，物以群分，环境对人的影响极大。"
        },
        3591: {
            "pinyin": "fāng záo yuán ruì",
            "meaning": "与“方枘圆凿”同，形容双方不协调、不相容。",
            "example": "性格迥异的两人若强行共事，难免方凿圆枘。"
        },
        3592: {
            "pinyin": "fāng zhèng bù ē",
            "meaning": "性格方正，不阿谀奉承。",
            "example": "他为官一生方正不阿，深得民心。"
        },
        3593: {
            "pinyin": "fāng zhǐ yuán lú",
            "meaning": "脚是方的、头是圆的，原指人的外形，引申为芸芸众生。",
            "example": "芸芸众生方趾圆颅，各有各的活法。"
        },
        3594: {
            "pinyin": "fāng lán jìng tǐ",
            "meaning": "芳香的兰草遍布全身，比喻德行高洁、品格美好。",
            "example": "他一生清廉，如同芳兰竟体，为人景仰。"
        },
        3595: {
            "pinyin": "fāng nián huá yuè",
            "meaning": "芳华年少、光阴正好，形容青春美好的岁月。",
            "example": "在芳年华月之时，更应努力读书。"
        },
        3596: {
            "pinyin": "fáng bù jí fáng",
            "meaning": "防备来不及防备，形容事起突然，难以及时应对。",
            "example": "这场意外来得太快，真是防不及防。"
        },
        3597: {
            "pinyin": "fáng bù shèng fáng",
            "meaning": "再怎么防备也防不过来，形容情况复杂、隐患众多。",
            "example": "网络诈骗手段层出不穷，令人防不胜防。"
        },
        3598: {
            "pinyin": "fáng huàn wèi rán",
            "meaning": "在祸患还没有发生之前就加以防备。",
            "example": "安全工作要防患未然，而不是亡羊补牢。"
        },
        3599: {
            "pinyin": "fáng mín zhī kǒu, shèn yú fáng chuān",
            "meaning": "压制百姓言论比堵塞河川还要危险，多用来强调言论自由的重要性。",
            "example": "古人早有防民之口，甚于防川之戒。"
        },
        3600: {
            "pinyin": "fáng wēi dù jiàn",
            "meaning": "在事情的微小迹象刚出现时就加以堵塞和防范。",
            "example": "对不良风气要防微杜渐，不能听之任之。"
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

    print(f"已为 3501–3600 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
