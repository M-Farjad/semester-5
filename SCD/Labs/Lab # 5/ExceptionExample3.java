import java.util.InputMismatchException;
import java.util.Scanner;

public class ExceptionExample3 {
    static Scanner console = new Scanner(System.in);

    public static void main(String[] args) {
        int dividend, divisor, quotient;
        try {
            System.out.print("Line 4: Enter the " + "dividend: ");
            dividend = console.nextInt();
            System.out.println();
            System.out.print("Line 7: Enter the " + "divisor: ");
            divisor = console.nextInt();
            System.out.println();
            quotient = dividend / divisor;
            System.out.println("Line 11: Quotient = " + quotient);
        } catch (ArithmeticException aeRef) {
            System.out.println("Line 13: Exception " + "caught: " + aeRef.toString());
            System.out.println("Line 14: Cannot divide by 0.");
        } catch (InputMismatchException imeRef) {
            System.out.println("Line 15: Exception " + "caught: " + imeRef.toString());
        }

    }
}
