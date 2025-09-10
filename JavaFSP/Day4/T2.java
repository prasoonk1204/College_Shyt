// WAP to create 4 different threads using main

package CS393.JavaFSP.Day4;

class Thread1 implements Runnable { 
    public void run() { 
        for (int i = 0; i < 10; i++) {
            System.out.println("Thread1's i=" + i);
        }
    }
}

class Thread2 implements Runnable { 
    public void run() { 
        for (int i = 0; i < 10; i++) {
            System.out.println("Thread2's i=" + i);
        }
    }
}

class Thread3 implements Runnable { 
    public void run() { 
        for (int i = 0; i < 10; i++) {
            System.out.println("Thread3's i=" + i);
        }
    }
}

public class T2 {
    public static void main(String[] args) {
        Thread1 ob1 = new Thread1();
        Thread2 ob2 = new Thread2();
        Thread3 ob3 = new Thread3();
        Thread t1 = new Thread(ob1); 
        Thread t2 = new Thread(ob2); 
        Thread t3 = new Thread(ob3); 
        t1.start();
        t2.start();
        t3.start();
        for (int i = 0; i < 10; i++) {
            System.out.println("Thread main's i=" + i);
        }
    }
}
