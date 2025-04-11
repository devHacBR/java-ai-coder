# engine/responder.py

def generate_java_code(parsed_data, previous_components=None):
    intent = parsed_data["intent"]

    if intent == "simple_gui":
        return simple_gui_code(parsed_data, previous_components or [])

    if intent == "bubble_sort":
        return bubble_sort_code()

    elif intent == "quick_sort":
        return quick_sort_code()

    elif intent == "file_reading":
        return file_reading_code()

    elif intent == "threading":
        return threading_code()
    
    elif intent == "inheritance":
        return class_inheritance_code()
    
    elif intent == "add_gui_component":
        return add_gui_component_code(parsed_data, previous_components or [])

    else:
        return (
            "// Sorry, I don’t know how to generate code for that yet.",
            "I couldn’t find enough information to generate Java code.",
            []
        )


def bubble_sort_code():
    code = '''\
public class BubbleSort {
    public static void main(String[] args) {
        int[] arr = {5, 2, 8, 3, 1};
        bubbleSort(arr);
        System.out.println("Sorted array:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }

    static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < n-i-1; j++) {
                if (arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }
}'''

    explanation = (
        "This Java program demonstrates **Bubble Sort**:\n"
        "- It defines an array `arr` with some integers.\n"
        "- The `bubbleSort` method compares each pair of elements and swaps them if needed.\n"
        "- After sorting, it prints the sorted array.\n"
        "- Bubble sort has O(n²) time complexity."
    )

    files = [
        {
            "path": "BubbleSort.java",
            "content": code
        }
    ]

    return code, explanation, files


def quick_sort_code():
    code = '''\
public class QuickSort {
    public static void main(String[] args) {
        int[] arr = {10, 7, 8, 9, 1, 5};
        quickSort(arr, 0, arr.length - 1);
        System.out.println("Sorted array:");
        for (int num : arr)
            System.out.print(num + " ");
    }

    static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = (low - 1);
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[i+1];
        arr[i+1] = arr[high];
        arr[high] = temp;

        return i + 1;
    }
}'''
    explanation = (
        "This Java program demonstrates **Quick Sort**, a divide-and-conquer sorting algorithm:\n"
        "- The array is partitioned around a pivot.\n"
        "- Subarrays are sorted recursively.\n"
        "- It’s faster than Bubble Sort with average time complexity O(n log n)."
    )
    files = [{"path": "QuickSort.java", "content": code}]
    return code, explanation, files



def file_reading_code():
    code = '''\
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class FileReaderExample {
    public static void main(String[] args) {
        String path = "sample.txt";
        try (BufferedReader reader = new BufferedReader(new FileReader(path))) {
            String line;
            while ((line = reader.readLine()) != null)
                System.out.println(line);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}'''
    explanation = (
        "This Java program reads a text file line-by-line using `BufferedReader`:\n"
        "- It tries to open and read `sample.txt`.\n"
        "- Each line is printed to the console.\n"
        "- Exceptions are caught with a try-catch block."
    )
    files = [{"path": "FileReaderExample.java", "content": code}]
    return code, explanation, files


def threading_code():
    code = '''\
class MyThread extends Thread {
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println("Thread running: " + i);
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
    }

    public static void main(String[] args) {
        MyThread t1 = new MyThread();
        t1.start();
    }
}'''
    explanation = (
        "This Java program demonstrates **threading**:\n"
        "- `MyThread` extends the `Thread` class.\n"
        "- `run()` method prints numbers with delay.\n"
        "- The thread starts with `.start()`."
    )
    files = [{"path": "MyThread.java", "content": code}]
    return code, explanation, files

def class_inheritance_code():
    code = '''\
class Animal {
    void speak() {
        System.out.println("Animal speaks");
    }
}

class Dog extends Animal {
    void speak() {
        System.out.println("Dog barks");
    }
}

public class InheritanceExample {
    public static void main(String[] args) {
        Animal a = new Dog();
        a.speak();
    }
}'''
    explanation = (
        "This Java program demonstrates **inheritance**:\n"
        "- `Dog` class inherits from `Animal`.\n"
        "- Method `speak()` is overridden in `Dog`.\n"
        "- Output shows polymorphism at work."
    )
    files = [{"path": "InheritanceExample.java", "content": code}]
    return code, explanation, files

def simple_gui_code(parsed_data=None, previous_components=None):
    code = '''\
import javax.swing.*;

public class SimpleGUI {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Simple GUI");
        JButton button = new JButton("Click Me!");
        
        button.setBounds(100, 100, 120, 40);
        frame.add(button);
        
        frame.setSize(300, 300);
        frame.setLayout(null);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}'''
    explanation = (
        "This Java program shows a **basic GUI using Swing**:\n"
        "- A window is created with a button.\n"
        "- The button is added using absolute positioning.\n"
        "- Clicking doesn't trigger action yet — just the layout."
    )
    files = [{"path": "SimpleGUI.java", "content": code}]
    return code, explanation, files

