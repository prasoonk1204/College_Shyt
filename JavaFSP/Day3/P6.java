// WAP to display the use of dynamic method dispatch
package CS393.JavaFSP.Day3;
class Parent {
    void disp(){
        System.out.println("This is the parent class method");
    }
}
class Child1 extends Parent {
    void disp(){
        System.out.println("This is the child1 class method");
    }
}
class Child2 extends Parent {
    void disp(){
        System.out.println("This is the child2 class method");
    }
}
public class P6 {
    public static void main(String[] args) {
        Parent p=new Parent();
        p.disp();
        Child1 ob1 = new Child1();
        Child2 ob2 = new Child2();
        ob1.disp();
        ob2.disp();
        p=ob1;
        p.disp();
        p=ob2;
        p.disp();
    }
}
