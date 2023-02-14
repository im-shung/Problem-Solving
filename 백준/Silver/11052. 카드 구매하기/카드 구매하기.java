import java.io.*;
import java.util.*;

// DP

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int N;

    static int[] D, input;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        input = new int[N + 1];
        D = new int[N + 1];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            D[i] = input[i] = Integer.parseInt(st.nextToken());
        }
    }

    static void pro() throws IOException {
        System.out.println(dp());
    }

    static int dp() {
        if (N == 1) return input[1];

        for (int K = 2; K <= N; K++) {
            for (int i = K - 1; i >= K/2 ; i--) {
                D[K] = Math.max(D[K - i] + D[i], D[K]);
            }
        }
        return D[N];
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}
