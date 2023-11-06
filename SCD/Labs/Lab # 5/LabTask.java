import java.util.*;

public class LabTask {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            try {
                System.out.print("Enter the length in feet: ");
                double feet = getValidInput(scanner);

                System.out.print("Enter the length in inches: ");
                double inches = getValidInput(scanner);

                double totalInches = feet * 12 + inches;
                double centimeters = totalInches * 2.54;

                System.out.println("Equivalent length in inches: " + totalInches + " inches");
                System.out.println("Equivalent length in centimeters: " + centimeters + " cm");

                break; // Successfully calculated and displayed the result, so exit the loop.
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a valid number.");
            } catch (IllegalArgumentException e) {
                System.out.println(e.getMessage());
            }
        }
    }

    private static double getValidInput(Scanner scanner) {
        String input = scanner.next();

        // Check for non-digit inputs and negative numbers
        if (!input.matches("-?\\d+(\\.\\d+)?")) {
            throw new IllegalArgumentException("Invalid input. Please enter a positive number.");
        }

        double value = Double.parseDouble(input);
        if (value < 0) {
            throw new IllegalArgumentException("Negative values are not allowed. Please enter a positive number.");
        }

        return value;
    }
}
