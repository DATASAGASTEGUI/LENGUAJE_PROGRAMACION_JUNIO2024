using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace ProyectoVentanaAritemetica
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void BtnLimpiar_Click(object sender, RoutedEventArgs e)
        {
            txtN1.Clear();
            txtN2.Clear();
            txtResultado.Clear();

            rbSumar.IsChecked = false;
            rbRestar.IsChecked = false;
            rbMultiplicar.IsChecked = false;
            rbDividir.IsChecked = false;
        }

        private void BtnSalir_Click(object sender, RoutedEventArgs e)
        {
            Close();
        }

        private void Operar_Checked(object sender, RoutedEventArgs e)
        {
            if(double.TryParse(txtN1.Text, out double num1) && 
                double.TryParse(txtN2.Text, out double num2) )
            {
                double resultado = 0;
                string operador = (sender as RadioButton).Content.ToString();
                OperacionesAritmeticas oa = null;
                switch (operador)
                {
                    case "Sumar": 
                        oa = new OperacionesAritmeticas(num1, num2, "+");
                        resultado = oa.CalcularResultado();break;
                    case "Restar":
                        oa = new OperacionesAritmeticas(num1, num2, "-");
                        resultado = oa.CalcularResultado(); break;
                    case "Multiplicar":
                        oa = new OperacionesAritmeticas(num1, num2, "*");
                        resultado = oa.CalcularResultado(); break;
                    case "Dividir":
                        oa = new OperacionesAritmeticas(num1, num2, "/");
                        resultado = oa.CalcularResultado(); break;
                }
                txtResultado.Text = resultado.ToString();   
            }else
            {
               MessageBox.Show("Entrada incorrecta","Advertencia",MessageBoxButton.OK, MessageBoxImage.Warning);
               BtnLimpiar_Click(null,null);
            }
        }
    }
}