import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class RegexMatcher {
	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter string 1");
		String s1 = "";
		try {
			s1 = br.readLine();
		} catch (IOException e) {
			System.out.println("Error in taking string 1 from user");
			e.printStackTrace();
		}
		System.out.println("Enter string 2");
		String s2 = "";
		try {
			s2 = br.readLine();
		} catch (IOException e) {
			System.out.println("Error in taking string 2 from user");
			e.printStackTrace();
		}
		if (test(s1,s2)) System.out.println("result: the strings match");
		else System.out.println("result: the strings do not match");
	}
	
	public static boolean test(String s1, String s2){
		if ((s1.equals("")) && (s2.equals(""))) {
			return true;
		}
		else if (s1.equals("")) {
			if (nextchar(s2)=='\0') return true;
			else return false;
		} 
		else if (s2.equals("")) {
			if (nextchar(s1)=='\0') return true;
			else return false;
		} //end of trivial cases
		else if (s1.charAt(0) == '?') {
			if (test(s1.substring(1),s2) || test(s1.substring(1),s2.substring(1)) ) return true;
			else return false;
		}
		else if (s2.charAt(0) == '?') {
			if (test(s1,s2.substring(1)) || test(s1.substring(1),s2.substring(1)) ) return true;
			else return false;
		}
		else if (s1.charAt(0) == '*') {
			char guess = nextchar(s1);
			if (guess == '\0') return true;
			for (int i=0; i>=0; i = s2.indexOf(guess, i+1)) {
				if (test(s1.substring(s1.indexOf(guess)),s2.substring(i))) return true;
			}
			return false;
		}
		else if (s2.charAt(0) == '*') {
			char next = nextchar(s2);
			if (next == '\0') return true;
			for (int i=0; i>=0; i = s1.indexOf(next, i+1)) {
				if (test(s1.substring(i),s2.substring(s2.indexOf(next)))) return true;
			}
			return false;
		}
		
		else if (s1.charAt(0)==s2.charAt(0)) {
			return test(s1.substring(1),s2.substring(1));
		}
		else return false;
		
	}
	
	public static char nextchar(String teststring) {
		for (int i=0; i<teststring.length(); i++) {
			if (teststring.charAt(i)!='?' && teststring.charAt(i)!='*') return teststring.charAt(i);
		}
		return '\0';
	}
}