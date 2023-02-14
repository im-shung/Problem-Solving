import java.io.*;
import java.util.*;

// DFS

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int N;
    static List<Integer> column = new ArrayList<>(); // 열
    static List<Integer> leftDi = new ArrayList<>(); // 왼쪽 대각선
    static List<Integer> rightDi = new ArrayList<>(); // 오른쪽 대각선
    static int ans;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        dfs(1);
        System.out.println(ans);

    }

    static void dfs(int r) {
        // 목적지인가? - 마지막 행
        if (r == N + 1) {
            ans += 1;
        } else {
            // 갈 수 있는가?
            for (int c = 1; c <= N; c++) {
                if (column.contains(c) || leftDi.contains(r + c) || rightDi.contains(r - c)) {
                    continue;
                }

                // 체크인
                column.add(c);
                leftDi.add(r + c);
                rightDi.add(r - c);

                // 간다.
                dfs(r + 1);

                // 체크아웃
                column.remove(column.size() - 1);
                leftDi.remove(leftDi.size() - 1);
                rightDi.remove(rightDi.size() - 1);
            }
        }

    }

}
