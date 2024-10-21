class Principal1
{
    static void Main1()
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
       suma = numero1 + numero2;

       //SALIDA
       Console.WriteLine("Suma: " + Math.Round(suma,2));

       Console.ReadLine();
    }
}
