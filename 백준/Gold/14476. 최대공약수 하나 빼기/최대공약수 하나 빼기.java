import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static StringTokenizer st;

    static int N;

    static int[] input, left, right;

    static int max, result, target;

    static void input() throws IOException {
//        br = new BufferedReader(new FileReader(new File("src/input.txt")));

        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        input = new int[N];
        left = new int[N];
        right = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            input[i] = Integer.parseInt(st.nextToken());
        }
    }

    private static void pro() {
        // 누적합
        // left는 {1, 1~2, 1~3, ... ,1~N} 의 최대공약수를 가지는 배열
        // right는 {1~N, 2~N, 3~N, ... ,N} 의 최대공약수를 가지는 배열
        left[0] = input[0];
        for (int i = 1; i < N - 1; i++) {
            left[i] = gcd(left[i - 1], input[i]);
        }
        right[N - 1] = input[N - 1];
        for (int i = N - 2; i >= 0; i--) {
            right[i] = gcd(right[i + 1], input[i]);
        }

        // N개의 정수 중 i번째 정수(K)를 뺐을 때, 나머지 N -1 개의 최대공약수가 가장 커지는 것을 찾아라.
        // 이때, 최대공약수는 K의 약수가 되면 안 된다.
        max = 0;
        result = 0;
        for (int k = 0; k < N; k++) {
            if (k == 0) {
                result = right[k + 1];
            } else if (k == N - 1) {
                result = left[k - 1];
            } else {
                result = gcd(left[k - 1], right[k + 1]);
            }

            if (input[k] % result != 0) {
                max = Math.max(result, max);
                target = input[k];
            }
        }
        StringBuilder sb = new StringBuilder();
        if (max == 0) {
            System.out.println(-1);
        } else {
            sb.append(max).append(" ").append(target);
            System.out.println(sb);
        }

    }

    static int gcd(int a, int b) {
        // gcd(a, b) = gcd(b, a % b)
        // a % b 가 0일 때 return b
        while (b != 0) {
            int r = a % b;
            a = b;
            b = r;
        }
        return a;
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}
