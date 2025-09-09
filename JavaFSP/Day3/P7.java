// WAP to display use of try and catch block.

package CS393.JavaFSP.Day3;

public class P7 {
    public static void main(String[] args) {
        int x=12;
        int y=2;

        try {
            int z=x/y;
            System.out.println("The result is "+z);
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
