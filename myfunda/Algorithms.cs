using System;
namespace myfunda
{
    public class Algorithms
    {
        public Algorithms()
        {
        }


        public static void BinarySearch(int[] myarray, int key)
        {
            int left = 0;
            int right = myarray.Length - 1;
            int position = -1;

            while (left <= right)
            {
                int mid = (left + right) / 2;

                if (myarray[mid] == key)
                {
                    position = mid;
                    break;
                }
                else if (myarray[mid] < key)
                {

                    left = mid + 1;
                }
                else
                {

                    right = mid - 1;
                }

            }


            if (position == -1)
            {
                Console.WriteLine("Not Found");
            }
            else
            {

                Console.WriteLine("Found at " + position.ToString());
            }

            Console.ReadKey();

        }


        public static void BubbleSort(int[] myarray)
        {

            Console.Write("\nArray before bubble sorting :");
            printArray(myarray);


            bool isSorted = false;
            while (isSorted == false)
            {
                isSorted = true;
                for (int i = 0; i < myarray.Length - 1; i++)
                {

                    if (myarray[i] > myarray[i + 1])
                    {
                        int tmp = myarray[i];
                        myarray[i] = myarray[i + 1];
                        myarray[i + 1] = tmp;
                        isSorted = false;
                    }
                }
            }

            Console.ReadKey();

            Console.Write("\nArray after bubble sorting : ");

            printArray(myarray);
        }


        public static void InsertionSort(int[] myarray)
        {

            Console.Write("\nArray before Insertion sorting :");
            printArray(myarray);


            for (int i = 1; i <= myarray.Length - 1; i++)
            {
                if (myarray[i] < myarray[i - 1])
                {
                    int k = myarray[i];


                    for (int j = i - 1; j >= 0; j--)
                    {
                        if (myarray[j] > k)
                        {
                            myarray[j + 1] = myarray[j];
                            myarray[j] = k;
                        }
                        else
                        {
                            myarray[j + 1] = k;
                            break;
                        }

                    }


                }


            }

            Console.ReadKey();

            Console.Write("\nArray after Insertion sorting :");

            printArray(myarray);
        }


        public static void SelectionSort(int[] myarray)
        {
            for (int i = 0; i < myarray.Length - 1; i++)
            {
                int minpo = i;

                for (int j = i + 1; j <= myarray.Length - 1; j++)
                {
                    if (myarray[j] < myarray[minpo])
                    {
                        minpo = j;
                    }
                }


                int temp = myarray[i];
                myarray[i] = myarray[minpo];
                myarray[minpo] = temp;

            }
        }

        public static void BuildMaxHeap(int[] heaparray)
        {
            //int[] myarray = new int[] { 20, 13, 2, 23, 15,33,21,54 };
            for (int i = (heaparray.Length / 2) - 1; i >= 0; i--)
            {
                Heapify(heaparray, heaparray.Length, i);
            }
        }
        public static void Heapify(int[] heaparray, int n, int i)
        {

            int max = i;  // Initialize largest as root
            int l = 2 * i + 1;  // left = 2*i + 1
            int r = 2 * i + 2;  // right = 2*i + 2

            // If left child is larger than root
            if (l < n && heaparray[l] > heaparray[max])
                max = l;

            // If right child is larger than largest so far
            if (r < n && heaparray[r] > heaparray[max])
                max = r;


            if (i != max)
            {
                int temp = heaparray[i];
                heaparray[i] = heaparray[max];
                heaparray[max] = temp;
                Heapify(heaparray, n, max);
            }


        }

        public static void printArray(int[] myarray)
        {
            foreach (int item in myarray)
            {

                Console.Write(item.ToString() + ",");
            }


        }

    }

    public class QuickFindUF
    {

        private int[] d;

        //Initialize the Quickfind Array
        public QuickFindUF(int n)
        {

            d = new int[n];
            for (int i = 0; i < n;i++)
            {

                d[i] = i;

            }

            Union(1,9);
            Union(2,1);
            Union(5, 6);
            Union(3,4);
            Union(8,6);
            Union(7,2);
                  

        }

        public bool Connected(int p, int q)
        {

            return d[p] == d[q];
        }

