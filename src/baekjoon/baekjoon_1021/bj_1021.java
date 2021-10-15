package baekjoon.baekjoon_1021;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class bj_1021 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 큐의 크기
        int M = Integer.parseInt(st.nextToken()); // 뽑아내려고 하는 수의 개수
        int cnt = 0; // 2번, 3번 연산의 횟수
        Deque<Integer> deque = new LinkedList<>();

        // deque 초기화
        for (int i = 1; i <= N; i++) {
            deque.offerLast(i);
        }

        st = new StringTokenizer(br.readLine());
        while (M-- > 0) {
            int target = Integer.parseInt(st.nextToken());
            while (target != deque.peekFirst()) {
                deque.
            }
            deque.pollFirst();
        }

    }

}
