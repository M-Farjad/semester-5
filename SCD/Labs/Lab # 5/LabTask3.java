import java.io.*;
import java.util.*;

public class LabTask3 {
    public static void main(String[] args) {
        double test1, test2, test3, test4;
        double average;

        try {
            Scanner inFile = new Scanner(new FileReader("test.txt"));
            PrintWriter outFile = new PrintWriter("testAvg.out");

            test1 = inFile.nextDouble();
            test2 = inFile.nextDouble();
            test3 = inFile.nextDouble();
            test4 = inFile.nextDouble();

            outFile.printf("test Scores: %.2f %.2f %.2f %.2f %n", test1, test2, test3, test4);

            average = (test1 + test2 + test3 + test4) / 4.0;

            outFile.printf("Average test Scores: %.2f", average);
            outFile.close();
        } catch (FileNotFoundException e) {
            System.err.println(e.toString());
        } catch (Exception e) {
            System.err.println(e.toString());
        }
    }
}
