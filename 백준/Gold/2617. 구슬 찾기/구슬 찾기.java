import java.io.*;
import java.util.*;

/*
Tree 트리
탐색 알고리즘: BFS 또는 DFS
인접 리스트를 쓴다면 O(V+E)
문제 요점: 부모 없는 노드, 자식 없는 노드의 개수를 구해라
 */

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int N, M;
    static ArrayList<Integer>[] in, out;
    static boolean[] visit;
    static int cnt;

    static void input() throws IOException {
     
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        // 인접 리스트 구성하기
        in = new ArrayList[N + 1]; // (u, v)를 연결하는 edge는 무게가 u > v임을 나타내는 그래프
        out = new ArrayList[N + 1]; // (u, v)를 연결하는 edge는 무게가 u < v임을 나타내는 그래프

        for (int i = 1; i <= N; i++) {
            in[i] = new ArrayList<>();
            out[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            in[u].add(v);
            out[v].add(u);
        }
    }

    static int bfs(ArrayList<Integer>[] adj, int x) {
        Queue<Integer> que = new LinkedList<>();
        visit = new boolean[N + 1];
        cnt = 0;
        
        que.add(x);
        visit[x] = true;

        while (!que.isEmpty()) {
            int cur = que.poll();

            for (int nxt : adj[cur]) {
                if (visit[nxt]) {
                    continue;
                }
                que.add(nxt);
                visit[nxt] = true;
                cnt++;
            }
        }

        return cnt;
    }

    static void pro() {

        int result = 0;

        for (int i = 1; i <= N; i++) { // 각 구슬에 대해 무거운 구슬과 가벼운 구슬의 개수를 구한다.
            int big = bfs(out, i);
            int small = bfs(in, i);

            // 무거운 구슬 또는 가벼운 구슬의 개수가 (n - 1)/2보다 많다면 무게가 중앙값인 구슬이 될 수 없다.
            if (big > ((N - 1)/2) || small > ((N - 1)/2)) {
                result++;
            }
        }

        // 정답 출력하기
        System.out.println(result);
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}
