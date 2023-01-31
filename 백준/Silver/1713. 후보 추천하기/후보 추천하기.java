/*
학생들이 추천을 시작하기 전에 모든 사진틀은 비어있다.
어떤 학생이 특정 학생을 추천하면, 추천받은 학생의 사진이 반드시 사진틀에 게시되어야 한다.
비어있는 사진틀이 없는 경우에는 현재까지 추천 받은 횟수가 가장 적은 학생의 사진을 삭제하고, 그 자리에 새롭게 추천받은 학생의 사진을 게시한다. 이때, 현재까지 추천 받은 횟수가 가장 적은 학생이 두 명 이상일 경우에는 그러한 학생들 중 게시된 지 가장 오래된 사진을 삭제한다.
현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우에는 추천받은 횟수만 증가시킨다.
사진틀에 게시된 사진이 삭제되는 경우에는 해당 학생이 추천받은 횟수는 0으로 바뀐다.

 */

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int N, S;

    static Person[] people;

    static void input() throws IOException {
        N = Integer.parseInt(br.readLine());
        S = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());

    }

    static void pro() {

        people = new Person[101];

        List<Person> list = new ArrayList<>();
        for (int sequence = 0; sequence < S; sequence++) {
            int num = Integer.parseInt(st.nextToken());
            if (people[num] == null) {
                people[num] = new Person(num, 0, sequence, false);
            }

            if (people[num].isIn) {
                people[num].count++;
            } else {
                if (list.size() == N) {
                    Collections.sort(list);
                    Person removeTarget = list.remove(N - 1); // 큐의 poll 처럼 객체를 반환
                    removeTarget.isIn = false;
                    removeTarget.count = 0;
                }
                people[num].count = 1;
                people[num].isIn = true;
                people[num].timestamp = sequence;
                list.add(people[num]);
            }
        }

        list.sort(Comparator.comparingInt(o -> o.number));

        StringBuilder sb = new StringBuilder();
        list.forEach(person -> sb.append(person.number).append(" "));
        System.out.println(sb);

    }


    public static void main(String[] args) throws IOException {
        input();
        pro();
    }
}

class Person implements Comparable<Person> {

    int number;

    int count;

    int timestamp;

    boolean isIn;

    public Person(int number, int count, int timestamp, boolean isIn) {
        this.number = number;
        this.count = count;
        this.timestamp = timestamp;
        this.isIn = isIn;
    }

    @Override
    public int compareTo(Person o2) {
        int comp1 = o2.count - count;
        if (comp1 == 0) {
            return o2.timestamp - timestamp;
        } else {
            return comp1;
        }
    }
}
