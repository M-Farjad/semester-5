import java.util.*;

public class ExceptionExample1 {

    static Scanner console = new Scanner(System.in);

    public static void main(String[] args) {
        int dividend, divisor, quotient;

        System.out.print("Line 2: Enter the " + "dividend: ");
        dividend = console.nextInt();
        System.out.println();

        System.out.print("Line 5: Enter the " + "divisor: ");
        divisor = console.nextInt();
        System.out.println();

        quotient = dividend / divisor;
        System.out.println("Line 9: Quotient = " + quotient);
    }
}