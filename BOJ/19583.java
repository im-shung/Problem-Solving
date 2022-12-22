import java.awt.Point;
import java.io.*;
import java.text.ParseException;
import java.util.*;

/*
time 계산: String -> int
HashSet 이용
*/

public class Main {

    static HashSet<String> names = new HashSet<>();
    static HashSet<String> result = new HashSet<>();

    static int startTime, endTime, quitTime, userTime;
    static String name;

    public static void main(String[] args) throws IOException, ParseException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        startTime = toIntTime(st.nextToken());
        endTime = toIntTime(st.nextToken());
        quitTime = toIntTime(st.nextToken());

        String line;
        while ((line = br.readLine()) != null) {
            st = new StringTokenizer(line);

            userTime = toIntTime(st.nextToken());
            name = st.nextToken();

            if (result.contains(name)) {
                continue;
            }

            if (userTime <= startTime) {
                names.add(name);
            } else if (endTime <= userTime && userTime <= quitTime) {
                if (names.contains(name)) {
                    result.add(name);
                }
            }

        }

        System.out.println(result.size());

    }

    static int toIntTime(String s) {
        int h = Integer.parseInt(s.substring(0, 2));
        int m = Integer.parseInt(s.substring(3, 5));

        return h * 60 + m;
    }

}
