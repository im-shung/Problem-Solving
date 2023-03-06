import java.util.*;

/* 좌표 (Y,X)
[Y]
6   ㅡㅡ
       |
5    ㅡ 
    3  4  [X]

<문제점>
예제 1
(5,3)에서 (6,3)으로 갈 수 없다.
그러나 상하좌우로 이동하는 bfs()에서는 갈 수 있는 길로 인식한다.
이 문제점을 막기 위해 좌표를 2배로 늘린다. -> 좌표마다 사이사이에 빈칸이 생긴다.

*/

class Node {
	int y;
	int x;
	int length;

	public Node(int y, int x, int length) {
		this.y = y;
		this.x = x;
		this.length = length;
	}
    
    public String toString() {
        return "y = " + y + ", x = " + x + ", length = " + length;
    }
}

class Solution {
	static final int[] DY = {1, -1, 0, 0};
	static final int[] DX = {0, 0, 1, -1};
	
	static final int N = 103;
	static boolean[][] map;
	static int answer = Integer.MAX_VALUE;

	public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
		map = new boolean[N][N];

		// 직사각형 경계 분리
		// 경계는 1
		for (int[] data : rectangle) {
			// rectangle[i]: [x1, y1, x2, y2]
			int x1 = data[0] * 2;
			int y1 = data[1] * 2;
			int x2 = data[2] * 2;
			int y2 = data[3] * 2;
			for (int x = x1; x <= x2; x++) {
                for (int y = y1; y <= y2; y++) {
                    map[y][x] = true;
                }
			}
		}
        
        // 직사각형 내부는 0
		for (int[] data : rectangle) {
			// rectangle[i]: [x1, y1, x2, y2]
			int x1 = data[0] * 2;
			int y1 = data[1] * 2;
			int x2 = data[2] * 2;
			int y2 = data[3] * 2;
			for (int x = x1 + 1; x < x2; x++) {
                for (int y = y1 + 1; y < y2; y++) {
                    map[y][x] = false;
                }
			}
		}
        
        bfs(characterX * 2, characterY * 2, itemX * 2, itemY * 2);
        
		return answer;
	}

	public void bfs(int characterX, int characterY, int itemX, int itemY) {
		Deque<Node> que = new ArrayDeque<>();
		que.add(new Node(characterY, characterX, 0));
        map[characterY][characterX] = true;
        
		while (!que.isEmpty()) {
			// 1. 큐에서 꺼냄
			Node cur = que.poll();
			// 2. 목적지인가? -> 아이템 위치 
			if (cur.y == itemY && cur.x == itemX) {
				answer = Math.min(answer, cur.length / 2);
			} else {
				// 3. 연결된 곳인가?
				for (int i = 0; i < 4; i++) {
					int dy = cur.y + DY[i];
					int dx = cur.x + DX[i];
					
					// 4. 갈 수 있는가? -> 직사각형의 경계만 갈 수 있음
					if (0 <= dy && dy < N && 0 <= dx && dx < N) {
						if (map[dy][dx] == true) {
							// 5. 체크인
							map[dy][dx] = false;
							// 6. 큐에 넣음
							que.add(new Node(dy, dx, cur.length + 1));
						}
					}
				}
			}
		}
	}
}