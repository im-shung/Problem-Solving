import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
		
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		int a = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());
		sb.append(a + b).append("\n")
		.append(a - b).append("\n")
		.append(a * b).append("\n")
		.append(a / b).append("\n")
		.append(a % b);
		
		System.out.println(sb);
	}
}
