import java.awt.Point;
import java.io.*;
import java.util.*;

/*
Tree 트리
"Root" 를 시작으로 하는 그래프 탐색 문제
탐색 알고리즘: BFS 또는 DFS
인접 리스트를 쓴다면 O(V+E)
 */

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int N, M;
    static ArrayList<Point>[] adj;
    static boolean[] visit;

    static void input() throws IOException {
   
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        // 인접 리스트 구성하기
        adj = new ArrayList[N + 1];

        // 정점 1 ~ N
        for (int i = 1; i <= N; i++) {
            adj[i] = new ArrayList<>();
        }

        // 간선 N -1 개
        for (int i = 1; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int dist = Integer.parseInt(st.nextToken());
            // 누가 자식이고 부모인지 모르는 상태로 시작한다.
            adj[a].add(new Point(b, dist));
            adj[b].add(new Point(a, dist));
        }
    }


    // dfs(x, goal)  := 정점 x 에서 출발해서 정점 goal에 도달할 때까지의 거리(dist)를 더해가는 함수
    static void dfs(int x, int goal, int dist) {
        visit[x] = true;

        if (x == goal) {
            sb.append(dist).append("\n");
            return;
        }

        for (Point vertex : adj[x]) {
            if (vertex.x == x || visit[vertex.x]) {
                continue;
            }
            dfs(vertex.x, goal, dist + vertex.y);
        }
    }

    static void pro() throws IOException {
        // 1번 정점이 ROOT 이므로, 여기서 시작해서 Tree의 구조를 파악하자.
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            visit = new boolean[N + 1];
            int x = Integer.parseInt(st.nextToken());
            int goal = Integer.parseInt(st.nextToken());
            dfs(x, goal, 0);
        }

        // 정답 출력하기
        System.out.println(sb);
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}
