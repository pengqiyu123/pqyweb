import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    enrich = {
        2901: {
            "pinyin": "dǒu fāng míng shì",
            "meaning": "斗方：一二尺见方的小幅诗文或书画。指好在斗方上题诗作画以自我标榜的所谓“名士”，多含讥讽之意。",
            "example": "这些所谓斗方名士，日日只顾题诗作画，实无真学问。"
        },
        2902: {
            "pinyin": "dǒu jiǔ bǎi piān",
            "meaning": "一斗美酒能作百篇诗，形容文学才思敏捷、诗兴极盛。",
            "example": "李白素有斗酒百篇之誉，才情令人叹服。"
        },
        2903: {
            "pinyin": "dǒu jiǔ xué shì",
            "meaning": "指喝着斗酒便能作诗的学士，形容文人的豪放与才情。",
            "example": "几位斗酒学士促膝长谈，诗酒唱和至深夜。"
        },
        2904: {
            "pinyin": "dǒu jiǔ zhī jī",
            "meaning": "一斗酒配一只鸡，形容简单而豪爽的宴饮，亦指家常便饭的款待。",
            "example": "老友远道而来，他只备了斗酒只鸡，却饱含真情。"
        },
        2905: {
            "pinyin": "dǒu nán yī rén",
            "meaning": "斗南：斗宿之南，指南方。泛指一地中才华或声望首屈一指的人。",
            "example": "他学问渊博，为本校公认的斗南一人。"
        },
        2906: {
            "pinyin": "dǒu shāo zhī qì",
            "meaning": "斗筲：容量很小的器具。比喻器量狭小或才识浅陋的人。",
            "example": "胸怀若只是斗筲之器，又怎能成大事业？"
        },
        2907: {
            "pinyin": "dǒu shēng zhī shuǐ",
            "meaning": "斗、升：小量的容积单位。比喻数量极少、极其有限。",
            "example": "靠那点斗升之水，很难浇灌整片庄稼。"
        },
        2908: {
            "pinyin": "dǒu sǔn hé fèng",
            "meaning": "榫卯严密相合，比喻衔接得十分紧密、严丝合缝。",
            "example": "这篇文章结构严谨，可谓斗榫合缝。"
        },
        2909: {
            "pinyin": "dǒu sù chǐ bù",
            "meaning": "一斗谷、一尺布，比喻很少的财物或报酬。",
            "example": "他不图斗粟尺布，只愿为村里做点实事。"
        },
        2910: {
            "pinyin": "dǒu zhuǎn shēn héng",
            "meaning": "北斗旋转、参星横陈，形容斗转星移、时序变换。",
            "example": "斗转参横，不觉又是一年过去了。"
        },
        2911: {
            "pinyin": "dǒu zhuǎn xīng yí",
            "meaning": "北斗星旋转、群星移动，比喻时间流逝或世事变迁。",
            "example": "斗转星移，故乡早已焕然一新。"
        },
        2912: {
            "pinyin": "dǒu sǒu jīng shén",
            "meaning": "抖起精神，形容振作精神、精神焕发。",
            "example": "休息片刻后，他又抖擞精神投入工作。"
        },
        2913: {
            "pinyin": "dǒu zhé shé xíng",
            "meaning": "像斗折一样曲折、像蛇行一样蜿蜒，形容道路或文字曲折盘旋。",
            "example": "山路斗折蛇行，行人步履维艰。"
        },
        2914: {
            "pinyin": "dòu ér zhù zhuī",
            "meaning": "临战才铸兵器，比喻事到临头才准备，行动不及时。",
            "example": "项目启动在即才想搭团队，未免有些斗而铸锥。"
        },
        2915: {
            "pinyin": "dòu jī zǒu gǒu",
            "meaning": "斗鸡赛狗，比喻沉溺于玩乐斗争的小把戏，不务正业。",
            "example": "他整日斗鸡走狗，把正事全都抛在脑后。"
        },
        2916: {
            "pinyin": "dòu zhì áng yáng",
            "meaning": "形容斗志高昂、士气旺盛。",
            "example": "队员们个个斗志昂扬，迎接决赛的到来。"
        },
        2917: {
            "pinyin": "dòu kòu nián huá",
            "meaning": "原指十三四岁的少女年纪，后也泛指青春年少的美好时光。",
            "example": "她正值豆蔻年华，前途一片光明。"
        },
        2918: {
            "pinyin": "dòu pōu guā fēn",
            "meaning": "像瓜被剖开、豆从荚中裂出，比喻国土等被分割瓜分。",
            "example": "旧中国曾一度遭受列强豆剖瓜分的屈辱。"
        },
        2919: {
            "pinyin": "dòu chóng yú míng",
            "meaning": "原指多吃豆子使人发胖、食榆实使人昏睡，后也用来形容习性难改或饮食不节。",
            "example": "他自知体胖，好似豆重榆瞑，却又难以节制。"
        },
        2920: {
            "pinyin": "dū tóu yì xìng",
            "meaning": "原为河北地方称呼，指“都头异姓”为极尊贵的称谓，后泛指尊贵显赫的人。",
            "example": "在那小城，他几乎被视作都头异姓般的人物。"
        },
        2921: {
            "pinyin": "dú shǒu zūn qián",
            "meaning": "原指在尊长面前施以毒手，后多泛指无情的打击或极其严厉的处置。",
            "example": "他对旧部下也毫不留情，真是毒手尊前。"
        },
        2922: {
            "pinyin": "dú shū dé jiàn",
            "meaning": "间：窍门。指读书能抓住要领，心领神会。",
            "example": "他读书得间，很快就掌握了这门学科的精髓。"
        },
        2923: {
            "pinyin": "dú shū sān dào",
            "meaning": "指读书要做到心到、眼到、口到，形容读书专心认真。",
            "example": "老师常提醒我们读书三到，这样记得才牢。"
        },
        2924: {
            "pinyin": "dú shū sān yú",
            "meaning": "余：空闲时间。指利用冬、夜、雨等一切空余时间读书学习。",
            "example": "他深信读书三余之法，再忙也抽空学习。"
        },
        2925: {
            "pinyin": "dú shū zhǒng zǐ",
            "meaning": "指能承续文脉、在文化上承前启后的读书人。",
            "example": "家族里读书种子不断，世代多出学者。"
        },
        2926: {
            "pinyin": "dú bà yī fāng",
            "meaning": "独自称霸一方，形容在某个地区或领域中势力独大。",
            "example": "这家企业一度独霸一方，几乎没有对手。"
        },
        2927: {
            "pinyin": "dú bù dāng shí",
            "meaning": "才能或声望在当时无人能及。",
            "example": "他书法成就独步当时，名满天下。"
        },
        2928: {
            "pinyin": "dú bù tiān xià",
            "meaning": "在天下范围内独一无二、无人可比。",
            "example": "这座工程的规模可谓独步天下。"
        },
        2929: {
            "pinyin": "dú bù yī shí",
            "meaning": "在一个时期内独一无二，形容才能或成就出众。",
            "example": "他的小说风格独步一时，引领潮流。"
        },
        2930: {
            "pinyin": "dú chū jī zhù",
            "meaning": "机杼：织布机。比喻文学创作有独到构思，不因袭前人。",
            "example": "这本书立意新颖，真有独出机杼之妙。"
        },
        2931: {
            "pinyin": "dú chū jǐ jiàn",
            "meaning": "提出与众不同的见解。",
            "example": "在会议上，他独出己见，提出了全新的方案。"
        },
        2932: {
            "pinyin": "dú chū xīn cái",
            "meaning": "形容构思精巧别致，自成一家。",
            "example": "这座建筑设计独出心裁，极具个性。"
        },
        2933: {
            "pinyin": "dú cǐ yī jiā, bié wú fēn diàn",
            "meaning": "原为商品广告语，后多用来形容事物独一无二，别处没有。",
            "example": "这种民俗表演在全国可谓独此一家，别无分店。"
        },
        2934: {
            "pinyin": "dú dāng yī miàn",
            "meaning": "能独自承担起一方面的工作或责任。",
            "example": "经过几年历练，他已经可以独当一面。"
        },
        2935: {
            "pinyin": "dú dào zhī chù",
            "meaning": "指事物或见解上独特的精妙之处。",
            "example": "这段论证颇有独到之处，令人耳目一新."
        },
        2936: {
            "pinyin": "dú dé zhī jiàn",
            "meaning": "独自领悟到的见解，多指独特而有价值的看法。",
            "example": "他在研究中形成了不少独得之见。"
        },
        2937: {
            "pinyin": "dú duàn dú xíng",
            "meaning": "事情全凭个人主观判断并付诸行动，不与他人商量。",
            "example": "重大决策若一味独断独行，难免出错。"
        },
        2938: {
            "pinyin": "dú duàn zhuān xíng",
            "meaning": "专擅作主，独自处理政务或事务，不听劝告。",
            "example": "他长期独断专行，最终失去了民心。"
        },
        2939: {
            "pinyin": "dú fū mín zéi",
            "meaning": "指残暴无道、祸害百姓的君主或统治者。",
            "example": "独夫民贼终究会被历史所唾弃。"
        },
        2940: {
            "pinyin": "dú hè jī qún",
            "meaning": "像鹤立在鸡群之中，形容人的仪表或才能非常出众。",
            "example": "他在人群中宛如独鹤鸡群，十分惹眼。"
        },
        2941: {
            "pinyin": "dú jiǎn chōu sī",
            "meaning": "像从单个蚕茧抽丝，形容条理清晰、层层展开，也可比喻单相思或独自从事繁琐工作。",
            "example": "这篇长文独茧抽丝，将复杂问题分析得井井有条。"
        },
        2942: {
            "pinyin": "dú jù jiàng xīn",
            "meaning": "具有他人难以企及的独特匠心或巧妙构思。",
            "example": "这件作品设计精巧，真可谓独具匠心。"
        },
        2943: {
            "pinyin": "dú jù zhī yǎn",
            "meaning": "具有独到的眼光和见解，目光敏锐。",
            "example": "投资需要独具只眼，善于发现潜力项目。"
        },
        2944: {
            "pinyin": "dú lǎn dà quán",
            "meaning": "把大权全部掌握在自己手中。",
            "example": "他在公司独揽大权，事事亲自作主。"
        },
        2945: {
            "pinyin": "dú lì zì zhǔ",
            "meaning": "独立自主地处理事务，不受外力控制。",
            "example": "一个国家要维护独立自主的外交政策。"
        },
        2946: {
            "pinyin": "dú mù bù chéng lín",
            "meaning": "一棵树成不了树林，比喻单靠个人力量成不了大事。",
            "example": "团队协作很重要，独木不成林。"
        },
        2947: {
            "pinyin": "dú mù nán zhī",
            "meaning": "一根木头难以支撑大厦，比喻单凭一人难以承担重任。",
            "example": "企业发展不能靠一个人，独木难支。"
        },
        2948: {
            "pinyin": "dú pì xī jìng",
            "meaning": "另辟一条小路，比喻开创不同凡响的新途径或新风格。",
            "example": "他在科研上独辟蹊径，取得了突破性成果。"
        },
        2949: {
            "pinyin": "dú qīng dú xǐng",
            "meaning": "自己清醒而他人糊涂，形容能在纷乱环境中保持清醒头脑。",
            "example": "身处喧嚣尘世，更要学会独清独醒。"
        },
        2950: {
            "pinyin": "dú shàn qí shēn",
            "meaning": "只顾自己行为端正，不管他人，亦指只求自保。",
            "example": "知识分子既要独善其身，也要兼济天下。"
        },
        2951: {
            "pinyin": "dú shì dú fēi",
            "meaning": "只认定自己的是对的、别人的是错的，形容偏执固执。",
            "example": "他待人处事总是独是独非，难以沟通。"
        },
        2952: {
            "pinyin": "dú shù yī zhì",
            "meaning": "比喻自成一格，树立起独特的旗帜或风格。",
            "example": "这位画家在山水画领域独树一帜。"
        },
        2953: {
            "pinyin": "dú wǎng dú lái",
            "meaning": "独自往来，不与他人结伴，也比喻来去自如、不受拘束。",
            "example": "他性格孤傲，向来独往独来。"
        },
        2954: {
            "pinyin": "dú xíng qí dào",
            "meaning": "只按照自己的道路行事，不顾他人看法。",
            "example": "即便遭到质疑，他仍独行其道。"
        },
        2955: {
            "pinyin": "dú xíng qí shì",
            "meaning": "只坚持自己认为对的做法，形容固执己见。",
            "example": "团队协作中若人人独行其是，事情很难做好。"
        },
        2956: {
            "pinyin": "dú xué guǎ wén",
            "meaning": "只靠自学而少与人交流，知识难免片面。",
            "example": "古人说独学寡闻，学习要多与他人切磋。"
        },
        2957: {
            "pinyin": "dú yī wú èr",
            "meaning": "唯一的，没有第二个，形容非常突出而独特。",
            "example": "这件文物在世上独一无二，极其珍贵。"
        },
        2958: {
            "pinyin": "dú yì yú rén",
            "meaning": "与众不同，有别于常人。",
            "example": "他的见解独异于人，经常出人意料。"
        },
        2959: {
            "pinyin": "dú yǒu qiān qiū",
            "meaning": "独具千秋之长处，形容事物自有其长久可贵的价值。",
            "example": "这部老电影虽画质一般，却独有千秋。"
        },
        2960: {
            "pinyin": "dú zhàn áo tóu",
            "meaning": "科举时代指考中第一名。今多比喻位居首位、成绩最好。",
            "example": "他在竞赛中独占鳌头，夺得冠军。"
        },
        2961: {
            "pinyin": "dú zuò chóu chéng",
            "meaning": "独自坐在愁城之中，形容深陷忧愁、郁郁寡欢。",
            "example": "夜深人静，他独坐愁城，思绪万千。"
        },
        2962: {
            "pinyin": "dǔ ér lùn zhī",
            "meaning": "笃：切实、确实。指切实地加以论述或认真地推论某事。",
            "example": "此事尚难笃而论之，还需进一步考证资料。"
        },
        2963: {
            "pinyin": "dǔ jìn jǔ yuǎn",
            "meaning": "笃：厚实、诚恳。对亲近者厚道，对疏远者也能举荐，形容一视同仁、公正待人。",
            "example": "为官者当笃近举远，不可偏私一隅。"
        },
        2964: {
            "pinyin": "dǔ shí hào xué",
            "meaning": "笃实：踏实、诚恳。形容待人诚恳、踏实肯干且好学不倦。",
            "example": "他为人笃实好学，很受老师器重。"
        },
        2965: {
            "pinyin": "dǔ xìn hào xué",
            "meaning": "笃信：忠实地信仰。指对道德和事业有坚定信念，并勤奋好学。",
            "example": "笃信好学，守死善道，是古人推崇的品格。"
        },
        2966: {
            "pinyin": "dǔ xué bù juàn",
            "meaning": "笃学：专心好学。形容专心学习、不知疲倦。",
            "example": "青年人应当笃学不倦，不负青春。"
        },
        2967: {
            "pinyin": "dǔ xué hào gǔ",
            "meaning": "专心致志地学习古代典籍和学问。",
            "example": "他自幼笃学好古，熟读经史子集。"
        },
        2968: {
            "pinyin": "dǔ jǐng shāng qíng",
            "meaning": "见到某种景物而触动内心，引发伤感。",
            "example": "重游旧地，难免睹景伤情。"
        },
        2969: {
            "pinyin": "dǔ wēi zhī zhù",
            "meaning": "从细微之处就能推知事物的显著变化，形容观察敏锐、善于推理。",
            "example": "优秀的管理者往往能睹微知著，及早调整策略。"
        },
        2970: {
            "pinyin": "dǔ wù sī rén",
            "meaning": "见到熟悉的物品而想起相关的人，多指触景生情。",
            "example": "看到那把旧雨伞，他不禁睹物思人。"
        },
        2971: {
            "pinyin": "dǔ wù xīng qíng",
            "meaning": "见到某种事物而引发情感波动。",
            "example": "春花烂漫，总叫人睹物兴情。"
        },
        2972: {
            "pinyin": "dù jiàn fáng méng",
            "meaning": "杜：堵住；渐、萌：事物的开端和萌芽。比喻在祸患刚萌生时就加以防止。",
            "example": "治乱之道，在于早早杜渐防萌。"
        },
        2973: {
            "pinyin": "dù jiàn fáng wēi",
            "meaning": "杜绝事物的开端，防备细微之处的祸患，比喻防患于未然。",
            "example": "对腐败问题必须杜渐防微，绝不姑息。"
        },
        2974: {
            "pinyin": "dù juān tí xuè",
            "meaning": "相传杜鹃鸟啼声悲切，啼到吐血染红花木，形容悲愤哀怨到了极点。",
            "example": "山中杜鹃啼血，更添几分凄凉。"
        },
        2975: {
            "pinyin": "dù jué hòu huàn",
            "meaning": "杜绝将来的祸患，指把隐患消除在未然。",
            "example": "完善制度，方能杜绝后患。"
        },
        2976: {
            "pinyin": "dù jué rén shì",
            "meaning": "人事：与人交往的事务。指断绝与外界社会交往，多用于仕途或交际场合。",
            "example": "他辞官回乡，几乎杜绝人事，专心著书。"
        },
        2977: {
            "pinyin": "dù jué yán lù",
            "meaning": "堵塞言路，使人不敢或不能发表意见。",
            "example": "若动辄打压不同意见，便是杜绝言路。"
        },
        2978: {
            "pinyin": "dù kǒu guǒ zú",
            "meaning": "捂住嘴、裹住脚，比喻言行受到严厉限制，不敢言、不敢动。",
            "example": "在高压之下，百姓只得杜口裹足。"
        },
        2979: {
            "pinyin": "dù kǒu tūn shēng",
            "meaning": "紧闭嘴巴，把要说的话咽回去，形容有苦难言或不敢出声。",
            "example": "受了委屈，他也只能杜口吞声。"
        },
        2980: {
            "pinyin": "dù mén huì jì",
            "meaning": "关上门、隐匿行迹，形容闭门隐居，不问世事。",
            "example": "他辞官后杜门晦迹，只与古书为伴。"
        },
        2981: {
            "pinyin": "dù mén jué jì",
            "meaning": "指隐居不出，与世隔绝。",
            "example": "战乱之时，他索性杜门绝迹，保全家人。"
        },
        2982: {
            "pinyin": "dù mén què sǎo",
            "meaning": "杜门：关门谢客；却扫：不再扫径迎宾。比喻闭门谢客，过隐居生活。",
            "example": "他厌倦应酬，决定杜门却扫，专心创作。"
        },
        2983: {
            "pinyin": "dù mén xiè kè",
            "meaning": "杜门：关门；谢客：辞谢来客。指闭门不见宾客。",
            "example": "他一心读书，索性杜门谢客。"
        },
        2984: {
            "pinyin": "dù mén zì jué",
            "meaning": "关门不出，主动断绝与外界往来。",
            "example": "自从那件事后，他几乎杜门自绝，不再见客。"
        },
        2985: {
            "pinyin": "dù mén zì shǒu",
            "meaning": "关起门来，安分守己，不再求仕或参与世事。",
            "example": "他辞官归里，只想杜门自守，过清静日子。"
        },
        2986: {
            "pinyin": "dù wēi shèn fáng",
            "meaning": "杜绝细微之患，谨慎防备萌芽中的祸害。",
            "example": "治理社会治安要杜微慎防，防止小案演变成大祸。"
        },
        2987: {
            "pinyin": "dù xì fáng wēi",
            "meaning": "杜绝裂隙，防备细微的祸患，形容防患于未然。",
            "example": "制度设计要周密，方能杜隙防微。"
        },
        2988: {
            "pinyin": "dù lǐ lèi xià",
            "meaning": "眼泪往肚里流，形容有苦说不出、内心极度委屈。",
            "example": "受尽指责的他只好肚里泪下，一声不吭。"
        },
        2989: {
            "pinyin": "dù guó hài mín",
            "meaning": "蠹：蛀虫，比喻侵蚀。形容行为严重损害国家利益，危害百姓。",
            "example": "这些贪官污吏简直是蠹国害民。"
        },
        2990: {
            "pinyin": "dù jū qí chǔ",
            "meaning": "像蛀虫藏在木中、棋子布满棋盘，比喻坏人深入社会、散布各处。",
            "example": "若不整肃吏治，蠹居棋处之弊将愈演愈烈。"
        },
        2991: {
            "pinyin": "dù zhòng mù zhé",
            "meaning": "蛀虫多了木头就会折断，比喻不利因素积累过多终致大祸。",
            "example": "这些小毛病若任其发展，恐有蠹众木折之虞。"
        },
        2992: {
            "pinyin": "dù zhuó pōu liáng zhù",
            "meaning": "虫蛀鸟啄足以毁坏梁柱，比喻微小的害处若不防范会酿成大祸。",
            "example": "管理若松懈，蠹啄剖梁柱也不足为奇。"
        },
        2993: {
            "pinyin": "dù néng hài xián",
            "meaning": "妒忌有才能的人并加以迫害。",
            "example": "用人之道重在识才爱才，切忌妒能害贤。"
        },
        2994: {
            "pinyin": "dù xián jí néng",
            "meaning": "妒忌贤德和有才能的人。",
            "example": "一个胸襟狭隘、妒贤嫉能的领导难以服众。"
        },
        2995: {
            "pinyin": "dù rì rú nián",
            "meaning": "形容日子过得极其难熬，像一年那么长。",
            "example": "在狭小牢房中，他真是度日如年。"
        },
        2996: {
            "pinyin": "dù wài zhī rén",
            "meaning": "度外：打算之外。指与某人或集团没有关系的外人、局外人。",
            "example": "他原本只是度外之人，却意外卷入这场纷争。"
        },
        2997: {
            "pinyin": "duān běn zhèng yuán",
            "meaning": "端正根本，澄清源头，比喻从根本上整顿、治理。",
            "example": "要解决腐败问题，必须端本正源，完善制度。"
        },
        2998: {
            "pinyin": "duān ní kě chá",
            "meaning": "端倪：线索、眉目。事情的头绪已经可以察觉。",
            "example": "案件经过细致排查，真相已是端倪可察。"
        },
        2999: {
            "pinyin": "duǎn bīng xiāng jiē",
            "meaning": "短兵：短兵器。指双方近距离展开肉搏战，也比喻直接激烈的交锋。",
            "example": "谈判桌上双方短兵相接，气氛十分紧张。"
        },
        3000: {
            "pinyin": "duǎn gěng jí shēn",
            "meaning": "绠：汲水的绳子。比喻能力薄弱，难以胜任艰巨任务，多用作谦辞。",
            "example": "此事重大，我恐短绠汲深，还望另择贤能。"
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

    print(f"已为 2901–3000 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
