import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ReverseSpiral {
	static int n, x, y;
	static String[][] mat;

	public static void main(String[] args) {
		takeinput();
		x = (n - 1) / 2;
		y = x;
		
		int counter = 0;
		System.out.println(mat[x][y]);
		while (counter < n) {
			counter++;
			iter(counter, false, -1); // go left
			iter(counter, true, 1); //
			counter++;
			iter(counter, false, 1);
			iter(counter, true, -1);
		}
	}

	private static void iter(int counter, boolean isx, int increment) {
		for (int j = 0; j < counter; j++) {
			if (isx == true)
				x = x + increment;
			else
				y = y + increment;
			System.out.println(mat[x][y]);
			if ((x == 0) && (y == 0))
				System.exit(0);;
		}
	}

	public static void takeinput() {
		System.out.println("Enter value for n:\n");
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String inp;
		try {
			n = Integer.parseInt(inp = br.readLine());
		}
		catch (Exception e) {
			System.out.println("Error in taking input");
		}
		if ((n % 2) == 0) {
			System.out.println("n is odd. Exiting now");
			System.exit(1);
		}
		mat = new String[n][n];
		
		System.out.println(n + " by " + n + " matrix\n");
		System.out.println("Enter values for following:\n");
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				System.out.println("(" + i + "," + j + ")");
				try {
					inp = br.readLine();
					mat[i][j] = inp;
				} catch (IOException ioe) {
					System.out.println("IO error trying to read matrix");
					System.exit(1);
				}
			}
		}
	}

	

}
