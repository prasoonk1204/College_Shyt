// WAP to display the use of linked list in java

import java.util.*;
class ll {
    public static void main(String args[]) {
        LinkedList al = new LinkedList();
        // Adding elements to the linked list
        al.add("Ayan");
        al.add("Roy");
        al.add("S");
        al.add("25");

        // Size of the linked list
        System.out.println("Size of the linked list after additions: " + al.size());
        // Displaying the linked list
        System.out.println("Linked List: " + al);

        // Traversing the linked list
        System.out.println("Traversing the linked list:");
        Iterator itr = al.iterator();
        while (itr.hasNext()) {
            System.out.println(itr.next());
        }

        // Removing an element from the linked list
        al.remove("Roy");
        al.remove(2); // Removing using index

        // Size after removal
        System.out.println("Size of the linked list after removal: " + al.size());
        // Displaying the linked list after removal
        System.out.println("After removing S: " + al);

        // Iteration after removal
        System.out.println("Iterating through the linked list after removal:");
        Iterator itr1 = al.iterator();
        while (itr1.hasNext()) {
            System.out.println(itr1.next());
        }
    }
}
