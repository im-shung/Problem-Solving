import java.io.*;
import java.util.*;

// DFS

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int N;
    static int[][] map;
    static boolean[] column = new boolean[15]; // 열
    static boolean[] leftDi = new boolean[30]; // 왼쪽 대각선
    static boolean[] rightDi = new boolean[30]; // 오른쪽 대각선
    static int ans;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        dfs(1);
        System.out.println(ans);
    }

    static void dfs(int r) {

        // 목적지인가? - 마지막 행
        if (r == N + 1) {
            ans += 1;
        } else {

            // 갈 수 있는가?
            for (int c = 1; c <= N; c++) {
                if (column[c] || leftDi[r + c] || rightDi[r - c + N]) continue;

                // 체크인
                column[c] = true;
                leftDi[r + c] = true;
                rightDi[r - c + N] = true;

                // 간다.
                dfs(r + 1);

                // 체크아웃
                column[c] = false;
                leftDi[r + c] = false;
                rightDi[r - c  + N] = false;
            }
        }
    }
}
