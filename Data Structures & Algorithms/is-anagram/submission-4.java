class Solution {
    public boolean isAnagram(String s, String t) {
        int chArr[]=new int[255];

        for(char ch1:s.toCharArray()) chArr[ch1]++;
        for(char ch2:t.toCharArray()) chArr[ch2]--;

        for(int i=0;i<chArr.length;i++){
            if(chArr[i]!=0) return false;
        }
        return true;
    }
}
