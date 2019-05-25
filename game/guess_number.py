import random


def create_answer():
    pool = list(range(0, 10))
    answer = random.sample(pool, 4)
    return answer  # e.g: '1234'


def compare(a, b):
    # a is user answer
    # b is correct answer
    aa = 0
    bb = 0
    index = 0
    for i in a:
        if i == b[index]:
            aa += 1
            index += 1
        elif i in b:
            bb += 1
            index += 1
        else:
            index += 1
    return [str(aa)+'A', str(bb)+'B']


def check_dup(a):
    for i in a:
        if a.count(i) > 1:
            return True
    return False


def run():
    print ("""RULES:
    If correct answer is: 1234
    Your answer is: 1456
    You will get HINT "1A,1B"
    A stands for correct number in correct position, here is '1'
    B stands for correct number in wrong position, here is '4'
    You will have 8 times to guess the answer""")

    correct_answer = create_answer()
    i = 8
    j = 0
    k = 0
    while i > 0:
        print ('*********************************')
        if i > 1:
            print ('you have %s times to try' % i)
        else:
            print ('last chance')

        # user input must be string due to answer begins with 0. e.g: 0123
        user_input_answer = str(raw_input('give me your 4 digit answer: '))

        if user_input_answer == 'show me the answer' and k == 0:
            print (correct_answer)
            k += 1
            continue
        elif user_input_answer == 'i am your dad':
            print ('answer: ' + correct_answer + '\nCongradulation!')
            return

        try:
            # user_input_answer = string, catch error
            int(user_input_answer)
            # user_input_answer is not 4 digit0
            if len(user_input_answer) != 4:
                j += 1
                print ('answer must be 4 digit')
                continue
            elif check_dup(list(user_input_answer)):
                j += 1
                print ('The number in answer is duplicated')
                continue
        except ValueError:
            j += 1
            print ('wrong format answer')
            continue
        finally:
            if j >= 3:
                print ('sb')
                return

        if user_input_answer == correct_answer:
            print ('Congradulation!')
            return
        else:
            user_answer_list = list(str(user_input_answer))
            print (compare(user_answer_list, list(correct_answer)))
            i -= 1

    print ('answer is: ' + correct_answer + '\nfail')


def main():
    run()


if __name__ == "__main__":
    main()