class Solution {
    public int longestConsecutive(int[] nums) {
        int cnt=1,lon=1;
        if(nums.length==0) return 0;
        Arrays.sort(nums);
        for(int i=1;i<nums.length;i++){
            if(nums[i]!=nums[i-1]){
                if(nums[i]==nums[i-1]+1) cnt++;
                else{
                lon=Math.max(lon,cnt);
                cnt=1;
            }
            }
            
            
        }
        return Math.max(lon,cnt);
    }
}
