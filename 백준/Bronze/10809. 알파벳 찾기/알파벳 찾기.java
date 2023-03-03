import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		String line = br.readLine();
		int[] alphabet = new int[26];
		for (int i = 0; i < alphabet.length; i++) {
			alphabet[i] = -1;
		}
		
		for (int i = 0; i < line.length(); i++) {
			if (alphabet[line.charAt(i) - 'a'] == -1) {
				alphabet[line.charAt(i) - 'a'] = i;
			} 
		}
		
		for (int i = 0; i < alphabet.length; i++) {
			sb.append(alphabet[i]).append(" ");
		}
		System.out.println(sb);
		
	}
}
