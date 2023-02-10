import java.io.*;
import java.util.*;

/*
접근법
통나무 높이를 내림차순으로 정렬 
우선순위 1~5를 나열한다고 하면 (우선순위가 작을 수록 통나무 높이가 큼)
"4 2 1 3 5" 로 나열해야 가장 적은 차이로 최소값을 구할 수 있다.
index의 차이를 2로 두는 것이 포인트다. 
 */

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int T, N;

    static int[] input;

    static int result;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());

        T = Integer.parseInt(st.nextToken());
    }

    static void pro() throws IOException {
        for (int t = 0; t < T; t++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());

            input = new int[N];

            st = new StringTokenizer(br.readLine());
            for (int n = 0; n < N; n++) {
                input[n] = Integer.parseInt(st.nextToken());
            }

            input = Arrays.stream(input).sorted().toArray();
            result = 0;
            for (int n = 2; n < N; n++) {
                result = Math.max(input[n] - input[n - 2], result);
            }
            sb.append(result).append("\n");
        }
        System.out.println(sb);
    }


    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}


