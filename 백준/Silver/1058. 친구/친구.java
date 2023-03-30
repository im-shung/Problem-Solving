import java.io.*;
import java.util.*;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	static final int MAX = 51;
	
	static int N;
	static ArrayList<Integer>[] adjList;
	static boolean[] visit;
	static int ans;

	private static void input() throws IOException {
		N = Integer.parseInt(br.readLine());
		adjList = new ArrayList[MAX];
		visit = new boolean[MAX];
		for (int i = 0; i < N; i++) adjList[i] = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			String line = br.readLine();
			for(int j = 0; j < N; j++) {
				char s = line.charAt(j);
				
				if (s == 'Y') adjList[i].add(j);
			}
		}
		//System.out.println(Arrays.toString(adjList));
	}

	private static void pro() {
		for (int i = 0; i < N; i++) {
			// visit 배열을 초기화합니다. 
			Arrays.fill(visit, false);
			// 자신의 친구를 탐색합니다.
			dfs(i, 0);
			// 방문했던 친구의 수를 셉니다.
			ans = Math.max(ans, checkTwoFriend(i)); 
		}
	}
	
	private static int checkTwoFriend(int x) {
		int friend = 0;
		for (int i = 0; i < N; i++) {
			// 자기 자신은 제외합니다.
			if (x == i) continue;
			// 방문 표시가 되어있다면 2-친구입니다.
			if (visit[i]) friend++;
		}
		return friend;
	}
	
	private static void dfs(int x, int cnt) {
		// 방문 체크 합니다.
		visit[x] = true;
		// 깊이 2까지만 탐색합니다.
		if (cnt == 2) {
			return;
		}
		// 친구의 친구들을 탐색합니다.
		for (int nxt : adjList[x]) {
			// 65라인
			dfs(nxt, cnt + 1);
		}
		// 동일인물을 방문하면 안 되기 때문에 visit[x] = false는 실행하지 않습니다.
	}

	public static void main(String[] args) throws Exception {
		//br = new BufferedReader(new FileReader("src/input.txt"));
		/* 입력 */
		input();
		/* 처리 */
		pro();
		/* 출력 */
		System.out.println(ans);
		br.close();
	}
}


/*
65 라인에 
if (!visit[nxt]) 
	dfs(nxt, cnt + 1); 

이미 방문한 곳을 재방문하지 않는다면 문제가 있다.

<<map>>
NYYNYN
YNYNNN
YYNYNN
NNYNNN
YNNNNY
NNNNYN

0은 dfs(1) -> dfs(2)를 거쳐서 1과 2를 방문한다.
그리고 돌아와서 2는 이미 방문 표시가 되어 방문하지 않는다.
그러나 dfs(2) -> dfs(3)으로... 3을 갈 수 있는 기회를 놓친다.

 */


/*
 6
NYYNYN
YNYNNN
YYNYNN
NNYNNN
YNNNNY
NNNNYN
5
 */