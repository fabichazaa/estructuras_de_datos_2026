import java.time.LocalDateTime;

public class Main {
    public static void main(String[] args) {
        Paciente paciente = new Paciente("Ana López", "34567890", "OSDE");
        Medico medico = new Medico("Dr. Martín Pérez", "Pediatría", "12345-AB");

        LocalDateTime fechaTurno1 = LocalDateTime.of(2026, 6, 10, 9, 30);
        LocalDateTime fechaTurno2 = LocalDateTime.of(2026, 6, 12, 11, 0);

        System.out.println("Solicitando turnos...");
        paciente.solicitarTurno(medico, fechaTurno1);
        paciente.solicitarTurno(medico, fechaTurno2);

        System.out.println();
        paciente.listarTurnosPaciente();
        System.out.println();
        medico.listarTurnosPendientes();

        System.out.println();
        System.out.println("Cancelando el primer turno...");
        if (!paciente.getTurnos().isEmpty()) {
            Turno turnoACancelar = paciente.getTurnos().get(0);
            paciente.cancelarTurno(turnoACancelar);
        }

        System.out.println();
        paciente.listarTurnosPaciente();
        System.out.println();
        medico.listarTurnosPendientes();
    }
}
