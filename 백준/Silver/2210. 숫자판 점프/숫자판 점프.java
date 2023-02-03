import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
int형 숫자가 중복인지 아닌지 볼 때 숫자의 범위만큼 boolean 배열을 생성해서 visit을 체크한다.
dfs 전후로 number 계산해주고, 목적지에 도착했을 때 visit 배열을 바탕으로 count를 세준다. 
 */

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static StringTokenizer st;

    static StringBuilder sb = new StringBuilder();

    static final int[] my = {1, -1, 0, 0};
    static final int[] mx = {0, 0, 1, -1};

    static int[][] map = new int[5][5];
    static boolean[] visit = new boolean[1_000_000];

    static int count = 0;
    static int number;

    static void input() throws IOException {
//        br = new BufferedReader(new FileReader(new File("src/input.txt")));

        for (int y = 0; y < 5; y++) {
            st = new StringTokenizer(br.readLine());
            for (int x = 0; x < 5; x++) {
                map[y][x] = Integer.parseInt(st.nextToken());
            }
        }
    }

    private static void pro() {
        for (int y = 0; y < 5; y++) {
            for (int x = 0; x < 5; x++) {
                dfs(y, x, 0);
            }
        }
        ;
        System.out.println(count);
    }

    static void dfs(int y, int x, int length) {
        // 1. 체크인 생략
        // 2. 목적지인가? -> 길이가 6이되면
        if (length == 6) {
            if (visit[number] == false) {
                visit[number] = true;
                count++;
            }
        } else {
            // 3. 연결된 곳인가?
            for (int d = 0; d < 4; d++) {
                int ty = y + my[d];
                int tx = x + mx[d];

                // 4. 갈 수 있는가? -> 맵 범위 안에서
                if (0 <= ty && ty < 5 && 0 <= tx && tx < 5) {
                    // 5. 간다
                    // 숫자는 dfs 전후로 * 10 해주고 /10 해준다. 
                    number = number * 10 + map[y][x];
                    dfs(ty, tx, length + 1);
                    number /= 10;
                }
            }
        }
        // 6. 체크아웃 생략
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }
}
