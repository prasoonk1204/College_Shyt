// WAP to display the use of functional interface using lambda expression
package CS393.JavaFSP.Day3;
interface A2 {
    void disp();
    
}
public class P5 {
    public static void main(String[] args) {
        A2 ob = () -> { // This is lambda expression replacing the functional interface 
            System.out.println("This is implementation using lambda expression");
        };
        ob.disp();
    }
}
