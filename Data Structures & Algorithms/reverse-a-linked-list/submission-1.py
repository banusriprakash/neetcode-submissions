# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ls=[]

        

        
        tmp=head

        while tmp!=None:
            ls.append(tmp.val)
            tmp=tmp.next

        i=0
        j=len(ls)-1

        while i<j:
            t=ls[i]
            ls[i]=ls[j]
            ls[j]=t
            i+=1
            j-=1

        print(ls)
        dum=ListNode(-1)
        curr=dum

        for val in ls:
            curr.next=ListNode(val)
            curr=curr.next
        return dum.next
        