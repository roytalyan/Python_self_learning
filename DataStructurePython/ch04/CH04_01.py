# -*- coding: gbk -*-


MAXSTACK=100 #�����ջ���������
global stack
stack=[None]*MAXSTACK  #��ջ����������
top=-1 #��ջ�Ķ���

#�ж��Ƿ�Ϊ�ն�ջ
def isEmpty():
    if top==-1:
        return True
    else:
        return False

#��ָ��������ѹ���ջ
def push(data):
    global top
    global MAXSTACK
    global stack
    if top>=MAXSTACK-1:
        print('��ջ����,�޷��ټ���')
    else:
        top +=1
        stack[top]=data #������ѹ���ջ

#�Ӷ�ջ��������*/
def pop():
    global top
    global stack
    if isEmpty():
        print('��ջ�ǿ�')
    else:
        print('������Ԫ��Ϊ: %d' % stack[top])
        top=top-1     
        
#������
i=2
count=0
while True:
    i=int(input('Ҫѹ���ջ,������1,Ҫ����������0,ֹͣ����������-1: '))
    if i==-1:
        break
    elif i==1:
        value=int(input('������Ԫ��ֵ:'))
        push(value)
    elif i==0:
        pop()

print('============================')
if top <0:
    print('\n ��ջ�ǿյ�')
else:
    i=top
    while i>=0:
        print('��ջ������˳��Ϊ:%d' %(stack[i]))
        count +=1
        i =i-1
    print 

print('============================')  