public class Main {
    public static void main(String[] args) {
        Envio envio = new Envio("Calle Falsa 123", "Calle Verdadera 456", 10.0);
        envio.mostrarInformacion();
        System.out.println("------------------------------");
        envio.enviarEnvio();

        envio.mostrarInformacion();
        System.out.println("------------------------------");

        envio.marcarComoEntregado();

        envio.mostrarInformacion();
        System.out.println("------------------------------");

    }
}