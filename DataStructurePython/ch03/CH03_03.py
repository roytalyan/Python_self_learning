# coding:GBK


import sys
class employee:
    def __init__(self):
        self.num=0
        self.salary=0
        self.name=''
        self.next=None
        
def del_ptr(head,ptr):  #ɾ���ڵ��ӳ���
    top=head
    if ptr.num==head.num:  #[����1]:Ҫɾ���Ľڵ�������ͷ��
        # head=head.num
        head = head.next

        print('��ɾ���� %d ��Ա�� ������%s н��:%d' %(ptr.num,ptr.name,ptr.salary))
    else:
        while top.next!=ptr:  #�ҵ�ɾ���ڵ��ǰһ��λ��
            top=top.next
        if ptr.next==None:   #ɾ��������ĩβ�Ľڵ�
            top.next=None
            print('��ɾ���� %d ��Ա�� ������%s н��:%d' %(ptr.num,ptr.name,ptr.salary))
        else:
            top.next=ptr.next #ɾ���ڴ����е���һ�ڵ�
            print('��ɾ���� %d ��Ա�� ������%s н��:%d' %(ptr.num,ptr.name,ptr.salary))
    return head  #��������

def main():
    findword=0
    namedata=['Allen','Scott','Marry','John',\
              'Mark','Ricky','Lisa','Jasica',\
              'Hanson','Amy','Bob','Jack']
    data=[[1001,32367],[1002,24388],[1003,27556],[1007,31299], \
          [1012,42660],[1014,25676],[1018,44145],[1043,52182], \
          [1031,32769],[1037,21100],[1041,32196],[1046,25776]]
    print('Ա����� нˮ Ա����� нˮ Ա����� нˮ Ա����� нˮ')
    print('-------------------------------------------------------')
    for i in range(3):
        for j in range(4):
            print('%2d  [%3d]  ' %(data[j*3+i][0],data[j*3+i][1]))
        print()
    head=employee() #��������ͷ��
    if not head:
        print('Error!! �ڴ����ʧ��!!')
        sys.exit(0)
    head.num=data[0][0]
    head.name=namedata[0]
    head.salary=data[0][1]
    head.next=None
    roy = head
	
    ptr=head
    for i in range(1,12):  #��������
        newnode=employee()
        newnode.num=data[i][0]
        newnode.name=namedata[i]
        newnode.salary=data[i][1]
        newnode.num=data[i][0]
        newnode.next=None
        ptr.next=newnode
        ptr=ptr.next
			
    while(True):
        findword=int(input('������Ҫɾ����Ա�����,Ҫ����ɾ������,������-1��'))
        if(findword==-1): #ѭ���ж�����
            break
        else:
            ptr=head
            find=0
            while ptr!=None:
                if ptr.num==findword:
                    ptr=del_ptr(head,ptr)
                    find=find+1
                    head=ptr
                ptr=ptr.next
            if find==0:
                print('######û���ҵ�######')
			
    ptr=head
    print('\tԱ�����    ����\tнˮ')   #��ӡʣ�������е�����
    print('\t==============================')
    while(ptr!=None):
        print('\t[%2d]\t[ %-10s]\t[%3d]' %(ptr.num,ptr.name,ptr.salary))
        ptr=ptr.next
main()
