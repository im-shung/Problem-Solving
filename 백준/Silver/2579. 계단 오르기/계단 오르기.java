import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int N;
    static int[] arr;
    static int[] dp;
    static int result = 0;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        arr = new int[301];
        dp = new int[301];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
    }

    static void pro() {
        dp();
        System.out.println(result);
    }
   
    static void dp() {
        /* n < 3 */
        // dp[0] 일 경우는 1칸을 갔을 경우이다. ➔ 1칸을 가기위해서는 단 하나의 경우 밖에없다.
        dp[0] = arr[0];

        // dp[1] 일 경우는 2칸을 갔을 경우이다.➔ 2칸을 가기위해서는 1칸+1칸 갔을 경우와 한번에 2칸을 갔을 경우로 나눌수 있다. 이 두경우 중 최대값을 저장한다.
        dp[1] = Math.max(arr[0] + arr[1], arr[1]);

        // dp[2] 일 경우는 3칸을 갔을 경우이다.➔ 3칸을 가기위해서는 1칸+2칸 갔을 경우와 2칸+1칸 갔을 경우로 나눌수 있다. 이 두경우 중 최대값을 저장한다.
        dp[2] = Math.max(arr[0] + arr[2], arr[1] + arr[2]);

        /* n >= 3 */
        // dp[n] = max( 이전 계단을 밟지 않고 온 경우 || 이전 계단을 밟고 온 경우 )
        // dp[n] = max( dp[n-2] + array[n]|| dp[n-3] + array[n] + array[n-1] )
        for (int n = 3; n < N; n++) {
            dp[n] = Math.max(dp[n - 3] + arr[n] + arr[n - 1], dp[n - 2] + arr[n]);
        }

        result = dp[N - 1];
    }


    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}
