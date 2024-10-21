using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SQLite;
using System.Collections;
using System.Text.RegularExpressions;
using System.Security.Cryptography;

namespace ProyectoConsoleCrud
{
    internal class ProgramSQLite
    {
        static void Main(string[] args)
        {
            //CONFIGURAR LA CONSOLA
            /*
            Cls();
            Console.Title = "MENU APLICACION";
            Console.ForegroundColor = ConsoleColor.White;
            Console.BackgroundColor = ConsoleColor.Magenta;
            Console.SetWindowSize(150, 20); // Ancho: 100 columnas, Alto: 30 filas
            Console.SetBufferSize(150, 300); // Tamaño del buffer
            */
            while (true)
            {
                Cls();
                Console.WriteLine("[1] Buscar un producto por si ID.");
                Console.WriteLine("[2] Mostrar todos los productos");
                Console.WriteLine("[3] Insertar un producto");
                Console.WriteLine("[4] Actualizar un producto");
                Console.WriteLine("[5] Eliminar un producto por su ID");
                Console.WriteLine("[6] Salir");

                Console.Write("Ingrese  opción? ");
                string opcion = Console.ReadLine();

                switch (opcion)
                {
                    case "1": Cls(); opcion1(); Pause(); break;
                    case "2": Cls(); opcion2(); Pause(); break;
                    case "3": Cls(); opcion3(); Pause(); break;
                    case "4": Cls(); opcion4(); Pause(); break;
                    case "5": Cls(); opcion5(); Pause(); break;
                    case "6": Cls(); Environment.Exit(0); break;
                }
            }

        }

        public static void crearTabla()
        {
            SQLiteConnection conexion = ObtenerConexion();
            if (conexion != null)
            {
                Console.WriteLine("OK: CONEXION");
                try
                {
                   string query = @"
                   CREATE TABLE IF NOT EXISTS Producto (
                      id_producto  INTEGER  PRIMARY KEY AUTOINCREMENT,
                      nombre       TEXT    NOT NULL,
                      descripcion  TEXT    NOT NULL,
                      precio       REAL    NOT NULL,
                      stock        INTEGER NOT NULL,
                      categoria    TEXT    NOT NULL
                   )";
                   SQLiteCommand cmd = new SQLiteCommand(query,conexion);
                   cmd.ExecuteNonQuery();
                   Console.WriteLine("OK: CREATE TABLE");
                }
                catch 
                {
                    Console.WriteLine("ERROR: CREATE TABLE");
                }
            }
            else
            {
                Console.WriteLine("ERROR: CONEXION");
            }
            conexion.Close();
        }

        public static SQLiteConnection ObtenerConexion()
        {
            //string ruta_relativa = "data/ferreteria.sqlite";
            //string ruta_absoluta = Path.GetFullPath(ruta_relativa);

            string conexionPath = @"Data Source=C:/LENGUAJE_PROGRAMACION/TRABAJANDO_CSHARP/ProyectoConsoleCrud/bin/Debug/data/ferreteria.sqlite;Version=3;";

            SQLiteConnection conexion = new SQLiteConnection(conexionPath);
            try
            {
                conexion.Open();
                return conexion;
            }
            catch (SQLiteException ex)
            {
                Console.WriteLine(ex.Message);
                return null;
            }
        }

        public static void opcion1()
        {
            Console.WriteLine("[1] BUSCAR UN PRODUCTO POR SU ID");
            Console.WriteLine("--------------------------------");
            Console.Write("Ingrese id del producto a buscar? ");
            string idProducto = Console.ReadLine();
            string patron = "[0-9]+"; //Alfabeto Español
            bool correcto = Regex.IsMatch(idProducto, patron);
            if (correcto)
            {
                Select2(int.Parse(idProducto));
            }
            else
            {
                Console.WriteLine("ID no válido");
            }
        }

        public static void opcion2()
        {
            Console.WriteLine("[2] MOSTRAR TODOS LOS PRODUCTOS");
            Console.WriteLine("-------------------------------");
            Select3();
        }

