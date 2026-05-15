class Solution {

    public String encode(List<String> strs) {
        
        StringBuilder sb=new StringBuilder();
        for(String s:strs){
            sb.append(s.length()).append("#").append(s);
        }
        return new String(sb);
    }

    public List<String> decode(String str) {
       List<String> res = new ArrayList<>();
        int i = 0;
        
        while (i < str.length()) {
            // 1. Find the delimiter '#' starting from current position i
            int j = str.indexOf("#", i);
            
            // 2. The number between i and j is our length
            int length = Integer.parseInt(str.substring(i, j));
            
            // 3. Move i to the start of the actual string (just after '#')
            i = j + 1;
            
            // 4. Extract the string and move i to the start of the next segment
            res.add(str.substring(i, i + length));
            i += length;
        }
        return res;
    }
}
