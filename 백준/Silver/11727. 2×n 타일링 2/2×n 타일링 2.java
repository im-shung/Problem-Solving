import java.io.*;
import java.util.*;

// DP

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int N;
    static int[] D;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        D = new int[N + 2];

        dp();
        System.out.println(D[N]);
    }

    static void dp() {
        // 초기값
        D[1] = 1;
        D[2] = 3;

        if (N >= 3) {
            // 점화식
            for (int i = 3; i <= N; i++) {
                D[i] = (D[i - 1] + 2 * D[i - 2]) % 10_007;
            }
        }

    }
}
