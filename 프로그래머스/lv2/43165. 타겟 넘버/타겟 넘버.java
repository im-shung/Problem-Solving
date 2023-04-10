class Solution {
    static int n ;
    static int count = 0;
    static int[] snumbers;
    static int starget;
    
    public int solution(int[] numbers, int target) {
        n = numbers.length;
        snumbers = numbers;
        starget = target;
        
        dfs(0, 0, 0);
        return count;
    }
    
    private void dfs(int depth, int startIdx, int answer) {
        if (depth == n) {
            if (answer == starget) count++;
            return;
        }
        
        for (int i = startIdx; i < n; i++) {
            dfs(depth + 1, i + 1, answer + snumbers[i]);
            dfs(depth + 1, i + 1, answer - snumbers[i]);
        }
        
    }
        
}