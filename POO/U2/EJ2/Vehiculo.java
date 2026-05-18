public abstract class Vehiculo {
    private final String patente;
    private final String color;
    private final String modelo;

    public Vehiculo(String patente, String color, String modelo) {
        this.patente = patente;
        this.color = color;
        this.modelo = modelo;
    }

    public String getPatente() {
        return this.patente;
    }

    public String getColor() {
        return this.color;
    }

    public String getModelo() {
        return this.modelo;
    }
}