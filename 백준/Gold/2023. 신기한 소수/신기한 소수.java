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
    static int[] answer;
    static boolean[][] visit;

    public static void main(String[] args) throws Exception {
        /* 입력 */
        N = Integer.parseInt(br.readLine());
        answer = new int[N];
        visit = new boolean[N][10];
        /* 처리 */
        for (int i = 0; i < 4; i++) {
            answer[0] = primeNumbers[i];
            find(1, answer[0]);
        }

        /* 출력 */
        System.out.println(sb);
    }

    private static void find(int cnt, int num) {
//        System.out.println("answer = " + Arrays.toString(answer));

        if (cnt == N) {
            sb.append(num).append("\n");
            return; // 까먹지 말기!!!!!
        }

        int x;
        for (int i = 0; i <= 9; i++) {
            x = num * 10;
            if (!visit[cnt][i]) {
                visit[cnt][i] = true;
                answer[cnt] = i;
                x += i;
//                System.out.println("num = " + x);
                if (isPrimeNumber(x)) find(cnt + 1, x );
                visit[cnt][i] = false;
            }
        }
    }

    private static boolean isPrimeNumber(int x) {
        for (int n = 2; n < x; n++) {
            if (x % n == 0) {
                return false;
            }
        }
        return true;
    }

}