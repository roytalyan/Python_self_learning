# coding:gbk


class student:
    def __init__(self):
        self.name=''
        self.no=''
        self.next=None

head=student()  #��������ͷԪ��
ptr = head    #���ô�ȡָ��λ��
ptr.next = None    #Ŀǰ��һ�¸�Ԫ��
select=0
while select!=2:
    select=int(input('(1)���� (2)�뿪 =>'))
    if select ==2:
        break
    ptr.name=input('���� :')
    ptr.no=input('ѧ�� :')
    new_data=student() #������һԪ��
    ptr.next=new_data   #������һԪ��
    new_data.next = None  #��һԪ�ص�next������ΪNone
    ptr = new_data  #��ȡָ������Ϊ��Ԫ������λ��

ptr.next = head  #���ô�ȡָ���ͷ��ʼ
print()
ptr=head

while True:
     print('������%s\tѧ��:%s\n' %(ptr.name,ptr.no))
     ptr=ptr.next  #��head������һԪ��
     if ptr.next==head:
         break
print('---------------------------------------------------------')


# class student:
#     def __init__(self):
#         self.name = ''
#         self.no = ''
#         self.next = None
#
#
# head = student()  # ��������ͷԪ��
# ptr = head  # ���ô�ȡָ��λ��
# ptr.name = 'test'
# ptr.no = 0
# ptr.next = None  # Ŀǰ��һ�¸�Ԫ��
# select = 0
# while select != 2:
#     select = int(input('(1)���� (2)�뿪 =>'))
#     if select == 2:
#         break
#
#     new_data = student()  # ������һԪ��
#     new_data.name = input('���� :')
#     new_data.no = input('ѧ�� :')
#
#     ptr.next = new_data  # ������һԪ��
#     new_data.next = None  # ��һԪ�ص�next������ΪNone
#     ptr = new_data  # ��ȡָ������Ϊ��Ԫ������λ��
#
# ptr.next = head  # ���ô�ȡָ���ͷ��ʼ
# print()
# ptr = head
#
# while True:
#     print('������%s\tѧ��:%s\n' % (ptr.name, ptr.no))
#     ptr = ptr.next  # ��head������һԪ��
#     if ptr == head:    ############## ptr == head
#         break
# print('---------------------------------------------------------')