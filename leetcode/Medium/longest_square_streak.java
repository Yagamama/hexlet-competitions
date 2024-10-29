import java.util.Set;
import java.util.HashSet;
import java.lang.Math;

class Solution {
    public static void main(String[] args){
        int[] a = {4,3,6,16,8,2};
        int res = longestSquareStreak(a);
        System.out.println(res);  // 3
        int[] b = {2,3,5,6,7};
        res = longestSquareStreak(b);
        System.out.println(res);  // -1
    }

    public static int longestSquareStreak(int[] nums) {
        int count = 0;
        Set<Integer> s = new HashSet<>();
        for (int num : nums) {
            s.add(num);
        }
        for (int num: s){
            int c = 0;
            long n = num;
            while (s.contains((int) n)){
                c++;
                if (n*n > 1e5){break;}
                n *= n;
            }
            count = Math.max(c, count);
        }
        return count < 2 ? -1 : count;
    } 
}
    