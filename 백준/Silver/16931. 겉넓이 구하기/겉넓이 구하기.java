import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int N, M;
    static int[][] map;
    static int ans;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[N + 2][M + 2];

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 위와 아래
        ans = N * M * 2;

        // 동
        for (int i = N; i > 0; i--) {
            for (int j = 1; j <= M; j++) {
                int diff = map[i][j] - map[i + 1][j];
                if (diff > 0) {
                    ans += diff;
                }
            }
        }

        // 서
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= M; j++) {
                int diff = map[i][j] - map[i - 1][j];
                if (diff > 0) {
                    ans += diff;
                }
            }
        }

        // 남
        for (int j = 1; j <= M; j++) {
            for (int i = 1; i <= N; i++) {
                int diff = map[i][j] - map[i][j - 1];
                if (diff > 0) {
                    ans += diff;
                }
            }
        }

        // 북
        for (int j = M; j > 0 ; j--) {
            for (int i = 1; i <= N; i++) {
                int diff = map[i][j] - map[i][j + 1];
                if (diff > 0) {
                    ans += diff;
                }
            }
        }

        System.out.println(ans);

    }


}
