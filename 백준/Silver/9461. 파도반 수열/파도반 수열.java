import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static final int N = 100;

    static int T;

    static long[] dp = new long[101];


    static void input() throws IOException {
        T = Integer.parseInt(br.readLine());
    }

    static void pro() throws IOException {
        dp();

        for (int i = 0; i < T; i++) {
            int n = Integer.parseInt(br.readLine());
            sb.append(dp[n]).append("\n");
        }

        System.out.println(sb);
    }

    static void dp() {
        dp[1] = 1;
        dp[2] = 1;
        dp[3] = 1;
        dp[4] = 2;
        dp[5] = 2;

        for (int i = 6; i <= N; i++) {
            dp[i] = dp[i - 1] + dp[i - 5];
        }
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}
