class Solution {
    public boolean hasDuplicate(int[] nums) {
        List<Integer> ls=new ArrayList<>();

        for(int num:nums){
            if(ls.contains(num)) return true;
            else ls.add(num);
        }
        return false;
    }
}