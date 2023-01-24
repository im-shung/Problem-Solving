import java.io.*;
import java.util.*;

public class Main {

    private static final int SIZE = 40;
    private static final int[] num = {0, 1};

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int T, N;
    static int[][] memo;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());

        T = Integer.parseInt(st.nextToken());
        memo = new int[SIZE + 1][2];
    }

    static void pro() throws IOException {
        fibo();
        
        for (int t = 0; t < T; t++) {
            N = Integer.parseInt(br.readLine());
            System.out.println(memo[N][0] +" " + memo[N][1]);
        }
    }

    static void fibo() {
        memo[0][0] = 1;
        memo[1][1] = 1;
        for (int n = 2; n <= SIZE; n++) {
            for (int i : num) {
                memo[n][i] = memo[n - 1][i] + memo[n - 2][i];
            }
        }
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}
