import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		char[] arrA = st.nextToken().toCharArray();
		char[] arrB = st.nextToken().toCharArray();
		
		char[] reversedA = new char[3];
		char[] reversedB = new char[3];
		
		for (int i = 2; i >= 0; i--) {
			reversedA[2 - i] = arrA[i];
			reversedB[2 - i] = arrB[i];
		}
		int a = Integer.parseInt(new String(reversedA));
		int b = Integer.parseInt(new String(reversedB));
		System.out.println(Math.max(a, b));
		
	}
}
