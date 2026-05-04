
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Publicacion {
    private String descripcion;
    private LocalDateTime fechaPublicacion;

    public Publicacion(String descripcion){
        this.descripcion = descripcion;
        this.fechaPublicacion = LocalDateTime.now();
    }

    public String getDescripcion() {
        return descripcion;
    }

    public LocalDateTime getFechaPublicacion() {
        return fechaPublicacion;
    }

    @Override
    public String toString() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        return "Publicación: " + descripcion + " - Fecha: " + fechaPublicacion.format(formatter);
    }
}