import java.io.*;
import java.util.*;

public class Main {

    private static final int N = 10;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int T;
    static int[] memo;

    static void input() throws IOException {
       st = new StringTokenizer(br.readLine());

        T = Integer.parseInt(st.nextToken());
        memo = new int[N + 1];
    }

    static void pro() throws IOException {
        dp();
        for (int t = 0; t < T; t++) {
            int n = Integer.parseInt(br.readLine());
            System.out.println(memo[n]);
        }
    }

    static void dp() {
        memo[1] = 1;
        memo[2] = 2;
        memo[3] = 4;

        for (int n = 4; n <= N; n++){
            memo[n] = memo[n - 3] + memo[n - 2] + memo[n - 1];
        }
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}
