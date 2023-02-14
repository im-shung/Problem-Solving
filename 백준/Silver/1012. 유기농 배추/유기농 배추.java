import java.io.*;
import java.util.*;

// BFS

class Location {
    int y;
    int x;

    public Location(int y, int x) {
        this.y = y;
        this.x = x;
    }
}

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static final int[] DY = {-1, 1, 0, 0};
    static final int[] DX = {0, 0, -1, 1};
    static int T, R, C, K;
    static int[][] map;
    static boolean[][] visit;
    static int groupCount;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        T = Integer.parseInt(st.nextToken());

        for (int t = 0; t < T; t++) {
            st = new StringTokenizer(br.readLine());
            R = Integer.parseInt(st.nextToken());
            C = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());

            map = new int[R][C];
            visit = new boolean[R][C];

            int y, x;
            for (int k = 0; k < K; k++) {
                st = new StringTokenizer(br.readLine());
                y = Integer.parseInt(st.nextToken());
                x = Integer.parseInt(st.nextToken());
                map[y][x] = 1;
            }

            for (int r = 0; r < R; r++) {
                for (int c = 0; c < C; c++) {
                    if (map[r][c] == 1 && !visit[r][c]) {
                        groupCount++;
                        bfs(r, c);
                    }
                }
            }
            sb.append(groupCount).append("\n");
            groupCount = 0;
        }
        System.out.println(sb);
    }

    private static void bfs(int r, int c) {
        Queue<Location> queue = new ArrayDeque<>();
        queue.add(new Location(r, c));
        visit[r][c] = true;

        int y, x, dy, dx;
        while (!queue.isEmpty()) {
            // 1. 큐에서 꺼냄
            Location current = queue.poll();
            y = current.y;
            x = current.x;

            // 2. 목적지인가? - 생략

            // 3. 연결된 곳을 순회
            for (int i = 0; i < 4; i++) {
                dy = y + DY[i];
                dx = x + DX[i];

                // 4. 갈 수 있는가?
                if (0 <= dy && dy < R && 0 <= dx && dx < C) {
                    if (!visit[dy][dx] && map[dy][dx] == 1) {
                        // 5. 체크인
                        visit[dy][dx] = true;
                        // 6. 큐에 넣음
                        queue.add(new Location(dy, dx));
                    }
                }
            }
        }
    }


}
