package baekjoon.baekjoon_10773;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_10773 {

    public static int[] stack;
    public static int size = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        stack = new int[N];
        int sum = 0;

        while (N-- > 0) {
            int num = Integer.parseInt(br.readLine());

            if (num == 0) { // 0이 들어오면 가장 최근에 쓴 수를 지운다.
                pop();
            }
            else {
                push(num);
            }
        }

        for (int val : stack) {
            sum += val;
        }

        sb.append(sum);
        System.out.println(sb);
    }

    public static void push(int item) {
        stack[size] = item;
        size++;
    }

    public static void pop() {
        stack[size - 1] = 0;
        size--;
    }
}
