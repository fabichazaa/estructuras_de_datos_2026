import java.util.UUID;

public class EspacioEstacionamiento {
    private final String numeroUnico;
    private boolean estado;
    private Vehiculo vehiculo;

    
    public EspacioEstacionamiento(){
        this.numeroUnico = generarNumeroUnico();
        this.estado = true;
    } 

    public EspacioEstacionamiento(Vehiculo vehiculo){
        this.vehiculo = vehiculo;
        this.numeroUnico = generarNumeroUnico();
        this.estado = false;
    }

    private String generarNumeroUnico() {
        UUID uuid = UUID.randomUUID();
        return uuid.toString();
    }

    public String getNumeroUnico() {
        return this.numeroUnico;
    }

    public boolean getEstado() {
        return this.estado;
    }

    public Vehiculo getVehiculo() { 
        return this.vehiculo;
    }
    
    public String estaDisponible() {
        return this.estado ? "Si" : "No";
    }

    public boolean ocuparEspacio(Vehiculo vehiculoIngresado) {
        if (!this.estado) {
            System.out.println("El espacio de estacionamiento ya esta ocupado! Numero unico:" 
            + this.numeroUnico);
            return false;
        }

        this.vehiculo = vehiculoIngresado;
        this.estado = false;
        return true;
    }

    public void liberarEspacio() {
        this.vehiculo = null;
        this.estado = true;
    }

    @Override
    public String toString() {
        return "-- Espacio Estacionamiento --\nNumero Unico: " + this.numeroUnico + 
        "\nEstado: " + (this.estado ? "Disponible" : "Ocupado")
        + "\nVehiculo: " + (this.vehiculo == null ? "-" : this.vehiculo.toString()) + "\n";
    }
}