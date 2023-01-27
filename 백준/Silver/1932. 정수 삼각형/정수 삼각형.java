import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int N;
    static int[][] triangle, dp;
    static int result = 0;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        triangle = new int[N + 1][N + 1];
        dp = new int[N + 1][N + 1];

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= i; j++) {
                triangle[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }

    static void pro() {
        dp();
        System.out.println(result);
    }

    // h: height
    // n: index
    static void dp() {

        for (int h = 1; h <= N; h++) {
            for (int n = 1; n <= h; n++) {
                dp[h][n] = Math.max(dp[h - 1][n - 1], dp[h - 1][n]) + triangle[h][n];
            }
        }

        result = Arrays.stream(dp[N]).max().getAsInt();
    }


    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}
