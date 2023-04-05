import java.util.*;

class Solution {
    
    static class Element implements Comparable<Element> {
        
        int[] su; // 자릿수배열
        String full; // 기존 수
        
        public Element(String full, int maxLen) {
            this.full = full;
            
            // 자릿수배열 생성
            su = new int[maxLen];
            for (int i = 0; i < maxLen; i++) {
                if (i < full.length()) {
                    su[i] = full.charAt(i) -'0'; // full.charAt(i) 는 0~9까지
                } else { // 기존 수의 길이보다 maxLen이 클 때.. 이전 수를 넣는다.
                    su[i] = su[i-1];
                }
            }
       }
        
        @Override
        public int compareTo(Element o) {
            int i;
            for (i = 0; i < this.su.length; i++) {
                if (o.su[i] != this.su[i]) break;
            }
            return o.su[i] - this.su[i];
        }
        
        public String toString() {
            return "su="+Arrays.toString(su) +",full="+full;
        }
    }
    
    public String solution(int[] numbers) {
        
        // int배열에서 최대 길이를 구한다.
        Arrays.sort(numbers);
        int n = numbers.length;
        int max = numbers[n-1];
        int maxLen = (max+"").length();

        
        // 최대길이만큼의 자릿수배열을 갖는 Element를 생성한다.
        Element[] elements = new Element[n];
        for (int i = 0; i < n; i++) {
            elements[i] = new Element(numbers[i] + "", maxLen);
        }

        // 정렬 
        Arrays.sort(elements);
        
        //test
        System.out.println(Arrays.toString(elements));
        
        StringBuilder sb = new StringBuilder();
        for (Element e : elements) {
            sb.append(e.full);
        }

        return sb.toString();
    }
}