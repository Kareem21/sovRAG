




# Change Codes
All change codes are listed in the new Changes screen in Configuration 
 &gt; Business Parameters &gt; General &gt; Change Codes. You need to ensure 
 that you have sufficient authority in your user roles to see the screen.

&nbsp;

Filters

The filter at the top applies to the Change Code list allowing you to 
 filter by the area of the change codes. When Document Management [8] is 
 selected, the list of change codes:

	

- Will only be applicable to Viewpoint Notifications feature, 
    	 these will not be seen in Changes screen.

	

- Can only be linked to Notifications and Workflows type of item.

&nbsp;

Change Codes

This shows all the existing change codes in Viewpoint. Each change code 
 is a type of change possible in Viewpoint and once performed, there will 
 be a record of it in the Changes screen. The exceptions are User Defined 
 Change Code 01 to User Defined Change 10 which are for use with a Workflow 
 macro item. These change codes allow for a workflow to trigger items linked 
 to the specified User Defined Change Code. Refer to [Checklist 
 Item - Field Type: Macros](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Checklist_Item_-_Field_Type__Macros.htm).

&nbsp;

Edit button

Click this to change the settings for the selected change code in terms 
 of:

	

- Description - This is the description that will appear in the 
    	 Changes screen. The description can contain just normal text as well 
    	 as field codes. For fields, enclose the code within '(-...-)'. For 
    	 example:  
    &#13;&#10;	![](../image318.gif)  
    &#13;&#10;	<span style="font-weight: bold; font-style: italic;">Note</span>: You 
    	 can obtain field code from Configuration &gt; Settings. Select the 
    	 Menu Group, Section and Screen; and refer to the Database Field column 
    	 for the field that you want.  
    &#13;&#10;	

	

- Show in Summary - This determines if the change will appear 
    	 when you select Summary in the Changes screen.

	

- Required Confirmation - This determines whether or not to display 
    	 the [Change Processing screen](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Change_Processing_Screen.htm). 
    	 If this is unticked, the Change Processing screen will not be seen 
    	 unless there are items linked to the Change Code.

	

- Customised - If ticked, the customisation will not be overwritten 
    	 during an upgrade.

&nbsp;

Event Links

This shows items that have been linked to the selected change code.

&nbsp;

Filters

Two filters are available for the Linked Item list:

	

- Linked Item type - You can choose to view only certain types 
    	 of linked items or all.

	

- Selection - This shows the selection option available for a 
    	 linked item. Select an option to see items with this selection.

&nbsp;

Command buttons

Click on the relevant command button to perform the necessary.

	

