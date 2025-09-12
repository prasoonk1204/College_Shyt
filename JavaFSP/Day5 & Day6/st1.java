// WAP to accept a string from the user and check whether it is a palindrome or not.
import java.util.Scanner;
public class st1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String str = sc.nextLine();
        String rev = "";
        // We can use a for loop to reverse the string
        // for (int i = str.length() - 1; i >= 0; i--) {
        //     rev += str.charAt(i);
        // }

        // We can use StringBuffer to reverse the string
        rev = (new StringBuffer(str)).reverse().toString();

        if (str.equals(rev)) { 
            System.out.println(str + " is a palindrome.");
        } else {
            System.out.println(str + " is not a palindrome.");
        }
        sc.close();
    }
}