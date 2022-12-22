import java.util.Scanner;

public class Main {
	public static void main(String [] args) {
		Scanner scanner = new Scanner(System.in);
		
		int T=scanner.nextInt();

		
		for(int i=0; i<T; i++) {
			int x1=scanner.nextInt();
			int y1=scanner.nextInt();
			int x2=scanner.nextInt();
			int y2=scanner.nextInt();
			int n=scanner.nextInt();

			int inout=0;
			
			for(int j=0; j<n; j++) {
				int cx=scanner.nextInt();
				int cy=scanner.nextInt();
				int r=scanner.nextInt();
				
				int Line1=(cx-x1)*(cx-x1)+(cy-y1)*(cy-y1);
				int Line2=(cx-x2)*(cx-x2)+(cy-y2)*(cy-y2);

				if(Line1<r*r && Line2>r*r)
					inout++;
				else if(Line1>r*r && Line2<r*r)
					inout++;
			}
			
			System.out.println(inout);
			
		}
		scanner.close();
	}
}