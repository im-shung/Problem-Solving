import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int N;
    static int[][] matrix, dp;
    static int result = 0;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        matrix = new int[N + 1][3];
        dp = new int[N + 1][3];
        for (int t = 1; t <= N; t++) {
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < 3; i++) {
                matrix[t][i] = Integer.parseInt(st.nextToken());
            }
        }
    }

    static void pro() {
        dp();
        System.out.println(result);
    }

    static void dp() {
        for (int n = 1; n <= N; n++) {
            dp[n][0] = Math.min(dp[n - 1][1], dp[n - 1][2]) + matrix[n][0];
            dp[n][1] = Math.min(dp[n - 1][0], dp[n - 1][2]) + matrix[n][1];
            dp[n][2] = Math.min(dp[n - 1][1], dp[n - 1][0]) + matrix[n][2];

            result = Math.min(Math.min(dp[n][0], dp[n][1]), dp[n][2]);
        }
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}
