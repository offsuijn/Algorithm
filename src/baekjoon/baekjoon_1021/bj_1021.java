package baekjoon.baekjoon_1021;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class bj_1021 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 큐의 크기
        int M = Integer.parseInt(st.nextToken()); // 뽑아내려고 하는 수의 개수
        int cnt = 0; // 2번, 3번 연산의 합
        LinkedList<Integer> deque = new LinkedList<Integer>();

        // deque 초기화
        for (int i = 1; i <= N; i++) {
            deque.offerLast(i);
        }

        st = new StringTokenizer(br.readLine());
        while (M-- > 0) {
            int target = Integer.parseInt(st.nextToken()); // 뽑아내려고 하는 수

            if (target != deque.peekFirst()) {
                int k = deque.indexOf(target) + 1; // 뽑아내려고 하는 수의 위치
                int center = 0; // 큐의 가운데

                if (deque.size() % 2 == 1) { // size가 홀수인 경우
                    center = deque.size() / 2 + 1;
                }
                else { // size가 짝수인 경우
                    center = deque.size() / 2;
                }

                if (k <= center) { // 뽑아내려고 하는 수가 가운데이거나 가운데보다 앞에 있는 경우
                    int l = k - 1;
                    while (l-- > 0) { // target이 가장 앞에 오도록 왼쪽으로 한 칸 이동
                        cnt++;
                        deque.offerLast(deque.pollFirst());
                    }
                }
                else { // 뽑아내려고 하는 수가 가운데보다 뒤에 있는 경우
                    int l = deque.size() - k + 1;
                    while (l-- > 0) { // target이 가장 앞에 오도록 오른쪽으로 한 칸 이동
                        cnt++;
                        deque.offerFirst(deque.pollLast());
                    }
                }
            }
            deque.pollFirst();
        }

        sb.append(cnt);
        System.out.println(sb);
    }

}
