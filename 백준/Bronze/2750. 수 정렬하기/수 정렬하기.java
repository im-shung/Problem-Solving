import java.io.*;
import java.util.*;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();

	static int N;
	static int[] arr;

	static void input() throws IOException {
		N = Integer.parseInt(br.readLine());

		arr = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		br.readLine(); 
	}

	
	public static void bubbleSort() {
		// 코드 작성
		int n = arr.length;
		for (int i = 0; i <= n - 2; i++) {
			for (int j = 0; j <= n - i - 2; j++) {
				if (arr[j] > arr[j + 1]) swap(j, j + 1);
			}
		}
	}
	
	private static void swap(int i, int j) { // i, j번째 인덱스의 값 교환
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}
	public static void pro() throws Exception {
		bubbleSort();
		for (int a : arr) {
			sb.append(a).append("\n");
		}
	}

	public static void main(String[] args) throws Exception {
		/* 입력 */
		input();
		/* 처리 */
		pro();
		/* 출력 */
		System.out.println(sb);
	}
}
