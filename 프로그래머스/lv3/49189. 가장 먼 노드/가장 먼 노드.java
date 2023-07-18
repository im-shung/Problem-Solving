import java.util.*;

class Solution {
    boolean[] visited;
    int[] dist;
    int max = 0;
    ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
    
    public int solution(int n, int[][] edge) {
        for(int i=0; i<=n; i++) {
            adj.add(new ArrayList<>());
        }
        for(int[] a : edge){
            adj.get(a[0]).add(a[1]);
            adj.get(a[1]).add(a[0]);
        }        
        visited = new boolean[n+1];    
        dist = new int[n+1]; 
        bfs();
        int answer = 0;
        for(int i = 1; i <= n; i++) {
            if (max == dist[i]) answer++;
        }
        
        return answer;
    }

    
    void bfs() {
        Queue<Integer> que = new LinkedList<>();
        que.offer(1);
        que.offer(0);
        visited[1] = true;
        
        while(!que.isEmpty()) {
            int node = que.poll();
            int ddist = que.poll();
            
            for(int next : adj.get(node)) {
                if (visited[next]) continue;
                visited[next] = true;
                dist[next] = ddist + 1;
                que.add(next);
                que.add(dist[next]);
                max = Math.max(dist[next], max);
            }
        }
        
    }
}