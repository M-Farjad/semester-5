package lab4_task;
import java.util.Scanner;

public class main_class {
	static Scanner userInput = new Scanner(System.in);
	public static void main(String[] args) {
		College_Management college_manage = new College_Management();
		boolean open = college_manage.Open(true);
		if(open)
        System.out.println("Currently college is open.     Days(Monday to Friday)     Timing(8:00AM to 2:00PM)\n");
		else
		System.out.println("Currently college is close.     Days(Monday to Friday)     Timing(8:00AM to 2:00PM)\n");


        System.out.println("Admn kindly enter college, departments, classes info: \n");

		System.out.println("Enter College Name: ");
		college_manage.setcollege_name(userInput.nextLine());

		System.out.println("Enter College Location: ");
		college_manage.setcity(userInput.nextLine());

		System.out.println("Enter College Contact number: ");
		college_manage.setcontact_number(userInput.nextLine());

		college_manage.addDepartment();

		college_manage.CollegeDetails();


		Classroom newclass1 = new Classroom();
		newclass1.setClassId("C1");
		System.out.println(newclass1.getClassId());
		newclass1.setDepartmentId("CS");
		newclass1.getDepartmentId();
		newclass1.setSection("A");
		System.out.println(newclass1.getSection());
		college_manage.classAddition(newclass1, "CS");
        
		Classroom newclass2 = new Classroom();
		newclass2.setClassId("E1");
		newclass2.setDepartmentId("ENG");
		newclass2.setSection("B");
		college_manage.classAddition(newclass2, "Engineering");

		college_manage.SearchDepartment("Computer Science");
	}
}
