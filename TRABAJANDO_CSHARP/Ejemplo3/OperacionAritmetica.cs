class OperacionAritmetica    
{
    //1.ATRIBUTOS DE LA CLASE
    //ENTRADA
    public double numero1;
    public double numero2;
    public char operador; 
    //SALIDA
    public double resultado;

    //CONSTRUCTORES
    public OperacionAritmetica() 
    {
       this.numero1 = 0;
       this.numero2 = 0;
       this.operador = '+'; 
    } 

    public OperacionAritmetica(double numero1, double numero2, char operador) 
    {
       this.numero1 = numero1;
       this.numero2 = numero2;
       this.operador = operador; 
    } 

    //PROCESO
    public double proceso() 
    {
       switch(this.operador)
       {
        case '+': this.resultado = this.numero1 + this.numero2;break;
        case '-': this.resultado = this.numero1 - this.numero2;break;
        case '*': this.resultado = this.numero1 * this.numero2;break;
        case '/': this.resultado = this.numero1 / this.numero2;break;
       }
       return this.resultado;
    }  

    public override string ToString() {
       return this.numero1 + " " + this.operador + " " + this.numero2 + " = " +
              Math.Round(this.proceso(),2);
    } 
    
}