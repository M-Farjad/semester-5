package lab4_task;

import java.util.ArrayList;
import java.util.Scanner;

public class College_Management {
	Scanner userInput = new Scanner(System.in);
	private String college_name;
	private String city;
	private String contact_number;

	public ArrayList<Department> department;
	//public Auditorium auditorium;
	// private ArrayList<Hostel> hostels;
	// private ArrayList<Parking> parkings;
	private Department dep;
	private int size;
	private int total_classrooms;
	public ArrayList<Classroom> classrooms;
	
	public College_Management() {
		//this.hostels = hostels;
		//this.parkings = parkings;
		this.total_classrooms = 0;
		this.department= new ArrayList<Department>();
		//this.auditorium = new Auditorium();
	}
	
	public void setcollege_name(String college_name) {
		this.college_name = college_name;
	}
	
	public void setcity(String city) {
		this.city = city;
	}
	
	public void setcontact_number(String contact_number) {
		this.contact_number = contact_number;
	}
	
	public String getcollege_name() {
		return college_name;
	}
	
	public String getcity() {
		return city;
	}
	
	public String getcontact_number() {
		return contact_number;
	}

	public int gettotal_departments() {
		return department.size();
	}
	
	public Boolean Open(Boolean check) {
		if(check)
		{
			return true;
		}else {
			return false;
		}
	}

	private void departmentsInfoAddition(){
		dep = new Department();
		department.add(dep);
		
		System.out.println("Enter Departemnt name: ");
        dep.setdepartment_name(userInput.nextLine());

		userInput.nextLine();

		System.out.println("Enter Departemnt ID: ");
        dep.setdepartmentId(userInput.nextLine());

		System.out.println("Enter Departemnt HOD name: ");
        dep.setHOD_name(userInput.nextLine());

		System.out.println("Enter Departemnt total staff: ");
        dep.settotal_staff(userInput.nextInt());

		System.out.println("Enter Departemnt total classrooms: ");
        size = userInput.nextInt();
        total_classrooms+=size;

	}

	public void SearchDepartment(String name){
		for(int i = 0;i<department.size();i++){
			if(department.get(i).getdepartment_name() == name){
				department.get(i).DepartmentDetails();
			}
		}
	}

    public void classAddition(Classroom classroom,String departmentName){
        for(int i = 0;i<department.size();i++){
				System.out.println(department.get(i).getdepartment_name());
		}

        for(int i = 0;i<department.size();i++){
			if(department.get(i).getdepartment_name() == departmentName){
				department.get(i).add_class(classroom);
			}
		}
	}

	public void classSearching(String classroom){
        for(int i = 0;i<department.size();i++){
			department.get(i).SearchClass(classroom);
		}
	}

	public void addDepartment(){
    int choice = 1;
        while(choice==1)
		{
			System.out.println("Do you wanna to enter department(1 for yes and 0 for no): ");
		choice = userInput.nextInt();
		if(choice==1)
		{
			departmentsInfoAddition();
		}else {
        break;
		}
		}
	}

	public void CollegeDetails() {
		System.out.println("Name of the college is: "+getcollege_name()+"\n");
		System.out.println("Location of the college is: "+getcity()+"\n");
		System.out.println("Contact Number of the college is: "+getcontact_number()+"\n");

		
        System.out.println("Total Departments in the college are: "+department.size()+"\n");
		System.out.println("Total classrooms in Departments of the college are: "+total_classrooms+"\n");
	}

}
