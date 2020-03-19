package jni.test;

class Calculator {
    public Calculator() {
        initialize();
    }

    private long peer;

    public native long add(long a, long b);

    public native long subtract(long a, long b);

    protected native void initialize();

    protected native void finalize() throws Throwable;
}

public class NativePeer {
    public static void main(String[] args) {
        try {
            System.loadLibrary("test_package");
        } catch(Exception e) {
            System.out.println(e.getMessage());
        }

        Calculator calculator = new Calculator();
        System.out.println("2 + 2 = " + calculator.add(2, 2));
        System.out.println("8 - 4 = " + calculator.subtract(8, 4));
    }
}