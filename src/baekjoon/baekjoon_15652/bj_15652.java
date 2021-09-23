package baekjoon.baekjoon_15652;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_15652 {

    public static int N, M;
    public static int[] arr;
    public static StringBuilder sb;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[M];

        dfs(0, 0);
        System.out.println(sb);
    }

    private static void dfs(int start, int depth) {
        if (depth == M) {
            for (int val : arr) {
                sb.append(val + " ");
            }
            sb.append('\n');
            return;
        }

        for(int i = start; i < N; i++) {
            arr[depth] = i + 1;
            dfs(i, depth + 1);
        }
    }
}
