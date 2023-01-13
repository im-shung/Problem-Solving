import java.awt.Point;
import java.io.*;
import java.text.ParseException;
import java.util.*;

/*
Graph & Search
격자형 그래프
그래프는 정점과 간선을 가지는 자료구조이다.
Vertex(정점): 흰색 격자들
Edge(간선): 상하좌우로 인접한 흰색 격자들
 */

public class Main {

    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, 1, -1};

    static int N, M;
    static int[][] matrix;
    static boolean[][] visit;

    public static void main(String[] args) throws IOException, ParseException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        matrix = new int [N][M];
        visit = new boolean [N][M];

        for (int i = 0; i < N; i++) {
            String[] line = br.readLine().split("");
            for (int j = 0; j < M; j++) {
                matrix[i][j] = Integer.parseInt(line[j]);
            }
        }

        String result = "NO";
        for (int i = 0; i < M; i++) {
            if (matrix[0][i] == 0 && !visit[0][i]) {
                if (bfs(0, i)){
                    result = "YES";
                    break;
                }
            }
        }
        System.out.println(result);

    }

    // 전류가 안쪽까지 전달되면 true 리턴, 아니면 false 리턴
    static boolean bfs(int x, int y) {
        Queue<Point> queue = new LinkedList<>();

        queue.add(new Point(x, y));
        visit[x][y] = true;

        while (!queue.isEmpty()) {
            Point vertex =  queue.poll();
            int movingValue = matrix[vertex.x][vertex.y];

            // 전류가 안쪽에 도달
            if (vertex.x == N - 1) {
                return true;
            }

            for (int i = 0; i < 4; i++) {
                Point next = new Point(vertex.x + dr[i] , vertex.y + dc[i]);

                // 갈 수 있는 칸인가??
                if (next.x < 0 || next.y < 0 || next.x > N - 1  || next.y > M - 1)
                    continue;

                // 이미 방문한 칸인가??
                if (visit[next.x][next.y])
                    continue;

                // 전류를 차단하는 검은색 격자인가??
                if (matrix[next.x][next.y] == 1)
                    continue;

                queue.add(next);
                visit[next.x][next.y] = true;

            }
        }
        return false;
    }

}
