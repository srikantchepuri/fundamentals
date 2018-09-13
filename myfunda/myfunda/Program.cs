using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace myfunda
{
    class MainClass
    {
        public static void Main(string[] args)
        {

            BinaryTreeExcercise();
            
           
            //MainClass mc = new MainClass();

            //mc.MakeLinkedList();


            //RegexExcercises();

            //SortringExcercises();

            Console.ReadKey();




        }

        public static void QuickFindAlgorithms()
        {
            QuickFindUF qf = new QuickFindUF(10);

            Console.WriteLine(qf.Connected(1, 2).ToString());
            Console.ReadKey();

        }

        public static void SortringExcercises()
        {
            int[] myarray = new int[] { 20, 13, 2, 23, 15, 33, 21, 54 };
            Algorithms csa = new Algorithms();

            ////csa.InsertionSort(myarray);
            Algorithms.BubbleSort(myarray);
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

       

        public static void BinaryTreeExcercise()
        {
            
             BinaryTree bt = new BinaryTree(1);
            bt.root.left = new BinaryTreeNode(2);
            bt.root.right = new BinaryTreeNode(3);
            bt.root.left.left = new BinaryTreeNode(4);
            bt.root.left.right = new BinaryTreeNode(5);

            Console.WriteLine("Binary Tree Created");

            Console.WriteLine("InOrder Traversal");
            bt.TraverseInOrder(bt.root);
            Console.WriteLine("PreOrder Traversal");
            bt.TraversePreOrder(bt.root);
            Console.WriteLine("PostOrder Traversal");
            bt.TraversePostOrder(bt.root);



            Console.WriteLine("Insert a Node");
            bt.InsertNode(new BinaryTreeNode(6));
            Console.WriteLine("InOrder Traversal");
            bt.TraverseInOrder(bt.root);

            Console.WriteLine("Insert a Node");
            bt.InsertNode(new BinaryTreeNode(7));
            Console.WriteLine("InOrder Traversal");
            bt.TraverseInOrder(bt.root);


            Console.WriteLine("Insert a Node");
            bt.InsertNode(new BinaryTreeNode(8));
            Console.WriteLine("InOrder Traversal");
            bt.TraverseInOrder(bt.root);

            Console.WriteLine("Insert a Node");
            bt.InsertNode(new BinaryTreeNode(9));
            Console.WriteLine("InOrder Traversal");
            bt.TraverseInOrder(bt.root);

        }





    }
}
