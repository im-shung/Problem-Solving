import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int M;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());

    }

    static void pro() throws IOException {
        int ball = 1;
        for (int m = 0; m < M; m++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            if (x == ball) {
                ball = y;
            }
            else if (y == ball) {
                ball = x;
            }
        }
        System.out.println(ball);
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}
