import java.io.*;
import java.util.*;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();

	static int N, K, M;

	static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		// 배열을 입력 받을 필요가 없이, K번째 인덱스의 위치만 계산한다.
		br.readLine(); 
	}

	public static void pro() throws Exception {
		for (int i = 1; i <= M; i++) {
			int len = Integer.parseInt(br.readLine());
			// len이 양수냐 음수냐를 나눠서 생각한다.
			// K의 위치를 뒤집는다.
			// len이 양수이면 1부터 len만큼 뒤집기, 음수이면 n부터 -len크기만큼 뒤집는다.
			if (len > 0 && K <= len) { 				
				K = len - K + 1;			// 끝(len)에서 K만큼 왼쪽으로 이동
			} 
            else if (len < 0 && K > N + len) { 					
				K = (2 * N) - K + len + 1;	// 끝(2*n)에서 K만큼 왼쪽으로 이동, -len만큼 왼쪽으로 이동
			}
			// 인덱스가 1부터 시작하므로 1을 더해준다.
		}
	}
	

	public static void main(String[] args) throws Exception {
		/* 입력 */
		input();
		/* 처리 */
		pro();
		/* 출력 */
		System.out.println(K);
	}
}
