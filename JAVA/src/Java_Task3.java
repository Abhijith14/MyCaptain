import java.util.Scanner;

public class Java_Task3 {
    public static void main(String[] args)
    {
        int choice;
        System.out.println("Pick one : 1. Hi\t 2. Hey\t 3. Hello");
        Scanner sc = new Scanner(System.in);
        choice = sc.nextInt();

        switch(choice)
        {
            case 1:
                    System.out.println("You Said Hi");
                    break;
            case 2:
                    System.out.println("You Said Hey");
                    break;
            case 3:
                    System.out.println("You Said Hello");
                    break;
            default:
                    System.out.println("Invalid Choice !!");
        }
    }
}
