import java.util.*;

class Solution {
    
    static class Element implements Comparable<Element> {
        
        String full;
        
        public Element(String full) {
            this.full = full;
       }
        
        @Override
        public int compareTo(Element o) {
            return Integer.parseInt(o.full + this.full) - Integer.parseInt(this.full + o.full);
        }
        
        public String toString() {
            return "full="+full;
        }
        // return a+b < b+a
    }
    
    public String solution(int[] numbers) {
        // int배열에서 최대 길이를 구한다.
        Arrays.sort(numbers);
        int n = numbers.length;
        int max = numbers[n-1];
        if (max == 0) return "0";

        // test
        // System.out.println(maxLen);
        
        // 최대길이만큼의 자릿수배열을 갖는 Element 배열을 생성한다.
        Element[] elements = new Element[n];
        for (int i = 0; i < n; i++) {
            elements[i] = new Element(numbers[i] + "");
        }

        // 정렬 
        Arrays.sort(elements);
        
        //test
        // System.out.println(Arrays.toString(elements));
        
        StringBuilder sb = new StringBuilder();
        for (Element e : elements) {
            sb.append(e.full);
        }

        return sb.toString();
    }
}