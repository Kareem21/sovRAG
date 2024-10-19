




# Viewpoint Local Agent
Viewpoint Local Agent performs synchronisation tasks between the server 
 database and user's Local Database in the background so that front-end 
 user operation in Viewpoint is not interrupted. Users can continue to 
 use Viewpoint normally without any waiting period during:

	

- the synchronisation of configuration data between server database 
    	 and Local Database

	

- uploading of document holders and files from Local Database 
    	 to the server database

Viewpoint Local Agent resides in the user's workstation and utilises 
 Application Server to perform the above periodically.

![](../VPlocal%20agent.png)

Viewpoint Local Agent is to be enabled through ViewPointDbMgt.exe but 
 users can choose when to launch Viewpoint Local Agent and to disable it 
 through [User Options](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/User_Options.htm).

&nbsp;
## Interface
When opening Viewpoint Local Agent, you will see the following tabs:

	

- Tasks

	

- Failed Items

	

- Options

At the bottom, you will see the status of Viewpoint Local Agent and 
 the following details:

	

- Environment name

	

- Current date

	

- Logged-in user's ID

	

- Application version number

	

- Server name

	

- Database name

&nbsp;
### Tasks tab
<span class="hcp3">This shows tasks for Viewpoint 
 Local Agent and the status which can be:</span>

	

- <span class="hcp5">Pending</span> 
    	 – Viewpoint Local Agent has yet to complete the task.

	

- <span class="hcp5">In 
    	 Progress</span> – Viewpoint Local Agent is in the middle of completing 
    	 the task.

	

- <span class="hcp5">Failed</span> 
    	 – Viewpoint Local Agent has failed to complete the task.

	

- <span class="hcp5">Completed</span> 
    	 – Viewpoint Local Agent has completed the task successfully.

<span class="hcp3">There 
 are four command buttons under this tab:</span>

	

- <span class="hcp5">Edit</span> 
    	 <span>- Click this to edit details of the document holder before it 
    	 is uploaded to the server database. This button is enabled only when 
    	 the Task is 'Transfer Local In-tray Item', the Local Agent status 
    	 is 'Stopped' and the Task status is 'Pending'.</span>

	

- <span class="hcp5">Refresh</span> 
    	 - Click this to refresh grid records.

	

- <span class="hcp5">Stop/Resume</span> 
    	 - Click this to stop/resume Viewpoint Local Agent. The status will 
    	 be reflected on the bottom left corner of the screen. Once Viewpoint 
    	 Local Agent has been stopped, all pending tasks will remain as such 
    	 until Viewpoint Local Agent is started again.

	

- <span class="hcp5">Open 
    	 Log</span> - Click this to open the log file to view the task status 
    	 or error. This button is disabled when there is no log. Log files 
    	 are stored on a daily basis. When clicking Open Log button in Local 
    	 Agent program while the task agent is running, the latest log file 
    	 will be copied over to a temporary folder and open in the temporary 
    	 folder.

&nbsp;
### Failed Items tab
<span class="hcp3"><span class="hcp3">T</span>his tab shows tasks that 
 have failed according to the following classification:</span>

	

- All items

	

- Add to existing holder

	

- Add to existing holder (Holder 
    	 Deleted)

	

- New document holder

<span class="hcp3">Within 
 this tab are the following command buttons:</span>

	

- <span class="hcp5">Select 
    	 All</span> - Click this to select all records from the grid.

	

- <span class="hcp5">Deselect 
    	 All</span> - &nbsp;Click this to deselect all records from the grid.

	

- <span class="hcp5">Edit</span> 
    	 - Click this to edit details of the document holder before it is uploaded 
    	 to the server database. This button is enabled only when the Task 
    	 is 'Transfer Local In-tray Item', the Local Agent status is 'Stopped' 
    	 and the Task status is 'Pending'.

	

- <span class="hcp5">Refresh</span> 
    	 - Click this to refresh grid records.

	

- <span class="hcp5">Move 
    	 to Queue</span> - Click this to transfer the failed local in-tray 
    	 items back to queue so that it will re-upload into the server again.

	

- <span class="hcp5">Delete</span> 
    	 - Click this to delete the local in-tray item. Once deleted, the item 
    	 will not be able to recover and the user will need to store the document 
    	 with a new document holder number.

&nbsp;
### Options tab
The Options tab consists of the settings 
 for Viewpoint Local Agent. <span class="hcp3">The 
 'Tasks' options are:</span>

	

