class Principal
{
   static void Main() 
   {
      ejemplo3();
   }

   static void ejemplo1() {
      OperacionAritmetica oa = new OperacionAritmetica(4,5,'+');
      Console.WriteLine("Suma: " + oa.proceso());

      oa.numero1 = 9;
      oa.numero2 = 10;
      oa.operador = '*';
      Console.WriteLine("Multiplicación: " + oa.proceso());
   }

   static void ejemplo2() {
      Console.Clear();
      //DEFINIR TIPOS VARIABLES
      double numero1, numero2, resultado;
      char operador;
      //ENTRADA
      Console.WriteLine("Ingresar número 1? ");
      numero1 = double.Parse(Console.ReadLine());
      Console.WriteLine("Ingresar número 2? ");
      numero2 = double.Parse(Console.ReadLine());
      Console.WriteLine("Ingresar operador? ");
      operador = char.Parse(Console.ReadLine());

      //PROCESO
      OperacionAritmetica oa = new OperacionAritmetica(numero1,numero2,operador);
      resultado = oa.proceso();
   
      //SALIDA
      Console.WriteLine("Resultado: " + Math.Round(resultado,2));
      Console.WriteLine(oa); //Llamar al ToString

      Console.ReadLine();
   }

   static void ejemplo3() {
      Console.Clear();
      Random random = new Random();
      char[] operador = {'+','-','*','/'};

      OperacionAritmetica[] vector_objetos = new OperacionAritmetica[10];
      for(int i=0; i<vector_objetos.Length; i++) {
         int indice = random.Next(0,operador.Length);
         vector_objetos[i] = new OperacionAritmetica(random.Next(1,10), random.Next(1,10),operador[indice]);
      }

      foreach(OperacionAritmetica oa in vector_objetos) {
         Console.WriteLine(oa);
      }
      Console.ReadLine();
   }
}