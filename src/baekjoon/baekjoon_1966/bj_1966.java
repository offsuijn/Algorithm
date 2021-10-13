package baekjoon.baekjoon_1966;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class bj_1966 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int K = Integer.parseInt(br.readLine()); // test 개수

        while (K-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int N = Integer.parseInt(st.nextToken()); // 문서의 개수
            int M = Integer.parseInt(st.nextToken()); // target 문서가 Queue에서 몇 번째에 놓여 있는지
            int cnt = 0; // 인쇄된 횟수
            Queue<int[]> queue = new LinkedList<int[]>();

            // Queue 초기화
            st = new StringTokenizer(br.readLine(), " ");
            for (int i = 0; i < N; i++) {
                int[] arr = new int[2];
                arr[0] = i; // 초기 위치
                arr[1] = Integer.parseInt(st.nextToken()); // value
                queue.offer(arr);
            }

            // target 문서 탐색
            while (true) {
                boolean highest = true; // Queue 중 중요도가 가장 높으면 true

                for (int[] a : queue) {
                    if (queue.peek()[1] < a[1]) { // 현재 문서보다 중요도가 높은 문서가 하나라도 있는 경우
                        queue.offer(queue.poll()); // Queue의 가장 뒤에 재배치
                        highest = false;
                        break;
                    }
                }

                if (highest) {
                    cnt++;

                    if (queue.peek()[0] == M) { // poll할 문서의 초기값이 M과 같은 경우
                        sb.append(cnt).append('\n'); // 인쇄 순서 출력하고 탈출
                        break;
                    }
                    queue.poll();
                }

            }

        }
        System.out.println(sb);

    }

}
