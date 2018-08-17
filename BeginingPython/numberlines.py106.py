import fileinput

for line in fileinput.input(inplace=False):
    line = line.rstrip()
    num = fileinput.lineno()
    print '%1s # %i' %(line, num)

