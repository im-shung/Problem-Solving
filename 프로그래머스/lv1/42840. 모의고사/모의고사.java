import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        // 1: 1, 2, 3, 4, 5
        // 2: 2, 1, 2, 3, 2, 4, 2, 5
        // 3: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5
        int[] count = {0, 0, 0};
        int[][] person = {{1, 2, 3, 4, 5}, {2, 1, 2, 3, 2, 4, 2, 5}, {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}};
        
        int max = 0;
        for(int i = 0; i < answers.length; i++) {
            for (int j = 0; j < 3; j++) {
                
                if (person[j][i % person[j].length] == answers[i]) {
                    count[j]++;
                    max = Math.max(max, count[j]);
                }
            }
        }
        
        int[] answer = {};
        int index = 0;
        for(int i = 0; i < 3; i++) {
            if (count[i] == max) {
                index++;
            }
        }
        answer = new int[index];
        index = 0;
        for(int i = 0; i < 3; i++) {
            if (count[i] == max) {
                answer[index++] = i + 1;
            }
        }
        return answer;
    }
}