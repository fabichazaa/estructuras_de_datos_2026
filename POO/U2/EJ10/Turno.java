import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Turno {
    private LocalDateTime fecha;
    private String estado;
    private final Paciente paciente;
    private final Medico medico;

    public Turno(LocalDateTime fecha, String estado, Paciente paciente, Medico medico) {
        this.fecha = fecha;
        this.estado = estado;
        this.paciente = paciente;
        this.medico = medico;
    }

    public LocalDateTime getFecha() {
        return fecha;
    }

    public String getEstado() {
        return estado;
    }

    public void setFecha(LocalDateTime fecha) {
        this.fecha = fecha;
    }

    public boolean actualizarEstado(String nuevoEstado) {
        if (nuevoEstado == null || nuevoEstado.isBlank()) {
            return false;
        }
        this.estado = nuevoEstado;
        return true;
    }

    public void mostrarInformacionTurno() {
        DateTimeFormatter formato = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");
        String fechaTexto = fecha.format(formato);
        System.out.println("  Fecha: " + fechaTexto + ", estado: " + estado);
        System.out.println("    Paciente: " + paciente.getNombre() + " (DNI: " + paciente.getDNI() + ")");
        System.out.println("    Médico: " + medico.getNombre() + " - " + medico.getEspecialidad() + " (Matrícula: " + medico.getMatricula() + ")");
    }
}
