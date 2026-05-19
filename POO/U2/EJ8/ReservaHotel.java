
import java.util.Date;

public class ReservaHotel {
    private final int numeroReserva;
    private String nombreHuesped;
    private Date fechaIngreso;
    private Date fechaEgreso;
    private int numeroHabitacion;
    private EstadoReserva estado;

    public ReservaHotel(String nombreHuesped, Date fechaIngreso, Date fechaEgreso, int numeroHabitacion) {
        this.numeroReserva = (int) (Math.random() * 10000);
        this.nombreHuesped = nombreHuesped;
        this.fechaIngreso = fechaIngreso;
        this.fechaEgreso = fechaEgreso;
        this.numeroHabitacion = numeroHabitacion;
        this.estado = EstadoReserva.PENDIENTE;
    }

    public int getNumeroReserva() {
        return numeroReserva;
    }

    public Date getFechaIngreso() {
        return fechaIngreso;
    }

    public Date getFechaEgreso() {
        return fechaEgreso;
    }

    public int getNumeroHabitacion() {
        return numeroHabitacion;
    }

    public EstadoReserva getEstado() {
        return estado;
    }

    public void setNombreHuesped(String nombreHuesped) {
        this.nombreHuesped = nombreHuesped;
    }

    public void setFechaIngreso(Date fechaIngreso) {
        this.fechaIngreso = fechaIngreso;
    }

    public void setFechaEgreso(Date fechaEgreso) {
        this.fechaEgreso = fechaEgreso;
    }

    public void setNumeroHabitacion(int numeroHabitacion) {
        this.numeroHabitacion = numeroHabitacion;
    }

    public void confirmarReserva() {
        if (estado == EstadoReserva.PENDIENTE) {
            estado = EstadoReserva.CONFIRMADA;
            System.out.println("Reserva " + numeroReserva + " confirmada.");
        } else {
            System.out.println("No se puede confirmar la reserva. Estado actual: " + estado);
        }
    }

    public void cancelarReserva() {
        if (estado == EstadoReserva.PENDIENTE || estado == EstadoReserva.CONFIRMADA) {
            estado = EstadoReserva.CANCELADA;
            System.out.println("Reserva " + numeroReserva + " cancelada.");
        } else {
            System.out.println("No se puede cancelar la reserva. Estado actual: " + estado);
        }
    }

    public boolean calcularEstadia() {
        if (estado == EstadoReserva.CONFIRMADA) {
            long diffInMillies = Math.abs(fechaEgreso.getTime() - fechaIngreso.getTime());
            long diffInDays = diffInMillies / (24 * 60 * 60 * 1000);
            System.out.println("La estadía es de " + diffInDays + " días.");
            return true;
        } else {
            System.out.println("No se puede calcular la estadía. La reserva no está confirmada.");
            return false;
        }
    }

    public void mostrarDetalles() {
        System.out.println("Número de Reserva: " + numeroReserva);
        System.out.println("Nombre del Huésped: " + nombreHuesped);
        System.out.println("Fecha de Ingreso: " + fechaIngreso);
        System.out.println("Fecha de Egreso: " + fechaEgreso);
        System.out.println("Número de Habitación: " + numeroHabitacion);
        System.out.println("Estado de la Reserva: " + estado);
    }

    @Override
    public String toString() {
        return "ReservaHotel " +
                "numeroReserva=" + numeroReserva +
                ", nombreHuesped='" + nombreHuesped + '\'' +
                ", fechaIngreso=" + fechaIngreso +
                ", fechaEgreso=" + fechaEgreso +
                ", numeroHabitacion=" + numeroHabitacion +
                ", estado=" + estado +
                '}';
    }
}
