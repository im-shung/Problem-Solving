import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.*;
import java.util.StringTokenizer;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();

	static int T, N, M;
	static String X, Y;
	static int[] board;

	public static void main(String[] args) throws Exception {
		/* 입력 */
		T = Integer.parseInt(br.readLine());
		while (--T >= 0) {
			int ans = 0;
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			X = "";
			Y = "";
			// String : X
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < M; i++) {
				X = String.valueOf(X + +Integer.parseInt(st.nextToken()));
			}
			// String : Y
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < M; i++) {
				Y = String.valueOf(Y + +Integer.parseInt(st.nextToken()));
			}
//            System.out.println("x = " + X);
//            System.out.println("y = " + Y);
			board = new int[N];
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				board[i] = Integer.parseInt(st.nextToken());
			}

			/* 처리 */
			String startValue = "";
			int end = M - 1;
			for (int i = 0; i <= end; i++) {
				startValue = String.valueOf(startValue + board[i]);
			}
			if (isPossible(startValue))
				ans++;
			
			int len = N;
			while (--len > 0) {
				end = (end + 1) % N;
				startValue = String.valueOf(startValue.substring(1) + board[end]);
				if (isPossible(startValue))
					ans++;
			}
		
			/* 출력 */
			System.out.println(ans);
		}
	}
	
	private static boolean isPossible(String Z) {
		int z = Integer.parseInt(Z);
		return Integer.parseInt(X) <= z && z <= Integer.parseInt(Y);
	}
}