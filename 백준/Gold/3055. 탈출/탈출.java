import java.io.*;
import java.util.*;

// BFS

class Location {

    static final int[] DY = {-1, 1, 0, 0};
    static final int[] DX = {0, 0, -1, 1};

    int y;
    int x;
    char type;
    int time;

    public Location(int y, int x, char type, int time) {
        this.y = y;
        this.x = x;
        this.type = type;
        this.time = time;
    }

    @Override
    public String toString() {
        return "Location{" +
                       "y=" + y +
                       ", x=" + x +
                       ", type=" + type +
                       '}';
    }
}

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static final char EMPTY = '.';  // 비어있음
    static final char WATER = '*';  // 물
    static final char D = 'D';      // 비버
    static final char S = 'S';      // 고슴도치
    static int R, C;
    static char[][] map;
    static boolean[][] visit;
    static Deque<Location> queue = new ArrayDeque<>();

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        map = new char[R][C];
        visit = new boolean[R][C];

        for (int y = 0; y < R; y++) {
            String line = br.readLine();
            for (int x = 0; x < C; x++) {
                map[y][x] = line.charAt(x);
            }
        }

        for (int y = 0; y < R; y++) {
            for (int x = 0; x < C; x++) {
                // bfs 초기 설정
                // 물이 고슴도치보다 먼저 이동해야하므로 큐에 먼저 넣는다.
                if (map[y][x] == WATER) {
                    queue.addFirst(new Location(y, x, WATER, 0));
                } else if (map[y][x] == S) {
                    queue.addLast(new Location(y, x, S, 0));
                    visit[y][x] = true;
                }
            }
        }

        int ans = bfs();
        if (ans > 0) {
            System.out.println(ans);
        } else {
            System.out.println("KAKTUS");
        }

    }

    private static int bfs() {
        while (!queue.isEmpty()) {
            // 1. 큐에서 꺼냄 - 물 또는 고슴도치가 꺼내진다.
            Location current = queue.pollFirst();
            int y = current.y;
            int x = current.x;
            char type = current.type;
            int time = current.time;

//            System.out.printf("%c = ", map[y][x]);
//            System.out.println(current);

            // 2. 목적지 인가? - 비버의 굴
            if (map[y][x] == D) {
                return time;
            }

            // 3. 연결된 곳인가?
            for (int i = 0; i < 4; i++) {
                int dy = y + Location.DY[i];
                int dx = x + Location.DX[i];

                // 4. 갈 수 있는가? (공통) -> 맵을 벗어나지 않고
                if (isOutOfMap(dy, dx)) continue;

                // 큐에서 꺼낸 게 물인 경우
                if (type == WATER) {

                    // 4. 갈 수 있는 가? (물) -> 비어있는 곳, 고슴도치
                    if (map[dy][dx] == S || map[dy][dx] == EMPTY) {
                        // !!! 비어있는 곳은 다음 턴에 물이 된다. !!!
                        map[dy][dx] = WATER;
                        // 5. 체크인 - 생략
                        // 6. 큐에 널음
                        queue.addLast(new Location(dy, dx, map[dy][dx], time + 1));
                    }
                }

                // 큐에서 꺼낸 게 고슴도치인 경우
                else if (type == S || type == EMPTY) {
                    if (visit[dy][dx]) continue;

                    // 4. 갈 수 있는 가? (고슴도치) -> 비어있는 곳, 비버
                    if (map[dy][dx] == D || map[dy][dx] == EMPTY) {
                        // 5. 체크인
                        visit[dy][dx] = true;
                        // 6. 큐에 널음
                        queue.addLast(new Location(dy, dx, map[dy][dx], time + 1));
                    }
                }
            }
        }
        // 비버의 집으로 도착 못한 경우
        return 0;
    }


    public static boolean isOutOfMap(int y, int x) {
        return !(0 <= y && y < R && 0 <= x && x < C);
    }

}
