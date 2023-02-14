import java.io.*;
import java.util.*;

// DP

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int N;

    static int[] D;

    static int count;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        D = new int[1_000_001];
    }

    static void pro() throws IOException {
        System.out.println(dp());
    }

    static int dp() {
        D[1] = 1;
        D[2] = 2;

        if (N < 3) {
            return D[N];
        }

        for (int K = 3; K <= N; K++) {
            D[K] = (D[K - 1] + D[K - 2]) % 15746;
        }

        return D[N];
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}
