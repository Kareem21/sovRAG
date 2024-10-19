[]()




# Filings
The Filings screen is where you record filings that are required for 
 the company and all the preparation required. You can access this screen 
 in File Maintenance screen through:

	

- General &gt; Master File &gt; Folders &gt; Filings for Master 
    	 Files that are not managed entities.

	

- Entity Administration &gt; Initiate/Report &gt; Filings for 
    	 Master Files that are managed entities.

Information for this screen can be populated manually or automatically 
 using [File Review](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/File_Review_Function.htm) function. There 
 are three sections in this screen and you can click on:

	

- ![](../image307.gif) 
    	 - To minimise this section and hide the command buttons. In the grid, 
    	 only the selected row will be seen.

	

- ![](../image308.gif) 
    	 - To expand the section and show the command buttons.

&nbsp;
### Filing Types
This section allows you to record the types of filings required.

&nbsp;

Filter

The filter applies to the Filing Types List.

&nbsp;

Filing Types List

The list shows the types of filing that apply to the selected Master 
 File.

&nbsp;

Command buttons

Click on the relevant command button to perform the necessary. The buttons 
 apply to the Filing Types section.

	

- <span class="hcp3">New</span> - Click this to 
    	 [add](javascript:TextPopup(this)) 
    	 a new filing type.
    
    	<div class="droptext" id="POPUP317057140" style="display: none;">
    		
        			    1. Enter the relevant information.
        			    1. Click Update when done.
        		
     </div>

	

- <span class="hcp3">Edit</span> - Click this to 
    	 edit selected filing type.

	

- <span class="hcp3">Delete</span> - Click this 
    	 to delete the selected filing type.

<span class="hcp5">Note</span>: You 
 can only deactivate a filing type if there are no pending filing instances.

&nbsp;
### Filings
This section allows you to record filings due.

&nbsp;

Filings List

The list shows instances of a selected filing type.

&nbsp;

Command buttons

Click on the relevant command button to perform the necessary. The buttons 
 apply to the Filings section.

	

- <span class="hcp3">New</span> - Click this to 
    	 [add](javascript:TextPopup(this)) 
    	 new filing due.
    
    	<div class="droptext" id="POPUP317064824" style="display: none;">
    		
        			    1. Enter the relevant information.
        			    1. Click Update when done.
        		
     </div>

	

- <span class="hcp3">Edit</span> - Click this to 
    	 edit selected filing.

	

- <span class="hcp3">Delete</span> - Click this 
    	 to delete the selected filing record.

	

- <span class="hcp3">Batch Maintenance</span> - 
    	 Click this to launch the [Batch Assign](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Tax_Batching.htm) 
    	 screen. This button is hidden by default due to [authority 
    	 settings](javascript:TextPopup(this)). The Filings need to be [configured 
    	 to enable this button](javascript:TextPopup(this)).
    
    	<div class="droptext" id="POPUP624484384" style="display: none;">
    		The following actions are required to enable this button for 
    		 the Filings:
    		&nbsp;
    		<h3>Assign Account Batch Number &nbsp;to Filing Sub-Type</h3>
    		The Batch Maintenance button is enabled for the Filing if the 
    		 batch is defined in the Tag Values of Lookup Value table ‘Filing 
    		 Sub Type [FLTS]’.
    		
        			    1. Go to Configuration &gt; Business Parameters &gt; General 
        			 &gt; Lookup Values and look for ‘Filing Sub Type [FLTS]’ table.
        			    1. Select the Filing Sub Type at the bottom grid and click 
        			 Edit.
        			    1. In the Tag Values, enter the tag in the format [Batch=&lt;batch 
        			 number&gt;], where Batch Number must within 1 to 5.
        			    1. Click Update.
        		
    		Repeat steps (2) to (4) for other Filing Sub Type.
    		&nbsp;
    		<h6 class="Heading8">Referencing Tag</h6>
    		Referencing tag is supported with the following tag syntax:
    		[CODEREF.FLTS.&lt;the referred Filing Sub Type Code&gt;]
    		Example:
    		[CODEREF.FLTS. VAET] is entered in the Tag Values to enable 
    		 a Filing Sub Type to refer to the Batch number that is assigned 
    		 to the Filing Sub Type code ‘VAET’.
    		&nbsp;
    		<h3>Assigning Accounting Journals to Filings</h3>
    		In the Filings screen, the Tax Account sub-ledger code is to 
    		 be entered in the Reference field of the Filing Type record.
    		This is to load all Accounting journals for the specified Tax 
    		 Account sub-ledger code when the Refresh button is clicked in 
    		 the Batch Assign screen.
    		
        			    1. Select the Filing Sub Type from the Filing Types section 
        			 (Top grid) and click Edit.
        			    1. In the ‘Reference’ field, enter the Tax Account sub-ledger 
        			 code.
        			    1. Click Update.
        		
     </div>
    	<div class="droptext" id="POPUP589108479" style="display: none;">
    		You can grant authority from the Configuration &gt; Settings 
    		 &gt; Customise &gt; Field Settings screen.
     </div>

<span class="hcp5">Note</span>: You 
 will not be able to set the status as Completed or deactivate the filing 
 if the related action(s) are not completed.

&nbsp;
### Filing Actions
This section allows you to record action required for the selected filing.

&nbsp;

Filing Actions List

This shows the actions for a selected filing instance.

&nbsp;

Command buttons

Click on the relevant command button to perform the necessary. The buttons 
 apply to the Filing Actions section.

	

- <span class="hcp3">New</span> - Click this to 
    	 [enter](javascript:TextPopup(this)) 
    	 an action item for the selected filing.
    
    	<div class="droptext" id="POPUP317059500" style="display: none;">
    		Enter the relevant information. Click Update when done.
     </div>

	

- <span class="hcp3">Edit</span> - Click this to 
    	 edit the action item.

	

- <span class="hcp3">Delete</span> - Click this 
    	 to delete the select action item.

	

- <span class="hcp3">Complete</span> - Click this 
    	 to indicate the action has been completed. This will update the Date 
    	 Done field with today's date and tick the Completed field. You can 
    	 also use tags to have the completion of an action update fields for 
    	 the Filing Record or perform a File Review automatically. Refer to 
    	 [Action 
    	 Codes for Filings, Meetings and Reviews](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Action_Codes_for_Filings,_Meetings_and_Reviews.htm).

If you are using Filings screen to keep track of Annual Return filings, 
 consider turning off Annual Return fields in M&amp;A/Dates screen and 
 Initiate/Report screen, as well as [customising 
 the template](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Coding_a_HTML_Template.htm) for the Entity File Summary screen.

&nbsp;

&nbsp;

See also:

	

- [File Review](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/File_Review_Function.htm)

	

- [Lookup Tables - 
    	 Filing Actions](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Lookup_Tables.htm)


 
&nbsp;

You are here:[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; [File Maintenance](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/File_Maintenance_screen.htm) &gt; [General](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Overview.htm#642b3b9347ca42c9b00b820c00c373fa=1) &gt; [Master File](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/MF_-_Setup.htm) &gt; [Folders](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Mailings.htm) &gt; Filings

 
&nbsp;
 
(c) Viewpoint Software for 
 Business Ltd
 
Version: 8.0.2022.09.20




