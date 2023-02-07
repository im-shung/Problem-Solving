import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static final int MAX_ANCESTOR = 17; // 2^16 < 정점 개수 (100_000) < 2^17

    static int N, M;

    static List<List<Integer>> adjList;

    static int[] dep = new int[100_001];

    static boolean[] visited = new boolean[100_001];

    static int[][] parent = new int[MAX_ANCESTOR + 1][100_001]; // parent[n][k]는 '정점 k의 2^n번째 조상'을 뜻한다.

    static void input() throws IOException {
//        br = new BufferedReader(new FileReader("src/input.txt"));
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        adjList = new ArrayList<>(N + 1);
        for (int i = 0; i <= N; i++) {
            adjList.add(new ArrayList<>());
        }

        // 인접 리스트(adjList) 초기화
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            adjList.get(a).add(b);
            adjList.get(b).add(a);
        }

    }

    static void pro() throws IOException {
        // 1. 최상위 조상 정점을 시작으로 DFS(혹은 BFS)를 수행하여 각 '정점의 깊이'와 '부모 정점'을 저장합니다.
        dfs(1, 1);

        // parent 배열을 채운다 => 2^17번째 조상까지 구해놓겠다.
        for (int n = 1; n <= MAX_ANCESTOR; n++) {
            for (int current = 1; current <= N; current++) {
                // 2^n번째 조상은 2^{n-1}번째 조상의 2^{n-1}번째 조상이다.
                // n = 1일 때, 2번째 조상은 1번째 조상의 1번째 조상이다.
                // n = 2일 때, 4번째 조상은 2번째 조상의 2번째 조상이다.
                parent[n][current] = parent[n - 1][parent[n - 1][current]];
            }
        }

        // M개의 줄에 차례대로 입력받은 두 정점의 가장 가까운 공통 조상을 출력한다.
        M = Integer.parseInt(br.readLine());
        
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            // 2. 정점의 부모를 따라 하나씩 올라가 LCA를 찾는다.
            // 2-1. 'a의 depth > b의 depth'를 만족하도록 swap 한다.
            int depA = dep[a];
            int depB = dep[b];

            if (depA < depB) {
                int temp = depA;
                depA = depB;
                depB = temp;

                temp = a;
                a = b;
                b = temp;
            }

            // 2-2. a의 depth == b의 depth 가 되도록 만든다.
            /*
            a의 depth == b의 depth 가 되도록 만든다.
            'a의 depth > b의 depth'가 되도록 위에서 swap 한 상태이다.
            그러므로 a의 depth를 2^n만큼 빼면서 a의 depth와 b의 depth를 같도록 만든다.
            a의 depth를 2^n만큼 뺀다 -> a를 a의 2^n번째 조상 위치로 옮긴다. 그리고 b랑 다시 비교한다.
            (MAX_ANCESTOR >= n >= 0)
             */
            for (int n = MAX_ANCESTOR; n >= 0; n--) {
                // Math.pow(2, n) == 2^n
                // 2^n <= 정점 a의 depth - 정점 b의 depth'
                if (depA - (int) Math.pow(2, n) >= depB) {
                    // depth를 맞추기 위해 차이를 빼준다.
                    // 정점 a의 depth = 정점 b의 depth - 2^n
                    depA -= (int) Math.pow(2, n);

                    // a = a의 n번째 조상
                    a = parent[n][a];
                }

                if (depA == depB) {
                    break;
                }
            }

            // 2-3. a와 b가 같을 때 까지 depth를 올린다.
            int ans = a;
            if (a != b) {
                for (int n = MAX_ANCESTOR; n >= 0; n--) {
                    if (parent[n][a] != parent[n][b]) {
                        a = parent[n][a];
                        b = parent[n][b];
                    }
                    ans = parent[n][a];
                }
            }
            // 2-4. LCA 출력
            sb.append(ans).append("\n");
        }
        System.out.println(sb);
    }
    
    static void dfs(int current, int depth) {
        // 1. 체크인
        visited[current] = true;
        dep[current] = depth;
        // 2. 목적지인가?

        // 3. 연결된 곳인가? - current의 인접 노드
        for (int adjNode : adjList.get(current)) {
            // 4. 갈 수 있는가? - 방문하지 않은 노드
            if (visited[adjNode] == false) {
                // 2^0 = 1
                // 인접 노드의 1 번째 조상은 current이다.
                parent[0][adjNode] = current;
                // 5. 간다
                dfs(adjNode, depth + 1);
            }
        }

        // 6. 체크아웃 - 생략
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}


