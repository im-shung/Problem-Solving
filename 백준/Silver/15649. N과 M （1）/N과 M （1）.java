import java.io.*;
import java.util.*;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int N, M;
	static int[] answer;
	static boolean[] checked;

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		answer = new int[M];
		checked = new boolean[N + 1];
		perm(0);
		System.out.println(sb);
	}

	private static void perm(int cnt) {
		if (cnt == M) {
			for (int a : answer) {
				sb.append(a).append(" ");
			}
			sb.append("\n");
			return;
		}
		for (int i = 1; i <= N; i++) {
			if (!checked[i]) {
				checked[i] = true;
				answer[cnt] = i;
				perm(cnt + 1);
				checked[i] = false;
			}
		}
	}

}
