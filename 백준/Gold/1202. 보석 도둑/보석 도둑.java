import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static StringTokenizer st;

    static int N, K;

    static List<Gem> inputGem;
    static List<Integer> bags;
    static PriorityQueue<Gem> pq;

    static void input() throws IOException {
//        br = new BufferedReader(new FileReader(new File("src/input.txt")));

        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        inputGem = new ArrayList<>(300_001);
        bags = new ArrayList<>(K);

        for (int gem = 0; gem < N; gem++) {
            st = new StringTokenizer(br.readLine());
            inputGem.add(
                    new Gem(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }

        for (int bag = 0; bag < K; bag++) {
            bags.add(Integer.parseInt(br.readLine()));
        }

    }

    static void pro() {
        // 보석 무게순 정렬
        inputGem.sort(Comparator.comparingInt(Gem::getWeight));

        // 가방 오름차순 정렬
        Collections.sort(bags);

        // 보석 높은 값 기준 힙
        pq = new PriorityQueue<Gem>(Comparator.comparingInt(Gem::getValue).reversed());

        int gem = 0;
        long totalPrice = 0;
        for (Integer bag : bags) {
            // 보석 리스트에서 제일 무게가 적은 보석과 가방의 무게를 비교한다.
            while (gem < N && inputGem.get(gem).weight <= bag) {
                pq.add(inputGem.get(gem));
                gem++;
            }

            if (!pq.isEmpty()) {
                totalPrice += pq.poll().value;
            }

        }
        System.out.println(totalPrice);
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}

class Gem {

    int weight;

    int value;

    public Gem(int weight, int value) {
        this.weight = weight;
        this.value = value;
    }

    public int getWeight() {
        return weight;
    }

    public int getValue() {
        return value;
    }

    @Override
    public String toString() {
        return "Gem{" +
                       "weight=" + weight +
                       ", price=" + value +
                       '}';
    }
}

