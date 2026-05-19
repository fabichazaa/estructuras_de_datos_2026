public class Reserva {
    private final int idReserva;
    private String nombrePasajero;
    private String dniPasajero;
    private final Vuelo vuelo;
    
    public Reserva(String nombrePasajero, String dniPasajero, Vuelo vuelo) {
        this.nombrePasajero = nombrePasajero;
        this.dniPasajero = dniPasajero;
        this.vuelo = vuelo;
        this.idReserva =  (int) (Math.random() * 10000);
    }

    public int getIdReserva() {
        return idReserva;
    }

    public String getNombrePasajero() {
        return nombrePasajero;
    }

    public String getDniPasajero() {
        return dniPasajero;
    }

    public Vuelo getVuelo() {
        return vuelo;
    }

    @Override
    public String toString() {
        return "Reserva " + idReserva + ": " + nombrePasajero + " (DNI " + dniPasajero + ")";
    }

    public void setNombrePasajero(String nombrePasajero) {
        this.nombrePasajero = nombrePasajero;
    }

    public void setDniPasajero(String dniPasajero) {
        this.dniPasajero = dniPasajero;
    }
}