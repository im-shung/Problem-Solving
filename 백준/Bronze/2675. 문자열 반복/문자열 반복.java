import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			st = new StringTokenizer(br.readLine());
			int R = Integer.parseInt(st.nextToken());
			String words = st.nextToken();
			for (int i = 0; i < words.length(); i++) {
				char c = words.charAt(i);
				for (int j = 0; j < R; j++) {
					sb.append(c);
				}
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}
}
