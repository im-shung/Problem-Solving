import java.awt.Point;
import java.io.*;
import java.text.ParseException;
import java.util.*;

/*
Graph & Search
격자형 그래프
그래프는 정점과 간선을 가지는 자료구조이다.
Vertex(정점): 게임구역 칸
Edge(간선): 오른쪽, 아래쪽 방향 * 게임 구역 칸의 값(이동할 수 있는 칸 개수)
 */

public class Main {

    static int[] dr = {1, 0};
    static int[] dc = {0, 1};

    static int N;
    static int[][] matrix;
    static boolean[][] visit;

    public static void main(String[] args) throws IOException, ParseException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        matrix = new int [N + 1][N + 1];
        visit = new boolean [N + 1][N + 1];

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= N; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        String message = "Hing";
        if (bfs (1, 1)) { // ‘쩰리’가 출발점 (1,1)부터 게임 구역을 탐색한다.
            message = "HaruHaru";
        }
        System.out.println(message);

    }

    // ‘쩰리’가 끝 점에 도달할 수 있으면 true 리턴, 아니면 false 리턴
    static boolean bfs(int x, int y) {
        Queue<Point> queue = new LinkedList<>();

        queue.add(new Point(x, y));
        visit[x][y] = true;

        while (!queue.isEmpty()) {
            Point vertex =  queue.poll();
            int movingValue = matrix[vertex.x][vertex.y];

            // ‘쩰리’가 끝 점에 도달 완료
            if (movingValue == -1) {
                return true;
            }

            for (int i = 0; i < 2; i++) {
                // 탐색할 수 있는 칸은 오른쪽, 아래쪽 방향 * 게임 구역 칸의 값(이동할 수 있는 칸 개수)
                Point next = new Point(vertex.x + (dr[i] * movingValue), vertex.y + (dc[i] * movingValue));

                // 갈 수 있는 칸인가??
                if (next.x < 1 || next.y < 1 || next.x > N || next.y > N)
                    continue;

                // 이미 방문한 칸인가??
                if (visit[next.x][next.y])
                    continue;

                // next 칸은 다른 칸으로 이동할 수 있는 칸인가??
                if (matrix[next.x][next.y] == 0)
                    continue;
                
                queue.add(next);

            }
        }
        return false;
    }

}
