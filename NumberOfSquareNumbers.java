/*java program to find out number of perfect squares between between any two numbers*/

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class NumberOfSquareNumbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for(int i = 0;i<t;i++)
            {         
            int n1 = sc.nextInt();
            int n2 = sc.nextInt();
            
            int num = (int)(Math.floor(Math.sqrt(n2))- Math.ceil(Math.sqrt(n1))+1) ;
            System.out.println(""+num);
        }
    }                        
}
