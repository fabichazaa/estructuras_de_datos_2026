import java.util.Random;

public class HelloWorld {
    public static void main(String[] args) {
        Random rand = new Random();
        int randomInt = rand.nextInt(100); // Generates 0 to 99

        if (randomInt < 40) {
            System.out.println("Beep boop hello hello");
        } else if (randomInt < 70) {
            System.out.println("This is Fabs speaking boops");
        } else {
            System.out.println("Lucky message!!");
        }
        
        String userName = "Fabs";
        System.out.println(userName);

        Cancion shakeItOff = new Cancion("Shake It Off", "Taylor Swift", "3:45");
        shakeItOff.obtenerInformacion();
        System.out.println("----------------------");
        shakeItOff.definirGenero("POP");
        shakeItOff.obtenerInformacion();
    }
}