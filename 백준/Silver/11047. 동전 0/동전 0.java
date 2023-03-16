import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	static int N, K;
	static int[] A;
	static int sum, cnt;
	
	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		A = new int[N];
		for(int i = N - 1; i >= 0; i--) {
			A[i] = Integer.parseInt(br.readLine());
		}
		pro();
		System.out.println(cnt);
	}
	
	private static void pro() {
		int i = 0;
		while (i < N) {
			if (sum + A[i] <= K) {
				sum += A[i];
				++cnt;
			} else {
				++i;
			}
		}

	}

}
