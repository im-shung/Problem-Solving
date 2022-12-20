import java.awt.Point;
import java.io.*;
import java.util.*;

public class Main {

    static Queue<Point> leftQueue = new LinkedList<>();
    static Queue<Point> rightQueue = new LinkedList<>();
    static HashMap<String, Point> pointDictionary = new HashMap<>();

    static String firstLeft;
    static String firstRight;
    static String[][] points = new String[3][10];
    static int[][] leftRightBasis = new int[3][10];
    static int result = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        firstLeft = st.nextToken();
        firstRight = st.nextToken();
        String[]  input = br.readLine().split("");

        initiatePoints();

        for (String alphabet : input) {
            Point point = getPointByAlphabet(alphabet);
            if (isRightFingerPart(point)) {
                rightQueue.offer(point);
            } else {
                leftQueue.offer(point);
            }
        }
        result += calculateTime(getPointByAlphabet(firstLeft), leftQueue) + calculateTime(getPointByAlphabet(firstRight), rightQueue);
        System.out.println(result);
    }

    static int calculateTime(Point first, Queue<Point> queue) {
        int time = 0;
        Point now = first;

        while (!queue.isEmpty()) {
            Point next = queue.poll();
            time += Math.abs(now.x - next.x) + Math.abs(now.y - next.y);
            time += 1;

            now = next;
        }

        return time;
    }

    static void initiatePoints() {
        points[0] = new String[]{"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"};
        points[1] = new String[]{"a", "s", "d", "f", "g", "h", "j", "k", "l"};
        points[2] = new String[]{"z", "x", "c", "v", "b", "n", "m"};

        leftRightBasis[0] = new int[]{0, 0, 0, 0, 0, 1, 1, 1, 1, 1};
        leftRightBasis[1] = new int[]{0, 0, 0, 0, 0, 1, 1, 1, 1, 0};
        leftRightBasis[2] = new int[]{0, 0, 0, 0, 1, 1, 1, 0, 0, 0};

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 10; j++) {
                if (i == 1 && j > 8 || i == 2 && j > 6){
                    continue;
                }
                pointDictionary.put(points[i][j], new Point(i, j));
            }
        }
    }

    static Point getPointByAlphabet(String alphabet) {
        return pointDictionary.get(alphabet);
    }

    static boolean isRightFingerPart(Point point) {
        return leftRightBasis[point.x][point.y] == 1;
    }

}
