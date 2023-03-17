import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	
	static final int SIZE = 19;
	static final int B = 1;
	static final int W = 2;
	static final int E = 0;
	
	static int[][] DIR = {{0, 1}, {1, 1}, {1, 0}, {1, -1}};
	
	static int[][] map = new int[SIZE][SIZE];
	static boolean[][][] visit = new boolean[SIZE][SIZE][4];
	
	static int[] answer = {-1, -1, -1};
	static boolean winFlag;
	
	public static void main(String[] args)  throws Exception {
		/* 입력 */
		for (int y = 0; y < SIZE; y++) {
			st = new StringTokenizer(br.readLine());
			for (int x = 0; x < SIZE; x++) {
				map[y][x] = Integer.parseInt(st.nextToken());
			}
		}
		
		pro();
		
		/* 출력 */
		if (winFlag) {
			sb.append(answer[2]).append("\n")
			.append(++answer[0]).append(" ").append(++answer[1]);
			System.out.println(sb);
		}
		else 
			System.out.println(0);

	}
	
	public static void pro() {
		for(int y = 0; y < SIZE; y++) {
			for (int x = 0; x < SIZE; x++) {
				if (map[y][x] != E) {
					find(y, x);
					if(winFlag) return;
				}
			}
		}
	}
	
	public static void find(int y, int x) {
		for (int d = 0; d < 4; d++) {
			if (!visit[y][x][d]) {
				answer[0] = y; answer[1] = x; answer[2] = map[y][x];
				count(map[y][x], y, x, d, 1);
				if (!winFlag) {
					answer[0] = -1; answer[1] = -1;
				} else {
					if (d == 3) {
						answer[0] += 4;
						answer[1] -= 4;
					}
					return;
				}
			}
		}
	}
	
	// 그래프 탐색  
	public static void count(int val, int y, int x, int d, int cnt) {

		if (map[y][x] != val || visit[y][x][d]) return;
		winFlag = cnt == 5 ? true : false;
		visit[y][x][d] = true;
		int dy = y + DIR[d][0];
		int dx = x + DIR[d][1];
		if (cannotGo(dy, dx) || visit[dy][dx][d]) return;
		
//		System.out.println("y=" + y +", x=" + x + ", d=" + d);
//		System.out.println("cnt=" + cnt  + "\n");
		
		// 간다.
		count(val, dy, dx, d, cnt + 1);
	}

	private static boolean cannotGo(int y, int x) {
		return (y < 0 || x < 0 || y >= SIZE || x >= SIZE);
	}
	
}
