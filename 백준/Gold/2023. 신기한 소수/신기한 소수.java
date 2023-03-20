import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.*;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int[] primeNumbers = {2, 3, 5, 7};

    static int N;

    public static void main(String[] args) throws Exception {
        /* 입력 */
        N = Integer.parseInt(br.readLine());
        /* 처리 */
        for (int i = 0; i < 4; i++) {
            find(1, primeNumbers[i]);
        }

        /* 출력 */
        System.out.println(sb);
    }

    private static void find(int cnt, int num) {
        if (cnt == N) {
            sb.append(num).append("\n");
            return; // 까먹지 말기!!!!!
        }

        int x;
        for (int i = 0; i <= 9; i++) {
        	x = Integer.parseInt(String.valueOf(num) + String.valueOf(i));
            if (isPrimeNumber(x)) find(cnt + 1, x);
        }
    }

    private static boolean isPrimeNumber(int x) {
        for (int n = 2; n <= Math.sqrt(x); n++) {
            if (x % n == 0) {
                return false;
            }
        }
        return true;
    }

}