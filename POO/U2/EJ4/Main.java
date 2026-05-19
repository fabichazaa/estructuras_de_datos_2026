public class Main {
    public static void main(String[] args) {
        Vuelo vuelo1 = new Vuelo("Buenos Aires", "Miami", 2);
        Vuelo vuelo2 = new Vuelo("Buenos Aires", "Paris", 3);
        
        Reserva reserva1 = reservarVuelo(vuelo1, "Pepa", "12345678");
        Reserva reserva2 = reservarVuelo(vuelo1, "Chipa", "53523133");
        Reserva reserva3 = reservarVuelo(vuelo1, "Churro", "5453164");

        vuelo1.mostrarReservas();
        vuelo1.removerReserva(reserva2);
        vuelo1.mostrarReservas();

        Reserva reserva4 = reservarVuelo(vuelo1, "Juan", "7524575");
        vuelo1.mostrarReservas();
        
    }

    public static Reserva reservarVuelo(Vuelo vuelo, String nombre, String dni) {
        if (vuelo.cantidadReservas() < vuelo.getCantidadMaximaPasajeros()){
            Reserva nuevaReserva = new Reserva(nombre, dni, vuelo);
            vuelo.agergarReserva(nuevaReserva);
            System.out.println("Reserva realizada exitosamente para " + nombre + ".");
            return nuevaReserva;
        } else {
            System.out.println("No se pueden agregar más reservas, el vuelo está lleno.");
            return null;
        }
    }
}