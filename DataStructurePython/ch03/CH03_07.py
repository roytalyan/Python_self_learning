# coding:gbk


class LinkedList:  #��������ṹ
    def __init__(self):
        self.coef=0
        self.exp=0
        self.next=None
def create_link(data): #��������ʽ�ӳ���
    for i in range(4):
        newnode=LinkedList()
        if not newnode:
            print("Error!! �ڴ����ʧ��!!")
            sys.exit(0)
        if i==0:
            newnode.coef=data[i]
            newnode.exp=3-i
            newnode.next=None
            head=newnode
            ptr=head
        elif data[i]!=0:
            newnode.coef=data[i]
            newnode.exp=3-i
            newnode.next=None
            ptr.next=newnode
            ptr=newnode
    return head

def print_link(head):  #��ӡ����ʽ�ӳ���
    while head !=None:
        if head.exp==1 and head.coef!=0:  #X^1ʱ����ʾָ��
            print("%dX + " %(head.coef) )
        elif head.exp!=0 and head.coef!=0:
            print("%dX^%d + " %(head.coef,head.exp) )
        elif head.exp ==0 and head.coef!=0: #X^0ʱ����ʾ����
            print("%d" %(head.coef))
        head=head.next
    print()
        
def sum_link(a,b): #����ʽ����ӳ���
    i=0
    ptr=b
    plus=[None]*4
    while a!=None: #�ж϶���ʽ1
        if a.exp==b.exp: #ָ����ȣ�ϵ�����
            plus[i]=a.coef+b.coef
            a=a.next
            b=b.next
            i=i+1
        elif b.exp>a.exp: #Bָ���ϴ󣬰�ϵ����ֵ��C
            plus[i]=b.coef
            b=b.next
            i=i+1
        elif a.exp>b.exp: #Aָ���ϴ󣬰�ϵ����ֵ��C
            plus[i]=a.coef
            a=a.next
            i=i+1
    return create_link(plus)     #������ӽ������C

def main():
    data1=[3,0,4,2]         #����ʽA��ϵ��
    data2=[6,8,6,9]         #����ʽB��ϵ��
    #c=LinkedList()
    print("ԭʼ����ʽ��\nA=" )
    a=create_link(data1)    #��������ʽA
    b=create_link(data2)    #��������ʽB
    print_link(a)           #��ӡ����ʽA
    print("B=" )
    print_link(b)           #��ӡ����ʽB
    print("����ʽ��ӵĽ����\nC=" ) #CΪA��B����ʽ��ӵĽ��
    print_link(sum_link(a,b))         #��ӡ����ʽC
    	
main()