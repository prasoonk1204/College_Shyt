// WAP in java to display the use of super method

package CS393.JavaFSP.Day3;

class A {
    int x,y;
    A(int a, int b) {
        x = a;
        y = b;
    }
    void disp1(){
        System.out.println(x+" "+y);
    }
}

class B extends A {
    int c,d;
    B(int p, int q, int r, int s) {
        super(p, q);
        c=r;
        d=s;
    }
    void disp2(){
        System.out.println(c+" "+d);
    }
}

public class P1 {
    public static void main(String[] args) {
        B ob = new B(10,20,30,40);
        ob.disp1();
        ob.disp2();
    }
}
