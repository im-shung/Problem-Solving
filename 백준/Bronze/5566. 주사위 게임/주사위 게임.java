import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.*;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int N, M;
    static int[] board;
    static int ans;

    public static void main(String[] args) throws Exception {
        /* 입력 */
    	st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        /* 처리 */
        board = new int[N];
        for (int i = 0; i < N; i++)
        	board[i] = Integer.parseInt(br.readLine());
        int curr = 0;
        for (int j = 0; j < M; j++) {
        	int move = Integer.parseInt(br.readLine());
        	curr += move;
        	ans++;
        	if (curr >= N - 1) break;
        	curr = curr + board[curr];
            if (curr >= N - 1) break;
        }
        /* 출력 */
       System.out.println(ans);
    }



}