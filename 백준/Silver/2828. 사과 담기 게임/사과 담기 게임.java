import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int screen, bascket, appleCount;
    static int[] falls;
    static int answer;

    private static void input() throws IOException {
        st = new StringTokenizer(br.readLine());
        // 스크린 칸수
        screen = Integer.parseInt(st.nextToken());
        // 바구니 칸수
        bascket = Integer.parseInt(st.nextToken());
        // 떨어지는 사과 개수
        appleCount = Integer.parseInt(br.readLine());
        // 사과의 떨어지는 위치들
        falls = new int[appleCount];
        for (int i = 0; i < appleCount; i++) {
            falls[i] = Integer.parseInt(br.readLine());
        }
    }

    private static void pro() {
        int lPos = 1;
        int rPos = bascket;

        for (int i = 0; i < appleCount; i++) {
            // 바구니 안쪽에 있는경우
            if (falls[i] >= lPos && falls[i] <= rPos) {
                continue;
            }
            // 바꾸니 왼쪽에 있는 경우
            else if (falls[i] < lPos) {
                int distance = lPos - falls[i];
                answer += distance;
                lPos = falls[i];
                rPos = rPos - distance;
            }
            // 바구니 오른쪽에 있는 경우
            else if (falls[i] > rPos) {
                int distance = falls[i] - rPos;
                answer += distance;
                rPos = falls[i];
                lPos = lPos + distance;
            }
        }
    }


    public static void main(String[] args) throws Exception {
        //br = new BufferedReader(new FileReader("src/input.txt"));
        /* 입력 */
        input();
        /* 처리 */
        pro();
        /* 출력 */
        System.out.println(answer);
    }
}
