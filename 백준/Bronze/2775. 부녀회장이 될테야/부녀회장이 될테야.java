import java.io.*;
import java.util.*;

public class Main {

    private static final int SIZE = 14;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int T, N, M;
    static int[][] matrix;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());

        T = Integer.parseInt(st.nextToken());
        matrix = new int[SIZE + 1][SIZE + 1];
    }

    static void pro() throws IOException {
        // 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
        for (int i = 1; i <= SIZE; i++) {
            matrix[0][i] = i;
        }

        // N층의 M호는 N층의 M-1호 + N-1층의 M호
        // 격자로 그려보면 이해가 된다.
        for (int i = 1; i <= SIZE; i++) {
            for (int j = 1; j <= SIZE; j++) {
                matrix[i][j] += matrix[i][j - 1] + matrix[i - 1][j];
            }
        }

        for (int t = 0; t < T; t++) {
            N = Integer.parseInt(br.readLine());
            M = Integer.parseInt(br.readLine());
            System.out.println(matrix[N][M]);
        }
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}
