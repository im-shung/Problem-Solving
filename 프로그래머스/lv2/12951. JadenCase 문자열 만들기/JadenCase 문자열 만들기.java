/*
숫자 0~9까지의 아스키코드값은
48~57

영문a~z까지의 아스키코드값은

대문자 65~90

소문자 97~122
*/

class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        int n = s.length();
        char[] temp = new char[n];
        
        boolean isEmptyChar = true; // 공백 문자 다음이 첫 문자이므로,, 이전 char이 공백문자였는지 체크
        for(int i = 0; i < n; i++) {
            char val = s.charAt(i);
            // 공백문자
            if (val == ' ') {
                isEmptyChar = true;
                temp[i] = val;
            }
            // 대문자
            else if (isBig(val)) {
                if (isEmptyChar == false) { // val이 첫 글자가 아니다!
                    temp[i] = convertBigToSmall(val);
                } else { // val이 첫 글자다!
                    temp[i] = val;
                    isEmptyChar = false;    
                }
            }
            // 소문자
            else if (isSmall(val)) {
                if (isEmptyChar == false) { // val이 첫 글자가 아니다!
                    temp[i] = val;
                } else { // val이 첫 글자다!
                    temp[i] = convertSmallToBig(val);
                    isEmptyChar = false;    
                }
            }
            // 숫자
            else { // 숫자는 그대로
                temp[i] = val;
                isEmptyChar = false;
            }
        }        
        sb.append(String.valueOf(temp));
        return sb.toString();
    }
    
    private char convertSmallToBig(char x) {
        return (char) (x - 32);
    }
    
    private char convertBigToSmall(char x) {
        return (char) (x + 32);
    }
    
    private boolean isSmall(char x) {
        return (97 <= x && x <= 122);
    }
    
    private boolean isBig(char x) {
        return (65 <= x && x<= 90);
    }
}