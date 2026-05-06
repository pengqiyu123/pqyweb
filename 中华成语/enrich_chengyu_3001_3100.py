import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 将 3001–3100 号成语的详细信息补充到 enrich 字典中
    enrich = {
        3001: {
            "pinyin": "duǎn hè bù wán",
            "meaning": "短褐：粗布短衣；完：完整。粗布短衣还破旧不完整，形容生活贫困、衣衫褴褛。",
            "example": "少年时他家境清贫，短褐不完，却依旧勤奋读书。"
        },
        3002: {
            "pinyin": "duǎn hè chuān jié",
            "meaning": "褐衣破损而缝缀连结，形容衣着破旧、生活艰难。",
            "example": "那时百姓多是短褐穿结，却仍自食其力。"
        },
        3003: {
            "pinyin": "duǎn jiàn bó shí",
            "meaning": "见识短浅，学识肤浅。",
            "example": "此言实属短见薄识，不足为据。"
        },
        3004: {
            "pinyin": "duǎn xiǎo jīng hàn",
            "meaning": "身材虽矮小但精力充沛、勇猛干练。",
            "example": "这位短小精悍的经理，处理问题干脆利落。"
        },
        3005: {
            "pinyin": "duǎn yī pǐ mǎ",
            "meaning": "穿着短衣、骑着一匹马，形容行装简朴或轻装出行。",
            "example": "他短衣匹马走南闯北，靠本事闯出了名堂。"
        },
        3006: {
            "pinyin": "duǎn yuán zì yú",
            "meaning": "垣：矮墙；逾：越过。自己翻越自家短墙，比喻亲身违背礼制法度。",
            "example": "身为官长若徇私舞弊，无异于短垣自逾。"
        },
        3007: {
            "pinyin": "duàn bì cán zhāng",
            "meaning": "壁、璋都是古代玉器。残缺不全的玉璧玉璋，比喻虽有残缺但仍十分珍贵的事物。",
            "example": "这些传世残卷虽如断壁残璋，却极具研究价值。"
        },
        3008: {
            "pinyin": "duàn bì tuí yuán",
            "meaning": "残断的墙壁和倒塌的院墙，形容房屋残破、景象荒凉。",
            "example": "战火过后，只余断壁颓垣，令人唏嘘。"
        },
        3009: {
            "pinyin": "duàn biān cán jiǎn",
            "meaning": "残缺的书编简册，比喻散佚残存的典籍文献。",
            "example": "考古工作者从断编残简中还原了那段历史。"
        },
        3010: {
            "pinyin": "duàn cháng xù duǎn",
            "meaning": "截取长处来补充短处，比喻取长补短、弥补不足。",
            "example": "团队合作贵在断长续短，互相弥补缺陷。"
        },
        3011: {
            "pinyin": "duàn dòu jué fù",
            "meaning": "脰：脖子；决腹：剖腹。指砍头剖腹，形容牺牲惨烈。",
            "example": "他宁死不屈，断脰决腹以明志。"
        },
        3012: {
            "pinyin": "duàn fà wén shēn",
            "meaning": "剪断头发，在身上刺画花纹，多用来形容古代少数民族的习俗或表示决绝之志。",
            "example": "史书中记载的断发文身，反映了当时部族的风俗。"
        },
        3013: {
            "pinyin": "duàn gēn jué zhǒng",
            "meaning": "把根断掉，使其绝后，比喻彻底消灭、绝不容留。",
            "example": "对这些恶习必须断根绝种，不能姑息。"
        },
        3014: {
            "pinyin": "duàn gěng piāo péng",
            "meaning": "断梗随风、蓬草飘荡，比喻漂泊无依、流离失所。",
            "example": "战乱之中，许多百姓如断梗飘蓬，居无定所。"
        },
        3015: {
            "pinyin": "duàn hè xù fú",
            "meaning": "斩断鹤脚、接续鸭脚，比喻强行拼凑、不合情理的改变。",
            "example": "这番改动有如断鹤续凫，反而破坏了作品原有的神韵。"
        },
        3016: {
            "pinyin": "duàn huán guī zōng",
            "meaning": "指被卖或出嫁的女子由官府判决退回娘家，后也泛指让人回归原属之处。",
            "example": "经过审理，官府判决其妻断还归宗，各自安生。"
        },
        3017: {
            "pinyin": "duàn jī huà zhōu",
            "meaning": "断齑：少量咸菜；画粥：把一碗粥划分几块。形容生活清苦而又刻苦求学。",
            "example": "他在外求学时断齑画粥，却从未放松读书。"
        },
        3018: {
            "pinyin": "duàn jiǎn cán biān",
            "meaning": "残缺的竹简书编，比喻残存下来的古籍文献。",
            "example": "这些出土文书多为断简残编，需要细心整理。"
        },
        3019: {
            "pinyin": "duàn jǐng tuí yuán",
            "meaning": "废井倒塌的围墙，形容极其荒凉破败的景象。",
            "example": "多年无人居住的小院，只剩断井颓垣。"
        },
        3020: {
            "pinyin": "duàn jué rú liú",
            "meaning": "形容处理政务、断决狱讼果断迅速，如流水一般畅通。",
            "example": "这位法官断决如流，很快就给出了公正裁决。"
        },
        3021: {
            "pinyin": "duàn làn cháo bào",
            "meaning": "原指破旧的朝廷文书，后多比喻毫无价值的文章、报纸等文字材料。",
            "example": "这些小道消息不过是断烂朝报，不足采信。"
        },
        3022: {
            "pinyin": "duàn mò cán chǔ",
            "meaning": "写字到一半墨尽纸残，比喻文章未写完或事情半途而废。",
            "example": "他的回忆录只写到青年时期，便成了断墨残楮。"
        },
        3023: {
            "pinyin": "duàn shǒu xù yù",
            "meaning": "砍下手却接上一块玉，比喻因小失大、得不偿失。",
            "example": "若为一时虚名而毁掉前程，无异于断手续玉。"
        },
        3024: {
            "pinyin": "duàn tóu jiāng jūn",
            "meaning": "被砍头的将军，常用以称赞为国捐躯、死节的将领。",
            "example": "这位断头将军的事迹，至今仍被人们传颂。"
        },
        3025: {
            "pinyin": "duàn wú cǐ lǐ",
            "meaning": "断然说没有这个道理，用来表示事情极不合理、难以接受。",
            "example": "一味推卸责任，简直断无此理。"
        },
        3026: {
            "pinyin": "duàn xiàn fēng zhēng",
            "meaning": "线断了的风筝，比喻失去依靠、下落不明的人或事物。",
            "example": "公司解散后，他像断线风筝一样，不知该何去何从。"
        },
        3027: {
            "pinyin": "duàn xiàn ǒu xì",
            "meaning": "线断了的木偶戏，比喻事情突然中断或局面不可收拾。",
            "example": "资金链一断，这个项目立刻成了断线偶戏。"
        },
        3028: {
            "pinyin": "duàn xiù zhī pǐ",
            "meaning": "出自汉哀帝割袖典故，原指男男性关系，现多泛指同性恋。",
            "example": "古书中以断袖之癖来指称男子之间的爱情。"
        },
        3029: {
            "pinyin": "duàn yàn gū hóng",
            "meaning": "断孤的大雁、孤飞的鸿雁，比喻孤立无援或书信断绝。",
            "example": "他远在海外，与故乡亲友几成断雁孤鸿。"
        },
        3030: {
            "pinyin": "duàn yuán cán bì",
            "meaning": "断裂的墙垣和残缺的墙壁，形容建筑残破、环境荒凉。",
            "example": "老城里多是断垣残壁，需要尽快修缮。"
        },
        3031: {
            "pinyin": "duàn zhāng qǔ yì",
            "meaning": "割裂上下文，只取其中一段来解释意思，比喻曲解原意。",
            "example": "读文章不能断章取义，否则容易误解作者本意。"
        },
        3032: {
            "pinyin": "duàn zhāng zhāi jù",
            "meaning": "只摘取文章中的片段句子，不顾上下文，多用来形容引用不当。",
            "example": "新闻报道若断章摘句，容易误导读者。"
        },
        3033: {
            "pinyin": "duàn zhī quàn xué",
            "meaning": "出自“断织劝学”的故事，比喻用恰当的比喻劝人勤学不辍。",
            "example": "她以断织劝学的故事鼓励孩子不要轻言放弃。"
        },
        3034: {
            "pinyin": "duàn zhī zhī jiè",
            "meaning": "出自“断机教子”典故，比喻用中断织布来告诫后人勤学的重要性。",
            "example": "古人断织之诫，千百年来一直被用来劝学。"
        },
        3035: {
            "pinyin": "duàn zhǔ zé lín",
            "meaning": "断杼：断机；择邻：选择好邻居。出自“断机择邻”的故事，比喻择师从友应谨慎。",
            "example": "父母望子成龙，在学校与师友的选择上格外注意断杼择邻。"
        },
        3036: {
            "pinyin": "duī àn yíng jī",
            "meaning": "案头的文稿堆积到几案都满了，形容文书、书籍极多。",
            "example": "他书房中堆案盈几，几乎无处下脚。"
        },
        3037: {
            "pinyin": "duī jī rú shān",
            "meaning": "堆积得像山一样高，形容数量极多。",
            "example": "仓库里货物堆积如山，一时难以清点完毕。"
        },
        3038: {
            "pinyin": "duī jīn dié yù",
            "meaning": "金银堆积、珠玉叠放，形容财富极其丰厚。",
            "example": "古籍中常有宫中堆金叠玉的奢华描写。"
        },
        3039: {
            "pinyin": "duī jīn jī yù",
            "meaning": "金玉堆积，形容财富极多、极为富有。",
            "example": "他虽身居堆金积玉之地，却仍保持俭朴。"
        },
        3040: {
            "pinyin": "duī shān jī hǎi",
            "meaning": "像山一样堆叠、像海一样汇聚，形容数量特别巨大。",
            "example": "战后废墟堆山积海，重建任务十分艰巨。"
        },
        3041: {
            "pinyin": "duì bù gōng táng",
            "meaning": "上公堂对簿陈词，指在法庭上受审或对质。",
            "example": "两家因宅基地纠纷对簿公堂多年。"
        },
        3042: {
            "pinyin": "duì chuáng yè yǔ",
            "meaning": "好友久别重逢，同床夜谈、听雨叙旧，比喻久别相聚的深情。",
            "example": "多年未见的同窗再聚，对床夜雨，话不完的往事。"
        },
        3043: {
            "pinyin": "duì dá rú liú",
            "meaning": "形容口才好，回答问题非常流利、顺畅。",
            "example": "他对业务烂熟于心，面试中对答如流。"
        },
        3044: {
            "pinyin": "duì jǐng guà huà",
            "meaning": "指在适当位置陈设字画，使环境与画面相得益彰，也比喻恰到好处的点缀。",
            "example": "客厅里一幅山水画对景挂画，平添几分雅致。"
        },
        3045: {
            "pinyin": "duì jǐng shāng qíng",
            "meaning": "面对眼前景物而触动情思，多指因景物勾起伤感。",
            "example": "再游旧地，他不免对景伤情。"
        },
        3046: {
            "pinyin": "duì jiǔ dāng gē",
            "meaning": "面对美酒就高声歌唱，形容借酒抒怀或及时行乐的情绪。",
            "example": "他举杯长叹，对酒当歌，感慨人生短暂。"
        },
        3047: {
            "pinyin": "duì niú tán qín",
            "meaning": "对着牛弹琴，比喻对不懂道理或不讲道理的人讲道理，白费口舌。",
            "example": "他根本不愿沟通，再多解释也是对牛弹琴。"
        },
        3048: {
            "pinyin": "duì tóu yuān jiā",
            "meaning": "彼此结下梁子、互相仇视的人。",
            "example": "两家因旧事成了对头冤家，多年难以化解。"
        },
        3049: {
            "pinyin": "duì zhèng xià yào",
            "meaning": "针对病症开药，比喻针对问题的关键采取措施。",
            "example": "只有找准矛盾焦点，才能对症下药。"
        },
        3050: {
            "pinyin": "duì zhèng zhī yào",
            "meaning": "针对病症的药方，比喻解决问题的有效办法。",
            "example": "这几条改革措施正是治理乱象的对症之药。"
        },
        3051: {
            "pinyin": "dūn shī shuō lǐ",
            "meaning": "出自“敦诗说礼”，指研读诗经、讲说礼制，比喻重视道德教化和礼乐教养。",
            "example": "古代士大夫多以敦诗说礼为修身之本。"
        },
        3052: {
            "pinyin": "dùn kāi máo sè",
            "meaning": "茅塞：比喻思路闭塞。一下子打通了思想上的郁结，形容忽然醒悟。",
            "example": "听完老师的讲解，他顿开茅塞，题目迎刃而解。"
        },
        3053: {
            "pinyin": "dùn kǒu wú yán",
            "meaning": "嘴巴立刻噤住说不出话来，形容无言以对或非常惊讶。",
            "example": "被问到细节，他顿口无言，只好连连赔笑。"
        },
        3054: {
            "pinyin": "dùn kǒu zhuō sāi",
            "meaning": "形容说话笨拙、不善言辞的样子。",
            "example": "他为人老实，却顿口拙腮，不会辩解自己。"
        },
        3055: {
            "pinyin": "dùn shǒu zài bài",
            "meaning": "古代一种隆重礼节，磕头至地，再拜致敬，表示极其恭敬。",
            "example": "他在先贤塑像前顿首再拜，以示崇敬。"
        },
        3056: {
            "pinyin": "dùn xué lěi gōng",
            "meaning": "指虽然起步较晚，但能勤学积累，也可以取得成就。",
            "example": "只要肯顿学累功，后来者一样可以赶上前人。"
        },
        3057: {
            "pinyin": "dùn zú bù qián",
            "meaning": "跺脚却不向前走，形容焦急懊恼却又无计可施。",
            "example": "资金迟迟不到位，让项目负责人顿足不前。"
        },
        3058: {
            "pinyin": "dùn zú chuí xiōng",
            "meaning": "跺脚捶胸，形容极度后悔或悲痛。",
            "example": "事后他才意识到失误之大，顿足捶胸懊恼不已。"
        },
        3059: {
            "pinyin": "dùn jì qián xíng",
            "meaning": "躲藏踪迹、隐匿形迹，形容深居简出、不露行迹。",
            "example": "他退隐山林，遁迹潜形，再不过问世事。"
        },
        3060: {
            "pinyin": "dùn míng nì jì",
            "meaning": "隐藏姓名、隐匿行迹，多形容不图名利、避世隐居。",
            "example": "这位高人遁名匿迹，多年无人知其行踪。"
        },
        3061: {
            "pinyin": "dùn rù kōng mén",
            "meaning": "指出家为僧尼，投入佛门修行。",
            "example": "看破红尘后，他索性遁入空门。"
        },
        3062: {
            "pinyin": "duō cái duō yì",
            "meaning": "有许多才华，通晓多种艺术。",
            "example": "她琴棋书画样样精通，可谓多才多艺。"
        },
        3063: {
            "pinyin": "duō cái shàn gǔ",
            "meaning": "贾：经商。既多财又善于经商，形容人富有而精明。",
            "example": "这位老老板多财善贾，生意越做越大。"
        },
        3064: {
            "pinyin": "duō cáng hòu wáng",
            "meaning": "藏财过多反而招致祸患，比喻吝啬贪婪最终会带来灭亡。",
            "example": "古书早有多藏厚亡之戒，企业经营亦当慎之。"
        },
        3065: {
            "pinyin": "duō chóu duō bìng",
            "meaning": "忧愁过多容易致病，形容因烦忧而损害健康。",
            "example": "医生提醒他要放宽心，省得多愁多病。"
        },
        3066: {
            "pinyin": "duō chóu shàn gǎn",
            "meaning": "多愁而又感情细腻，容易触景生情。",
            "example": "她性情多愁善感，一首歌都能听得落泪。"
        },
        3067: {
            "pinyin": "duō cǐ yī jǔ",
            "meaning": "多此一举：做了本不必要做的事，形容多余而无益的举动。",
            "example": "既然已经网上报名，再跑一趟现场就有些多此一举了。"
        },
        3068: {
            "pinyin": "duō duān guǎ yào",
            "meaning": "话题很多却抓不住要点，形容繁琐支离而不简要。",
            "example": "报告不要多端寡要，否则让人难以把握重点。"
        },
        3069: {
            "pinyin": "duō duō yì shàn",
            "meaning": "越多越好，多多益善。",
            "example": "有利于环保的措施多多益善。"
        },
        3070: {
            "pinyin": "duō gù zhī qiū",
            "meaning": "指国家多事多难的时期。",
            "example": "身处多故之秋，更需众志成城。"
        },
        3071: {
            "pinyin": "duō kǒu ā shī",
            "meaning": "多嘴好辩的老师傅，比喻爱插嘴、好评论的人。",
            "example": "他在旁边充当多口阿师，不时指指点点。"
        },
        3072: {
            "pinyin": "duō kuài hǎo shěng",
            "meaning": "又多又快、质量好又节省，原是生产建设的口号。",
            "example": "工程既要保质，又要争取多快好省地完成。"
        },
        3073: {
            "pinyin": "duō lì nián suǒ",
            "meaning": "经历的年月很多，形容资历深、经验多。",
            "example": "他多历年所，对行业变迁十分了解。"
        },
        3074: {
            "pinyin": "duō móu shàn duàn",
            "meaning": "善于筹划并能果断决断，形容有谋略又有决断力。",
            "example": "这位指挥官多谋善断，屡建奇功。"
        },
        3075: {
            "pinyin": "duō móu shàn lǜ",
            "meaning": "善于筹划思虑，形容考虑周到、谋划周密。",
            "example": "他处事多谋善虑，很少出差错。"
        },
        3076: {
            "pinyin": "duō nàn xīng bāng",
            "meaning": "多难可以使国家兴盛，指国家在磨难中奋发图强而振兴。",
            "example": "历史一再证明，多难兴邦并非空话。"
        },
        3077: {
            "pinyin": "duō qí wáng yáng",
            "meaning": "歧路太多以致迷失羊，比喻理论学说纷繁而无所适从。",
            "example": "面对众多方案，若无判断力，易成多歧亡羊之局。"
        },
        3078: {
            "pinyin": "duō qíng shàn gǎn",
            "meaning": "感情丰富、容易被触动。",
            "example": "他本性多情善感，总被小事牵动情绪。"
        },
        3079: {
            "pinyin": "duō rú niú máo",
            "meaning": "多得像牛身上的毛一样，形容数量极多。",
            "example": "类似的案例多如牛毛，足以证明问题的普遍性。"
        },
        3080: {
            "pinyin": "duō shì zhī qiū",
            "meaning": "多事之秋：事变频繁、局势不安定的时期。",
            "example": "在这多事之秋，更要保持冷静理智。"
        },
        3081: {
            "pinyin": "duō wén wéi fù",
            "meaning": "以学问丰富为财富，强调知识上的充实就是最大的富有。",
            "example": "书香世家向来以多文为富，不以金钱论成败。"
        },
        3082: {
            "pinyin": "duō xíng bù yì bì zì bì",
            "meaning": "作恶多端必将自取灭亡，出自古语“多行不义必自毙”。",
            "example": "这伙人作恶多年，终究印证了多行不义必自毙。"
        },
        3083: {
            "pinyin": "duō xǔ shǎo yǔ",
            "meaning": "许诺得多、兑现得少，形容口惠而实不至。",
            "example": "承诺不能多许少与，否则难以取信于人。"
        },
        3084: {
            "pinyin": "duō duō bī rén",
            "meaning": "形容说话或气势十分逼人，使人难以招架。",
            "example": "他质问起人来总是咄咄逼人，让人很不舒服。"
        },
        3085: {
            "pinyin": "duō duō guài shì",
            "meaning": "指令人惊奇的怪事或荒唐事。",
            "example": "这种操作简直是咄咄怪事，难以理解。"
        },
        3086: {
            "pinyin": "duō jiē biàn bàn",
            "meaning": "咄嗟：一呼一诺之间。形容事情办得非常迅速。",
            "example": "在各部门协同下，这项审批咄嗟便办。"
        },
        3087: {
            "pinyin": "duō jiē chì zhà",
            "meaning": "形容怒吼喝斥的声势，很有震慑力。",
            "example": "将军咄嗟叱咤，军中无人敢违抗军令。"
        },
        3088: {
            "pinyin": "duō jiē lì bàn",
            "meaning": "形容事情办得很快，当下就能完成。",
            "example": "这点小事，他咄嗟立办，不足挂齿。"
        },
        3089: {
            "pinyin": "duō jīng xié huá",
            "meaning": "掇：摘取；菁华：精华。比喻选取精华、去除糟粕。",
            "example": "编选教材要掇菁撷华，给学生最有价值的内容。"
        },
        3090: {
            "pinyin": "duō shí zhāng jù",
            "meaning": "拾取篇章句子，多指只在字句上用功而不求深入理解。",
            "example": "读书若只掇拾章句，难以真正融会贯通。"
        },
        3091: {
            "pinyin": "duō tún pěng pì",
            "meaning": "比喻阿谀奉承、竭力巴结权贵。",
            "example": "他靠掇臀捧屁上位，终究难得人心。"
        },
        3092: {
            "pinyin": "dù dé liàng lì",
            "meaning": "衡量自己的德行与能力，指做事要量力而行。",
            "example": "在接新项目之前，必须先度德量力。"
        },
        3093: {
            "pinyin": "dù jǐ yǐ shéng",
            "meaning": "以绳墨作标准来要求自己，比喻严于律己。",
            "example": "他一向度己以绳，从不徇私舞弊。"
        },
        3094: {
            "pinyin": "duó rén suǒ hào",
            "meaning": "夺取别人所喜爱的东西，多指强占他人所爱之物或爱好之人。",
            "example": "朋友之间不应夺人所好，更不能争风吃醋。"
        },
        3095: {
            "pinyin": "duó tāi huàn gǔ",
            "meaning": "本为佛家语，比喻在本质上进行改造，使之焕然一新。",
            "example": "这次制度改革可谓夺胎换骨，面貌一新。"
        },
        3096: {
            "pinyin": "duó mén ér chū",
            "meaning": "从门内夺路而出，形容仓促急迫地冲出困境。",
            "example": "火势突然变大，人们只得夺门而出。"
        },
        3097: {
            "pinyin": "duó qí tán jīng",
            "meaning": "多指喧宾夺主、抢了别人讲经说法的位置，比喻强行占据本不属于自己的地位。",
            "example": "晚辈发言虽好，却不可喧宾夺主，夺其谈经。"
        },
        3098: {
            "pinyin": "duǒ yí dà jiáo",
            "meaning": "朵颐：动腮颊；大嚼：大口吃东西。形容吃得又香又猛。",
            "example": "大家围坐一桌，对着美食朵颐大嚼。"
        },
        3099: {
            "pinyin": "duò yún wù zhōng",
            "meaning": "堕入云雾之中，比喻陷入迷惘、不明真相。",
            "example": "线索太杂，让人如堕云雾中，难以理清。"
        },
        3100: {
            "pinyin": "duò zèng bù gù",
            "meaning": "甑：蒸器。比喻贫困到连破甑都顾不上，或指遭逢重大变故顾不得小事。",
            "example": "局势危急之时，个人得失早已堕甑不顾。"
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

    print(f"已为 3001–3100 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
