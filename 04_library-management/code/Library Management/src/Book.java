
/**
 * @author rishi
 * main class book
 */
public class Book { //book class: stores title, author, publication and edition
 String title;
 String author;
 String publication;
 String edition;
 
 /**
 * @param parts
 */
public Book(String[] parts) {
	 this.title=parts[0];
	 this.author=parts[1];
	 this.publication=parts[2];
	 this.edition=parts[3];
}
public String gettitle() {
		return this.title;
	}
 public String getauthor() {
		return this.author;
	}
 public String getpuiblication() {
		return this.publication;
	}
 public String getedition() {
		return this.edition;
	}

	
}
