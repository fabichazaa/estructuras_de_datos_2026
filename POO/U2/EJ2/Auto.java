public class Auto extends Vehiculo {
    private final boolean cincoPuertas;

    public Auto(String patente, String color, String modelo) {
        super(patente, color, modelo);
        this.cincoPuertas = true;
    }

    public Auto(String patente, String color, String modelo, boolean cincoPuertas) {
        super(patente, color, modelo);
        this.cincoPuertas = cincoPuertas;
    }

    public boolean getCincoPuertas() {
        return this.cincoPuertas;
    }
}