import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int N;
    static int[][] input = new int[6][2];
    
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        for (int i = 0; i < 6; i++) {
            st = new StringTokenizer(br.readLine());
            input[i][0]  = Integer.parseInt(st.nextToken());
            input[i][1] = Integer.parseInt(st.nextToken());
        }

        int bigger = 0;
        int smaller = 0;
        for (int x = 0; x < 6; x++) {
            if (input[x % 6][0] == input[(x + 2) % 6][0]
                        && input[(x + 1) % 6][0] == input[(x + 3) % 6][0]) {
                bigger = input[(x + 5) % 6][1] * input[(x + 4) % 6][1];
                smaller = input[(x + 1) % 6][1] * input[(x + 2) % 6][1];
                break;
            }
        }
        System.out.println((bigger - smaller) * N);
    }
}
