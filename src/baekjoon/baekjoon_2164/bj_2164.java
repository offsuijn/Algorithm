package baekjoon.baekjoon_2164;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class bj_2164 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Queue<Integer> q = new LinkedList<>();

        int N = Integer.parseInt(br.readLine());

        for (int i = 1; i <= N; i++) {
            q.offer(i);
        }

        while (q.size() > 1) { // queue에 하나만 남을 때까지
            q.poll();
            q.offer(q.poll());
        }

        System.out.println(q.poll());
    }

}
