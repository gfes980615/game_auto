import lib.tool as tool
import time

skill_dict={
    'adele_skill_5_1': '7',     # 復原
    'adele_skill_5_2': 'b',     # 無限
    'adele_skill_5_3': 'home',  # 乙太風暴
    'adele_skill_back': 't',    # 回歸
    'adele_skill_bloom': 'a',   # 綻放
    'adele_skill_boost': 'n',   # 魔力爆裂
    'adele_skill_puncture': 'g',# 穿刺
    'adele_skill_trace': 's',   # 追蹤
    'warrior_buff_1': '5',      # 幻靈武具
}

skill_dict={
    'adele_skill_back': 't',    # 回歸
    'adele_skill_bloom': 'a',   # 綻放
    'adele_skill_trace': 's',   # 追蹤
    # 'adele_skill_puncture': 'g',# 穿刺
    'warrior_buff_1': '4',      # 幻靈武具
}

# skill_dict={
#     'adele_skill_back': 't',        # 回歸
#     'adele_skill_trace': 's',       # 追蹤
#     # 'adele_skill_deadMark': 'del'   # 死亡標記
# }


skill_chinese_dict={
    'adele_skill_5_1': '復原',
    'adele_skill_5_2': '無限',
    'adele_skill_5_3': '乙太風暴',
    'adele_skill_back': '回歸',
    'adele_skill_bloom': '綻放',
    'adele_skill_boost': '魔力爆裂',
    'adele_skill_puncture': '穿刺',
    'adele_skill_trace': '追蹤',
    'warrior_buff_1': '幻靈武具',
    'adele_skill_deadMark': '死亡標記',
}

while True:
    print('start skill')
    time.sleep(1)
    for skill in skill_dict:
        print('find '+ skill_chinese_dict.get(skill))
        if skill == 'adele_skill_trace':
            _, exist = tool.findImg('skill/' + skill)
            if exist == False:
                tool.pressKeyboard(skill_dict.get(skill))
        else:
            _, exist = tool.findImg('skill/' + skill)
            if exist:
                tool.pressKeyboard(skill_dict.get(skill))
            else:
                print('cd ...')
        time.sleep(0.5)

