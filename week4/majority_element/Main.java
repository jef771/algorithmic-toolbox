import java.util.*;
import java.io.*;
     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);

        HashMap<Integer, Integer> map = new HashMap<>();

        int n = in.nextInt();
        int[] a = new int[n];

        for(int i=0;i<n;i++) {
            int temp = in.nextInt();
            if(map.get(temp)!=null) {
                map.replace(temp, map.get(temp)+1);
            } else {
                map.put(temp, 1);
            }
        }
        
        map.forEach((k, v) -> {if(v > n/2){ System.out.println(1); System.exit(0);}});

        System.out.println(0);
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