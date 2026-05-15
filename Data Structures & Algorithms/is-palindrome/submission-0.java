class Solution {
    public boolean isPalindrome(String s) {
        String rpl=s.replaceAll("[^A-Za-z0-9]","").toLowerCase();
        StringBuilder sb=new StringBuilder(rpl).reverse();
        String rev=new String(sb);

        return rev.equals(rpl);

    }
}
