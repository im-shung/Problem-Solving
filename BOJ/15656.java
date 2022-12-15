import java.io.*;
import java.util.*;

public class Main {

    static StringBuilder sb = new StringBuilder();
    static FastReader scan = new FastReader();

    static int N, M;
    static int[] arr;
    static int[] answer;
    static boolean[] visit = new boolean[10_001];

    public static void main(String[] args) throws FileNotFoundException {
        N = scan.netxInt();
        M = scan.netxInt();

        arr = new int[N];
        answer = new int[M];
        for (int i = 0; i < N; i++) {
            arr[i] = scan.netxInt();
        }

        arr = Arrays.stream(arr).sorted().toArray();
        dfs(0, 0);
        System.out.println(sb);

    }

    static void dfs(int depth, int criteria) {

        if (depth == M) {
            for (int ans : answer) {
                sb.append(ans).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int a : arr) {
            answer[depth] = a;
            dfs(depth + 1, a);
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
