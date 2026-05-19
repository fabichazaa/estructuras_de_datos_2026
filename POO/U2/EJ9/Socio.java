
import java.util.ArrayList;
import java.util.List;

public class Socio {
    private String nombre;
    private final int numeroDeSocio;
    private String telefono;
    private final List<Prestamo> prestamos;

    public Socio(String nombre, String telefono) {
        this.nombre = nombre;
        this.numeroDeSocio = (int) (Math.random() * 10000);
        this.telefono = telefono;
        this.prestamos = new ArrayList<>();
    }

    public String getNombre() {
        return nombre;
    }

    public int getNumeroDeSocio() {
        return numeroDeSocio;
    }

    public String getTelefono() {
        return telefono;
    }

    public List<Prestamo> getPrestamos() {
        return prestamos;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    public void agregarPrestamo(Prestamo prestamo) {
        prestamos.add(prestamo);
    }

    public void finalizarPrestamo(Prestamo prestamo) {
        prestamos.remove(prestamo);
    }

    public void mostrarPrestamos() {
        System.out.println("------------------------------");
        System.out.println("Prestamos del socio " + nombre + ":");
        for (Prestamo prestamo : prestamos) {
            System.out.println(prestamo.toString());
        }
        System.out.println("------------------------------");

    }

    public void cantidadPrestamosActuales() {
        System.out.println("Cantidad de prestamos del socio " + nombre + ": " + prestamos.size());
    }
}
