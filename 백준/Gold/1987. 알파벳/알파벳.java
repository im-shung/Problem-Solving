import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.*;
import java.util.StringTokenizer;

public class Main {

	static class Node {
		int y;
		int x;
		int cnt;

		public Node(int y, int x, int cnt) {
			super();
			this.y = y;
			this.x = x;
			this.cnt = cnt;
		}

		@Override
		public String toString() {
			StringBuilder builder = new StringBuilder();
			builder.append("Node [y=").append(y).append(", x=").append(x).append(", cnt=").append(cnt).append("]");
			return builder.toString();
		}
		
		

	}

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();

	static int[][] DIR = {{0, 1}, {1,0}, {0, -1}, {-1, 0}};
	
	static int R, C;
	static char[][] map;
	static int ans;
	static boolean[] visit = new boolean[26];

	public static void main(String[] args) throws Exception {
		//br = new BufferedReader(new FileReader("src/input.txt"));
		/* 입력 */
		st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		map = new char[R + 1][C + 1];
		for (int i = 1; i <= R; i++) {
			String line = br.readLine();
			for (int j = 1; j <= C; j++) {
				map[i][j] = line.charAt(j - 1);
			}
		}
//		System.out.println(Arrays.deepToString(map));
		/* 처리 */

		find(1, 1, 1);
		
		/* 출력 */
		System.out.println(ans);
	}

	private static void find(int y, int x, int cnt) {
		if (visit[map[y][x] - 'A']) return;
		visit[map[y][x] - 'A'] = true;
		ans = Math.max(ans, cnt);
		
		for (int d = 0; d < 4; d++) {
			int dy = y + DIR[d][0];
			int dx = x + DIR[d][1];
			if (canNotGo(dy, dx)) continue;
			if (visit[map[dy][dx] - 'A']) continue;
			find(dy, dx, cnt + 1);
		}
		visit[map[y][x] - 'A'] = false;
		
	}
	
	
		
	
	private static boolean canNotGo(int y, int x) {
		return (y < 1 || y > R || x < 1 || x > C);
	}

}
