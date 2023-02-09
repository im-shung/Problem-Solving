import java.io.*;
import java.util.*;

/*
문제 이해하기 - https://www.acmicpc.net/board/view/101300
맨 왼쪽 집에서부터 차를 타고 오른쪽으로 간다고 생각해봅시다. 이 때 모든 집까지의 거리는 줄어들 것입니다. 맨 왼쪽집과만 멀어지기 때문이죠.
계속 가다보니 모든 집과의 거리가 갑자기 늘어나기 시작하는 때가 있습니다.내 오른쪽에 있는 집보다 내 왼쪽에 있는 집이 더 많아져서 모든 집까의 거리는 증가하기 때문입니다.
즉 왼쪽부터 오른쪽으로 갈 때 모든 집까지의 거리가 증가하는 지, 감소하는 지는 내 왼쪽의 집의 갯수가 더 많나, 내 오른쪽의 집의 갯수가 더 많나에 달렸습니다.
따라서 왼쪽 집의 갯수가 오른쪽 집의 갯수를 넘어서기 직전이 모든 집까지의 거리가 최솟값이 되는 지점입니다.(함수로 따지면 기울기가 -에서 +로 변화가 생기는 지점)
이때 이것을 무조건 만족하는 지점이 중간값입니다. 중간값이면 왼쪽과 오른쪽에 있는 집의 갯수가 같게 되거나 같게 되는 구간의 왼쪽 끝이 되기 때문입니다.
 */

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int N;

    static int[] input;

    static void input() throws IOException {
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        input = new int[N + 1];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            input[i] = Integer.parseInt(st.nextToken());
        }

    }

    static void pro() {
        Arrays.sort(input);
        
        // 왼쪽 집의 갯수가 오른쪽 집의 갯수를 넘어서기 직전의 인덱스
        // 짝수인 경우 N / 2
        if (N % 2 == 0) {
            System.out.println(input[N / 2]);
        } 
        // 홀수인 경우 N / 2 + 1
        else {
            System.out.println(input[N / 2 + 1]);
        }
    }


    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}


