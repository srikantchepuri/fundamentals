using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace myfunda
{
    class CSharp
    {
        //sbyte 8 bit   -128 to 127
        //byte  8 bit   0 to 255
        //short 16 bit  -32,768 to 32,767
        //ushort    16 bit  0 to 65,535
        //int   32 bit  -2,147,483,648 to 2,147,483,647
        //uint  32 bit  0 to 4,294,967,295
        //long  64 bit  -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
        //ulong 64 bit  0 to 18,446,744,073,709,551,615
        //char  16 bit  0 to 65535
        //float 32 bit  -1.5 x 1045 to 3.4 x 1038
        //double    64 bit  -5 x 10324 to 1.7 x 10308
        //decimal   128 bit -1028 to 7.9 x 1028
        //bool  --- True or false
        public void Checkedfuction()
        {
            int num;
            // assign maximum value
            num = int.MaxValue;
            Console.WriteLine(num);
            try
            {
                checked
                {
                    // forces stack overflow exception
                    num = num + 1;
                    Console.WriteLine(num);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
            Console.ReadLine();
        }

        public void UnCheckedfuction()
        {
            int num;
            // assign maximum value
            num = int.MaxValue;
            Console.WriteLine(num);
            try
            {
                unchecked
                {
                    // forces stack overflow exception
                    num = num + 1;
                    Console.WriteLine(num);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
            Console.ReadLine();
        }

        public void LockFunction()
        {
            CSharp p = new CSharp();
            // creating lock segment. all the resources that are used in lock segment, can't be used by another thread until it releases.
            lock (p)
            {
                p.PrintName();
            }
            Console.ReadLine();
        }

        struct book
        {
            public string bookname;
            public int price;
            public string category;
        }

        public void CheckStructures()
        {
            book language;

            // Storing value in language variable
            Console.Write("Enter book name:\t");
            language.bookname = Console.ReadLine();
            Console.Write("Enter book price:\t");
            language.price = Convert.ToInt32(Console.ReadLine());
            Console.Write("Enter book category:\t");
            language.category = Console.ReadLine();

            Console.Write("Book Name:\t{0}", language.bookname);
            Console.Write("\nBook Price:\t{0}", language.price);
            Console.Write("\nBook Category:\t{0}", language.category);
        }
        public void CheckEnum()
        {
            attandance present = attandance.Monday;//Valid
            Console.WriteLine(present);

            //attandance absent = attandance.Sunday;//Invalid
            Console.ReadLine();
        }
        public enum attandance
        {
            Monday,
            Tuesday,
            Wednesday,
            Thursday,
            Friday
        }

        public void PrintName()
        {
            Console.Write("This is a print function");
        }
    }


}