import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> minHeap = new PriorityQueue();
        for(int sc : scoville) minHeap.offer(sc);
        
        int answer = 0;
        int min = minHeap.peek();
        while(K > min && minHeap.size() > 1) {
            answer++;
            int a = minHeap.poll();
            int b = minHeap.poll();
            minHeap.offer(a + 2 * b);
            min = minHeap.peek();
        }
        
        if (K > min) {
            return -1;
        }
       
        return answer;
    }
}