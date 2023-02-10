import java.io.*;
import java.util.*;

/*
물의 양 / 리프 노드의 개수
 */

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int N, W;

    static int[] adj;

    static int count;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());

        adj = new int[N + 1];
    }

    static void pro() throws IOException {
        // 간선의 개수는 N-1
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            adj[u]++;
            adj[v]++;
        }

        // 리프 노드의 개수 판단
        for (int i = 2; i <= N; i++) {
            if (adj[i] == 1) {
                count++;
            }
        }

        System.out.println((double) W / count);
    }


    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}


