using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProyectoVentanaAritemetica
{
    class OperacionesAritmeticas
    {
        //Atributos Clase
        //Entrada
        private double numero1;
        private double numero2;
        private string operador;
        //Salida
        private double resultado;

        //Propiedades de la Clase
        public double Numero1
        {
            get { return numero1; }
            set { numero1 = value; }
        }

        public double Numero2
        {
            get { return numero2; }
            set { numero2 = value; }
        }

        public string Operador
        {
            get { return operador; }
            set { operador = value; }
        }

        public double Resultado
        {
            get { return resultado; }
        }

        //Contructores
        public OperacionesAritmeticas()
        {
            numero1 = 0;
            numero2 = 0;
            operador = "+";
            resultado = CalcularResultado();
        }

        public OperacionesAritmeticas(double n1, double n2, string ope)
        {
            numero1 = n1;
            numero2 = n2;
            operador = ope;
            resultado = CalcularResultado();
        }

        //Procesar la entrada
        public double CalcularResultado()
        {
            switch(operador)
            {
                case "+": return numero1 + numero2;
                case "-": return numero1 - numero2;
                case "*": return numero1 * numero2;
                case "/": return numero2 != 0 ? numero1 / numero2 : double.NaN;
                default: return double.NaN;
            }
        }
    }
}