        public static void opcion3()
        {
            Console.WriteLine("[3] INSERTAR UN PRODUCTO");
            Console.WriteLine("------------------------");
            Console.WriteLine("Lista de IDs no usados:");
            Console.WriteLine(string.Join(", ", ObtenerIdDisponibles().ToArray()));

            Console.WriteLine("Desea ingresar id producto 1.automatico/2.manual?");
            string opcion = Console.ReadLine();

            if (opcion == "1")
            {
                Console.WriteLine("Ingrese nombre? ");
                string nombre = Console.ReadLine();
                Console.WriteLine("Ingrese descripción? ");
                string descripcion = Console.ReadLine();
                Console.WriteLine("Ingrese precio? ");
                double precio = double.Parse(Console.ReadLine());
                Console.WriteLine("Ingrese stock? ");
                int stock = int.Parse(Console.ReadLine());
                Console.WriteLine("Ingrese categoría? ");
                string categoria = Console.ReadLine();

                Insert(nombre, descripcion, precio, stock, categoria);
            }
            if (opcion == "2")
            {
                Console.Write("Ingrese id del producto a insertar? ");
                string idProducto = Console.ReadLine();
                string patron = "[0-9]+"; //Alfabeto Español
                bool correcto = Regex.IsMatch(idProducto, patron);
                if (correcto)
                {
                    Select2(int.Parse(idProducto));
                }
                else
                {
                    Console.WriteLine("ID no válido");
                }

                Console.WriteLine("Ingrese nombre? ");
                string nombre = Console.ReadLine();
                Console.WriteLine("Ingrese descripción? ");
                string descripcion = Console.ReadLine();
                Console.WriteLine("Ingrese precio? ");
                double precio = double.Parse(Console.ReadLine());
                Console.WriteLine("Ingrese stock? ");
                int stock = int.Parse(Console.ReadLine());
                Console.WriteLine("Ingrese categoría? ");
                string categoria = Console.ReadLine();

                InsertManual(int.Parse(idProducto), nombre, descripcion, precio, stock, categoria);
            }

        }

        public static void opcion4()
        {
            Console.WriteLine("[4] ACTUALIZAR UN PRODUCTO");
            Console.WriteLine("--------------------------");
            Console.Write("Ingrese id del producto a actualizar? ");
            string idProducto = Console.ReadLine();
            string patron = "[0-9]+"; //Alfabeto Español
            bool correcto = Regex.IsMatch(idProducto, patron);
            if (correcto)
            {
                if (existeProducto(int.Parse(idProducto)))
                {
                    Select2(int.Parse(idProducto));
                    Console.WriteLine("Ingrese nombre nuevo? ");
                    string nombre = Console.ReadLine();
                    Console.WriteLine("Ingrese descripción nuevo? ");
                    string descripcion = Console.ReadLine();
                    Console.WriteLine("Ingrese precio nuevo? ");
                    double precio = double.Parse(Console.ReadLine());
                    Console.WriteLine("Ingrese stock nuevo? ");
                    int stock = int.Parse(Console.ReadLine());
                    Console.WriteLine("Ingrese categoría nuevo? ");
                    string categoria = Console.ReadLine();

                    Console.Write("Confirmar actualización S/N? ");
                    string confirmacion = Console.ReadLine();
                    if (confirmacion.ToUpper() == "S")
                    {
                        Update(int.Parse(idProducto), nombre, descripcion, precio, stock, categoria);
                        //Console.WriteLine("OK: UPDATE");
                    }
                    else
                    {
                        Console.WriteLine("Actualizar se cancelo");
                    }
                }
                else
                {
                    Console.WriteLine($"ID {idProducto} no existe");
                }
            }
            else
            {
                Console.WriteLine($"ID {idProducto} no válido");
            }
        }

        public static void opcion5()
        {
            Console.WriteLine("[5] ELIMINAR UN PRODUCTO POR SU ID");
            Console.WriteLine("----------------------------------");

            Console.Write("Ingrese id del producto a eliminar? ");
            string idProducto = Console.ReadLine();
            string patron = "[0-9]+"; //Alfabeto Español
            bool correcto = Regex.IsMatch(idProducto, patron);
            if (correcto)
            {
                if (existeProducto(int.Parse(idProducto)))
                {
                    Select2(int.Parse(idProducto));


                    Console.Write("Confirmar eliminación S/N? ");
                    string confirmacion = Console.ReadLine();
                    if (confirmacion.ToUpper() == "S")
                    {
                        Delete(int.Parse(idProducto));
                        //Console.WriteLine("OK: DELETE");
                    }
                    else
                    {
                        Console.WriteLine("Eliminar se cancelo");
                    }
                }
                else
                {
                    Console.WriteLine($"ID {idProducto} no existe");
                }
            }
            else
            {
                Console.WriteLine($"ID {idProducto} no válido");
            }
        }

