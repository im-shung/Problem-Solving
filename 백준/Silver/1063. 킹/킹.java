import java.io.*;
import java.util.*;

class Direction {

//    static final int[] DY = {-1, 1, 0, 0};
//    static final int[] DX = {0, 0, -1, 1};

    int row;
    int col;

    public Direction(int row, int col) {
        this.row = row;
        this.col = col;
    }

}

class Location {

    char col;
    int row;

    public Location(String str) {
        this.col = str.charAt(0);
        this.row = Integer.parseInt(String.valueOf(str.charAt(1)));
    }

    @Override
    public String toString() {
        return col + String.valueOf(row);
    }
}

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static final int SIZE = 8;
    static String king, stone;
    static int N;

    static HashMap<String, Direction> direction = new HashMap<>(Map.of(
            "R", new Direction(0, 1),
            "L", new Direction(0, -1),
            "B", new Direction(-1, 0),
            "T", new Direction(1, 0),
            "RT", new Direction(1, 1),
            "LT", new Direction(1, -1),
            "RB", new Direction(-1, 1),
            "LB", new Direction(-1, -1)
    ));

    public static boolean isOut(int row, char col) {
        return (row < 1 || row > SIZE || col < 'A' || col > 'H');
    }

    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        Location king = new Location(st.nextToken());
        Location stone = new Location(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        String op;
        for (int i = 0; i < N; i++) {
            op = br.readLine();
            int row = direction.get(op).row;
            int col = direction.get(op).col;

            // 킹의 범위를 확인한다.
            if (!isOut(king.row + row, (char) (king.col + col))) {
                // 돌의 범위를 확인한다.
                if (king.row + row == stone.row && (char) (king.col + col) == stone.col) {
                    if (!isOut(stone.row + row, (char) (stone.col + col))) {
                        stone.row += row;
                        stone.col += col;
                        king.row += row;
                        king.col += col;
                    }
                } else {
                    king.row += row;
                    king.col += col;
                }
            }
        }

        sb.append(king).append("\n").append(stone);
        System.out.println(sb);
    }
}
