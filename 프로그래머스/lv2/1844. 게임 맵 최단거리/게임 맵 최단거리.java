import java.util.*;

class Node {
	int r;
	int c;
	int len;
	
	public Node(int r, int c, int len) {
		this.r = r;
		this.c = c;
		this.len = len;
	}
}

class Solution {
	static int[] DR = {1, -1, 0, 0};
	static int[] DC = {0, 0, 1, -1};
	
	static boolean[][] visit;
	static int R, C;
	
    public int solution(int[][] maps) {
    	R = maps.length;
    	C = maps[0].length;
    	
    	visit = new boolean[R][C];
    	
        return bfs(maps);
    }
    
    public int bfs(int[][] maps) {
    	Deque<Node> queue = new ArrayDeque<>(); 
    	queue.add(new Node(0,0,1));
    	visit[0][0] = true;
    	
    	while (!queue.isEmpty()) {
        	// 1. 큐에서 꺼냄 
    		Node cur = queue.poll();
        	// 2. 목적지인가?
    		if (cur.r == R - 1 && cur.c == C - 1) {
    			return cur.len;
    		} 
        	// 3. 연결된 곳인가?
    		for (int i = 0; i < 4; i++) {
    			int dr = cur.r + DR[i];
    			int dc = cur.c + DC[i];
    			
    			// 4. 갈 수 있는가?
    			if (0 <= dr && dr < R && 0 <= dc && dc < C) {
    				if (!visit[dr][dc] && maps[dr][dc] == 1) {
    					// 5. 체크인
    					visit[dr][dc] = true;
    	            	// 6. 큐에 넣음 
    					queue.add(new Node(dr, dc, cur.len + 1));
    				}
    			}
    		}
        
    	}
    	
    	return -1;
    }
}