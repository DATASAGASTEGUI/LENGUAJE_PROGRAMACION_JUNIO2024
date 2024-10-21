class Principal
{
   static void Main() 
   {
      {
        double x = 1.72;
        int y = (int)x;
        Console.WriteLine("X: " + y);
      }

      {
        float x = 1.72f;
        int y = (int)x;
        Console.WriteLine("X: " + y);
      }

      {
         int numerador = 2;
         int denominador = 3;
         double cociente = Math.Round(numerador / (double)denominador,2);
         Console.WriteLine("Cociente: " + cociente);
      }
   }
}
