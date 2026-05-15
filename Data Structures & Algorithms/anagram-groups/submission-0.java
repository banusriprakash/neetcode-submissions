class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        Map<String,List<String>> mp=new HashMap<>();

        for(String str:strs){
            char charr[]=str.toCharArray();
            Arrays.sort(charr);
            String st=String.valueOf(charr);
            if(!mp.containsKey(st)){
                mp.put(st,new ArrayList<>());
               
            }
             mp.get(st).add(str);

        }

        List<List<String>> ans=new ArrayList<>(mp.values());

        return ans;
    }
}
