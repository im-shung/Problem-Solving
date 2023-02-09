class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        
        int maxA = 0;
        int maxB = 0;
        for(int i = 0; i < sizes.length; i++) {
            
            if (sizes[i][0] > sizes[i][1]) {
                maxA = Math.max(sizes[i][0] , maxA);
                maxB = Math.max(sizes[i][1] , maxB);
            } else {
                maxA = Math.max(sizes[i][1] , maxA);
                maxB = Math.max(sizes[i][0] , maxB);
            }
        }
        System.out.println(maxA + " "+ maxB);
        answer = maxA * maxB;
        return answer;
    }
}