package baekjoon.baekjoon_14888;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_14888 {

    public static int N;
    public static int Max = Integer.MIN_VALUE;
    public static int Min = Integer.MAX_VALUE;
    public static int[] number;
    public static int[] operator = new int[4];


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        number = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; i++) {
            number[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < 4; i++) {
            operator[i] = Integer.parseInt(st.nextToken());
        }

        dfs(number[0], 1);

        sb.append(Max).append('\n');
        sb.append(Min);
        System.out.println(sb);
    }

    public static void dfs(int num, int depth) {
        if (depth == N) { // 모든 계산을 마친 경우 최댓값과 최솟값 업데이트하기
            Max = Math.max(num, Max);
            Min = Math.min(num, Min);
            return;
        }

        for (int i = 0; i < 4; i++) {
            if (operator[i] > 0) { // 해당 연산자가 1개 이상인 경우
                operator[i]--; // 하나 감소시킨다.

                switch (i) {
                    case 0 : dfs(num + number[depth], depth + 1); break;
                    case 1 : dfs(num - number[depth], depth + 1); break;
                    case 2 : dfs(num * number[depth], depth + 1); break;
                    case 3 : dfs(num / number[depth], depth + 1); break;
                }
                operator[i]++; // 재귀호출이 끝나면 원상복구한다.
            }
        }
    }

}
