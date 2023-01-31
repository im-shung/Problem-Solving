import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Objects;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int T, N, M;

    static int[] A, B;

    static Long[] P1, P2;

    static void input() throws IOException {
//        br = new BufferedReader(new FileReader(new File("src/sds/input.txt")));
        T = Integer.parseInt(br.readLine());

        N = Integer.parseInt(br.readLine());
        A = new int[N];
        P1 = new Long[(N * (N + 1)) / 2];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        M = Integer.parseInt(br.readLine());
        B = new int[M];
        P2 = new Long[(M * (M + 1)) / 2];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }


    }

    static void pro() {
        // 부 배열 만들기
        makeSubArray();

        Arrays.sort(P1, Comparator.naturalOrder()); // A의 부 배열을 오름차순 정렬
        Arrays.sort(P2, Comparator.reverseOrder()); // B의 부 배열을 내림차순 정렬

        // 포인터
        int p1 = 0;
        int p2 = 0;

        long result = 0;
        while (true) {
            long sum = P1[p1] + P2[p2];
            if (sum == T) {
                // 배열에서 동일값의 개수
                // 정렬되어있기 떄문에 찾기 쉽다.
                long idxA = getCount(p1, P1);
                long idxB = getCount(p2, P2);

                // 부 배열 쌍의 개수를 더한다.
                result += idxA * idxB;

                // 동일값의 개수만큼 점프한다.
                p1 += idxA;
                p2 += idxB;
            } else if (sum > T) {
                p2 += 1;
            } else { // sum < T
                p1 += 1;
            }

            if (p1 == P1.length || p2 == P2.length) {
                break;
            }
        }

        System.out.println(result);
    }

    private static int getCount(int p, Long[] I) {
        int idx = 1;
        while ((p + idx < I.length) && Objects.equals(I[p], I[p + idx])) {
            idx++;
        }
        return idx;
    }

    static void makeSubArray() {
        int count = 0;
        // P1 만들기
        for (int i = 0; i < N; i++) {
            long sum = A[i];
            for (int j = i; j < N; j++) {
                if (i == j) {
                    P1[count++] = sum;
                } else {
                    sum += A[j];
                    P1[count] = sum;
                    if (count < P1.length - 1) {
                        count++;
                    }
                }
            }
        }

        // P2 만들기
        count = 0;
        for (int i = 0; i < M; i++) {
            long sum = B[i];
            for (int j = i; j < M; j++) {
                if (i == j) {
                    P2[count++] = sum;
                } else {
                    sum += B[j];
                    P2[count] = sum;
                    if (count < P2.length - 1) {
                        count++;
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }
}
