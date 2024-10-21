using MySql.Data.MySqlClient;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Media.Media3D;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace ProyectoVentanaMysql
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

        private MySqlConnection ObtenerConexion()
        {
            string conexionUrl = "Server=localhost;Database=ferreteria;Uid=root;Pwd=12345678;Port=3306";
            MySqlConnection conexion = new MySqlConnection(conexionUrl);
            try
            {
                conexion.Open();
                return conexion;
            }
            catch (MySqlException ex)
            {
                Console.WriteLine(ex.Message);
                return null;
            }
        }

        private void BtnBuscar_Click(object sender, RoutedEventArgs e)
        {
            string valorstring = txtIdProducto.Text;
            if (!int.TryParse(valorstring, out _)) {  // Devuelve true si la cadena es un entero
                MessageBox.Show("No es un ID valido", "Error", MessageBoxButton.OK, MessageBoxImage.Error);
                return;
            }

            int idProducto = int.Parse(valorstring);

            using (MySqlConnection conexion = ObtenerConexion())
            {
                if (conexion != null)
                {
                    try
                    {
                        string query = "SELECT nombre FROM Producto WHERE id_producto = @idProducto";
                        MySqlCommand comando = new MySqlCommand(query, conexion);
                        comando.Parameters.AddWithValue("@idProducto", idProducto);
                        MySqlDataReader reader = comando.ExecuteReader();
                        if (reader.Read())
                        {
                            txtNombreProducto.Text = "" + reader["nombre"];
                        }
                        else
                        {
                            MessageBox.Show($"ID {idProducto} no existe", "Warning", MessageBoxButton.OK, MessageBoxImage.Warning);
                        }
                    }
                    catch (MySqlException ex)
                    {
                        MessageBox.Show($"Query Select {ex.Message}", "Error", MessageBoxButton.OK, MessageBoxImage.Error);
                    }
                }
                else
                {
                    MessageBox.Show("Conexion", "Error", MessageBoxButton.OK, MessageBoxImage.Error);
                }
            }
        }

        private void BtnLimpiar_Click(object sender, RoutedEventArgs e)
        {
            txtIdProducto.Clear();
            txtNombreProducto.Clear();
        }

        private void BtnSalir_Click(object sender, RoutedEventArgs e)
        {
            Close();
        }
    }
}