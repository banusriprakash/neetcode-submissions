class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer,Integer> mp=new HashMap<>();

        for(int num:nums){
            mp.put(num,mp.getOrDefault(num,0)+1);
        }
        int max=-1;
        int ans=nums[0];
        for(Map.Entry<Integer,Integer> entry:mp.entrySet()){
            int key=entry.getKey();
            int value=entry.getValue();
            if(value>max){
                ans=key;
                max=value;
            }
        }
        return ans;
    }
}