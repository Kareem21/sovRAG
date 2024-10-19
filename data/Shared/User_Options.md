




# <span class="Bold">User Options</span>
The User Options screen is where you specify your preferences for Viewpoint. 
 The User Options screen is divided into:

	

- [General](javascript:TextPopup(this)) 
    	 - This is where you specify your preferred settings.
    
    	<div class="droptext" id="POPUP327482609" style="display: none;">
    		Location of Folder for Saving Revisions, 
    		 New Documents and Documents for Mailing (we recommend using a 
    		 sub-folder of "My Documents")
    		Set the path to be used for the storing of revisions, new documents 
    		 and documents to be e-mailed.
    		&nbsp;
    		Notify for New Tasks and Batches
    		Tick to be notified of new tasks or scanned batches assigned 
    		 to you. This will be done based on the interval set.
    		&nbsp;
    		Prompt "Document Checked Out" upon 
    		 Exit
    		Tick to receive alert for documents that are still checked out 
    		 when you choose to exit Viewpoint.
    		&nbsp;
    		Detect and Repair Missing Components at Start 
    		 Up
    		Tick this to have Viewpoint check for missing components when 
    		 user logs in. The components may be missing if ViewpointSetup.exe 
    		 was run using a user account that does not have administrator 
    		 rights on the machine.
    		&nbsp;
    		Microsoft Word - Manually Generate Forms/Reports
    		Tick this to manually generate documents. This means you need 
    		 to open Microsoft Word and click Generate. 
    		<span class="hcp2">Note</span>: 
    		 When updated, please perform a local database synchronisation 
    		 to reflect new setting's value.
    		&nbsp;
    		Maximum Number of Master File Windows Allowed
    		Enter the number of File Maintenance windows that you want opened 
    		 at any one time. A prompt message will be displayed if you are 
    		 trying to open more than is allowed. 
    		<span class="hcp2">Note: </span>When 
    		 updated, please perform a local database synchronisation to reflect 
    		 new setting's value.
    		&nbsp;
    		Refresh/Notification Interval (Minutes)
    		Enter the interval for the screen to be refreshed and check 
    		 for new tasks/scan batches. If the [Notifications](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Notifications.htm) 
    		 feature is enabled, then this checks for new notification items.
    		&nbsp;
    		Search Control Auto Suggest Delay
    		Enter the interval before auto-suggestion is displayed when 
    		 user enters at least three characters during a search. The value 
    		 is in milliseconds and cannot be more than 1000. If you do not 
    		 wish to enable the auto-suggestion, enter 0. Default value is 
    		 500 milliseconds = half a second.
    		&nbsp;
    		Record Limit for Custom Reports
    		Enter the number of records for inclusion in a custom report. 
    		 This is particularly important if your computer has restricted 
    		 memory. When you create a custom report, you will be able to view 
    		 the results in the View folder. The limit comes into effect when 
    		 you view, print or preview the report: if there is more than the 
    		 set number of records, the report will be truncated to show only 
    		 the number of records set as the limit. Therefore, if you need 
    		 to run a large report, increase the limit and save the new default. 
    		 After the report has been generated, reduce the limit to its original 
    		 default number of 1,500.
    		To disable a record limit, enter 0. 
    		<span class="hcp2">Note: </span>When 
    		 updated, please perform a local database synchronisation to reflect 
    		 new setting's value.
    		&nbsp;
    		Theme
    		Select the colour scheme for the Ribbon, Section Menu, Info 
    		 Pane, Tool, and Status bar.
    		&nbsp;
    		Spell Check Dictionary
    		Select the dictionary to use for checking spelling for Note 
    		 fields. Available languages are as follow:
    		
        			    - English - Great Britain (default)
        			    - English - US
        			    - French - France
        			    - Dutch
        			    - German
        		
    		PDF Printer Properties
    		Click to set up the [properties](javascript:TextPopup(this)) 
    		 for the Viewpoint PDF Printer.
    		<div class="droptext" id="POPUP4713667661" style="display: none;">
    			<div>
    The Viewpoint PDF Printer is only for use within Viewpoint to convert 
     documents to PDF files. The properties allow you to set the following:
        
        	    - Paper size - Select the paper size for the resulting PDF files.
        	    - Use Viewpoint PDF Printer (smaller file size) - If you have 
        	 Office 2007 and above, Microsoft PDF Printer is used by default. Tick 
        	 this to use Viewpoint PDF Printer instead for creation of smaller 
        	 PDF files from Viewpoint. Note that this is not applicable for conversion 
        	 to PDF through Word add-ins.
        	    - Embed Fonts in PDF File - Tick to include all font information 
        	 so that your documents will look the same after conversion. If you 
        	 do not embed fonts, font substitution will be performed when the font 
        	 used in the document is not available on your computer. This can result 
        	 in significant differences.
        	    - Other options 
        	
            		    - 
        - For next PDF File only - Select this if you want to apply 
            		 the password and/or watermark settings to the next PDF file created.
            		    - 
        - Save for all - Select this if you want to apply the password 
            		 and/or watermark settings for all PDF files created in Viewpoint.
            		    - 
        - Set Password - Tick to set password for PDF files created 
            		 in Viewpoint. See also [Password 
            		 Protection for PDF Files](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Password_Protection_for_PDF_files.htm).
            		    - 
        - Print Watermark - Tick to include watermark to the PDF files. 
            		 You can select the word 'Draft', 'Confidential' or 'Secret' as 
            		 your watermark.
            	
    
    </div>
      </div>
    		&nbsp;
    		Clear/Reset Settings
    		Click to clear current settings. Tick the relevant options:
    		
        			    - Reset Grid Layouts - this resets the customised settings 
        			 for grid layouts. Users must be authorised to customise the 
        			 layout of grids, menu and toolbars.
        			    - Delete Word Spool Files - this removes the .vps files 
        			 that are temporarily created in the user's sub-folder of the 
        			 UserPrev folder in the Viewpoint environment.
        			    - Restore Default Startup Screen - this resets the startup 
        			 screen to Viewpoint's default.
        			    - Reset Local Folder/Document Management Folder - this 
        			 resets the folder paths to the paths set in the local machine 
        			 registry
        			    - Reset User Registry - this clears Viewpoint Current 
        			 User Registry keys(HKEY_CURRENTUSER\Software\VB and VBA Program 
        			 Settings\Viewpoint.WIN) except for the items listed [here](javascript:TextPopup(this)).
        			<div class="droptext" id="POPUP344079135" style="display: none;">
        				
            					        - Application server setting (Viewpoint Connect\AppServer)
            					        - Task scheduler and notification setting (Viewpoint 
            					 Connect\TSNA)
            					        - User setting (Viewpoint Connect\User)
            					        - Defaults setting which store the temporary folder 
            					 path (Viewpoint Connect\Default)
            					        - Detect and repair option (Viewpoint Connect\Options)
            					        - ViewPoint Add-Ins - Outlook setting (Viewpoint 
            					 Connect\Outlook Index Actions)
            					        - Outlook Index Action (Viewpoint Connect\Outlook 
            					 Index Actions)
            					        - Document Management Folder path (Viewpoint Connect\DocumentManagerFolder)
            				
           </div>
        		
    		Add-ins Timeout (Seconds)
    		This function allows the configuration of the timeout period 
    		 between Viewpoint Add-ins and Viewpoint Connect. You may change 
    		 the value of this field to suit your network latency requirements. 
    		 The default value is 300 seconds with a minimum value of 60 seconds 
    		 and a maximum of 1800 seconds. Adding other values than 60-1800 
    		 seconds will prompt a message.
    		<h3>&nbsp;</h3>
    		<h3>Session-based Options</h3>
    		Disable the Change Processing Screen
    		Tick this to disable the [Change 
    		 Processing screen](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Change_Processing_Screen.htm) for the current login session. By default, 
    		 this screen is always enabled when you log in to Viewpoint but 
    		 can be turned off if you are entering historical data and do not 
    		 require the linked forms. This option will revert back to the 
    		 default setting (unticked) after logging out of Viewpoint.
      </div>

	

