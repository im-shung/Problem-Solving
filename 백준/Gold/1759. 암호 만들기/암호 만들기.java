import java.io.*;
import java.util.*;

// DFS 응용

/*
    실수 목록
    1) HashSet 자료형
    2) 문자 하나씩 입력 받기 - st.nextToken().charAt(0)
    3) DFS 체크인/체크아웃 조건 - 자음/모음 개수 check
    4) answer 배열 따로 두기
    5) answer 배열 크기
    6) 중복이 없어야하기 때문에 answer는 체크아웃 하지 않는다
    7) dfs 처음 호출 시 매개값 -1로 시작
*/
public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static HashSet<Character> vowel = new HashSet<>(List.of('a', 'e', 'i', 'o', 'u'));
    static int L, C;
    static char[] input;
    static char[] answer;
    static int countV;
    static int countC;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        input = new char[C];
        answer = new char[L];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < C; i++) {
            input[i] = st.nextToken().charAt(0); // !!! 문자 입력받을 때 !!!

        }
        Arrays.sort(input);

        dfs(0, -1); // -1을 매개값으로 넣어줘야 현재 Character의 인덱스가 0부터 시작할 수 있다.
        System.out.println(sb);

    }

    static void dfs(int len, int current) {
        // 1. 목적지인가?
        if (len == L) {
            if (countV >= 1 && countC >= 2) {
                sb.append(answer).append("\n");
            }
        } else {
            // 2. 연결된 곳인가? - 생략
            // 3. 갈 수 있는가?
            for (int idx = current + 1; idx < C; idx++) {

                // 현재 Character이 자음인지 체크
                boolean isVowel = false;
                if (vowel.contains(input[idx])) {
                    isVowel = true;
                }

                // 4. 체크인 - 자음/모음 개수 저장
                if (isVowel) {
                    countV++;
                } else {
                    countC++;
                }

                // 현재 Character 저장
                answer[len] = input[idx];

                // 5. 간다 dfs
                dfs(len + 1, idx);

                // 6. 체크아웃 - 자음/모음 개수 저장했던거 원상복귀
                if (isVowel) {
                    countV--;
                } else {
                    countC--;
                }
            }
        }
    }
}
