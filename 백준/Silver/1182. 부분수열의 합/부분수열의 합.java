import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	static int N, S, ans;
	static int[] A;

	public static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		S = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(br.readLine());
		A = new int[N];
		for (int i = 0; i < N; i++) {
			A[i] = Integer.parseInt(st.nextToken());
		}
	}

	public static void pro() {
		// i = 0은 공집합이므로 i는 1부터 시작한다.
		for (int i = 1; i < (1<<N); i++) {
			int sum = 0;
			for (int j = 0; j < N; j++) {
				if ((i & (1 << j)) > 0)
					sum += A[j];
			}
			if (sum == S) 
				ans += 1;
		}
	}

	public static void main(String[] args) throws IOException {
		/* 입력 */
		input();
		/* 처리 */
		pro();
		/* 출력 */
		System.out.println(ans);
	}
}
