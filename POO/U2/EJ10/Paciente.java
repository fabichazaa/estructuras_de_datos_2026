import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

public class Paciente {
    private String nombre;
    private String dni;
    private String obraSocial;
    private final List<Turno> turnos;

    public Paciente(String nombre, String dni, String obraSocial) {
        this.nombre = nombre;
        this.dni = dni;
        this.obraSocial = obraSocial;
        this.turnos = new ArrayList<>();
    }

    public String getNombre() {
        return nombre;
    }

    public String getDNI() {
        return dni;
    }

    public String getObraSocial() {
        return obraSocial;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setDNI(String dni) {
        this.dni = dni;
    }

    public void setObraSocial(String obraSocial) {
        this.obraSocial = obraSocial;
    }

    public boolean solicitarTurno(Medico medico, LocalDateTime fecha) {
        Turno turno = new Turno(fecha, "pendiente", this, medico);
        if (medico.agregarTurno(turno)) {
            turnos.add(turno);
            return true;
        }
        return false;
    }

    public boolean cancelarTurno(Turno turno) {
        if (turnos.contains(turno) && "pendiente".equalsIgnoreCase(turno.getEstado())) {
            boolean cancelado = turno.actualizarEstado("cancelado");
            if (cancelado) {
                return true;
            }
        }
        return false;
    }

    public List<Turno> getTurnos() {
        return turnos;
    }

    public void listarTurnosPaciente() {
        System.out.println("Turnos del paciente " + nombre + ":");
        if (turnos.isEmpty()) {
            System.out.println("  No hay turnos registrados.");
        } else {
            for (Turno turno : turnos) {
                turno.mostrarInformacionTurno();
            }
        }
    }
}
