package baekjoon.baekjoon_2108;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_2108 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int[] arr = new int[8001]; // index가 값이고 value가 빈도, 0의 index = 4000
        int N = Integer.parseInt(br.readLine());
        double sum = 0; // 총합

        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            sum += num;
            arr[num + 4000]++;
        }

        // 산술 평균
        double avrg = 9999;
        if (sum < 0) {
            sum *= -1;
            avrg = Math.round(sum / N);
            avrg *= -1;
        }else {
            avrg = Math.round(sum / N);
        }

        // 중앙값, 최빈값, 최대 - 최소
        int cnt = 0; // 전체 빈도
        int mid = 9999; //
        int mode = 9999; // 최빈값
        int howMany = -1; // 각 빈도수
        boolean mode_prev = false; // 최빈값이 최초로 중복될 경우 true
        int min = 9999; // 최솟값
        int max = 9999; // 최댓값
        boolean first = true;

        for(int i = 0; i < 8001; i++) {
            if (arr[i] == 0) { // 빈도가 0이므로 continue
                continue;
            }

            // 최솟값 구하기
           if (first) { // 처음 들어온 0이 아닌 수가 최솟값
               min = i - 4000;
               first = false;
           }

           // 최빈값 구하기
           if (arr[i] > howMany) { // 최빈값 update
               howMany = arr[i];
                mode = i - 4000;
                mode_prev = false;
           }else if (arr[i] == howMany) {
               if (!mode_prev) { // 중복 최빈값이 없는 경우
                   mode = i - 4000;
                   mode_prev = true;
               }
           }

           // 중앙값 구하기
           while (arr[i]-- > 0) {
               cnt += 1;
               if (cnt == N / 2 + 1) {
                    mid = i - 4000;
               }
           }

           // 최댓값 구하기
            if (cnt == N) {
                max = i - 4000;
            }

        }
        sb.append((int)avrg).append('\n');
        sb.append(mid).append('\n');
        sb.append(mode).append('\n');
        sb.append(max - min).append('\n');

        System.out.println(sb);
    }
}
