import java.io.*;
import java.util.*;

// 이분탐색

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int N, M;
    static int[] array;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        array = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            array[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());

        // 정렬하기 !!
        Arrays.sort(array);

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            int subject = Integer.parseInt(st.nextToken());
            int result = search(subject);
            sb.append(result).append("\n");
        }
        System.out.println(sb);
    }

    private static int search(int subject) {
        int left, right, mid;

        left = 0;
        right = N - 1;

        while (left <= right) {
            mid = (left + right) / 2;

            // 찾는 대상이 중간에 있는 값보다 큰 경우
            if (array[mid] < subject) {
                // left를 중간 인덱스 다음 인덱스로 옮긴다.
                left = mid + 1;
            }
            // 찾는 대상이 중간에 있는 값보다 작은 경우
            else if (array[mid] > subject) {
                // right를 중간 인덱스 이전 인덱스로 옮긴다.
                right = mid - 1;
            }
            // 찾는 대상이 mid에 있다.
            else {
                return 1;
            }
        }
        // 못 찾고 while문을 빠져나왔다.
        return 0;
    }

}
