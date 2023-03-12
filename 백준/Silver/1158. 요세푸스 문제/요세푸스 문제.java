import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int N, K;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
    }

    public static void pro() {
        Deque<Integer> que = new ArrayDeque<>();
        // 1~N을 큐에 삽입한다.
        for (int i = 1; i <= N; i++) {
            que.add(i);
        }

        sb.append("<");
        // front를 pop해서 K번째 사람인지 확인한다.
        // 아니라면, 다시 큐에 삽입한다.
        // 큐에 사람이 없을 때까지 반복한다.
        int cnt = 0;
        while (!que.isEmpty()) {
            int cur = que.poll();
            if (++cnt == K) {
                sb.append(cur).append(", ");
                cnt = 0;
            } else {
                que.add(cur);
            }
        }
        int len = sb.length() - 2;
        sb.setLength(len);
        sb.append(">");
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