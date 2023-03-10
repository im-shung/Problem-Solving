import java.io.*;
import java.util.*;

class Node {
	int x; // row
	int y; // column

	public Node(int x, int y) {
		this.x = x;
		this.y = y;
	}

	@Override
	public String toString() {
		return "Node [x=" + x + ", y=" + y + "]";
	}

}

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();

	static int N, M;
	static char[] A, answer;
	static boolean[] visit;

	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		answer = new char[N];

		st = new StringTokenizer(br.readLine());
		A = new char[M];
		visit = new boolean[M];
		for (int i = 0; i < M; i++) {
			A[i] = st.nextToken().charAt(0);
		}
		Arrays.sort(A);
	}

	public static void dfs(int len, int idx) {
		if (len == N) {
			int mCount = 0, jCount = 0;
			for (char a : answer) {
				if (a == 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u')
					mCount++;
				else
					jCount++;
			}
			if (mCount >= 1 && jCount >= 2)
				sb.append(answer).append("\n");
		} else {
			for (int x = idx; x < M; x++) {
				if (!visit[x]) {
					visit[x] = true;
					answer[len] = A[x];
					dfs(len + 1, x);
					visit[x] = false;
				}
			}
		}
	}
	
	public static void pro() {
		dfs(0, 0);
	}

	public static void main(String[] args) throws IOException {
		/* 입력 */
		input();
		/* 처리 */
		pro();
		/* 출력 */
		System.out.println(sb);
	}
}