        public static void Cls()
        {
            Console.Clear();
        }

        public static void Pause()
        {
            Console.Write("Presione una tecla para continuar...");
            Console.Read();
        }

        //CRUD = CREATE(INSERT) READ(SELECT) UPDATE DELETE

        public static void Select1()
        {
            using (SQLiteConnection conexion = ObtenerConexion())
            {
                if (conexion != null)
                {
                    try
                    {
                        string query = "SELECT * FROM Producto";
                        SQLiteCommand cmd = new SQLiteCommand(query, conexion);
                        SQLiteDataReader reader = cmd.ExecuteReader();
                        while (reader.Read())
                        {
                            int id_producto = int.Parse(reader["id_producto"].ToString());
                            string nombre = reader["nombre"].ToString();
                            string descripcion = reader["descripcion"].ToString();
                            double precio = double.Parse(reader["precio"].ToString());
                            int stock = int.Parse(reader["stock"].ToString());
                            string categoria = reader["categoria"].ToString();

                            Console.WriteLine("Id Producto: " + id_producto);
                            Console.WriteLine("Nombre     : " + nombre);
                            Console.WriteLine("Descripción: " + descripcion);
                            Console.WriteLine("Precio     : " + precio);
                            Console.WriteLine("Stock      : " + stock);
                            Console.WriteLine("Categoria  : " + categoria);
                            Console.WriteLine();
                        }
                        reader.Close();
                    }
                    catch (SQLiteException ex)
                    {
                        Console.WriteLine($"ERROR: QUERY {ex.Message}");
                    }
                }
                else
                {
                    Console.WriteLine("ERROR: CONEXION");
                }
            }
            
        }
        public static ArrayList ObtenerIdDisponibles()
        {
            HashSet<int> listaUsados = new HashSet<int>();
            ArrayList listaTodos = new ArrayList();
            ArrayList listaNoUsados = new ArrayList();
            using (SQLiteConnection conexion = ObtenerConexion())
            {
                if (conexion != null)
                {
                    try
                    {
                        string query1 = "SELECT id_producto FROM Producto";
                        string query2 = "SELECT id_producto FROM Producto ORDER BY id_producto DESC LIMIT 1";

                        SQLiteCommand cmdUsados = new SQLiteCommand(query1, conexion);
                        SQLiteDataReader reader1 = cmdUsados.ExecuteReader();

                        while (reader1.Read())
                        {
                            int id_producto = int.Parse(reader1["id_producto"].ToString());
                            listaUsados.Add(id_producto);
                        }
                        reader1.Close();
                        SQLiteCommand cmdTodos = new SQLiteCommand(query2, conexion);
                        SQLiteDataReader reader2 = cmdTodos.ExecuteReader();

                        while (reader2.Read())
                        {
                            int id_producto = int.Parse(reader2["id_producto"].ToString());
                            for (int i = 1; i <= id_producto; i++)
                            {
                                listaTodos.Add(i);
                            }
                        }
                        reader2.Close();
                        for (int i = 0; i < listaTodos.Count; i++)
                        {
                            if (!listaUsados.Contains((int)listaTodos[i]))
                            {
                                listaNoUsados.Add((int)listaTodos[i]);
                            }
                        }
                    }
                    catch (SQLiteException ex)
                    {
                        Console.WriteLine($"ERROR: QUERY {ex.Message}");
                    }
                }
                else
                {
                    Console.WriteLine("ERROR: CONEXION");
                }
            }
            return listaNoUsados;
        }

