class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int cnt=0;
        int lon=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==1){
                cnt++;
                lon=Math.max(cnt,lon);
            }
            else{
                cnt=0;
            }
        }
        return lon;
    }
}