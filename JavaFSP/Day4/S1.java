// WAP to display the use of sleep

package CS393.JavaFSP.Day4;

public class S1 {
    public static void main(String[] args) {
        for(int i=1;i<=10; i++){
            try {
                System.out.println(i);
                Thread.sleep(2000);
            } catch (InterruptedException e) {}
        }
    }
}
