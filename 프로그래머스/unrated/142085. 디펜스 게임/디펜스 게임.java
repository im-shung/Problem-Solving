import java.util.*;

class Solution {
    public int solution(int n, int k, int[] enemy) {
        int answer = 0;
        
        // 최대 힙 생성
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        // 라운드를 돈다.
        for (int e : enemy) {
            // 현재 enemy를 최대 힙에 삽입합니다.
            pq.add(e);
            // 현재 enemy의 공격을 막지 못하고, 무적권 스킬을 쓸 수 있다면
            if (n < e && k > 0) {
                // 지나온 라운드에서 최대 enemy를 가진 라운드에 무적권 스킬을 사용합니다.
                // 해당 enemy값을 가지고 있는 병사에 더해줍니다.
                n += pq.poll();
                // 무적권 스킬 - 1 
                k--;
            } 
            // 현재 enemy를 감소시킵니다.
            n -= e;
            
            // 현재 병사가 음수라면 게임이 종료됩니다.
            if (n < 0) 
                break;
            
            answer++;
            
            
        }
        return answer;
    }
}