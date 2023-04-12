/*
조건1. 부분 수열
조건2. 합이 k
조건3. 여러 개가 도출되면, 가장 짧은 길이
출력: 위 조건을 만족하는 부분 수열의 시작 index와 마지막 index
*/
class Solution {
    static int n;
    static int[] dp;
    
    public int[] solution(int[] sequence, int k) {
        n = sequence.length;
        
        int[] answer = new int[2];

        int sp = 0; // start pointer
        int ep = 0; // end pointer
        int subSum = sequence[sp]; // 부분합의 초기값
        int minLength = 1_000_999, currLength = 0;
        while(sp <= ep && ep < n) { 
            
            //System.out.println("sp="+sp+", ep="+ep);
            currLength = ep - sp + 1;
               
            // 현재 부분합이 k다.
            if (subSum == k) {
                if (minLength > currLength) { 
                    answer[0] = sp;
                    answer[1] = ep;
                    minLength = currLength; // !! 실수
                }
                // start와 end pointer 둘다 증가
                subSum -= sequence[sp];
                sp++; 
                ep++;
                
                // start pointer의 값이 k보다 크다면, 부분합이 k보다 크다는 것을 확신할 수 있으므로 while문을 빠져나온다. 왜냐하면 수열은 오름차순이라서 뒤로 갈 수록 커진다.
                if (ep == n || sequence[sp] > k) { // !! 실수
                    break;
                }             
                subSum += sequence[ep];
            }

            
            // 현재 부분합이 k보다 작다.
            if (subSum < k) { // end pointer를 증가
                ep++;
                if (ep == n) break;
                subSum += sequence[ep];
            }
            // 현재 부분합이 k보다 크다.
            if (subSum > k) { // start pointer를 증가
                subSum -= sequence[sp];
                sp++;
                // start pointer의 값이 k보다 크다면, 부분합이 k보다 크다는 것을 확신할 수 있으므로 while문을 빠져나온다. 왜냐하면 수열은 오름차순이라서 뒤로 갈 수록 커진다.
                if (sequence[sp] > k) { // !! 실수
                    break;
                }

            }
            
        }
        
        
        
        return answer;

    }
    
    // sequence는 비내림차순이므로 합이 k보다 커지면, 가지치기가 가능하다.
    // 원소의 길이가 1_000_000이므로... 비트마스킹? 은 못 할 듯
    // dfs로 풀면 O(1_000_000)인가? 시간복잡도가 맞는지 모르겠다.
    // dfs를 풀면 시작위치를 모든 원소에게 주어야 하니까 O(N^2)인듯
    
    // 그러면 다시 새로 접근하자.
    // DP로 풀까?
    // 부분 집합이 아니고 부분 수열이니까 가능하다.
    
    // 음...DP로 풀려니까 부분수열의 합을 구하려면 이중for문을 돌려야한다.
    
    // 이제 알겠다. 투포인터!! 
    

}