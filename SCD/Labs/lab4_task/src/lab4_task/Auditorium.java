package lab4_task;

public class Auditorium {
   private String auditorium_name;
   private String events_list;
   private String date;
   private String time;
   private String total_seats;
   private String department_Id;
   
   public Auditorium() {}
   
   public void setauditorium_name(String auditorium_name) {
	   this.auditorium_name = auditorium_name;
   }
   public void setevents_list(String events_list) {
	   this.events_list = events_list;
   }
   public void setdate(String date) {
	   this.date = date;
   }
   public void settime(String time) {
	   this.time = time;
   }
   public void settotal_seats(String total_seats) {
	   this.total_seats = total_seats;
   }
   public void setdepartment_Id(String department_Id) {
	   this.department_Id = department_Id;
   }
   
   public String getauditorium_name() {
	   return auditorium_name;
   }
   public String getevents_list() {
	   return events_list;
   }
   public String getdate() {
	   return date;
   }
   public String gettime() {
	   return time;
   }
   public String gettotal_seats() {
	   return total_seats;
   }
   public String getdepartment_Id() {
	   return department_Id;
   }
   
   public void BookEvents() {}
}
