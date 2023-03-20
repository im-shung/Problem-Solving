import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	static int N, M;
	static ArrayList<Integer>[] adjList;
	static boolean[] visited;
	static int ans;

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		adjList = new ArrayList[N + 1];
		visited = new boolean[N + 1];

		for (int i = 1; i <= N; i++) {
			adjList[i] = new ArrayList<>();
		}

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int v1 = Integer.parseInt(st.nextToken());
			int v2 = Integer.parseInt(st.nextToken());
			adjList[v1].add(v2);
			adjList[v2].add(v1);
		}

		for (int i = 1; i <= N; i++) {
			if (!visited[i]) {
				++ans;
				BFS(i); // 시작 정점 : i
			}

		}

//		System.out.println(ans);
//		System.out.println();
//		ans = 0;
//		visited = new boolean[N + 1];
//
//		for (int i = 1; i <= N; i++) {
//			if (!visited[i]) {
//				++ans;
//				DFS(i); // 시작 정점 : i
//			}
//		}
		System.out.println(ans);
	}

	private static void BFS(int startNode) {
		Queue<Integer> queue = new LinkedList<>();
		queue.add(startNode);
		visited[startNode] = true;
		while (!queue.isEmpty()) {
			int curr = queue.poll();
			//System.out.print(curr);
			for (int node : adjList[curr]) {
				if (!visited[node]) {
					visited[node] = true;
					queue.add(node);
				}
			}
		}
	}

	private static void DFS(int curr) {
		System.out.print(curr);
		for (int node : adjList[curr]) {
			if (!visited[node]) {
				visited[node] = true;
				DFS(node);
			}
		}
	}
}
