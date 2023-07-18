import java.util.*;

class Solution {
    public int solution(int[] topping) {
        HashSet<Integer> hs = new HashSet<>();
        int n = topping.length;
        int[] a1 = new int[n];
        int[] a2 = new int[n];
        
        for(int i=0; i<n; i++){
            hs.add(topping[i]);
            a1[i] = hs.size();
        }
        hs.clear();
        for(int i=n-1; i>-1; i--){
            hs.add(topping[i]);
            a2[i] = hs.size();
        }
        int answer = 0;
        for(int i=0; i<n-1; i++){
            if(a1[i] == a2[i+1]){
                answer++;
            }
        }
        return answer;
    }
}