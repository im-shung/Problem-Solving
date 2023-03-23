import java.io.*;
import java.util.*;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb;

	static int N;
	static int[] move;
	static int ans;

	private static void input() throws IOException {
		
		N = Integer.parseInt(br.readLine());
		move = new int[N + 1];
		Arrays.fill(move, -1);
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int num = Integer.parseInt(st.nextToken());
			int moving = Integer.parseInt(st.nextToken());
			if ((move[num] == 0 && moving == 1) || (move[num] == 1 && moving == 0)) {
				ans++;
			}
			move[num] = moving;
		}
	}

	
	private static void pro() {
	}

	public static void main(String[] args) throws Exception {
		/* 입력 */
		input();
		/* 처리 */
		pro();
		/* 출력 */
		System.out.println(ans);
		br.close();
	}
}