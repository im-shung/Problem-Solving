import java.io.*;
import java.util.*;

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
    static PriorityQueue<Node> priorityQue = new PriorityQueue<>();
    static int[] ans;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        ans = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            que.add(new Node(Integer.parseInt(st.nextToken()), i));
        }
    }

    public static void pro() {
        Node pre = que.peekLast();

        // idx = N ~ 1 순서로 원소를 꺼낸다.
        while (!que.isEmpty()) {
            Node cur = que.pollLast();

            // idx탑이 idx+1탑보다 크다면, idx+1탑의 신호를 수신한 탑은 idx이다.
            // idx탑이 idx+1탑보다 작다면, priorityQue에 넣는다.
            if (cur.height > pre.height) {
                ans[pre.idx] = cur.idx;
            } else {
                priorityQue.add(pre);
            }

            // priorityQue는 자신보다 높은 탑을 찾지 못한 원소들이 들어있다. 
            // priorityQue에 원소가 있고, 현재 높이가 원소 높이보다 크면 현재idx를 기록한다.
            while (priorityQue.size() > 0 && priorityQue.peek().height < cur.height) {
                Node node = priorityQue.poll();
                ans[node.idx] = cur.idx;
            }

            // 현재 탑보다 높으면서, 인덱스가 가장 가까운 탑을 찾는다.
            pre = cur;
        }

        // priorityQue에 원소가 남아있다면, 자신보다 높은 탑이 없다는 것이므로 0을 기록한다.
        while (!priorityQue.isEmpty()) {
            Node node = priorityQue.poll();
            ans[node.idx] = 0;
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