



# AEOI Filing Management
This feature retrieves information from Classification and Indicia, 
 Identity Register and Reportable Accounts screens to create Filings that 
 can be exported to efileConnect. Once exported, there will also be a record 
 of the filing in the Filings screen with the Filing’s status is efileConnect. 
 It is available in Viewpoint - Home screen. To access it:

	

- Using Ribbon - Click EA Global Ribbon button, select Global 
    	 Change &gt; Bank/Broker Signatory

	

- Using Section Menu - Click Home &gt; Entity Administration &gt; 
    	 &nbsp;Global Change &gt; Bank/Broker Signatory

This screen consists of two tabs:

	

- Selection tab – This is where user must first filter or select 
    	 the Filing namely by Reporting Authority and Reporting Period. All 
    	 other available fields are optional to filter the results by. It is 
    	 mandatory for a user to complete this screen to see the results and 
    	 begin the Filing export and validation process.

	

- Details tab – Based on <span style="font-family: Helvetica, sans-serif;">the 
    	 </span>parameter(s) selected by user in the Selection tab, the results 
    	 or details of the Filing will be shown accordingly.

&nbsp;

Selection tab

In the selection tab, the following screens can be seen:

	

- Reporting Authority - Select the list of the Reporting Authority. 
    	 This is a mandatory field. This is retrieved from the Jurisdiction 
    	 fields from the CRFI/FRFI record in the classification and indicia 
    	 of the Master File.

	

- Reporting Year - Enter the reporting period date from and date 
    	 to. This is a mandatory field. This creates the filing instance that 
    	 stores the Reporting Periods. efileConnect will match the Reporting 
    	 Period with its Filing Schedule to create the filings.

	

- Client/Group (O) - Select the Client/Group from the list to 
    	 filter and group by the Master Files (Reporting FIs) Client/Group. 
    	 This is an optional field.

	

- Administrator Group (O) - Select the Administrator Group from 
    	 the list to filter and group by the Master Files (Reporting FIs) Administrator. 
    	 This is an optional field.

	

- Organisational Unit (O) - Select the Organisational Unit from 
    	 the list to filter and group by the Master Files (Reporting FIs) Organisational 
    	 Unit. This is an optional field.

	

- Team (O) - Select the Team from the list to filter and group 
    	 by the Master Files (Reporting FIs) Team. This is an optional field.

	

- Sponsor/Trustee (O) - Select the Sponsor/Trustee from the list 
    	 to filter and group by the Master Files (Reporting FIs) Sponsor/ Trustee. 
    	 This is an optional field.

	

- Reporting FI (O) - Select the Reporting FI from the list to 
    	 filter and group by the Master Files (Reporting FIs). This is an optional 
    	 field.

&nbsp;

Checkbox

Group By - Ticking this option enables the Details tab to display records 
 by the selected criteria in checkboxes. This checkbox is ticked by default 
 for Sponsor/Trustee.

&nbsp;

Radio buttons

Select the relevant radio button.

	

- Status - Selecting one of the options enables to filter retrieved 
    	 records by Status such as All, New, Pending or Submitted to Reporting 
    	 Authority.

	

- 
    - 
        		
        
    - All - Able to view all filings and execute Create, Preview 
        		 and Export to efC, however does not execute efC Refresh button. 
        		 Only able to execute Create if the filings have not been created 
        		 in the Filing Instances.
        
        
        		
    - New - Able to view New filings and execute Create, Preview 
        		 and Export to efC, however does not execute efC Refresh button.
        
        
        		
    - Pending - Able to view Pending filings and execute efC Refresh 
        		 button to retrieve new status from efileConnect.
        
        
        		
    - Submitted to Reporting Authority - Able to view Completed 
        		 filings and execute efC Refresh button to retrieve new status 
        		 from efileConnect.
        
        
        	

&nbsp;

Command buttons

Click on the relevant command button to perform the necessary.

	

- <span class="hcp3">Clear Selection</span> - Click 
    	 this to clear the selection in the screen.

	

- <span class="hcp3">&gt;&gt; Retrieve</span> - 
    	 Click this to retrieve all records that meet the criteria in order.

&nbsp;

Details tab

This shows filing data retrieved based on the parameters in the Selection 
 tab. The information is displayed in a grid format with columns showing 
 the total number of items and/or status of the filing process/submission:

	

- No. of RAH - This column displays the number of Reportable Account(s) 
    	 for the group or line.

	

- No. of Balance Reporting(s)/No. of Payment Transaction(s) - 
    	 This column displays the number of Balance Reporting(s) over (‘/’) 
    	 the number of payment transaction(s) for the group or line. This column 
    	 breaks into 3 sub-columns:

	

    - 
        		
        
    - New - This refers to the newly created filing.
        
        
        		
    - Exported to efC - This refers to filing that has been exported 
        		 to efileConnect assigned with a Filing ID, however, yet to be 
        		 marked as Completed.
        
        
        		
    - Completed in efC - This refers to filing that has been exported 
        		 to efileConnect assigned with a Filing ID and marked as Completed.
        
        
        	

	

