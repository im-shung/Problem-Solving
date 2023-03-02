import java.io.*;
import java.util.*;

// Greedy
// K개로 쪼갠다 -> K-1개의 경계를 고른다

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int N, K;
    static int[] input;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        input = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            input[i] = Integer.parseInt(st.nextToken());
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
        // 인접한 원생들의 키 차이를 최대힙에 넣는다.
        for (int i = N - 1; i >= 1; i--) {
            pq.add(input[i] - input[i - 1]);
        }
        // count := K개의 조를 만들 때, 고를 수 있는 경계의 개수 
        int count = K - 1; 
        // 경계의 개수만큼 최대힙에서 빼낸다. 
        for (int i = 0; i < count; i++) {
            pq.poll();
        }
        // 최대힙의 나머지 요소들을 더한다. 
        int sum = 0;
        while (!pq.isEmpty()) {
            sum += pq.poll();
        }
        System.out.println(sum);
    }
}
