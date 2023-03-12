import java.io.*;
import java.util.*;

/*
j <= i 이므로
1. D[i] % M == 0 이 성립하는 i를 카운트한다.

배열의 연속된 구간(i~j)의 합: D[i] - D[j - 1]로 구할 수 있다.
모듈러 연산은 분배가 가능하기 때문에
2. (D[i] - D[j - 1]) % M = 0  ----> (D[i] % M) - (D[j - 1] % M) = 0 ----> (D[i] % M) == (D[j - 1] % M) 의 개수를 구하자.

 */
public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    //    static StringBuilder sb = new StringBuilder();
    static int N, M;
    static int[] A;
    static long[] D, modular;
    static long ans;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());

        A = new int[N + 1];
        D = new long[N + 1];
        modular = new long[M];
    }

    public static void pro() {
        for (int i = 1; i <= N; i++) {
            D[i] = (D[i - 1] + Integer.parseInt(st.nextToken())) % M;
            // 1. D[i] % M == 0 이 성립하는 i를 카운트한다.
            if (D[i] == 0) {
                ++ans;
            }
            // (D[i] % M) == (D[j - 1] % M) = x
            // 위의 식이 성립하는 x를 카운트한다. 즉 x는 M의 나머지(0~M-1)
            ++modular[(int) D[i]];
        }
        // modular[x]: x를 나머지로 하는 구간합의 개수.
        // 그 중에서 2개를 뽑는 경우의 수(nC2)를 ans에 더한다.
        // nC2 = n * (n - 1) / 2
        for (int i = 0; i < M; i++) {
            long x = modular[i];
            if (x > 0) {
                ans += x * (x - 1) / 2;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        /* 입력 */
        input();
        /* 처리 */
        pro();
        /* 출력 */
        System.out.println(ans);
    }
}