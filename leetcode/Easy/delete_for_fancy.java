package leetcode.Easy;

class Solution {
    public String makeFancyString(String s) {
        if (s.length() < 3)
            return s;
        StringBuilder res = new StringBuilder();
        char[] chars;
        chars = s.toCharArray();
        for(int i=0; i<chars.length-2; i++){
            if ((chars[i] != chars[i+1]) | (chars[i] != chars[i+2])){
                res.append(chars[i]);
            }
        }
        res.append(chars[chars.length - 2]);
        res.append(chars[chars.length - 1]);
        return res.toString();
    }
}