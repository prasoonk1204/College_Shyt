// WAP in java to display the use of parameterized constructor

class PC1 {
    int a,b;
    PC1(int x,int y){ // parameterized constructor
        a=x;
        b=y;
    }
    void disp(){
        System.out.println(a+" "+b);
    }
}

class P5 {
    public static void main(String[] args) {
        PC1 ob = new PC1(23,56); 
        ob.disp();
    }
}