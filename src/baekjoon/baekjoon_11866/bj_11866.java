package baekjoon.baekjoon_11866;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class bj_11866 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        Queue<Integer> circle = new LinkedList<>();
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        for (int i = 1; i <= N; i++) {
            circle.offer(i);
        }

        sb.append('<');

        while (circle.size() != 1) {

            for (int j = 1; j < K; j++) { // K - 1 명 뒤로 보내기
                circle.offer(circle.poll());
            }
            sb.append(circle.poll()).append(", ");
        }
        sb.append(circle.poll()).append('>');

        System.out.println(sb);
    }

}
