// import javax.swing.*;
// import java.awt.Color;
// import java.awt.FlowLayout;

// public class Main{

//     public static void main(String[] args) {
//          // 1. Crear la ventana principal
//        JFrame ventana = new JFrame("Mi Calculadora");
        
//         ventana.setSize(400, 300);
//         ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//         ventana.setLocationRelativeTo(null);   // centrar en pantalla

//         String[] operations = ["Addition", "Substraction", "Division", "Multiplication"];
//         JComboBox<String> dropdownOperationsField = new JComboBox<>(options);
//         // 2. Crear un panel con FlowLayout
//         JPanel panel = new JPanel(new FlowLayout());

//         // 3. Crear componentes
//         JLabel  inputLabel = new JLabel("Input parameters:");
//         JLabel  number1Label = new JLabel("Number 1:");
//         JLabel  number2Label = new JLabel("Number 2:");
//         JLabel  operationLabel = new JLabel("Operation:");
//         JTextField number1Field = new JTextField(15);
//         JTextField number2field = new JTextField(15);
      
//         JButton  resolveButton   = new JButton("Resolve");
//         resolveButton.setBackground(Color.GREEN);
//         JButton  cleanButton   = new JButton("Clean");
//         cleanButton.setBackground(Color.GREY);
//         JLabel  resultLabel = new JLabel("Result:");
//         JLabel  resultValueLabel = new JLabel("");

      

//         // 4. Asociar evento al botón
//         boton.addActionListener(e -> {
//             String nombre = campo.getText();
//             resultado.setText("Hello myster, " + nombre + "!");
//         });

//         boton2.addActionListener( e -> {
//           resultado.setText("");
//           campo.setText("");
//         });
//         // 5. Agregar componentes al panel
//         panel.add(inputLabel);
//         panel.add(number1Label);
//         panel.add(number2Label);
//         panel.add(operationLabel);
//         panel.add(number1Field);
//         panel.add(number2Field);
//         panel.add(dropdownOperationsField);
//         panel.add(resolveButton);
//         panel.add(cleanButton);
//         panel.add(resultLabel);
//         panel.add(resultValueLabel);

//         // 6. Agregar panel a la ventana y mostrar
//         ventana.add(panel);
//         ventana.setVisible(true);
//     }
// }
