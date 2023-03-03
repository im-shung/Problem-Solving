import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	public static void main(String[] args) throws IOException {
		int N = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		int min = Integer.MAX_VALUE;
		int max = Integer.MIN_VALUE;
		for (int i = 0; i < N; i++) {
			int val = Integer.parseInt(st.nextToken());
			if (min > val) {
				min = val;
            }
			if (max < val) {
				max = val;
			}
		}
		System.out.println(min + " " + max);
	}
}
