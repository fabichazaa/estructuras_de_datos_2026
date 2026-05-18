import java.util.UUID;

public class EspacioEstacionamiento {
    private String numeroUnico;
    private boolean estado;
    private Vehiculo vehiculo;

    
    private EspacioEstacionamiento(){
        this.numeroUnico = generarNumeroUnico();
        this.estado = false;
    } 

    private EspacioEstacionamiento(Vehiculo vehiculo){
        this.vehiculo = vehiculo;
        this.numeroUnico = generarNumeroUnico();
        this.estado = false;
    }

    private String generarNumeroUnico(){
        UUID uuid = UUID.randomUUID();
        return uuid.toString();
    }
}