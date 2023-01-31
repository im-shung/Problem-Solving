/*
티떱숲의 지도는 R행 C열로 이루어져 있다.
비어있는 곳은 '.'로 표시되어 있고, 물이 차있는 지역은 '*', 돌은 'X'로 표시되어 있다. 비버의 굴은 'D'로, 고슴도치의 위치는 'S'로 나타내어져 있다.

매 분마다 고슴도치는 현재 있는 칸과 인접한 네 칸 중 하나로 이동할 수 있다. (위, 아래, 오른쪽, 왼쪽)
물도 매 분마다 비어있는 칸으로 확장한다.
물이 있는 칸과 인접해있는 비어있는 칸(적어도 한 변을 공유)은 물이 차게 된다.
물과 고슴도치는 돌을 통과할 수 없다.
또, 고슴도치는 물로 차있는 구역으로 이동할 수 없고, 물도 비버의 소굴로 이동할 수 없다.

티떱숲의 지도가 주어졌을 때, 고슴도치가 안전하게 비버의 굴로 이동하기 위해 필요한 최소 시간을 구하는 프로그램을 작성하시오.

고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다. 즉, 다음 시간에 물이 찰 예정인 칸으로 고슴도치는 이동할 수 없다. 이동할 수 있으면 고슴도치가 물에 빠지기 때문이다.
-> 물이 차있는 지역은 '*'을 큐에 먼저 넣으면 해결된다.
 */

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static final int[] MX = {-1, 1, 0, 0};

    static final int[] MY = {0, 0, 1, -1};

    static int R, C;

    static char[][] map;

    static int[][] dp;

    static Deque<Point> queue;

    static Point beaver;

    static int result = 0;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());

        queue = new ArrayDeque<>();

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        map = new char[R][C];
        dp = new int[R][C];

        for (int i = 0; i < R; i++) {
            String line = br.readLine();
            for (int j = 0; j < C; j++) {
                map[i][j] = line.charAt(j);
            }
        }

    }

    static void pro() {
        // 매 턴마다 이동하는 '물'과 '고슴도치'를 큐에 삽입한다.
        // 물은 큐의 앞단(addFirst)에 삽입하고 고슴도치는 큐의 뒷단(addLast)에 삽입한다.
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (map[i][j] == '*') {
                    queue.addFirst(new Point(i, j, map[i][j]));
                } else if (map[i][j] == 'S') {
                    queue.addLast(new Point(i, j, map[i][j]));
                } else if (map[i][j] == 'D') {
                    beaver = new Point(i, j, map[i][j]);
                }
            }
        }

        bfs();
    }

    static void bfs() {
        boolean foundAnswer = false;

        while (!queue.isEmpty()) {

            // 1. 큐에서 꺼냄 -> 물(*) 또는 고슴도치(S)
            Point p = queue.pollFirst();

            // 2. 목적지인가? -> 고슴도치가 'D'에 도달했는가
            if (p.type == 'D') {
                System.out.println(dp[p.y][p.x]);
                foundAnswer = true;
                break;
            } else {
                // 3. 연결된 곳 순회

                for (int d = 0; d < 4; d++) {
                    int dy = p.y + MY[d];
                    int dx = p.x + MX[d];
                    // 4. 갈 수 있는가?(공통) -> 맵을 벗어나지 않고
                    if (0 <= dy && dy < R && 0 <= dx && dx < C) {
                        if (p.type == '.' || p.type == 'S') {
                            // 4. 갈 수 있는가?(고슴도치) -> ., D, 방문체크
                            if ((map[dy][dx] == '.' || map[dy][dx] == 'D') && dp[dy][dx] == 0) {
                                // 체크인(고슴도치) -> dp
                                dp[dy][dx] = dp[p.y][p.x] + 1;
                                // 6. 큐에 넣음
                                queue.addLast(new Point(dy, dx, map[dy][dx]));
                            }
                        }
                        else if (p.type == '*') {
                            // 4. 갈 수 있는가?(물) -> ., S
                            if (map[dy][dx] == '.' || map[dy][dx] == 'S') {
                                map[dy][dx] = '*';
                                queue.addLast(new Point(dy, dx, '*'));
                            }
                        }
                    }
                }
            }
        }
        if (!foundAnswer) {
            System.out.println("KAKTUS");
        }
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }
}

class Point {

    int y;

    int x;

    char type;

    public Point(int y, int x, char type) {
        this.y = y;
        this.x = x;
        this.type = type;
    }

    @Override
    public String toString() {
        return "Point{" +
                       "y=" + y +
                       ", x=" + x +
                       ", type=" + type +
                       '}';
    }
}