- efC No. - This column shows the Filing ID number that is created 
    	 in efileConnect.

	

- Status - This column shows the Filing Status of the Filing Instance.

	

- Last Action - This column shows the most recent Filing Action.

	

- Error Message(s) - This column displays the error message when 
    	 there is a ‘Exported with Error’ value in the column ‘Last Action’.

&nbsp;

Command buttons

Click on the relevant command button to perform the necessary. The command 
 buttons can be classified as:

	

- ‘Function/Action’ type – these are actions to apply to the selected 
    	 group(s) or Direct Reporting line within the Direct Reporting Entity 
    	 group.

	

    - 
        		
        
    - <span class="hcp3">Create</span> - This button 
        		 is activated for any new Filing. It is enabled only after any 
        		 of the Reporting FI RFI’s checkbox is ticked. The command button 
        		 will perform the actions as below:
        
        
        		
        - 
            			
            
        - In File Maintenance &gt; Entity Administration &gt; 
            			 Administration &gt; Filings screen:
            
            
            			
            - 
                				
                
            - Create the Filing Type (if it does not exist).
                
                
                				
            - Create the Filing Record or Instances (if it does 
                				 not exist) where Status is 'New'.
                
                
                				
            - Create the first Filing Action 'Ready to Export' 
                				 – if the ‘Last Action’ is empty.
                
                
                			
            
            			
        - Refreshes the AEOI Filing Management &gt; Details tab 
            			 with:
            
            
            			
            - 
                				
                
            - Status set to 'New', if previously empty.
                
                
                				
            - Last Action set to latest Filing Action’s Description.
                
                
                			
            
            		
        
        		
    - <span class="hcp3">Preview</span> - This button 
        		 is activated when an RFI record is selected, where column values 
        		 are:
        
        
        		
        - 
            			
            
        - Status is ‘New’ or ‘Pending’.
            
            
            			
        - Last Action is ‘Ready to Export’.
            
            
            		
        
        		
    - <span class="hcp3">Export to efC</span> - 
        		 This button is activated when there is a Filing created in the 
        		 Filings screen. The conditions are:
        
        
        		
        - 
            			
            
        - If CRS/FATCA template updated the Tag [/Editor.MustPreview=N/], 
            			 then this button is enabled at the same time as ‘Preview’.
            
            
            			
        - If CRS/FATCA template updated the Tag [/Editor.MustPreview=Y/], 
            			 then this button will not be enabled.
            
            
            		
        
        		
    - <span class="hcp3">efC Refresh</span> - This 
        		 button is enabled after user has clicked on ‘Submit’ (in XML Preview 
        		 window) or ‘Export to efC’. Once this button is clicked, the system 
        		 will refresh the selected RFI record with any new validation from 
        		 efileConnect.
        
        
        	

	

- 'Go To' type - These are command buttons to open the relevant 
    	 screen for the selected line.

	

    - 
        		
        
    - <span class="hcp3">Reportable Account -</span> 
        		 will open File Maintenance &gt; [Master File] &gt; AEOI &gt; Reportable 
        		 Accounts.
        
        
        		
    - <span class="hcp3">Filings -</span> will open 
        		 File Maintenance &gt; Entity Administration &gt; Administration 
        		 &gt; Filings.
        
        
        		
    - <span class="hcp3">Classification and Indicia 
        		 -</span> will open File Maintenance &gt; [Master File] &gt; AEOI 
        		 &gt; Classification and Indicia.
        
        
        	

User can select Sponsor or Trustee group(s) or any RFI in the Direct 
 Reporting Entity header by clicking on the checkbox and perform the relevant 
 action via any of the available ‘Function/Action’ buttons.

However, for users to select any line and navigate to the screen via 
 ‘Go To’ button, the related Master File must have access to the screen 
 itself. For example, an Individual Reportable Account Holder [RAH] or 
 Substantial Owner [SOW]/ Controlling Person [CNP] would not have a Filings 
 screen to navigate to.

&nbsp;

See also:

	

- [AEOI Reporting](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/AEOI_Reporting.htm) 

	

- [AEOI Review Tags](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/AEOI_Review_-_Tags.htm)

	

- [Filing Settings](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Filing_Settings.htm)

&nbsp;

You are here:[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; [Viewpoint - Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Overview.htm) &gt; [Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Overview.htm) &gt; [Entity Administration](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Address_Card_Maintenance.htm) &gt; [Global Change](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Administrator/Global_Change.htm) &gt; AEOI Filing Management

&nbsp;

(c) Viewpoint Software for 
 Business Ltd

Version: 8.0.2022.09.20


