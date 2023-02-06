import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int N, M;

    static List<List<Integer>> adjList;
    static int[] inDegree;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        adjList = new ArrayList<>(N + 1);
        for (int i = 0; i <= N; i++) {
            adjList.add(new ArrayList<>());
        }

        inDegree = new int[N + 1];
    }

    static void pro() throws IOException {
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int nodeA = Integer.parseInt(st.nextToken());
            int nodeB = Integer.parseInt(st.nextToken());
            // a -> b
            adjList.get(nodeA).add(nodeB); // A -> B 간선
            inDegree[nodeB]++;
        }

        Queue<Integer> queue = new ArrayDeque<>();

        // 차수가 0인 노드를
        // queue에 삽입
        for (int node = 1; node <= N; node++) {
            if (inDegree[node] == 0) {
                queue.add(node);
            }
        }

        while (!queue.isEmpty()) {
            int predecessor = queue.poll();
            sb.append(predecessor).append(" ");
            List<Integer> adj = adjList.get(predecessor);
            for (int index = 0; index < adj.size(); index++) {
                int successor = adj.get(index);
                if (--inDegree[successor] == 0) {
                    queue.add(successor);
                }
            }
        }

        System.out.println(sb);
    }



    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}


