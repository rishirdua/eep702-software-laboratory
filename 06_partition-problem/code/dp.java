import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class dp {
	public static void main (String args[]) throws NumberFormatException, IOException {
		BufferedReader brin = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Dynamic Programmingr");
		
		//Part A
		
		//Take inputs
		System.out.println("Enter N");
		int N = Integer.parseInt(brin.readLine());
		System.out.println("Enter K");
		int K = Integer.parseInt(brin.readLine());
		
		if (N<=0 || K<=0) {
			System.out.println("Error in inputs");
		}
		
		int[] x = new int [N];
		for (int i=0; i<N; i++) {
			System.out.println("Enter x" + i);
			x[i] = Integer.parseInt(brin.readLine());
		}
		int odd=0;
		int even=0;
		for (int i=0; i<N; i++) {
			if ((x[i] % 2) == 0) {
				even++;
			}
			else {
				odd++;
			}
		}
		int numoftriplets = 0;
		//Case 1: x1, x2, x3 are even
		if (even>=2) {
			numoftriplets = numoftriplets + even*(even-1)*(even-2)/6;
		}
		//Case 2: x1, x2 are odd, x3 is even
		if (even>=1) { 
			numoftriplets = numoftriplets + odd*(odd-1)*even/2;
		}
		
		//Show results to user
		System.out.println("The total number of possible triplets such that the sum is even is " + numoftriplets);
		
		
		//Part B
		Arrays.sort(x);
		int minindex=0;
		int umin=0;
		int increment;
		int[] u = new int[K+1];
		u[0] = 0;
		int S  = 0;
		for (int j=1; j<K; j++) {
			S = S + x[j];
		}
		for (int i=1; i<K; i++) {
			increment = (K-1)*(x[K+i-1] + x[i-1]) - 2*S;
			u[i] = u[i-1] + increment;
			S = S -x[i] + x[K+i-1];
			if (u[i]<umin) {
				umin=u[i];
				minindex = i;
			}
		}
		System.out.println("The students get packets containing the following number of candies:");
		for (int j=minindex; j<minindex+K; j++) {
			System.out.print(x[j] + "\t");
			
		}
		
		//Part C
		System.out.println("\nPartition problem");
        GetAllSubsetByStack get = new GetAllSubsetByStack(5);
        get.populateSubset(x, 0, x.length);
        System.out.println(GetAllSubsetByStack.getFound());
        System.out.println(GetAllSubsetByStack.toret);
	}
}
