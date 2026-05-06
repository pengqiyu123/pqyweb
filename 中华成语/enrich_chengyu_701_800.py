import json
from pathlib import Path


def main():
    base_dir = Path(__file__).parent
    json_path = base_dir / "chengyu_all_simple.json"

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # 为 701–800 条成语添加拼音、释义和例句
    enrich = {
        701: {
            "pinyin": "bì kēng luò jǐng",
            "meaning": "避开坑却掉进井里，比喻想躲开小祸却遇上大祸。",
            "example": "他换了工作，本想求稳，结果避坑落井，更不如从前。"
        },
        702: {
            "pinyin": "bì qí ruì qì, jī qí duò guī",
            "meaning": "避开敌人的锐气，攻击其疲惫回撤之时，是用兵的策略之一。",
            "example": "古人主张避其锐气，击其惰归，而不硬拼正面。"
        },
        703: {
            "pinyin": "bì ràng xián lù",
            "meaning": "主动让出出仕或升迁的道路给贤能之人。",
            "example": "他认为后辈更有才能，便避让贤路，甘作后援。"
        },
        704: {
            "pinyin": "bì shí jī xū",
            "meaning": "避开对方坚实之处，攻击其薄弱环节。",
            "example": "打比赛也要学会避实击虚，寻找对手弱点。"
        },
        705: {
            "pinyin": "bì shí jiù xū",
            "meaning": "避开实处，转而依托虚处，多指策略上从正面转为侧面。",
            "example": "谈判时他巧妙避实就虚，化解了难题。"
        },
        706: {
            "pinyin": "bì shì jué sú",
            "meaning": "躲避世俗而独居，不与世俗往来。",
            "example": "他性情淡泊，几乎要避世绝俗。"
        },
        707: {
            "pinyin": "bì xiōng qū jí",
            "meaning": "躲避凶险，追求吉利。",
            "example": "人们都希望趋利避害、避凶趋吉。"
        },
        708: {
            "pinyin": "bì zhòng jiù qīng",
            "meaning": "回避重要问题，只处理肤浅轻微的部分。",
            "example": "报告不能避重就轻，要直面矛盾。"
        },
        709: {
            "pinyin": "bì lěi sēn yán",
            "meaning": "防御工事密布而森严，比喻防守极为严密。",
            "example": "城池四周壁垒森严，难以攻破。"
        },
        710: {
            "pinyin": "bì lì qiān rèn",
            "meaning": "像墙壁一样笔直地耸立千仞高，形容山崖陡峭或气势雄伟。",
            "example": "江岸两旁山峰壁立千仞，景色壮观。"
        },
        711: {
            "pinyin": "biān cháng mò jí",
            "meaning": "鞭子太长，打不到马身，比喻力量虽大却达不到目的。",
            "example": "上级指示若落实不到基层，也就鞭长莫及。"
        },
        712: {
            "pinyin": "biān pì jìn lǐ",
            "meaning": "鞭策得深入细致，比喻分析问题透彻精到。",
            "example": "这篇评论对弊端的揭示可谓鞭辟近里。"
        },
        713: {
            "pinyin": "biān pì rù lǐ",
            "meaning": "词语来自佛经，指阐述精辟，深入事理。",
            "example": "他的演讲鞭辟入里，引人深思。"
        },
        714: {
            "pinyin": "biàn cái wú ài",
            "meaning": "辩论才能卓越，说话没有障碍。",
            "example": "她在法庭上辩才无碍，条理分明。"
        },
        715: {
            "pinyin": "biàn fēng wǔ rùn",
            "meaning": "风起而草木摇曳，雨下而滋润万物，比喻德政感化百姓。",
            "example": "新政推行如抃风舞润，百姓拍手称快。"
        },
        716: {
            "pinyin": "biàn běn jiā lì",
            "meaning": "比原来更加厉害，多指坏的方面加重。",
            "example": "若只罚不教，问题恐怕会变本加厉。"
        },
        717: {
            "pinyin": "biàn gǔ yì cháng",
            "meaning": "改变古制，变更常规，多指大刀阔斧的改革。",
            "example": "他主张变古易常，推动制度创新。"
        },
        718: {
            "pinyin": "biàn huà duō duān",
            "meaning": "变化多种多样。",
            "example": "市场行情变化多端，需要谨慎投资。"
        },
        719: {
            "pinyin": "biàn huà mò cè",
            "meaning": "变化多端，难以推测。",
            "example": "未来科技发展变化莫测。"
        },
        720: {
            "pinyin": "biàn huà wú cháng",
            "meaning": "事物变化不定，难以预料。",
            "example": "世事变化无常，要学会适应。"
        },
        721: {
            "pinyin": "biàn huà wú qióng",
            "meaning": "变化没有穷尽，形容变化非常多。",
            "example": "大自然的景色变化无穷。"
        },
        722: {
            "pinyin": "biàn huàn mò cè",
            "meaning": "变化多端，难以预测。",
            "example": "局势变幻莫测，让人难以下判断。"
        },
        723: {
            "pinyin": "biàn huàn wú cháng",
            "meaning": "情势经常变化，没有一定。",
            "example": "海上的天气变幻无常。"
        },
        724: {
            "pinyin": "biàn míng yì xìng",
            "meaning": "改变姓名，多为隐瞒身份之用。",
            "example": "他变名易姓，隐居乡间多年。"
        },
        725: {
            "pinyin": "biàn sè yì róng",
            "meaning": "改变脸色和容貌，比喻掩饰真相或乔装打扮。",
            "example": "间谍善于变色易容，难以识别。"
        },
        726: {
            "pinyin": "biàn sè zhī yán",
            "meaning": "说到某事就脸色大变的话，多指极其严厉的言辞。",
            "example": "在他那里，贪污二字是变色之言。"
        },
        727: {
            "pinyin": "biàn shēng bù cè",
            "meaning": "突然发生难以预料的变故。",
            "example": "若管理不善，随时可能变生不测。"
        },
        728: {
            "pinyin": "biàn shēng zhǒu yè",
            "meaning": "腋下忽生祸患，比喻近旁突然出现的危险。",
            "example": "内部矛盾若不处理，恐怕会变生肘腋。"
        },
        729: {
            "pinyin": "biàn wēi wéi ān",
            "meaning": "使危险转化为平安。",
            "example": "救援及时，总算变危为安。"
        },
        730: {
            "pinyin": "biàn dì kāi huā",
            "meaning": "到处都开花，比喻事业或活动蓬勃发展，遍地开张。",
            "example": "乡镇企业遍地开花，带动了当地经济。"
        },
        731: {
            "pinyin": "biàn tǐ lín shāng",
            "meaning": "全身像鱼鳞一样伤痕累累。",
            "example": "战士在战场上遍体鳞伤，却仍坚持战斗。"
        },
        732: {
            "pinyin": "biàn cí qiǎo shuō",
            "meaning": "花言巧语，善于辞令。",
            "example": "他惯用便辞巧说打动对方。"
        },
        733: {
            "pinyin": "biàn yí xíng shì",
            "meaning": "根据具体情况灵活处理事情。",
            "example": "下级可以在原则范围内便宜行事。"
        },
        734: {
            "pinyin": "biāo tóng fá yì",
            "meaning": "标举相同的，攻伐不同的，多指思想上不宽容。",
            "example": "学术界不宜标同伐异，应鼓励多元。"
        },
        735: {
            "pinyin": "biāo xīn lì yì",
            "meaning": "提出新奇的主张，力求与众不同。",
            "example": "设计要在实用基础上适度标新立异。"
        },
        736: {
            "pinyin": "biāo bǐng qiān gǔ",
            "meaning": "功绩或文采光耀千古。",
            "example": "他的业绩足以彪炳千古。"
        },
        737: {
            "pinyin": "biāo xíng dà hàn",
            "meaning": "身材高大魁梧的男子。",
            "example": "门口站着几个彪形大汉。"
        },
        738: {
            "pinyin": "biāo jǔ diàn zhì",
            "meaning": "像暴风举起、电光疾至，比喻行动迅猛。",
            "example": "大军飙举电至，迅速夺回要塞。"
        },
        739: {
            "pinyin": "biǎo lǐ rú yī",
            "meaning": "表面和内心完全一致，形容诚实无欺。",
            "example": "他为人表里如一，大家都信任他。"
        },
        740: {
            "pinyin": "biǎo lǐ shān hé",
            "meaning": "外有高山，内有大河，形容地势险要的国家或地区。",
            "example": "此地表里山河，易守难攻。"
        },
        741: {
            "pinyin": "biǎo lǐ shòu dí",
            "meaning": "内外同时受到敌人的进攻。",
            "example": "军队表里受敌，形势十分危急。"
        },
        742: {
            "pinyin": "biǎo lǐ wéi jiān",
            "meaning": "里外勾结一起做坏事。",
            "example": "贪官与不法商人表里为奸，侵吞公款。"
        },
        743: {
            "pinyin": "biǎo miàn wén zhāng",
            "meaning": "只在表面上做文章，比喻做给人看而无实质内容。",
            "example": "整改不能停留在表面文章上。"
        },
        744: {
            "pinyin": "biǎo zhuàng bù rú lǐ zhuàng",
            "meaning": "外表的强壮不如内里的坚实，强调内在更重要。",
            "example": "企业发展要重质不重量，表壮不如里壮。"
        },
        745: {
            "pinyin": "biāo méi zhī nián",
            "meaning": "摽落的梅子，比喻女子到了适婚年龄。",
            "example": "她已到摽梅之年，父母开始张罗婚事。"
        },
        746: {
            "pinyin": "bié chū jī zhù",
            "meaning": "在机杼上另出新意，比喻写作或创作有新意。",
            "example": "这部小说在结构上别出机杼。"
        },
        747: {
            "pinyin": "bié chū xīn cái",
            "meaning": "独创心意，另有匠心。",
            "example": "设计师在细节上别出心裁，令人耳目一新。"
        },
        748: {
            "pinyin": "bié fēng huái yǔ",
            "meaning": "南北风雨各不相同，比喻境遇或看法差异很大。",
            "example": "两地风俗别风淮雨，不可一概而论。"
        },
        749: {
            "pinyin": "bié hè gū luán",
            "meaning": "孤单的仙鹤和鸾鸟，比喻失去配偶的孤寡之人。",
            "example": "她守寡多年，如同别鹤孤鸾。"
        },
        750: {
            "pinyin": "bié jù fèi cháng",
            "meaning": "有别于一般人的情感或见识。",
            "example": "他对艺术的理解别具肺肠。"
        },
        751: {
            "pinyin": "bié jù jiàng xīn",
            "meaning": "另有独到的匠心和创造性。",
            "example": "这幅作品构思巧妙，别具匠心。"
        },
        752: {
            "pinyin": "bié jù yī gé",
            "meaning": "另有一种独特的格局和风格。",
            "example": "这家小店装潢别具一格，吸引了不少顾客。"
        },
        753: {
            "pinyin": "bié jù zhī yǎn",
            "meaning": "有独到的眼光和见解。",
            "example": "他对书画颇有研究，别具只眼。"
        },
        754: {
            "pinyin": "bié kāi shēng miàn",
            "meaning": "开创新的局面或风格。",
            "example": "这部影片在叙事上别开生面。"
        },
        755: {
            "pinyin": "bié lái wú yàng",
            "meaning": "分别以来一直平安无恙，多用于书信问候。",
            "example": "久未联系，但愿你别来无恙。"
        },
        756: {
            "pinyin": "bié shù yī zhì",
            "meaning": "另立旗帜，自成一派。",
            "example": "他在学界别树一帜，颇有影响。"
        },
        757: {
            "pinyin": "bié wú cháng wù",
            "meaning": "没有多余的东西，比喻家产贫乏或生活简朴。",
            "example": "他一身行囊，别无长物。"
        },
        758: {
            "pinyin": "bié yǒu dòng tiān",
            "meaning": "另有一片别致的天地，多形容景色或境界独特。",
            "example": "穿过石门，只见别有洞天。"
        },
        759: {
            "pinyin": "bié yǒu fēng qù",
            "meaning": "别具一番情趣和意味。",
            "example": "老街夜景别有风趣，令人流连。"
        },
        760: {
            "pinyin": "bié yǒu fēng wèi",
            "meaning": "有着不同寻常的滋味或特色。",
            "example": "这道家常菜做得别有风味。"
        },
        761: {
            "pinyin": "bié yǒu fèi cháng",
            "meaning": "另有一番心肠，多指用心良苦或别具见地。",
            "example": "他的话听似平常，实则别有肺肠。"
        },
        762: {
            "pinyin": "bié yǒu tiān dì",
            "meaning": "另有一片天地，比喻另有一番境界或成就。",
            "example": "在艺术领域，他闯出别有天地。"
        },
        763: {
            "pinyin": "bié yǒu yòng xīn",
            "meaning": "另存心思，常指存有某种企图。",
            "example": "他接近你似乎别有用心。"
        },
        764: {
            "pinyin": "bīn kè rú yún",
            "meaning": "宾客像云一样多，形容来客极多。",
            "example": "婚礼当天宾客如云，场面热闹非凡。"
        },
        765: {
            "pinyin": "bīn zhì rú guī",
            "meaning": "客人来到像回到自己家一样，形容主人殷勤好客。",
            "example": "这家旅店服务周到，让人宾至如归。"
        },
        766: {
            "pinyin": "bīn bīn yǒu lǐ",
            "meaning": "文雅有礼貌。",
            "example": "他待人彬彬有礼，深受欢迎。"
        },
        767: {
            "pinyin": "bìn luàn chāi héng",
            "meaning": "鬓发凌乱，簪钗歪斜，形容女子惊慌失措或打扮凌乱。",
            "example": "她匆忙赶来，鬓乱钗横。"
        },
        768: {
            "pinyin": "bīng dòng sān chǐ, fēi yī rì zhī hán",
            "meaning": "河冰冻三尺，并不是一天寒冷形成的，比喻事物的形成有个长期过程。",
            "example": "问题积累多年，所谓冰冻三尺，非一日之寒。"
        },
        769: {
            "pinyin": "bīng hán yú shuǐ",
            "meaning": "冰比水还冷，比喻学生青出于蓝胜于蓝。",
            "example": "后生可畏，正所谓冰寒于水。"
        },
        770: {
            "pinyin": "bīng hú qiū yuè",
            "meaning": "冰壶般晶莹，秋月般明净，比喻心地或品格清白高洁。",
            "example": "他为官一生，堪称冰壶秋月。"
        },
        771: {
            "pinyin": "bīng hún xuě pò",
            "meaning": "魂魄像冰雪一样洁白，比喻高洁的品格或忠贞的情怀。",
            "example": "烈士们冰魂雪魄，永垂不朽。"
        },
        772: {
            "pinyin": "bīng jī xuě cháng",
            "meaning": "肌肤如冰、心肠如雪，比喻性情冰清玉洁。",
            "example": "她为人冰肌雪肠，不染尘埃。"
        },
        773: {
            "pinyin": "bīng jī yù gǔ",
            "meaning": "肌肤如冰，骨骼如玉，比喻女子肌肤洁白细腻。",
            "example": "诗中描写的女子冰肌玉骨，美若天仙."
        },
        774: {
            "pinyin": "bīng jiě dòng shì",
            "meaning": "冰雪融化，比喻疑虑消除、矛盾化解。",
            "example": "经过坦诚沟通，双方冰解冻释。"
        },
        775: {
            "pinyin": "bīng qīng yù jié",
            "meaning": "品格像冰玉一样清洁，形容人高洁廉正。",
            "example": "他一生冰清玉洁，清正廉明。"
        },
        776: {
            "pinyin": "bīng qīng yù rùn",
            "meaning": "像冰一样清澈，像玉一样温润，形容品格高洁温和。",
            "example": "她气质淡雅，真是冰清玉润。"
        },
        777: {
            "pinyin": "bīng shān nán kào",
            "meaning": "冰山不能靠，比喻人冷漠难以接近。",
            "example": "他待人冷淡，被同事称作冰山难靠。"
        },
        778: {
            "pinyin": "bīng tàn bù tóng qì",
            "meaning": "冰与炭不能放在同一器皿，比喻两者性质完全相反，不能共存。",
            "example": "他们性格迥异，简直如冰炭不同器。"
        },
        779: {
            "pinyin": "bīng tàn bù tóu",
            "meaning": "冰和炭不能相投，比喻志趣迥异的人不能相合。",
            "example": "两人处事观念冰炭不投，很难共事。"
        },
        780: {
            "pinyin": "bīng tàn bù yán, lěng rè zì míng",
            "meaning": "冰炭不说话，人自知冷热，比喻事实胜于雄辩。",
            "example": "成绩如何，冰炭不言，冷热自明。"
        },
        781: {
            "pinyin": "bīng tiān xuě dì",
            "meaning": "冰天雪地，形容严寒的冬天或到处都是冰雪。",
            "example": "他们在冰天雪地里坚守岗位。"
        },
        782: {
            "pinyin": "bīng tiān xuě yáo",
            "meaning": "冰天雪窑，形容严寒异常的环境。",
            "example": "在那冰天雪窑的边境，战士们日夜巡逻。"
        },
        783: {
            "pinyin": "bīng xiāo wǎ jiě",
            "meaning": "冰消失、瓦破裂，比喻势力突然瓦解。",
            "example": "叛军在强大攻势下冰消瓦解。"
        },
        784: {
            "pinyin": "bīng xuě cōng míng",
            "meaning": "像冰雪一样晶莹剔透地聪明，形容人聪颖伶俐。",
            "example": "这孩子冰雪聪明，学什么都快。"
        },
        785: {
            "pinyin": "bīng bài rú shān dǎo",
            "meaning": "军队战败像山崩一样迅速溃散。",
            "example": "敌军兵败如山倒，丢盔弃甲而逃。"
        },
        786: {
            "pinyin": "bīng bù xuè rèn",
            "meaning": "用兵取得胜利而不见血，形容不战而屈人之兵。",
            "example": "若能和平解决争端，才是真正兵不血刃。"
        },
        787: {
            "pinyin": "bīng bù yàn zhà",
            "meaning": "用兵作战不厌弃施用计谋。",
            "example": "孙子云：兵不厌诈。"
        },
        788: {
            "pinyin": "bīng bù yóu jiāng",
            "meaning": "士兵不听将令，比喻下级不服从上级指挥。",
            "example": "军中最忌兵不由将。"
        },
        789: {
            "pinyin": "bīng chē zhī huì",
            "meaning": "战车聚集的大会，多指战争。",
            "example": "古代诸侯之间兵车之会频繁。"
        },
        790: {
            "pinyin": "bīng duō jiàng guǎng",
            "meaning": "兵士众多，将领也很多。",
            "example": "军中兵多将广，却缺乏统一指挥。"
        },
        791: {
            "pinyin": "bīng duō zhě bài",
            "meaning": "兵多未必取胜，反而容易失败。",
            "example": "若指挥不当，兵多者败。"
        },
        792: {
            "pinyin": "bīng guì shén sù",
            "meaning": "用兵贵在行动神速。",
            "example": "行军打仗，向来兵贵神速。"
        },
        793: {
            "pinyin": "bīng guì xiān shēng",
            "meaning": "用兵以先声夺人最为重要。",
            "example": "攻城略地，当兵贵先声。"
        },
        794: {
            "pinyin": "bīng huāng mǎ luàn",
            "meaning": "战乱频仍，局势混乱。",
            "example": "在兵荒马乱的年代，百姓流离失所。"
        },
        795: {
            "pinyin": "bīng lái jiàng dǎng, shuǐ lái tǔ yǎn",
            "meaning": "兵来就派将抵挡，水来就用土堵塞，比喻根据具体情况采取相应的措施。",
            "example": "工作中要兵来将挡，水来土掩。"
        },
        796: {
            "pinyin": "bīng lián huò jié",
            "meaning": "战祸连绵不绝。",
            "example": "那个时代兵连祸结，民不聊生。"
        },
        797: {
            "pinyin": "bīng lín chéng xià",
            "meaning": "军队逼近城下，比喻情势十分危急。",
            "example": "敌军兵临城下，守军严阵以待。"
        },
        798: {
            "pinyin": "bīng mǎ wèi dòng, liáng cǎo xiān xíng",
            "meaning": "军队尚未行动，粮草先运到，强调战前后勤准备的重要性。",
            "example": "做项目也要兵马未动，粮草先行。"
        },
        799: {
            "pinyin": "bīng qiáng mǎ zhuàng",
            "meaning": "军队强盛、兵马精良。",
            "example": "这支队伍兵强马壮，战斗力惊人。"
        },
        800: {
            "pinyin": "bīng róng xiāng jiàn",
            "meaning": "双方以武力相见，指用战争解决问题。",
            "example": "国家之间应以和平相处，避免兵戎相见。"
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

    print(f"已为 701–800 条成语更新详细信息，共更新 {updated} 条。")


if __name__ == "__main__":
    main()
