import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long[] distances = Arrays.stream(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();
        long[] prices = Arrays.stream(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray();

        long cost = 0; // 총 비용
        long minPrice = prices[0]; // 현재까지 가장 저렴한 주유 가격

        // 첫 번째 도시에서 두 번째 도시로 이동하는 비용
        cost += distances[0] * prices[0];

        for (int i = 1; i < n-1; i++) {
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            }
            cost += distances[i] * minPrice;
        }

        System.out.println(cost);
    }
}
