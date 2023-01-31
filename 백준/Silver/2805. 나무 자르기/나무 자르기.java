/*
목재절단기는 다음과 같이 동작한다.
먼저, 상근이는 절단기에 높이 H를 지정해야 한다. 높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다.
그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다. 따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다.

상근이는 환경에 매우 관심이 많기 때문에, 나무를 필요한 만큼만 집으로 가져가려고 한다.
이때, 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시
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

    static int[] trees;

    static int max;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        trees = new int[N];

        st = new StringTokenizer(br.readLine());

        max = 0;
        for (int i = 0; i < N; i++) {
            trees[i] = Integer.parseInt(st.nextToken());
            max = Math.max(max, trees[i]);
        }
    }

    static void pro() {
        int s = 0, e = max, mid = 0, result = 0;

        while (true) {
            mid = (s + e) / 2;
            long sum = calc(mid);
            if (sum == M) {
                result = mid;
                break;
            } else if (sum < M) {
                e = mid - 1;
            } else { // sum > M
                result = mid; // sum == M이 없는 경우를 대비한다.
                s = mid + 1;
            }

            // s == e의 경우는 의미가 있다.
            if (s > e) {
                break;
            }
        }
        System.out.println(result);
    }

    static long calc(int value) {
        long result = 0;
        for (int tree : trees) {
            if (tree > value) {
                result += tree - value;
            }
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }
}

