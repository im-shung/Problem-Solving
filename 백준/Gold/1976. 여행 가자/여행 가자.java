import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();

	static int N, M;
	static int[] parent, plan;

	public static void main(String[] args) throws Exception {
		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());
		
		parent = new int[N];
		plan = new int[M];
		init();
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				if (Integer.parseInt(st.nextToken()) == 1) 
					union(i, j);
			}
		}
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < M; i++) {
			plan[i] = Integer.parseInt(st.nextToken());
		}
		boolean isPossible = true;
		for (int i = 0; i < M - 1; i++) {
			int a = plan[i] - 1;
			int b = plan[i + 1] - 1;
			if (!isSame(a, b)) {
				isPossible = false;
				break;
			}
		}
		if (isPossible) System.out.println("YES");
		else System.out.println("NO");
	}

	private static boolean isSame(int a, int b) {
		int rootA = find(a);
		int rootB = find(b);
		return rootA == rootB;
	}

	private static int find(int x) {
		if (parent[x] == x) return x;
		return parent[x] = find(parent[x]);
	}
	
	private static void union(int a, int b) {
		int rootA = find(a);
		int rootB = find(b);
		if (rootA == rootB) return;
		else if (rootA < rootB) parent[rootA] = rootB;
		else parent[rootB] = rootA;
	}

	private static void init() {
		for (int i = 0; i < N; i++) {
			parent[i] = i;
		}
	}


}
