import java.util.*;

class tUf {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n;
        n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        //precompute:
        int[] hash = new int[13];
        for (int i = 0; i < n; i++) {
            hash[arr[i]] += 1;
            // System.out.println(hash[i]);
        }
        for (int i = 0; i < n; i++) {
            // hash[arr[i]] += 1;
            System.out.println(hash[i]+":"+arr[i]);
        }

        // int q;
        // q = sc.nextInt();
        // while (q-- != 0) {
        //     int number;
        //     number = sc.nextInt();
        //     // fetching:
        //     System.out.println(hash[number]);
        // }
    }
}