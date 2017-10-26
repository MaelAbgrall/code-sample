using System;

namespace ConsoleApp1
{
    class Program
    {
        public static void Print(string somethingFromUser)
        {
            Console.WriteLine("you wrote" + somethingFromUser +"\n");
        }

        #region region main

        static void Main(string[] args)
        {
            Console.WriteLine("Hello World! \n new line \t tab");
            byte mybyte; //0-255
            short myshort;
            int myint;
            long mylongint;
            float myfloat;
            double mydoublefloat;

            Console.WriteLine("say something");
            var something = Console.ReadLine();

            Console.WriteLine("do you want to print it? [yes/no]");
            string line = Console.ReadLine();
            switch (line)
            {
                case "y":
                case "yes":
                    Print(something);
                    break;

                case "nice square":
                    NiceSquare square = new NiceSquare(something);
                    Console.WriteLine(square.getmySquare());
                    break;

                default:
                    break;
            }
            Console.WriteLine("\n end of programm, press any key to exit...");
            Console.ReadKey();
        }
        
        #endregion
    }
}
