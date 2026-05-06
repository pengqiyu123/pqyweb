import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 将 3901–4000 号成语的详细信息补充到 enrich 字典中
    enrich = {
        3901: {
            "pinyin": "fū chàng fù suí",
            "meaning": "丈夫领唱、妻子附和，比喻夫妻感情融洽、步调一致，也用来形容相互配合默契。",
            "example": "他们多年以来夫唱妇随，把小店经营得有声有色。"
        },
        3902: {
            "pinyin": "fū qī fǎn mù",
            "meaning": "夫妻之间反目成仇，形容家庭失和、感情破裂。",
            "example": "本是一段佳话，如今却闹到夫妻反目的地步。"
        },
        3903: {
            "pinyin": "fū rén qún dài",
            "meaning": "指凭借妻室、亲属的关系得到提拔或好处，比喻裙带关系。",
            "example": "用夫人裙带来谋取官职，终究难以服众。"
        },
        3904: {
            "pinyin": "fū róng qī guì",
            "meaning": "丈夫显贵、妻子也随之尊贵，形容夫妻因一方得志而共享荣华。",
            "example": "他仕途顺利，父母安享晚年，真可谓夫荣妻贵。"
        },
        3905: {
            "pinyin": "fū zǐ zì dào",
            "meaning": "出自《论语》，原指孔子阐述自己的主张，后来也指本人与人谈论自己的见解或经历。",
            "example": "文章多是夫子自道，记录了他的亲身体验。"
        },
        3906: {
            "pinyin": "fū pí liáo cǎo",
            "meaning": "形容做事只停留在表面，草率敷衍，不下功夫。",
            "example": "这份报告写得肤皮潦草，缺乏扎实的数据支持。"
        },
        3907: {
            "pinyin": "fū shòu zhī sù",
            "meaning": "亲身经历者的控诉或申诉，具有直接体验的意味。",
            "example": "这些回忆录可看作是战争幸存者的肤受之诉。"
        },
        3908: {
            "pinyin": "fū shòu zhī yán",
            "meaning": "亲身经历者说出的话，比喻根据亲身体验而发的议论。",
            "example": "他对行业乱象的批评，确是多年打拼后的肤受之言。"
        },
        3909: {
            "pinyin": "fū yǎn liǎo shì",
            "meaning": "做事不负责任，只求表面上应付过去。",
            "example": "既然答应了群众，就不能敷衍了事。"
        },
        3910: {
            "pinyin": "fū yǎn sè zé",
            "meaning": "工作敷衍、塞责了事，只求不出差错，不求尽职尽责。",
            "example": "他对待审核工作一向敷衍塞责，难免出纰漏。"
        },
        3911: {
            "pinyin": "fú diān chí wéi",
            "meaning": "扶住倾颠、支撑危局，比喻在危急时刻出手相助、稳定局势。",
            "example": "多亏老领导扶颠持危，企业才渡过难关。"
        },
        3912: {
            "pinyin": "fú lǎo xié yòu",
            "meaning": "搀扶着老人、携带着幼儿，形容一家老小同行的情景，也用来形容照顾周全。",
            "example": "节假日景区里扶老携幼的游客随处可见。"
        },
        3913: {
            "pinyin": "fú qiáng mō bì",
            "meaning": "扶着墙、摸着壁前行，比喻在黑暗或困难中摸索前进。",
            "example": "创业初期，他们只能扶墙摸壁，一点点摸索经验。"
        },
        3914: {
            "pinyin": "fú qīng jì ruò",
            "meaning": "扶持倾危，救济弱小，形容仗义行善、扶危助困。",
            "example": "历代仁人志士都主张扶倾济弱、匡扶正义。"
        },
        3915: {
            "pinyin": "fú ruò yì qiáng",
            "meaning": "扶助弱小、抑制强暴，形容主持公道、维护正义。",
            "example": "法律的宗旨之一，就是扶弱抑强，保护弱势群体。"
        },
        3916: {
            "pinyin": "fú wéi dìng luàn",
            "meaning": "在危乱之时加以扶持、平定乱局。",
            "example": "这支部队多次在关键时刻扶危定乱。"
        },
        3917: {
            "pinyin": "fú wéi jì kùn",
            "meaning": "在危难中救济困苦的人，形容乐于解危救困。",
            "example": "慈善组织长期致力于扶危济困。"
        },
        3918: {
            "pinyin": "fú yáo wàn lǐ",
            "meaning": "乘着旋风飞腾万里，比喻前程远大或地位、声望迅速提高。",
            "example": "他立志扶摇万里，报效家国。"
        },
        3919: {
            "pinyin": "fú yáo zhí shàng",
            "meaning": "好像乘着旋风直上云霄，比喻地位、名声迅速上升。",
            "example": "这几年公司发展扶摇直上，成为行业龙头。"
        },
        3920: {
            "pinyin": "fú bù chóng zhì, huò bì zhòng lái",
            "meaning": "福分不会一再降临，灾祸却常接踵而至，用来劝人不可贪福忘忧。",
            "example": "古人常说福不重至，祸必重来，提醒人要居安思危。"
        },
        3921: {
            "pinyin": "fú dì dòng tiān",
            "meaning": "传说中神仙居住的洞府仙境，后多比喻景色优美、环境幽静的好地方。",
            "example": "这座古镇山清水秀，简直是一处福地洞天。"
        },
        3922: {
            "pinyin": "fú guò zāi shēng",
            "meaning": "福气太过反而招致灾祸，比喻乐极生悲或得意忘形招来不幸。",
            "example": "行事若太张扬，小心得了福过灾生。"
        },
        3923: {
            "pinyin": "fú huì shuāng xiū",
            "meaning": "同时修持福报和智慧，多用于佛教语境，也用来形容德行与才智并重的修养。",
            "example": "他一生行善读书，可谓福慧双修。"
        },
        3924: {
            "pinyin": "fú lù shuāng quán",
            "meaning": "既有福气又得俸禄，形容福分和官运都很好。",
            "example": "身居要职又家庭和美，真是福禄双全。"
        },
        3925: {
            "pinyin": "fú rú dōng hǎi",
            "meaning": "祝颂他人福气像东海那样深广无边，多与“寿比南山”连用。",
            "example": "祝您福如东海、寿比南山。"
        },
        3926: {
            "pinyin": "fú shàn huò yín",
            "meaning": "上天降福给善人，降祸给淫邪之徒，体现因果报应的观念。",
            "example": "古语云福善祸淫，人终究难逃因果。"
        },
        3927: {
            "pinyin": "fú shòu mián mián",
            "meaning": "福气和寿命绵延不绝，常用作对长辈的祝颂之词。",
            "example": "老人家福寿绵绵，儿孙满堂。"
        },
        3928: {
            "pinyin": "fú shòu qí tiān",
            "meaning": "福禄与寿命高齐苍天，形容福寿极其隆盛。",
            "example": "祝二老福寿齐天，安享晚年。"
        },
        3929: {
            "pinyin": "fú shòu wú jiāng",
            "meaning": "福气和寿命没有边际，形容长寿而多福。",
            "example": "乡亲们都来为寿星贺喜，祝他福寿无疆。"
        },
        3930: {
            "pinyin": "fú wú shuāng zhì",
            "meaning": "福运很少连续到来，比喻好事难以一再遇见。",
            "example": "别指望总有意外之财，毕竟福无双至。"
        },
        3931: {
            "pinyin": "fú xī huò suǒ fú, huò xī fú suǒ yǐ",
            "meaning": "出自《老子》，意为福中藏祸、祸中伏福，说明祸福相依、难以绝对分割。",
            "example": "历史一再证明，福兮祸所伏，祸兮福所倚。"
        },
        3932: {
            "pinyin": "fú yǐ huò fú",
            "meaning": "福分依附在祸患之上，祸患潜藏在福分之中，强调祸福互相依存。",
            "example": "看问题不能只图眼前利益，当知福倚祸伏之理。"
        },
        3933: {
            "pinyin": "fú zhì xīn líng",
            "meaning": "福气来到时心思变得格外灵巧，比喻人在机缘到来时会突然想到好办法。",
            "example": "关键时刻他灵机一动，真是福至心灵。"
        },
        3934: {
            "pinyin": "fú bái zài bǐ",
            "meaning": "一边举杯饮酒，一边执笔作文，形容文人饮酒赋诗、兴致盎然的样子。",
            "example": "宴席上众人浮白载笔，诗兴大作。"
        },
        3935: {
            "pinyin": "fú guā chén lǐ",
            "meaning": "把瓜浮在水面、李子沉在水中以消暑，比喻夏日清凉的饮食享受。",
            "example": "童年记忆里，总少不了浮瓜沉李的清凉时光。"
        },
        3936: {
            "pinyin": "fú guāng lüè yǐng",
            "meaning": "水面上掠过的光影，比喻印象肤浅、观察不细致，或事物短暂易逝。",
            "example": "对这座城市，他不过浮光掠影地看了一圈。"
        },
        3937: {
            "pinyin": "fú huā làng ruǐ",
            "meaning": "浮艳的花朵、浪漫的花蕊，比喻外表华丽而内容空洞的事物。",
            "example": "这种作品浮花浪蕊，缺乏真正的思想力量。"
        },
        3938: {
            "pinyin": "fú jiā fàn zhái",
            "meaning": "家像浮在水面、宅随波漂流，比喻以船为家、到处飘泊的生活。",
            "example": "渔民们浮家泛宅，逐水草而居。"
        },
        3939: {
            "pinyin": "fú míng bó lì",
            "meaning": "虚浮的名声和微薄的利益，多用来表示不看重名利。",
            "example": "在他眼里，浮名薄利远不如心中志业重要。"
        },
        3940: {
            "pinyin": "fú míng xū yù",
            "meaning": "不切实际的虚名和称誉，形容没有真正实力却被过分吹捧。",
            "example": "这些奖项多半是浮名虚誉，不足为凭。"
        },
        3941: {
            "pinyin": "fú pí liáo cǎo",
            "meaning": "与“肤皮潦草”同，指工作粗枝大叶，只做表面文章。",
            "example": "工程验收不能浮皮潦草，安全问题容不得半点马虎。"
        },
        3942: {
            "pinyin": "fú shēng ruò mèng",
            "meaning": "人生像浮游一样短暂，如梦般虚幻，常用来感叹人生无常。",
            "example": "繁华散尽，只觉浮生若梦。"
        },
        3943: {
            "pinyin": "fú shēng qiē xiǎng",
            "meaning": "声音飘忽却又清晰入耳，多形容乐声悠扬、回响不绝。",
            "example": "琴音在厅堂中浮声切响，令人陶醉。"
        },
        3944: {
            "pinyin": "fú wén qiǎo yǔ",
            "meaning": "浮华的文辞和巧妙的言语，比喻徒有其表、华而不实的文章或言论。",
            "example": "治理国家不能只靠浮文巧语。"
        },
        3945: {
            "pinyin": "fú xiǎng lián piān",
            "meaning": "纷飞不止的联想接连不断，形容思绪万千、想象丰富。",
            "example": "看着老照片，他不禁浮想联翩。"
        },
        3946: {
            "pinyin": "fú yī dà bái",
            "meaning": "古人斟满大杯白酒敬人，比喻痛快畅饮或以酒行礼。",
            "example": "多年未见，老友一来便要与他浮一大白。"
        },
        3947: {
            "pinyin": "fú yǔ xū cí",
            "meaning": "空洞浮夸的言语和辞藻，形容言不由衷、缺乏实质。",
            "example": "会议发言要务实，切忌浮语虚辞。"
        },
        3948: {
            "pinyin": "fú yún bì rì",
            "meaning": "浮云遮蔽太阳，比喻小人一时得势，掩盖贤才或正道。",
            "example": "历史告诉我们，浮云蔽日终难长久。"
        },
        3949: {
            "pinyin": "fú yún zhāo lù",
            "meaning": "浮云和晨露都很短暂，比喻荣华富贵转瞬即逝。",
            "example": "他早看淡浮云朝露般的功名。"
        },
        3950: {
            "pinyin": "fú yún fù guì",
            "meaning": "把富贵看得像浮云一样轻淡，形容不把名利放在心上。",
            "example": "在真正的志士眼中，浮云富贵不值一提。"
        },
        3951: {
            "pinyin": "fú zōng làng jì",
            "meaning": "行踪像浪花一样飘忽不定，形容到处漂泊、居无定所。",
            "example": "多年来他浮踪浪迹，足迹遍布各地。"
        },
        3952: {
            "pinyin": "fú gǔ xiāng yìng",
            "meaning": "敲击木鼓，声音互相应和，比喻彼此呼应、反响热烈。",
            "example": "这番倡议一出，群情激昂，如桴鼓相应。"
        },
        3953: {
            "pinyin": "fú dī zuò xiǎo",
            "meaning": "低头哈腰、自贬身价地讨好别人，形容过分谦卑或卑躬屈膝。",
            "example": "为求升迁，他处处伏低做小。"
        },
        3954: {
            "pinyin": "fú dì shèng rén",
            "meaning": "形容对人毕恭毕敬、几乎要伏地膜拜，也带讽刺意味。",
            "example": "他对上司阿谀逢迎，简直像见了伏地圣人。"
        },
        3955: {
            "pinyin": "fú ér huái tiān",
            "meaning": "趴在地上对着天空吠叫，比喻地位卑微却好高骛远地妄加指责。",
            "example": "只会伏而咶天，却不踏实做事，自然得不到尊重。"
        },
        3956: {
            "pinyin": "fú fǎ shòu zhū",
            "meaning": "伏罪于法律之下而受到诛杀，指罪犯依法被处决。",
            "example": "凶手最终伏法受诛，还了受害者一个公道。"
        },
        3957: {
            "pinyin": "fú hǔ xiáng lóng",
            "meaning": "能制服猛虎、降伏蛟龙，比喻本领高强，能战胜强大对手或困难。",
            "example": "这位老将素有伏虎降龙之名。"
        },
        3958: {
            "pinyin": "fú lóng fèng chú",
            "meaning": "卧伏的龙和幼小的凤凰，比喻潜藏不露的奇才。",
            "example": "刘备曾言得一伏龙凤雏，便可安天下。"
        },
        3959: {
            "pinyin": "fú jìng hè xī",
            "meaning": "鸭腿短、鹤膝长，比喻勉强增减本不相称的事物，适得其反。",
            "example": "方案被硬行修改，结果凫胫鹤膝，更加不伦不类。"
        },
        3960: {
            "pinyin": "fú qū què yuè",
            "meaning": "像水鸟快步、雀鸟跳跃那样欢腾，形容高兴得又蹦又跳。",
            "example": "孩子们听到要去春游，一个个凫趋雀跃。"
        },
        3961: {
            "pinyin": "fú dī zuò xiǎo",
            "meaning": "同“伏低做小”，形容过分谦卑、低声下气地讨好别人。",
            "example": "为了拉订单，他处处服低做小。"
        },
        3962: {
            "pinyin": "fú tián lì sè",
            "meaning": "从事耕田、努力种植庄稼，形容勤劳务农。",
            "example": "乡亲们服田力穑，一年到头不敢懈怠。"
        },
        3963: {
            "pinyin": "fú róng bìng dì",
            "meaning": "两朵荷花同生一蒂，比喻夫妻恩爱或兄弟情深。",
            "example": "新婚洞房里张挂着芙蓉并蒂的图画。"
        },
        3964: {
            "pinyin": "fú róng chū shuǐ",
            "meaning": "荷花出水，形容女子姿容清丽脱俗。",
            "example": "她一身素衣，宛如芙蓉出水。"
        },
        3965: {
            "pinyin": "fú rán bù yuè",
            "meaning": "神色怏怏、不高兴，形容略带愠色的样子。",
            "example": "听到批评，他有些怫然不悦。"
        },
        3966: {
            "pinyin": "fú rán zuò sè",
            "meaning": "面露怒色，形容因生气而变脸。",
            "example": "话音未落，他已怫然作色。"
        },
        3967: {
            "pinyin": "fú xiù ér guī",
            "meaning": "甩袖而回，多指因愤懑而拂袖离去。",
            "example": "他拂袖而归，再也不愿参与这场争论。"
        },
        3968: {
            "pinyin": "fú xiù ér qù",
            "meaning": "甩袖子就走，形容愤然离去的样子。",
            "example": "对方态度傲慢，他只得拂袖而去。"
        },
        3969: {
            "pinyin": "fǔ yuè tāng huò",
            "meaning": "斧钺、滚汤、油锅等酷刑的总称，比喻极其残酷的刑罚。",
            "example": "古代法度严苛，稍有不慎便有斧钺汤镬之祸。"
        },
        3970: {
            "pinyin": "fǔ yuè zhī zhū",
            "meaning": "以斧钺等重刑处死，指最严厉的惩罚。",
            "example": "叛国大罪理当受斧钺之诛。"
        },
        3971: {
            "pinyin": "fǔ shí dì jiè",
            "meaning": "像俯身拾取地上的芥菜那样容易，比喻取用极为容易。",
            "example": "在信息时代，获取资料几如俯拾地芥。"
        },
        3972: {
            "pinyin": "fǔ shí jí shì",
            "meaning": "一俯身就能拾到，比喻到处都是、极其常见。",
            "example": "这类例子在生活中俯拾即是。"
        },
        3973: {
            "pinyin": "fǔ shí jiē shì",
            "meaning": "低头捡拾，处处可得，比喻多得不胜枚举。",
            "example": "优秀的创新案例在这座城市俯拾皆是。"
        },
        3974: {
            "pinyin": "fǔ shí yǎng qǔ",
            "meaning": "低头可拾、抬头可取，比喻容易得到。",
            "example": "当年人才辈出，英雄俯拾仰取。"
        },
        3975: {
            "pinyin": "fǔ shǒu jiù fù",
            "meaning": "低头就任人捆绑，比喻束手就擒、听任处置。",
            "example": "面对铁证，他终于俯首就缚。"
        },
        3976: {
            "pinyin": "fǔ shǒu tiē ěr",
            "meaning": "低着头、贴着耳朵倾听，形容十分驯服听话。",
            "example": "在强权面前，他只会俯首帖耳。"
        },
        3977: {
            "pinyin": "fǔ shǒu tīng mìng",
            "meaning": "低头听从命令，形容完全服从、没有主见。",
            "example": "做事不能一味俯首听命，也要坚持原则。"
        },
        3978: {
            "pinyin": "fǔ yǎng wéi wéi",
            "meaning": "低头抬头之间连声唯唯，形容恭顺怯懦、唯唯诺诺的样子。",
            "example": "他在上司面前俯仰唯唯，从不敢提出异议。"
        },
        3979: {
            "pinyin": "fǔ yǎng wú kuì",
            "meaning": "低头抬头都无愧于心，形容行为光明磊落。",
            "example": "只要问心无愧，便可俯仰无愧。"
        },
        3980: {
            "pinyin": "fǔ yǎng yóu rén",
            "meaning": "一举一动都受制于人，比喻处境被动、不得自由。",
            "example": "缺乏核心技术，只能在市场上俯仰由人。"
        },
        3981: {
            "pinyin": "fǔ yǎng zhī jiān",
            "meaning": "在低头抬头之间，比喻时间极短。",
            "example": "巨变往往发生在俯仰之间。"
        },
        3982: {
            "pinyin": "fǔ bèi è hóu",
            "meaning": "一手拍背、一手掐喉，形容控制别人要害，使之无法反抗。",
            "example": "关键资源被少数人拊背扼喉地掌控。"
        },
        3983: {
            "pinyin": "fǔ gōng zì wèn",
            "meaning": "低头审视自身，反复自我反省。",
            "example": "每逢决策失误，他都会抚躬自问。"
        },
        3984: {
            "pinyin": "fǔ jīn zhuī xī",
            "meaning": "由眼前事物联想到往昔，形容借今事追忆往事。",
            "example": "在古城漫步，难免抚今追昔。"
        },
        3985: {
            "pinyin": "fǔ jǐng shāng qíng",
            "meaning": "因眼前景物而触动伤感情绪。",
            "example": "他在故乡旧宅前抚景伤情，久久不语。"
        },
        3986: {
            "pinyin": "fǔ suí wàn fāng",
            "meaning": "安抚天下四方百姓，形容广泛抚慰、使民心安定。",
            "example": "新政实施之后，有助于抚绥万方。"
        },
        3987: {
            "pinyin": "fǔ xīn zì wèn",
            "meaning": "用手按着胸口自我询问，表示反省良心。",
            "example": "抚心自问，他并无亏欠。"
        },
        3988: {
            "pinyin": "fǔ zhǎng dà xiào",
            "meaning": "拍着手大笑，形容极为开心、畅快的笑声。",
            "example": "听完笑话，大家抚掌大笑。"
        },
        3989: {
            "pinyin": "fǔ dǐ chōu xīn",
            "meaning": "从锅底抽出柴火，比喻从根本上解决问题或切断根源。",
            "example": "要治理污染，必须釜底抽薪，改革粗放发展模式。"
        },
        3990: {
            "pinyin": "fǔ dǐ yóu yú",
            "meaning": "锅底有鱼游动，比喻处境极其危险却浑然不觉。",
            "example": "在金融泡沫中盲目加杠杆，无异于釜底游鱼。"
        },
        3991: {
            "pinyin": "fǔ zhōng shēng yú",
            "meaning": "锅里竟然长出鱼来，比喻家中清贫到连煮饭都难，或形容环境极其困窘。",
            "example": "他少年时家贫如洗，几近釜中生鱼的地步。"
        },
        3992: {
            "pinyin": "fǔ zhōng yóu yú",
            "meaning": "锅里的水中有鱼游动，比喻危在旦夕却尚未觉察的处境。",
            "example": "若不及时改革，企业恐成釜中游鱼。"
        },
        3993: {
            "pinyin": "fǔ chē chún chǐ",
            "meaning": "辅车与唇齿一样互相依存，比喻关系极为密切、兴亡与共。",
            "example": "两国地缘相接，如辅车唇齿，休戚相关。"
        },
        3994: {
            "pinyin": "fǔ chē xiāng yī",
            "meaning": "辅骨与牙齿彼此依附，比喻关系密切、互相依存。",
            "example": "区域内城市发展辅车相依，离不开协同合作。"
        },
        3995: {
            "pinyin": "fǔ shì cháng mín",
            "meaning": "辅佐世道、使百姓长久受益，形容有志于济世安民。",
            "example": "他立志从政，以期辅世长民。"
        },
        3996: {
            "pinyin": "fǔ guǐ bù chì",
            "meaning": "盛放祭品的簠簋器皿都整理不好，比喻礼制废弛、朝政不修。",
            "example": "史书批评某朝簠簋不饬，纲纪松弛。"
        },
        3997: {
            "pinyin": "fù fěn hé láng",
            "meaning": "给俊美男子傅脂抹粉，比喻男子姿容俊秀。",
            "example": "他相貌堂堂，真有几分傅粉何郎的风姿。"
        },
        3998: {
            "pinyin": "fù fěn shī zhū",
            "meaning": "敷粉涂朱，形容浓妆艳抹。",
            "example": "她并不喜欢傅粉施朱，更偏爱素面朝天。"
        },
        3999: {
            "pinyin": "fù zhī bǐng dīng",
            "meaning": "交付给火焰焚烧，比喻彻底毁灭或弃之不顾。",
            "example": "战乱中无数典籍被付之丙丁。"
        },
        4000: {
            "pinyin": "fù zhī dōng liú",
            "meaning": "任凭东流之水冲走，比喻希望、成果等白白付诸东流。",
            "example": "若不抓住机遇，多年努力恐将付之东流。"
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

    print(f"已为 3901–4000 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
