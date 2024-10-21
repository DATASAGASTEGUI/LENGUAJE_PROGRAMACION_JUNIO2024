class Principal2
{
    static void Main()
    {
       Console.Clear();

       //DEFINIR TIPOS VARIABLES
       double numero1, numero2, suma;

       //ENTRADA
       Console.Write("Ingresar número 1? ");
       numero1 = Convert.ToDouble(Console.ReadLine());
       Console.Write("Ingresar número 2? ");
       numero2 = Convert.ToDouble(Console.ReadLine());         

       //PROCESO
       suma = sumar(numero1,numero2);

       //SALIDA
       Console.WriteLine("Suma: " + Math.Round(suma,2));

       Console.ReadLine();
    }

    static double sumar(double n1, double n2) {
        return n1 + n2;
    }
}