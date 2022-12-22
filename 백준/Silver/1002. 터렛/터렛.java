import java.util.Scanner;

public class Main {
	public static void main(String [] args) {
		Scanner scanner = new Scanner(System.in);

		int T = 0;
		T = scanner.nextInt();

		for(int j=0; j<T; j++) {
			int x1 = scanner.nextInt();
			int y1 = scanner.nextInt();
			int r1 = scanner.nextInt();
			int x2 = scanner.nextInt();
			int y2 = scanner.nextInt();
			int r2 = scanner.nextInt();

			int x = 0;

			double rr = Math.sqrt((x1-x2)*(x1-x2) + (y1- y2)*(y1- y2));
			double rr2 = Math.sqrt((r1-r2)*(r1-r2));
			
			if(x1==x2 && y1 == y2 && r1 == r2)
				x = -1;
			else if(r1+r2<rr)
				x = 0;
			else if(rr2>rr)
				x = 0;
			else if(rr == rr2)
				x = 1;
			else if(r1 + r2 == rr)
				x = 1;
			else
				x = 2;
			
			System.out.println(x);
			}
		scanner.close();
	}
}