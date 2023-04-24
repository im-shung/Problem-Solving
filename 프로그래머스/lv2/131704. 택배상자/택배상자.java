import java.util.*;

class Solution {
    public int solution(int[] order) {
        Deque<Integer> stack = new ArrayDeque<>();
        int n = order.length;
        int num = 1;
        int top = 0;
        int answer = 0;
        while (0 <= top && top < n) {
            // System.out.println("num = " + num + ", order[top] = " + order[top]);
            if (!stack.isEmpty() && stack.peek() > order[top]) {
                break;
            }
            
            while (num <= order[top]) {
                stack.addFirst(num); // 보조 컨테이너 벨트에 보관합니다.
                num++; 
            }
            // System.out.println("stack = " + stack);
            if (stack.peek() == order[top]) {    
                answer++; 
                stack.pollFirst();  // 보조 컨테이너 벨트에서 뺍니다. 
            } 
            top++;
            
        }
        
        //
        
        return answer;
    }
}