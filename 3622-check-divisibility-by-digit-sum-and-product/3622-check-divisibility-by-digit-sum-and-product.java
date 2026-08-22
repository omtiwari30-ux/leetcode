class Solution {
    public boolean checkDivisibility(int n) {
        int digits=0;
        int sum=0;
        int product=1;
        int copy=n;
        while(n!=0){
            digits=n%10;
            sum+=digits;
            product*=digits;

            n/=10;

        }

        int res=sum+product;

        if (copy%res==0)
            return true;
        else
            return false;
    }
}