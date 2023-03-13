import java.io.*;
import java.util.*;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();

	static int N, M;
	static int[] A;
	static boolean[] V;
	static int ans;

	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		A = new int[N];
		V = new boolean[N];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < A.length; i++) {
			A[i] = Integer.parseInt(st.nextToken());
		}
	}

	public static void dfs(int x, int len, int sum) {
		if (len == 3) {
			if (sum <= M) ans = Math.max(ans, sum);
		}
		else {
			for(int i = x; i < N; i++) {
				if (!V[i]) {
					V[i] = true;
					dfs(i, len + 1, sum + A[i]);
					V[i] = false;
				}
			}
		}
	}
	
	public static void pro() throws Exception {
		dfs(0, 0, 0);
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
