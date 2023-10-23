package lab4_task;

import java.util.ArrayList;

public class Department {
   private String departmentId;
   private String department_name;
   private String HOD_name;
   private int total_staff;
   //private int total_students;
   public ArrayList<Classroom> classroom;
   
   public Department() {
      
   }

   public void setclassrooms(ArrayList<Classroom> classrooms){
      this.classroom = classrooms;
   }
   
   public void setdepartmentId(String departmentId) {
	   this.departmentId = departmentId;
   }
   
   public void setdepartment_name(String department_name) {
	   this.department_name = department_name;
   }
   
   public void setHOD_name(String HOD_name) {
	   this.HOD_name = HOD_name;
   }
   public void settotal_staff(int total_staff) {
	   this.total_staff = total_staff;
   }
   
   // public void settotal_students(int total_students) {
	//    this.total_students = total_students;
   // }
   
   public String getdepartmentId() {
	   return departmentId;
   }
   
   public String getdepartment_name() {
	   return department_name;
   }
   
   public String getHOD_name() {
	   return HOD_name;
   }
   public int gettotal_staff() {
	   return total_staff;
   }
   
   public int gettotal_classrooms() {
	   return classroom.size();
   }

   public void add_class(Classroom newClass){
      classroom.add(newClass);
   }

   public void SearchClass(String Id){
      for(int i = 0;i<classroom.size();i++){
			if(classroom.get(i).getClassId() == Id){
				classroom.get(i).ClassroomDetails();
			}
		}
   }
   
   public void DepartmentDetails() {
      System.out.println("ID of Department is: "+getdepartmentId()+"\n");
		System.out.println("Name of Department is: "+getdepartment_name()+"\n");
		System.out.println("Name of HOD is: "+getHOD_name()+"\n");
      System.out.println("Total Classrooms in the "+getdepartment_name()+" are: "+classroom.size()+"\n");
   }
   public void ShowEvents() {}

   
}
