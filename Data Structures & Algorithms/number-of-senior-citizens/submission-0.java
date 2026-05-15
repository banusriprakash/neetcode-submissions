class Solution {
    public int countSeniors(String[] details) {
        int cnt=0;
        for(String str:details){
            int i = Math.max(str.indexOf('M'), Math.max(str.indexOf('F'), str.indexOf('O')));
            String val=str.substring(i+1,i+3);
            System.out.println(val);
             if(Integer.parseInt(val)>60) cnt++;
        }
        return cnt;
    }
}