import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 为 1101–1200 条成语添加拼音、释义和例句
    enrich = {
        # TODO: 填充 1101–1200 号成语的详细信息
        1101: {
            "pinyin": "bù rù hǔ xué, yān dé hǔ zǐ",
            "meaning": "不进入老虎洞里，怎能捉到老虎崽，比喻不冒风险就难有大成就。",
            "example": "创业难免有风险，不入虎穴，焉得虎子。"
        },
        1102: {
            "pinyin": "bù rù shí yí",
            "meaning": "不符合当时的风尚或需要，显得过时或不合时宜。",
            "example": "这种老式管理办法早已不入时宜，需要改革。"
        },
        1103: {
            "pinyin": "bù sāi xià liú, bù zhǐ bù xíng",
            "meaning": "不堵住下游的水流就不能停止，比喻要从根源上治理祸患。",
            "example": "整治污染必须从源头入手，不塞下流，不止不行。"
        },
        1104: {
            "pinyin": "bù sān bù sì",
            "meaning": "不像三、不像四，比喻举止行为不正派，或样子怪异。",
            "example": "他整天游手好闲，打扮得不三不四。"
        },
        1105: {
            "pinyin": "bù shān bù lǚ",
            "meaning": "既不穿长衫，又不穿鞋，多形容衣着随便、不拘小节。",
            "example": "他平时在家总是不衫不履，一副随意的样子。"
        },
        1106: {
            "pinyin": "bù shǎng zhī gōng",
            "meaning": "没有得到赏赐的功劳，多指未被承认的贡献。",
            "example": "项目成功背后也有许多不赏之功。"
        },
        1107: {
            "pinyin": "bù shàng bù xià",
            "meaning": "不上也不下，比喻处境尴尬，进退两难。",
            "example": "职位空缺迟迟不定，让他感到不上不下。"
        },
        1108: {
            "pinyin": "bù shě zhòu yè",
            "meaning": "日夜不停，形容时间或事物持续不断地运转。",
            "example": "江河不舍昼夜地向前奔流。"
        },
        1109: {
            "pinyin": "bù shèn liǎo liǎo",
            "meaning": "了解得不太清楚。",
            "example": "他对这件事的来龙去脉不甚了了。"
        },
        1110: {
            "pinyin": "bù shēng bù miè",
            "meaning": "既不生也不灭，多用在佛家语境中，表示超脱生死的永恒状态。",
            "example": "佛家认为真如本性不生不灭。"
        },
        1111: {
            "pinyin": "bù shèng bēi sháo",
            "meaning": "酒量不大，喝不了多少杯，比喻酒兴浓烈。",
            "example": "好友相聚，不觉不胜杯杓，各自多饮了几杯。"
        },
        1112: {
            "pinyin": "bù shèng méi jǔ",
            "meaning": "多得数不过来。",
            "example": "城市里的高楼大厦不胜枚举。"
        },
        1113: {
            "pinyin": "bù shèng qí fán",
            "meaning": "烦琐到难以承受，形容事情太多、太琐碎。",
            "example": "这份手续实在繁杂，让人不胜其烦。"
        },
        1114: {
            "pinyin": "bù shèng qí rèn",
            "meaning": "能力不足以承担其责任。",
            "example": "这项重任非他莫属，别人恐怕不胜其任。"
        },
        1115: {
            "pinyin": "bù shī guī cuò",
            "meaning": "连极小的部分也不失去，比喻十分准确周全。",
            "example": "他引经据典，不失圭撮，令人信服。"
        },
        1116: {
            "pinyin": "bù shī háo lí",
            "meaning": "连一丝一毫都不差。",
            "example": "按照图纸施工，尺寸不失毫厘。"
        },
        1117: {
            "pinyin": "bù shī shí jī",
            "meaning": "不会错过有利的时机。",
            "example": "成功者善于把握机会，从不失时机。"
        },
        1118: {
            "pinyin": "bù shí bù zhī",
            "meaning": "既不识又不知，比喻非常愚昧。",
            "example": "若对历史一无所知，难免显得不识不知。"
        },
        1119: {
            "pinyin": "bù shí dà tǐ",
            "meaning": "不懂得顾全大局，只计较小事。",
            "example": "做领导必须通盘考虑，不能不识大体。"
        },
        1120: {
            "pinyin": "bù shí gāo dī",
            "meaning": "不懂得分辨事情的轻重或人的高低优劣。",
            "example": "他对长辈无礼，实在是不识高低。"
        },
        1121: {
            "pinyin": "bù shí shí wù",
            "meaning": "不懂得适应时代形势和局势的发展。",
            "example": "一味固守成规，难免被说成不识时务。"
        },
        1122: {
            "pinyin": "bù shí tái jǔ",
            "meaning": "不明白别人的好意或提携之意。",
            "example": "别人一番善意劝告，他却以为多事，真是不识抬举。"
        },
        1123: {
            "pinyin": "bù shí tài shān",
            "meaning": "不了解对方的身份或本领很大，比喻眼光浅陋。",
            "example": "他对那位老教授颐指气使，可谓是不识泰山。"
        },
        1124: {
            "pinyin": "bù shí yī dīng",
            "meaning": "连一个字都不认识，形容人极其文盲。",
            "example": "他幼年家贫，不识一丁，只能靠口头记账。"
        },
        1125: {
            "pinyin": "bù shí zhī wú",
            "meaning": "形容极其无知，没有一点见识。",
            "example": "若连基本常识都不懂，只能说是不识之无。"
        },
        1126: {
            "pinyin": "bù shí zhī xū",
            "meaning": "不是经常需要而是偶尔才用到的东西或准备。",
            "example": "家中备一些常用药，以备不时之需。"
        },
        1127: {
            "pinyin": "bù shí mǎ gān",
            "meaning": "不吃马肝，比喻明知有害的事坚决不做。",
            "example": "高利贷如同毒药，理应不食马肝，远而避之。"
        },
        1128: {
            "pinyin": "bù shí zhōu sù",
            "meaning": "不吃周朝的粮食，比喻不愿依附当权者，保持节操。",
            "example": "他清高自守，如同不食周粟的隐士。"
        },
        1129: {
            "pinyin": "bù shí zhī dì",
            "meaning": "连生计都难以维持的地方，比喻极贫瘠的地区。",
            "example": "那时此地荒芜贫瘠，几乎是不食之地。"
        },
        1130: {
            "pinyin": "bù shì zhī gōng",
            "meaning": "非常罕见、超出一世的伟大功业。",
            "example": "创立这一制度可谓不世之功。"
        },
        1131: {
            "pinyin": "bù sǐ bù huó",
            "meaning": "既没死也不好好活着，形容状态很差或境况尴尬。",
            "example": "这家公司经营不善，处于不死不活的状态。"
        },
        1132: {
            "pinyin": "bù sù zhī kè",
            "meaning": "没被预先邀请而突然来到的客人。",
            "example": "这位不速之客的出现让大家颇为意外。"
        },
        1133: {
            "pinyin": "bù tiǎn zhī yí",
            "meaning": "自谦礼物薄陋，不够丰厚。",
            "example": "区区薄礼，聊表心意，不腆之仪，还望笑纳。"
        },
        1134: {
            "pinyin": "bù tiāo zhī zǔ",
            "meaning": "宗庙中永远不得迁移牌位的始祖，指地位极高的祖先。",
            "example": "他被后世尊为不祧之祖，世代享祀。"
        },
        1135: {
            "pinyin": "bù tōng shuǐ huǒ",
            "meaning": "连水火都不相通，比喻毫无来往或互不相容。",
            "example": "两家长期反目，不通水火。"
        },
        1136: {
            "pinyin": "bù tóng fán xiǎng",
            "meaning": "跟平常的声音不同，形容事物出众、气度不凡。",
            "example": "这首新作气势恢宏，真是不同凡响。"
        },
        1137: {
            "pinyin": "bù tóng liú sú",
            "meaning": "不随波逐流于世俗，形容品格高洁或有独立见解。",
            "example": "他为人正直，不同流俗，坚持原则。"
        },
        1138: {
            "pinyin": "bù tòng bù yǎng",
            "meaning": "既不疼也不痒，比喻说话或做事起不到实际作用。",
            "example": "光搞表面文章，不痛不痒，难以解决问题。"
        },
        1139: {
            "pinyin": "bù tǔ bù rú",
            "meaning": "既咽不下去也吐不出来，比喻对坏人坏事既不能容忍又难以处理。",
            "example": "对这样的同事，他真是觉得不吐不茹。"
        },
        1140: {
            "pinyin": "bù wàng gōu hè",
            "meaning": "不忘记身处沟壑中的贫贱之人。",
            "example": "他发迹之后仍不忘沟壑，常回乡探望乡亲。"
        },
        1141: {
            "pinyin": "bù wàng gù jiù",
            "meaning": "不忘记老朋友和旧日交情。",
            "example": "他虽贵为高官，却始终不忘故旧。"
        },
        1142: {
            "pinyin": "bù wéi nóng shí",
            "meaning": "不违背农事节令，顺应农时。",
            "example": "古代明君讲究不违农时，让百姓安心耕作。"
        },
        1143: {
            "pinyin": "bù wéi yǐ shèn",
            "meaning": "对别人不做得太过分，适可而止。",
            "example": "批评要有分寸，不为已甚。"
        },
        1144: {
            "pinyin": "bù wéi wǔ dǒu mǐ zhé yāo",
            "meaning": "不肯为五斗米折腰，比喻不为小利屈节。",
            "example": "他宁可辞职，也不为五斗米折腰。"
        },
        1145: {
            "pinyin": "bù wén bù wèn",
            "meaning": "既不听也不问，形容对事情极端漠不关心。",
            "example": "对孩子的成长父母若不闻不问，是不负责任的。"
        },
        1146: {
            "pinyin": "bù wén bù wǔ",
            "meaning": "既谈不上文雅也谈不上勇武，形容才能平庸。",
            "example": "他既不擅长文，也不善武，真有些不文不武。"
        },
        1147: {
            "pinyin": "bù wèn qīng hóng zào bái",
            "meaning": "不分是非，不问缘由就加以责备或处理。",
            "example": "处理问题不能不问青红皂白，一味粗暴。"
        },
        1148: {
            "pinyin": "bù wú xiǎo bǔ",
            "meaning": "还是有一点小小的补益。",
            "example": "虽然只是建议，但对改进工作不无小补。"
        },
        1149: {
            "pinyin": "bù wǔ zhī hè",
            "meaning": "不像会跳舞的鹤，比喻徒有其表而无真才实学的人。",
            "example": "他看似气宇轩昂，其实是不舞之鹤。"
        },
        1150: {
            "pinyin": "bù wù kōng míng",
            "meaning": "不追求虚有其表的名声。",
            "example": "他踏实做事，不务空名。"
        },
        1151: {
            "pinyin": "bù wù zhèng yè",
            "meaning": "不从事正当职业，形容人整日游手好闲。",
            "example": "他整天上网打游戏，简直是不务正业。"
        },
        1152: {
            "pinyin": "bù xī gōng běn",
            "meaning": "不吝惜工时和成本。",
            "example": "为了提高产品质量，企业不惜工本升级设备。"
        },
        1153: {
            "pinyin": "bù xiāng shàng xià",
            "meaning": "高低难分，水平相当。",
            "example": "两支队伍实力不相上下，比赛十分精彩。"
        },
        1154: {
            "pinyin": "bù xiāng wéi móu",
            "meaning": "彼此志趣或立场不同，不会共同谋划。",
            "example": "在原则问题上，他们向来不相为谋。"
        },
        1155: {
            "pinyin": "bù xiāng wén wèn",
            "meaning": "互相之间没有音信往来。",
            "example": "自从搬家以后，两家几乎不相闻问。"
        },
        1156: {
            "pinyin": "bù xiáng zhī zhào",
            "meaning": "预示将要出现不吉利事情的征兆。",
            "example": "接连发生事故，被看作是不祥之兆。"
        },
        1157: {
            "pinyin": "bù xiào zǐ sūn",
            "meaning": "不孝顺的后代。",
            "example": "他挥霍祖业，被亲戚们骂作不肖子孙。"
        },
        1158: {
            "pinyin": "bù xiè yī gù",
            "meaning": "认为不值得正眼看一下，形容极端轻视。",
            "example": "对于那些无聊的流言，他一向不屑一顾。"
        },
        1159: {
            "pinyin": "bù xǐng rén shì",
            "meaning": "昏迷不醒，失去知觉。",
            "example": "他高烧不退，昏迷不省人事。"
        },
        1160: {
            "pinyin": "bù xiū biān fú",
            "meaning": "不修饰衣着外表，比喻不注意外形而重内容。",
            "example": "他为人朴实，不修边幅，却深受学生爱戴。"
        },
        1161: {
            "pinyin": "bù xú bù jí",
            "meaning": "不快不慢，形容做事从容稳重。",
            "example": "他讲话不徐不疾，却十分有力。"
        },
        1162: {
            "pinyin": "bù xù rén yán",
            "meaning": "不在乎他人的议论和非议。",
            "example": "只要问心无愧，就不必过分在意流言，不恤人言。"
        },
        1163: {
            "pinyin": "bù xué wú shù",
            "meaning": "自己不肯学习，却又没有本领。",
            "example": "不肯下功夫，只会抱怨，是不学无术的表现。"
        },
        1164: {
            "pinyin": "bù xùn sī qíng",
            "meaning": "不徇私情，秉公办事。",
            "example": "他一向刚直，不徇私情。"
        },
        1165: {
            "pinyin": "bù yán ér xìn",
            "meaning": "不用多说，别人就信任，形容为人诚实可靠。",
            "example": "他做人厚道，不言而信。"
        },
        1166: {
            "pinyin": "bù yán ér yù",
            "meaning": "不用解释就可以明白，多指道理显而易见。",
            "example": "这次改革的意义不言而喻。"
        },
        1167: {
            "pinyin": "bù yàn qí fán",
            "meaning": "不嫌麻烦，一次次耐心去做。",
            "example": "老师不厌其烦地给我们讲解难题。"
        },
        1168: {
            "pinyin": "bù yàn qí xiáng",
            "meaning": "不嫌细致繁琐，把情况讲得很清楚。",
            "example": "说明书写得不厌其详，便于初学者理解。"
        },
        1169: {
            "pinyin": "bù yī bù ráo",
            "meaning": "紧追不放，步步逼迫。",
            "example": "他对对方的失误穷追猛打，不依不饶。"
        },
        1170: {
            "pinyin": "bù yī ér zú",
            "meaning": "不只一种，足够多种，形容情况或方式很多。",
            "example": "类似的例子不一而足，此处不再赘述。"
        },
        1171: {
            "pinyin": "bù yí bù huì",
            "meaning": "既不刚愎自用，也不优柔寡断，形容持中而和。",
            "example": "他处事不夷不惠，能权衡利弊。"
        },
        1172: {
            "pinyin": "bù yí yú lì",
            "meaning": "不遗留一分力气，形容竭尽全力。",
            "example": "为了完成任务，大家不遗余力地加班。"
        },
        1173: {
            "pinyin": "bù yǐ guī jǔ, bù néng chéng fāng yuán",
            "meaning": "没有规矩就不能成方圆，比喻做事要有制度和准则。",
            "example": "管理要靠制度，不以规矩，不能成方圆。"
        },
        1174: {
            "pinyin": "bù yǐ rén fèi yán",
            "meaning": "不因对人的好恶而抛弃他所说的有道理的话。",
            "example": "领导要做到不以人废言，善于听取不同意见。"
        },
        1175: {
            "pinyin": "bù yǐ wéi chǐ",
            "meaning": "不把某事看作可耻，反觉心安理得。",
            "example": "他对自己的失信行为竟不以为耻，令人叹息。"
        },
        1176: {
            "pinyin": "bù yǐ wéi qí",
            "meaning": "不认为奇怪或值得惊讶。",
            "example": "如今远程办公已很普遍，人们对此早不以为奇。"
        },
        1177: {
            "pinyin": "bù yǐ wéi rán",
            "meaning": "不认为是对的，表示不同意某种看法。",
            "example": "对此结论，他颇不以为然。"
        },
        1178: {
            "pinyin": "bù yǐ wéi yì",
            "meaning": "不放在心上，不加在意。",
            "example": "别人对他的闲言碎语，他向来不以为意。"
        },
        1179: {
            "pinyin": "bù yǐ yī shěng yǎn dà dé",
            "meaning": "不会因为一时的小过失而抹杀一个人的大功德。",
            "example": "对于有功之人，不能不以一眚掩大德。"
        },
        1180: {
            "pinyin": "bù yì lè hū",
            "meaning": "不是很快乐吗？常用作感叹句，表示乐趣无穷。",
            "example": "与三五知己畅谈古今，不亦乐乎。"
        },
        1181: {
            "pinyin": "bù yì ér fēi",
            "meaning": "东西没有长翅膀却飞走了，比喻东西突然丢失。",
            "example": "钱包不翼而飞，让他懊恼不已。"
        },
        1182: {
            "pinyin": "bù yì yī zì",
            "meaning": "一个字都不能改，形容文章十分精当。",
            "example": "这篇檄文措辞严谨，不易一字。"
        },
        1183: {
            "pinyin": "bù yì zhī diǎn",
            "meaning": "不能随意改变的典章制度。",
            "example": "这些规定早已成为不易之典。"
        },
        1184: {
            "pinyin": "bù yì zhī lùn",
            "meaning": "不容轻易改变的正确论断。",
            "example": "勤奋是成功的重要条件，这几乎是不易之论。"
        },
        1185: {
            "pinyin": "bù yì zhī cái",
            "meaning": "来路不正的钱财。",
            "example": "君子爱财，取之有道，绝不贪不义之财。"
        },
        1186: {
            "pinyin": "bù yīn bù yáng",
            "meaning": "态度怪异，忽冷忽热，让人难以捉摸。",
            "example": "他说话总是不阴不阳，让人不舒服。"
        },
        1187: {
            "pinyin": "bù yīn rén rè",
            "meaning": "不因别人的热情而改变自己的冷淡态度。",
            "example": "他生性淡漠，不因人热，也不刻意逢迎。"
        },
        1188: {
            "pinyin": "bù yǐn dào quán",
            "meaning": "不喝盗来的泉水，比喻坚守节操，不取不义之利。",
            "example": "他宁可口渴，也不饮盗泉之水。"
        },
        1189: {
            "pinyin": "bù yóu fēn shuō",
            "meaning": "不容分辩，形容态度强硬。",
            "example": "他不由分说就把责任推给别人。"
        },
        1190: {
            "pinyin": "bù yóu zì zhǔ",
            "meaning": "由不得自己做主，形容身不由己。",
            "example": "身处乱局，他往往不由自主地被卷入。"
        },
        1191: {
            "pinyin": "bù yú zhī yù",
            "meaning": "没有预料到的赞誉。",
            "example": "作品一经发表，即获好评，这番不虞之誉让他颇感意外。"
        },
        1192: {
            "pinyin": "bù yuǎn qiān lǐ",
            "meaning": "不嫌路远而赶来，多形容对某人或某事极重视。",
            "example": "他不远千里前来道谢。"
        },
        1193: {
            "pinyin": "bù yuǎn wàn lǐ",
            "meaning": "与“ 不远千里 ”相似，形容不辞路途遥远而赶来。",
            "example": "朋友不远万里来访，他十分感动。"
        },
        1194: {
            "pinyin": "bù yuē ér tóng",
            "meaning": "事先没有约定却意见或行动一致。",
            "example": "大家对这个方案不约而同地点头赞成。"
        },
        1195: {
            "pinyin": "bù zài huà xià",
            "meaning": "用不着说都可以明白，形容事情显而易见。",
            "example": "他在团队中的重要性已是不在话下。"
        },
        1196: {
            "pinyin": "bù zài qí wèi, bù móu qí zhèng",
            "meaning": "不在这个职位上就不过问这方面的政务。",
            "example": "古人讲究不在其位，不谋其政。"
        },
        1197: {
            "pinyin": "bù zàn yī cí",
            "meaning": "一句称赞的话也没有，多指沉默不语。",
            "example": "他听完发言后不赞一词，只是若有所思。"
        },
        1198: {
            "pinyin": "bù zé shǒu duàn",
            "meaning": "不选择手段，为达到目的什么办法都用。",
            "example": "为了牟利，他不择手段，甚至违法乱纪。"
        },
        1199: {
            "pinyin": "bù zhé bù kòu",
            "meaning": "毫不打折扣，形容执行命令或完成任务非常彻底。",
            "example": "这项政策要不折不扣地落实到位。"
        },
        1200: {
            "pinyin": "bù zhèng zhī fēng",
            "meaning": "不正派的社会风气。",
            "example": "必须下大力气纠治不正之风。"
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

    print(f"已为 1101–1200 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
