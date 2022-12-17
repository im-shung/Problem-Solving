import java.io.*;
import java.util.*;

public class Main {

    static StringBuilder sb = new StringBuilder();

    static int[] arr;
    static int[] answer;
    static boolean[] visit = new boolean[10_001];

    static int N, M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N];
        answer = new int[M];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
        dfs(0);
        System.out.println(sb);

    }

    static void dfs(int depth) {
        if (depth == M) {
            for (int ans : answer) {
                sb.append(ans).append(" ");
            }
            sb.append("\n");
            return;
        }

        int previousElement = -1;
        for (int i = 0; i < N; i++) { // arr에 같은 숫자가 있을 수도 있으므로 visit은 index로 관리해야 한다.
            int nowElement = arr[i];
            if (!visit[i] && !Objects.equals(nowElement, previousElement)) {
                previousElement = nowElement;
                visit[i] = true;
                answer[depth] = arr[i];
                dfs(depth + 1);
                visit[i] = false;
            }
        }
    }

}