"""
def simple_gui_code(parsed_data=None, previous_components=None):
    if previous_components is None:
        previous_components = ["button"]  # Default base GUI has a button

    frame_code = '''\
    import javax.swing.*;

    public class SimpleGUI {
        public static void main(String[] args) {
        JFrame frame = new JFrame("Simple GUI");
    '''

    components_code = []
    y = 60
    for i, component in enumerate(previous_components):
        name = component + str(i + 1)

        if component == "button":
            components_code.append(f'        JButton {name} = new JButton("Click Me!");')
            components_code.append(f'        {name}.setBounds(100, {y}, 120, 30);')
            components_code.append(f'        frame.add({name});')

        elif component == "text_field":
            components_code.append(f'        JTextField {name} = new JTextField();')
            components_code.append(f'        {name}.setBounds(100, {y}, 120, 30);')
            components_code.append(f'        frame.add({name});')

        elif component == "label":
            components_code.append(f'        JLabel {name} = new JLabel("Label");')
            components_code.append(f'        {name}.setBounds(100, {y}, 120, 30);')
            components_code.append(f'        frame.add({name});')

        elif component == "checkbox":
            components_code.append(f'        JCheckBox {name} = new JCheckBox("Accept");')
            components_code.append(f'        {name}.setBounds(100, {y}, 120, 30);')
            components_code.append(f'        frame.add({name});')

        y += 40  # Increase vertical spacing

    footer_code = '''\
        frame.setSize(300, 300);
        frame.setLayout(null);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        }
    } '''

    full_code = frame_code + "\n" + "\n".join(components_code) + "\n" + footer_code

    explanation = (
        "This Java program creates a GUI using Swing with the following components:\n"
        f"- {', '.join(previous_components)}\n"
        "- Each element is positioned absolutely.\n"
        "- No event listeners are added yet."
    )

    files = [{"path": "SimpleGUI.java", "content": full_code}]
    return full_code, explanation, files
"""

def add_gui_component_code(parsed_data, previous_components):
    component = parsed_data.get("component", "").lower()
    
    base_code, explanation, files = simple_gui_code()
    updated_code = base_code
    added_component_code = ""
    extra_explanation = ""

    if component == "text_field":
        added_component_code = (
            'JTextField textField = new JTextField();\n'
            'textField.setBounds(100, 160, 120, 30);\n'
            'frame.add(textField);\n'
        )
        extra_explanation = "- Added a `JTextField` below the button."

    elif component == "label":
        added_component_code = (
            'JLabel label = new JLabel("Hello!");\n'
            'label.setBounds(100, 200, 100, 30);\n'
            'frame.add(label);\n'
        )
        extra_explanation = "- Added a `JLabel` to display static text."

    elif component == "checkbox":
        added_component_code = (
            'JCheckBox checkBox = new JCheckBox("Accept");\n'
            'checkBox.setBounds(100, 240, 120, 30);\n'
            'frame.add(checkBox);\n'
        )
        extra_explanation = "- Added a `JCheckBox` to the GUI."

    elif component == "textfield_button":
        added_component_code = (
            'JTextField input = new JTextField();\n'
            'input.setBounds(100, 160, 120, 30);\n'
            'frame.add(input);\n\n'
            'JButton submit = new JButton("Submit");\n'
            'submit.setBounds(100, 200, 120, 30);\n'
            'frame.add(submit);\n'
        )
        extra_explanation = "- Added a `JTextField` and `Submit` button."

    else:
        return (
            "// Component not supported yet.",
            "Sorry, I can only add a button, label, checkbox, or text field at the moment.",
            []
        )

    # Insert component lines after `frame.add(button);`
    insert_after = "frame.add(button);"
    updated_code = updated_code.replace(
        insert_after,
        insert_after + "\n        " + added_component_code.strip().replace('\n', '\n        ')
    )

    updated_explanation = explanation + "\n" + extra_explanation

    files = [{"path": "SimpleGUI.java", "content": updated_code}]
    return updated_code, updated_explanation, files

"""
def add_gui_component_code(parsed_data, previous_components):
    component = parsed_data.get("component", "").lower()

    # Start with previous components and append new one if valid
    updated_components = previous_components.copy()

    if component in ["text_field", "label", "checkbox", "textfield_button", "button"]:
        updated_components.append(component)
    else:
        return (
            "// Component not supported yet.",
            "Sorry, I can only add a button, label, checkbox, or text field at the moment.",
            []
        )

    # Generate updated GUI code with all components
    return simple_gui_code(previous_components=updated_components)
"""