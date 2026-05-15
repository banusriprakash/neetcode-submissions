class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> mp=new HashMap<>();
        int ans[]=new int[2];
        for(int i=0;i<nums.length;i++){
            mp.put(nums[i],i);
        }

        for(int i=0;i<nums.length;i++){
            int diff=target-nums[i];
            if(mp.containsKey(diff) && mp.get(diff)!=i){
                ans[0]=i;
                ans[1]=mp.get(diff);
            }
        }
        Arrays.sort(ans);
        return ans;
    }
}
