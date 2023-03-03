import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
		
	public static void main(String[] args) throws IOException {
		int dan = Integer.parseInt(br.readLine());
		for (int i = 1; i <= 9; i++) {
			sb.append(dan).append(" * ").append(i).append(" = ").append(dan * i).append("\n");
		}
		System.out.println(sb);
	}
}
