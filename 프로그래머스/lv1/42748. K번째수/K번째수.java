import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        

        int[] answer = new int[commands.length];
        int i = 0;
        for (int[] command : commands) {
            int s = command[0];
            int e = command[1];
            int k = command[2];
            Integer[] memo = new Integer[e-s+1];
            for(int ii = s-1; ii <= e-1; ii++) {
                memo[ii-s+1] = array[ii];
            }
            Arrays.sort(memo);
            // System.out.println(Arrays.toString(memo));
            answer[i++] = memo[k-1];
        }

        return answer;
    }
}