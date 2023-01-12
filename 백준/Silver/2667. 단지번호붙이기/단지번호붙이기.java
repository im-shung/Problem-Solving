import java.io.*;
import java.text.ParseException;
import java.util.*;

/*
Graph & Search
- 인접행렬: int [][]
- 인접리스트:
 */

public class Main {

    static int[] dr = {-1, 0, 0, 1};
    static int[] dc = {0, 1, -1, 0};

    static int N, count;
    static int[][] matrix;
    static boolean[][] visit;

    public static void main(String[] args) throws IOException, ParseException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        matrix = new int [N][N];
        visit = new boolean [N][N];


        for (int i = 0; i < N; i++) {
            String [] line = br.readLine().split("");
            for (int j = 0; j < N; j++) {
                matrix[i][j] = Integer.parseInt(line[j]);
            }
        }

        List<Integer> homeCount = new ArrayList<>();
        count = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (visit[i][j])
                    continue;

                if (matrix[i][j] == 1)
                    dfs(i, j);

                if (count != 0){
                    homeCount.add(count);
                    count = 0;
                }

            }
        }

        Collections.sort(homeCount);
        System.out.println(homeCount.size());
        homeCount.forEach(System.out::println);
    }


    static void dfs(int x, int y) {
        visit[x][y] = true;
        count++;

        for (int i = 0; i < 4; i++) {
            int dx = x + dr[i];
            int dy = y + dc[i];

            if (dx < 0 || dy < 0 || dx >= N || dy >= N)
                continue;

            if (visit[dx][dy])
                continue;

            if (matrix[dx][dy] == 1)
                dfs(dx, dy);

        }

    }

}
