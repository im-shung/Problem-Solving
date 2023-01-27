import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int A, B, C, D;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());
        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        C = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());

    }

    static void pro() {
        System.out.println(Math.min(A + D, B + C));
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}
