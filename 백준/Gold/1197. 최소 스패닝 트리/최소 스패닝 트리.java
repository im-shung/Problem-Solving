import java.io.*;
import java.util.*;

public class Main {

	static class Edge implements Comparable<Edge>{
		int u;
		int v;
		int weight;

		public Edge(int u, int v, int weight) {
			super();
			this.u = u;
			this.v = v;
			this.weight = weight;
		}

		@Override
		public int compareTo(Edge o) {
			return this.weight - o.weight;
		}

		@Override
		public String toString() {
			StringBuilder builder = new StringBuilder();
			builder.append("Edge [u=").append(u).append(", v=").append(v).append(", weight=").append(weight)
					.append("]");
			return builder.toString();
		}
	}

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();

	static int V, E; // 정점 개수, 간선 개수
	static Edge[] edgeList; // 간선리스트
	static PriorityQueue<Edge> pq; // 간선우선순위큐
	

	private static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		V = Integer.parseInt(st.nextToken());
		E = Integer.parseInt(st.nextToken());
		edgeList = new Edge[E];
		pq = new PriorityQueue<>();
		for (int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			int weight = Integer.parseInt(st.nextToken());
			edgeList[i] = new Edge(u, v, weight);
			pq.add(edgeList[i]);
		}
	}

	// 유니온 파인드
	static int[] parents;
	
	// 크기가 1인 서로소 집합
	static void make() {
		parents = new int[V + 1];
		for (int i = 1; i <= V; i++) {
			parents[i] = i;
		}
	}
	
	// 대표 노드 반환
	static int find(int x) {
		if (parents[x] == x) return x;
		return parents[x] = find(parents[x]);
	}
	
	// X U Y
	static boolean union(int x, int y) {
		int xRoot = find(x); // x노드의 대표 노드
		int yRoot = find(y); // y노드의 대표 노드
		if (xRoot == yRoot) return false;
		parents[yRoot] = xRoot;
		return true;
	}
	
    // 간선개수, 총 가중치 합
	static int edgeCnt, totalWeight;
	
	private static void pro() {
		// 노드 자기 자신을 parent로 둔다.
		make();
	
		// 스패닝 트리: (간선개수 = 정점개수-1)
        // 매번 최소 가중치를 갖는 간선을 택한다.
		while (edgeCnt < V - 1) {
			Edge e = pq.poll();
            // 노드 u와 노드 v를 연결시킨다. (유니온)
			if (union(e.u, e.v)) {
				edgeCnt++;
				totalWeight += e.weight;
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
		System.out.println(totalWeight);
		br.close();
	}

}
