// WAP in java to display the use of single level inheritance
class A { //Parent Class
    int i=10;
}
class B extends A { //inheriting from parent class
    void disp(){
        System.out.println(i);
    }
}
class P7 {
    public static void main(String[] args) {
        B ob = new B();
        ob.disp();
    }
}
