public class St2 {
    public static void main(String[] args) {
        String s = "Strings are immutable";
        s = s.concat(" all the time");
        System.out.println(s);

        char result = s.charAt(7);
        System.out.println(result);

        String str1 = "Strings are immutable";
        String str2 = new String("Strings are immutable");
        String str3 = new String("Integers are not immutable");

        int res = str1.compareTo(str2);
        System.out.println("Comp1 " + res);

        res = str2.compareTo(str3);
        System.out.println("Comp2 " + res);
    }
}
