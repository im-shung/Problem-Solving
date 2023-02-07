import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static final int INF = (int) 1e7;

    static int V, E;

    static int[][] dist;

    static void input() throws IOException {
        V = Integer.parseInt(br.readLine());
        E = Integer.parseInt(br.readLine());

        dist = new int[V + 1][V + 1]; // 비용은 100,000보다 작거나 같은 자연수
        for (int i = 1; i <= V; i++) {
            for (int j = 1; j <= V; j++) {
                if (i != j) {
                    dist[i][j] = INF;
                }
            }
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            dist[start][end] = Math.min(weight, dist[start][end]);
        }
    }

    static void pro() throws IOException {
        for (int middle = 1; middle <= V; middle++) { // 모든 가능한 경유지 middle
            for (int start = 1; start <= V; start++) { // 모든 정점 start
                for (int end = 1; end <= V; end++) { // 모든 정점 end
                    if (dist[start][end] > dist[start][middle] + dist[middle][end]) {
                        dist[start][end] = dist[start][middle] + dist[middle][end];
                    }
                }
            }
        }

        for (int i = 1; i <= V; i++) {
            for (int j = 1; j <= V; j++) {
                if (dist[i][j] == INF) {
                    sb.append(0).append(" ");
                } else {
                    sb.append(dist[i][j]).append(" ");
                }
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }


    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}