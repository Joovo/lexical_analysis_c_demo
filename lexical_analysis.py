import re
OP=('<','>','|','.','+','=','-','/','*','%','^','&','++','+=','-=','*=','/=','%=','&=','|=')
SEPARATOR=('#',';',',','(',')')
ID=('include','printf','return','h','main','studio')
KEY=('char','const','int','float','double','argv','argc')

print_list =[]
OP_list=[]
content_list=[]
NUM_list=[]
SEPARATOR_list=[]
KEY_list=[]
ID_list=[]
STRING_list=[]


def main():
    cflag = 0  # 控制多行注释
    oflag = 0
    op_first = ''
    fr = open('./test.cpp','r',encoding='utf-8')
    # 行号
    line_num = 0
    for line in fr.readlines():
        # 存放字符的列表
        each = [str(i) for i in line]
        # 分解每个字符
        word = ''
        for e in each:
            # 是操作符
            if oflag == 1:
                if e in ['=', '<', '>', '+', '-', '*', '/', '%', '|', '&']:
                    OP_list.append(op_first + e)
                    print_list.append('Line:' + str(line_num) + ' (' + op_first + e + ', OP)')
                    content_list.append(op_first + e)
                elif re.match(r'[a-zA-Z\_]', e):
                    word = word + e
                    OP_list.append(op_first)
                    print_list.append('Line:' + str(line_num) + ' (' + op_first + ', OP)')
                    content_list.append(op_first)
                oflag = 0
                continue
            # 是常数 NUM
            elif oflag == 2:
                if e==' ' or e in SEPARATOR:
                    try:
                        num=eval(word)
                    except:
                        word=''
                        oflag=0
                        continue
                if e == ' ':
                    NUM_list.append(word)
                    print_list.append('Line:' + str(line_num) + ' (' + word + ', NUM)')
                    content_list.append(word)
                    word = ''
                    oflag = 0
                elif e in SEPARATOR:
                    NUM_list.append(word)
                    print_list.append('Line:' + str(line_num) + ' (' + word + ', NUM)')
                    content_list.append(word)
                    SEPARATOR_list.append(e)
                    print_list.append('Line:' + str(line_num) + ' (' + e + ', SEPARATOR)')
                    content_list.append(e)
                    word = ''
                    oflag = 0
                else:
                    word = word + e
                continue
            # 是关键字或变量名
            elif oflag == 3:
                if e == ' ':
                    if word in KEY:
                        KEY_list.append(word)
                        print_list.append('Line:' + str(line_num) + ' (' + word + ', KEY)')
                        content_list.append(word)
                    elif word in ID:
                        ID_list.append(word)
                        print_list.append('Line:' + str(line_num) + ' (' + word + ', ID)')
                        content_list.append(word)
                    word = ''
                    oflag = 0
                elif e in SEPARATOR:
                    if word in KEY:
                        KEY_list.append(word)
                        print_list.append('Line:' + str(line_num) + ' (' + word + ', KEY)')
                        content_list.append(word)
                    elif word in ID:
                        ID_list.append(word)
                        print_list.append('Line:' + str(line_num) + ' (' + word + ', ID)')
                        content_list.append(word)
                    SEPARATOR_list.append(e)
                    print_list.append('Line:' + str(line_num) + ' (' + e + ', SEPARATOR)')
                    content_list.append(e)
                    word = ''
                    oflag = 0
                else:
                    word = word + e
                continue
            # 是字符串 STRING
            elif oflag == 4:
                if e != '"':
                    word = word + e
                elif e == '"':
                    word = word + e
                    STRING_list.append(word)
                    print_list.append('Line:' + str(line_num) + ' (' + word + ', STRING)')
                    content_list.append(word)
                    word = ''
                    oflag = 0
                continue

            # 判断是否是操作符（OP）
            if e in OP:
                oflag = 1
                op_first = e
                continue
            # 判断是否是分隔符（SEPARATOR）
            if e in SEPARATOR:
                SEPARATOR_list.append(e)
                print_list.append('Line:' + str(line_num) + ' (' + e + ', SEPARATOR)')
                content_list.append(e)
                continue
            # 判断是否是常数 NUM
            if re.match(r'[0-9]', e):
                oflag = 2
                word = word + e
                continue
            # 判断是否是关键字或变量名
            if re.match(r'[a-zA-Z\_]', e):
                oflag = 3
                word = word + e
                continue
            # 判断是否是字符串
            if e == '"':
                oflag = 4
                word = word + e
                continue

if __name__ == '__main__':
    main()
    for i in print_list:
        print(i)
