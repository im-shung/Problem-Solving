import java.io.*;
import java.util.*;

// 최단 경로
/*
        // 주난이가 점프를 하면 상하좌우로 파동이 퍼진다. (1에서 0으로 바뀐다.)
        // 한 번의 점프는 한 겹의 친구들을 쓰러뜨린다
        // 한 겹을 체크하기 위해 도착한 위치가 몇번째 점프인지 체크해야 한다.
        // 최단 경로를 찾기 위해 우선순위 큐를 사용한다.
 */

class Location implements Comparable<Location>{

    static final int[] DY = {-1, 1, 0, 0};
    static final int[] DX = {0, 0, -1, 1};

    int y;
    int x;
    int time;

    public Location(int y, int x, int time) {
        this.y = y;
        this.x = x;
        this.time = time;
    }

    @Override
    public int compareTo(Location o) {
        return this.time - o.time;
    }

    @Override
    public String toString() {
        return "Location{" +
                       "y=" + y +
                       ", x=" + x +
                       ", time=" + time +
                       '}';
    }
}

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int N, M;
    static char[][] map;
    static boolean[][] visit;
    static int x1, y1, x2, y2;
    static int ans;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new char[N][M];
        visit = new boolean[N][M];

        st = new StringTokenizer(br.readLine());
        y1 = Integer.parseInt(st.nextToken()) - 1;
        x1 = Integer.parseInt(st.nextToken()) - 1;
        y2 = Integer.parseInt(st.nextToken()) - 1;
        x2 = Integer.parseInt(st.nextToken()) - 1;

        for (int i = 0; i < N; i++) {
           String line = br.readLine();
            for (int j = 0; j < M; j++) {
                map[i][j] = line.charAt(j);
            }
        }
        
        System.out.println(bfs());

    }

    static int bfs() {
        PriorityQueue<Location> queue = new PriorityQueue<>();
        queue.add(new Location(y1, x1, 0));

        while (!queue.isEmpty()) {
            // 큐에서 꺼냄
            Location current = queue.poll();

            // 연결된 곳인가?
            for (int i = 0; i < 4; i++) {
                int dy = current.y + Location.DY[i];
                int dx = current.x + Location.DX[i];

                // 갈 수 있는가?
                if (0 <= dy && dy < N && 0 <= dx && dx < M) {
                    if (visit[dy][dx]) continue;
                    // 체크인
                    visit[dy][dx] = true;

                    // 목적지인가?
                    if (map[dy][dx] == '#') {
                        return current.time + 1;
                    }
                    else if (map[dy][dx] == '0') {
                        queue.add(new Location(dy, dx, current.time));
                    } else if (map[dy][dx] == '1') {
                        map[dy][dx] = '0';
                        queue.add(new Location(dy, dx, current.time + 1));
                    }
                }
            }
        }
        return 0;
    }
}
