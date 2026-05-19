import java.time.LocalDate;

public class Main {
    public static void main(String[] args) {
        Socio socio = new Socio("Chipa", "46572");
        Socio socio2 = new Socio("Pepa", "65763");
        Socio socio3 = new Socio("Churro", "12345");
        Socio socio4 = new Socio("Juan", "54321");

        Libro libro1 = new Libro("Harry Potter", "J.K. Rowling", "123456789", 3);
        Libro libro2 = new Libro("El Señor de los Anillos", "J.R.R. Tolkien", "987654321", 2);
        Libro libro3 = new Libro("Cien Años de Soledad", "Gabriel García Márquez", "111111111", 1);
        Libro libro4 = new Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "222222222", 4);

        libro1.mostrarInformacion();
        libro1.mostrarPrestamos();
        solicitarPrestamo(libro1, socio);
        solicitarPrestamo(libro1, socio2);
        solicitarPrestamo(libro1, socio3);
        solicitarPrestamo(libro1, socio4);

        libro1.mostrarInformacion();
        libro1.mostrarPrestamos();

        socio.mostrarPrestamos();

        solicitarPrestamo(libro2, socio);
        solicitarPrestamo(libro3, socio);
        solicitarPrestamo(libro4, socio);
        socio.mostrarPrestamos();

    }

    // Prestamos duran 31 dias
    public static Prestamo solicitarPrestamo(Libro libro, Socio socio) {
        if (socio.getPrestamos().size() >= 3) {
            System.out.println("El socio " + socio.getNombre() + " ya tiene el máximo de 3 préstamos activos.");
            return null;
        }

        if (libro.getStock() > 0) {
            LocalDate hoy = LocalDate.now();
            LocalDate dentroDe31Dias = hoy.plusDays(31);
            Prestamo nuevoPrestamo = new Prestamo(hoy, dentroDe31Dias, libro, socio);
            socio.agregarPrestamo(nuevoPrestamo);
            libro.agregarPrestamo(nuevoPrestamo);
            System.out.println("Préstamo solicitado exitosamente para " + socio.getNombre() +
             " del libro " + libro.getTitulo() + ".");
            return nuevoPrestamo;
        } else {
            System.out.println("No hay copias disponibles del libro " + libro.getTitulo() + " para prestar.");
            return null;
        }
    }
}
