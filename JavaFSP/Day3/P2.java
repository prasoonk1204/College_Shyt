// WAP in java to display the use of abstract class

package CS393.JavaFSP.Day3;

abstract class Parent{
    abstract void disp1(); // abstract method
    void disp() { // normal method
        System.out.println("Testing for abstract class");
    }
}

class Child extends Parent{
    void disp1() {
        System.out.println("The body is provided by child class");
    }
    void disp3() {
        System.out.println("Child");
    }
}

public class P2 {
    public static void main(String[] args) {
        Child ob = new Child();
        ob.disp();
        ob.disp1();
        ob.disp3();
    }
}
