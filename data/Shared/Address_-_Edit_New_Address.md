




# Edit/New Address
This tab can be accessed from the List or List/Link tab by clicking: 
 

	

- New to create a new address card - address details that you 
    	 have entered in the Find Address tab when you perform a search will 
    	 be available. If the details are complete, you can click Update.

	

- Edit to edit details of an existing address card - address details 
    	 of the selected address card will be displayed. Once you have made 
    	 the necessary changes, you can click Update.

&nbsp;

Command buttons

Click on the relevant command button to perform the necessary.

	

- Copy <span class="hcp3">- 
    	 Click this to copy the address details to Windows Clipboard. This 
    	 allows you to paste the address details to external location like 
    	 Notepad, MS Word or your e-mail message.</span>

	

- Update <span class="hcp3">- 
    	 Click this to</span> <span class="dropspot" style="font-weight: normal;">save 
    	 the information added to the Address Card.</span>

	

- Cancel - <span class="hcp3">Click 
    	 this to cancel changes made to the Address Card.</span>

	

- Access - <span class="hcp3">Click 
    	 this</span> <span class="hcp3">[view 
    	 or give more access](javascript:TextPopup(this)) to the encrypted Address Card. 
    	 This is seen when you have [confidential 
    	 database](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Confidential_Database.htm) set up.</span>
    
    	<div class="droptext" id="POPUP403662285" style="display: none;">
    		This opens the Access Authorities 
    		 screen where access to the encrypted Master File/Address Card 
    		 can be given to groups of users or specific users.
    		&nbsp;
    		Give 
    		 Access to Groups of Users
    		This is to give access to multiple 
    		 users that belong to a certain group such as User Group or Administrator 
    		 Group.
    		
        			    1. Select All, User Groups 
        			 or Admin Groups as the filter.
        			    1. Click to select the group 
        			 from the list.
        			    1. Click Add &gt;&gt;&gt;.
        			    1. The selection will be added 
        			 to the grid on the right.
        		
    		&nbsp;
    		Give 
    		 Access to Selected User
    		This is to give access to specific 
    		 users. This can be users that belong to different groups.
    		
        			    1. Select the relevant group 
        			 as the filter, e.g. Administrators.
        			    1. Click to select the user 
        			 from the list.
        			    1. Click Add&gt;&gt;&gt;.
        			    1. The selection will be added 
        			 to the grid on the right.
        		
    		&nbsp;
    		Revoke 
    		 Access
    		You can revoke access to the encrypted 
    		 Master File/Address Card by clicking to select the group/user 
    		 from the grid on the right and clicking Delete.
     </div>

	

- Close - <span class="hcp3">Click 
    	 this to exit the Address Card Master screen.</span>

	

- Make as Global Address Card <span class="hcp3">- This is only seen in the Master Configuration 
    	 environment i.e. the 'Set as Master Configuration database' is ticked 
    	 in System Defaults &gt; Configuration Management. Click this to convert 
    	 the Address Card to a Global Address Card which allows the Address 
    	 Card to be replicated in subscriber environments but without any editing 
    	 abilities. Global Address Cards can only be updated in the Master 
    	 Configuration environment. Once converted to Global Address Card, 
    	 the command button will no longer be available and it is not possible 
    	 to reverse the process. For more details on Master Configuration environment, 
    	 refer to [Master Configuration Environment 
    	 (MCE) and Data Replication](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Master_Configuration_Environment_and_Data_Replication.htm).</span>

	

&nbsp;
## Create New Address Card
New Address Cards can be created by entering the details manually or 
 by copying from an existing Address Card.

&nbsp;
### Create New Address Card Manually

	

