import java.util.Scanner;

public class Java_Task2 {
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int minutes = sc.nextInt();

        int years = minutes/525600;
        int rem = minutes - (years * 525600);
        int days = rem/1440;

        System.out.println(minutes + " minutes is approximately " + years + " years and "+days+" days");
    }
}
