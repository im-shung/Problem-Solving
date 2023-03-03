import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		String line = br.readLine().strip();
		int count = 0;
		for (String str : line.split(" ")) {
			if (str != "") count++;
		}
		System.out.println(count);
	}
}