        public void Union(int p, int q)
        {
            int pid = d[p];

            for (int i = 0;i<d.Length;i++)
            {
                if (d[i] == pid) { d[i] = d[q]; }

            }

           
        }



        public void BinarySearch(int[] myarray, int key)
        {



            int position = -1;
            int left = 0;
            int right = myarray.Length - 1;

            while (left < right)
            {
                int median = (right + left) / 2;

                if (myarray[median] == key)
                {
                    position = median;
                    break;
                }
                else if (myarray[median] > key)
                {
                    right = median;
                }
                else
                {
                    left = median;
                }

            }

            if (position != -1)
            {
                Console.WriteLine("The key :" + key.ToString() + " is found at :" + position.ToString());
            }
            else
            {
                Console.WriteLine("The key :" + key.ToString() + " is not found in the array");
            }




            Console.ReadKey();



        }

        public void JumpSearch(int[] myarray, int m, int key)
        {
            bool found = false;
            for (int i = 0; i < myarray.Length; i = i + m)
            {
                if (myarray[i] == key)
                {
                    Console.WriteLine("The key :" + key.ToString() + " is found at :" + i.ToString());
                    found = true;
                }
                else if (myarray[i] > key && i != 0)
                {
                    for (int j = i - m; j < i; j++)
                    {
                        if (myarray[j] == key)
                        {
                            Console.WriteLine("The key :" + key.ToString() + " is found at :" + i.ToString());
                            found = true;
                        }
                    }
                }

            }

            if (found == false)
                Console.WriteLine("Key not found in array");


        }

        public void LinearSearch(int[] myarray, int key)
        {



            int position = -1;
            for (int i = 0; i < myarray.Length; i++)
            {
                if (key == myarray[i])
                {

                    position = i;
                }
            }
            if (position != -1)
            {
                Console.WriteLine("The key :" + key.ToString() + " is found at :" + position.ToString());
            }
            else
            {
                Console.WriteLine("The key :" + key.ToString() + " is not found in the array");
            }

            Console.ReadKey();
        }
        public void InsertionSort(int[] myarray)
        {
            for (int i = 1; i <= myarray.Length - 1; i++)
            {
                int k = myarray[i];
                int j = i - 1;

                while (j >= 0 && myarray[j] > k)
                {
                    myarray[j + 1] = myarray[j];

                    j--;
                }
                myarray[j + 1] = k;

            }
        }

        public void SelectionSort(int[] myarray)
        {
            for (int i = 0; i < myarray.Length - 1; i++)
            {
                int min_position = i;

                for (int j = i + 1; j <= myarray.Length - 1; j++)
                {
                    if (myarray[j] < myarray[min_position])
                    {
                        min_position = j;
                    }
                }


                int temp = myarray[i];
                myarray[i] = myarray[min_position];
                myarray[min_position] = temp;

            }
        }

        public void BuildMaxHeap(int[] heaparray)
        {
            //int[] myarray = new int[] { 20, 13, 2, 23, 15,33,21,54 };
            for (int i = (heaparray.Length / 2) - 1; i >= 0; i--)
            {
                Heapify(heaparray, heaparray.Length, i);
            }
        }
        public void Heapify(int[] heaparray, int n, int i)
        {

            int max = i;  // Initialize largest as root
            int l = 2 * i + 1;  // left = 2*i + 1
            int r = 2 * i + 2;  // right = 2*i + 2

            // If left child is larger than root
            if (l < n && heaparray[l] > heaparray[max])
                max = l;

            // If right child is larger than largest so far
            if (r < n && heaparray[r] > heaparray[max])
                max = r;


            if (i != max)
            {
                int temp = heaparray[i];
                heaparray[i] = heaparray[max];
                heaparray[max] = temp;
                Heapify(heaparray, n, max);
            }


        }

        public void BubbleSort(int[] myarray)
        {
            bool swap = true;

            while (swap)
            {
                swap = false;
                for (int j = 0; j < myarray.Length - 1; j++)
                {
                    if (myarray[j] > myarray[j + 1])
                    {
                        int temp = myarray[j];
                        myarray[j] = myarray[j + 1];
                        myarray[j + 1] = temp;
                        swap = true;
                    }
                }

            }

        }


        public void MergeSort(int[] myarray, int left, int right)
        {
            if (left < right)
            {
                //int middle
            }
        }
    }

}