- [Confidential 
    	 Database](javascript:TextPopup(this)) - This is available only if you have 
    	 set up confidential database. Click [here](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Confidential_Database.htm) 
    	 for information on Confidential Database.
    
    	<div class="droptext" id="POPUP327304071" style="display: none;">
    		Connect to Confidential Data
    		Select the confidential database that you want to connect and 
    		 click OK. To disconnect, select Disconnect [DISCN].
     </div>

	

- [Local 
    	 Database](javascript:TextPopup(this)) - This is available when local cache 
    	 is enabled in Viewpoint Database Management. Click [here](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Local_Database.htm) 
    	 for information on Local Database.
    
    	<div class="droptext" id="POPUP68552112" style="display: none;">
    		Local Database
    		
        			    - <span class="hcp3">Status</span> – This 
        			 shows the status of the local database on your workstation. 
        			 If the local database has been set up, the status will show 
        			 as 'Connected'. If Local Database option is enabled but has 
        			 not been set up on the client workstation, this will show 
        			 as 'Not Connected'.
        			    - <span class="hcp3">Synchronised</span> 
        			 – This indicates if synchronisation is required between the 
        			 local database and the server database. If there is a difference, 
        			 then this will show as 'Yes', otherwise 'No'.
        			    - <span class="hcp3">Detect &amp; Repair</span> 
        			 – Click this to check for differences between the local database 
        			 and the server database. When prompted, click OK to start 
        			 checking and perform synchronisation when differences are 
        			 detected.
        		
    		&nbsp;
    		Viewpoint Local Agent
    		
        			    - Enable Viewpoint Local Agent 
        			 <span style="font-weight: normal;">– Tick this to enable Viewpoint 
        			 Local Agent for your workstation. Prior to enabling this, 
        			 you need to ensure that the Viewpoint Local Agent feature 
        			 is enabled in ViewPointDbMgt.exe.</span>
        			    - <span class="hcp3">Status</span> - This 
        			 indicates if Local Agent is currently running or not. The 
        			 status can be:
        			    - 
        - 
            				        - Active - Local Agent is currently running
            				        - Inactive - Local Agent is not running
            				        - Not Available - Local Agent is not enabled 
            				        - 'ViewPoint.Win.LocalAgent.exe' not found - Local 
            				 Agent has not been installed correctly and cannot be launched
            			
        			    - <span class="hcp3">Launch Viewpoint Local 
        			 Agent</span> <span style="font-style: italic;">-</span> <span>If 
        			 Viewpoint Local Agent is not running, click this to launch 
        			 Viewpoint Local Agent.</span>
        			    - <span class="hcp3">Launch Viewpoint Local 
        			 Agent upon log in to Viewpoint Connect</span> – Tick this 
        			 to automatically launch Viewpoint Local Agent when logs in 
        			 to Viewpoint Connect.
        			    - <span class="hcp3">Shut down Viewpoint 
        			 Local Agent upon log out from Viewpoint Connect</span> – Tick 
        			 this to automatically shut down Viewpoint Local Agent when 
        			 logs out from Viewpoint Connect.
        		
    		<span class="hcp2">Note</span>: 
    		 If Viewpoint Local Agent feature is disabled in ViewPointDbMgt.exe, 
    		 then Viewpoint Local Agent installed on users' workstations will 
    		 also be disabled.
     </div>

&nbsp;

Command buttons

Click on the relevant command button to perform the necessary.

	

- <span class="hcp3">OK</span> - Click this to save 
    	 your settings.

	

- <span class="hcp3">Cancel</span> - Click this 
    	 to close the window without making changes.


 
&nbsp;

You are here:[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; [Viewpoint - Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Overview.htm) &gt; [Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Overview.htm) &gt; [To Do](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Overview.htm) &gt; User Options
 
&nbsp;
 
(c) Viewpoint Software for 
 Business Ltd
 
Version: 8.0.2022.09.20




