/*
	Parametric Search: 답이 나올 수 있는 전체 범위에서 binary search를 통해, 가능한 해 중에서 문제에서 요구하는 최대 혹은 최소 해를 찾는다.

	1. 답이 될 수 있는 범위 설정 (left, right 변수)
	2. 해당 값(mid)이 답이 될 수 있는지 판별
 */

public class Solution {
	static int N; // 입국심사를 기다리는 사람의 수
	static int[] time; // 각 심사관이 한 명을 심사하는데 걸리는 시간
	static final int MAX_TIME = 1_000_000_000;
	static final int MAX_PEOPLE = 1_000_000_000;

	public long solution(int n, int[] times) {
		N = n;
		time = times;

		// 모든 사람이 심사를 받는데 걸리는 시간의 최솟값 x 를 구하라

		// Binary Search
		// x: 모든 사람이 심사를 받는데 걸리는 시간
		// 모든 사람 * 최소 시간 <= x <= 모든 사람 * 최대 시간
		long left = 1;
		long right = (long) MAX_PEOPLE * MAX_TIME; // 최대값
		while (left < right) {
			long mid = (left + right) / 2;
			// answer condition -> mid 시간 내에 모든 사람이 심사를 받을 수 있는가?
			if (isPossible(mid)) {
				right = mid;
			} else {
				left = mid + 1;
			}
		}

        // 최솟값을 리턴한다.
		return left;
	}

	public boolean isPossible(long x) {
		long n = N;
		for (int t : time) {
			n = n - (x / t); // t시간 내에 처리할 수 있는 사람 수를 뺀다.
		}
		return n <= 0;
	}
}