        public static void Select2(int id_producto_buscar)
        {
            using (SQLiteConnection conexion = ObtenerConexion())
            {
                if (conexion != null)
                {
                    try
                    {
                        string query = "SELECT * FROM Producto WHERE id_producto = @id_producto_p";
                        SQLiteCommand cmd = new SQLiteCommand(query, conexion);
                        cmd.Parameters.AddWithValue("@id_producto_p", id_producto_buscar);
                        SQLiteDataReader reader = cmd.ExecuteReader();
                        if (reader.Read())
                        {
                            int id_producto = int.Parse(reader["id_producto"].ToString());
                            string nombre = reader["nombre"].ToString();
                            string descripcion = reader["descripcion"].ToString();
                            double precio = double.Parse(reader["precio"].ToString());
                            int stock = int.Parse(reader["stock"].ToString());
                            string categoria = reader["categoria"].ToString();

                            Console.WriteLine("Id Producto: " + id_producto);
                            Console.WriteLine("Nombre     : " + nombre);
                            Console.WriteLine("Descripción: " + descripcion);
                            Console.WriteLine("Precio     : " + precio);
                            Console.WriteLine("Stock      : " + stock);
                            Console.WriteLine("Categoria  : " + categoria);
                            Console.WriteLine();
                        }
                        else
                        {
                            Console.WriteLine($"ID {id_producto_buscar} NO EXISTE");
                        }
                        reader.Close();
                    }
                    catch (SQLiteException ex)
                    {
                        Console.WriteLine($"ERROR: QUERY {ex.Message}");
                    }
                }
                else
                {
                    Console.WriteLine("ERROR: CONEXION");
                }
            }
        }

        public static bool existeProducto(int id_producto_buscar)
        {
            bool existe = false;
            using (SQLiteConnection conexion = ObtenerConexion())
            {
                if (conexion != null)
                {
                    try
                    {
                        string query = "SELECT * FROM Producto WHERE id_producto = @id_producto_p";
                        SQLiteCommand cmd = new SQLiteCommand(query, conexion);
                        cmd.Parameters.AddWithValue("@id_producto_p", id_producto_buscar);
                        SQLiteDataReader reader = cmd.ExecuteReader();
                        if (reader.Read())
                        {
                            existe = true;
                        }
                        reader.Close();
                    }
                    catch (SQLiteException ex)
                    {
                        Console.WriteLine($"ERROR: QUERY {ex.Message}");
                    }
                }
                else
                {
                    Console.WriteLine("ERROR: CONEXION");
                }
                conexion.Close();
            }
            return existe;
        }

        public static void Select3()
        {
            using (SQLiteConnection conexion = ObtenerConexion())
            {
                if (conexion != null)
                {
                    try
                    {
                        string query = "SELECT * FROM Producto";
                        SQLiteCommand cmd = new SQLiteCommand(query, conexion);
                        SQLiteDataReader reader = cmd.ExecuteReader();
                        while (reader.Read())
                        {
                            int id_producto = int.Parse(reader["id_producto"].ToString());
                            string nombre = reader["nombre"].ToString();
                            string descripcion = reader["descripcion"].ToString();
                            double precio = double.Parse(reader["precio"].ToString());
                            int stock = int.Parse(reader["stock"].ToString());
                            string categoria = reader["categoria"].ToString();


                            Console.WriteLine("{0,5} {1,-20} {2,-50} {3,10} {4,10} {5,-20}",
                                                                                   id_producto,
                                                                                   nombre,
                                                                                   descripcion,
                                                                                   precio,
                                                                                   stock,
                                                                                   categoria
                                                                                   );
                        }
                        reader.Close();
                    }
                    catch (SQLiteException ex)
                    {
                        Console.WriteLine($"ERROR: QUERY {ex.Message}");
                    }
                }
                else
                {
                    Console.WriteLine("ERROR: CONEXION");
                }
            }
        }

        public static void Insert(string nombre,
                                  string descripcion, double precio,
                                  int stock, string categoria)
        {
            using (SQLiteConnection conexion = ObtenerConexion())
            {
                if (conexion != null)
                {
                    try
                    {
                        string query = @"INSERT INTO Producto(nombre,descripcion,precio,stock, categoria)
                                         VALUES(@nombre_p, @descripcion_p, @precio_p, @stock_p, @categoria_p)";
                        SQLiteCommand cmd = new SQLiteCommand(query, conexion);
                        cmd.Parameters.AddWithValue("@nombre_p", nombre);
                        cmd.Parameters.AddWithValue("@descripcion_p", descripcion);
                        cmd.Parameters.AddWithValue("@precio_p", precio);
                        cmd.Parameters.AddWithValue("@stock_p", stock);
                        cmd.Parameters.AddWithValue("@categoria_p", categoria);
                        cmd.ExecuteNonQuery();
                        Console.WriteLine("OK: QUERY INSERT");
                    }
                    catch (SQLiteException ex)
                    {
                        Console.WriteLine($"ERROR: QUERY {ex.Message}");
                    }
                }
                else
                {
                    Console.WriteLine("ERROR: CONEXION");
                }
                conexion.Close();
            }
        }

