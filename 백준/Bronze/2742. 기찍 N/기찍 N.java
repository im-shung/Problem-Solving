import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		int N = Integer.parseInt(br.readLine());		
	
		for (int i = N; i >= 1; i--) {
			sb.append(i).append("\n");
		}
		System.out.println(sb);
	}
}
