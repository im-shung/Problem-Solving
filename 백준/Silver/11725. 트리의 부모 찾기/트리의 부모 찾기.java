import java.io.*;
import java.util.*;

/*
Tree 트리
"Root" 를 시작으로 하는 그래프 탐색 문제
탐색 알고리즘: BFS 또는 DFS
인접 리스트를 쓴다면 O(V+E)
 */

public class Main {

    static int N;
    static ArrayList<Integer>[] adj;
    static int[] parent;

    static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        // 인접 리스트 구성하기
        adj = new ArrayList[N + 1];
        parent = new int[N + 1];

        // 정점 1 ~ N
        for (int i = 1; i <= N; i++) {
            adj[i] = new ArrayList<>();
        }

        // 간선 N -1 개
        for (int i = 1; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            // 누가 자식이고 부모인지 모르는 상태로 시작한다.
            adj[a].add(b);
            adj[b].add(a);
        }
    }


    // dfs(x, par)  := 정점 x 의 부모가 par 였고, x의 children 들을 찾아주는 함수
    static void dfs(int x, int par) {
        parent[x] = par;

        for (int y : adj[x]) {
            if (y == par) {
                continue;
            }
            parent[y] = x; 
            dfs(y, x);
        }
    }

    static void pro() {
        // 1번 정점이 ROOT 이므로, 여기서 시작해서 Tree의 구조를 파악하자.
        dfs(1, -1);

        // 정답 출력하기
        StringBuilder sb = new StringBuilder(); // StringBuilder를 써야 시간이 단축된다.
        for (int i = 2; i <= N; i++) {
            sb.append(parent[i]).append("\n");
        }
        System.out.println(sb);
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}
