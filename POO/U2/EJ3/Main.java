public class Main {
    public static void main (String[] args) {
        Empleado empleado1 = new Empleado("Pepa", "Desarrollador Jr");
        Empleado empleado2 = new Empleado("Chipa", "Team Lead");

        Puerta puerta1 = new Puerta("Cafeteria");
        Puerta puerta2 = new Puerta("Sala Conferencia");
        Puerta puerta3 = new Puerta("Laboratorio");

        Permiso permiso1 = new Permiso(puerta1);
        Permiso permiso2 = new Permiso(puerta2);
        Permiso permiso3 = new Permiso(puerta3);


        agregarPermiso(empleado1, permiso1);
        agregarPermiso(empleado1, permiso2);
        agregarPermiso(empleado1, permiso3);
        System.out.println("** Accesos " + empleado1.getNombre() + " **");
        empleado1.listarPermisos();
        System.out.println("------------------------------");


        agregarPermiso(empleado2, permiso1);
        System.out.println("** Accesos " + empleado2.getNombre() + " **");
        empleado2.listarPermisos();
        System.out.println("------------------------------");

        abrirPuerta(empleado1, puerta1);
        abrirPuerta(empleado2, puerta3);

    }

    public static void agregarPermiso(Empleado empleado, Permiso permiso) {
        empleado.agregarPermiso(permiso);
    }

    public static void quitarPermiso(Empleado empleado, Permiso permiso) {
        empleado.removerPermiso(permiso);
    }

    public static void abrirPuerta(Empleado empleado, Puerta puerta){
        boolean resultado = empleado.abrirPuerta(puerta);
        if (resultado) {
            System.out.println("Puerta '" + puerta.getZonaAsignada() + "' abierta por " + 
            empleado.getNombre() + ".");
        } else {
            System.out.println(empleado.getNombre() + " no tiene acceso a '" 
            + puerta.getZonaAsignada() + "'.");
        }
    }
}
