import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	public static void main(String[] args) throws IOException {
		int N = Integer.parseInt(br.readLine());
		int[] scores = new int[N];
		st = new StringTokenizer(br.readLine());
		int max = -1;
		for (int i = 0; i < scores.length; i++) {
			scores[i] = Integer.parseInt(st.nextToken());
			max = Math.max(max, scores[i]);
		}
		double[] nscores = new double[N];
		double sum = 0.0;
		for (int i = 0; i < scores.length; i++) {
			nscores[i] = ((double) scores[i] / max) * 100;
			sum += nscores[i];
		}
		System.out.println(sum / N);
		
	}
}
