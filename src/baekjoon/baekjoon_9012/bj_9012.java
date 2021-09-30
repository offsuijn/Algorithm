package baekjoon.baekjoon_9012;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_9012 {

    public static int size;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        while(N-- > 0) {
            size = 0;
            boolean flag = true; // 짝이 맞으면 true
            String[] arr = br.readLine().split("");

            for(String s : arr) {
                // "("가 들어올 경우
                if (s.equals("(")) {
                    push();
                    continue;
                }
                else { // ")"가 들어올 경우
                    if (size == 0) { // ")"은 있는데 "("가 없는 경우 -> 짝이 맞지 않음
                        flag = false;
                        break;
                    }
                    pop();
                }
            }

            if (flag) {
                if (size != 0) { // "("이 남아있는 경우 -> 짝이 맞지 않음
                    flag  = false;
                }
            }

            if (flag) {
                sb.append("YES").append('\n');
            }
            else {
                sb.append("NO").append('\n');
            }
        }

        System.out.println(sb);

    }

    public static void push() {
        size++;
    }

    public static void pop() {
        size--;
    }
}
