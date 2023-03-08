import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> m = new HashMap<>();
        for (String p : participant) {
            if (m.containsKey(p)) 
                m.put(p, m.get(p) + 1);
            else 
                m.put(p, 1);
        }
        String answer = "";
        for (String c : completion) {
            m.put(c, m.get(c) - 1);
        }
        for (String k : m.keySet()) {
            if (m.get(k) > 0) answer = k;
        }
        return answer;
    }
}