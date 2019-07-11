using System;

namespace myfunda
{
    class MainClass
    {
        public static void Main(string[] args)
        {


            //int[] tmparray = new int[]{ 20,13, 7, 2, 8, 3 };

            //BubbleSort(tmparray);

            //InsertionSort(tmparray);

            //int[] sortedarray = new int[] { 2,5,7,9,11,13,15,17,23}; 

            //BinarySearch(sortedarray,2);


            QuickFindUF qf=new QuickFindUF(10);

            Console.WriteLine(qf.Connected(1,2).ToString());
            Console.ReadKey();

            MainClass mc = new MainClass();

            mc.MakeLinkedList();


            //RegexExcercises();

            SortringExcercises();

            Console.ReadKey();




        }

        public static void SortringExcercises()
        {
            int[] myarray = new int[] { 20, 13, 2, 23, 15, 33, 21, 54 };
            CSAlgorithms csa = new CSAlgorithms();
            ////csa.InsertionSort(myarray);
            ////csa.BubbleSort(myarray);
            ////csa.SelectionSort(myarray);
            ////csa.BuildMaxHeap(myarray);

            ////csa.LinearSearch(myarray, 22);

            //int[] mysortedarray = new int[] { 2, 13, 22, 23, 25, 33, 41, 54 };
            //csa.BinarySearch(mysortedarray, 2);

            int[] mysortedarray = new int[] { 2, 13, 22, 23, 25, 33, 41, 54, 96 };
            csa.JumpSearch(mysortedarray, 3, 100);


            //CS Algorithms
            //CSharp csh = new CSharp();
            //csh.Checkedfuction();


            ////Data Structures
            //Stack stk = new Stack();
            //stk.push(20);
            //stk.push(23);
            //stk.push(13);
            //stk.PrintStack();


            //stk.pop();
            //stk.PrintStack();


            //Console.WriteLine("\n\n\nQueue Program\n");

            //Queue q = new Queue();
            //q.EnQueue(21);
            //q.EnQueue(24);
            //q.EnQueue(55);
            //q.EnQueue(63);
            //q.EnQueue(100);
            //q.EnQueue(31);
            //q.Print();

            //q.DeQueue();
            //q.DeQueue();

            //q.Print();
            //q.EnQueue(99);
            //q.Print();

        }

        public static void RegexExcercises()
        {
            //string input = "A Thousand Splendid Sun s S";
            //MatchCollection matches = Regex.Matches(input, @"\bS\S*");

            //string input = "123-45-6789";
            //MatchCollection matches = Regex.Matches(input, @"^\d{3}-\d{2}-\d{4}$");

            List<string> input = new List<string>();
            input.Add("321-555-4321");
            input.Add("123.555.1234");
            string regex = @"^\d{3}[.-]\d{3}[.-]\d{4}$";



            List<string> matches = new List<string>();
            foreach (string s in input)
            {
                if (Regex.Match(s, regex).Success)
                {
                    matches.Add(s);
                }
            }





            //Mr.Schafer
            //Mr Smith
            //Ms Davis
            //Mrs.Robinson
            //Mr.T


            if (matches.Count > 0)
            {
                foreach (string m in matches)
                {
                    Console.WriteLine(m);
                }

            }
            else
            {
                Console.WriteLine("No matches found :(");
            }


            //Match Social Security Number. 



        }

        public void MakeLinkedList()
        {
            LinkedList myLinkedList = new LinkedList();

            myLinkedList.head = new LinkedList.Node(1);

            LinkedList.Node second=new myfunda.LinkedList.Node(2);
            LinkedList.Node third = new myfunda.LinkedList.Node(3);

            myLinkedList.head.next = second;
            second.next = third;

            myLinkedList.PrintLinkedList();

            myLinkedList.Push(new LinkedList.Node(4));

            myLinkedList.PrintLinkedList();
            myLinkedList.Append(new LinkedList.Node(5));
            myLinkedList.PrintLinkedList();


        }

       





    }
}
