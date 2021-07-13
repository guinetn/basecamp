# GEMS

Linq: Enumerable.Range(1, 5).Select(i => {})

Windows:
    setx AZURE_STORAGE_CONNECTION_STRING "<yourconnectionstring>"
    After adding the environment variable you must start a new instance of the command window.
    string connectionString = Environment.GetEnvironmentVariable("AZURE_STORAGE_CONNECTION_STRING");

string fileName = "quickstart" + Guid.NewGuid().ToString() + ".txt";
string localFilePath = Path.Combine(localPath, fileName);

https://www.infoworld.com/article/3573782/how-to-benchmark-c-code-using-benchmarkdotnet.html