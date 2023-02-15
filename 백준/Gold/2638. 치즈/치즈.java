import java.io.*;
import java.util.*;

// BFS 응용, 시뮬레이션

class Location {

    static final int[] DY = {-1, 1, 0, 0};
    static final int[] DX = {0, 0, -1, 1};

    int y;
    int x;

    public Location(int y, int x) {
        this.y = y;
        this.x = x;
    }

    @Override
    public String toString() {
        return "Location{" +
                       "y=" + y +
                       ", x=" + x +
                       '}';
    }
}

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static final int CHEESE = 1;
    static final int BLANK = 0;
    static final int REAL_BLANK = 2;
    static final int MELT = 3;
    static int R, C;
    static int[][] map;
    static boolean[][] visit;
    static boolean isMelt;
    static boolean isRemain;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        map = new int[R][C];
        visit = new boolean[R][C];

        // 격자형 배열 map 초기화
        for (int y = 0; y < R; y++) {
            st = new StringTokenizer(br.readLine());
            for (int x = 0; x < C; x++) {
                map[y][x] = Integer.parseInt(st.nextToken());
            }
        }

        int time = 0;
        while (true) {

            // 1. BFS - 치즈 내부/외부 공기 구분하기
            bfs(0, 0);

            // 2. 모든 치즈 칸을 조사, 한 시간에 녹는지 확인한다.
            for (int y = 0; y < R; y++) {
                for (int x = 0; x < C; x++) {
                    if (map[y][x] == CHEESE) {
                        int cnt = 0;
                        for (int i = 0; i < 4; i++) {
                            int dy = y + Location.DY[i];
                            int dx = x + Location.DX[i];
                            // 갈 수 있는 곳인가?
                            if (isOutOfMap(dy, dx)) continue;
                            // 인접한 칸이 외부 공기면, cnt + 1
                            if (map[dy][dx] == REAL_BLANK) cnt++;
                        }

                        // 녹는 대상으로 표기
                        if (cnt >= 2) {
                            isMelt = true;
                            map[y][x] = MELT;
                        }
                    } // end of if CHEESE
                }
            } // end of for문

            // 3. 녹는 대상으로 표기된 경우 외부 공기로 바꾸기
            if (isMelt) {
                for (int y = 0; y < R; y++) {
                    for (int x = 0; x < C; x++) {
                        if (map[y][x] == MELT) map[y][x] = REAL_BLANK;
                        if (map[y][x] == CHEESE) isRemain = true;
                    }
                }
            }
            
            // 4. 시간 증가
            time++;

            // 5. 치즈가 더 이상 안 남은 경우 종료
            if (!isRemain) break;
            isMelt = isRemain = false;

        } // end of While
        System.out.println(time);
    }

    private static void bfs(int r, int c) {
        // visit 초기화
        for (boolean[] v : visit) {
            Arrays.fill(v, false);
        }

        // bfs 초기 설정
        Queue<Location> queue = new ArrayDeque<>();
        queue.add(new Location(r, c));
        visit[r][c] = true;

        while (!queue.isEmpty()) {
            // 1. 큐에서 꺼냄
            Location current = queue.poll();
            int y = current.y;
            int x = current.x;
            // 2. 목적지에 도달했는가? - 생략

            // 3. 연결된 곳인가?
            for (int i = 0; i < 4; i++) {
                int dy = y + Location.DY[i];
                int dx = x + Location.DX[i];

                // 4. 갈 수 있는 곳인가?
                if (isOutOfMap(dy, dx) || visit[dy][dx]) {
                    continue;
                }

                // 인접한 칸이 치즈가 아닌 경우
                if (map[dy][dx] != CHEESE) {
                    // 외부 공기 칸임을 표시
                    map[dy][dx] = REAL_BLANK;
                    // 5. 체크인
                    visit[dy][dx] = true;
                    // 6. 큐에 넣음
                    queue.add(new Location(dy, dx));
                }
            }
        } // end of While
    }

    public static boolean isOutOfMap(int y, int x) {
        return !(0 <= y && y < R && 0 <= x && x < C);
    }

}
