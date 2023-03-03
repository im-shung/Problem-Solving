import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	public static void main(String[] args) throws IOException {
		int max = 0;
		int idx = -1;
		for (int i = 1; i <= 9; i++) {
			st = new StringTokenizer(br.readLine());
			int val = Integer.parseInt(st.nextToken());
			if (max < val) {
				max = val;
				idx = i;
			}
		}
		System.out.println(max + "\n" + idx);
	}
}
