import java.io.*;
import java.util.*;

// DP

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int N;
    static long[] D;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        D = new long[N + 1];

        dp();
        System.out.println(D[N]);
    }

    static void dp() {
        D[0] = 0;
        D[1] = 1;

        for (int i = 2; i <= N; i++) {
            D[i] = D[i - 1] + D[i - 2];
        }
    }
}
