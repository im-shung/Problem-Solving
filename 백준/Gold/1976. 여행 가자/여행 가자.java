import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();

	static int N, M;
	static int[] parent, plan;
	static boolean isPossible = true;

	// 크기가 1인 서로소 집합
	private static void make() {
		for (int i = 0; i < N; i++) {
			parent[i] = i;
		}
	}
	
	private static void input() throws Exception {
		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());
		
		parent = new int[N];
		plan = new int[M];
		make();
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				if (Integer.parseInt(st.nextToken()) == 1) 
					union(i, j);
			}
		}
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < M; i++) {
			plan[i] = Integer.parseInt(st.nextToken()) - 1;
		}
	}
	
	// x와 y 노드가 같은 집합인지 확인
	private static boolean isSame(int a, int b) {
		int rootA = find(a);
		int rootB = find(b);
		return rootA == rootB;
	}

	// x 노드의 대표 노드 반환
	private static int find(int x) {
		if (parent[x] == x) return x;
		return parent[x] = find(parent[x]);
	}
	
	// x U y
	private static void union(int a, int b) {
		int rootA = find(a);
		int rootB = find(b);
		if (rootA == rootB) return;
		else if (rootA < rootB) parent[rootA] = rootB;
		else parent[rootB] = rootA;
	}

	private static void pro() {
		for (int i = 0; i < M - 1; i++) {
			int a = plan[i];
			int b = plan[i + 1];
			if (!isSame(a, b)) { // a 와 b가 연결되어 있는가?
				isPossible = false;
				break;
			}
		}
	}
	
	public static void main(String[] args) throws Exception {
		/* 입력 */
		input();
		/* 처리 */
		pro();
		/* 출력 */
		if (isPossible) System.out.println("YES");
		else System.out.println("NO");
	}
}
