import java.io.*;
import java.util.*;

public class Main {

    private static final int[] BASKET = {5, 3};

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
        int result = getBasket();
        if (result> 9999) {
            System.out.println(-1);
        } else {
            System.out.println(result);
        }
    }

    /*
    1kg에 대한 최적해 -> (선택)2kg에 대한 최적해 -> (선택)3kg에 대한 최적해
     */
    static int getBasket() {
        for (int n = 1; n <= N; n++) {
            int min = 9999;
            for (int basket : BASKET) {
                if (n >= basket) {
                    int ret = memo[n - basket];
                    min = Math.min(min, ret);
                }
                memo[n] = min + 1;
            }
        }
        return memo[N];
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}
