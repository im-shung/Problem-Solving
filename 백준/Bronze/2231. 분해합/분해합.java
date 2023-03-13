import java.io.*;
import java.util.*;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();

	static int N;
	static int ans = 1_000_999;

	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
	}

	public static void pro() throws Exception {
		for (int x = 1; x <= N; x++) {
			
			int temp = x;
			int sum = x;
			while (temp > 0) {
				sum += temp % 10;
				temp /= 10;
			}

			if (sum == N)
				ans = Math.min(ans, x);
		}
	}

	public static void main(String[] args) throws Exception {
		/* 입력 */
		input();
		/* 처리 */
		pro();
		/* 출력 */
		System.out.println(ans == 1_000_999 ? 0 : ans);
		br.close();
	}
}
