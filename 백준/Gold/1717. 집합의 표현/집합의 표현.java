import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int N, M;

    static int[] parent;

    static void input() throws IOException {
//        br = new BufferedReader(new FileReader("src/input.txt"));
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        parent = new int[N + 1];
    }

    static void pro() throws IOException {
        init();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int op = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (op == 0) { // union
                union(a, b);
            } else { // find
                if (find(a) == find(b)) { // a와 b가 연결되어 있다면
                    sb.append("YES").append("\n");
                } else {
                    sb.append("NO").append("\n");
                }
            }
        }
        System.out.println(sb);
    }

    static void union(int node1, int node2) {
        // root = node의 부모 = find(node)
        int root1 = find(node1);
        int root2 = find(node2);

        // 두 트리를 합친다.
        if (root1 < root2) {
            parent[root1] = root2;
        } else {
            parent[root2] = root1;
        }
    }

    static int find(int node) {
        // 루트노드(대표집합번호)인 경우
        if (node == parent[node]) {
            return node;
        }
        // node: 현재 노드(->A)
        // parent[node]: A의 부모 노드(->B)
        // find(parent[node]): B의 부모 노드(->C)를 검색, A의 부모를 C로 변경
        else {
            return parent[node] = find(parent[node]);
        }
    }

    static void init() {
        for (int i = 1; i <= N; i++) {
            parent[i] = i;
        }
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}


