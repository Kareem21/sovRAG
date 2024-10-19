




# Workflow Library
All workflow templates are maintained in this screen and includes also 
 requests in Viewpoint Engage. When setting up workflow templates as Viewpoint 
 Engage requests, ensure that:

	

- The workflow template is published to Viewpoint Engage - in 
    	 the workflow template properties, select either 'Publish [PS]' or 
    	 'ESP Only [PO]' for ESP Publishing field. If set to 'Publish [PS]', 
    	 then the workflow template can be started in both Viewpoint Connect 
    	 and Engage.

	

- Workflow steps for Viewpoint Engage are set correctly - in the 
    	 workflow step properties, select the applicable option for the ESP 
    	 Publish Option field:

	

- 
    - 
        		
        
    - Action [2] - this displays the step and makes the step actionable 
        		 in Viewpoint Engage.
        
        
        		
    - Don't show [4] - this hides the step in Viewpoint Engage.
        
        
        		
    - Show [1] - this displays the step in Viewpoint Engage as 
        		 read-only.
        
        
        	

&nbsp;

Filter

The filter applies to the workflow template list.

&nbsp;

Workflow template list

This is a list the existing workflow templates.

&nbsp;

Command buttons

Click on the relevant command button to perform the necessary.

	

- <span class="hcp2">New</span> - Click this to 
    	 [create](javascript:TextPopup(this)) 
    	 a new workflow template.
    
    	<div class="droptext" id="POPUP405854980" style="display: none;">
    		
        			    1. Enter the details for the workflow template record. 
        			 For more information, refer to [Workflow 
        			 Creation](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Workflow_Creation.htm).
        			    1. Click Update.
        			    1. Click Edit with Workflow Designer to define the workflow 
        			 design.
        		
     </div>

	

- <span class="hcp2">Edit</span> - Click this to 
    	 edit properties of the selected workflow template.

	

- <span class="hcp2">Delete</span> - Click this 
    	 to delete the selected template.

	

- <span class="hcp2">Copy</span> - Click this to 
    	 [copy](javascript:TextPopup(this)) 
    	 the selected template.
    
    	<div class="droptext" id="POPUP587396527" style="display: none;">
    		Workflow templates can be duplicated with a new default auto-incremental 
    		 key and description. All the workflow details, workflow steps, 
    		 step properties and workflow diagram in the original template 
    		 will be copied to the duplicate template. Users can also break 
    		 the dependencies between the workflow steps to duplicate the steps 
    		 with a new step key for each of them.
    		
        			    1. <span>In 
        			 </span><span class="hcp2">Configuration &gt; 
        			 Business Parameters &gt; Workflow &gt; Workflow Library</span><span>, 
        			 select the workflow template from the list.</span>
        			    1. <span>Click 
        			 </span><span class="hcp2">Copy</span><span>.</span>
        			    1. Enter 
        			 a new description.
        			    1. <span>Click 
        			 </span><span class="hcp2">Update</span><span>.</span>
        			    1. <span>In 
        			 the Dependencies pop-up screen, select the workflow steps 
        			 that you wish to duplicate.</span>
        			    1. <span>Click 
        			 </span><span class="hcp2">Break Dependency</span><span>.</span>
        			    1. <span>Click 
        			 </span><span class="hcp2">Close</span><span> 
        			 when completed.</span>
        		
     </div>

	

- <span class="hcp2">Edit with Workflow Designer</span> 
    	 - Click this to open the [Workflow 
    	 Designer](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Workflow_Designer_Screen.htm) screen. This allows you to make changes to the workflow 
    	 template.

	

