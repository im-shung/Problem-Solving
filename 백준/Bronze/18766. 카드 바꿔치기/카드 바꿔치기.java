import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int[] R;
    static int[] Y;
    static int[] B;

    static int n, testCase;
    static StringBuilder sb = new StringBuilder();

    private static void input() throws IOException {
//        st = new StringTokenizer(br.readLine());
        // 카드 개수
        n = Integer.parseInt(br.readLine());
        R = new int[10];
        Y = new int[10];
        B = new int[10];
        // 게임 이전 카드 정보
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            String word = st.nextToken();
            if (word.charAt(0) == 'R') R[word.charAt(1) - '0']++;
            else if (word.charAt(0) == 'Y') Y[word.charAt(1) - '0']++;
            else if (word.charAt(0) == 'B') B[word.charAt(1) - '0']++;
        }

        // 게임 이후 카드 정보
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            String word = st.nextToken();
            if (word.charAt(0) == 'R') R[word.charAt(1) - '0']--;
            else if (word.charAt(0) == 'Y') Y[word.charAt(1) - '0']--;
            else if (word.charAt(0) == 'B') B[word.charAt(1) - '0']--;
        }
    }

    private static void pro() {
        boolean flag = false;
        for (int i = 0; i <= 9; i++) {
            if (R[i] != 0 || Y[i] != 0 || B[i] != 0)
            {
                flag = true;
                break;
            }
        }
        if (flag) sb.append("CHEATER\n");
        else sb.append("NOT CHEATER\n");
    }


    public static void main(String[] args) throws Exception {
        //br = new BufferedReader(new FileReader("src/input.txt"));
        testCase = Integer.parseInt(br.readLine());
        for (int t = 0; t < testCase; t++) {
            /* 입력 */
            input();
            /* 처리 */
            pro();
        }
        /* 출력 */
        System.out.println(sb);
    }
}
