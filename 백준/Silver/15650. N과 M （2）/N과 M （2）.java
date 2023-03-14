import java.io.*;
import java.util.*;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int N, M;
	static int[] answer;

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		answer = new int[M];
		comb(0, 1);
		System.out.println(sb);
	}

	// cnt := cnt번째 카드 뽑기
	private static void comb(int cnt, int startIndex) {
		if (cnt == M) {
			for (int a : answer)
				sb.append(a).append(" ");
			sb.append("\n");
			return;
		}
		for (int i = startIndex; i <= N; i++) {
			answer[cnt] = i;
			comb(cnt + 1, i + 1);
		}
	}

}
