import java.util.Scanner;

class 5
{
    static int[] print(int num[], int n)
    {
       
        return num;
    }
    static int fact(int n)
    {
        int fact=1;
        for(int i=1;i<=n;i++){
            fact=fact*i;
        }
        return fact;
    }
public static void main(String[] args) {
   Scanner sc=new Scanner(System.in);
   int t,cno=1;
   t=sc.nextInt();
   for(int k=0;k<t;k++)
   {
       int n,trace,temp=0;
       n=sc.nextInt();
       int[] num=new int[n];
       int f=fact(n)/fact(n-2);
       int[][] ar=new int[f][n];
       int[][] ar1=new int[n][n];
       int[][] new1=new int[n][n];
       for(int i=0;i<n;i++)
       {
           num[i]=i+1;
       }
       int ij=0;
       for (int j = 1; j <= n; j++) {
           
                for (int i = 0; i < n-1; i++,ij++) {
                    temp = num[i];
                    num[i] = num[i+1];
                    num[i+1] = temp;
                    for(int m=0;m<n;m++)
						ar[ij][m]=num[m];
				}
            }
            trace=sc.nextInt();
            if(trace<n||trace>n*n)
				System.out.println("IMPOSSIBLE");
            else if(trace>=n)
            {
                int rem,temp1,x1=0,x=0;
                boolean tp=true;
                temp1=n-1;
                x=trace%n;
                if(x==0)
                {
                    for(int i=0;i<n;i++)
                    new1[i][i]=trace/n;
                }
                else{
                new1[0][0]=x;
                rem=trace-x;
                while(tp)
                {
                    if(rem%temp1==0)
                    {
                        x1=rem/temp1;
                        tp=false;
                    }
                    else
                    {  
                        temp1=temp1-1;
                    }
                }
                for(int i=1;i<n;i++)
                new1[i][i]=x1;
                if(n-temp1==2)
                {  
                    new1[0][0]=1;
                    new1[temp1][temp1]=x-1;
                }
                }
               
                for(int i=0;i<n;i++)
                {
                    for(int j=0;j<f;j++)
                    {
                        if(ar[j][i]==new1[i][i])
                        {
                            for(int m=0;m<n;m++)
                            {
                                ar1[i][m]=ar[j][m];
                                ar[j][m]=100;
                            }
                            j=100;
                        }
                    }
                }
                boolean last=true;
                for(int i=0;i<n;i++)
                {
                    for(int j=0;j<n;j++)
                    {  
                        if(ar1[i][j]==0)
                        {  
                            last=false;
                            j=100;
                            i=100;
                        }
                    }
                }
                if(last==false)
					System.out.printf("Case #%d: IMPOSSIBLE\n",k+1);
                else{
					System.out.printf("Case #%d: POSSIBLE\n",k+1);
					for(int i=0;i<n;i++)
					{
                    for(int j=0;j<n;j++)
					{
                        System.out.print(ar1[i][j]+" ");
					}
						System.out.println();
					}
            }
           
   }
}
}
}