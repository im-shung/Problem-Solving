import java.io.*;
import java.util.*;

class Node {
    int R;
    int C;

    public Node(int r, int c) {
        super();
        R = r;
        C = c;
    }

}

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static final int EMPTY = 0;
    static final int VIRUS = 2;

    static int[] DR = { 1, -1, 0, 0 };
    static int[] DC = { 0, 0, 1, -1 };

    static int[][] MAP, BLANK;
    static boolean[][] VISIT;

    static int N, M;
    static int ANSWER;
    static int BLANK_COUNT;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        MAP = new int[N + 1][M + 1];
        BLANK = new int[N * M + 1][2];
        VISIT = new boolean[N + 1][M + 1];

        for (int R = 1; R <= N; R++) {
            st = new StringTokenizer(br.readLine());
            for (int C = 1; C <= M; C++) {
                MAP[R][C] = Integer.parseInt(st.nextToken());
            }
        }
    }

    // 바이러스 퍼뜨리기!!
    public static void bfs() {
        Deque<Node> que = new ArrayDeque<>();
        // 모든 바이러스가 시작점으로 가능하니까, 전부 큐에 넣어준다.
        for (int R = 1; R <= N; R++) {
            for (int C = 1; C <= M; C++) {
                VISIT[R][C] = false;
                if (MAP[R][C] == VIRUS) {
                    que.add(new Node(R, C));
                    VISIT[R][C] = true;
                }
            }
        }
        // BFS 과정
        while (!que.isEmpty()) {
            // 1. 큐에서 꺼냄
            Node cur = que.poll();
            // 2. 목적지인가?
            // 3. 연결된 곳인가?
            for (int i = 0; i < 4; i++) {
                int NR = cur.R + DR[i];
                int NC = cur.C + DC[i];
                // 4. 갈 수 있는가? -> 맵 벗어나면 x, 방문했다면 x, 빈 칸이 아니면 x
                if (NR < 1 || NC < 1 || NR > N || NC > M) continue;
                if (VISIT[NR][NC]) continue;
                if(MAP[NR][NC] != EMPTY) continue;
                // 5. 체크인
                VISIT[NR][NC] = true;
                // 6. 큐에 넣음
                que.add(new Node(NR, NC));
            }
        }
        // 탐색이 종료된 시점이니, 안전 영역의 넓이를 계산하고, 정답을 갱신한다.
        int count = 0;
        for (int R = 1; R <= N; R++) for (int C = 1; C <= M; C++) if (MAP[R][C] == EMPTY && !VISIT[R][C]) count++;
        ANSWER = Math.max(ANSWER, count);
    }

    // idx 번째 빈 칸에 벽을 세울 지 말 지 결정해야 하고, 이 전까지 selected_cnt 개의 벽을 세웠다.
    static void dfs(int idx, int selected_cnt) {
        // 3 개의 벽을 모두 세운 상태
        if (selected_cnt == 3) {
            bfs();
            return;
        }
        // 더 이상 세울 수 있는 벽이 없는 상태
        if (idx > BLANK_COUNT) return;

        MAP[BLANK[idx][0]][BLANK[idx][1]] = 1;
        dfs(idx + 1, selected_cnt + 1);

        MAP[BLANK[idx][0]][BLANK[idx][1]] = 0;
        dfs(idx + 1, selected_cnt);
    }

    public static void pro() {
        // 모든 벽의 위치를 먼저 모아놓자.
        for (int R = 1; R <= N; R++) {
            for (int C = 1; C <= M; C++) {
                if (MAP[R][C] == EMPTY) {
                    BLANK_COUNT++;
                    BLANK[BLANK_COUNT][0] = R;
                    BLANK[BLANK_COUNT][1] = C;
                }
            }
        }
        // 벽을 3개 세우는 모든 방법을 확인해보자!
        dfs(1, 0);
    }

    public static void main(String[] args) throws IOException {
        /* 입력 */
        input();
        /* 처리 */
        pro();
        /* 출력 */
        System.out.println(ANSWER);
    }
}