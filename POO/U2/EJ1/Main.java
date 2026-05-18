
public static void main(String[] args) {
    CuentaRedSocial taylorSwift = new CuentaRedSocial("taylorswift13", "taylorswift13@industry.com");

    CuentaRedSocial fan1 = new CuentaRedSocial("fan1", "fan1@gmail.com");
    fan1.seguirCuenta(taylorSwift);
    CuentaRedSocial fan2 = new CuentaRedSocial("fan2", "fan2@gmail.com");
    fan2.seguirCuenta(taylorSwift);
    CuentaRedSocial nightblair = new CuentaRedSocial("nightblair", "fan2@gmail.com");
    nightblair.seguirCuenta(taylorSwift);
    CuentaRedSocial fabichaza = new CuentaRedSocial("fabichaza", "fan2@gmail.com");
    fabichaza.seguirCuenta(taylorSwift);

    System.out.println("** Seguidores de Taylor Swift **");
    taylorSwift.mostrarSeguidores();
    System.out.println("------------------------------");

    taylorSwift.agregarPublicacion("Lanzamiento de nuevo álbum!");
    taylorSwift.agregarPublicacion("Gracias por todo el apoyo!");
    taylorSwift.agregarPublicacion("Amo a mis fans!");

    System.out.println("** Publicaciones de Taylor Swift **");
    taylorSwift.mostrarPublicaciones();
    System.out.println("------------------------------");

    System.out.println("** Información de la cuenta de Taylor Swift **");
    System.out.println(taylorSwift.toString());


}