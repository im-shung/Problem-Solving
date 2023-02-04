import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int N;

    static int[] input;
    static long[] dp;

    static void input() throws IOException {
        N = Integer.parseInt(br.readLine());
        input = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            input[i] = Integer.parseInt(br.readLine());
        }
    }

    static void pro() throws IOException {
        if (N == 1) {
            System.out.println(input[1]);
        } else if (N == 2) {
            System.out.println(input[1] + input[2]);
        } else {
            dp();
            System.out.println(Arrays.stream(dp).max().getAsLong());
        }
    }

    static void dp() {
        dp = new long[N + 1];
        dp[1] = input[1];
        dp[2] = input[1] + input[2];
        for (int i = 3; i <= N; i++) {
            dp[i] = Math.max(input[i] + input[i - 1] + dp[i - 3], input[i] + dp[i - 2]);
            dp[i] = Math.max(dp[i], dp[i - 1]);
        }
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}