        public static void InsertManual(int idProducto, string nombre,
                                  string descripcion, double precio,
                                  int stock, string categoria)
        {
            using (SQLiteConnection conexion = ObtenerConexion())
            {
                if (conexion != null)
                {
                    try
                    {
                        string query = @"INSERT INTO Producto(id_producto,nombre,descripcion,precio,stock, categoria)
                                         VALUES(@id_producto_p, @nombre_p, @descripcion_p, @precio_p, @stock_p, @categoria_p)";
                        SQLiteCommand cmd = new SQLiteCommand(query, conexion);
                        cmd.Parameters.AddWithValue("@id_producto_p", idProducto);
                        cmd.Parameters.AddWithValue("@nombre_p", nombre);
                        cmd.Parameters.AddWithValue("@descripcion_p", descripcion);
                        cmd.Parameters.AddWithValue("@precio_p", precio);
                        cmd.Parameters.AddWithValue("@stock_p", stock);
                        cmd.Parameters.AddWithValue("@categoria_p", categoria);
                        cmd.ExecuteNonQuery();
                        Console.WriteLine("OK: QUERY INSERT MANUAL");
                    }
                    catch (SQLiteException ex)
                    {
                        Console.WriteLine($"ERROR: QUERY {ex.Message}");
                    }
                }
                else
                {
                    Console.WriteLine("ERROR: CONEXION");
                }
            }
        }

        public static void Update(int id_producto_buscar, string nombre_nuevo,
                                  string descripcion_nuevo, double precio_nuevo,
                                  int stock_nuevo, string categoria_nuevo)
        {
            using (SQLiteConnection conexion = ObtenerConexion())
            {
                if (conexion != null)
                {
                    try
                    {
                        string query = @"UPDATE Producto 
                                         SET nombre = @nombre_p, 
                                             descripcion = @descripcion_p,
                                             precio = @precio_p,
                                             stock = @stock_p,
                                             categoria = @categoria_p 
                                         WHERE id_producto = @id_producto_p";
                        SQLiteCommand cmd = new SQLiteCommand(query, conexion);
                        cmd.Parameters.AddWithValue("@id_producto_p", id_producto_buscar);
                        cmd.Parameters.AddWithValue("@nombre_p", nombre_nuevo);
                        cmd.Parameters.AddWithValue("@descripcion_p", descripcion_nuevo);
                        cmd.Parameters.AddWithValue("@precio_p", precio_nuevo);
                        cmd.Parameters.AddWithValue("@stock_p", stock_nuevo);
                        cmd.Parameters.AddWithValue("@categoria_p", categoria_nuevo);
                        int rowsAffected = cmd.ExecuteNonQuery();
                        if (rowsAffected > 0)
                        {
                            Console.WriteLine("OK: UPDATE");
                        }
                        else
                        {
                            Console.WriteLine("ERROR: NO EXISTE REGISTRO PARA ACTUALIZAR");
                        }
                    }
                    catch (SQLiteException ex)
                    {
                        Console.WriteLine($"ERROR: QUERY UPDATE {ex.Message}");
                    }
                }
                else
                {
                    Console.WriteLine("ERROR: CONEXION");
                }
            }
        }

        public static void Delete(int id_producto_eliminar)
        {
            using (SQLiteConnection conexion = ObtenerConexion())
            {
                if (conexion != null)
                {
                    try
                    {
                        string query = @"DELETE FROM Producto                                   
                                         WHERE id_producto = @id_producto_p";
                        SQLiteCommand cmd = new SQLiteCommand(query, conexion);
                        cmd.Parameters.AddWithValue("@id_producto_p", id_producto_eliminar);
                        int rowsAffected = cmd.ExecuteNonQuery();
                        if (rowsAffected > 0)
                        {
                            Console.WriteLine("OK: DELETE");
                        }
                        else
                        {
                            Console.WriteLine("ERROR: NO EXISTE REGISTRO PARA ELIMINAR");
                        }
                    }
                    catch (SQLiteException ex)
                    {
                        Console.WriteLine($"ERROR: QUERY DELETE {ex.Message}");
                    }
                }
                else
                {
                    Console.WriteLine("ERROR: CONEXION");
                }
            }
        }


    }
}
