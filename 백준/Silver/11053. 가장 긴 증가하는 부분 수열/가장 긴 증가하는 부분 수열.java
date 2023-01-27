import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int N;
    static int[] seq, dp;
    static int result = 0;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        seq = new int[N];
        dp = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            seq[i] = Integer.parseInt(st.nextToken());
        }
    }

    static void pro() {
        dp();
        System.out.println(result);
    }

    static void dp() {
        for (int i = 0; i < N; i++) {
            // 모든 부분수열의 길이는 '최소한 1 이상'
            dp[i] = 1;

            // 0 ~ i 이전 원소들 탐색
            for (int j = 0; j < i; j++) {

                // j번째 원소가 i번째 원소보다 작으면서 i번째 dp가 j번째 dp+1 값보다 작은경우
                if (seq[i] > seq[j] && dp[i] < dp[j] + 1) {
                    dp[i] = dp[j] + 1;
                }
            }
        }
        result = Arrays.stream(dp).max().getAsInt();
    }


    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}
