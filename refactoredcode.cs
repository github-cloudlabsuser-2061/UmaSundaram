using System;

class Program
{
    static void Main(string[] args)
    {
        try
        {
            int[] arr = { /* your array elements here */ };
            int total = CalculateSum(arr);
            Console.WriteLine("Sum of the numbers: " + total);
        }
        catch (Exception ex)
        {
            Console.WriteLine("\nProgram terminated by user.");
            Environment.Exit(1);
        }
    }

    static int CalculateSum(int[] arr)
    {
        int sum = 0;
        foreach (int num in arr)
        {
            sum += num;
        }
        return sum;
    }
}