import java.io.*;
import java.util.*;

public class Main {

    public static int N;
    public static int M;
    public static boolean[] visit;
    public static int[] arr;
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws FileNotFoundException {
        FastReader scan = new FastReader();
        N = scan.netxInt();
        M = scan.netxInt();

        visit  = new boolean[N];
        arr = new int[M];

        dfs(0);
        System.out.println(sb);

    }

    static void dfs (int depth) {

        // 재귀 길이가 M과 같아지면 그래프 탐색과정에서 담은 배열을 출력
        if (depth == M) {
            for (int val : arr) {
                sb.append(val).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = 0; i < N; i++) {

            // 만약 해당 노드를 방문하지 않았다면?
            if (!visit[i]) {
                visit[i] = true;        // 해당 노드를 방문상태로 변경
                arr[depth] = i + 1;     // 해당 깊이를 index로 하며 i + 1 값 저장
                dfs(depth + 1);   // 다음 자식 노드 방문을 위해 depth + 1 증가시키면서 재귀호출

                // 자식노드 방문이 끝나고 돌아오면 방문노드를 방문하지 않은 상태로 변경
                visit[i] = false;
            }
        }
    }

    static class FastReader {

        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public FastReader(String s) throws FileNotFoundException {
            br = new BufferedReader(new FileReader(new File(s)));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int netxInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
