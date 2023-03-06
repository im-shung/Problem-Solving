import java.util.*;

class Solution {
    static int[] parent;
    
    public int solution(int n, int[][] computers) {
        
        // 초기화
        parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        
        // union
        for(int a = 0; a < n; a++) {
            for (int b = 0; b < n; b++) {
                if (computers[a][b] == 1 && a != b) {
                    union(a, b);
                }
            }
        }
        
        // find -> 집합의 대표 번호를 set에 넣는다.
        HashSet<Integer> set = new HashSet<>();
        for (int i = 0; i < n; i++) {
            set.add(find(i));
        }
        
        // set의 size가 네트워크의 개수와 같다.
        return set.size();
    }
    
    
    public void union(int node1, int node2) {
        int root1 = find(node1);
        int root2 = find(node2);
        if (root1 < root2) parent[root1] = root2;
        else parent[root2] = root1;
    }
    
    public int find(int node) {
        if (node == parent[node]) {
            return node;
        }
        return parent[node] = find(parent[node]);
    }
}