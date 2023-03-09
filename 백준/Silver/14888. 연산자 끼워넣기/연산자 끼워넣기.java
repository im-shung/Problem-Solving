import java.io.*;
import java.util.*;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	static int N;
	static int[] A, visit, count;
	static int min = Integer.MAX_VALUE;
	static int max = Integer.MIN_VALUE;

	static void input() throws IOException {
		count = new int[4];
		visit = new int[4];
		N = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		A = new int[N];
		for (int i = 0; i < N; i++) {
			A[i] = Integer.parseInt(st.nextToken());
		}
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < 4; i++) {
			count[i] = Integer.parseInt(st.nextToken());
		}
	}

	public static void dfs(int idx, int result, int opCount) {
		if (opCount == N) {	
			max = Math.max(result, max);
			min = Math.min(result, min);
			return;
		} 
		for (int i = 0; i < 4; i++) {
			if (visit[i] < count[i]) {
				int temp = result;
				if (i == 0) result = result + A[idx];
				else if (i == 1) result = result - A[idx];
				else if (i == 2) result = result * A[idx];
				else result = (result < 0) ? -(-result / A[idx]) : (result / A[idx]); 
				
				// 체크인
				visit[i]++; idx++; opCount++; 
				dfs(idx, result, opCount);
				// 체크아웃
				visit[i]--; idx--; opCount--;
				result = temp;
			}
		}
	}
	
	public static void pro() {
		// idx, result, opCount
		dfs(1, A[0], 1);
	}

	public static void main(String[] args) throws IOException {
		/* 입력 */
		input();
		/* 처리 */
		pro();
		/* 출력 */
		System.out.println(max);
		System.out.println(min);
	}
}
