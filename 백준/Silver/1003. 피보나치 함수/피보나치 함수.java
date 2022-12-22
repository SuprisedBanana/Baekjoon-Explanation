import java.util.Scanner;

public class Main{
	public static void main(String [] args) {
		Scanner scanner = new Scanner(System.in);

		int T = scanner.nextInt();
		
		int fibo [][] = new int[41][2];
		fibo[0][0] = 1;
		fibo[0][1] = 0;
		fibo[1][0] = 0;
		fibo[1][1] = 1;
		
		
		for(int i=2; i<=40; i++) {
			fibo[i][0] = fibo[i-1][0]+fibo[i-2][0];
			fibo[i][1] = fibo[i-1][1]+fibo[i-2][1];
		}
		
		for(int j=0; j<T; j++) {
			int N = scanner.nextInt();

			System.out.println(fibo[N][0]+" "+fibo[N][1]);
		}
			

		
		scanner.close();
	}
}
