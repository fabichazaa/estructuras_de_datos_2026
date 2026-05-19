import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.UUID;

public class Empleado {
    Random rand = new Random();
    private final int idEmpleado;
    private final String nombre;
    private String rol;
    private final String numeroTarjeta;

    private final List<Permiso> permisos;

    public Empleado(String nombre, String rol) {
        this.nombre = nombre;
        this.rol = rol;
        this.idEmpleado = rand.nextInt(10000);
        this.numeroTarjeta = generarUUID();
        this.permisos = new ArrayList<>();
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

    private Permiso encontrarPermiso(Permiso permisoBuscado) {
        int idPermiso = permisoBuscado.getIdPermiso();
        for (Permiso permiso: this.permisos) {
            if (permiso.getIdPermiso() == idPermiso) {
                return permiso;
            }
        }
        return null;
    }

    private Permiso encontrarPermisoPorPuerta(Puerta permisoPuerta) {
        int idPuerta = permisoPuerta.getIdPuerta();
        for (Permiso permiso: this.permisos) {
            if (permiso.getPuerta().getIdPuerta() == idPuerta) {
                return permiso;
            }
        }
        return null;
    }

    public void agregarPermiso(Permiso nuevoPermiso) {
        this.permisos.add(nuevoPermiso);
    }

    public boolean removerPermiso(Permiso permiso) {
        Permiso permisoBuscado = encontrarPermiso(permiso);
        if (permisoBuscado != null) {
            this.permisos.remove(permisoBuscado);
        }
        return false;
    }

    public boolean abrirPuerta(Puerta puerta) {
        Permiso permiso = encontrarPermisoPorPuerta(puerta);
        if (permiso != null) {
            puerta.abrirPuerta();
            return true;
        }
        return false;
    }

    public void listarPermisos() {
        for (Permiso permiso: this.permisos){
            System.out.println(permiso.toString());
        }
    }

    @Override
    public String toString() {
        return this.nombre + " - " + this.rol;
    }
}
