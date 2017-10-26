using System;
using System.Collections.Generic;
using System.Text;

namespace ConsoleApp1
{
    
    class NiceSquare
    {
        private string mySquare;
        
        /**
         * NiceSquare render "something" inside a nice square
        **/
        public NiceSquare(string something)
        {
            

            mySquare = "+";

            for (byte i = 0; i<something.Length + 2 ; i++)
            {
                mySquare = mySquare + "-";
            }

            mySquare = mySquare + "+\n| " + something + " |\n+";

            for (byte i = 0; i <= something.Length +1 ; i++)
            {
                mySquare = mySquare + "-";
            }

            mySquare = mySquare + "+\n";

        }

        public string getmySquare()
        {
            return mySquare;
        }
    }
}
