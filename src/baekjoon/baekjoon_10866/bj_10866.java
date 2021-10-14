package baekjoon.baekjoon_10866;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class bj_10866 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        Deque<Integer> deque = new LinkedList<>();
        int N = Integer.parseInt(br.readLine());

        while (N-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            switch (st.nextToken()) {
                case "push_front" :
                    deque.addFirst(Integer.parseInt(st.nextToken()));
                    break;

                case "push_back" :
                    deque.addLast(Integer.parseInt(st.nextToken()));
                    break;

                case "pop_front" :
                    if (deque.isEmpty()) { // 덱에 들어있는 정수가 없는 경우 -1을 출력
                        sb.append(-1).append('\n');
                        break;
                    }
                    sb.append(deque.pollFirst()).append('\n');
                    break;

                case "pop_back" :
                    if (deque.isEmpty()) {
                        sb.append(-1).append('\n');
                        break;
                    }
                    sb.append(deque.pollLast()).append('\n');
                    break;

                case "size" :
                    sb.append(deque.size()).append('\n');
                    break;

                case "empty" :
                    if (deque.isEmpty()) { // 덱이 비어있으면 1을, 아니면 0을 출력
                        sb.append(1).append('\n');
                        break;
                    }
                    sb.append(0).append('\n');
                    break;

                case "front" :
                    if (deque.isEmpty()) {
                        sb.append(-1).append('\n');
                        break;
                    }
                    sb.append(deque.peekFirst()).append('\n');
                    break;

                case "back" :
                    if (deque.isEmpty()) {
                        sb.append(-1).append('\n');
                        break;
                    }
                    sb.append(deque.peekLast()).append('\n');
                    break;
            }
        }

        System.out.println(sb);
    }

}
