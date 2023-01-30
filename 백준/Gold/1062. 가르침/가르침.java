/*
남극언어의 모든 단어는 "anta"로 시작되고, "tica"로 끝난다.
남극언어에 단어는 N개 밖에 없다고 가정한다. 학생들이 읽을 수 있는 단어의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N과 K가 주어진다. N은 50보다 작거나 같은 자연수이고, K는 26보다 작거나 같은 자연수 또는 0이다.
둘째 줄부터 N개의 줄에 남극 언어의 단어가 주어진다. 단어는 영어 소문자로만 이루어져 있고, 길이가 8보다 크거나 같고, 15보다 작거나 같다.
모든 단어는 중복되지 않는다.
 */

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static final int ALPHABET = 26;

    static int N, K;
    static boolean[] visited;
    static String[] words;
    static int result = 0;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());


        visited = new boolean[ALPHABET];
        words = new String[N];

        for (int i = 0; i < N; i++) {
            words[i] = br.readLine();
        }

        for (char c = 'a'; c <= 'z'; c++) {
            dfs(c, 1);
        }

        System.out.println(result);
    }

    // a, c, i, n, t
    static void dfs(char x, int height) {
        // 1. 체크인
        visited[x - 'a'] = true;

        // 2. 목적지인가?
        if (height == K) {
            int cnt = 0;
            for (String word : words) {
                int len = 0;
                for (int i = 0; i < word.length(); i++) {
                    if (visited[word.charAt(i) - 'a']) {
                        len++;
                    } else {
                        break;
                    }
                }
                if (len == word.length()) {
                    cnt++;
                }
            }
            result = Math.max(result, cnt);
        } else {
            // 3. 연결된 곳을 순회
            for (char c = x; c <= 'z'; c++) {
                // 4. 갈 수 있는가?
                if (!visited[c - 'a']) {
                    // 5. 간다.
                    dfs(c, height + 1);
                }
            }
        }

        // 6. 체크아웃
        visited[x - 'a'] = false;
    }

}
