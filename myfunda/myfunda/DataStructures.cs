using System;
namespace myfunda
{
    

    public class LinkedList
    {
        public Node head;

        public class Node
        {

            public int data;
            public Node next;

            public Node (int d)
            {

                data = d;
                next = null;
            }
        }

        public void PrintLinkedList()
        {
            LinkedList.Node n = this.head;
            while (n != null)
            {
                System.Console.WriteLine(n.data.ToString());
                n = n.next;
            }
        }

        public void Push(Node n)
        {
            Node h = this.head;
            this.head = n;
            this.head.next = h;

        }

        public Node LastNode()
        {
            LinkedList.Node n = this.head;

            while (n.next!=null)
            {

                n = n.next;
            }
            return n;
        }

        public void Append(Node n)
        {
            this.LastNode().next=n;

        }

        internal void InsertAfter(Node prevNode, Node newNode)
        {
            if (prevNode == null)
            {
                Console.WriteLine("The given previous node Cannot be null");
                return;
            }
           
            newNode.next = prevNode.next;
            prevNode.next = newNode;
        }



    }

    class Stack
    {
        static int max = 5;
        int[] array = new int[max];
        int top;

        public Stack()
        {
            top = -1;
        }

        public bool push(int item)
        {
            if (top >= max)
            {
                System.Console.WriteLine("Stack overflow exception.\n");
                return false;
            }
            else
            {
                array[++top] = item;
                return true;
            }
        }



        public int pop()
        {
            if (!isEmpty())
            {
                return array[top--];
            }
            else
            {
                Console.WriteLine("Stack Underflow\n");
                return -1;
            }
        }

        public bool isEmpty()
        {
            return (top < 0);
        }

        public void PrintStack()
        {

            for (int i = 0; i <= top; i++)
            {
                Console.Write(array[i].ToString() + ",");
            }
            Console.Write("\n");
        }


    }

    class Queue
    {
        static int max = 5;
        int[] array = new int[max];
        int start = 0;
        int end = -1;
        int size = 0;

        public bool isFull()
        {
            return (size == max);
        }

        public void EnQueue(int item)
        {
            if (isFull())
            {
                Console.WriteLine("Queue Overflow");
            }
            else
            {

                end = (end + 1) % max;
                array[end] = item;
                size++;
            }
        }

        public int DeQueue()
        {

            if (size == 0)
            {
                Console.WriteLine("Queue already empty");
                return -1;
            }
            else
            {
                int next = start;
                start = (start + 1) % max;
                size--;
                return next;
            }


        }

        public int Front()
        {
            if (size == 0)
            {
                Console.WriteLine("Queue empty");
                return -1;
            }
            else
            {
                return start;
            }
        }

        public int End()
        {
            if (size == 0)
            {
                Console.WriteLine("Queue empty");
                return -1;
            }
            else
            {
                return end;
            }
        }

        public void Print()
        {
            int str = start;
            for (int i = 1; i <= size; i++)
            {
                Console.WriteLine(array[str]);
                str = (str + 1) % max;

            }
        }
    }

    class BinaryTreeNode
    {
        int key;
        public BinaryTreeNode left, right;

        public BinaryTreeNode(int item)
        {
            key = item;
            left = null;
            right = null;
        }
    }

    class BinaryTree
    {
        public BinaryTreeNode root;

        public BinaryTree(int key)
        {
            root = new BinaryTreeNode(key);
        }
        public BinaryTree()
        {
            root = null;
        }
    }
}


