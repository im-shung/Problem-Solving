import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int T, N;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        T = Integer.parseInt(st.nextToken());

        for (int t = 0; t < T; t++) {
            String input = br.readLine();
            N = input.length();

            arr = new int[N + 1];

            int sum = 0;
            for (int i = 0; i < N; i++) {
                if (input.charAt(i) == 'O') {
                    arr[i + 1] = arr[i] + 1;
                } else if (input.charAt(i) == 'X') {
                    arr[i + 1] = 0;
                }
                sum += arr[i + 1];
            }
            sb.append(sum).append("\n");
        }
        System.out.println(sb);
    }
}
