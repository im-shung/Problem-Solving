import java.util.*;

class Solution {
    public int solution(int[] topping) {
        HashSet<Integer> set = new HashSet<>();
        int N = topping.length;
        int[] arr1 = new int[N];
        int[] arr2 = new int[N];
        
        for(int i = 0; i < N; i++) {
            set.add(topping[i]);
            arr1[i] = set.size();
        }
        
        set.clear();
        
        for (int i = N - 1; i >= 0; i--) {
            set.add(topping[i]);
            arr2[i] = set.size();
        }
        
        int answer = 0;
        for (int i = 0; i < N - 1; i++) {
            if (arr1[i] == arr2[i + 1]) {
                answer++;
            }
        }
        

        return answer;
    }
}