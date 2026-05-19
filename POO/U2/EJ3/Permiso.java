import java.util.Random;

public class Permiso {
    Random rand = new Random();
    private final int idPermiso;
    private Puerta puerta;

    public Permiso(Puerta puerta)
    {
        this.puerta = puerta;
        this.idPermiso = rand.nextInt(10000);
    }

    public int getIdPermiso() {
        return this.idPermiso;
    }

    public Puerta getPuerta() {
        return this.puerta;
    }

    public void setIdPuertaPermitida(Puerta puerta) {
        this.puerta = puerta;
    }

    @Override
    public String toString() {
        return "Acceso habilitado: " + this.puerta.getZonaAsignada();
    }
}
