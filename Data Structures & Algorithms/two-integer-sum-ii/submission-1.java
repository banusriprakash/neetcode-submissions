class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int ans[]=new int[2];
        Map<Integer,Integer> mp=new HashMap<>();
        for(int i=0;i<numbers.length;i++){
            mp.put(numbers[i],i);
        }
        for(int i=0;i<numbers.length;i++){
            int diff=target-numbers[i];
            if(mp.containsKey(diff)){
                ans[0]=mp.get(diff)+1;
                ans[1]=i+1;
            }
        }
        return ans;
    }
}
