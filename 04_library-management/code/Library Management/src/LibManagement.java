import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Writer;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * 
 */

/**
 * @author rishi
 *
 */

/**
 * @author rishi
 *
 */
public class LibManagement { // main class

	/**
	 * @param args
	 * @throws IOException 
	 */
	static int i;
	static Book[] booklist;
	static Book[] issuelist;
	static int loggedin = 0;
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader brin = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Library Manager");
		int userinput;
		
		// initialize
		i = countbooks();
		booklist = makelist();
		
		while(0==0) {
			//show current user level
			if (loggedin==0) {
				System.out.println("Using as Guest");
			}
			else if (loggedin==1){
				System.out.println("Logged in as admin");
			}
			else if (loggedin == 2) {
				System.out.println("Logged in as student");
			}
				
			System.out.println("Enter choice: 1: login, 2: view all, 3: search 4: add (admin only), 5: remove (admin only), 6: Issue book (student only) 7: View fines, 8: logout, 9:exit");
			userinput = Integer.parseInt(brin.readLine());
			
			if (userinput==1) {//Login
				System.out.println("Enter username");
				String username = brin.readLine();
				System.out.println("Enter password");
				String pass = brin.readLine();
				if (username.equals("admin") && pass.equals("pass")) {
					loggedin=1;
					System.out.println("Hello admin!");
				}
				else if (username.equals("student") && pass.equals("pass")) {
					loggedin=2;
					System.out.println("Hello student!");
				}
				else {
					System.out.println("Incorrect credentials");
				}
			}
			if (userinput==2) {//Search for books
				displaybooks();
			}
			if (userinput==3) { //Search for books
				searchbooks();
			}
			if (userinput==4) { //add books (admin only)
				if (loggedin==1) {
					addbook();
					i++;
					booklist = makelist();
				}
				else {
					System.out.println("You are not allowed\tPlease log in first");
				}
			}
			if (userinput==5) { //remove books (admin only)
				if (loggedin==1) {
					removebook();
					i--;
					booklist = makelist();
				}
				else {
					System.out.println("You are not allowed\tPlease log in first");
				}
			}	
			if (userinput==6) {// issue book
				if (loggedin==2) {
					System.out.println("Issue book");
					issuebooks();
					
				}
				else {
					System.out.println("You are not allowed\tPlease log in first");
				}
			}
			
			if (userinput==7) { //fine
				calculatefine();
			}
			
			if (userinput==8) { //logout
				loggedin=0;
				System.out.println("You are logged out");
			}
			
			if (userinput==9) {
				System.exit(0);
			}
		}

	}
	
	/**
	 * counts number of books
	 * @return
	 * @throws IOException
	 */
	private static int countbooks() throws IOException {
		FileInputStream fstream = new FileInputStream("books.txt");
		BufferedReader br = new BufferedReader(new InputStreamReader(fstream));
		int j=0;
		//Read File Line By Line
		try {
			while ((br.readLine()) != null)   {
				j++;
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		br.close();
		return j;
	}
	
	/**
	 * makes array list of books
	 * @return
	 * @throws IOException
	 */
	public static Book[] makelist() throws IOException {
		Book[] booklist = new Book[1024];
		String[] parts = new String[4]; 
		FileInputStream fstream = new FileInputStream("books.txt");
		BufferedReader br = new BufferedReader(new InputStreamReader(fstream));
	
		String strLine;
		int j=0;
		//Read File Line By Line
		try {
			while ((strLine = br.readLine()) != null)   {
				parts = strLine.split("\t");
				booklist[j] = new Book(parts);
				j++;
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		br.close();
		return booklist;
	}
	
	/**
	 * @throws IOException
	 */
	public static void addbook() throws IOException {
		Writer output;
		output = new BufferedWriter(new FileWriter("books.txt", true));
		BufferedReader brin = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter title\n");
		String intitle = brin.readLine();
		System.out.println("Enter author\n");
		String inauthor= brin.readLine();
		System.out.println("Enter publication\n");
		String inpublication = brin.readLine();
		System.out.println("Enter edition\n");
		String inedition = brin.readLine();
		output.append(intitle + "\t" + inauthor + "\t" + inpublication + "\t" +inedition + "\n");
		output.close();	
	}
	
	/**
	 * @throws IOException
	 */
	public static void removebook() throws IOException {
		System.out.println("The list of books is as follows:\n");
		for (int k=0; k<i; k++) {
			System.out.println("ID\t" + k + "\t" + booklist[k].gettitle() + ", ed: " + booklist[k].getedition() + " by " + booklist[k].getauthor() + ". Publication: " + booklist[k].getpuiblication());
		}
		BufferedReader brin = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter ID of book to delete");
		int bookID = -1;
		try {
			bookID = Integer.parseInt(brin.readLine());
		} catch (IOException e) {
			System.out.println("Error in taking string from user");
			e.printStackTrace();
		}
		System.out.println("Are you sure? (y/n)");
		String confirm = brin.readLine();
		if (confirm.equalsIgnoreCase("y")) {
			FileInputStream fstream = new FileInputStream("books.txt");
			BufferedReader br = new BufferedReader(new InputStreamReader(fstream));
			Writer output;
			output = new BufferedWriter(new FileWriter("books.txt.new", false));
			int k=0;
			String strLine;
			try {
				while ((strLine = br.readLine()) != null)   {
					if (k!=bookID)	output.append(strLine + "\n");
					k++;
				}
			} catch (IOException e) {
				e.printStackTrace();
			}
			br.close();
			output.close();
			
			File file = new File("books.txt.new");	    
		    File file2 = new File("books.txt");
		    
		    file.renameTo(file2);
		    System.out.println("Deleted");
		}
		
		
	}
	
	/**
	 * shows list of books
	 */
	public static void displaybooks() {//Display the books
			System.out.println("The list of books is as follows:\n");
			for (int k=0; k<i; k++) {
				System.out.println(booklist[k].gettitle() + "\t" + booklist[k].getedition() + "\t" + booklist[k].getauthor() + "\t" + booklist[k].getpuiblication());
			}
	}
	
	/**
	 * searches for books
	 */
	public static void searchbooks() { 
		BufferedReader brin = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter string to search");
		String searchstring = null;
		try {
			searchstring = brin.readLine();
		} catch (IOException e) {
			System.out.println("Error in taking string from user");
			e.printStackTrace();
		}
		int id = searchid(searchstring);
		if (id>=0) {
			System.out.println("The book is " + booklist[id].gettitle() + ", ed: " + booklist[id].getedition() + " by " + booklist[id].getauthor() + ". Publication: " + booklist[id].getpuiblication());
		}
		else {
			System.out.println("Sorry! Book not found\n");
		}
	}
	
	public static void issuebooks()  throws IOException { 
		displaybooks();
		BufferedReader brin = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter book name to issue");
		String searchstring = null;
		try {
			searchstring = brin.readLine();
		} catch (IOException e) {
			System.out.println("Error in taking string from user");
			e.printStackTrace();
		}
		int id = searchid(searchstring);
		if (id>=0) {
			System.out.println("The book is " + booklist[id].gettitle() + ", ed: " + booklist[id].getedition() + " by " + booklist[id].getauthor() + ". Publication: " + booklist[id].getpuiblication());
			System.out.println("Issued");
		}
		else {
			System.out.println("Book not found");
		}
		Writer output;
		output = new BufferedWriter(new FileWriter("issued.txt", true));
		Date date = new Date();
		SimpleDateFormat sdf = new SimpleDateFormat("MM/dd/yyyy HH:mm:ss");
		String datetoday = sdf.format(date);
		output.append(booklist[id].gettitle() + "\t" + booklist[id].getauthor() + "\t" + booklist[id].getpuiblication() + "\t" +booklist[id].getedition() + "\t" + datetoday + "\n");
		output.close();	
		
	}
	
	public static void calculatefine() throws IOException{
		
		Book[] booklist = new Book[1024];
		String[] parts = new String[4]; 
		FileInputStream fstream = new FileInputStream("issued.txt");
		BufferedReader br = new BufferedReader(new InputStreamReader(fstream));
	
		String strLine;
		int j=0;
		//Read File Line By Line
		long totalfine = 0;
		try {
			System.out.println("Delay\tFine");
			while ((strLine = br.readLine()) != null)   {
				parts = strLine.split("\t");
				String dateStart = parts[4];
				//HH converts hour in 24 hours format (0-23), day calculation
				SimpleDateFormat format = new SimpleDateFormat("MM/dd/yyyy HH:mm:ss");
		 
				Date d1 = null;
				Date d2 = new Date();
		 
				try {
					d1 = format.parse(dateStart);
					
		 
					//in milliseconds
					long diff = d2.getTime() - d1.getTime();
		 
					long diffDays = diff / (24 * 60 * 60 * 1000);
					long fine = diffDays * 10;
					totalfine = totalfine + fine;
					 
					System.out.println(diffDays + " days, Fine:\tINR" + fine);
					
		 
				} catch (Exception e) {
					e.printStackTrace();
				}
				j++;
			}
			System.out.println("________________________");
			System.out.println("Total Fine:\tINR " + totalfine);
		} catch (IOException e) {
			e.printStackTrace();
		}
		br.close();
		
 
		
	}
	
	
	/**
	 * @param searchstring
	 * @return
	 */
	private static int searchid(String searchstring) {
		searchstring = searchstring.toLowerCase();
		for (int k=0; k<i; k++) {
			if ((booklist[k].gettitle().toLowerCase().equals(searchstring)) || (booklist[k].getauthor().toLowerCase().equals(searchstring)) || (booklist[k].getpuiblication().toLowerCase().equals(searchstring)) || (booklist[k].getedition().toLowerCase().equals(searchstring))) {
				return k;
			}
		}
		return -1;
	}
	

}
