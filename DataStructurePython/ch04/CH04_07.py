# -*- coding: gbk -*-


def hanoi(n, p1, p2, p3):
    if n==1: # �ݹ����
        print('���Ӵ� %d �Ƶ� %d' %(p1, p3))
    else:
        hanoi(n-1, p1, p3, p2)
        print('���Ӵ� %d �Ƶ� %d' %(p1, p3))
        hanoi(n-1, p2, p1, p3)

j=int(input('������Ҫ�ƶ����ӵ�������'))
hanoi(j,1, 2, 3)