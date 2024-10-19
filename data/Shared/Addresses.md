




# <span class="Bold">Addresses</span>
This screen is for you to enter, review and maintain correspondence 
 as well as communication details.

&nbsp;

Address Type

This allows you to:

	

- View and create address links to the Master File - select Master 
    	 File Addresses.

	

- View statutory locations linked to the Entity File - select 
    	 Statutory Address/Location.

	

- View both addresses and statutory locations - select All.

<span class="hcp2">Note:</span> New 
 addresses can be added if the one you want to use does not already exist 
 in the system. It is advisable to check the Address Cards for an address 
 first, before you proceed to create a new one.

&nbsp;

Current / Past / All

Select if you want to see only current address, past address or all.

&nbsp;

Addresses List

The address list displays addresses that are linked to a Master File. 
 New addresses can be added if the one you want to use does not already 
 exist in the system. It is advisable to check the Address Cards for an 
 address first, before you proceed to create a new one.

&nbsp;

Command buttons

Click on the relevant command button to perform the necessary.

	

- <span class="hcp3">New -</span> Click to [add](javascript:TextPopup(this)) 
    	 new address link to the Master File.
    
    	<div class="droptext" id="POPUP193468205" style="display: none;">
    		
        			    1. In the Address Card Master, you can either:
        			
            				        - [Search for 
            				 an existing address card in Find Address](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Address_-_Find_Address.htm); or
            				        - [Enter new 
            				 address card in Edit/New Address](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Address_-_Edit_New_Address.htm)
            			
        			    1. Tick the address type in List/Link.
        			    1. Click OK.
        			    1. Click Update.
        		
    		&nbsp;
     </div>

	

- <span class="hcp3">Edit</span> - Click to [edit](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Address_-_Edit_New_Address.htm) a selected 
    	 address card.

	

- <span class="hcp3">Delete</span> - Click to [delete](javascript:TextPopup(this)) 
    	 the selected address link. The Address Card will not be deleted from 
    	 the database, only the link to the Master File is removed.
    
    	<div class="droptext" id="POPUP193460910" style="display: none;">
    		Click Yes to confirm.
    		&nbsp;
     </div>

	

- <span class="hcp3">Change</span> - Click to change 
    	 the selected address link. The Address Card Master screen will appear 
    	 for you to select a new address card and to complete the effective 
    	 date. The existing address link record will be deactivated, and the 
    	 From date will be filled in with the effective date of the change. 
    	 The effective date of the address change will affect the address displayed 
    	 on forms and reports, i.e. if the date of the address change is after 
    	 a particular change, the generated form will display the previous 
    	 address.

	

- <span class="hcp3">Undo</span> - Click to undo 
    	 ALL changes made to the address card links before you click the Update 
    	 button.

<span class="hcp2">Note</span>: If 
 you add or change address types with codes that start with 'R' or 'S' 
 &nbsp;for a Master File which acts as an officer for an entity, you will 
 be prompted to file the changes. If the option 'Trigger Global Change 
 of Particular for Shareholders' in System Defaults &gt; Entity/Forms is 
 enabled, then this prompt is also seen if the Master File is a shareholder.

&nbsp;

Contact Details

Contact details for the Master File are entered here.

&nbsp;

Command buttons

Click on the relevant command button to perform the necessary.

	

- <span class="hcp3">New -</span> Click to [add](javascript:TextPopup(this)) 
    	 new contact details.
    
    	<div class="droptext" id="POPUP193472721" style="display: none;">
    		
        			    1. Once you have clicked New, select the contact detail 
        			 type.
        			    1. Select the country value, if applicable.
        			    1. Enter the details in Number/E-mail column.
        			    1. Enter the 'From' date, 'To' date, and Remark if applicable. 
        			 The 'From' date and 'To' date will determine if the contact 
        			 is 'Active' or 'Inactive' by comparing against the current 
        			 date. If the current date is within the 'From' date and 'To' 
        			 date range, it will be classified as 'Active'.
        			    1. Click Update.
        		
    		<span class="hcp2">Note:</span> 
    		 User is allowed to create a same contact type only when the existing 
    		 contact type has been deactivated (the current date is not within 
    		 the 'To' date and 'From' date range).
    		&nbsp;
     </div>

	

- <span class="hcp3">Delete</span> - Click to [delete](javascript:TextPopup(this)) 
    	 the selected contact details.
    
    	<div class="droptext" id="POPUP193443652" style="display: none;">
    		Click Yes to confirm.
    		&nbsp;
     </div>

	

- <span class="hcp3">Undo</span> 
    	 - Click to undo any changes made.

	

- <span class="hcp3">Update</span> 
    	 - Click to update any changes made.

The Viewpoint Clipboard function also works on the contact details that 
 have been entered, allowing the information to be copied from one Master 
 File to another Master File. Note that this applies only to the Number/E-mail 
 column.

If a format mask has been set up for the contact detail type in Contact 
 Types [ADRC] lookup table, the format mask will also be applied so that 
 the value copied and pasted follows the format mask.

&nbsp;

[Can I make country 
 mandatory for telephone numbers?](javascript:TextPopup(this))
 
<div class="droptext" id="POPUP484845873" style="display: none;">
	

Yes, this is possible. Enter the [REQCNTR=Y] tag for the contact 
	 type in Contact Types [ADRC] lookup table.

	

&nbsp;
 </div>

[How do I set 
 the country calling code?](javascript:TextPopup(this))
 
<div class="droptext" id="POPUP483810509" style="display: none;">
	

This is done using the [TELPREFIX=&lt;Code&gt;] tag in the Country 
	 Codes [CNTR] lookup table.

	

&nbsp;
 </div>

&nbsp;

&nbsp;

See also:

	

- [Statutory 
    	 - Company](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Administrator/Statutory_-_Company.htm)

	

- [Address Card Maintenance](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Address_Card_Maintenance.htm)

	

- [Viewpoint Clipboard](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Viewpoint_Clipboard.htm)

	

- [Contacts 
    	 Cleanup](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Contact_Global_Cleanup.htm)


 
&nbsp;

You are here:[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; [File Maintenance](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/File_Maintenance_screen.htm) &gt; [General](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Overview.htm#642b3b9347ca42c9b00b820c00c373fa=1) &gt; [Master File](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/MF_-_Setup.htm) &gt; [Master File](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/MF_-_Setup.htm) &gt; Addresses
 
&nbsp;
 
(c) Viewpoint Software for 
 Business Ltd
 
Version: 8.0.2022.09.20




