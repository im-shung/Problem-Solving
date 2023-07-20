import java.util.*;

class Solution {
    
    ArrayList<Integer>[] adj;
    int[] dist;
    
    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
        dist = new int[n+1];
        Arrays.fill(dist, -1);
        adj = new ArrayList[n+1];
        for(int i = 1; i <= n; i++) adj[i] = new ArrayList<Integer>();
        for(int[] road : roads) {
            adj[road[0]].add(road[1]);
            adj[road[1]].add(road[0]);
        }
        bfs(destination);
        int[] answer = new int[sources.length];
        for(int i=0; i<sources.length; i++){
            answer[i] = dist[sources[i]];
        }
        
        
        return answer;
    }
    
    void bfs(int destination) {
        Queue<Integer> que = new LinkedList<>();
        que.offer(destination);
        dist[destination] = 0;
        
        while(!que.isEmpty()) {
            int node = que.poll();
            
            for(int next : adj[node]) {
                if (dist[next] == -1) {
                    dist[next] = dist[node] + 1;
                    que.offer(next);
                }
            }
        }
    }
}