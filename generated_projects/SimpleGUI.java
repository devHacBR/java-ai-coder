import javax.swing.*;

public class SimpleGUI {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Simple GUI");
        JButton button = new JButton("Click Me!");
        
        button.setBounds(100, 100, 120, 40);
        frame.add(button);
        JTextField textField = new JTextField();
        textField.setBounds(100, 160, 120, 30);
        frame.add(textField);
        
        frame.setSize(300, 300);
        frame.setLayout(null);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}