import java.io.*;
import java.util.*;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();

	static int N, ans;
	static Stack<Integer> stack = new Stack<>();

	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		
		for (int i = 0; i < N; i++) {
			stack.push(Integer.parseInt(br.readLine()));
		}
	}

	
	public static void pro() {
		ans = 1;
		int top = stack.pop();
		while (!stack.isEmpty()) {
			int newTop = stack.pop();
			if (newTop > top) {
				ans++;
				top = newTop;
			}
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
