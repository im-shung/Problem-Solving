import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int N;
    static int[] memo;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        memo = new int[N + 1];
    }

    static void pro() {
        int result = dp();
        System.out.println(result);
    }

    static int dp() {
        if (N == 1) return 0;
        memo[0] = Integer.MAX_VALUE;
        memo[1] = 0;
        memo[2] = 1;

        for (int n = 3; n <= N; n++){
            int min = (int) 1e7;
            if (n % 3 == 0) {
                min = Math.min(min, memo[n/3]);
            }
            if (n % 2 == 0) {
                min = Math.min(min, memo[n/2]);
            }
            min = Math.min(min, memo[n - 1]);

            memo[n] =  min + 1;
        }
        return memo[N];
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}
