import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		boolean[] namugi = new boolean[42];
		for (int i = 0; i < 10; i++) {
			int N = Integer.parseInt(br.readLine());		
			namugi[N % 42] = true;
		}
		int count = 0;
		for (boolean b : namugi) {
			if (b == true) count++;
		}
		System.out.println(count);
	}
}
