




# Safe Custody Register
The Safe Custody Register can be used to record the location of all 
 documents that are relevant to a particular Master File. The movements 
 of these documents can also be recorded so that the whereabouts of a document 
 at any time is known, making it easier for you to locate it when you need 
 to retrieve it. If you are also using Document Management, documents that 
 are stored there can be linked to the Safe Custody Register.

You can access Safe Custody Register in File Maintenance screen by clicking 
 General &gt; Master File &gt; Folders &gt; Safe Custody Register.

There are two sections in this screen and you can click on:

	

- ![](../image307.gif) 
    	 - To minimise this section and hide the command buttons. In the grid, 
    	 only the selected row will be seen.

	

- ![](../image308.gif) 
    	 - To expand the section and show the command buttons.

Filters

The filters apply to the Safe Custody Item list:

	

- Category - You can filter by the category. The categories are 
    	 maintained in Documents Categories [DCAT] lookup table.

	

- Document Type - You can use the filter by the document type. 
    	 The types are maintained in Document Types [DCMT] lookup table.

&nbsp;

Safe Custody Register Document List

This shows all Safe Custody Register documents that you have entered 
 for the Master File.

&nbsp;

Command buttons

Click on the relevant command button to perform the necessary. The buttons 
 apply to the Safe Custody Register Document list.

	

- <span class="hcp3">New</span> - Click this to 
    	 [add](javascript:TextPopup(this)) 
    	 a new safe custody register entry. You can [configure 
    	 running number for Safe Custody Register](javascript:TextPopup(this)). This 
    	 will increase the document number automatically.
    
    	<div class="droptext" id="POPUP560005735" style="display: none;">
    		&nbsp;Follow the below steps to configure the running number:
    		
        			    1. Click Configuration &gt; Business Parameters &gt; General 
        			 &gt; Lookup Values and locate the Document Number Codes [DOCT] 
        			 lookup table.
        			    1. Create a new lookup value to be used as the document 
        			 number, if none exists. Take note of the code you are using.
        			    1. Once this is done, go to Settings &gt; Customise &gt; 
        			 System Running Numbers.
        			    1. Create a new record using the lookup value created in 
        			 step(2).
        			    1. Go to Settings &gt; Customise &gt; Field Settings.
        			    1. Select the Menu Group 'File [8]'.
        			    1. Select the Section 'General [FTDMAINF]'.
        			    1. Click Find.
        			    1. Select 'Safe Custody Register' and click Select.
        			    1. Select the Document No. field from the list and click 
        			 Edit.
        			    1. In the Default field, enter REF:XX, where XX is the 
        			 code you used in step(2).
        			    1. Tick the Customised checkbox.
        			    1. Click Update.
        		
     </div>
    	<div class="droptext" id="POPUP365414967" style="display: none;">
    		
        			    1. Enter the other details of the record.
        			    1. Click Update.
        		
     </div>

	

- <span class="hcp3">Edit</span> - Click this to 
    	 edit the details of the record including the Date Cancelled.

	

- <span class="hcp3">Cancel</span> - Click to cancel 
    	 an entry. You may do this if the document is no longer valid; for 
    	 instance, if an agreement or passport has expired and is superseded 
    	 by a newer version. Cancelled entries will still be listed in the 
    	 safe custody register. Remember to update any linked document holders.

	

- <span class="hcp3">Delete</span> - Click to delete 
    	 an entry.

&nbsp;

Movement Record

The Movement Record helps you keep track of the location of the physical 
 Safe Custody Register documents.

&nbsp;

Command buttons

Click on the relevant command button to perform the necessary. The buttons 
 apply to the Movement Record.

	

- <span class="hcp3">New</span> - Click this to 
    	 [add](javascript:TextPopup(this)) 
    	 a new movement.
    
    	<div class="droptext" id="POPUP365132058" style="display: none;">
    		
        			    1. Enter the information required on the 
        			 movement.
        			    1. Click Update.
        		
     </div>

	

- <span class="hcp3">Edit</span> - Click this to 
    	 edit a movement record.

	

- <span class="hcp3">Delete</span> - Click this 
    	 to delete a movement record.


 
&nbsp;

You are here:[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; [File Maintenance](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/File_Maintenance_screen.htm) &gt; [General](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Overview.htm#642b3b9347ca42c9b00b820c00c373fa=1) &gt; [Master File](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/MF_-_Setup.htm) &gt; [Folders](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Mailings.htm) &gt; Safe Custody Register
 
&nbsp;
 
(c) Viewpoint Software for 
 Business Ltd
 
Version: 8.0.2022.09.20




