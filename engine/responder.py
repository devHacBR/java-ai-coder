# engine/responder.py

def generate_java_code(parsed_data):
    intent = parsed_data["intent"]

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

    elif intent == "simple_gui":
        return simple_gui_code()

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

def simple_gui_code():
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

