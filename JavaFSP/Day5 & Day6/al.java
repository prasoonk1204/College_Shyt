// WAP to display the use of array list in java
import java.util.*;
class al {
    public static void main(String[] args) {
        ArrayList al = new ArrayList();

        System.out.println("Initial size of ArrayList: " + al.size());

        // Adding elements to the ArrayList
        al.add("C");
        al.add("A");
        al.add("E");
        al.add("B");
        al.add("D");
        al.add("F");
        al.add(5);
        al.add("Ayan");
        al.add(20.25);
        al.add(1,"A2"); // Adding element in middle

        // Displaying the ArrayList
        System.out.println("ArrayList: " + al);
        // Displaying the size of the ArrayList after additions
        System.out.println("Size of ArrayList after additions: " + al.size());

        // Removing elements from the ArrayList
        al.remove("F");
        al.remove(2); // Removing element from index 2

        // Displaying the ArrayList after removals
        System.out.println("ArrayList after removal: " + al);
        // Displaying the size of the ArrayList after removals
        System.out.println("Size of ArrayList after removals: " + al.size());

        // Traversing the ArrayList through iterator
        System.out.println("Traversing the ArrayList:");
        Iterator itr = al.iterator();
        while(itr.hasNext()) {
            System.out.println(itr.next());
        }

        // Traversing the ArrayList through iterator but converting to string
        System.out.println("Traversing the ArrayList (String):");
        String s;
        Iterator itr1 = al.iterator();
        while(itr1.hasNext()) {
            s = itr1.next().toString();
            System.out.println(s);
        }

        // Traversing the list using for but converting to string
        System.out.println("Traversing the ArrayList using for loop (String):");
        String s2;
        for(int i = 0; i < al.size(); i++) {
            s2 = al.get(i).toString();
            System.out.println(s2);
        }
    }
}
