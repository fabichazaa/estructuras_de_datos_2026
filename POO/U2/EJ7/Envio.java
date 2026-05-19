public class Envio {
    private final int numeroSeguimiento;
    private String direccionOrigen;
    private String direccionDestino;
    private double peso;
    private EstadoEnvio estado;

    public Envio( String direccionDestino, String direccionOrigen, double peso) {
        this.numeroSeguimiento = (int) (Math.random() * 10000);
        this.direccionOrigen = direccionOrigen;
        this.direccionDestino = direccionDestino;
        this.peso = peso;
        this.estado = EstadoEnvio.PREPARANDO;  // Estado inicial
    }

    public int getNumeroSeguimiento() {
        return this.numeroSeguimiento;
    }

    public String getDireccionOrigen() {
        return this.direccionOrigen;
    }

    public String getDireccionDestino() {
        return this.direccionDestino;
    }

    public double getPeso() {
        return this.peso;
    }

    public EstadoEnvio getEstado() {
        return this.estado;
    }

    public void setDireccionOrigen(String direccionOrigen) {
        this.direccionOrigen = direccionOrigen;
    }

    public void setDireccionDestino(String direccionDestino) {
        this.direccionDestino = direccionDestino;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public void enviarEnvio() {
        if (this.estado == EstadoEnvio.PREPARANDO) {
            this.estado = EstadoEnvio.ENVIANDO;
            System.out.println("El envío con número de seguimiento " + this.numeroSeguimiento + "ha sido enviado.");
        } else {
            System.out.println("El envío no se puede enviar. Estado actual: " + this.estado.toString());
        }
    }

    public void marcarComoEntregado() {
        if (this.estado == EstadoEnvio.ENVIANDO) {
            this.estado = EstadoEnvio.ENVIADO;
            System.out.println("El envío con número de seguimiento " + this.numeroSeguimiento + " ha sido entregado.");
        } else {
            System.out.println("El envío no se puede marcar como entregado. Estado actual: " + this.estado.toString());
        }
    }

    public void mostrarInformacion() {
        System.out.println("Número de Seguimiento: " + this.numeroSeguimiento);
        System.out.println("Dirección de Origen: " + this.direccionOrigen);
        System.out.println("Dirección de Destino: " + this.direccionDestino);
        System.out.println("Peso: " + this.peso + " kg");
        System.out.println("Estado: " + this.estado.toString());
    }

}

