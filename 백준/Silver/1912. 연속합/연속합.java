import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static StringTokenizer st;

    static StringBuilder sb = new StringBuilder();

    static int N;
    static int[] input;
    static int[] dp;

    static void input() throws IOException {

        N = Integer.parseInt(br.readLine());

        input = new int[N];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            input[i] = Integer.parseInt(st.nextToken());
        }
    }

    private static void pro() {
        // -1,000 <= 입력 값 <= 1,000
        // 따라서 dp 초기화는 -1,000 보다 더 작은 숫자로 해야함
        dp = new int[N];
        Arrays.fill(dp, Integer.MIN_VALUE);

        dp[0] = input[0];

        for (int i = 1; i < N; i++) {
            // input[i]의 입장에서 dp[i - 1]을 포함하는 것이 이득인지 이득이 아닌지 판단한다.
            dp[i] = Math.max(dp[i - 1] + input[i], input[i]);
        }
        System.out.println(Arrays.stream(dp).max().getAsInt());
    }


    public static void main(String[] args) throws IOException {
        input();
        pro();
    }
}
