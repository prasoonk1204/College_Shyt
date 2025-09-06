// Write a program to write the use of class and object

class Test1 {
    int a,b;
    void input(){
        a = 10;
        b = 20;
    }
    void disp(){
        System.out.println("The value of a is: "+a+" "+b);
    }
}

class P2{
    public static void main(String[] args) {
        Test1 t1 = new Test1();
        t1.input();
        t1.disp();
    }
}