/*find if an array contains duplicate values*/
import java.util.*;
class Duplicate{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter size of array");
		int n = sc.nextInt();
		System.out.println("Enter array elements between 1 and "+n);
		
		int[] arr = new int[n+1];
		for(int i = 1;i<=n;i++)
		{
			arr[i] = sc.nextInt();

		}
		int[] temp = new int[n+1];
		for(int i = 1;i<=n;i++)
		{
			temp[arr[i]] += 1;
		}
		for(int i = 1;i<=n;i++)
		{	
			if(temp[i] > 1)
				System.out.println("Duplicate: "+i);
		}

	}

}