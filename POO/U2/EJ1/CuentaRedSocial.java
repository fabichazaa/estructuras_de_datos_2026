import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

public class CuentaRedSocial {
    private final String nombreDeUsuario;
    private final String correo;
    private final LocalDateTime fechaDeCreacion;
    // Entre CuentaRedSocial y seguidores/seguidos hay una asociacion
    private final List<CuentaRedSocial> seguidores = new ArrayList<>();
    
    /* Entre CuentaRedSocial y Publicacion hay una composicion.
    - La publicacion es la parte, cuentaRedSocial es el todo. 
    - Hay una pertenencia entre estos dos, ya que una publicacion pertenece a una unica instancia de CuenaRedSocial
    - Si la cuenta de la red social se elimina, van a desaparecer todas las publicaciones
    */
    private final List<Publicacion> publicaciones = new ArrayList<>();

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

    public void agregarPublicacion(String descripcion){
        Publicacion p = new Publicacion(descripcion);
        this.publicaciones.add(p);
    }

    public LocalDateTime calcularAntiguedad(){
        return LocalDateTime.now().minusYears(this.fechaDeCreacion.getYear())
                .minusMonths(this.fechaDeCreacion.getMonthValue())
                .minusDays(this.fechaDeCreacion.getDayOfMonth());
    }

    @Override
    public String toString() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");

        return "Nombre de usuario: " + nombreDeUsuario +
                "\nCorreo: " + correo +
                "\nFecha de creacion: " + fechaDeCreacion.format(formatter) +
                "\nSeguidores: " + seguidores.size() +
                "\nPublicaciones: " + publicaciones.size();
    }
}