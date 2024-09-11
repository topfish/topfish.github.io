"""
1. 把markdown文件转换成html文件
2. 通过index-temp.html模板生成index.html文件
"""

import os.path
import markdown


def turn_to_html(filename):
    # md转html
    text = ''
    with open("./markdown-type/"+filename, 'r', encoding='utf-8') as file:
        text = file.read()
    html = markdown.markdown(text)
    with open('./html-type/'+filename[:-3]+'.html', 'w', encoding='utf-8') as file:
        file.write(html)


def gent_html(filenames):
    text = ''
    with open('index-temp.html', 'r', encoding='utf-8') as file:
        text = file.read()
    start, end = 0, 0
    for i in range(len(text)):
        if text[i:i+6] == '<body>':
            start = i+7
        if text[i:i+7] == '</body>':
            end = i
            break
    body = text[start:end]
    # <p><a href="html-type/鬼谷子.html">鬼谷子</a></p>
    for filename in filenames:
        body += r'    <p><a href="html-type/' + filename[:-3] + r'.html">' + filename[:-3] + '</a></p>\n'
    # print("body:\n", body)
    text = text[:start] + body + text[end:]
    # print("text:\n", text)
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(text)


if __name__ == "__main__":
    filenames = os.listdir("./markdown-type")

    # md转html
    for filename in filenames:
        turn_to_html(filename)

    # 生成index.html
    gent_html(filenames)

