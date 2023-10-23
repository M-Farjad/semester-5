package lab4_task;

public class Student {
   private String StudentId;
   private String StudentName;
   private String Gender;
   private String Year;
   private String ClassId;
   
   public Student() {}
   
   public void setStudentId(String StudentId) {
	   this.StudentId = StudentId;
   }
   public void setStudentName(String StudentName) {
	   this.StudentName = StudentName;
   }
   public void setGender(String Gender) {
	   this.Gender = Gender;
   }
   public void setYear(String Year) {
	   this.Year = Year;
   }
   public void setClassId(String ClassId) {
	   this.ClassId = ClassId;
   }
   public String getStudentId() {
	   return StudentId;
   }
   public String getStudentName() {
	   return StudentName;
   }
   public String getGender() {
	   return Gender;
   }
   public String getYear() {
	   return Year;
   }
   public String getClassId() {
	   return ClassId;
   }
}

class UG_Student extends Student{
   	
}
class PG_Student extends Student{
   	
}