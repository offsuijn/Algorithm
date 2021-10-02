package baekjoon.baekjoon_1874;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_1874 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        // 2 -> 1 은 꺼낼 수 있어도, 1 -> 2 로는 꺼낼 수 없다. 왜냐하면 1을 꺼내려면 2를 먼저 버려야하기 때문임
        // arr은 내림차순으로 되어있어야 수열을 만들 수 있음
    }
}
