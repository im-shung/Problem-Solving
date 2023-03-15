import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();

	static final int S = 0;
	static final int T = 1;

	static int N;
	static int[][] input;
	static long minDiff = Long.MAX_VALUE;

	static boolean[] isSelected;

	public static void main(String[] args) throws Exception, IOException {
		N = Integer.parseInt(br.readLine());
		input = new int[N][2];
		isSelected = new boolean[N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			input[i][S] = Integer.parseInt(st.nextToken());
			input[i][T] = Integer.parseInt(st.nextToken());
		}
		subSum(0, 0);
		System.out.println(minDiff);
	}

	// 신맛: 곱, 쓴맛: 합
	// cnt := cnt번째 재료
	private static void subSum(int cnt, int len) {
		// 마지막 재료까지 탐색한 후, 선택된 재료들의 신맛과 쓴맛의 차이를 구하라.
		if (cnt == N) {
			if (len == 0) return;
			long tasteS = 1, taseteT = 0;
			for (int i = 0; i < N; i++) {
				if (isSelected[i]) {
					tasteS *= input[i][S];
					taseteT += input[i][T];
				}
			}
			long curDiff = Math.abs(tasteS - taseteT);
			if (curDiff < minDiff)
				minDiff = curDiff;
			return;
		}

		isSelected[cnt] = true;
		subSum(cnt + 1, len + 1);

		isSelected[cnt] = false;
		subSum(cnt + 1, len);
	}

}