- <span class="hcp2">Verify</span> - Click this 
    	 to [verify](javascript:TextPopup(this)) 
    	 on the setup of the selected workflow template. 
    
    	<div class="droptext" id="POPUP597923223" style="display: none;">
    		The verification is similar to the one in Step Library except 
    		 that now it is for the whole workflow and includes checking:
    		
        			    - The workflow record being assigned a Key.
        			    - The workflow steps are defined correctly
        			    - The workflow steps with invalid configurations are updated 
        			 correctly. 
        			    - The workflow steps complexity level
        			    - The OUTPUT tag for decision step is assigned with a 
        			 valid key.
        			    - Tags that are used to:
        			
            				    - 
        - Update workflow step caption/description with information 
            				 from step item.
            				    - 
        - Specify Rating Group.
            				    - 
        - Display scores.
            				    - 
        - Show help texts.
            				    - 
        - Retrieve checklist items from a linked workflow 
            				 to the main workflow.
            				    - 
        - Copy information from an earlier workflow step.
            				    - 
        - Perform automatic copy function using Clipboard.
            				    - 
        - Filter Master Files defined in the field type 'Master 
            				 File'.
            				    - 
        - Show certain items under certain condition.
            				    - 
        - Link documents automatically to document holder 
            				 when a document is stored.
            				    - 
        - Retrieve information for more than one instance.
            				    - 
        - Specify the record for screen shortcut for field 
            				 type 'Go to Screen'.
            				    - 
        - Specify details for invoice creation using workflow.
            				    - 
        - Specify details for the field type 'Input Field'.
            				    - 
        - Perform Macros.
            				    - 
        - Update &nbsp;User Fields with checklist item’s value 
            				 or score.
            				    - 
        - Transfer linked items to a new Master File.
            				    - 
        - Define the formula for calculating scores or values.
            				    - 
        - Define the details for field types ‘Yes/No’, ‘Lookup 
            				 Value’ and ‘User Table’.
            				    - 
        - Specify the scope of File Review.
            				    - 
        - Configure the Key Code and Change Code for Change 
            				 Link.
            			
        		
    		<span class="hcp2">Note:</span> Verification can 
    		 also be done by clicking the Verify button in the Ribbon in Workflow 
    		 Designer Screen. 
    		&nbsp;
    		Command Button in Verify Window
    		Click on the relevant command button to perform the necessary.
    		
        			    - <span class="hcp2">Find and Replace</span> 
        			 - Click this to find and replace invalid configurations in 
        			 the workflow steps.
        		
    		
        			
            				    1. 
        1. Select a workflow template.
            				    1. 
        1. Click Verify. 
            				    1. 
        1. Select the invalid 
            				 configuration in the workflow step and click Find and 
            				 Replace. The following are the available Field Types and 
            				 items:
            				
                					    - 
        - 
            - Approval Card Number
                					    - 
        - 
            - Disbursement Entry 
                					 - Service Code
                					    - 
        - 
            - Document Holder - 
                					 Filing Cabinet
                					    - 
        - 
            - Service - Service 
                					 Code
                					    - 
        - 
            - Task Type
                					    - 
        - 
            - Time Entry - Service 
                					 Code
                				
            			
        			
            				    1. 
        1. Select 
            				 the invalid value to be replaced and click <b style="font-weight: normal;">Replace</b>.
            				    1. 
        1. The Change Processing 
            				 screen will pop up once the value has been replaced.
            				    1. 
        1. Click Queue. 
            			
        		
    		
        			    - <span class="hcp2">Close</span> - Click this 
        			 to close the template. 
        		
    		Filter
    		The filter applies to the type list which can be filtered by:
    		
        			    - Warning
        			    - Info
        			    - All
        		
    		<span class="hcp2">Note:</span> The items classified 
    		 as Warning will be displayed by default. 
    		&nbsp;
     </div>

	

- <span class="hcp2">Dependencies</span> - Click 
    	 this to check the [dependencies](javascript:TextPopup(this)) 
    	 for the selected workflow template.
    
    	<div class="droptext" id="POPUP550723313" style="display: none;">
    		Breaking the dependencies between the workflow steps will result 
    		 in duplicate steps being created for the workflow.
    		
        			    1. <span lang="EN-GB" xml:lang="EN-GB" style="">In 
        			 <b>Configuration &gt; Business Parameters &gt; Workflow &gt; 
        			 Workflow Library</b>, select the workflow template from the 
        			 list.</span>
        			    1. <span lang="EN-GB" xml:lang="EN-GB" class="hcp7">Click 
        			 <b>Dependencies</b>.</span>
        			    1. <span lang="EN-GB" xml:lang="EN-GB" class="hcp7">All 
        			 of the steps in the workflow will be shown, expand the step 
        			 to view the other workflows that the step is being used in.</span>
        			    1. <span lang="EN-GB" xml:lang="EN-GB" class="hcp7">Tick 
        			 the checkbox in the Select column to enable the <b>Break Dependency</b> 
        			 command button. The button is greyed out when there is no 
        			 step selected.</span>
        			    1. <span lang="EN-GB" xml:lang="EN-GB" class="hcp7">Assign 
        			 new step key in the Proposed Step Key column. If no step key 
        			 is assigned,</span><span> </span><span lang="EN-GB" xml:lang="EN-GB">the 
        			 default auto incremental step key will be assigned.</span>
        			    1. <span lang="EN-GB" xml:lang="EN-GB" class="hcp7">Click 
        			 <b>Break Dependency.</b></span>
        			    1. <span>Click <b>Close</b> when completed.</span>
        		
    		<span class="hcp8">Note:</span> 
    		 The Dependencies screen will pop up automatically when user copies 
    		 a workflow template.
     </div>

	

