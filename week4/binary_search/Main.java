import java.util.*;
import java.io.*;
     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        int x = 0;
        int n = in.nextInt();
        int[] arr = new int[n];

        for(int i=0;i<n;i++) {
            arr[i] = in.nextInt();
        }

        int m = in.nextInt();

        for(int i=0; i<m; i++) {
            int temp = in.nextInt();
            int result = binarySearch(arr, temp); 
            out.print(result + " ");
        }
        out.close();
    }
     

    public static int binarySearch(int[] a, int target) {
        int L = 0, R = a.length-1;

        while (L <= R) {
            int mid = L + (R-L) / 2;
            if(a[mid] == target) {
                return mid;
            } else if(a[mid] < target) {
                L = ++mid;
            } else {
                R = --mid;
            }
        }

        return -1;
    }


    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;
     
        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }
     
        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }
     
        public int nextInt() {
                return Integer.parseInt(next());
        }
    }
}