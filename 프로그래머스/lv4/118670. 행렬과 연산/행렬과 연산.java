import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int[][] solution(int[][] rc, String[] operations) {
        int[][] answer = new int[rc.length][rc[0].length];

        Deque<Integer> left = new ArrayDeque<>();
        Deque<Deque<Integer>> mid = new ArrayDeque<>();
        Deque<Integer> right = new ArrayDeque<>();

        // 1. 초기화
        for (int i = 0; i < rc.length; i++) {
            left.addLast(rc[i][0]);
            Deque<Integer> midEachRowQueue = new ArrayDeque<>();
            for (int j = 1; j < rc[i].length - 1; j++) {
                midEachRowQueue.addLast(rc[i][j]);
            }
            mid.addLast(midEachRowQueue);
            right.addLast(rc[i][rc[i].length - 1]);
        }

        // 2. 연산
        for (String operation : operations) {
            // 2-1. ShiftRow 연산
            if (operation.equals("ShiftRow")) {
                left.addFirst(left.pollLast());
                right.addFirst(right.pollLast());
                mid.addFirst(mid.pollLast());
            }
            else if (operation.equals("Rotate")) {
                mid.peekFirst().addFirst(left.pollFirst());
                right.addFirst(mid.peekFirst().pollLast());
                mid.peekLast().addLast(right.pollLast());
                left.addLast(mid.peekLast().pollFirst());
            }
        }
        
        // 3. answer 로 큐값 옮기기
        for (int i = 0; i < answer.length; i++) {
            answer[i][0] = left.pollFirst();
            Deque<Integer> midEachRowQueue = mid.pollFirst();
            for (int j = 1; j < answer[i].length - 1; j++) {
                answer[i][j] = midEachRowQueue.pollFirst();
            }
            answer[i][answer[i].length - 1] = right.pollFirst();
        }

        
        return answer;
    }
}