public class Main {
    public static void main(String[] args) {
        Menu menu = new Menu("Cafe Cuties");
        menu.agregarPlato("Caramel Machiatto", "Café con leche, caramelo y espuma de leche", 150.0, false);
        menu.agregarPlato("Capuccino", "Café con leche y espuma de leche", 120.0, false);
        menu.agregarPlato("Latte", "Café con leche y un toque de espuma de leche", 130.0, false);
        menu.agregarPlato("Té Verde", "Té verde con un toque de limón", 100.0, true);
        menu.mostrarMenu();

        menu.removerPlatoPorNombre("Latte");
        menu.mostrarMenu();
    }
}