import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
		
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		int a = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());
		int diff = a - b;
		if (diff > 0) System.out.println(">");
		else if (diff < 0) System.out.println("<");
		else System.out.println("==");

		
	}
}
