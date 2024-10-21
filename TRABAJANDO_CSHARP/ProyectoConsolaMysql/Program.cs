using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProyectoConsolaMysql
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string conexionUrl = "Server=localhost;Database=ferreteria;Uid=root;Pwd=12345678;Port=3307";
            try
            {
                MySqlConnection conexion = new MySqlConnection(conexionUrl);
                conexion.Open();
                Console.WriteLine("OK: CONEXION");

                string query = "SELECT * FROM Producto";
                MySqlCommand comando = new MySqlCommand(query, conexion);
                MySqlDataReader reader = comando.ExecuteReader();
                while (reader.Read())
                {
                    Console.WriteLine("Id Producto: "+ reader["id_producto"]);
                    Console.WriteLine("Nombre     : "+ reader["nombre"]);
                }

            } 
            catch 
            {
                Console.WriteLine("ERROR: CONEXION");
            }
        }
    }
}
