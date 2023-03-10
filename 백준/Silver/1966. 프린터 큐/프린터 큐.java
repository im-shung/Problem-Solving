import java.io.*;
import java.util.*;

public class Main {

	static class Node {
		int num;
		int priority;

		public Node(int num, int priority) {
			this.num = num;
			this.priority = priority;
		}

	}

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();

	static int N; // 문서의 개수
	static int M; // M번째 문서

	public static void main(String[] args) throws IOException {
		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());

			st = new StringTokenizer(br.readLine());

			Deque<Node> que = new ArrayDeque<>();
			List<Integer> order = new ArrayList<>(N);

			for (int i = 0; i < N; i++) {
				int p = Integer.parseInt(st.nextToken());
				que.add(new Node(i, p));
				order.add(p);
			}

			Collections.sort(order, Collections.reverseOrder());

			// 먼저 요청된 것을 먼저 인쇄
			// 선입선출
			// 큐 새로운 조건
			// front의 중요도보다 나머지 중요도가 높다면
			// front를 back으로 보낸다.
			int i = 0;
			int ans = 0; // M번째 문서가 인쇄된 순서
			while (!que.isEmpty()) {
				Node cur = que.poll();
				if (cur.priority != order.get(i))
					que.addLast(cur);
				else {
					ans++; i++;
					if (cur.num == M)
						break;
				}
			}

			System.out.println(ans);
		} // end of testcase
	}
}
