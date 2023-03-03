import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		int H = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		M -= 45;
		if (M < 0) {
			M += +60;
			if (H == 0) H = 23;
			else H -= 1;
		}
		System.out.println(H + " " + M);

	}
}
