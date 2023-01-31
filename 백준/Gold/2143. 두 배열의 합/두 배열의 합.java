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

    static int[] inputA, inputB;

    static Long[] subA, subB;

    static void input() throws IOException {
        T = Integer.parseInt(br.readLine());

        N = Integer.parseInt(br.readLine());
        inputA = new int[N];
        subA = new Long[(N * (N + 1)) / 2];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            inputA[i] = Integer.parseInt(st.nextToken());
        }

        M = Integer.parseInt(br.readLine());
        inputB = new int[M];
        subB = new Long[(M * (M + 1)) / 2];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            inputB[i] = Integer.parseInt(st.nextToken());
        }
    }

    static void pro() {
        // 부 배열 만들기
        makeSubArray();

        Arrays.sort(subA); // A의 부 배열을 오름차순 정렬
        Arrays.sort(subB, Comparator.reverseOrder()); // B의 부 배열을 내림차순 정렬

        // 포인터
        int ptA = 0;
        int ptB = 0;

        long result = 0;
        while (true) {
            long currentA = subA[ptA];
            long target = T - currentA;

            if (subB[ptB] > target) {
                ptB++;
            } else if (subB[ptB] < target) {
                ptA++;
            } else { // target == subB[ptB]
                long countA = 0;
                long countB = 0;

                while (ptA < subA.length && subA[ptA] == currentA) {
                    ptA++;
                    countA++;
                }

                while(ptB < subB.length && subB[ptB] == target) {
                    ptB++;
                    countB++;
                }

                result += countA * countB;
            }

            if (ptA == subA.length || ptB == subB.length) {
                break;
            }
        }

        System.out.println(result);
    }

//    static void pro2() {
//        List<Long> subA = new ArrayList<>();
//        List<Long> subB = new ArrayList<>();
//
//        for (int i = 0; i < N; i++) {
//            long sum = inputA[i];
//            subA.add(sum);
//            for (int j = i + 1; j < N; j++) {
//                sum += inputA[j];
//                subA.add(sum);
//            }
//        }
//
//        for (int i = 0; i < M; i++) {
//            long sum = inputB[i];
//            subB.add(sum);
//            for (int j = i + 1; j < M; j++) {
//                sum += inputB[j];
//                subB.add(sum);
//            }
//        }
//
//        Collections.sort(subA);
//        Collections.sort(subB, Comparator.reverseOrder());
//
//        long result = 0;
//        int ptA = 0, ptB = 0;
//
//        while (true) {
//            long currentA = subA.get(ptA);
//            long target = T - currentA;
//            if (subB.get(ptB) > target) {
//                ptB++;
//            } else if (subB.get(ptB) < target) {
//                ptA++;
//            } else { // target == currentB
//                long countA = 0;
//                long countB = 0;
//                while (ptA < subA.size() && subA.get(ptA) == currentA) {
//                    ptA++;
//                    countA++;
//                }
//                while (ptB < subB.size() && subB.get(ptA) == target) {
//                    ptB++;
//                    countB++;
//                }
//
//                result += countA * countB;
//            }
//
//            if (ptA == subA.size() || ptB == subB.size()) {
//                break;
//            }
//        }
//    }

    static void makeSubArray() {
        int count = 0;
        // P1 만들기
        for (int i = 0; i < N; i++) {
            long sum = inputA[i];
            for (int j = i; j < N; j++) {
                if (i == j) {
                    subA[count++] = sum;
                } else {
                    sum += inputA[j];
                    subA[count] = sum;
                    if (count < subA.length - 1) {
                        count++;
                    }
                }
            }
        }

        // P2 만들기
        count = 0;
        for (int i = 0; i < M; i++) {
            long sum = inputB[i];
            for (int j = i; j < M; j++) {
                if (i == j) {
                    subB[count++] = sum;
                } else {
                    sum += inputB[j];
                    subB[count] = sum;
                    if (count < subB.length - 1) {
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

