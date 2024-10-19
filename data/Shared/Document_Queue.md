




# Document Queue
The Document Queue contains billing documents and reports (both Word 
 and Excel) that you chose to send to Document Queue. The screen comprises 
 the List and Detail Window. This screen can be accessed through:

	

- Ribbon - Home tab &gt; Documents &gt; Documents Overview &gt; 
    	 Action Items &gt; Document Queue.

	

- Viewpoint - Home screen - Click Home &gt; To Do &gt; Documents 
    	 &gt; Document Queue.

&nbsp;
<div>

<p><img src="../image370.gif" alt="" style="border-top-color: initial; border-top-style: none; border-top-width: initial; border-right-color: initial; border-right-style: none; border-right-width: initial; border-bottom-color: initial; border-bottom-style: none; border-bottom-width: initial; border-left-color: initial; border-left-style: none; border-left-width: initial;" width="23" height="21" border="0"> </p>
<p>Click this to view<span class="dropspot"> </span><a class="dropspot" href="javascript:TextPopup(this)" id="a11">the 
 Selection Setup to filter the records in the grid.</a></p>
<div class="droptext" id="POPUP392937807" style="display: none;">
	<ol class="hcp2">
		<li><p>In the Selection Setup, select your option from:</p>
		<ul class="hcp1">
			<li><p>Favourites - Click the desired <a class="dropspot" href="javascript:TextPopup(this)" id="a1">option</a>.</p>
			<div class="droptext" id="POPUP580521688" style="display: none;">
				<p>The following option is displayed when the condition 
				 is met:</p>
				<table class="Table1" cellspacing="0px" width="100%">
					<colgroup><col style="width: 32.726%;">
					<col style="width: 67.274%;">
					</colgroup><tbody><tr class="t1st">
						<td><p>Name</p></td>
						<td><p>Condition</p></td>
					</tr>
					<tr class="t2Row">
						<td class="t1Col"><p>Me</p></td>
						<td class="t2Col"><p>This is displayed in the list 
						 by default.</p></td>
					</tr>
					<tr class="t1Row">
						<td class="t1Col"><p>I am the Viewpoint Users' 
						 Manager</p></td>
						<td class="t2Col"><p>If the login user is specified 
						 as the manager of other user(s).</p></td>
					</tr>
					<tr class="t2Row">
						<td class="t1Col"><p>My primary Administrator Group</p></td>
						<td class="t2Col"><p>If the login user's Group 
						 Access is greater or equal to 'Files where Administrator 
						 and in Group[2]' in Home &gt; Configuration &gt; 
						 Users &amp; Security &gt; Users.</p></td>
					</tr>
					<tr class="t1Row">
						<td class="t1Col"><p>All my Administrator Groups</p></td>
						<td class="t2Col"><p>If the login user's Group 
						 Access is greater or equal to 'Files where Administrator, 
						 in Group + Group Member[3]' in Home &gt; Configuration 
						 &gt; Users &amp; Security &gt; Users.</p></td>
					</tr>
					<tr class="t2Row">
						<td class="t1Col"><p>My User Group</p></td>
						<td class="t2Col"><p>If the login user's Group 
						 Access is equal to 'All Files[4]' in Home &gt; 
						 Configuration &gt; Users &amp; Security &gt; Users.</p></td>
					</tr>
					<tr class="t1Row">
						<td class="t1Col"><p>All Users</p></td>
						<td class="t2Col"><p>If the login user's Group 
						 Access is equal to 'All Files[4]' in Home &gt; 
						 Configuration &gt; Users &amp; Security &gt; Users.</p></td>
					</tr>
				</tbody></table>
   </div></li>
			<li><p>Users - Tick to select the user(s).</p></li>
			<li><p>Workgroups - Tick to select the workgroup(s).</p></li>
			<li><p>Administrator Groups - Tick to select the Administrator 
			 Group(s).</p></li>
			<li><p>User Groups - Tick to select the User Group(s).</p></li>
			<li><p>Organisational Units - Tick to select the Organisational 
			 Unit(s).</p></li>
			<li><p>User Relations- Tick to select the user(s).</p></li>
		</ul></li>
		<li><p>Tick Apply to all screens if you want your selection to 
		 be applied to all other screens in Viewpoint - Home screen.</p></li>
		<li><p>Click Select.</p></li>
	</ol>
	<p><span class="hcp3">Note:</span> 
	 The available tabs depend on the File Access set for the user account 
	 in Configuration &gt; Users &amp; Security &gt; <a href="file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Users.htm">Users</a>.</p>
	<p>&nbsp;</p>
  </div>


 </div>
