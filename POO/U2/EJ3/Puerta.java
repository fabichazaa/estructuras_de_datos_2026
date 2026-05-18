import java.util.Random;

public class Puerta {
    Random rand = new Random();
    private final int idPuerta;
    private boolean estado;
    private final String zonaAsignada;

    public Puerta(String zonaAignada) {
        this.estado = false;
        this.zonaAsignada = zonaAignada;
        this.idPuerta = rand.nextInt(10000);
    }

    public int getIdPuerta() {
        return this.idPuerta;
    }

    public boolean getEstado() {
        return this.estado;
    }

    public String getZonaAsignada() {
        return this.zonaAsignada;
    }
}