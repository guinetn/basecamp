# IReadOnlyCollections

- IReadOnlyList
- IReadOnlyDictionary
- IReadOnlyCollection

```cs
public static async Task<List<Student>> GetStudentListAsync()
{
    // Send Dummy Data from here.
    return await Task.FromResult<List<Student>>(
        new List<Student>
        {
            new Student { Id=1,Name="Tom",Standard=9 },
            new Student { Id=2,Name="Mac",Standard=9 },
            new Student { Id=3,Name="Harry",Standard=9 },
        }
    );
}
Add() is available in the returned object

To prevent from adding an item to the list: Add() is not available

public static async Task<IReadOnlyList<Student>> GetReadOnlyStudentsAsync()
{
    // Send Dummy Data from here.
    return await Task.FromResult<List<Student>>(
        new List<Student>
        {
            new Student { Id=1,Name="Tom",Standard=9 },
            new Student { Id=2,Name="Mac",Standard=9 },
            new Student { Id=3,Name="Harry",Standard=9 },
        }
    );
}
Add() is not available in the returned object
list[0].Id=2 → IReadOnlyList<T> doesnt stop from modifying the items within the list 
anyone can cast IReadOnlyList<T> back to List<T> so DON'T depend too much on it (or xxx.AsReadOnly() )
The same way you can use other IReadonlycollections:
- IReadOnlyList
- IReadOnlyDictionary
- IReadOnlyCollection

```