// WAP to display the use of priority queue in java
import java.util.*;
class pqueue {
    public static void main(String args[]) {
        PriorityQueue pq = new PriorityQueue();

        pq.add("Sumit");
        pq.add("Vijay");
        pq.add("Jai");
        pq.add("Raj");
        pq.add("Anuj");

        System.out.println("Priority Queue: " + pq);

        System.out.println("Head element: " + pq.peek());

        System.out.println("Removing head element: " + pq.poll());
        System.out.println("Priority Queue after removing head: " + pq);

        System.out.println("Is the priority queue empty? " + pq.isEmpty());

        System.out.println("Size of the priority queue: " + pq.size());

        System.out.println("Iterating through the priority queue:");
        Iterator itr = pq.iterator();
        while (itr.hasNext()) {
            System.out.println(itr.next());
        }

        // Removing first element
        System.out.println("After first removal: ");
        pq.remove();
        System.out.println(pq);

        // Clearing the priority queue
        pq.clear();
        System.out.println("Priority Queue after clearing all elements: " + pq);
    }
}
