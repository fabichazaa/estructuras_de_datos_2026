
import java.time.LocalDate;

public class Prestamo {
    private LocalDate fechaPrestamo;
    private LocalDate fechaDevolucion;
    private boolean concluido;
    private final Libro libro;
    private final Socio socio;

    public Prestamo(LocalDate fechaPrestamo, LocalDate fechaDevolucion, Libro libro, Socio socio) {
        this.fechaPrestamo = fechaPrestamo;
        this.fechaDevolucion = fechaDevolucion;
        this.concluido = false;
        this.libro = libro;
        this.socio = socio;
    }

    public LocalDate getFechaPrestamo() {
        return fechaPrestamo;
    }

    public LocalDate getFechaDevolucion() {
        return fechaDevolucion;
    }

    public Libro getLibro() {
        return libro;
    }
    
    public Socio getSocio() {
        return socio;
    }
    
    public boolean isConcluido() {
        return concluido;
    }

    public void setFechaPrestamo(LocalDate fechaPrestamo) {
        this.fechaPrestamo = fechaPrestamo;
    }

    public void setFechaDevolucion(LocalDate fechaDevolucion) {
        this.fechaDevolucion = fechaDevolucion;
    }

    public boolean estaVencido() {
        LocalDate fechaActual = LocalDate.now();
        return fechaActual.isAfter(fechaDevolucion);
    }

    public void finalizarPrestamo() {
        this.concluido = true;
        System.out.println("Préstamo finalizado exitosamente.");
    }

    @Override
    public String toString() {
        return "Libro " + this.libro.getTitulo() + " solcitiado por " + this.socio.getNombre() + " | " +
        "Fecha prestamo:" + fechaPrestamo + " | Fecha devolucion:" + fechaDevolucion;
    }
}
