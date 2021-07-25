# BackgroundWorker

Winforms user interface will freeze when your application is doing a time consuming operation
Its because your application is running on a single thread. for GUI and methods, events
Lengthy operation will block your user interface till it is done.
Fix: move slow operations into another thread

The BackgroundWorker class allows you to run an operation on a separate, dedicated thread.
	Time-consuming operations like downloads and database transactions can cause your user interface (UI) to seem as though it has stopped responding

## When you want a responsive UI and you are faced with long delays associated with such operations, the BackgroundWorker class provides a convenient solution.


        private void startAsyncButton_Click(System.Object sender,  System.EventArgs e)
        {
                    // Start the asynchronous operation.
                    bw.RunWorkerAsync( 225 );
        }

            _________________  private void bw_DoWork(object sender,   DoWorkEventArgs e)
        |					{
        |					            // Get the BackgroundWorker that raised this event.
        |					            BackgroundWorker worker = sender as BackgroundWorker;
        |
        |					            // Assign the result of the computation to the Result property of DoWorkEventArgs
        |					            // object. This is will be available to the RunWorkerCompleted eventhandler.
        |
        |					            e.Result = ComputeFibonacci( (int)e.Argument, worker, e);
        |					}							↓
        |												↓
        |									long ComputeFibonacci(int n, BackgroundWorker worker, DoWorkEventArgs e)
        |									{
        |										...
        |										worker.ReportProgress(percentComplete);
        |									}
        |
        |	BackgroundWorker bw = new BackgroundWorker();
        |__ bw.DoWork += new DoWorkEventHandler( bw_DoWork );
            bw.ProgressChanged += new ProgressChangedEventHandler( bw_ProgressChanged );
                        ↓
                                                bw.RunWorkerCompleted 	+=  new RunWorkerCompletedEventHandler( bw_RunWorkerCompleted );
                        ↓
                                                                                                                ↓
                        ↓
    private void bw_ProgressChanged(object sender,  ProgressChangedEventArgs e)			private void bw_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
    {																					{
        this.progressBar1.Value = e.ProgressPercentage;								   	  // UPDATE YOUR GUI HERE
        // UPDATE YOUR GUI HERE															}
    }



    private void cancelAsyncButton_Click(System.Object sender,  System.EventArgs e)
        {
                // Cancel the asynchronous operation.
                this.bw.CancelAsync();
        }







```c#

```