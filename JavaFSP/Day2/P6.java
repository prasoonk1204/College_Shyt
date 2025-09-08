// Write a program to display the creation of garbage in java

class garbage {
    int a,b;
    void input(int x, int y) {
        a = x;
        b = y;
    }
    void disp() {
        System.out.println("The value of a and b are "+a+" "+b);
    }
}
class P6 {
    public static void main(String[] args) {
        garbage ob1 = new garbage();
        garbage ob2 = new garbage();
        ob1.input(20,40);
        ob2.input(120,400);
        ob2=ob1; // Assigning one object to another
        ob1.disp();
        ob2.disp();
    }
}
