// WAP to display use of multiple catch against single try block.
package CS393.JavaFSP.Day3;

public class P8 {
    public static void main(String[] args) {
        int x = 12;
        int y = 0;
        int p[] = { 10, 4, 6, 2 };
        try {
            int z = x / y;
            System.out.println("The result is " + z);
            p[17]=10;
        } catch (ArithmeticException e) {
            System.out.println("This results to infinity");
        }
        catch (Exception e) {
            System.out.println(e);
        }
    }
}
