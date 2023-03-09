import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N, ans;
	static boolean[] visit;

	public static void main(String[] args) throws Exception {
		N = Integer.parseInt(br.readLine());
		// 시작점
		for (int n = 1; n <= N; n++) {
			dfs(n, 0);
		}
		System.out.println(ans);
	}

	public static void dfs(int n, int sum) {
		if (sum >= N) {
			if (sum == N)
				ans++;
			return;
		}
		dfs(n + 1, sum + n);
	}
}
