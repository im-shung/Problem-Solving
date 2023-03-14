
/*
 * 조합문제
 * 1) 중복 없이
 * 2) 순서 고정 (알파벳이 암호에서 증가하는 순서)
 */

import java.io.*;
import java.util.*;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	static int L, C; // 암호 길이, 문자 종류
	static char[] answer, input;

	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		L = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());

		answer = new char[L];
		input = new char[C];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < C; i++) {
			input[i] = st.nextToken().charAt(0);
		}
		Arrays.sort(input);
		comb(0, 0);
		System.out.println(sb);
	}

	// cnt := cnt번째 카드 뽑기
	private static void comb(int cnt, int startIndex) {
		if (cnt == L) {
			int mo = 0, ja = 0;
			for (char a : answer) {
				if (a == 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u')
					mo++;
				else
					ja++;
			}
			if (mo >= 1 && ja >= 2) {
				for (char a : answer) 
					sb.append(a);
				sb.append("\n");
			}

			return;
		}
		for (int i = startIndex; i < C; i++) {
			answer[cnt] = input[i];
			comb(cnt + 1, i + 1);
		}
	}

}
