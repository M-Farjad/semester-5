package lab4_task;

public class Hostel {
   private String StudentId;
   private String BlockNumber;
   private String RoomNumber;
   
   public Hostel() {}
   
   public void setStudentId(String StudentId) {
	   this.StudentId = StudentId;
   }
   public void setBlockNumber(String BlockNumber) {
	   this.BlockNumber = BlockNumber;
   }
   public void setRoomNumber(String RoomNumber) {
	   this.RoomNumber = RoomNumber;
   }
   public String getStudentId() {
	   return StudentId;
   }
   public String getBlockNumber() {
	   return BlockNumber;
   }
   public String getRoomNumber() {
	   return RoomNumber;
   }

   public void HostelDetails() {}
   public void CheckIn() {}
   public void CheckOut() {}
}

class BoysHostel extends Hostel{
   	
}
class GirlsHostel extends Hostel{
   	
}