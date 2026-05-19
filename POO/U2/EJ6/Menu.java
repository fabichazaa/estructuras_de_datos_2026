
import java.util.ArrayList;
import java.util.List;

public class Menu {
    private String nombreRestaurante;
    private final List<Plato> platos;

    public Menu(String nombreRestaurante) {
        this.nombreRestaurante = nombreRestaurante;
        this.platos = new ArrayList<>();
    }

    public String getNombreRestaurante() {
        return nombreRestaurante;
    }

    public void setNombreRestaurante(String nombreRestaurante) {
        this.nombreRestaurante = nombreRestaurante;
    }

    public void agregarPlato(String nombre, String descripcion, double precio, boolean esVegano) {
        Plato plato = new Plato(nombre, descripcion, precio, esVegano);
        platos.add(plato);
    }

    public boolean removerPlato(int codigo) {
        return platos.removeIf(plato -> plato.getCodigo() == codigo);
    }

    public boolean removerPlatoPorNombre(String nombre) {
        return platos.removeIf(plato -> plato.getNombre().equalsIgnoreCase(nombre));
    }
    
    public void mostrarMenu() {
        System.out.println("~~~ Menú del restaurante " + nombreRestaurante + " ~~~");
        for (Plato plato : platos) {
            System.out.println(plato);
        }
    }
}
