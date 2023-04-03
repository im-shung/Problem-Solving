import java.util.*;

class Solution {
    
    static int N;
    static char[] num, answer;
    static boolean[] visit;
    static StringBuilder sb = new StringBuilder();
    static int ans;
    static Set<Integer> memo = new HashSet<>();
    
    public int solution(String numbers) {
        N = numbers.length();
        num = numbers.toCharArray();
        visit = new boolean[N];
        answer = new char[N];
        System.out.println(Arrays.toString(num));
        
        for(int n = 1; n <= N; n++) {
            dfs(n, 0);
        }

        return ans;
    }
    
    public void dfs(int depth, int cnt) {
        
        if (cnt == depth) {
            sb.setLength(0);
            for (int i = 0; i < depth; i++) {
                sb.append(answer[i]);
            }
            
            
            int num = Integer.parseInt(sb.toString());
            if (memo.contains(num)) return;
            memo.add(num);
            if (num >= 2 && isPrime(num)) {
                System.out.println(num);
                ans++;
            }
            return;
        }
        
        
        for (int i = 0; i < N; i++) {
            if (!visit[i]) {
                visit[i] = true;
                answer[cnt] = num[i];
                
                dfs(depth, cnt + 1);
                
                visit[i] = false;
            }
        }
       
    }
    
    private boolean isPrime(int num) {

        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}