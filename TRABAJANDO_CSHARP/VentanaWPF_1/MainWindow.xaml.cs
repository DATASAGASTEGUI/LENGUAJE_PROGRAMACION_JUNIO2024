using System.Linq.Expressions;
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

namespace VentanaWPF_1
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

        private void BtnSumar_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                double n1 = double.Parse(TxtN1.Text);// CAE
                double n2 = double.Parse(TxtN2.Text);

                double r = Sumar.Suma(n1, n2);


                TxtResultado.Text = r.ToString();
            } catch(Exception ex1)
            {
                MessageBox.Show("Entrada Incorrecta");
            }
        }

        private void BtnNuevo_Click(object sender, RoutedEventArgs e)
        {
            TxtN1.Text = "";
            TxtN2.Text = "";
            TxtResultado.Text = "";

            rbSumar.IsChecked = false;
            rbMultiplicar.IsChecked = false;
        }

        private void BtnSalir_Click(object sender, RoutedEventArgs e)
        {
            this.Close();
        }

        private void rbSumar_Checked(object sender, RoutedEventArgs e)
        {
            try { 
            double n1 = double.Parse(TxtN1.Text);// 5
            double n2 = double.Parse(TxtN2.Text);

            double r = Sumar.Suma(n1, n2);


            TxtResultado.Text = r.ToString();
        }catch(Exception ex)
            {
                MessageBox.Show("Entrada Incorrecta");
            }
        }

        private void rbMultiplicar_Checked(object sender, RoutedEventArgs e)
        {
            double n1 = double.Parse(TxtN1.Text);// 5
            double n2 = double.Parse(TxtN2.Text);

            double r = Sumar.Multiplicar(n1, n2);


            TxtResultado.Text = r.ToString();
        }

        private void CboAritmetica_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            string opcion = ((ComboBoxItem)CboAritmetica.SelectedItem)?.Content.ToString();
       
            if (opcion == "Sumar")
            {
                try
                {
                    double n1 = double.Parse(TxtN1.Text);// 5
                    double n2 = double.Parse(TxtN2.Text);

                    double r = Sumar.Suma(n1, n2);


                    TxtResultado.Text = r.ToString();
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Entrada Incorrecta");
                }
            }
        
            if(opcion == "Multiplicar")
            {
                double n1 = double.Parse(TxtN1.Text);// 5
                double n2 = double.Parse(TxtN2.Text);
                double r = Sumar.Multiplicar(n1, n2);
                TxtResultado.Text = r.ToString();

            }

        }
    }
}