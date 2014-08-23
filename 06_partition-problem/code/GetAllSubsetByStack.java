import java.util.Stack;

public class GetAllSubsetByStack {

    /** Set a value for target sum */
    public static int TARGET_SUM;
    private static boolean found;

    private Stack<Integer> stack = new Stack<Integer>();

    /** Store the sum of current elements stored in stack */
    private int sumInStack = 0;

    public GetAllSubsetByStack(int i) {
    	TARGET_SUM = i;
	}
    public static String toret = "";
	public void populateSubset(int[] data, int fromIndex, int endIndex) {
			
		 /*
	        * Check if sum of elements stored in Stack is equal to the expected
	        * target sum.
	        * 
	        * If so, call print method to print the candidate satisfied result.
	        */
			
			
			if (sumInStack >= TARGET_SUM) {
			    if (sumInStack == TARGET_SUM) {
			        toret = toret + print(stack);
			        found = true;
			    }
			    // there is no need to continue when we have an answer
			    // because nothing we add from here on in will make it
			    // add to anything less than what we have...
			   return;
			}
	        

	        for (int currentIndex = fromIndex; currentIndex < endIndex; currentIndex++) {

	            if (sumInStack + data[currentIndex] <= TARGET_SUM) {
	                stack.push(data[currentIndex]);
	                sumInStack += data[currentIndex];

	                /*
	                * Make the currentIndex +1, and then use recursion to proceed
	                * further.
	                */
	                populateSubset(data, currentIndex + 1, endIndex);
	                sumInStack -= (Integer) stack.pop();
	            }
	        }
	        
	    }

	    /**
	    * Print satisfied result. i.e. 15 = 4+6+5
	    */

	    private String print(Stack<Integer> stack) {
	        StringBuilder sb = new StringBuilder();
	        sb.append(TARGET_SUM).append(" = ");
	        for (Integer i : stack) {
	            sb.append(i).append("+");
	        }
	        return sb.deleteCharAt(sb.length() - 1).toString();
	    }

		public static boolean getFound() {
			return found;
		}

		public static void setFound(boolean found) {
			GetAllSubsetByStack.found = found;
		}
}