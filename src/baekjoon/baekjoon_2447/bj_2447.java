package baekjoon.baekjoon_2447;

import java.io.*;

public class bj_2447 {
    static char[][] arr;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        arr = new char[N][N];

        print_star(0, 0, N, false);

        for(int i = 0; i < N; i++) {
            bw.write(arr[i]);
            bw.write('\n');
        }
        bw.flush();
        bw.close();
    }

    // 별을 찍는 함수
    private static void print_star(int x, int y, int N, boolean blank) {

        // 공백인 경우 : blank가 true면 공백
        if (blank) {
            for (int i = x; i < x + N; i++) {
                for (int j = y; j < y + N; j++) {
                    arr[i][j] = ' ';
                }
            }
            return;
        }

        // size가 1이고, 공백이 아닐 경우
        if (N == 1) {
            arr[x][y] = '*';
            return;
        }

        // 각 단계에서 9칸의 블럭으로 구분하고, 그 중 가운데인 5번째 칸을 공백으로 만들거나 재귀 호출을 반복한다.
        int size = N / 3; // 블럭의 사이즈
        int cnt = 0; // 별이 출력된 누적수
        for (int i = x; i < x + N; i += size) {
            for (int j = y; j < y + N; j += size) {
                cnt++;
                if (cnt == 5) { // 공백인 경우 : 9칸 중 5번째 칸이 가운데이므로 공백칸이다.
                    print_star(i, j, size, true);
                }
                else {
                    print_star(i, j, size, false);
                }
            }
        }
    }
}
