package lab4_task;

public class Canteen {
   private String InchargeId;
   private String ItemsList;
   private String AvailableList;
   
   public Canteen() {}
   
   public void setInchargeId(String InchargeId) {
	   this.InchargeId = InchargeId;
   }
   public void setItemsList(String ItemsList) {
	   this.ItemsList = ItemsList;
   }
   public void AvailableList(String AvailableList) {
	   this.AvailableList = AvailableList;
   }
   
   public String getInchargeId() {
	   return InchargeId;
   }
   public String getItemsList() {
	   return ItemsList;
   }
   public String getAvailableList() {
	   return AvailableList;
   }
   
   public void ShowItems() {}
   public void Buy() {}
}
