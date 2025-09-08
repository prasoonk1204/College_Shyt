// Variable Overriding
class A {
    int a = 10;
}

class B extends A {
    int a = 20;
    void disp() {
        System.out.println(a);
        System.out.println(super.a);
    }
}
class P10 {
    public static void main(String[] args) {
        B ob = new B();
        ob.disp();
    }
}