- <span class="hcp5">Synchronise 
    	 Local Cache</span> - Tick this to enable the application to perform 
    	 synchronisation whenever there is update on the local database.

	

- <span class="hcp5">Transfer 
    	 Local In-tray</span> - Tick this to enable the application to perform 
    	 document upload from local In-Tray in Viewpoint.WIN to the server.

The 'Viewpoint Local Agent Program 
 Options' are:

	

- <span class="hcp5">Show 
    	 Notification in Taskbar</span> - Tick this to enable popup notification 
    	 on the task progress.

	

- <span class="hcp5">Interval</span> 
    	 - Enter the time interval for the application to perform task in the 
    	 unit measure of minute.

	

- <span class="hcp5">Number 
    	 of retries</span> - Enter the number of attempts for Viewpoint Local 
    	 Agent to complete a failed task. The default value is 5 attempts. 
    	 Each attempt will take place after the interval set in Retry after 
    	 field below. Maximum number of attempts is 35791.

	

- <span class="hcp5">Retry 
    	 after</span> - Enter the time interval in minutes for each retry by 
    	 Viewpoint Local Agent to complete a failed task. The default interval 
    	 is 30 minutes.

&nbsp;
## Viewpoint Local Agent Tasks
Tasks performed by Viewpoint Local Agent are as follows:

	

- [Transfer 
    	 Local In-tray Item](javascript:TextPopup(this)) - this is to upload new document 
    	 holders and files from Local Database to server database.
    
    	<div class="droptext" id="POPUP599122776" style="display: none;">
    		The physical document file will be moved to the local Document 
    		 Store folder with the following path:
    		[User Document Management Folder]\DOCSTORE\[Holder no. structure 
    		 in four levels].
    		For example, Holder number 110:
    		C:\Users\SallyMichaels\Documents\Viewpoint.VPMALN50.VP73XX\DOCSTORE\00\00\01\10
    		When the new document holder is added, Viewpoint Local Agent 
    		 will display the status as ‘Pending’. During the upload process, 
    		 the status will show as ‘In Progress’. Once completed, it will 
    		 update the status into ‘Completed’. The record in the local database 
    		 as well as the local files will be removed.
    		If the task has failed, it will update the status into ‘Failed’. 
    		 The records in the local database remain. The failed records will 
    		 be transferred to the ‘Failed Items’ tab.
    		&nbsp;
     </div>

	

- [Add 
    	 document(s) to existing holder](javascript:TextPopup(this)) - this is to upload 
    	 new document files to server database.
    
    	<div class="droptext" id="POPUP599231773" style="display: none;">
    		When the new document is added, Viewpoint Local Agent will display 
    		 the status as ‘Pending’. During the upload process, the status 
    		 will show as ‘In Progress’. Once completed, it will update the 
    		 status as ‘Completed’. The record in the local database as well 
    		 as the local files will be removed.
    		If the task failed, there are two types of possibilities:
    		
        			    - Holder does not exist in the Server (or deleted by other 
        			 user). The record will be transferred to the ‘Failed Items’ 
        			 tab. Under the ‘Failed Items’ tab, the Move to Queue button 
        			 is disabled.
        			    - For other types of error, the record will be transferred 
        			 to the ‘Failed Items’ tab. User can still click on Move to 
        			 Queue button to queue the item for re-upload into the server 
        			 again.
        		
    		<span style="font-weight: bold; font-style: italic;">Note</span>: 
    		 If editing holder details such as the description or index fields, 
    		 then change will be saved directly to the server database.
    		&nbsp;
     </div>

	

- [Synchronise 
    	 Local Database](javascript:TextPopup(this)) - this is to update the Local Database 
    	 with configuration data from the server database.
    
    	<div class="droptext" id="POPUP599252862" style="display: none;">
    		The Task column will display ‘Synchronise Local Cache’. When 
    		 the data is edited in Viewpoint.WIN, the Viewpoint Local Agent 
    		 will display the status as ‘Pending’. During the synchronisation 
    		 process, the status will show as ‘In Progress’. Once completed, 
    		 it will update the status into ‘Completed’.
    		If the local cache synchronise failed, Viewpoint Local Agent 
    		 will re-create the task with ‘Pending’ status. The task will be 
    		 picked up again on the next interval session.
     </div>

&nbsp;

&nbsp;

See also:

	

- [Local Database](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Local_Database.htm)


 
&nbsp;

[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; Viewpoint Local Agent
 
&nbsp;
 
(c) Viewpoint Software for 
 Business Ltd
 
Version: 8.0.2022.09.20




