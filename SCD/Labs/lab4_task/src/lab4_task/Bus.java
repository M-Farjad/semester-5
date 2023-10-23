package lab4_task;

public class Bus {
   private String BusId;
   private String BusNumber;
   private String DriverName;
   private String Destination;
   private String TotalSeats;
   
   public void setBusId(String BusId) {
	   this.BusId = BusId;
   }
   
   public void setBusNumber(String BusNumber) {
	   this.BusNumber = BusNumber;
   }
   public void setDriverName(String DriverName) {
	   this.DriverName = DriverName;
   }
   
   public void setDestination(String Destination) {
	   this.Destination = Destination;
   }
   public void setTotalSeats(String TotalSeats) {
	   this.TotalSeats = TotalSeats;
   }
   
   public String getBusId() {
	   return BusId;
   }
   
   public String getBusNumber() {
	   return BusNumber;
   }
   public String getDriverName() {
	   return DriverName;
   }
   
   public String getDestination() {
	   return Destination;
   }
   public String getTotalSeats() {
	   return TotalSeats;
   }
   
   public void BusDetails() {}
   public void SeatsAvailability() {}
}
