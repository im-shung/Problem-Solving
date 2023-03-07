import java.io.*;
import java.util.*;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int N, target;
	static int[] arr;

	public static void main(String[] args) throws Exception, IOException {
		// 입력
		N = Integer.parseInt(br.readLine());
		arr = new int[N];

		int left = 0;
		int right = -1;

		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			right = Math.max(right, arr[i]);
		}

		target = Integer.parseInt(br.readLine());

		// 처리
		while (left <= right) {
			int mid = (left + right) / 2;
			long sum = getSum(mid);

			if (sum <= target) {
				left = mid + 1; // 상한액 증가
			} else {
				right = mid - 1; // 상한액 감소
			}
		}

		// 출력
		System.out.println(right);

	}

	public static long getSum(long bound) {
		long sum = 0;
		for (int val : arr) {
			if (val > bound)
				sum += bound;
			else
				sum += val;
		}
		return sum;
	}
}
