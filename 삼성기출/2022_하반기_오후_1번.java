import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

class Node {
    int x; // row
    int y; // column

    public Node(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public String toString() {
        return "Node [x=" + x + ", y=" + y + "]";
    }

}

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int[][] D = { { -1, 0 }, { 0, -1 }, { 0, 1 }, { 1, 0 } };

    static final int BLANK = 0;
    static final int CAMP = 1;
    static final int CLOSE = 2;

    static Node[] persons;
    static Node[] px;

    static int[][] map; // map := 빈칸, 편의점, 베이스캠프 폐쇄 체크용
    static int[][] step; // step := 최단 거리 기록용
    static boolean[][] visit;

    static int N, M, t, end;

    static void input() throws IOException {
        br = new BufferedReader(new FileReader("src/input.txt"));
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][N];
        step = new int[N][N];
        visit = new boolean[N][N];
        for (int x = 0; x < N; x++) {
            st = new StringTokenizer(br.readLine());
            for (int y = 0; y < N; y++) {
                map[x][y] = Integer.parseInt(st.nextToken());
            }
        }
        px = new Node[M];
        persons = new Node[M];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken()) - 1;
            int y = Integer.parseInt(st.nextToken()) - 1;
            px[i] = new Node(x, y);
        }
    }

    public static void printMap(int[][] map) {
        System.out.println("======================");
        for (int x = 0; x < N; x++) {
            for (int y = 0; y < N; y++) {
                System.out.print(map[x][y] + " ");
            }
            System.out.println();
        }
        System.out.println("======================");
    }

    public static boolean cannotGo(int dx, int dy) {
        return (dx < 0 || dy < 0 || dx >= N || dy >= N);
    }

    // 편의점이 시작점!! 완전 탐색!!
    public static void bfs(Node start) {
        Deque<Node> que = new ArrayDeque<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                visit[i][j] = false;
                step[i][j] = Integer.MAX_VALUE;
            }
        }
        que.add(start);
        visit[start.x][start.y] = true;
        while (!que.isEmpty()) {
            Node cur = que.poll();
            for (int i = 0; i < 4; i++) {
                int dx = cur.x + D[i][0];
                int dy = cur.y + D[i][1];
                // 갈 수 있는가? -> map 외부 x, 이미방문 x, 폐쇄된 편의점 x, 폐쇄된 베이스캠프 x
                if (cannotGo(dx, dy))
                    continue;
                if (visit[dx][dy] || map[dx][dy] == CLOSE)
                    continue;
                // 체크인
                visit[dx][dy] = true;
                step[dx][dy] = step[cur.x][cur.y] + 1;
                que.add(new Node(dx, dy));
            }
        }
    }

    static void move(int num) {
        Node dest = px[num];
        int min = N * N + 2;
        int nx = 0, ny = 0;
        // 거리가 최소인 방향으로 이동한다. 방향우선순위는 북(-1,0) 서(0,-1) 동(0,1) 남(1,0) 순이다.
        for (int i = 0; i < 4; i++) {
            int dx = persons[num].x + D[i][0];
            int dy = persons[num].y + D[i][1];
            if (cannotGo(dx, dy))
                continue;
            if (map[dx][dy] == CLOSE)
                continue;
            // 편의점에 도달하면, 편의점은 폐쇄되고, end카운트를 증가한다.
            if (dx == dest.x && dy == dest.y) {
                map[dx][dy] = CLOSE;
                end += 1;
                persons[num] = null;
                return;
            }
            if (min > step[dx][dy]) {
                min = step[dx][dy];
                nx = dx;
                ny = dy;
            }
        }
        persons[num].x = nx;
        persons[num].y = ny;
    }

    public static void pro() {
        boolean theEnd = false;
        while (true) {
            // 격자 안에 사람이 있는가? -> que 에 있는 사람들을 1칸 이동시키자.
            for (int i = 0; i < M; i++) {
                if (persons[i] == null)
                    continue;

                // 편의점으로부터의 거리를 구하자.
                bfs(px[i]);

                // 상하좌우 중 어디로 이동할 것인가? -> 최단거리로 갈 수 있는 방향
                move(i);

                if (end == M){
                    theEnd = true;
                    break;
                }
            }

            if (theEnd) break;

            // t번째사람을 격자 안에 넣자.
            if (t < M) {
                // 편의점과 가까운 베이스캠프를 찾자.
                bfs(px[t]);
                int minDest = N * N + 2;
                int nx = 0, ny = 0;
                for (int x = 0; x < N; x++) { // 열과 행이 작은 순
                    for (int y = 0; y < N; y++) {
                        if (map[x][y] == CAMP && minDest > step[x][y]) {
                            minDest = step[x][y];
                            nx = x;
                            ny = y;
                        }
                    }
                }
                persons[t] = new Node(nx, ny);
                // 베이스캠프 폐쇄
                map[nx][ny] = CLOSE;
            }
            t += 1;
        }
    }

    public static void main(String[] args) throws IOException {
        /* 입력 */
        input();
        /* 처리 */
        pro();
        /* 출력 */
        System.out.println(++t);
    }
}