class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int ans[]=new int[2];
        for(int i=0;i<numbers.length-1;i++){
            int sum=0;
            for(int j=i+1;j<numbers.length;j++){
                sum=numbers[i]+numbers[j];
                if(sum==target){
                    ans[0]=i+1;
                    ans[1]=j+1;
                    break;
                }
            }
        }
        return ans;
    }
}
