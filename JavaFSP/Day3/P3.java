// WAP in java to display the use of interface
package CS393.JavaFSP.Day3;

interface i1 {
    void disp1();
}
interface i2 {
    void disp2();
}
class Inner implements i1, i2 {
    public void disp1() {
        System.out.println("Display for interface1");
    }
    public void disp2() {
        System.out.println("Display for interface2");
    }
}
public class P3 {
    public static void main(String[] args) {
        Inner ob1 = new Inner();
        ob1.disp1();
        Inner ob2 = new Inner();
        ob2.disp2();
    }
}
