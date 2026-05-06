import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 将 3201–3300 号成语的详细信息补充到 enrich 字典中
    enrich = {
        3201: {
            "pinyin": "dà shuǐ chōng le lóng wáng miào",
            "meaning": "大水把龙王庙都冲了，比喻自己人之间因不相识而互相冲突或误会。",
            "example": "原来双方都是一个系统的同事，真是大水冲了龙王庙，一家人不认一家人。"
        },
        3202: {
            "pinyin": "dà sì huī huò",
            "meaning": "肆意挥霍金钱，奢侈浪费。",
            "example": "中彩票后他开始大肆挥霍，不久便又回到一贫如洗的境地。"
        },
        3203: {
            "pinyin": "dà sì pū zhāng",
            "meaning": "铺张：讲排场，摆阔气。形容过分讲究排场，浪费钱财。",
            "example": "办婚礼重在真诚，不必大肆铺张。"
        },
        3204: {
            "pinyin": "dà sì xuān chuán",
            "meaning": "到处大张旗鼓地宣传，多含贬义。",
            "example": "一项普通活动没必要大肆宣传，反而容易引起反感。"
        },
        3205: {
            "pinyin": "dà tí xiǎo zuò",
            "meaning": "题目定得很大，实际做得很小，比喻名义上说得很大而实干不足。",
            "example": "若只是口号响亮而措施乏力，那就成了大题小做。"
        },
        3206: {
            "pinyin": "dà tíng guǎng zhòng",
            "meaning": "朝廷广大的公众场合，比喻众目睽睽之下。",
            "example": "他在大廷广众之下公开道歉，态度诚恳。"
        },
        3207: {
            "pinyin": "dà shà jiāng diān",
            "meaning": "高大的楼宇将要倾倒，比喻局势危急，整个机构或国家快要覆灭。",
            "example": "企业连年亏损，大厦将颠，必须痛下决心改革。"
        },
        3208: {
            "pinyin": "dà xiāng jìng tíng",
            "meaning": "迳庭：差别很大。形容两者之间截然不同，相差悬殊。",
            "example": "他说的和事实大相迳庭，根本不能采信。"
        },
        3209: {
            "pinyin": "dà xǐ ruò kuáng",
            "meaning": "高兴得像发狂一样，形容极度兴奋、欣喜若狂。",
            "example": "听到考上理想大学的消息，全家人无不大喜若狂。"
        },
        3210: {
            "pinyin": "dài mǎ wàng běi",
            "meaning": "代国的马向北眺望故土，比喻思念故乡或旧主。",
            "example": "他旅居海外多年，仍如代马望北，心系故园。"
        },
        3211: {
            "pinyin": "dài mǎ yī fēng",
            "meaning": "代地的马迎风伫立，比喻骏马矫健或志向高远。",
            "example": "少年壮志凌云，如代马依风，意气风发。"
        },
        3212: {
            "pinyin": "dài rén shuō xiàng",
            "meaning": "替别人向权贵说好话或推荐，表示为人奔走举荐。",
            "example": "他愿意代人说项，帮助年轻人争取机会。"
        },
        3213: {
            "pinyin": "dài wéi shuō xiàng",
            "meaning": "代替别人说情或推荐，与“代人说项”意义相近。",
            "example": "若你真有实力，自会有人代为说项。"
        },
        3214: {
            "pinyin": "dài yuè páo zǔ",
            "meaning": "越俎代庖的倒装，说的是本该厨师干的活被别人代劳，比喻越权办事。",
            "example": "专业的事情应交给专业的人，切勿代越庖俎。"
        },
        3215: {
            "pinyin": "dài jiǎn yāo wéi",
            "meaning": "腰带渐渐缩短，形容人因病或忧愁而日渐消瘦。",
            "example": "近来他为项目操心过度，带减腰围，面容憔悴。"
        },
        3216: {
            "pinyin": "dài lì hé shān",
            "meaning": "带：衣带；砺：磨刀石；河：黄河；山：泰山。比喻时间久远、誓言坚定，国运长久或情谊不变。",
            "example": "两国缔结盟约，誓保带砺河山之好。"
        },
        3217: {
            "pinyin": "dài shuǐ tuō ní",
            "meaning": "原指道路泥泞难行，后比喻做事拖拉、不干脆或文章累赘。",
            "example": "写作要言简意赅，切忌带水拖泥。"
        },
        3218: {
            "pinyin": "dài zuì lì gōng",
            "meaning": "身带罪名立下功劳，多指立功赎罪。",
            "example": "他虽曾犯错，如今带罪立功，也算将功折罪。"
        },
        3219: {
            "pinyin": "dài jiǎ ér gū",
            "meaning": "贾：买卖；沽：卖。比喻怀才以待时机，一旦有人求购就出仕或献身某事。",
            "example": "他宁愿潜心著述，静待佳音，真是待贾而沽的高士。"
        },
        3220: {
            "pinyin": "dài tù shǒu zhū",
            "meaning": "比喻心存侥幸，守着老经验不思进取，也指坐等意外收获。",
            "example": "市场竞争激烈，若还想着待兔守株，迟早会被淘汰。"
        },
        3221: {
            "pinyin": "dài yuè xī xiāng",
            "meaning": "出自《西厢记》“待月西厢下”，多用来描写闺阁相思或幽会情景。",
            "example": "那回中秋之夜，他独自徘徊廊下，有几分待月西厢的寂寞。"
        },
        3222: {
            "pinyin": "dài fà hán chǐ",
            "meaning": "头上长发、嘴里长牙，比喻年纪尚幼。",
            "example": "我当年戴发含齿之时，便随父亲游历四方。"
        },
        3223: {
            "pinyin": "dài fà hán yá",
            "meaning": "与“戴发含齿”同，指孩童年幼之时。",
            "example": "自你戴发含牙起，我便视你如己出。"
        },
        3224: {
            "pinyin": "dài gāo mào r",
            "meaning": "给人戴上高帽儿，比喻说奉承话、吹捧别人。",
            "example": "别给我戴高帽儿，还是多提点实在的意见吧。"
        },
        3225: {
            "pinyin": "dài gāo mào zi",
            "meaning": "同“戴高帽儿”，指阿谀奉承、吹捧别人。",
            "example": "他向来不爱听人戴高帽子，更看重实际成绩。"
        },
        3226: {
            "pinyin": "dài jī pèi tún",
            "meaning": "戴着鸡佩着猪，多指古代的一种礼俗，也比喻礼节周全。",
            "example": "乡人迎亲时鸡鸣豚吠，仿佛旧日戴鸡佩豚的礼仪重现。"
        },
        3227: {
            "pinyin": "dān jīng jí lǜ",
            "meaning": "竭尽心力地思考筹划，极尽忧虑之苦。",
            "example": "他为公司转型殚精极虑，几乎夜夜难眠。"
        },
        3228: {
            "pinyin": "dān jīng jié lì",
            "meaning": "竭尽全部精力和力气。",
            "example": "只要大家殚精竭力，这个项目一定能成功。"
        },
        3229: {
            "pinyin": "dān móu lù lì",
            "meaning": "殚：用尽；戮力：合力。竭尽谋划，合力经营。",
            "example": "众人殚谋戮力，终于渡过了难关。"
        },
        3230: {
            "pinyin": "dān shí zhī chǔ",
            "meaning": "儋石：很少的储粮。比喻微薄的家产或储备。",
            "example": "他一生清廉，至老不过儋石之储。"
        },
        3231: {
            "pinyin": "dǎn chàn xīn jīng",
            "meaning": "吓得胆子发颤、心里惊怕，形容非常害怕。",
            "example": "那次车祸的经历至今令他胆颤心惊。"
        },
        3232: {
            "pinyin": "dǎn dà pō tiān",
            "meaning": "形容胆量极大，敢作敢为，有时含鲁莽之意。",
            "example": "他做事胆大泼天，却不懂权衡风险。"
        },
        3233: {
            "pinyin": "dǎn dà xīn xióng",
            "meaning": "胆量大而心气豪雄。",
            "example": "这些青年个个胆大心雄，不畏艰难。"
        },
        3234: {
            "pinyin": "dǎn dà yú shēn",
            "meaning": "形容胆量之大远远超过自身条件，多含褒义的勇敢或贬义的冒进。",
            "example": "创业需要胆大于身，但也要有周密的计划。"
        },
        3235: {
            "pinyin": "dǎn hán fà shù",
            "meaning": "吓得寒气从心底升起、头发直竖，形容极度恐惧。",
            "example": "听完那个惊悚故事，孩子们一个个胆寒发竖。"
        },
        3236: {
            "pinyin": "dǎn sàng hún jīng",
            "meaning": "吓得胆丧魂惊，极度害怕。",
            "example": "突如其来的爆炸声让路人胆丧魂惊。"
        },
        3237: {
            "pinyin": "dǎn sàng hún xiāo",
            "meaning": "吓得胆量丧失、魂魄消散，形容惊吓过度。",
            "example": "他在事故中亲眼见到惨状，几乎胆丧魂消。"
        },
        3238: {
            "pinyin": "dǎn xiǎo rú dòu",
            "meaning": "胆子小得像豆子一样，比喻非常胆小。",
            "example": "别看他人高马大，其实胆小如豆。"
        },
        3239: {
            "pinyin": "dǎn xiǎo rú xí",
            "meaning": "鼷：小鼠。比喻极其胆小。",
            "example": "孩子从小就胆小如鼷，需要多鼓励。"
        },
        3240: {
            "pinyin": "dǎn zhàn xīn huāng",
            "meaning": "吓得胆战心慌，十分恐惧不安。",
            "example": "第一次上台演讲，他难免胆战心慌。"
        },
        3241: {
            "pinyin": "dǎn zhàn xīn yáo",
            "meaning": "与“胆战心慌”近义，形容非常害怕、心神不定。",
            "example": "听到门外脚步声，他不由胆战心摇。"
        },
        3242: {
            "pinyin": "dǎn zhuàng qì cū",
            "meaning": "胆量大、气势粗豪。",
            "example": "他素来胆壮气粗，说话做事直来直去。"
        },
        3243: {
            "pinyin": "dǎn zhuàng xīn xióng",
            "meaning": "胆量很大、心气豪雄。",
            "example": "有这样一支胆壮心雄的队伍，再难的任务也能完成。"
        },
        3244: {
            "pinyin": "dàn mù rù dì",
            "meaning": "从早到晚忙碌奔走，几乎钻进地里，比喻奔走劳碌、营生辛苦。",
            "example": "他为一家人的生计旦暮入地，毫无怨言。"
        },
        3245: {
            "pinyin": "dàn huàn bù jīng",
            "meaning": "诞：荒唐；不经：不合常理。指荒诞虚幻、毫无根据。",
            "example": "这种说法实在诞幻不经，不足为凭。"
        },
        3246: {
            "pinyin": "dàn màn bù jīng",
            "meaning": "谩：荒诞不实。指胡说八道、不合事实。",
            "example": "他在酒席上的夸口，多半是诞谩不经。"
        },
        3247: {
            "pinyin": "dàn wǎng bù jīng",
            "meaning": "诞与罔并用，形容荒诞虚妄、不合情理。",
            "example": "这些谣言诞罔不经，听听也就罢了。"
        },
        3248: {
            "pinyin": "dàn wàng bù jīng",
            "meaning": "妄：胡乱。形容荒唐离谱、毫无根据的言论。",
            "example": "他对历史的评述多有牵强，实属诞妄不经。"
        },
        3249: {
            "pinyin": "tán jiá wú yú",
            "meaning": "弹铗而歌却无鱼可食，比喻怀才不遇或生活困顿。",
            "example": "他自比弹铗无鱼的士人，只愿秉持清节。"
        },
        3250: {
            "pinyin": "dàn wán hēi zhì",
            "meaning": "比喻极小的地方或事物。",
            "example": "在这弹丸黑志之地，他却干出了不凡的事业。"
        },
        3251: {
            "pinyin": "dàn wán hēi zǐ",
            "meaning": "比喻极小，多形容狭小之地或微不足道之物。",
            "example": "那村落不过弹丸黑子，却自成一番景致。"
        },
        3252: {
            "pinyin": "dàn yǔ qiāng lín",
            "meaning": "子弹像雨点般飞射、枪支像树林般密集，形容战斗激烈。",
            "example": "他们在弹雨枪林中突围而出，伤亡惨重。"
        },
        3253: {
            "pinyin": "dàn bó yǐ míng zhì，níng jìng yǐ zhì yuǎn",
            "meaning": "出自《诸葛亮诫子书》，意思是淡泊名利以表明志向，宁静寡欲以成就远大目标。",
            "example": "他常以“淡泊以明志，宁静以致远”勉励晚辈。"
        },
        3254: {
            "pinyin": "dàn fàn huáng jī",
            "meaning": "粗茶淡饭和咸菜，形容饮食清贫朴素。",
            "example": "他们虽只吃淡饭黄齑，却将供养节省下来做善事。"
        },
        3255: {
            "pinyin": "dàn sǎo é méi",
            "meaning": "轻轻扫拭蛾眉，形容女子化妆淡雅。",
            "example": "她淡扫蛾眉、素衣浅笑，自有一番清丽气质。"
        },
        3256: {
            "pinyin": "dàn xiě qīng miáo",
            "meaning": "着墨不多，略加勾勒，形容写作或绘画笔墨简淡。",
            "example": "这段景物描写淡写轻描，却极见功力。"
        },
        3257: {
            "pinyin": "dāng xíng ér wáng",
            "meaning": "出自《汉书·黥布传》，指先受刑受难，后又飞黄腾达。",
            "example": "他常以当刑而王的故事自勉，相信困厄终会过去。"
        },
        3258: {
            "pinyin": "dāng háng běn sè",
            "meaning": "指各自从事自己擅长的行业，发挥本色本领。",
            "example": "分工合作、当行本色，才能把项目做好。"
        },
        3259: {
            "pinyin": "dǎng è yòu jiān",
            "meaning": "偏袒、袒护奸恶之人。",
            "example": "若官员党恶佑奸，必将失去民心。"
        },
        3260: {
            "pinyin": "dǎng jiān shì shèng",
            "meaning": "党羽坚固、势力强大。",
            "example": "那时权臣党坚势盛，朝中正直之士多被排斥。"
        },
        3261: {
            "pinyin": "dǎng tóng dù yì",
            "meaning": "只偏袒同伙而妒忌不同意见的人。",
            "example": "为政者若党同妒异，终会贻害国家。"
        },
        3262: {
            "pinyin": "dǎng xié chǒu zhèng",
            "meaning": "与坏人结党，丑毁正直的人。",
            "example": "他上疏痛陈宦官党邪丑正之害。"
        },
        3263: {
            "pinyin": "dǎng xié xiàn zhèng",
            "meaning": "与邪恶之人结伙，陷害正直之人。",
            "example": "史书严斥那些党邪陷正的小人。"
        },
        3264: {
            "pinyin": "dǎng lùn kǎn kǎn",
            "meaning": "谠论：公正、正直的言论；侃侃：理直气壮。形容对上敢言直谏、从容有据。",
            "example": "他在会上谠论侃侃，不惧权贵。"
        },
        3265: {
            "pinyin": "dǎng yán jiā lùn",
            "meaning": "公正、正直而精彩有力的言论。",
            "example": "这份报告可谓谠言嘉论，切中时弊。"
        },
        3266: {
            "pinyin": "dàng chǎn qīng jiā",
            "meaning": "家产全部丧失，形容破产。",
            "example": "一次错误投资，让他荡产倾家。"
        },
        3267: {
            "pinyin": "dàng hǎi bá shān",
            "meaning": "摇动大海、拔起高山，比喻力气巨大或气势极其雄壮。",
            "example": "勇士们个个力能荡海拔山。"
        },
        3268: {
            "pinyin": "dàng hún shè pò",
            "meaning": "震撼心神，令人魂魄为之摇动。",
            "example": "那场交响乐气势恢宏，真可谓荡魂摄魄。"
        },
        3269: {
            "pinyin": "dāo gēng huǒ yún",
            "meaning": "用刀开垦、用火除草，比喻原始落后的农业生产方式，也形容艰苦创业。",
            "example": "祖辈在这片土地上刀耕火耘，才换来今日的丰收。"
        },
        3270: {
            "pinyin": "dāo guāng xuè yǐng",
            "meaning": "刀光闪烁、血影交错，形容杀戮惨烈的战场景象。",
            "example": "他从刀光血影中走出，更懂得和平的可贵。"
        },
        3271: {
            "pinyin": "dāo qiāng rù kù",
            "meaning": "刀枪收进兵器库，比喻战争结束、不再动武。",
            "example": "刀枪入库、马放南山，是人们共同的愿望。"
        },
        3272: {
            "pinyin": "dāo tóu jiàn shǒu",
            "meaning": "刀尖剑端，比喻险要之处或激烈对峙的前沿。",
            "example": "他总身先士卒，冲在刀头剑首之地。"
        },
        3273: {
            "pinyin": "dāo tóu yàn wěi",
            "meaning": "比喻文章或书法起笔如刀锋、收笔如燕尾，亦指器物形制前锐后阔。",
            "example": "这幅字笔势凌厉，真有刀头燕尾之姿。"
        },
        3274: {
            "pinyin": "dāo xià liú rén",
            "meaning": "在行刑或惩罚之前留人一命，用作宽恕或请求饶命之词。",
            "example": "他苦苦哀求刀下留人，希望官府从轻发落。"
        },
        3275: {
            "pinyin": "dāo zǔ yú shēng",
            "meaning": "刀俎之下幸存，比喻在极其危险的境地中侥幸活下来。",
            "example": "他从敌营中刀俎余生，更加珍惜和平。"
        },
        3276: {
            "pinyin": "dǎo yǐ qǔ bǎo",
            "meaning": "以劝导的方式使人选择自保，多指开导他人走稳妥之路。",
            "example": "朋友几番导以取保，他终于打消了铤而走险的念头。"
        },
        3277: {
            "pinyin": "dǎo dé qí lǐ",
            "meaning": "用道德来引导，用礼制来整齐，使百姓归服。",
            "example": "古代圣王讲求导德齐礼，以德化民。"
        },
        3278: {
            "pinyin": "dào dǎ yī wǎ",
            "meaning": "犹言倒打一耙，比喻自己有错反而先责怪别人。",
            "example": "明明是他迟到，却还倒打一瓦埋怨别人没提醒。"
        },
        3279: {
            "pinyin": "dài lì gù jiāo",
            "meaning": "指贫贱时结交的老朋友。",
            "example": "他成名后仍与当年戴笠故交往来如初。"
        },
        3280: {
            "pinyin": "dài méi hán chǐ",
            "meaning": "头上生眉、口中生齿，比喻年纪尚轻的少年。",
            "example": "我戴眉含齿之时，常听祖母讲旧时故事。"
        },
        3281: {
            "pinyin": "dài qīng lǚ zhuó",
            "meaning": "清指天、浊指地，犹言戴天履地，形容人活在天地之间。",
            "example": "人一生戴清履浊，当知敬畏天地。"
        },
        3282: {
            "pinyin": "dài rì dài dòu",
            "meaning": "头顶日月星斗，犹言普天之下。",
            "example": "戴日戴斗，人人皆盼太平盛世。"
        },
        3283: {
            "pinyin": "dài shuāng lǚ bīng",
            "meaning": "头顶霜雪、脚踏冰地，形容不畏严寒、奔波劳作。",
            "example": "邮递员戴霜履冰，把邮件按时送到山村。"
        },
        3284: {
            "pinyin": "dài tiān jí dì",
            "meaning": "犹言戴天履地，头顶青天、脚踏大地，形容人的生存处境或所受恩德之深。",
            "example": "蒙父母养育之恩，如戴天蹐地，终身难报。"
        },
        3285: {
            "pinyin": "dài xuán lǚ huáng",
            "meaning": "玄指天、黄指地，犹言戴天履地，形容人活在天地之间。",
            "example": "他戴玄履黄一生行善，终得善终。"
        },
        3286: {
            "pinyin": "dān huáng jiǎ yǐ",
            "meaning": "以朱笔、黄笔在书上点校、评定次第。比喻精心考订文献。",
            "example": "学者花多年光阴丹黄甲乙，只为还原历史真相。"
        },
        3287: {
            "pinyin": "dān qī suí mèng",
            "meaning": "出自《文心雕龙》，后来用以指追随古圣先贤的脚步。",
            "example": "他立志丹漆随梦，潜心研读先贤著作。"
        },
        3288: {
            "pinyin": "dān qiān jiǎ yǐ",
            "meaning": "与“丹黄甲乙”义近，指用朱墨标点、评定文稿。",
            "example": "编辑们为这套文集丹铅甲乙，反复推敲字句。"
        },
        3289: {
            "pinyin": "dān qīng miào shǒu",
            "meaning": "丹青：绘画；妙手：技艺高超的人。指绘画技艺高超的画家。",
            "example": "这幅山水出自丹青妙手，气韵生动。"
        },
        3290: {
            "pinyin": "dān shū bái mǎ",
            "meaning": "古时急件文书常用赤字书写并由白马驿使传递，后以“丹书白马”指重要诏令或盟约。",
            "example": "两国缔结丹书白马之盟，誓保边境安宁。"
        },
        3291: {
            "pinyin": "dān jīng rěn pà",
            "meaning": "承受惊吓却强自忍耐，形容长期在恐惧压力下生活。",
            "example": "那些年他在战乱中担惊忍怕，终于盼来和平。"
        },
        3292: {
            "pinyin": "dān jīng shòu kǒng",
            "meaning": "不断惊惧、承受恐吓，形容长期提心吊胆。",
            "example": "受暴家庭中的孩子常年担惊受恐。"
        },
        3293: {
            "pinyin": "dān xuě tián hé",
            "meaning": "拿雪去填河，比喻徒劳无功的事。",
            "example": "不从体制上改革，单靠临时补贴无异于担雪填河。"
        },
        3294: {
            "pinyin": "ē dǎng xiāng wéi",
            "meaning": "互相包庇、袒护，多指官吏之间互相偏袒。",
            "example": "若一味阿党相为，纪纲何以维持？"
        },
        3295: {
            "pinyin": "ē qí suǒ hào",
            "meaning": "迎合别人所爱好或所欲求的东西，多含贬义。",
            "example": "他善于阿其所好，专挑上司爱听的话说。"
        },
        3296: {
            "pinyin": "ē shí qū sú",
            "meaning": "附和时势、追逐流俗。",
            "example": "真正的学者不应阿时趋俗，而要坚守学术良知。"
        },
        3297: {
            "pinyin": "ē yú chǎn mèi",
            "meaning": "用甜言蜜语巴结人，极尽谄媚之态。",
            "example": "他整日阿谀谄媚，只图升官发财。"
        },
        3298: {
            "pinyin": "ē yú féng yíng",
            "meaning": "以谄媚阿谀的方式逢迎讨好他人。",
            "example": "这种阿谀逢迎的作风，终究不会长久。"
        },
        3299: {
            "pinyin": "ē yú fèng cheng",
            "meaning": "用过分恭维的话巴结奉承人。",
            "example": "他不屑于靠阿谀奉承获取职位。"
        },
        3300: {
            "pinyin": "ē yú qǔ róng",
            "meaning": "用谄媚奉承的方式取悦别人，以求容身或得宠。",
            "example": "在原则问题上，绝不能靠阿谀取容。"
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

    print(f"已为 3201–3300 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
