import java.io.*;
import java.util.*;

// 가장 긴 + 연속적인 증가 수열 

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	public static void main(String[] args) throws IOException {
		
		int N = Integer.parseInt(br.readLine());
		int[] dp = new int[N + 1];
		
		int max = 0;
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			int val = Integer.parseInt(st.nextToken());
			dp[val] = dp[val - 1] + 1;
			max = Math.max(max, dp[val]);
		}
		System.out.println(N - max);
		
	}
}
