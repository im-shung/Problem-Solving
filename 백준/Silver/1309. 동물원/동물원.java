import java.io.*;
import java.util.*;

// DP

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int N;
    static int[][] D;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        D = new int[100_001][3];

        System.out.println(dp());
    }

    static int dp() {
        // 첫번째 행에 올 수 있는 사자 배치
        D[1][0] = 1; // ox
        D[1][1] = 1; // xo
        D[1][2] = 1; // xx

        for (int n = 2; n <= N; n++) {
            // n번째 행에 올 수 있는 사자 배치 
            D[n][0] = D[n - 1][1] + D[n - 1][2];
            D[n][1] = D[n - 1][0] + D[n - 1][2];
            D[n][2] = D[n - 1][0] + D[n - 1][1] + D[n - 1][2];
            
            D[n][0] %= 9901;
            D[n][1] %= 9901;
            D[n][2] %= 9901;
        }
        
        int ans = (D[N][0] + D[N][1] + D[N][2]) % 9901;
        return ans;
    }
}
