import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Medico {
    private final String nombre;
    private String especialidad;
    private final String matricula;
    private final List<Turno> turnos;

    public Medico(String nombre, String especialidad, String matricula) {
        this.nombre = nombre;
        this.especialidad = especialidad;
        this.matricula = matricula;
        this.turnos = new ArrayList<>();
    }

    public String getNombre() {
        return nombre;
    }

    public String getEspecialidad() {
        return especialidad;
    }

    public String getMatricula() {
        return matricula;
    }

    public void setEspecialidad(String especialidad) {
        this.especialidad = especialidad;
    }

    boolean agregarTurno(Turno turno) {
        if (turno == null) {
            return false;
        }
        turnos.add(turno);
        return true;
    }

    public boolean cancelarTurno(Turno turno) {
        if (turnos.contains(turno) && "pendiente".equalsIgnoreCase(turno.getEstado())) {
            return turno.actualizarEstado("cancelado");
        }
        return false;
    }

    public void listarTurnosPendientes() {
        System.out.println("Turnos pendientes del médico " + nombre + ":");
        List<Turno> pendientes = turnos.stream()
                .filter(t -> "pendiente".equalsIgnoreCase(t.getEstado()))
                .collect(Collectors.toList());

        if (pendientes.isEmpty()) {
            System.out.println("  No hay turnos pendientes.");
        } else {
            for (Turno turno : pendientes) {
                turno.mostrarInformacionTurno();
            }
        }
    }
}
