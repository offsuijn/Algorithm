package baekjoon.baekjoon_1874;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class bj_1874 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        Stack<Integer> stack = new Stack<>();
        int N = Integer.parseInt(br.readLine());

        int start = 0; // stack에 가장 마지막으로 push한 값

        while (N-- > 0) {
            int seq = Integer.parseInt(br.readLine());

            // top의 숫자가 수열보다 작으면 -> 수열까지 push한 뒤 pop
            if (seq > start) {
                for (int i = start + 1; i <= seq; i++) {
                    stack.push(i);
                    sb.append('+').append('\n');
                }
                start = seq;
            }
            // top의 숫자가 수열보다 크면 -> 'NO'
            else if (seq < stack.peek()) {
                System.out.println("NO");
                System.exit(0);
            }

            stack.pop();
            sb.append('-').append('\n');
        }

        System.out.println(sb);
    }
}
