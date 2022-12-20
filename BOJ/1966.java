import java.awt.Point;
import java.io.*;
import java.util.*;

public class Main {

    static int N, M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());

        for (int t = 0; t < T; t++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            Queue<Point> queue = new LinkedList<>();
            int[] sortedList = new int[N];
            int key = 0;

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                int importance = Integer.parseInt(st.nextToken());
                sortedList[i] = importance;
                if (i == M) {
                    key = importance;
                    queue.add(new Point(importance, 1));
                } else {
                    queue.add(new Point(importance, 0));
                }
            }

            Arrays.sort(sortedList);

            int maxIndex = N - 1;
            int count = 0;
            Point now;
            while (!queue.isEmpty()) {
                now = queue.poll();

                // now가 큐에서 최댓값인지 검사
                if (now.x == sortedList[maxIndex]) {
                    count += 1;
                    maxIndex -= 1;
                    if (now.x == key && now.y == 1) {
                        break;
                    }
                } else {
                    queue.offer(now);
                }
            }
            System.out.println(count);
        }
    }
}
