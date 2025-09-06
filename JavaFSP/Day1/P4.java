// WAP in java to display the use of constructor

class Constructor1 {
    int a,b;
    Constructor1(){ // constructor
        a=10;
        b=20;
    }
    void disp(){
        System.out.println(a+" "+b);
    }
}

class P4 {
    public static void main(String[] args) {
        Constructor1 ob = new Constructor1(); // Here constructor is called automatically
        ob.disp();
    }
}