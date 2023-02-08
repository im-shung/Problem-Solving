import java.io.*;
import java.util.*;

class Edge {

    int vertex;
    int weight;

    public Edge(int vertex, int weight) {
        this.vertex = vertex;
        this.weight = weight;
    }
}

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int N;

    static List<List<Integer>> adjList;

    static int[] cost;

    static int[] result;

    static int[] inDegree;

    static Queue<Integer> queue = new ArrayDeque<>();

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        adjList = new ArrayList<>(N + 1);
        for (int i = 0; i <= N; i++) {
            adjList.add(new ArrayList<>());
        }

        cost = new int[N + 1];
        inDegree = new int[N + 1];
        result = new int[N + 1];

        for (int vj = 1; vj <= N; vj++) {
            st = new StringTokenizer(br.readLine());
            cost[vj] = Integer.parseInt(st.nextToken());

            while (true) {
                int vi = Integer.parseInt(st.nextToken());
                if (vi == -1) {
                    break;
                }
                // 선행자 vi -> 후행자 vj
                adjList.get(vi).add(vj);
                inDegree[vj]++;
            }
        }
    }

    static void pro() {

        for (int v = 1; v <= N; v++) {
            if (inDegree[v] == 0) {
                queue.add(v);
            }
        }

        while (!queue.isEmpty()) {
            int current = queue.poll();
            result[current] += cost[current];

            for (Integer next : adjList.get(current)) {
                inDegree[next]--;
                // 선행자의 값 중 최대값을 넣어준다.
                if (result[next] < result[current]) {
                    result[next] = result[current];
                }
       
                if (inDegree[next] == 0) {
                    queue.add(next);
                }
            }

        }

        for (int i = 1; i <= N; i++) {
            sb.append(result[i]).append("\n");
        }

        System.out.println(sb);
    }

    static void union(int a, int b) {

    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}


