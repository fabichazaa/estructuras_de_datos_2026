
import java.time.LocalDate;
import java.time.ZoneId;
import java.util.Date;

public class Main {
    public static void main(String[] args) {

        LocalDate inicio = LocalDate.of(2024, 6, 1);
        LocalDate fin = LocalDate.of(2024, 6, 5);

        Date fechaInicio = Date.from(inicio.atStartOfDay(ZoneId.systemDefault()).toInstant());
        Date fechaFin = Date.from(fin.atStartOfDay(ZoneId.systemDefault()).toInstant());

        ReservaHotel reserva = new ReservaHotel("Chipa", fechaInicio, fechaFin, 101);
        reserva.mostrarDetalles();
        System.out.println("------------------------------");
        reserva.confirmarReserva();
        reserva.mostrarDetalles();
        System.out.println("------------------------------");
        reserva.calcularEstadia();
    }
}
