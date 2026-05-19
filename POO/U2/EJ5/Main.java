
import java.time.LocalDate;
import java.time.ZoneId;
import java.util.Date;

public class Main {
    public static void main (String[] args) {
        Tarea tarea1 = new Tarea("Matematica", "Resolver ejercicios del 1 al 10", Date.from(LocalDate.of(2026, 6, 30).atStartOfDay(ZoneId.systemDefault()).toInstant()));
        Tarea tarea2 = new Tarea("Programacion", "Desarrollar un programa en Java", Date.from(LocalDate.of(2026, 6, 30).atStartOfDay(ZoneId.systemDefault()).toInstant()));


        tarea1.mostrarResumen();
        System.out.println("------------------------------");
        tarea2.mostrarResumen();
        System.out.println("------------------------------");


        tarea1.cambiarEstado();
        tarea1.mostrarResumen();
        System.out.println("------------------------------");
    }
}