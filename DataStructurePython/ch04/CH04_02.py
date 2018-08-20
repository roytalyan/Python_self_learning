# -*- coding: gbk -*-

from __future__ import print_function
import random
global top

top=-1
k=0

def push(stack,MAX,val):
    global top
    if top>=MAX-1:
        print('[��ջ�Ѿ�����]')
    else:
        top=top+1
        stack[top]=val
        
def pop(stack):
    global top
    if top<0:
        print('[��ջ�Ѿ�����]')
    else:
        top=top-1
        return stack[top]

def shuffle(old):
    result=[]
    while old:
        p=random.randrange(0,len(old))
        result.append(old[p])
        old.pop(p)
    return result

card=[None]*52
card_new=[None]*52
stack=[0]*52
for i in range(52):
    card[i]=i+1

print('[ϴ����...���Ժ�!]')

card_new=shuffle(card)

i=0
while i!=52:
    push(stack,52,card_new[i])  #��52����ѹ���ջ
    i=i+1

print('[��ʱ�뷢��]')
print('[��ʾ���ҵ���] ����\t  ����\t   ����\t    �ϼ�')
print('=================================')

while top>=0:
    #print(stack[top])
    style = (stack[top]) % 4	#�����ƵĻ�ɫ
    #print('style=', style)
    if style==0:  #÷��
        ascVal='club'
    elif style==1:  #����
        ascVal='diamond'
    elif style==2:   #����
        ascVal='heart'
    elif style==3:
        ascVal='spade'   #����
    
    print('[%s%3d]\t' %(ascVal,stack[top]%13+1),end='')
    if top%4==0:
        print()
    top-=1