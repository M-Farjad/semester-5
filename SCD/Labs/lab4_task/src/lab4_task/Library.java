package lab4_task;

public class Library {
   private String LibraryId;
   private String LibrarianName;
   private String BookSection;
   private String TotalBooks;
   
   public Library() {}
   
   public void setLibraryId(String LibraryId) {
	   this.LibraryId = LibraryId;
   }
   public void setLibrarianName(String LibrarianName) {
	   this.LibrarianName = LibrarianName;
   }
   public void setBookSection(String BookSection) {
	   this.BookSection = BookSection;
   }
   public void setTotalBooks(String TotalBooks) {
	   this.TotalBooks = TotalBooks;
   }
   public String getLibraryId() {
	   return LibraryId;
   }
   public String getLibrarianName() {
	   return LibrarianName;
   }
   public String getBookSection() {
	   return BookSection;
   }
   public String getTotalBooks() {
	   return TotalBooks;
   }
   
   public void LibraryDetails() {}
   public void SearchBooks() {}
   public void LendBooks() {}
   public void ReturnBooks() {}
   public void PayFine() {}
}
