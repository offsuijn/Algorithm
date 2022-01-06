package book_coding_test.greedy;

public class exchange {
    /**
     * 거스름돈 문제
     */
    public static void main(String[] args) {

        int n = 1250;
        int cnt = 0;

        int[] coin_types = {500, 100, 50, 10};

        for (int coin : coin_types) {
            cnt += n / coin;
            n %= coin;
        }

        System.out.println(cnt);

    }

}