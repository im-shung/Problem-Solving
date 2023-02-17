import java.io.*;
import java.util.*;

// DFS

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int N, K;
    static String[] words;
    static char[] baseWords = {'a', 'c', 'i', 'n', 't'};
    static boolean[] alphabet = new boolean[26];
    static int result;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        words = new String[N];

        for (int i = 0; i < N; i++) {
            words[i] = br.readLine();
        }

        // 읽을 수 있는 알파벳을 true 표시한다.
        for (char baseWord : baseWords) {
            alphabet[baseWord - 'a'] = true;
        }

        dfs(0, 0);
        System.out.println(result);
    }

    private static void dfs(int x, int len) {
        // 목적지인가?
        if (len == K - 5) {
            int subResult = 0;
            for (String word : words) {
                int wordLength = word.length();
                int cnt = 0;
                for (int i = 0; i < word.length(); i++) {
                    if (alphabet[word.charAt(i) - 'a']) {
                        cnt++;
                    }
                }

                if (cnt == wordLength) {
                    subResult++;
                }
            }
            // 학생들이 읽을 수 있는 단어 개수의 최댓값
            result = Math.max(subResult, result);
        } else {
            // 연결된 곳인가?
            for (int c = x; c < 26; c++) {
                // 갈 수 있는가?
                if (!alphabet[c]) {
                    // 체크인 - 읽을 수 있는 알파벳을 true 표시한다.
                    alphabet[c] = true;

                    // 5. 간다 dfs
                    dfs(c, len + 1);

                    // 체크 아웃
                    alphabet[c] = false;
                }
            }
        }
    }
}
