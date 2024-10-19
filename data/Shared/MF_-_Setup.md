




# <span class="Bold">Setup</span>
<span class="Bold">In the New Master File wizard, this is the first 
 tab as it requires basic information of the Master File such as the activities 
 and roles of a particular individual or entity. Once the Master File has 
 been created, this then is shown as the Setup screen. Information entered 
 earlier can be amended in the screen, if necessary. Among these information 
 are:</span>

&nbsp;

Master File Type

When creating a new Master File, you must specify if the Master File 
 is for an individual or non-individual. This determines the fields that 
 you see for the other sections. You can add more Master File types in 
 the Master File Types [ADTP] lookup value table in Configuration &gt; 
 Business Parameters &gt; General &gt; Lookup Values.

&nbsp;

Entity Name/Surname

This is the Master File name. If the Master File is for an individual, 
 then this is one part of the Master File name.

&nbsp;

Administrator Group

If you would like to control access to the Master File, then you need 
 to ensure that the right Administrator Group is assigned to the Master 
 File. This works for all security models with the exception of Security 
 Model 1 which does not allow selective access to Master Files.

&nbsp;

Components Activated

The options here indicate the components where the Master File will 
 be accessible.

	

- Entity Administration - Tick this if the Master File is a managed 
    	 entity.

	

- Time &amp; Billing (Sales Ledger) - Tick this if you want to 
    	 record time and prepare invoices for the Master File.

	

- Supplier (Purchase Ledger) - Tick this if you want to prepare 
    	 purchase orders for the Master File.

	

- Accounting - Tick this to enter accounting journals for the 
    	 Master File.

&nbsp;

Required to Complete

The options here give you access to the following screens:

	

- Identity Register

	

- Identity Details

	

- CDD

&nbsp;

Roles Allowed

The options here determine whether or not the Master File can be selected 
 for a specific role.

&nbsp;

Relationship Roles Allowed

This is seen only if the Enable detailed 'Relationship Roles' option 
 is ticked in [System 
 Defaults &gt; General/Master File](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/System_Defaults_-_General_Master_File.htm) and works with the following options 
 in Roles Allowed:

	

- Statutory/Trust/Foundation Officer

	

- Relation

When this is in use, you need to select the relationship types for the 
 Master File. Otherwise, it is sufficient to just tick Statutory/Trust 
 Officer and/or Relation for the Master File in Roles Allowed.

&nbsp;

Confidential Master File

The option seen here is to specify whether or not the Master File is 
 encrypted with the actual information sent to the [confidential 
 database](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Confidential_Database.htm). It is not available if there is no confidential database 
 set up or when you are not connected to the confidential database.

To connect to confidential database, go to [User 
 Options](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/User_Options.htm); to encrypt a Master File, go to Setup of the Master File 
 that you wish to encrypt.

&nbsp;

Command buttons

Click on the relevant command button to perform the necessary.

	

- <span class="hcp2">Update</span> - Click this 
    	 to update the changes made.

	

- <span class="hcp2">Cancel</span> - Click this 
    	 to cancel the changes.

	

- <span class="hcp2">Access</span> - Click this 
    	 to [view or 
    	 give other users access](javascript:TextPopup(this)) to the encrypted Master 
    	 File. This requires the user to be connected to the confidential database 
    	 and the Master File to be encrypted, i.e. the option 'Confidential 
    	 Master File' is ticked.
    
    	<div class="droptext" id="POPUP403662285" style="display: none;">
    		This opens the Access Authorities screen where access to the 
    		 encrypted Master File/Address Card can be given to groups of users 
    		 or specific users.
    		&nbsp;
    		Give 
    		 Access to Groups of Users
    		This is to give access to multiple users that belong to a certain 
    		 group such as User Group or Administrator Group.
    		
        			    1. Select All, User Groups or Admin Groups as the filter.
        			    1. Click to select the group from the list.
        			    1. Click Add &gt;&gt;&gt;.
        			    1. The selection will be added to the grid on the right.
        		
    		&nbsp;
    		Give 
    		 Access to Selected User
    		This is to give access to specific users. This can be users 
    		 that belong to different groups.
    		
        			    1. Select the relevant group as the filter, e.g. Administrators.
        			    1. Click to select the user from the list.
        			    1. Click Add &gt;&gt;&gt;.
        			    1. The selection will be added to the grid on the right.
        		
    		&nbsp;
    		Revoke 
    		 Access
    		You can revoke access to the encrypted Master File/Address Card 
    		 by clicking to select the group/user from the grid on the right 
    		 and clicking Delete.
     </div>

	

- <span class="hcp2">Make as Global Master File</span> 
    	 - This is only seen in the Master Configuration environment, i.e. 
    	 the 'Set as Master Configuration database' is ticked in [System 
    	 Defaults &gt; Configuration Management](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/System_Defaults_-_Configuration_Management.htm). Click this to convert 
    	 the Master File to a Global Master File which allows the Master File 
    	 to be replicated in subscriber environments but without any editing 
    	 abilities. Global Master Files can only be updated in the Master Configuration 
    	 environment. Once converted to Global Master File, the command button 
    	 will no longer be available and it is not possible to reverse the 
    	 process. For more details on Master Configuration environment, refer 
    	 to [Master 
    	 Configuration Environment (MCE) and Data Replication](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Master_Configuration_Environment_and_Data_Replication.htm).

&nbsp;

See also:

	

- [New Master File](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/New_Master_File.htm)


 
&nbsp;

You are here:[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; [File Maintenance](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/File_Maintenance_screen.htm) &gt; [General](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Overview.htm#642b3b9347ca42c9b00b820c00c373fa=1) &gt; [Master File]() &gt; [Master File]() &gt; Setup
 
&nbsp;
 
(c) Viewpoint Software for 
 Business Ltd
 
Version: 8.0.2022.09.20




