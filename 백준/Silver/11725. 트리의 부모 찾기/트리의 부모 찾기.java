import java.util.*;
import java.io.*;

/** 
* 알고리즘 : 트리 
* 1. 일반적인 입력을 통해 트리를 구성하면 안된다.
* 2. bfs 또는 dfs와 같은 탐색을 통한 트리 구현
* 3. 트리 구현방법중 부모의 노드를 구하는 방식을 사용한다.
*/
public class Main {
	static StringBuilder sb = new StringBuilder();
	static int[] p;
	static List<Integer>[] adj;
	
	static void dfs(int curr) {
		for(int i = 0; i<adj[curr].size(); i++) {
			int next = adj[curr].get(i);
			if(p[curr] == next) continue;
			p[next] = curr;
			dfs(next);
		}
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int n = Integer.parseInt(br.readLine());
		adj = new List[n + 1];
		p = new int[n + 1];
		
		for(int i = 1; i<=n; i++) {
			adj[i] = new ArrayList<>();
		}
		
		for(int i = 1; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			adj[u].add(v);
			adj[v].add(u);
		}
		
		dfs(1);
		for(int i = 2; i<=n; i++) {
			sb.append(p[i]).append('\n');
		}
		System.out.println(sb);
	}
}