/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode tmp1=list1;
        ListNode tmp2=list2;
        List<Integer> ls=new ArrayList<>();
        while(tmp1!=null){
            ls.add(tmp1.val);
            tmp1=tmp1.next;
        }
        while(tmp2!=null){
            ls.add(tmp2.val);
            tmp2=tmp2.next;
        }
        Collections.sort(ls);
        ListNode dumm=new ListNode(-1);
        ListNode org=dumm;
        for(int i=0;i<ls.size();i++){
            dumm.next=new ListNode(ls.get(i));
            dumm=dumm.next;
        }
        return org.next;
    }
}