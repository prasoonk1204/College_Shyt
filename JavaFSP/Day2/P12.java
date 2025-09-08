// This keyword
class this_eg {
    int a,b;
    this_eg(int a, int b) {
        this.a = a;
        this.b = b;
    }
    void disp() {
        System.out.println("The value of a and b are "+a+" "+b);
    }
}
class P12 {
    public static void main(String[] args) {
        this_eg ob = new this_eg(10,20);
        ob.disp();
    }
}
