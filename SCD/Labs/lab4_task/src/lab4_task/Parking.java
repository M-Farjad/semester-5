package lab4_task;

public class Parking {
  private String SlotId;
  private String VehicleNumber;
  private String VehicleOwnerName;
  
  public Parking() {}
  
  public void setSlotId(String SlotId) {
	  this.SlotId = SlotId;
  }
  public void setVehicleNumber(String VehicleNumber) {
	  this.VehicleNumber = VehicleNumber;
  }
  public void setVehicleOwnerName(String VehicleOwnerName) {
	  this.VehicleOwnerName = VehicleOwnerName;
  }
  public String getSlotId() {
	  return SlotId;
  }
  public String getVehicleNumber() {
	  return VehicleNumber;
  }
  public String setVehicleOwnerName() {
	  return VehicleOwnerName;
  }
  
  public void ParkVehicle() {}
}
