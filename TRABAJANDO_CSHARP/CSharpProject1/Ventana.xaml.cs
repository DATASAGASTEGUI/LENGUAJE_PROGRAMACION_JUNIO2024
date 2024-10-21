using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace CSharpProject1
{
    /// <summary>
    /// Lógica de interacción para Ventana.xaml
    /// </summary>
    public partial class Ventana : Window
    {
        public Ventana()
        {
            InitializeComponent();
        }

        // Método para sumar los números ingresados en las cajas
        private void Sumar(object sender, RoutedEventArgs e)
        {
            try
            {
                double n1, n2, suma;
                n1 = double.Parse(txtN1.Text);
                n2 = double.Parse(txtN2.Text);
                suma = n1 + n2;
                txtSuma.Text = Convert.ToString(Math.Round(suma, 2));
            }
            catch (FormatException ex)
            {
                //MessageBox.Show(ex.Message, "ERROR", MessageBoxButton.OK, MessageBoxImage.Error);
                MessageBox.Show("ENTRADA INCORRECTA", "Error", MessageBoxButton.OK, MessageBoxImage.Error);
            }

        }

        // Método para limpiar las cajas de texto
        private void Limpiar(object sender, RoutedEventArgs e)
        {
            txtN1.Text = "";
            txtN2.Text = "";
            txtSuma.Text = "";
        }

        // Método para cerrar la ventana
        private void CerrarVentana(object sender, RoutedEventArgs e)
        {
            this.Close();
        }
    }
}
