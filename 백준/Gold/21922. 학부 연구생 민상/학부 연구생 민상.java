import java.io.*;
import java.util.*;

/*
 * 핵심
 * 이번 문제에서는 2가지 체크 배열이 필요하다.
 * 1. 바람 방향 체크: 인접 노드 방문이 바람 방향에 따라 달라진다. 따라서 바람 방향 기록용으로 wind를 두었다. wind[y][x] = {방향 값}
 * 2. 방문 체크: 앉을 수 있는 칸을 셀 때, 바람 방향에 따라 앉았던 칸을 다시 방문할 수 있다. 따라서 중복 카운트 방지용으로 visit을 두었다.
 */

public class Main {

	static class Node {

		int y;
		int x;

		int dir;

		public Node(int y, int x, int dir) {
			this.y = y;
			this.x = x;
			this.dir = dir;
		}

		@Override
		public String toString() {
			return "Node{" + "y=" + y + ", x=" + x + ", dir=" + dir + '}';
		}
	}

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();

	// 화살표 방향이 UP, DOWN, LEFT, RIGHT
	static int[][] DIR = { {}, { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
	static final int U = 1;
	static final int D = 2;
	static final int L = 3;
	static final int R = 4;

	static Deque<Node> que = new ArrayDeque<>();
	static int N, M;
	static int[][] map;
	static int[][][] wind;
	static boolean[][] visit;
	static int ans;

	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		map = new int[N][M];
		wind = new int[N][M][5];
		visit = new boolean[N][M];

		for (int y = 0; y < N; y++) {
			st = new StringTokenizer(br.readLine());
			for (int x = 0; x < M; x++) {
				map[y][x] = Integer.parseInt(st.nextToken());
				// 에어컨이면 상하좌우 칸을 큐에 삽입합니다.
				if (map[y][x] == 9) {
					checkAndCount(y, x);
					for (int i = 1; i <= 4; i++) {
						int dy = y + DIR[i][0];
						int dx = x + DIR[i][1];
						if (cannotGo(dy, dx) || wind[dy][dx][i] == i || map[dy][dx] == 9)
							continue;
						// wind에 방향 표시!!
						wind[dy][dx][i] = i;
						checkAndCount(dy, dx);
						que.add(new Node(dy, dx, i));
					}

				}
			}
		}
	}

	public static void checkAndCount(int y, int x) {
		if (!visit[y][x]) ++ans;
		visit[y][x] = true;
	}
	
	public static boolean cannotGo(int y, int x) {
		return (y < 0 || x < 0 || y >= N || x >= M);
	}
	
    public static void printMap(int[][][] map) {
        System.out.println("========================");
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                System.out.print(Arrays.toString(map[i][j]) + " ");
            }
            System.out.println();
        }
    }

	public static void bfs() {
		while (!que.isEmpty()) {
			Node cur = que.poll();
//			System.out.println(cur);
//			printMap(wind);
			int K = map[cur.y][cur.x];

			int dy = cur.y;
			int dx = cur.x;
			int ddir = 0;

			// 방향을 설정합니다. 
			if (K == 3) {
				if (cur.dir == L) {
					ddir = D;
				} else if (cur.dir == R) {
					ddir = U;
				} else if (cur.dir == U) {
					ddir = R;
				} else if (cur.dir == D) {
					ddir = L;
				}
			} else if (K == 4) {
				if (cur.dir == L) {
					ddir = U;
				} else if (cur.dir == R) {
					ddir = D;
				} else if (cur.dir == U) {
					ddir = L;
				} else if (cur.dir == D) {
					ddir = R;
				}
			} else {
				if (K == 1 && (cur.dir == L || cur.dir == R))
					continue;
				if (K == 2 && (cur.dir == U || cur.dir == D))
					continue;
				ddir = cur.dir;
			}

			// 방향에 따라 dy, dx를 설정합니다.
			dy += DIR[ddir][0];
			dx += DIR[ddir][1];
			// 맵을 벗어나는 경우 
			if (cannotGo(dy, dx))
				continue;
			// 같은 방향으로 이미 방문한 경우
			if (wind[dy][dx][ddir] == ddir)
				continue;
			checkAndCount(dy, dx);
			if (map[dy][dx] == 0)
				visit[dy][dx] = true;
	
			// visit에 방향 표시!!
			wind[dy][dx][ddir] = ddir;
			que.add(new Node(dy, dx, ddir));
		}
	}

	public static void pro() throws Exception {
		bfs();
	}

	public static void main(String[] args) throws Exception {
		/* 입력 */
		input();
		/* 처리 */
		pro();
		/* 출력 */
		System.out.println(ans);
	}
}
