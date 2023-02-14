import java.io.*;
import java.util.*;

// DP

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int N, K;

    static int[][] D;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        D = new int[K + 1][N + 1];
    }

    static void pro() throws IOException {
        System.out.println(dp());
    }

    static int dp() {
        for (int n = 0; n <= N; n++) {
            D[1][n] = 1;
        }

        for (int k = 1; k <= K; k++) {
            D[k][0] = 1;
        }

       for (int k = 1; k <= K; k++) {
           for (int n = 1; n <= N; n++) {
               D[k][n] = (D[k][n - 1] + D[k - 1][n]) % 1_000_000_000;
           }
       }

       return D[K][N];
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}
