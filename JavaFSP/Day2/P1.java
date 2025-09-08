// WAP in java to display use of method overloading
class func_overloading{
    void disp(){
        System.out.println("No Argument");
    }
    void disp(int x){
        System.out.println(x);
    }
    void disp(int x, int y){
        System.out.println(x+" "+y);
    }
}

public class P1 {
    public static void main(String[] args) {
        func_overloading ob = new func_overloading();
        ob.disp(50,60);
        ob.disp();
        ob.disp(90);
    }
}   