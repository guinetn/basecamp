## Covariance / Contravariance

Implicit reference conversion for array types, delegate types, generic type arguments
Covariance preserves assignment compatibility and contravariance reverses it.
 
### Covariance 
method can have more derived return type 

Covariance for arrays enables implicit conversion of an array of a more derived type to an array of a less derived type. But this operation is not type safe:
```cs
object[] array = new String[10];  
array[0] = 10; // run-time exception: implicit conversionnot type safe operation  
```

```cs
IEnumerable<string> strings = new List<string>();  
// An object that is instantiated with a more derived type argument
// is assigned to an object instantiated with a less derived type argument.
// Assignment compatibility is preserved.
IEnumerable<object> objects = strings;  
```

```cs
class Cells {}  
class Human : Cells {}  
  
class Program  
{  
    // Define the delegate.  
    public delegate Cells HandlerMethod();  
  
    public static Cells CellsHandler()  
    {  
        return null;  
    }  
  
    public static Human HumanHandler()  
    {  
        return null;  
    }  
  
    static void Test()  
    {  
        HandlerMethod handlerCells = CellsHandler;  
  
        // Covariance enables this assignment.  
        HandlerMethod handlerHuman = HumanHandler;  
    }  
}  
```
### Contravariance
method can have less derived parameter types  

```cs
// Event handler that accepts a parameter of the EventArgs type.  
private void MultiHandler(object sender, System.EventArgs e)  
{  
    label1.Text = System.DateTime.Now.ToString();  
}  
  
public Form1()  
{  
    InitializeComponent();  
  
    // You can use a method that has an EventArgs parameter,  
    // although the event expects the KeyEventArgs parameter.  
    this.button1.KeyDown += this.MultiHandler;  
  
    // You can use the same method
    // for an event that expects the MouseEventArgs parameter.  
    this.button1.MouseClick += this.MultiHandler;  
  
}  
```
 