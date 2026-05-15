class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> mp=new HashMap<>();
        List<Integer> ls=new ArrayList<>();
        for(int num:nums){
            mp.put(num,mp.getOrDefault(num,0)+1);
        }

        List<Integer> keys = new ArrayList<>(mp.keySet());
        keys.sort((a, b) -> mp.get(b) - mp.get(a));

        for(int i = 0; i < k; i++) {
            ls.add(keys.get(i));
        }

        int ans[]=new int[ls.size()];

        for(int i=0;i<ls.size();i++){
            ans[i]=ls.get(i);
        }
        return ans;
    }
}
