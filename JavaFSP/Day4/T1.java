// WAp to dispay a thread using runnable interface

package CS393.JavaFSP.Day4;

class Thread1 implements Runnable { // Step 1
    public void run() { // Step 4
        for (int i = 0; i < 10; i++) {
            System.out.println("Thread1's i=" + i);
        }
    }
}

public class T1 {
    public static void main(String[] args) {
        Thread1 ob = new Thread1();
        Thread t = new Thread(ob); // Step2
        t.start();// Step 3
        for (int i = 0; i < 10; i++) {
            System.out.println("Thread main's i=" + i);
        }
    }
}
