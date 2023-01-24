import java.io.*;
import java.util.*;

public class Main {

    private static final int MODULER = 10_007;
    private static final int SIZE = 1_000;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int N;
    static int[] memo;

    static void input() throws IOException {
       st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        memo = new int[SIZE + 1];
    }

    static void pro() {
        System.out.println(dp());
    }

    static int dp() {
        memo[1] = 1;
        memo[2] = 2;

        if (N <= 2) {
            return memo[N];
        }

        for (int n = 3; n <= N; n++) {
            memo[n] = memo[n - 1] + memo[n - 2];
            memo[n] %= MODULER;
        }

        return memo[N];
    }


    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}
