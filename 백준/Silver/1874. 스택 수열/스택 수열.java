import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

/*
조건: 스택에 1~n까지의 수를 push, push 순서는 오름차순

임의의 수열이 주어졌을 때, 스택을 이용해서 그 수열을 만들 수 있는가?
-> 있다면, push와 pop 연산의 순서를 계산
	-> push는 +, pop은 - 로 표현
-> 없다면, NO를 출력
 */
public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();

	static int N;
	static int[] A;
	static int last;
	static Stack<Integer> stack = new Stack<>();

	public static void main(String[] args) throws Exception {
		/* 입력 */
		N = Integer.parseInt(br.readLine());
		/* 처리 */
		int preNum = 1;
		boolean possible = true;

		for (int i = 0; i < N; i++) {
			int check = Integer.parseInt(br.readLine());

			/*
			 * push를 못하는 상황은 뭘까? -> push는 반드시 오름차순으로 진행된다. 이전에 push된 수는 preNum에 저장된다.
			 * (preNum > check) : push 할 수 없는 경우 (check != peek()) : pop 할 수 없는 경우
			 * (check != stack.peek()) : pop 할 수 없는 경우
			 */

			if (preNum > check && check != stack.peek()) {
				possible = false;
				break;
			}

			while (preNum <= check) {
				stack.push(preNum++);
				sb.append("+\n");
			}

			stack.pop();
			sb.append("-\n");
		}

		/* 출력 */
		if (possible)
			System.out.println(sb);
		else
			System.out.println("NO");
	}

}
