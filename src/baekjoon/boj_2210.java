// https://www.acmicpc.net/problem/2210

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Boj_2210 {
    static int[][] board = new int[5][5];
    static int[] dx = {0, 0, -1, +1};
    static int[] dy = {-1, +1, 0, 0};
    static Set<Integer> set = new HashSet<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        for (int i = 0; i < 5; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                dfs(i, j, board[i][j], 0);
            }
        }

        System.out.println(set.size());
    }

    public static void dfs(int x, int y, int sum, int cnt) {
        int nx, ny;

        if (cnt == 5) {
            if (!set.contains(sum)) {
                set.add(sum);
            }
            return ;
        }

        for (int k = 0; k < 4; k++) {
            nx = x + dx[k];
            ny = y + dy[k];

            if (nx >= 0 && nx < 5 && ny >= 0 && ny < 5) {
                dfs(nx, ny, 10*sum + board[nx][ny], cnt+1);
            }
        }
    }
}
