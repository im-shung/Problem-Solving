import java.util.*;

class Solution {
	static int res = 100;
	static boolean[] visit;

	public int solution(String begin, String target, String[] words) {
		visit = new boolean[words.length];
        
		dfs(begin, target, words, 0);
        if (res == 100) return 0;
		else return res;
	}

	public void dfs(String begin, String target, String[] words, int length) {
		// 목적지인가? -> begin과 target이 같으면
		if (begin.equals(target)) {
			res = Math.min(res, length);
		} else {
			// 연결된 곳인가? -> words에 있는 단어들
			for (int i = 0; i < words.length; i++) {
				if (!visit[i]) {
					// 알파벳 하나만 차이 나는지 체크
					int cnt = 0;
					for (int w = 0; w < words[i].length(); w++) {
						if (words[i].charAt(w) != begin.charAt(w))
							cnt++;
					}
					// 갈 수 있는가?
					if (cnt == 1) {
						// 체크인
						visit[i] = true;
						// 간다
						dfs(words[i], target, words, length + 1);
						// 체크아웃
						visit[i] = false;
					}
				}
			}
		}

	}
}