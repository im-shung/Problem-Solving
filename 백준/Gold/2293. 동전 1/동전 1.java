import java.io.*;
import java.util.*;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	static int N, money;
	static Integer[] coins;
	static int[] dp;

	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		money = Integer.parseInt(st.nextToken());
		coins = new Integer[N];
		dp = new int[money + 1];
		for (int i = 0; i < N; i++) {
			coins[i] = Integer.parseInt(br.readLine());
		}
		// 오름차순 정렬합니다. --사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.
//		Arrays.sort(coins);
//		System.out.println(Arrays.toString(coins));
	}

	public static void pro() {
		dp[0] = 1;
		for (int coin : coins) {
			for (int k = coin; k <= money; k++) {
				dp[k] += dp[k - coin];
//				System.out.println(Arrays.toString(dp));
			}

		}

//		System.out.println(Arrays.toString(dp));
	}

	public static void main(String[] args) throws IOException {
		//br = new BufferedReader(new FileReader("src/input.txt"));
		/* 입력 */
		input();
		/* 처리 */
		pro();
		/* 출력 */
		System.out.println(dp[money]);
	}
}
