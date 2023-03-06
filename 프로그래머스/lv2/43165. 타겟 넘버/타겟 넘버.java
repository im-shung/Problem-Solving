class Solution {
    static int count = 0;
    
    public int solution(int[] numbers, int target) {
        
        dfs(numbers, 0, 0, target);
        return count;
    }
    
    void dfs(int[] numbers, int idx, int result, int target) {
        // 1. 체크인
        // 2. 목적지인가?
        if (idx == numbers.length) {
            if (result == target) {
                count++;
            }
        } else {
            // 3. 연결된 곳인가?
            // 4. 갈 수 있는가?
            // 5. 간다.
            dfs(numbers, idx + 1, result + numbers[idx], target);
            dfs(numbers, idx + 1, result - numbers[idx], target);
        }
        
        
        // 6. 체크아웃
    }
}