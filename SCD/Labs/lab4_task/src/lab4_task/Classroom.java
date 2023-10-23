package lab4_task;

public class Classroom {
   private String ClassId;
   private String Section;
   private String DepartmentId;
   
   public Classroom() {}
   
   public void setClassId(String ClassId) {
	   this.ClassId = ClassId;
   }
   public void setSection(String Section) {
	   this.Section = Section;
   }
   public void setDepartmentId(String DepartmentId) {
	   this.DepartmentId = DepartmentId;
   }
   
   public String getClassId() {
	   return ClassId;
   }
   public String getSection() {
	   return Section;
   }
   public String getDepartmentId() {
	   return DepartmentId;
   }
   
   public void ClassroomDetails() {
      System.out.println("ID of Classroom is: "+getDepartmentId()+"\n");
		System.out.println("Section of Classroom is: "+getSection()+"\n");
		System.out.println("Department ID of Classroom is: "+getDepartmentId()+"\n");
   }
   public boolean IsOccupied(boolean check) {
	   if(check) {
		   return true;
	   }else {
		   return false;
	   }
   }
}
