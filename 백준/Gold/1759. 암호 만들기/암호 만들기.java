/*
암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다.
또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다.
즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.

새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다.
C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.
 */

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb;

    static HashSet<Character> vowel = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));

    static int L, C;

    static boolean[] visited;

    static char[] input;

    static char[] answer;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());
        sb = new StringBuilder();

        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        input = new char[C];
        visited = new boolean[C];
        answer = new char[L];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < C; i++) {
            input[i] = st.nextToken().charAt(0);
        }

        Arrays.sort(input);

    }

    static void pro() {
        dfs(-1, 0, 0, 0);

        System.out.println(sb.substring(0, sb.length() - 1));
    }

    static void dfs(int current, int ja, int mo, int length) {
        // 1. 체크인 - 생략 가능
        // 2. 목적지인가?
        if (length == L) {
            if (mo >= 1 && ja >= 2) {
                sb.append(answer).append("\n");
            }
        } else {
            // 3. 연결된 곳 순회 current ~ C
            for (int i = current + 1; i < C; i++) {
                // 4. 갈 수 있는가? - 생략 가능
                // 5. 간다. dfs
                answer[length] = input[i];
                if (vowel.contains(input[i])){
                    dfs(i, ja, mo + 1, length + 1);
                } else {
                    dfs(i, ja + 1 , mo, length + 1);
                }
            }
        }

        // 6. 체크아웃 - 생략 가능
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }
}
