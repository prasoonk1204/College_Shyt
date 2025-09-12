// WAP to display the use of stack in java

import java.util.*;
class stk
{
    public static void main(String args[])
    {
        Stack s = new Stack();
        s.push("Ayan");
        s.push("Sovik");
        s.push("Amit");
        s.push("Ashish");
        s.push("Rajat");
        s.push("Prantor");

        System.out.println("Stack: " + s);
        System.out.println("Top element: " + s.peek().toString());

        System.out.println("Before popping any value ");
        Iterator i = s.iterator();
        while(i.hasNext()){
            System.out.println(i.next());
        }

        s.pop();

        System.out.println("After popping a value ");
        Iterator i2 = s.iterator();
        while(i2.hasNext()){
            System.out.println(i2.next());
        }

        // Removing elements from the stack
        s.remove(2);
        System.out.println("Stack after removing element at index 2: " + s);
        System.out.println("After removing");
        Iterator i3 = s.iterator();
        while(i3.hasNext()){
            System.out.println(i3.next());
        }

        // To check whether the stack is empty or not
        boolean b=s.empty();
        System.out.println("Is the stack empty? " + b);

        // To search an element in the stack
        int p=s.search("Ashish");
        System.out.println("Position of Ashish in the stack: " + p);
        int p1=s.search("Ayan");
        System.out.println("Position of Ayan in the stack: " + p1);

        // To remove all the elements from the stack
        s.removeAllElements();
        System.out.println("Stack after removing all elements: " + s);
    }
}