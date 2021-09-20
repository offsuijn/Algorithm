package baekjoon.baekjoon_15650;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_15650 {

    public static int N;
    public static int M;
    public static int[] arr;
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[M];
        dfs( 0, 0);

        System.out.println(sb);
    }

    private static void dfs(int start, int depth) {
        if (depth == M) { // depth와 M이 같을 경우, 출력
            for (int val : arr) {
                sb.append(val).append(' ');
            }
            sb.append('\n');
            return;
        }

        for (int i = start; i < N; i++) {
            arr[depth] = i + 1;

            dfs(i + 1, depth + 1);
        }

    }
}
