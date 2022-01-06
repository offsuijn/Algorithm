package book_coding_test.greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class card_game {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int row = Integer.parseInt(st.nextToken());
        int col = Integer.parseInt(st.nextToken());

        int result = 0;
        while(row-- > 0) {
            st = new StringTokenizer(br.readLine());
            int min = 10000;
            while(st.hasMoreTokens()) {
                min = Math.min(min, Integer.parseInt(st.nextToken()));
            }
            result = Math.max(result, min);
        }

        System.out.println(result);
    }
}
