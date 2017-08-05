import java.util.*;

class SumOfNumbersWithoutMod{

	public static void main(String args[]){

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int n1 = n;
		int sum = 0;
		int newNum = 0;
		int temp,temp2;

		//REVERSE
		while(n>0){
			temp = (n/10)*10;
			temp2 = n-temp;
			newNum = newNum*10+temp2;
			n = n/10;
		}
		System.out.println("Reverse is " +newNum);

		//SUM OF DIGITS

		while(n1>0){
			temp = (n1/10)*10;
			temp2 = n1-temp;
			sum += temp2;
			n1 = n1/10;
		}
		System.out.println("Sum is "+sum);		
	}
}