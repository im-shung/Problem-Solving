import java.util.*;

class Solution {
    
    static int N, K, ans;
    static boolean[] visit;
    static int[][] D;
    
    public int solution(int k, int[][] dungeons) {
        K = k; D = dungeons;
        N = dungeons.length;
        visit = new boolean[N];
        
        /*
        @param1 탐색한 던전갯수
        @param2 현재 남아있는 피로도
        @param3 방문한 던전갯수
        */
        dfs(0, K, 0);
        
        return ans;
    }
    
    private void dfs(int depth, int pirodo, int visitCnt) {
        // 목적지에 도달했는가? -> 던전 모두 체크(방문) 완료! 
        if (visitCnt == N) {
            // 최대 던전 수를 갱신한다
            ans = Math.max(ans, depth);
            return;
        }
        
        // 모든 던전을 체크(방문) 한다
        for (int i = 0; i < N; i++) {
            if (!visit[i]) {
                // 체크인
                visit[i] = true;
       
                // 최소 필요 피로도를 만족했을 경우 --> 해당 던전을 방문O (depth + 1)
                if (pirodo >= D[i][0])
                    dfs(depth + 1, pirodo - D[i][1], visitCnt + 1);
                // 최소 필요 피로도를 만족하지 못한 경우 --> 해당 던전을 방문X (depth 그대로)
                else 
                    dfs(depth, pirodo, visitCnt + 1);
                
                //체크아웃
                visit[i] = false;
            }
        }
    }
}