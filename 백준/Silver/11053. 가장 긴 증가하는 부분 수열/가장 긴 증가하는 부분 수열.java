import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int N;

    static int[] seq;
    static int[] dp;

    static void input() throws IOException {
//        br = new BufferedReader(new FileReader("src/input.txt"));

        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        seq = new int[N];
        dp = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            seq[i] = Integer.parseInt(st.nextToken());
        }

    }

    static void pro() throws IOException {
        for (int i = 0; i < N; i++) {
            dp[i] = 1;
            for (int j = 0; j < i ; j++) {
                if (seq[j] < seq[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }
        System.out.println(Arrays.stream(dp).max().getAsInt());
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}


