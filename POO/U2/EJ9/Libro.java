
import java.util.ArrayList;
import java.util.List;

public class Libro {
    private String titulo;
    private String autor;
    private String isbn;
    private int stock;
    private final List<Prestamo> prestamos;

    public Libro(String titulo, String autor, String isbn, int stock) {
        this.titulo = titulo;
        this.autor = autor;
        this.isbn = isbn;
        this.stock = stock;
        this.prestamos = new ArrayList<>();
    }

    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public String getISBN() {
        return isbn;
    }

    public int getStock() {
        return stock;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public void setISBN(String isbn) {
        this.isbn = isbn;
    }

    public int reducirStock() {
        if (stock > 0) {
            stock--;
            return stock;
        } else {
            System.out.println("No hay stock disponible para el libro: " + titulo);
            return stock;
        }
    }

    public int aumentarStock() {
        stock++;
        return stock;
    }

    public void agregarPrestamo(Prestamo prestamo) {
        prestamos.add(prestamo);
        reducirStock();
    }

    public void finalizarPrestamo(Prestamo prestamo) {
        prestamos.remove(prestamo);
        aumentarStock();
    }

    public void mostrarPrestamos() {
        System.out.println("------------------------------");
        System.out.println("Prestamos del libro " + titulo + ":");
        if (prestamos.isEmpty()) {
            System.out.println("No hay préstamos activos para este libro.");
        } else {
            for (Prestamo prestamo : prestamos) {
                System.out.println(prestamo.toString());
            }
        }
        System.out.println("------------------------------");
    }

    public void mostrarInformacion() {
        System.out.println("------------------------------");
        System.out.println("Título: " + titulo);
        System.out.println("Autor: " + autor);
        System.out.println("ISBN: " + isbn);
        System.out.println("Stock disponible: " + stock);
        System.err.println("Cantidad de préstamos actuales: " + prestamos.size());
        System.out.println("------------------------------");

    }
}
