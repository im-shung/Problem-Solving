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

	}

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();

	static Deque<Node> que = new ArrayDeque<>();
	static int[][] DIR = { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };

	static int N, M;
	static int[][] arr;
	static boolean[][] visit;
	static int cnt;

	public static void main(String[] args) throws Exception {
		/* 입력 */
//		br = new BufferedReader(new FileReader("src/input.txt"));
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		arr = new int[N][M];
		visit = new boolean[N][M];
		for (int i = 0; i < N; i++) {
			String str = br.readLine();
			for (int j = 0; j < M; j++) {
				arr[i][j] = str.charAt(j) - '0'; // '1' - '0' = 1
			}
		}
		/* 처리 */
		pro();

		/* 출력 */

	}

	public static void bfs() {
		que.add(new Node(0, 0, 1));
		visit[0][0] = true;

		while (!que.isEmpty()) {
			Node curr = que.poll();
			if (curr.y == N - 1 && curr.x == M - 1) {
				System.out.println(curr.cnt);
				return;
			}
			for (int i = 0; i < 4; i++) {
				int dy = curr.y + DIR[i][0];
				int dx = curr.x + DIR[i][1];

				if (dy < 0 || dx < 0 || dy >= N || dx >= M)
					continue;
				if (visit[dy][dx])
					continue;
				if (arr[dy][dx] == 0)
					continue;
				visit[dy][dx] = true;
				que.add(new Node(dy, dx, curr.cnt + 1));
			}
		}
	}

	public static void pro() {
		bfs();
	}

}
