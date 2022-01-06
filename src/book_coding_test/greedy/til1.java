package book_coding_test.greedy;

import java.io.IOException;
import java.util.Scanner;

public class til1 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();
        int result = 0;

        while (N >= K) {
            int target = (N / K) * K;
            result += (N - target);
            N = target;

            result++;
            N /= K;
        }

        result += N - 1;
        System.out.println(result);

    }
}
