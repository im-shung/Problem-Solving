import java.util.*;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        int N = citations.length;
        int maxCnt = citations[N - 1];
        int answer = 0;
        // 논문별 인용 횟수 0~max
        for (int h = 0; h <= maxCnt; h++) {
            int lowIdxCnt = 0;
            int highIdxCnt = 0;
            
            // 논문을 돌면서 h편 이상인 논문 & h편 이하의 논문의 갯수를 구한다.
            for (int idx = 0; idx < N; idx++) {
                if (citations[idx] >= h) {
                    highIdxCnt++;
                } else {
                    lowIdxCnt++;
                }
            }
            
            if (highIdxCnt >= h && lowIdxCnt <= h) {
                answer = Math.max(answer, h);
            }
        }
        return answer;
        
    }
}