- <span class="hcp2">Import</span> - Click this 
    	 to [import](javascript:TextPopup(this)) 
    	 workflow templates.
    
    	<div class="droptext" id="POPUP405750778" style="display: none;">
    		
        			    1. Select the folder containing the workflow template(s) 
        			 you want to import.
        			    1. Click Import - Load List.
        			    1. Tick the workflow templates you want to import. By default, 
        			 all workflows will be selected. Workflows marked as 'Customised' 
        			 will not be selected.
        			    1. Click Import.
        			    1. Click Close when completed.
        		
    		Note: If you import a workflow which is the same with an existing 
    		 workflow template but with a different version description, the 
    		 message will be displayed in the Import Workflow screen.
     </div>

	

- <span class="hcp2">Export</span> - Click this 
    	 to [export](javascript:TextPopup(this)) 
    	 workflow templates.
    
    	<div class="droptext" id="POPUP405756172" style="display: none;">
    		
        			    1. Select the folder where you want to export the workflow 
        			 to.
        			    1. Click Export.
        			    1. Click Close when complete.
        		
     </div>

	

- <span class="hcp2">Attributes </span><span style="font-weight: normal;">- 
    	 Click this to set up attributes for the selected template. When exporting 
    	 this checklist, you will also get the .dtr file which contains the 
    	 attributes information. Refer to [Attributes](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Attributes.htm) 
    	 for more information.</span>

### Workflows in Engage Servicing Portal
Workflow templates that are made available for ESP are known as requests 
 and is to be initiated from the Requests screen in the Entity tab. However, 
 it is possible to allow the request to be initiated from within the Home 
 tab. This requires the following:

	

- In CP-AD (Front-office), there must be a Database and Master 
    	 File specified for the relevant organisation or group that requires 
    	 the initiation from Home tab. This is done in Configuration &gt; Engage 
    	 Servicing Portal &gt; Configuration &gt; [Organisation](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/ESP_Organisations_(Configuration).htm). 
    	 <span class="hcp8">Note</span>: 
    	 For Auto Load Profile mode, the Database field is automatically filled 
    	 with value and is not editable.

	

- In VP-BP (Back-office), the workflow template must contain a 
    	 [Master File 
    	 attribute](javascript:TextPopup(this)) where the value is the same Master File 
    	 as specified for the organisation in CP-AD.
    
    	<div class="droptext" id="POPUP575934357" style="display: none;">
    		
        			    1. In Workflow Library, select the workflow template.
        			    1. Click Attributes.
        			    1. In the Attributes Configuration screen, add the following:
        			
            				    - 
        - Type - select Master File
            				    - 
        - Value - select the same Master File for the organisation 
            				 in CP-AD.
            			
        			    1. Click Update.
        		
     </div>

&nbsp;

[Can I print 
 out the workflow template?](javascript:TextPopup(this))
 
<div class="droptext" id="POPUP405722829" style="display: none;">
	

Yes, this is possible. In Workflow Library, select the workflow 
	 template and click Edit with Workflow Designer. The Ribbon in Workflow 
	 Designer contains these buttons:

	
		

- Workflow - Click to print out the workflow diagram as well 
    		 as details for all of the workflow steps.

		

- Step - Click to print out details of the selected step.

	
 </div>

&nbsp;

&nbsp;

See also:

	

- [Checklist/Workflow 
    	 Step Creation](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Checklist_Workflow_Step_Creation.htm)

	

- [Step Library](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Step_Library.htm)

	

- [Workflow Creation](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Workflow_Creation.htm)

	

- [Workflow 
    	 Designer Screen](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Workflow_Designer_Screen.htm)

	

- [Working with Workflow](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Working_with_Workflow.htm)


 
&nbsp;

You are here:[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; [Viewpoint - Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Overview.htm) &gt; [Configuration](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Configuration.htm) &gt; [Business Parameters](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Lookup_Values.htm) &gt; [Workflow](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Workflow.htm) &gt; Workflow Library
 
&nbsp;
 
(c) Viewpoint Software for 
 Business Ltd
 
Version: 8.0.2022.09.20




