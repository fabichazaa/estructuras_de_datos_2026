public static void main (String[] args){
    Vehiculo autoFabi = new Auto("123ABC", "pink", "Dolphyn", true);
    Vehiculo autoEli = new Auto("637SDF", "black", "Dolphyn", true);
    EspacioEstacionamiento espacio1 = new EspacioEstacionamiento();
    EspacioEstacionamiento espacio2 = new EspacioEstacionamiento(autoFabi);

    System.out.println(espacio1.toString());
    System.out.println(espacio2.toString());

    espacio1.ocuparEspacio(autoEli);

    System.out.println(espacio1.toString());

    espacio1.liberarEspacio();

    System.out.println(espacio1.toString());



}