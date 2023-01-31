/*
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다.
이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
 */

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int N, M;

    static int[] A;

    static int count = 0;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        A = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
    }

    static void pro() {
        int left = 0;
        int right = 0;
        int sum = A[left];

        while (true) {
            if (sum == M) {
                count++;
                sum -= A[left++];
            } else if(sum < M) {
                if (right == N - 1) {
                    System.out.println(count);
                    break;
                }
                sum += A[++right];
            } else {
                sum -= A[left++];
            }
        }
    }


    public static void main(String[] args) throws IOException {
        input();
        pro();
    }
}

