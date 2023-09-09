// gets min absolute difference when partitioning an array into two sets
public class SetPartition {
    public static int function(int[] arr, int index, int dif){

        int n = arr.length;

        if (index == n - 1) {
            // return absolute difference between the sets
            return Math.abs(dif);
        } else{
            int br1= function(arr,index+1,dif-arr[index+1]);
            int br2=function(arr,index+1,dif+arr[index+1]);
            return Math.min(br1,br2);
        }
    }

    public static void main(String[] args) {
        int[] arr = new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9};
        System.out.println(function(arr, -1, 0));
    }
}