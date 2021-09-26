package baekjoon.baekjoon_2580;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_2580 {

    public static int[][] arr = new int[9][9];

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i  = 0; i < 9; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < 9; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        sudoku(0, 0);
    }

    public static void sudoku(int row, int col) {
        if (col == 9) { // 행을 다 채운 경우 다음 열 시작
            sudoku(row + 1, 0);
            return;
        }

        if (row == 9) { // 행과 열을 모두 채운 경우 출력
            StringBuilder sb = new StringBuilder();
            for (int i  = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    sb.append(arr[i][j]).append(' ');
                }
                sb.append('\n');
            }
            System.out.println(sb);
            System.exit(0); // 시스템 종료
        }

        if (arr[row][col] == 0) { // 해당 값이 0인 경우 가능한 수 넣기
            for (int i = 1; i <= 9; i++) {
                if(findAnswer(row, col, i)) {
                    arr[row][col] = i;
                    sudoku(row, col + 1);
                }
            }
            arr[row][col] = 0;
            return;
        }
        sudoku(row, col + 1);
    }

    public static boolean findAnswer(int row, int col, int value) {
        for (int i = 0; i < 9; i++) { // 같은 행에 숫자가 중복되는지 검사
            if (arr[row][i] == value) {
                return false;
            }
        }

        for (int i = 0; i < 9; i++) { // 같은 열에 숫자가 중복되는지 검사
            if (arr[i][col] == value) {
                return false;
            }
        }

        for (int i = (row / 3) * 3; i < (row / 3) * 3 + 3; i++) { // 같은 박스 안에 숫자가 중복되는지 검사
            for (int j = (col / 3) * 3; j < (col / 3) * 3 + 3; j++) {
                if (arr[i][j] == value) {
                    return false;
                }
            }
        }

        return true;
    }

}
