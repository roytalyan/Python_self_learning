# coding:utf-8

class ListNode:
    def __init__(self, x):
        self.val = x;
        self.next = None;


def nonrecurse(head):  # 循环的方法反转链表
    if head is None or head.next is None:
        return head;
    pre = None;
    cur = head;
    h = head;
    while cur:
        h = cur;
        tmp = cur.next;
        cur.next = pre;
        pre = cur;
        cur = tmp;
    return h;


def fun(x):
    p = x
    q = None
    while p != None:
        r = q
        q = p
        p = p.next
        q.next = r
    return q

def func1(head):
    p = head
    q = p.next
    p.next = None
    while q:
        r = q.next
        q.next = p
        p = q
        q = r
    return p

head = ListNode(1);  # 测试代码
p1 = ListNode(2);  # 建立链表1->2->3->4->None;
p2 = ListNode(3);
p3 = ListNode(4);
head.next = p1;
p1.next = p2;
p2.next = p3;
# px = nonrecurse(head);  # 输出链表 4->3->2->1->None
px = func1(head)
while px:
    print px.val;
    px = px.next;



