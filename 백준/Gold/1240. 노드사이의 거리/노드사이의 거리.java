import java.io.*;
import java.util.*;

/*
Tree 트리

탐색 알고리즘: BFS 또는 DFS
인접 리스트를 쓴다면 O(V+E)
 */


class Edge {

    int node;
    int dist; // node 사이의 거리

    public Edge(int node, int dist) {
        this.node = node;
        this.dist = dist;
    }
}

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int N, M;
    static ArrayList<Edge>[] adj;
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
            adj[a].add(new Edge(b, dist));
            adj[b].add(new Edge(a, dist));
        }
    }

    // dfs(x, goal)  := 정점 x 에서 출발해서 정점 goal에 도달할 때까지의 거리(dist)를 더해가는 함수
    static void dfs(int x, int goal, int dist) {
        visit[x] = true;

        // 목표 정점에 도달했는가??
        if (x == goal) {
            sb.append(dist).append("\n");
            return;
        }

        // x와 연결된 노드들을 탐색한다.
        for (Edge vertex : adj[x]) {
            // 이미 방문했는가??
            if (visit[vertex.node]) {
                continue;
            }

            // 현재 노드를 출발점으로, 이전 dist와 현재 dist 를 더해서 dfs()를 호출한다.
            dfs(vertex.node, goal, dist + vertex.dist);
        }
    }

    static void pro() throws IOException {
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int goal = Integer.parseInt(st.nextToken());

            // 방문 배열은 매번 초기화한다.
            visit = new boolean[N + 1];
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
