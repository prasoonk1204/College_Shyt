// WAP in java to take two numbers and find their sum and display the result using the concept of class and object.

class Sum{
    int a,b,sum;
    void input(){
        a = 10;
        b = 20;
    }
    void calc(){
        sum=(a+b);
    }
    void disp(){
        System.out.println("The sum of a and b is: "+sum);
    }
}
class P3{
    public static void main(String[] args) {
        Sum ob = new Sum();
        ob.input();
        ob.calc();
        ob.disp();
    }
}