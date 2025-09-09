package CS393.JavaFSP.Day3;
// WAP in java to display the use of functional interface

interface A1 { // This is functional interface as it has only one abstract class
    void disp();
}
public class P4 {
    public static void main(String[] args) {
        A1 ob = new A1() { // Anonymous inner class as it doesnot have any name
            public void disp() {
                System.out.println("This is implementation using anonymous inner class");
            }
        };
        ob.disp();
    }
}
