import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		/*
			|\_/|
			|q p|   /}
			( 0 )"""\
			|"^"`    |
			||_/=\\__|
		 */
		sb.append("|\\_/|").append("\n")
		.append("|q p|   /}").append("\n")
		.append("( 0 )\"\"\"\\").append("\n")
		.append("|\"^\"`    |").append("\n")
		.append("||_/=\\\\__|");
		System.out.println(sb);
	}
}
