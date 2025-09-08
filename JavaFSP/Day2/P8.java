// WAP in java to display the use of multilevel inheritance

class A
{
    int a=50;
}
class B extends A
{
    int b=a*a;
}
class C extends B
{
    void disp(){
        System.out.println("The value of a and b are "+a+" "+b);
    }
}
class P8
{
    public static void main(String args[])
    {
        C ob=new C();
        ob.disp();
    }
}