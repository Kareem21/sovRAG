




# Status
This shows an overview of available status types for the Master File. 
 The display is based on the design of the summary screen template that 
 is set for this screen. If necessary, you can save this screen as a HTML 
 or PDF file; or print it out by right-clicking in the screen and selecting 
 the option you want.

The status of the Master File, CDD, Entity File, Billing File, Supplier 
 File and Account File are maintained in the respective Status type screens:

	

- Master File - This is where you set the status for the Master 
    	 File and the effective date of the status as well as additional remark 
    	 in the Note field. The Master File status options are maintained in 
    	 the Master File Status [RECS] lookup table. If you enable Master File 
    	 Sub-Status field, this will be right below the Status field. Options 
    	 for sub-status are maintained in the Master File Sub-Status [ROSU] 
    	 lookup table.  
    &#13;&#10;	  
    &#13;&#10;	<span class="hcp2">Note</span>: Default 
    	 Master File status for new Master Files is set in [System 
    	 Defaults &gt; General/Master File](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/System_Defaults_-_General_Master_File.htm).

	

- CDD - This is seen only if the Master File require Client Due 
    	 Diligence and allows for updates to the CDD Status, Risk Level and 
    	 Profile fields. If you enable the Local Risk Level field, this will 
    	 be below the Risk Level field. These fields are also in the [CDD](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/MF_-_CDD.htm) 
    	 screen.

	

- Entity - This is where you set the status for the Entity File 
    	 and the effective date of the status. Available options are maintained 
    	 in the Company Status [COST] lookup value table. If you enable the 
    	 Entity Sub-Status field, this will be under the Entity Status field. 
    	 Options for entity sub-status are maintained in the Entity Sub-Status 
    	 [COSU] lookup table.

	

- Billing File - This is where you set the status for the Billing 
    	 File and the effective date of the status. The options here are maintained 
    	 in the Billing File Status [BFST] lookup table where the standard 
    	 values are [here](javascript:TextPopup(this)). 
    	 You will also see the list of Matters for the Billing File and if 
    	 necessary, change the Matter status. All Matter status must be greater 
    	 than or equal to the Billing File status.  
    &#13;&#10;	  
    &#13;&#10;	<span class="hcp2">Note</span>: Status 
    	 of less than 5 is considered as 'active'.
    
    	<div class="droptext" id="POPUP596826459" style="display: none;">
    		
        			    - 0 - Open
        			    - 1 - Blocked invoicing (automatic 
        			 invoicing is not possible for the Billing File but you can 
        			 still record time)
        			    - 2 - Blocked time entry (automatic 
        			 invoicing is possible and users can only create time entries 
        			 for the service specified in 'Blocked Matters - Time Service' 
        			 in System Defaults - Time Management)
        			    - 3 - On Hold (you can only 
        			 do matter/invoice settlements)
        			    - 5 - Suspended (similar to 
        			 Closed)
        			    - 9 - Closed
        		
     </div>

	

- Supplier - This is where you set the status for the Supplier 
    	 File as well as the effective date of the status. The options here 
    	 are maintained in the Billing File Status [BFST] lookup table.

	

- Account File - This is where you can deactivate the status for 
    	 the Account File and the effective date of the change. The deactivation 
    	 is by unticking the Account File Active option.

To make changes, select the relevant Status type screen and include 
 the Effective Date when you change the status before you click Update. 
 Note that you cannot change the status of a Master File to Close/Inactive[8] 
 or Marked for Removal[9] if the other statuses have not been deactivated.

A record of the changes made will be shown in a grid at the bottom of 
 the screen with the following details:

	

- Date Change - this is the date of when the change was made.

	

- Effective Date - this is the date entered in the Effective Date 
    	 field for the status change.

	

- Type - this refers to the type of status that was changed. The 
    	 types are values in the Status Changes Types [SCTP] lookup table.

	

- Description - this shows the previous status and the new status.

	

- Note - this shows the information entered in the Note field 
    	 for the status change.

&nbsp;

See also:

	

- [Lookup Tables](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Lookup_Tables.htm)

&nbsp;
## Change History Screen
This screen shows the status changes that have been made and allows 
 you to update the Effective Date and Note for the change.

&nbsp;

Change list

The list shows all status changes from all Status screens.

&nbsp;

Effective Date

This allows for updating the effective date of a selected change.

&nbsp;

Note

This allows for updating the Note information of a selected change.

&nbsp;

Command buttons

Click on the relevant command buttons to perform the necessary.

	

- <span class="hcp4">Update</span> - Click this 
    	 to save the changes made.

	

- <span class="hcp4">Cancel</span> - Click this 
    	 to cancel the changes.

&nbsp;
## &nbsp;Status Summary Screen
This shows an overview of all the statuses of the Master File.

&nbsp;

&nbsp;

See also:

	

- [Summary Screen](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Summary_Screen.htm)


 
&nbsp;

You are here:[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; [File Maintenance](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/File_Maintenance_screen.htm) &gt; [General](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Overview.htm#642b3b9347ca42c9b00b820c00c373fa=1) &gt; [Master File](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/MF_-_Setup.htm) &gt; [Master File](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/MF_-_Setup.htm) &gt; Status
 
&nbsp;
 
(c) Viewpoint Software for 
 Business Ltd
 
Version: 8.0.2022.09.20




