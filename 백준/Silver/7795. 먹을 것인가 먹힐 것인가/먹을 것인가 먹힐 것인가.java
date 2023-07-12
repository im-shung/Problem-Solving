import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int T, N, M;
    static int[] A, B;
    private static void input() throws IOException {
        st = new StringTokenizer(br.readLine());
        T = Integer.parseInt(st.nextToken());
    }

    private static void pro() throws IOException {
        int answer;
        for (int t = 0; t < T; t++) {
            answer = 0;
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            A = new int[N];
            B = new int[M];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                A[i] = -Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < M; i++) {
                B[i] = -Integer.parseInt(st.nextToken());
            }

            Arrays.sort(A);
            Arrays.sort(B);

            for (int i = 0; i < N; i++) {
                for(int j = 0; j < M; j++) {
                    if (-A[i] > -B[j]) {
                        answer += M - j;
                        break;
                    }
                }
            }
            System.out.println(answer);
        }

    }

    public static void main(String[] args) throws Exception {
        //br = new BufferedReader(new FileReader("src/input.txt"));
        /* 입력 */
        input();
        /* 처리 */
        pro();
        /* 출력 */
        //System.out.println(answer);
    }
}
