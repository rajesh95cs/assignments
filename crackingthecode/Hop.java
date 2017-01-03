
public class Hop {


    public static int[] map = new int[100];

    public static int hop(int n){
		if (n<0){
			return 0;
		}
		else if(n==0){
			return 1;
		}
		else if(map[n]>-1){
			return map[n];
		}
		else {
			map[n]=hop(n-1)+hop(n-2)+hop(n-3);
			return map[n];
		}
			
	}
	
	public static void main(String[] args){
		int n = 25;
		for(int i=0;i<n;i++){
			map[i]=-1;
		}
		//System.out.println(map[2]);
		System.out.println(hop(n));
		
	}

}
