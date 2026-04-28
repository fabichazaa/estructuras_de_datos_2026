public class Cancion {
    private String nombre;
    private String autor;
    private String duracion;
    private String genero;

    public Cancion(String nombre, String autor, String duracion){
        this.nombre = nombre;
        this.autor = autor;
        this.duracion = duracion;
    }
    
    public void obtenerInformacion(){
        System.out.println("Cancion: " + this.nombre + 
        "\nAutor: " + this.autor + 
        "\nDuracion: " + this.duracion +
        "\nGenero: " + this.genero);
    }
    
    public void definirGenero(String genero){
        this.genero = genero;
    }

}