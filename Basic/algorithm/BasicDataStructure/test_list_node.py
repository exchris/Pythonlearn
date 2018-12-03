from list_node import ListNode

ln1 = ListNode(1);
ln2 = ListNode(2);
ln3 = ListNode(3);
ln4 = ListNode(4);


ln1.next = ln2
ln2.next = ln3
ln3.next = ln4

print(ln1.__dict__)
print(ln2.__dict__)
print(ln3.__dict__)
print(ln4.__dict__)
