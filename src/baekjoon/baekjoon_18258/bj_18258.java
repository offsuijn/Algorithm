package baekjoon.baekjoon_18258;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class bj_18258 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        Deque<Integer> q = new LinkedList<>();

        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());

        while (N-- > 0) {
            st = new StringTokenizer(br.readLine(), " ");

            switch (st.nextToken()) {

                case "push" :
                    q.offer(Integer.parseInt(st.nextToken()));
                    break;

                case "pop" :
                    Integer item = q.poll();
                    if (item == null) {
                        sb.append(-1).append('\n');
                    }
                    else {
                        sb.append(item).append('\n');
                    }
                    break;

                case "size" :
                    sb.append(q.size()).append('\n');
                    break;

                case "empty" :
                    if (q.isEmpty()) {
                        sb.append(1).append('\n');
                    }
                    else {
                        sb.append(0).append('\n');
                    }
                    break;

                case "front" :
                    Integer item1 = q.peekFirst();
                    if (item1 == null) {
                        sb.append(-1).append('\n');
                    }
                    else {
                        sb.append(item1).append('\n');
                    }
                    break;

                case "back" :
                    Integer item2 = q.peekLast();
                    if (item2 == null) {
                        sb.append(-1).append('\n');
                    }
                    else {
                        sb.append(item2).append('\n');
                    }
                    break;
            }
        }

        System.out.println(sb);
    }
}
