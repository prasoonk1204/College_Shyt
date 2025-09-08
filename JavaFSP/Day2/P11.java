// Method Overriding
class Parent {
    int a=15,b=30;
    void disp() {
        int c=a+b;
        System.out.println("The sum is = "+c);
    }
}
class Child extends Parent {
    void disp() {
        super.disp();
        int d=a*b;
        System.out.println("The product is = "+d);
    }
}
class P11 {
    public static void main(String[] args) {
        Child ob = new Child();
        ob.disp();
    }
}
