// WAP to display the use of vector in java
import java.util.*;
class vec {
    public static void main(String args[]) {
        Vector vec = new Vector();
        // Adding elements to the vector
        vec.add("Ayan");
        vec.add("Roy");
        vec.add("S");
        vec.add("25");

        // Size of the vector
        System.out.println("Size of the vector after additions: " + vec.size());
        // Displaying the vector
        System.out.println("Vector: " + vec);

        // Traversing the vector
        System.out.println("Traversing the vector:");
        Iterator en = vec.iterator();
        while (en.hasNext()) {
            System.out.println(en.next());
        }

        // Removing an element from the vector
        vec.remove("Roy");
        vec.remove(2); // Removing using index
        
        // Size after removal
        System.out.println("Size of the vector after removal: " + vec.size());
        // Displaying the vector after removal
        System.out.println("After removing S: " + vec);

        // Iteration after removal
        System.out.println("Iterating through the vector after removal:");
        Iterator en1 = vec.iterator();
        while (en1.hasNext()) {
            System.out.println(en1.next());
        }
    }
}