&nbsp;

Filters

The filters apply to the document list.

	

- Document format - You can choose to view only certain format 
    	 only, e.g. Word or all.

	

- Generation status - You can choose to view documents according 
    	 to a specific status or all.

[What does the 
 Document Generated Status mean?](javascript:TextPopup(this))
 
<div class="droptext" id="POPUP321194816" style="display: none;">
	

The status lets you know if the document has been generated or not. 
	 There are eight statuses:

	
		

- Pending - This indicates that the document has not been 
    		 generated. You can:

		

- 
    - 
        			
        
    - Generate the document
        
        
        			
    - Delete the document record
        
        
        			
    - Transfer the document record to another user
        
        
        		

		

- In Progress - This applies only to documents that are being 
    		 processed by the [Task 
    		 Scheduler](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Task_Scheduler/Task_Scheduler.htm).

		

- Ready to Deliver - This indicates that the document has 
    		 been generated and is queued for delivery.

		

- Delivering - This indicates that the document is in the 
    		 queue and ready to be sent out.

		

- Failed to Deliver - This indicates that the recipient does 
    		 not exist, validation failed or there was an error.

		

- Delivered - This indicates that the document was successfully 
    		 delivered.

		

- Error - This indicates that the document failed to be generated 
    		 due to an error in the template.

		

- Completed - This indicates that the document has been generated 
    		 and you can perform any of the document process.

		

- All - This will list all the documents available in the 
    		 Document Queue. 

	
	
<span class="hcp3">Note</span>: 
	 For Ready to Deliver, Delivering, Failed to Deliver and Delivered 
	 statuses are only applicable for the documents that contain Delivery 
	 Manager tag.
 </div>

&nbsp;

List

This is a listing of documents that you have sent to Document Queue 
 and for each document is a Detail window on the right. If the document's 
 template has Document Manager index tags, a holder will be created for 
 the document once it has been generated and you will see the following 
 command buttons:

	

- <span class="hcp5">Store</span> - Click this to 
    	 store the holder. This is only enabled if all mandatory index fields 
    	 have been completed.

	

- <span class="hcp5">Edit In-tray</span> - Click 
    	 this to [edit](javascript:TextPopup(this)) 
    	 the pending holder.
    
    	<div class="droptext" id="POPUP4302684241" style="display: none;">
    		Edit Holder Details - this is to update information for the 
    		 holder such as filing cabinet or the index fields. Click Save 
    		 in In-tray.
    		&nbsp;
    		Edit Holder Content - this is to make changes to the content 
    		 of the holder such as:
    		
        			    - Removing document from the holder
        			    1. 
        1. 
            				        1. Click to select the document.
            				        1. Press Delete key.
            				        1. Click OK to confirm the deletion.
            				        1. Click Save in In-tray.
            			
        			    - Adding document to the holder
        			        1. 
            				        1. Open the folder containing the file.
            				        1. Click and drag the file to the Detail Window.
            				        1. Click Save in In-tray.
            			
        		
     </div>

	

- <span class="hcp5">Add Task</span> - Click this 
    	 to [add](javascript:TextPopup(this)) 
    	 a task to the document in the selected holder. This will create a 
    	 document task.
    
    	<div class="droptext" id="POPUP4302618551" style="display: none;">
    		
        			    1. Enter the task details:
        			
            				        - Task Type - Select the task type. This is set up 
            				 in Configuration &gt; Business Parameters &gt; Document 
            				 Management &nbsp;&gt; Tasks.
            				        - Task Description - Enter a description of the task.
            				        - Assigned to - Select the assignee.
            				        - Date due - Enter the date of when the task needs 
            				 to be completed.
            				        - Note - Enter additional notes about the task.
            			
        			    1. Click Update.
        		
    		&nbsp;
     </div>

	

- <span class="hcp5">Cancel</span> - Click this 
    	 to cancel changes to the holder. This is only enabled after you have 
    	 chosen Edit In-tray.

If the document's template does not have Document Manager index tags, 
 you will see only this:

	

- <span class="hcp5">Create Holder</span> - Click this to create 
    	 a holder.

&nbsp;

Command buttons

Click on the relevant command button to perform the necessary.

	

- <span class="hcp5">Open</span> - Click this to 
    	 view document that has been generated.

	

