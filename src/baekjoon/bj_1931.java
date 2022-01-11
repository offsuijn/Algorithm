package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class bj_1931 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());

        // Greedy : 겹치지 않는 회의 중 가장 빨리 끝나는 것을 선택하자!
        int[][] arr = new int[N][2];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken()); // 시작시간
            arr[i][1] = Integer.parseInt(st.nextToken()); // 종료시간
        }

        Arrays.sort(arr, new Comparator<int[]>() {

            @Override
            public int compare(int[] o1, int[] o2) {

                // 종료시간이 같을 경우, 시작시간이 빠른 순서대로 정렬
                if (o1[1] == o2[1]) {
                    return o1[0] - o2[0];
                }

                return o1[1] - o2[1]; // 종료시간이 빠른 것부터 정렬
            }
        });

        int cnt = 0;
        int prev_end_time = 0;

        for(int i = 0; i < N; i++) {
            if (arr[i][0] >= prev_end_time) {
                prev_end_time = arr[i][1];
                cnt++;
            }
        }

        System.out.println(cnt);
    }
}