- New <span class="hcp4">- 
    	 Click this to [link](javascript:TextPopup(this)) 
    	 an item to the selected change code. This will open the Change Link 
    	 screen.</span>
    
    	<div class="droptext" id="POPUP518143641" style="display: none;">
    		
        			    1. Select the change code.
        			    1. Click New.
        			    1. In the Change Link screen, 
        			 specify the following:
        			
            				        - Change Code - This 
            				 defaults to the selected change code.
            				        - Link Type - Select 
            				 the item type to link to the change code. Ensure that 
            				 the relevant item type has been set up in your environment. 
            				 The available item types are:
            				        - 
            - 
                					            - API 
                					 Integration - This will create the content items and 
                					 send them to an external REST API service via Task 
                					 Scheduler and Notification Agent (TSNA) service. A 
                					 Task Scheduler job type 'External REST API Integration 
                					 [EAPI]' is used to push the contents to the external 
                					 REST API based on the Service Name defined in the 
                					 Change Link. Refer to [Link 
                					 Type: API Integration](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Task_Scheduler/Change_Codes_-_Link_Type__API_Integration.htm).
                					            - Approval 
                					 Cards - This will indicate that the change requires 
                					 approval. The approval is to be completed in the Changes 
                					 screen.
                					            - Checklists 
                					 - This will display the checklist in the [Change Processing Screen](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Change_Processing_Screen.htm).
                					            - E-mail 
                					 Notifications - This will display the e-mail notification 
                					 in the [Change 
                					 Processing Screen](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Change_Processing_Screen.htm). In order for the e-mail notification 
                					 to be sent, it must be selected and queued; and you 
                					 must have [Task 
                					 Scheduler and Notification Agent](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Task_Scheduler/Task_Scheduler.htm) set up. Refer 
                					 to [Link Type: E-mail 
                					 Notifications](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Change_Codes_-_Link_Type__E-mail_Notification.htm).
                					            - Excel 
                					 Statements - This will display the Excel statement&nbsp;in 
                					 the [Change 
                					 Processing Screen](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Change_Processing_Screen.htm).
                					            - Forms 
                					 - This will display the form&nbsp;in the [Change Processing Screen](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Change_Processing_Screen.htm).
                					            - Macros 
                					 - This is to perform a predefined action when the 
                					 change takes place. Refer to [Link 
                					 Type: Macros](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Change_Codes_-_Link_Type__Macros.htm).
                					            - Notes 
                					 - This will display the note and its explanation in 
                					 the [Change 
                					 Processing Screen](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Change_Processing_Screen.htm). Refer to [Link 
                					 Type: Notes](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Change_Codes_-_Link_Type__Notes.htm).
                					            - Notifications 
                					 - This will create a notification item. Refer to [Link 
                					 Type: Notifications](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Change_Codes_-_Link_Type__Notifications.htm).
                					            - Standard 
                					 Reports - This will display the report in the [Change Processing Screen](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Change_Processing_Screen.htm).
                					            - Tasks 
                					 - This will display the task&nbsp;in the [Change Processing Screen](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Change_Processing_Screen.htm). 
                					 Refer to [Link Type: 
                					 Tasks](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Change_Codes_-_Link_Type__Tasks.htm).
                					            - Word 
                					 Reports - This will display the Word report&nbsp;in 
                					 the [Change 
                					 Processing Screen](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Change_Processing_Screen.htm).
                					            - Workflows 
                					 - This will display the workflow&nbsp;in the [Change Processing Screen](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Change_Processing_Screen.htm).
                				
            				        - &lt;Link Item&gt; - 
            				 Select the item to link. The caption will change depending 
            				 on the Link Type selected. It is not available for the 
            				 Link Types E-mail Notifications, Macros, Notes, Notifications, 
            				 and Tasks.
            				        - Description - Enter 
            				 a description for the link type. If the link type is 'Notes', 
            				 this can be used to enter the message in short. To elaborate, 
            				 use the Help Text field below.
            				        - Selection - This is 
            				 not available when the Link Type is 'Tasks' or 'Notes'. 
            				 Select the default selection mode for the item where:
            				            - 
                					            - De-activated [D] 
                					 - use this to deactivate the Change Link. This retains 
                					 the Change Link but it will not be applied.
                					            - Default selected 
                					 [Y] - item will automatically be selected for generation 
                					 but user can choose to deselect it.
                					            - Default un-selected 
                					 [N] - item is not selected by default but can be selected 
                					 by user.
                					            - Mandatory - item 
                					 will be selected and cannot be deselected.
                					            - Mandatory - selection 
                					 not visible [X] - the item is selected but will not 
                					 be seen in the Change Processing screen.
                				
            				        - Tag Values - Tags can 
            				 be entered to set conditions for the linked items.
            				        - Help Text - This is 
            				 where you can enter more detailed explanation about the 
            				 item to guide users in deciding whether the item is needed 
            				 for that particular change. If the link type is 'Notes', 
            				 this field can be used for a longer explanation. This 
            				 will be seen under the linked item in the Change Processing 
            				 screen.
            				        - Note - Enter additional 
            				 note related to the Change Link. This is not available 
            				 if the Link Type is 'Notes'.
            				        - Change 
            				 Link Parameters table - This part of the screen defines 
            				 the [parameters](javascript:TextPopup(this)) 
            				 for form generation.
            				<div class="droptext" id="POPUP3345555921" style="display: none;">
            					
                						            - SF (Form) - this is to specify value for 
                						 'Linked to' and 'Allow Combine Forms'.
                						            - 
                - 
                    							                - Linked To - You can specify if the form 
                    							 is linked to the Country of Incorporation, 
                    							 Country of Registration or Not Applicable. 
                    							 If Not Applicable is selected, the form will 
                    							 be triggered for all jurisdictions. If the 
                    							 form is for a foreign registered company in 
                    							 which the 'Country of Registration' values 
                    							 is selected, the EF parameter will be included 
                    							 without any value, see below:  
                    &#13;&#10;							  
                    &#13;&#10;							![](../image183.jpg)
                    							                - Allow Combine Forms - You can choose 
                    							 either 'Combine Changes' or 'Not Allowed' 
                    							 depending on whether or not you want all changes 
                    							 in one form or separate forms.
                    						
                						            - EN (Entity) - this controls the selection 
                						 of fields related to an entity. It allows you 
                						 to apply more specific criteria when generating 
                						 a form.
                						            - MF (Master File) - this controls the selection 
                						 of appropriate fields related to a Master File. 
                						 This is similar to EN, where more than one selection 
                						 value can be set.
                						            - CC (Change fields) - this controls the selection 
                						 of change fields associated with the change code. 
                						 You can use the operators to compare the field 
                						 with specified value, to check for changes to 
                						 a field or check if the field is empty or not.  
                &#13;&#10;						&nbsp;
                						<table style="border-collapse: separate;" cellspacing="0">
                							<colgroup><col style="width: 21.002%;">
                							<col style="width: 45.665%;">
                							<col style="width: 33.333%;">
                							</colgroup><tbody><tr style="height: 28px;">
                								<td style="border-top-color: rgb(128, 128, 128); border-top-style: solid; border-top-width: 1px; border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px; border-left-color: rgb(128, 128, 128); border-left-style: solid; border-left-width: 1px;">
                
                <span class="hcp10">Operator</span>
                
                </td>
                								<td class="hcp11">
                
                <span class="hcp10">Explanation</span>
                
                </td>
                								<td class="hcp11">
                
                <span class="hcp10">Example</span>
                
                </td>
                							</tr>
                							<tr style="height: 42px;">
                								<td class="hcp12">
                
                =
                
                </td>
                								<td class="hcp13">
                
                To 
                								 specify that the field value must be equal 
                								 to the specified value
                
                </td>
                								<td class="hcp13">
                
                Statutory 
                								 Officer Type Code = D
                
                </td>
                							</tr>
                							<tr style="height: 42px;">
                								<td class="hcp12">
                
                &lt;&gt;
                
                </td>
                								<td class="hcp13">
                
                To 
                								 specify that the field value must not 
                								 be equal to the specified value
                
                </td>
                								<td class="hcp13">
                
                Certificate 
                								 No. &lt;&gt; 0
                
                </td>
                							</tr>
                							<tr style="height: 42px;">
                								<td class="hcp12">
                
                In
                
                </td>
                								<td class="hcp13">
                
                To 
                								 specify that the field value can be any 
                								 of the listed values
                
                </td>
                								<td class="hcp13">
                
                New 
                								 Status Code In W,L
                
                </td>
                							</tr>
                							<tr style="height: 42px;">
                								<td class="hcp12">
                
                Not 
                								 In
                
                </td>
                								<td class="hcp13">
                
                To 
                								 specify that the field value cannot be 
                								 any of the listed values
                
                </td>
                								<td class="hcp13">
                
                New 
                								 Status Code Not In W,L
                
                </td>
                							</tr>
                							<tr style="height: 42px;">
                								<td class="hcp12">
                
                &gt;=
                
                </td>
                								<td class="hcp13">
                
                To 
                								 specify that the field value must be greater 
                								 than or equal to the specified value
                
                </td>
                								<td class="hcp13">
                
                &nbsp;
                
                </td>
                							</tr>
                							<tr style="height: 42px;">
                								<td class="hcp12">
                
                &gt;
                
                </td>
                								<td class="hcp13">
                
                To 
                								 specify that the field value must be greater 
                								 than the specified value
                
                </td>
                								<td class="hcp13">
                
                &nbsp;
                
                </td>
                							</tr>
                							<tr style="height: 46px;">
                								<td class="hcp12">
                
                &lt;
                
                </td>
                								<td class="hcp13">
                
                To 
                								 specify that the field value must be less 
                								 than the specified value
                
                </td>
                								<td class="hcp13">
                
                &nbsp;
                
                </td>
                							</tr>
                							<tr style="height: 28px;">
                								<td class="hcp12">
                
                &lt;=
                
                </td>
                								<td class="hcp13">
                
                To 
                								 specify that the field value must be less 
                								 than or equal to the specified value
                
                </td>
                								<td class="hcp13">
                
                &nbsp;
                
                </td>
                							</tr>
                							<tr style="height: 28px;">
                								<td class="hcp12">
                
                Like
                
                </td>
                								<td class="hcp13">
                
                To 
                								 specify that the field value contains 
                								 the specified value. This can include 
                								 wildcard '*'.
                
                </td>
                								<td class="hcp13">
                
                Statutory 
                								 Officer Type Code Like D*
                
                </td>
                							</tr>
                							<tr style="height: 28px;">
                								<td class="hcp12">
                
                Has 
                								 changed
                
                </td>
                								<td class="hcp13">
                
                To 
                								 specify that the field value has changed
                
                </td>
                								<td class="hcp13">
                
                AdNrSR 
                								 Has changed
                
                </td>
                							</tr>
                							<tr style="height: 28px;">
                								<td class="hcp12">
                
                Has 
                								 not changed
                
                </td>
                								<td class="hcp13">
                
                To 
                								 specify that the field value has not changed
                
                </td>
                								<td class="hcp13">
                
                AdNrSR 
                								 Has not changed
                
                </td>
                							</tr>
                							<tr style="height: 28px;">
                								<td class="hcp12">
                
                Has 
                								 changed from/to
                
                </td>
                								<td class="hcp13">
                
                To 
                								 specify that the field value has changed 
                								 from a particular value to a specified 
                								 value. The previous value must be specified 
                								 first followed by a pipe and the new value 
                								 e.g. Yes|No.
                
                								
                
                For multiple previous values, use a 
                								 forward slash e.g. A/B|C means when the 
                								 value has changed from either A or B to 
                								 C.
                
                </td>
                								<td class="hcp13">&nbsp;</td>
                							</tr>
                							<tr style="height: 28px;">
                								<td class="hcp12">
                
                Has 
                								 changed from
                
                </td>
                								<td class="hcp13">
                
                To 
                								 specify that the field value has changed 
                								 from a specified value. If more than one 
                								 value, separate with a forward slash e.g. 
                								 A/B.
                
                </td>
                								<td class="hcp13">&nbsp;</td>
                							</tr>
                							<tr style="height: 28px;">
                								<td class="hcp12">
                
                Has 
                								 changed to
                
                </td>
                								<td class="hcp13">
                
                To 
                								 specify that the field value has changed 
                								 to a specified value. If more than one 
                								 value, separate with a forward slash e.g. 
                								 A/B.
                
                </td>
                								<td class="hcp13">
                
                &nbsp;
                
                </td>
                							</tr>
                							<tr style="height: 28px;">
                								<td class="hcp12">
                
                Is 
                								 empty
                
                </td>
                								<td class="hcp13">
                
                To 
                								 specify that the field is empty
                
                </td>
                								<td class="hcp13">
                
                &nbsp;
                
                </td>
                							</tr>
                							<tr style="height: 28px;">
                								<td class="hcp12">
                
                Is 
                								 not empty
                
                </td>
                								<td class="hcp13">
                
                To 
                								 specify that the field is not &nbsp;empty
                
                </td>
                								<td class="hcp13">
                
                AdNrSR 
                								 Is not empty
                
                </td>
                							</tr>
                						</tbody></table>
                
                						
                
            - SQL (SQL Defined) - this controls the selection 
                						 criteria based on the queries entered in the Tag 
                						 Values field. This gives you more control on what 
                						 variable to select for which query. For example:  
                &#13;&#10;						  
                &#13;&#10;						With the following SQL queries:  
                &#13;&#10;						  
                &#13;&#10;						[/SQL.SQLOFC=SELECT EntCode, AddrCode FROM Officers 
                						 WHERE OfficerText='Chairman'/]  
                &#13;&#10;						[/SQL.SQLOFC1=SELECT EntCode, AddrCode FROM Officers 
                						 WHERE LEFT (OfficerType,1) IN 'P'/]  
                &#13;&#10;						  
                &#13;&#10;						You can select the fields defined and set a specific 
                						 variable as per below:  
                &#13;&#10;						  
                &#13;&#10;						![](../image182.jpg)  
                &#13;&#10;						  
                &#13;&#10;						This means that if Barcelona Celebrations (BARCVI) 
                						 appoints a Chairman, or if Aphrodite Limited (APHROD) 
                						 appoints a Power of Attorney, the form is triggered.  
                &#13;&#10;						&nbsp;
                
                					
            					
            To remove a parameter, right-click on the item and 
            					 click Remove:
            
            					
            
            ![](../image184.jpg)
                </div>
            
            			
        
        			
        
    1. Click Update.
        
        		
    		
    &nbsp;
       </div>

	

- Edit<span class="hcp4">&nbsp;- 
    	 Click this to edit the linking properties for the selected linked 
    	 item.</span>

	

- Delete<span class="hcp4">&nbsp;- 
    	 Click this to remove the selected linked item.</span>

&nbsp;

[I have a Notifications 
 item linked to Document Management change codes but this is not seen.](javascript:TextPopup(this))
   
<div class="droptext" id="POPUP461639591" style="display: none;">
	

For Notifications on Document Management change codes, ensure that 
	 the option 'Add Master File Code to Master File Name Display' in [System 
	 Defaults &gt; Document Management](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/System_Defaults_-_Document_Management.htm) is ticked.

	

&nbsp;
   </div>

&nbsp;

&nbsp;

See also:

	

- [Change 
    	 Codes - Tags](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Change_Codes_Link_Items_-_Tags.htm)


   
&nbsp;

You are here:[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; [Viewpoint - Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Overview.htm) &gt; [Configuration](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Configuration.htm) &gt; [Business Parameters](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Lookup_Values.htm) &gt; [General](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Lookup_Values.htm) &gt; Change Codes
   
&nbsp;
   
(c) Viewpoint Software for 
 Business Ltd
   
Version: 8.0.2022.09.20


  

