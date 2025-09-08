// Hierarchical Inheritance

class A {
    int a=10,b=15,c=20;
}
class B extends A {
    void calc() {
        int x=a+b+c;
        System.out.println("The sum is = "+x);
    }
}
class C extends A {
    void calc1(){
        int x=a*b*c;
        System.out.println("The product is = "+x);
    }
}
class P9 {
    public static void main(String[] args) {
        B ob=new B();
        ob.calc();
        C ob1=new C();
        ob1.calc1();
    }
}