1. Enter the details for the address card:
    
    	
        		
        
    - Local Address - If you have turned on local address feature, 
        		 you will see this field and additional text boxes for all the 
        		 address fields. The options available are set up in the Address 
        		 Local Setting [ADLS] [lookup 
        		 table](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Lookup_Tables.htm) in Configuration &gt; Business Parameters &gt; General 
        		 &gt; Lookup Values. If you select 'Not Required' or 'Same as Main 
        		 Address', the duplicate text boxes for the address fields will 
        		 not be active.
        
        
        		
    - Country - The country selection will determine the Postal 
        		 Code placement as set up in the Country Codes [CNTR] lookup table 
        		 in Configuration &gt; Business Parameters &gt; General &gt; Lookup 
        		 Values.
        
        
        		
    - Region/State - If the region or state already exists in 
        		 the database, you can select it from the list. If not, type in 
        		 the new one.
        
        
        		
    - City - If the city already exists in the database, you can 
        		 select it from the list. If not, type in the new one.
        
        
        		
    - Address Format - This is seen if an address format has been 
        		 set up for the selected country code. The format is set up using 
        		 [ACF] tag in Country Codes [CNTR] [lookup 
        		 table](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Lookup_Tables.htm).
        
        
        		
    - Address - Enter the address details. If an address format 
        		 is used, each address line may have its own caption as predefined 
        		 for the format.
        
        
        		
    - Postcode [PC] - Enter the postal code.
        
        
        		
    - Postcode options - This determines the placement of the 
        		 postcode within the address. You can specify a [default 
        		 postcode option](javascript:TextPopup(this)) for a country through the 
        		 &nbsp;Country Codes [CNTR] [lookup 
        		 table](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Lookup_Tables.htm).  
        &#13;&#10;		For 'CRC Address [PC]' option, this will format the address in 
        		 one line without any separation (comma, space or line return) 
        		 in between the information.
        
        		<div class="droptext" id="POPUP346227542" style="display: none;">
        			
            				        1. In Configuration &gt; Business Parameters &gt; General 
            				 &gt; Lookup Values, select Country Codes [CNTR].
            				        1. Select the country code.
            				        1. Click Edit.
            				        1. Specify the postcode option for the country by selecting 
            				 the appropriate option for Postcode Format field.
            				        1. Click Update.
            			
          </div>
        
        		
    - Address flags - Tick if there are any flags to be set on 
        		 the address being created. Ensure the Active check box is ticked 
        		 to enable the address to be used.
        
        
        		
        - 
            			
            
        - Statutory - This flags the address as a statutory address.
            
            
            			
        - Confidential - This flags the address as confidential 
            			 and will be hidden from users without the proper authority.
            
            
            			
        - Restricted - Editing of these addresses is restricted 
            			 to users with the proper authority only.
            
            
            			
        - Active - This flags the address as active address. Inactivate 
            			 addresses that you do not want to use by removing the tick.
            
            
            			
        - Encrypt - This appears only if you are connected to 
            			 a [confidential database](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Confidential_Database.htm). 
            			 Tick this if you want to encrypt to address details. You need 
            			 authority level 8 - Power User to have access to this option.
            
            
            		
        
        		
    - Description - Enter a description of the address, if applicable. 
        		 This can help you to identify the address during a search.
        
        
        		
    - Address No. - This is a system-assigned number given to 
        		 the address.
        
        
        	

	

1. Click Update.

<span class="hcp9">Note</span>: You 
 can specify which address card and local address details are mandatory 
 using the [AFMAN] tag in Country Codes [CNTR] [lookup 
 table](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Lookup_Tables.htm).

&nbsp;
### Create New Address Card using Copy
This is to allow you to copy an existing Address Card details to a new 
 Address Card and amend accordingly.

For example, if you have an existing Address Card with the following 
 details:

	

- Address - 9 Coutts House, Summerhill Road

	

- City - Onchan

	

- Postcode - IM31Nw IM3

	

- Country - Isle of Man

and you want to create a new Address Card with the following details:

	

- Address - 11 Coutts House, Summerhill Road

	

- City - Onchan

	

- Postcode - IM31Nw IM3

	

- Country - Isle of Man

To do this, use the Copy function.

	

1. In Address Card Master, search for the existing Address Card 
    	 with similar address details.

	

1. In List/Link, click to select the Address Card.

	

1. Click Copy.

	

1. In Edit/Address, make the changes.

	

1. Click Update.

&nbsp;
## Edit Existing Address Card
This should only be used to correct the address details of an address 
 card.

&nbsp;
### Edit in File Maintenance screen:

	

1. Click General &gt; Addresses or Entity Administration &gt; Statutory.

	

1. Select the address you want to edit.

	

1. Click Edit.

	

1. Click OK.

	

1. Click Edit/New Address.

	

1. Make the necessary change.

	

1. Click Update.

### Edit in Viewpoint - Home screen:

	

1. Click Administrator &gt; Address Card Maintenance.

	

1. Click Find Address and enter search criteria.

	

1. Click Find.

	

1. In List, select the address card you want to edit.

	

1. Click Edit.

	

1. Make the necessary change.

	

1. Click Update.

&nbsp;
## Assigning Access to Address in Confidential Database
To assign access to the address in Confidential Database, user must 
 first connects to the Confidential Database and tick the option 'Encrypt' 
 in the Edit/New Address screen.

	

1. Click Access. This will launch the Access Authorities window 
    	 for that selected Address.

	

1. The User/Group of the login user will be granted with User Access 
    	 Rights to the Address by default.
    
    	
        		
        
    - To assign user, select the user/group from the Group/User 
        		 Listing and click Add&gt;&gt;&gt;.
        
        
        		
    - To unassign user, select the user/group from the Groups/Users 
        		 Access Rights and click Delete.
        
        
        	

&nbsp;
## Set Address Card as Global Address Card
This setting is applicable only in Master Configuration database. The 
 button&nbsp;'Make as Global Address Card' is visible when the 'Set as 
 Master Configuration database' option is ticked in Configuration &gt; 
 Settings &gt; System Defaults &gt; Configuration Management screen. Once 
 enabled, the system will disallow user from editing the Address Card from 
 the Subscriber's environment. This button will disappear after the Address 
 Card is enabled as Global Address Card.

<span class="hcp9">Note</span><span>: 
 'Make as Global Address Card' action cannot be undone.</span>

&nbsp;

See also:

	

- [Local Address Card](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Local_Address_Card.htm)

	

- [Address Card Maintenance](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Address_Card_Maintenance.htm)

	

- [Addresses](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Addresses.htm)


  
&nbsp;

[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; Edit/New Address
  
&nbsp;
  
(c) Viewpoint Software for 
 Business Ltd
  
Version: 8.0.2022.09.20


 

