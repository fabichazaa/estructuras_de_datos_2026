import java.util.List;
import java.util.Random;
import java.util.UUID;

public class Empleado {
    Random rand = new Random();
    private final int idEmpleado;
    private final String nombre;
    private String rol;
    private final String numeroTarjeta;

    private List<Permiso> permisos;

    public Empleado(String nombre, String rol) {
        this.nombre = nombre;
        this.rol = rol;
        this.idEmpleado = rand.nextInt(10000);
        this.numeroTarjeta = generarUUID();
    }

    private String generarUUID() {
        UUID uuid = UUID.randomUUID();
        return uuid.toString();
    }

    public int getIdEmpleado() {
        return this.idEmpleado;
    }

    public String getNombre() {
        return this.nombre;
    }

    public String getRol() {
        return this.rol;
    }

    public String getNumeroTarjeta() {
        return this.numeroTarjeta;
    }

    public void setRol(String rol) {
        this.rol = rol;
    }

    public void agregarPermiso(Permiso nuevoPermiso) {
        this.permisos.add(nuevoPermiso);
    }

    private Permiso encontrarPermiso(int idPermiso) {
        for (Permiso permiso: permisos) {
            if (permiso.getIdPermiso() == idPermiso) {
                return permiso;
            }
        }
        return null;
    }

    public boolean removerPermiso(int idPermiso) {
        Permiso permisoBuscado = encontrarPermiso(idPermiso);
        if (permisoBuscado != null) {
        }
        return false;
    }
}
