import java.util.*;

class Solution {
    String[] arr = {"A", "E", "I", "O", "U"};
    HashMap<String, Integer> dic = new HashMap<>();
    int order = 0;
    
    public int solution(String word) {
        
        fuc("", 0);
        
        return dic.get(word);
    }
    
    void fuc(String word, int length) {
        if (length > 5) return;
        dic.put(word, order++);
        for(String ch : arr) {
            fuc(word + ch, length + 1);
        }
    }
}