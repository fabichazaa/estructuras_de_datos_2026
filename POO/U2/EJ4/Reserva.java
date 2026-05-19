public class Reserva {
    private final int idReserva;
    private String nombrePasajero;
    private String dniPasajero;
    private int idVuelo;
    
    public Reserva(String nombrePasajero, String dniPasajero) {
        this.nombrePasajero = nombrePasajero;
        this.dniPasajero = dniPasajero;
    }
}