- <span class="hcp5">Select All</span> - Click this 
    	 to select all documents.

	

- <span class="hcp5">Deselect All</span> - Click 
    	 this to deselect all documents.

	

- <span class="hcp5">Generate</span> - Click this 
    	 to [generate](javascript:TextPopup(this)) 
    	 the selected pending document. For documents with [Document 
    	 Manager index tags](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Document_Manager/Document_Management_Tags.htm), a holder will be created automatically for 
    	 the generated document, allowing the document to be stored directly 
    	 from this screen.
    
    	<div class="droptext" id="POPUP321215672" style="display: none;">
    		Select the generation option and click Start:-
    		&nbsp;
    		<h6 class="Heading8">Generate the document(s) only</h6>
    		Choose this to have the program generate the selected document(s). 
    		 To view the generated document(s), tick 'Open the generated document(s)' 
    		 option.
    		<span class="hcp3">Note</span>: 
    		 If you will be utilising Delivery Manager for the document, choose 
    		 this option without opening the generated document.
    		&nbsp;
    		<h6 class="Heading8">Generate the document(s) and:</h6>
    		Choose this to have the program generate the selected document(s) 
    		 and perform additional action. You can:
    		
        			    - Define the location for the generated documents in Location.
        			    - Choose to convert the document to e-mail and send it, 
        			 place it in Outlook's Drafts folder, open the e-mail or save 
        			 it as .msg file.
        			    - Choose to convert the document(s) to Acrobat PDF format 
        			 and add to E-mail Bin by ticking the option 'Add the document(s) 
        			 to the E-mail Bin'.
        		
    		&nbsp;
    		<h6 class="Heading8">Print the generated document(s) to the default 
    		 printer</h6>
    		Choose this to have the program sent the document to the default 
    		 printer.
    		&nbsp;
    		<h6 class="Heading8">Remove all e-mail tags and e-mail body from 
    		 generated document(s)</h6>
    		Select this to remove e-mail tags and section in the generated 
    		 Word document. This function will be disabled if the 'Convert 
    		 e-mail formats and...' or 'Add the document(s) to the E-mail Bin' 
    		 options are ticked.
    		&nbsp;
    		<span class="hcp3">Note</span>: 
    		 If you do not wish to retain the record in Document Queue after 
    		 the document has been generated, tick the option 'Delete the document(s) 
    		 from the Document Queue'.
    		&nbsp;
     </div>

	

- <span class="hcp5">Delete</span> - Click this 
    	 to delete the selected document(s). Note that this will delete the 
    	 physical documents with Document Manager index tags in Archive and 
    	 Temporary Folder as well.

	

- <span class="hcp5">Print</span> - Click this to 
    	 print the selected document(s). This is applicable only for documents 
    	 that have been generated. Note that when printing a 'PDF' document 
    	 (XFA-based document), the document will not print directly to the 
    	 default printer; instead, it will open in any PDF reader. The printing 
    	 would be done via the PDF reader. 

	

- <span class="hcp5">Check In</span> - Click this 
    	 to check in the document into server. This option is applicable only 
    	 when Viewpoint.WIN is connected to the Application Server.

	

- <span class="hcp5">Delivery Manager</span> - Click 
    	 this to open [Document 
    	 Delivery Manager](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Document_Manager/Delivery_Manager.htm) screen. This applies only to Word documents.

	

- <span class="hcp5">Transfer</span> - Click this 
    	 to change the user for the selected document to another user. This 
    	 will remove the record of the document from the original user's Document 
    	 Queue list.

	

- <span class="hcp5">Move to In-tray</span> - This 
    	 will send the generated document to your [In-tray](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Document_Manager/In_tray.htm).

&nbsp;

See also:

	

- [Word Reports](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Word_Reports.htm)

	

- [Excel Statements](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Excel_Statements.htm)

	

- [Billing 
    	 Templates](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Billing_Templates_Library.htm)

	

- [Report 
    	 Queue Generation](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Task_Scheduler/Report_Queue_Generation.htm)

	

- [XML Viewer](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/XML_Viewer_Screen.htm)


 
&nbsp;

You are here:[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; [Viewpoint - Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Overview.htm) &gt; [Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Overview.htm) &gt; [To Do](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Overview.htm) &gt; [Documents](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Form_queue.htm) &gt; Document Queue
 
&nbsp;
 
(c) Viewpoint Software for 
 Business Ltd
 
Version: 8.0.2022.09.20




