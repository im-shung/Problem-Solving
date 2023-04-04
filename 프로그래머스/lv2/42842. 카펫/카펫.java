class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {0, 0};
        int tmp = 1;
        boolean flag = false;
        for (int i = 3; i <= yellow+2; i++) { // 가로
            tmp = 0;
            for (int j = 3; j <= i; j++) { // 세로
                tmp += i-2;
                // System.out.println("i="+i+",j="+j+"tmp="+tmp);
                if (tmp == yellow) {
                    if (i*j != brown+yellow) continue;
                    
                    answer[0] = i; answer[1] = j;
                    flag = true;
                    break;
                }
            }
            if (flag) break;
        }
        
        return answer;
    }
}