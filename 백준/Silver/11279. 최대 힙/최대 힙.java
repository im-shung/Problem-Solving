import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static MaxHeap maxHeap = new MaxHeap(100_001);

    static int N;

    static void input() throws IOException {
//        br = new BufferedReader(new FileReader(new File("src/input.txt")));

        N = Integer.parseInt(br.readLine());
    }

    static void pro() throws IOException {
        // x가 자연수라면 배열에 x를 삽입
        // x가 0이라면 배열에서 최대값을 출력하고, 제거한다.
        for (int i = 0; i < N; i++) {
            int val = Integer.parseInt(br.readLine());
            if (val == 0) {
                if (maxHeap.list.size() == 1) { // 비어있는 배열인 경우 0을 출력한다
                    System.out.println(0);
                } else { // 최대값을 출력하고 제거한다.
                    System.out.println(maxHeap.delete());
                }
            } else { // 삽입한다.
                maxHeap.insert(val);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        input();
        pro();
    }

}

class MaxHeap {

    List<Integer> list;

    public MaxHeap(int n) {
        list = new ArrayList<>(n);
        list.add(0);
    }

    // 트리 삽입
    void insert(int val) {
        //1. 마지막에 추가
        list.add(val);
        //2. 부모랑 조건 비교, 교환
        int current = list.size() - 1;
        int parent = current / 2;
        while (true) {
            //1. current 가 root면 탈출
            //2. 부모, 자식 조건을 만족하면 탈출
            if (current == 1 || list.get(parent) > list.get(current)) {
                break;
            }

            int temp = list.get(parent);
            list.set(parent, list.get(current));
            list.set(current, temp);

            current = parent;
            parent = current / 2;
        }
    }

    int delete() {
        //1. Root 제거
        int top = list.get(1);
        //2. 마지막 노드를 Root로 이동
        list.set(1, list.get(list.size() - 1));
        list.remove(list.size() - 1);
        //3. 왼쪽, 오른쪽 중 조건이 안맞는 것을 선택 후 조건에 맞게 SWAP
        int currentNode = 1;
        while (true) {
            int leftNode = currentNode * 2;
            int rightNode = currentNode * 2 + 1;

            if (leftNode >= list.size()) {
                break;
            }

            int targetValue = list.get(leftNode);
            int targetNode = leftNode;

            if (rightNode < list.size() && targetValue < list.get(rightNode)) {
                targetNode = rightNode;
                targetValue = list.get(rightNode);
            }

            if (list.get(currentNode) < targetValue) {
                int temp = list.get(currentNode);
                list.set(currentNode, list.get(targetNode));
                list.set(targetNode, temp);
                currentNode = targetNode;
            } else {
                break;
            }
        }
        return top;
    }
}
