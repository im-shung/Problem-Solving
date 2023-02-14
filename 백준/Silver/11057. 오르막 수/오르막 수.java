import java.io.*;
import java.util.*;

// DP

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int N;
    static int[][] D;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        D = new int[N + 1][10];

        System.out.println(dp());
    }

    static int dp() {
        // 숫자 길이가 1일 때, 오르막 수는 모두 1이다.
        for (int i = 0; i <= 9; i++) {
            D[1][i] = 1;
        }

        if (N > 1) {
            // 숫자의 길이가 2~N일 때,
            // D[N][K] = D[N-1][K] + D[N-1][K+1] + ... + D[N-1][9]
            int sum;
            for (int n = 2; n <= N; n++) {
                for (int k = 0; k <= 9; k++) {
                    sum = 0;
                    for (int p = k; p <= 9; p++) {
                        sum += D[n - 1][p];
                    }
                    D[n][k] = sum % 10_007;
                }
            }
        }

        int ans = (Arrays.stream(D[N]).sum()) % 10_007;
        return ans;
    }
}
