import java.util.Scanner;

public class LabTask2 {

    public static void main(String[] args) {
        int lowerlimit;
        int divisor;
        int result;
        Scanner scanner = new Scanner(System.in);

        try {
            lowerlimit = scanner.nextInt();
            divisor = scanner.nextInt();
            System.out.println("Enter the try block");
            result = lowerlimit / divisor;

            if (lowerlimit < 100)
                throw new Exception("Lower Limit Exception.");
            System.out.println("Existing the try block.");

        } catch (ArithmeticException e) {
            System.out.println("Exception: " + e.getMessage());
            result = 110;
        } catch (Exception e) {
            System.out.println("Exception: " + e.getMessage());
        }
        System.out.println("After the catch block.");
    }
}
