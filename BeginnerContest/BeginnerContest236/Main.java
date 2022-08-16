import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        /*default
        String a = sc.next(); //単語を読む
        int b = sc.nextInt(); //数字を読む
        */

        String s = sc.next(); //単語を読む
        int a = sc.nextInt(); //数字を読む
        int b = sc.nextInt(); //数字を読む
        char char_a = s.charAt(a-1);
        char char_b = s.charAt(b-1);
        String ans = s.substring(0, a-1) + char_b + s.substring(a, b-1) +  char_a + s.substring(b);
        System.out.println(ans);
        /*a
        */
        /* b
        int N = sc.nextInt(); //数字を読む
        int this_a = 0;
        int[] a = new int[N];
        Arrays.fill(a, 0);
        for (int i = 0; i < 4*N-1; i++) {
            this_a = sc.nextInt(); // 数字を読む
            a[this_a-1]++;
        }
        for (int i = 0; i < N; i++) {
            if(a[i] == 3){
                System.out.println(i+1);
                break;
            }
        }
         */
        /*c
        int n = sc.nextInt(); //数字を読む
        int m = sc.nextInt(); //数字を読む
        String[] s = new String[n];
        for (int i = 0; i < n; i++) {
            s[i] = sc.next(); //単語を読む
        }
        int count = 0;
        String t;
        t = sc.next(); //単語を読む
        System.out.println("Yes"); //最初は必ずある
        count++;
        boolean check_next_flag = true; //次のTをチェックするかどうかのフラグ、Yesの後にはTrueになる
        for (int i = 1; i < n-1; i++) {//二つ目からチェックする
            if(count != m-1){
                if(check_next_flag){
                    t = sc.next(); //単語を読む
                }
                if(t.equals(s[i])){
                    System.out.println("Yes");
                    count++;
                    check_next_flag = true;
                }else{
                    System.out.println("No");
                    check_next_flag = false;
                }
            }else{//m-1個見つけたら、m個目は終点以外あり得ない
                System.out.println("No");
            }
        }
        System.out.println("Yes"); //最後は必ずある
        */
        /*d
        */
    }
}