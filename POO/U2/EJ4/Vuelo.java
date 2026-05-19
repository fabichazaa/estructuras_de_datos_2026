import java.util.ArrayList;
import java.util.List;

public class Vuelo {
    private final int numeroVuelo;
    private String ciudadOrigen;
    private String ciudadDestino;
    private int cantidadMaximaPasajeros;
    private final List<Reserva> reservas;

    public Vuelo(String ciudadOrigen, String ciudadDestino, int cantidadMaximaPasajeros) {
        this.ciudadOrigen = ciudadOrigen;
        this.ciudadDestino = ciudadDestino;
        this.cantidadMaximaPasajeros = cantidadMaximaPasajeros;
        this.reservas = new ArrayList<>();
        this.numeroVuelo = (int) (Math.random() * 10000);
    }

    public int getNumeroVuelo() {
        return numeroVuelo;
    }

    public String getCiudadOrigen() {
        return ciudadOrigen;
    }

    public String getCiudadDestino() {
        return ciudadDestino;
    }

    public int getCantidadMaximaPasajeros() {
        return cantidadMaximaPasajeros;
    }

    public void setCiudadOrigen(String ciudadOrigen) {
        this.ciudadOrigen = ciudadOrigen;
    }

    public void setCiudadDestino(String ciudadDestino) {
        this.ciudadDestino = ciudadDestino;
    }

    public void setCantidadMaximaPasajeros(int cantidadMaximaPasajeros) {
        this.cantidadMaximaPasajeros = cantidadMaximaPasajeros;
    }

    public void agergarReserva(Reserva reserva) {
        if (reservas.size() < cantidadMaximaPasajeros) {
            reservas.add(reserva);
        } else {
            System.out.println("No se pueden agregar más reservas, el vuelo está lleno.");
        }
    }

    public void removerReserva(Reserva reserva) {
        reservas.remove(reserva);
    }

    public int cantidadReservas() {
        return reservas.size();
    }

    public List<Reserva> getReservas() {
        return reservas;
    }

    public void mostrarReservas() {
        System.out.println("--- Reservas para el vuelo " + numeroVuelo + " ---");
        for (Reserva reserva : reservas) {
            System.out.println(reserva.toString());
        }
    }

    @Override
    public String toString() {
        return "Vuelo " + numeroVuelo + ": " + ciudadOrigen + " -> " + ciudadDestino +
                " (capacidad " + cantidadMaximaPasajeros + ", reservas " + reservas.size() + ")";
    }
}