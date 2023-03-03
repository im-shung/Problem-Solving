import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	public static void main(String[] args) throws IOException {
		int[] input = new int[8];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < input.length; i++) {
			input[i] = Integer.parseInt(st.nextToken());
		}
		
		String ans = "";
		for (int i = 0; i < input.length - 1; i++) {
			if (input[i] == input[i + 1] + 1) {
				ans = "descending";
			} else if (input[i] == input[i + 1] - 1) {
				ans = "ascending";
			} else {
				ans = "mixed";
				break;
			}
		}
		System.out.println(ans);
		
	}
}
