class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> mp=new HashMap<>();

        for(String str:strs){
            char arr[]=str.toCharArray();
            Arrays.sort(arr);
            String org=new String(arr);

            if(!mp.containsKey(org)){
                List<String> ls=new ArrayList<>();
                ls.add(str);
                mp.put(org,ls);
            }
            else mp.get(org).add(str);
        }

        return new ArrayList<>(mp.values());
    }
}
