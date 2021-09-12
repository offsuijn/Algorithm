package baekjoon.baekjoon_11729;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_11729 {
    public static StringBuilder sb = new StringBuilder();
    static int count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        hanoi(N, 1, 2, 3);
        System.out.println(count);
        System.out.println(sb);
    }

    // 원반 옮겨드립니다.
    private static void hanoi(int n, int start, int bridge, int end) {
        // n이 1인 경우
        if (n == 1) {
            sb.append(start + " " + end).append('\n');
            count++;
            return;
        }

        // 마지막 원반만 남기고 나머지를 bridge로 이동
        hanoi(n - 1, start, end, bridge);

        // 마지막 원반 이동
        sb.append(start + " " + end).append('\n');
        count++;

        // bridge에 있는 나머지 원반을 end로 이동
        hanoi(n - 1, bridge, start, end);
    }
}
