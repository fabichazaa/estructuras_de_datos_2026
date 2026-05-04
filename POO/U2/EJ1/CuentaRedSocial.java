import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

public class CuentaRedSocial {
    private String nombreDeUsuario;
    private String correo;
    private LocalDateTime fechaDeCreacion;
    private List<CuentaRedSocial> seguidores = new ArrayList<>();
    private List<Publicacion> publicaciones = new ArrayList<>();

    public CuentaRedSocial(String nombreDeUsuario, String correo){
        this.nombreDeUsuario = nombreDeUsuario;
        this.correo = correo;
        this.fechaDeCreacion = LocalDateTime.now();
    }

    public String getNombreDeUsuario() {
        return nombreDeUsuario;
    }

    public LocalDateTime getFechaDeCreacion() {
        return fechaDeCreacion;
    }

    public List<CuentaRedSocial> getSeguidores() {
        return seguidores;
    }

    public void mostrarSeguidores() {
        for (CuentaRedSocial seguidor : this.seguidores) {
            System.out.println(seguidor.getNombreDeUsuario());
        }
    }
    
    public List<Publicacion> getPublicaciones() {
        return publicaciones;
    }

    public void mostrarPublicaciones() {
        for (Publicacion publicacion : this.publicaciones) {
            System.out.println(publicacion.toString());
        }
    }

    public void seguirCuenta(CuentaRedSocial cuenta) {
        cuenta.agregarSeguidor(this);
    }

    public void agregarSeguidor(CuentaRedSocial seguidor){
        this.seguidores.add(seguidor);
    }

    public void agregarPublicacion(Publicacion publicacion){
        this.publicaciones.add(publicacion);
    }

    public LocalDateTime calcularAntiguedad(){
        return LocalDateTime.now().minusYears(this.fechaDeCreacion.getYear())
                .minusMonths(this.fechaDeCreacion.getMonthValue())
                .minusDays(this.fechaDeCreacion.getDayOfMonth());
    }

    public Publicacion realizarPublicacion(String descripcion){
        Publicacion nuevaPublicacion =  new Publicacion(descripcion);
        this.agregarPublicacion(nuevaPublicacion);
        return nuevaPublicacion;
    }

    @Override
    public String toString() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");

        return "Nombre de usuario: " + nombreDeUsuario +
                "\nCorreo: " + correo +
                "\nFecha de creacion:" + fechaDeCreacion.format(formatter) +
                "\nSeguidores: " + seguidores.size() +
                "\nPublicaciones: " + publicaciones.size();
    }
}