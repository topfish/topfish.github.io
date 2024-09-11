"""
道德经.md文件加标题级数
易因.md文件处理
"""

def daodejing():
    with open('./markdown-type/道德经.md', 'r', encoding='utf-8') as file:
        text = file.read()

    for n in range(81):
        for i in range(len(text)):
            if text[i:i+2] == "章第" and text[i-4] != r"#":
                text = text[:i-2]+r'### '+text[i-2:]
                break

    with open('./markdown-type/道德经.md', 'w', encoding='utf-8') as file:
        file.write(text)


def yiyin():
    with open('./markdown-type/易因.md', 'r', encoding='utf-8') as file:
        text = file.read()

    zhus = ['附录', '《文言》', '《象》', '《彖2》', '《彖》']
    for i in range(len(text)):
        for zhu in zhus:
            if text[i:i+len(zhu)] == zhu and text[i-2] != '-':
                text = text[:i] + '- ' + text[i:]

    cutis = ['初九：', '九二：', '九三：', '九四：', '九五：', '上九：', '用九：', '初六：', '六二：', '六三：', '六四：', '六五：', '上六：', '用六：']
    for i in range(len(text)):
        for cuti in cutis:
            if text[i:i+len(cuti)] == cuti and text[i-2:i] != '**':
                text = text[:i] + '**' + text[i:i+len(cuti)-1] + "**" + text[i+len(cuti)-1:]

    with open('./markdown-type/易因.md', 'w', encoding='utf-8') as file:
        file.write(text)


if __name__ == "__main__":
    # daodejing()
    yiyin()
