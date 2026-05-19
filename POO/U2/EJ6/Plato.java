public class Plato {
    private final int codigo;
    private String nombre;
    private String descripcion;
    private double precio;
    private double precioFinal;
    private boolean esVegano;

    public Plato(String nombre, String descripcion, double precio, boolean esVegano) {
        this.codigo = (int) (Math.random() * 10000);
        this.nombre = nombre;
        this.descripcion = descripcion;
        this.precio = precio;
        this.precioFinal = precio;
        this.esVegano = esVegano;
    }

    public int getCodigo() {
        return this.codigo;
    }

    public String getNombre() {
        return this.nombre;
    }

    public String getDescripcion() {
        return this.descripcion;
    }

    public double getPercio() {
        return this.precio;
    }

    public boolean isEsVegano() {
        return this.esVegano;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    public void setEsVegano(boolean esVegano) {
        this.esVegano = esVegano;
    }

    public void aplicarDescuento(double porcentaje) {
        if (porcentaje < 0 || porcentaje > 100) {
            System.out.println("Porcentaje de descuento inválido. Debe estar entre 0 y 100.");
            return;
        }
        double descuento = this.precio * (porcentaje / 100);
        precioFinal = this.precio - descuento;
    }

    public double getPrecioFinal() {
        return this.precioFinal;
    }

    @Override
    public String toString() {
        return "Plato " + this.codigo + ": " + this.nombre + " - " 
        + this.descripcion + " - $" + this.precio + " - " + (this.esVegano ? "Vegano" : "No vegano");
    }
}