import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		int a = Integer.parseInt(br.readLine());		
		int b = Integer.parseInt(br.readLine());		
		int c = Integer.parseInt(br.readLine());		
		int total = a * b * c;
		
		int[] count = new int[10];
		while (total > 0) {
			count[total % 10]++;
			total /= 10;
		}
	
		for (int i = 0; i < count.length; i++) {
			sb.append(count[i]).append("\n");
		}
		System.out.println(sb);
	}
}
