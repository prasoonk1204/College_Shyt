// WAP to accept two number, find there sum and display the result after 10 sec
package CS393.JavaFSP.Day4;

import java.util.Scanner;

public class S3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter first number: ");
        int num1 = sc.nextInt();

        System.out.print("Enter second number: ");
        int num2 = sc.nextInt();

        int sum = num1 + num2;

        try {
            System.out.println("Calculating sum... please wait 10 seconds.");
            Thread.sleep(10000); 
        } catch (InterruptedException e) {}


        System.out.println("The sum is: " + sum);

        sc.close();
    }
}
