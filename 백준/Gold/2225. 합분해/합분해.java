import java.io.*;
import java.util.*;

// DP

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int N, K;
    static int[][] D;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        D = new int[K + 1][N + 1];

        System.out.println(dp());
    }

    static int dp() {
        // 1개를 선택해서 N을 만드는 경우는 한 가지
        for (int n = 0; n <= N; n++) {
            D[1][n] = 1;
        }

        // 몇 개를 선택하던지 0을 만들 수 있는건 1개
        for (int k = 1; k <= K; k++) {
            D[k][0] = 1;
        }

        // K개를 사용해서 N을 만드는 경우는
        // (K-1개로 N을 만드는 경우 - 이 경우의 수에서 +0을 하면 K개로 N을 만드는 경우가 되기 때문에 경우의수가 동일함.) +
        // (K개로 N-1을 만드는 경우 - 이 경우들에서 숫자 하나만 N으로 만들수 있게 1큰수로 바꿔주면 됨.)
        // 설명 출처 - https://www.acmicpc.net/source/44927008
        for (int k = 1; k <= K; k++) {
            for (int n = 1; n <= N; n++) {
                D[k][n] = D[k][n - 1] + D[k - 1][n];
                
                if (D[k][n] > 1_000_000_000) {
                    D[k][n] -= 1_000_000_000;
                }
            }
        }

        return D[K][N];
    }
}
