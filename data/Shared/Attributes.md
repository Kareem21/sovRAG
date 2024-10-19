



# Attributes
This is to control access to the following:

	

- Reports such as Word reports, Custom reports, Standard reports 
    	 and Excel statements

	

- Correspondence documents

	

- Checklists

	

- Workflows

When an attribute is set up, the items will become available only to 
 the Master File(s) or user(s) specified in the attribute configuration.

&nbsp;
## Attribute Configuration
Configuring the attributes takes place in the Attributes Configuration 
 screen which can be accessed by clicking on the Attributes command button. 
 This command button is located in screens where the items are maintained:

	

- Configuration &gt; Document Libraries &gt; [Word 
    	 Reports](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Word_Reports_Library.htm) and [Correspondence](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Correspondence_Library.htm) 
    	 screens for Word templates for Word reports and Correspondence documents.

	

- Configuration &gt; Business Parameters &gt; Workflow &gt; [Step Library](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Step_Library.htm) screen for checklists.

	

- Configuration &gt; Business Parameters &gt; Workflow &gt; [Workflow Library](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Workflow_Library.htm) screen for workflows.

	

- Configuration &gt; Business Parameters &gt; [Standard 
    	 Reports](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Standard_Reports_Configuration.htm) screen for Standard Reports.

	

- Configuration &gt; Settings &gt; Customise &gt; [Custom 
    	 Reports](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Custom_Reports_Configuration.htm) screen for Custom Reports.

	

- [Excel Statements](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Excel_Statements_-_Design_Statement.htm) 
    	 screen with Design Statement option ticked.

When configuring the attribute, you can specify if the item is to be 
 made available to (use the = operator) or not available to (use the &lt;&gt; 
 operator):

	

- Specific Master File or Master Files - use 'Master File' and 
    	 specify the Master File.

	

- Groups of Master Files - you can choose to make it available 
    	 for Master Files that are:

	

- 
    - 
        		
        
    - Of the same type - use 'Master File - Type' or 'Master File 
        		 - Entity Type' and specify the type.
        
        
        		
    - In the same Administrator Group - &nbsp;use 'Master File 
        		 - Admin Group' &nbsp;and specify the administrator group.
        
        
        		
    - Of a certain status - use 'Master File - Status' and specify 
        		 the status.
        
        
        		
    - Incorporated in a certain jurisdiction - use 'Master File 
        		 - Entity Jurisdiction' and specify the country.
        
        
        		
    - Of the same Organisational Unit - use 'Master File - Organisation 
        		 Unit' and specify the organisational unit.
        
        
        		
    - In the same team - use 'Master File - Team' and specify 
        		 the team.
        
        
        	

	

- Specific user or users - use 'User' and specify the user.

	

- Groups of users - you can choose to make it available to users 
    	 in the same:

	

    - 
        		
        
    - User Group - use 'User - User Group' and specify the group.
        
        
        		
    - Admin Group - use 'User - Admin Group' and specify the administrator 
        		 group.
        
        
        		
    - Organisational Unit - use 'User - Organisation Unit' and 
        		 specify the organisational unit.
        
        
        		
    - Access Group - use 'User - Access Group' and specify the 
        		 access group. 
        
        
        	

When you have more than one type of attribute set up, the condition 
 'OR' is applied if they are the same category

e.g.

Master File - Type = Company

Master File - Type = Trust

means the item will be available to Master Files of the type 'Company' 
 or 'Trust'. The item will not be available for Master Files that are not 
 of either type.

&nbsp;

Master File - Type = Company

Master File - Admin Group = GROUP1

means the item will be available to Master Files of the type 'Company' 
 or Master Files in the GROUP1 administrator group.

&nbsp;

User = ANNE

User = SM

means the item will be available to the user with the code 'ANNE' or 
 'SM'. Other users will not be able to see the item.

&nbsp;

If the attribute type is of different category, then the condition 'AND' 
 is applied

e.g.

Master File - Admin Group = GROUP1

User - User Group = Managers

means the item will be available to users in the User Group 'Managers' 
 for Master Files in the GROUP1 administrator group only.

&nbsp;

<span style="font-weight: bold; font-style: italic;">Note</span>: For 
 workflows that are published to Engage Servicing Portal, only attributes 
 based on Master File parameters are applicable. For attribute based on 
 user parameters, this is only restricted to the ESP Common User i.e. the 
 user ID used for authenticating communication between ESP and Viewpoint 
 Back Office.

&nbsp;
### Attributes Configuration Screen
This is where the attributes are set up for the selected item.

&nbsp;

Master File Attributes list

This shows all the Master File attributes that have been set up. To 
 add a new one, click to select the type of attribute and specify the value. 
 Click Update to save the attribute.

&nbsp;

User Attributes list

This shows all the user attributes that have been set up. To add a new 
 one, click to select the type of attribute and specify the value. Click 
 Update to save the attribute.

&nbsp;

Command buttons

Click on the relevant command button to perform the necessary.

	

- <span class="hcp4">Copy</span> - Click this to 
    	 copy all attributes that have been set up.

	

- <span class="hcp4">Paste</span> - Click this to 
    	 paste attributes that you have copied.

	

- <span class="hcp4">Update</span> - Click this 
    	 to save changes to the attribute setup.

	

- <span class="hcp4">Delete</span> - Click this 
    	 to remove a selected attribute type.

	

- <span class="hcp4">Close/Cancel</span> - Click 
    	 Close to exit the screen. Click Cancel to cancel any changes made.

&nbsp;

[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; Attributes

&nbsp;

(c) Viewpoint Software for 
 Business Ltd

Version: 8.0.2022.09.20


