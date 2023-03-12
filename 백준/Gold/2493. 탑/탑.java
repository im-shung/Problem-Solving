import java.io.*;
import java.util.*;

/*
코드 업그레이드: 스택 사용
 */
public class Main {

    static class Node implements Comparable<Node> {

        int height;
        int idx;

        public Node(int height, int idx) {
            this.height = height;
            this.idx = idx;
        }


        @Override
        public int compareTo(Node o) {
            return this.height - o.height;
        }
    }

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static int N;
    static Deque<Node> que = new ArrayDeque<>();
    static int[] ans, A;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        A = new int[N + 1];
        ans = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
    }

    public static void pro() {
        // 탑을 뒤에서부터 스택에 삽입한다.
        for (int i = N; i > 0; i--) {
            // curHeight := i번째 탑 높이
            int curHeight = A[i];
            while (!que.isEmpty()) {
                Node last = que.peekFirst();
                // i번째 탑이 i + a번째 탑보다 높으면, ans[i + a] = i 를 기록한다.
                if (curHeight >= last.height) {
                    que.pollFirst();
                    ans[last.idx] = i;
                } else { // 그렇지 않으면 break. i + a번째 탑보다 뒤에 있는 탑들은 i + a보다 높이가 높다.
                    break;
                }
            }
            // i번째 탑을 que에 삽입한다 !
            que.addFirst(new Node(curHeight, i));
        }

        for (int i = 1; i <= N; i++) {
            sb.append(ans[i]).append(" ");
        }
    }

    public static void main(String[] args) throws IOException {
        /* 입력 */
        input();
        /* 처리 */
        pro();
        /* 출력 */
        System.out.println(sb);
    }
}