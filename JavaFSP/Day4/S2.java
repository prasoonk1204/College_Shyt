// WAP to create a timmer where the timer will countdown from 10 to 0 and on reaching 0 a bomb need to be exploded
// package CS393.JavaFSP.Day4;

public class S2 {
    public static void main(String[] args) {
        for(int i=10;i>=0; i--){
            try {
                System.out.println(i);
                Thread.sleep(2000);
                if(i==0) System.out.println("Bomb.....");
            } catch (InterruptedException e) {}
        }
    }
}
