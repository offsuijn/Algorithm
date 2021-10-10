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
        StringTokenizer st;

        int K = Integer.parseInt(br.readLine());

        while (K-- > 0) {
            st = new StringTokenizer(br.readLine(), " ");
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int targ = M;

            Queue<Integer> queue = new LinkedList<>();

            st = new StringTokenizer(br.readLine(), " ");
            while (st.hasMoreTokens()) {
                queue.offer(Integer.parseInt(st.nextToken()));
            }

            while (queue.size() > 1) {
                for (int i : queue) {
                    if (queue.peek() < i) { // Queue의 가장 뒤에 재배치
                        queue.offer(queue.poll());
                        break;
                    }
                }

            }

            queue.poll();

        }


    }

}
