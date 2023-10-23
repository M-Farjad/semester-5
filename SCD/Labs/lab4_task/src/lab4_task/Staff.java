package lab4_task;

public class Staff {
   private String StaffId;
   private String StaffName;
   private String DepartmentId;
   private String Salary;
   
   public Staff() {}
   
   public void setStaffId(String StaffId) {
	   this.StaffId = StaffId;
   }
   public void setStaffName(String StaffName) {
	   this.StaffName = StaffName;
   }
   public void setDepartmentId(String DepartmentId) {
	   this.DepartmentId = DepartmentId;
   }
   public void setSalary(String Salary) {
	   this.Salary = Salary;
   }
   
   public String getStaffId() {
	   return StaffId;
   }
   public String getStaffName() {
	   return StaffName;
   }
   public String getDepartmentId() {
	   return DepartmentId;
   }
   public String getSalary() {
	   return Salary;
   }
   
   public void StaffDetails() {}
}

class Teaching_Staff extends Staff{
   	
}
class Non_Teaching_Staff extends Staff{
   	
}
