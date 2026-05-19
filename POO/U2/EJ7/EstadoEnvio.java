public enum EstadoEnvio {
    PREPARANDO("En preparación"),
    ENVIANDO("Enviando"),
    ENVIADO("Enviado");

    private final String descripcion;

    EstadoEnvio(String descripcion) {
        this.descripcion = descripcion;
    }

    public String getDescripcion() {
        return descripcion;
    }

    @Override
    public String toString() {
        return descripcion;
    }
}