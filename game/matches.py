# coding: utf-8

add = {
    '0':   [8],
    '1':   [7],
    '2':   [],
    '3':   [9],
    '4':   [],
    '5':   [9, 6],
    '6':   [8],
    '7':   [],
    '8':   [],
    '9':   [0],
    '+':   [],
    '-':   ['+']
}

minus ={
    '0':   [],
    '1':   [],
    '2':   [],
    '3':   [],
    '4':   [],
    '5':   [],
    '6':   [5],
    '7':   [1],
    '8':   [0, 6],
    '9':   [3, 5],
    '+':   ['-'],
    '-':   []
}

change = {
    '0':   [6, 9],
    '1':   [],
    '2':   [3],
    '3':   [2, 5],
    '4':   [],
    '5':   [3],
    '6':   [0, 9],
    '7':   [],
    '8':   [],
    '9':   [0, 6],
    '+':   [],
    '-':   []
}


def get_equality():
    number_list = []
    symbol_list = []
    # eval_str = raw_input('Give me your equality: ')
    # user_input = list(str(eval_str))
    # eval_str = user_input = '6-2+1=8'
    # eval_str = user_input = '1+2=4'
    # eval_str = user_input = '4-1=2'
    # eval_str = user_input = '3-9=6'
    eval_str = user_input = '9-2=5'
    try:
        for i in user_input[::2]:
            number_list.append(str(int(i)))

        symbol = user_input[1::2]
        if symbol[-1] != '=':
            raise NameError
        for i in list(symbol[0:-1]):
            if i not in ['+', '-']:
                raise NameError
        for i in list(symbol[0:-1]):
            symbol_list.append(i)
    except:
        print 'wrong format equality'
        return 1

    return number_list, symbol_list, list(user_input)


def list_to_str(l):
    x = ''
    for i in l:
        x += str(i)
    return x


def assert_equality():
    try:
        number_input, symbol_input, input_list_input = get_equality()
    except:
        return 1

    number_org = number_input[:]
    symbol_org = symbol_input[:]
    input_list_org = input_list_input[:]

    equality = ''
    for i in range(0, len(number_org)):
        if i < len(number_org) - 2:
            equality += number_org[i]
            equality += symbol_org[i]
        elif i == len(number_org) - 2:
            equality += number_org[i]

    if eval(equality) == int(number_org[-1]):
        print 'no need to change'
        return 1

    # print equality,     number_org,           symbol_org,         input_list_org
    #       6-2+1      ['6', '2', '1', '8']     ['-', '+']      ['6', '-', '2', '+', '1', '=', '8']

    # assert change before =
    number = number_org[:]
    input_list = input_list_org[:]

    for i in range(0, len(number)-1):
        if change[number[i]]:  # 6:[0,9]
            for j in range(0, len(change[number[i]])):
                input_list[2*i] = str(change[number[i]][j])
                if eval(list_to_str(input_list[0:len(input_list)-2])) == int(input_list[-1]):
                    print "change {} to {}".format(equality[2*i], input_list[2*i])
                    print list_to_str(input_list[0:len(input_list)-2]) + '=' + str(input_list[-1])
                    number = number_org[:]
                    input_list = input_list_org[:]

    number_org = number_input[:]
    symbol_org = symbol_input[:]
    input_list_org = input_list_input[:]
    input_list = input_list_input[:]

    # assert change after =
    if change[number[-1]]:
        for i in range(0, len(change[number[-1]])):
            input_list[-1] = str(change[number[-1]][i])
            if eval(list_to_str(input_list[0:len(input_list)-2])) == int(input_list[-1]):
                print "change {} to {}".format(input_list_org[-1], change[number[-1]][i])
                print list_to_str(input_list[0:len(input_list) - 2]) + '=' + str(input_list[-1])

    number_org = number_input[:]
    symbol_org = symbol_input[:]
    input_list_org = input_list_input[:]

    # assert add and minus
    # print equality,   number_org,        symbol_org,        input_list_org           input_list_without_equal
    #         3-9      ['3', '9', '6']        ['-']      ['3', '-', '9', '=',' '6']       ['3', '-', '9', '6']
    number = number_org[:]
    input_list = input_list_org[:]
    input_list_without_equal = input_list_org[:]
    input_list_without_equal.remove('=')
    for i in range(0, len(input_list_without_equal)):  # i从 0-input_list_without_equal的长度
        for j in range(0, len(add[input_list_without_equal[i]])):  # j从 0-字典add的value的长度
            # print add[input_list_without_equal[i]][j]  # input_list_without_equal中每一个元素在add字典中的value
            if not add[input_list_without_equal[i]]:
                print 'eeeeeeeeeeeeeeeee'
                continue
            try:
                input_list_without_equal[i] = str(add[input_list_without_equal[i]][j])
            except:
                print 'except'
                print i
                print j
            # print input_list_without_equal
            for k in range(i+1, len(input_list_without_equal)): # k从 input_list_without_equal[i+1]个元素的index 到最后
                for l in range(0, len(minus[input_list_without_equal[k]])):
                    # print minus[input_list_without_equal[k]][l]
                    input_list_without_equal[k] = str(minus[input_list_without_equal[k]][l])
                    # print input_list_without_equal
                    if eval(list_to_str(input_list_without_equal[:-1])) == int(input_list_without_equal[-1]):
                        # print "move one match from {} to {}".format(input_list_without_equal[k], input_list_without_equal[i])
                        print list_to_str(input_list_without_equal[:-1]) + '=' + str(input_list_without_equal[-1])
                        input_list_without_equal = input_list_org[:]
                        input_list_without_equal.remove('=')
                    else:
                        input_list_without_equal = input_list_org[:]
                        input_list_without_equal.remove('=')

            #     input_list_without_equal[i] = str(add[input_list_without_equal[i]][j])
            #     input_list_without_equal[k] =


def main():
    rc = assert_equality()
    if rc == 1:
        return


if __name__ == "__main__":
    main()

