class Solution {
    public int removeElement(int[] nums, int val) {
      
        List<Integer> ans=new ArrayList<>();
        for(int num:nums){
            if(val!=num) ans.add(num);
        }

        for(int i=0;i<ans.size();i++){
            nums[i]=ans.get(i);
        }
        return ans.size();
    }
}