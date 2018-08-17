def lines(file):
    for line in file: yield line
    yield '\n'


def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []


# file = 'util.py'
#
# result = []
# result.append(blocks(file))
# for i in result:
#     print i


# def yield_test(n):
#     for i in range(n):
#         yield call(i)
#         print("i=",i)
#
#     print("do something.")
#     print("end.")
#
# def call(i):
#     return i*2
#
#
# for i in yield_test(5):
#     print(i,",")