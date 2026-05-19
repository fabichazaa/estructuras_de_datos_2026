
import java.util.Date;

public class Tarea {
    private final int identificadorUnico;
    private String title;
    private String description;
    private Date fechaEntrega;
    private boolean estado;


    public Tarea(String title, String description, Date fechaEntrega) {
        this.title = title;
        this.description = description;
        this.fechaEntrega = fechaEntrega;
        this.estado = false;
        this.identificadorUnico = (int) (Math.random() * 10000);
    }

    public int getIdentificadorUnico() {
        return identificadorUnico;
    }

    public String getTitle() {
        return title;
    }

    public String getDescription() {
        return description;
    }

    public Date getFechaEntrega() {
        return fechaEntrega;
    }

    public boolean isEstado() {
        return estado;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public void setFechaEntrega(Date fechaEntrega) {
        this.fechaEntrega = fechaEntrega;
    }

    public void cambiarEstado() {
        this.estado = !this.estado;
    }   

    public boolean estaVencida() {
        Date hoy = new Date();
        return fechaEntrega.before(hoy);
    }

    public void mostrarResumen() {
        System.out.println(this.toString());
    }

    @Override
    public String toString() {
        return "Tarea " + this.identificadorUnico + ": " + this.title + " - " 
        + this.description + " (Fecha de entrega: " + this.fechaEntrega + ", Estado: " 
        + (this.estado ? "Completada" : "Pendiente") + ")";
    }
}
