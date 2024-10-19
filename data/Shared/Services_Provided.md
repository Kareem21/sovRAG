




# Services Provided
This screen is required for security model 5 - Services Provided Model 
 [5] to control screen access for the Master File. It shows the services 
 for the Master File and this determines the screen access rights for the 
 Master File. The services are created in User Roles [URLS] lookup table 
 where 'SP' is included in the Electronic Filing Code field. 

By default, this screen is not active but can be activated by running 
 the Enable Services Provided Model localise script. The script will do 
 the following:

	

- enable Services Provided screen

	

- deactivate Group Access ‘Files where Administrator [1]’ and 
    	 ‘Files where Administrator, in Group + Group Member [3]’ in User setup 
    	 as these do not apply security model 5

After running the localise script, ensure that you do the following: 
 

	

- in Windows Menu screen, tick the User Group Authority option 
    	 for the screen

	

- assign access to the screen for the relevant User Role so that 
    	 the relevant user will be able to add the services for the Master 
    	 File

&nbsp;

Status

Select the Service status 'Active', 'Inactive' or 'All'. 

&nbsp;

Command buttons

These apply to the Services Provided list. Click on the relevant command 
 buttons to perform the necessary.

	

- <span class="hcp2">New</span> - Click this to 
    	 [add](javascript:TextPopup(this)) 
    	 a new Service.
    
    	<div class="droptext" id="POPUP41325759911" style="display: none;">
    		
        			    1. Enter the details of the new Service.
        			    1. Click Update to save the changes.
        		
     </div>

	

- <span class="hcp2">Edit</span> - Click this to 
    	 edit the selected Service.

	

- <span class="hcp2">Deactivate </span>- Click this 
    	 to deactivate the selected Service.

	

- <span class="hcp2">Delete</span> - Click this 
    	 to [delete](javascript:TextPopup(this)) 
    	 the selected Service.
    
    	<div class="droptext" id="POPUP41327738911" style="display: none;">
    		Click Yes to confirm the deletion.
     </div>

Service List

This lists all available Services based on the status selected. For 
 new Master Files, there will be a default record where the Administrator 
 Group is the same as the Administrator Group in the Setup screen, but 
 without any service defined.

&nbsp;

&nbsp;

See also:

	

- [Security Models](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Security_Models.htm)

	

- [Administrator 
    	 Groups](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Administrator_Groups.htm)


 
&nbsp;

You are here:[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; [File Maintenance](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/File_Maintenance_screen.htm) &gt; [General](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Overview.htm#642b3b9347ca42c9b00b820c00c373fa=1) &gt; [Master File](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/MF_-_Setup.htm) &gt; [Master File](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/MF_-_Setup.htm) &gt; Services Provided
 
&nbsp;
 
(c) Viewpoint Software for 
 Business Ltd
 
Version: 8.0.2022.09.20




