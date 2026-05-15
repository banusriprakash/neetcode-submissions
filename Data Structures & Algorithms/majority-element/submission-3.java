class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer,Integer> mp=new HashMap<>();

        for(int num:nums){
            mp.put(num,mp.getOrDefault(num,0)+1);
        }

        int ans=0;

        for(Map.Entry<Integer,Integer> entry:mp.entrySet()){
            int key=entry.getKey();
            int val=entry.getValue();
            if(val>nums.length/2){
                ans=key;
            }
        }
        return ans;
    }
}