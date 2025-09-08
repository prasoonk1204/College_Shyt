// WAP in java to calculate the area of a rectangle and that of a circle by overlading the area method

class Area {
    public void area(int a, int b) {
        System.out.println("Area of rectangle = " + (a * b));
    }
    public void area(int r) {
        System.out.println("Area of circle = " + (3.14 * r * r));
    }
}

class P2 {
    public static void main(String[] args) {
        Area ob = new Area();
        ob.area(10, 20);
        ob.area(5);
    }
}
