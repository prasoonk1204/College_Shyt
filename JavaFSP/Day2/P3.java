// constructor overloading

class CO {
    int a,b;
    CO(){
        a=20;
        b=40;
    }
    CO(int x){
        a=x;
        b=180;
    }
    CO(int x, int y){
        a=x;
        b=y;
    }
    void disp(){
        System.out.println("The value of a and b are "+a+" "+b);
    }
}

class P3 {
    public static void main(String[] args) {
        CO ob1 = new CO(50);
        CO ob2 = new CO(50,80);
        CO ob3 = new CO();

        ob1.disp();
        ob2.disp();
        ob3.disp(); 
    }
}
