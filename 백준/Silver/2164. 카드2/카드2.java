import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.*;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	static int N;
	static Deque<Integer> que = new ArrayDeque<>();
	public static void main(String[] args) throws Exception {
		N = Integer.parseInt(br.readLine());
		
		// 큐 삽입
		for (int i = 1; i <= N; i++) {
			que.addLast(i);
		}
		
		// 큐 size가 1이 될 때까지 반복
		while (!que.isEmpty()) {
			// 1. front를 버림
			int front = que.pollFirst();
			
			// 2. 그 다음 값을 rear로 보냄
			if (que.size() >= 1)
				que.addLast(que.pollFirst());
			else
				System.out.println(front);
		
		}
	}

}
