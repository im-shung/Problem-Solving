import java.util.*;

class Solution {
    
    static int N, K, ans;
    static boolean[] visit;
    static int[][] D;
    
    public int solution(int k, int[][] dungeons) {
        K = k; D = dungeons;
        N = dungeons.length;
        visit = new boolean[N];
        
        // 시작점, 초기 피로도
        dfs(0, K, 0);
        
        return ans;
    }
    
    private void dfs(int depth, int pirodo, int visitCnt) {
        if (visitCnt == N) {
            ans = Math.max(ans, depth);
     
            return;
        }
        
        for (int i = 0; i < N; i++) {
            // 방문하지 않았으며, 최소 필요 피로도를 만족한다.
            if (!visit[i]) {
                // 체크인
                visit[i] = true;
       
                // dfs 간다.
                if (pirodo >= D[i][0])
                    dfs(depth + 1, pirodo - D[i][1], visitCnt + 1);
                else 
                    dfs(depth, pirodo, visitCnt + 1);
                
                //체크아웃
                visit[i] = false;
            }
        }
    }
}