




# Activities Profiles
The Activities Profile is used as a templates to create Activities.

&nbsp;

Filters

The filters apply to the identity register type list.

	

- Type status &nbsp;- You can choose to view only active types, 
    	 inactive ones or all.

	

- Category - You can choose to view the activity profile based 
    	 on the category or all.

Select/Apply button

This allows for additional criteria to apply to the activity profile 
 type list.

&nbsp;

Command buttons

Click on the relevant command button to perform the necessary.

	

- New <span class="hcp3">&nbsp;- 
    	 Click to [create](javascript:TextPopup(this)) 
    	 </span><span class="hcp3">a new activity profile.</span>
    
    	<div class="droptext" id="POPUP412511967" style="display: none;">
    		
        			    1. Enter 
        			 details for the new Activity Profile
        		
    		
        			
            				    - 
        - Key 
            				 <span class="hcp3">-</span> <span class="hcp3">Enter 
            				 specific key to the activity profile that differentiates 
            				 the record from other activity profiles. This field is 
            				 mandatory.</span>
            				    - 
        - Description 
            				 <span class="hcp3">- Enter the description 
            				 of the activity profile. This field is mandatory.</span>
            				    - 
        - Review 
            				 Rule Initiated<span class="hcp3"> - It 
            				 is mandatory to tick this checkbox in order to include 
            				 this template into the File Review Scope when performing 
            				 File Review to create an activity automatically.</span>
            				    - 
        - Ad-hoc 
            				 Initiated <span class="hcp3">-</span> 
            				 <span class="hcp3">It is mandatory to 
            				 tick this checkbox in order for the template to be displayed 
            				 in the Activity Template Selection pop-up screen when 
            				 creating an ad-hoc activity.</span>
            				    - 
        - Grid 
            				 Definition <span class="hcp3">-</span> 
            				 <span class="hcp3">This specifies which 
            				 grid that will be linked to the activity when it is created 
            				 automatically by the File Review function. Note that users 
            				 must have access on the grid records in order for it to 
            				 be displayed. This field is mandatory.</span>
            				    - 
        - Master 
            				 File Field <span class="hcp3">- This field 
            				 is to define the Master File that will be linked to the 
            				 activity when it is created automatically by the File 
            				 Review function. The list will vary depending on the Grid 
            				 Definition selected. This field is mandatory. Note that 
            				 this field will not be shown in the File Maintenance's 
            				 Activities screen.</span>
            				    - 
        - Date 
            				 Field <span class="hcp3">- This will define 
            				 the date field that will be referred by the File Review 
            				 function when creating an activity automatically. The 
            				 list will vary depending on the Grid Definition selected. 
            				 </span>
            				    - 
        - Filter 
            				 <span class="hcp3">- This is where you 
            				 can define additional SQL filter that is specific to the 
            				 Grid Definition selected, if necessary. The File Review 
            				 function will then refer to this field and filter out 
            				 the appropriate information when creating the activity 
            				 automatically.</span>
            				    - 
        - Create 
            				 Days Before <span class="hcp3">- This 
            				 field will determine the creation date for the activity 
            				 based on the Date Field values. The File Review function 
            				 will refer to this information to decide if an activity 
            				 or workflow record should be created. This field is mandatory.</span>
            				    - 
        - Category 
            				 <span class="hcp3">- Select the category 
            				 to be specified for the Select Workflow screen during 
            				 workflow creation process. The available options are categories&nbsp;defined 
            				 in the Workflow Categories [WFAC] lookup table. This field 
            				 is mandatory.</span>
            				    - 
        - Sub-Category 
            				 <span class="hcp3">- Select the subcategory 
            				 for workflow's category. This field is mandatory.</span>
            				    - 
        - Assign 
            				 To <span class="hcp3">- Select and assign 
            				 to an administrator when activity is created. For more 
            				 information regarding the list of options, you can refer 
            				 [here](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Assign_To_Codes.htm). 
            				 This field is mandatory.</span>
            				    - 
        - Matter 
            				 Type <span class="hcp3">- This is to specify 
            				 the matter type of the Activities record in the Billing 
            				 File. Note that this field is not applicable if Practice 
            				 Management license is not installed.</span>
            				    - 
        - Booking 
            				 Service <span class="hcp3">- This is where 
            				 you specify the default service in Activity Budget, if 
            				 applicable. This field can no longer be edited once the 
            				 activity profile is created. The Booking Service option 
            				 will only show all Service Master with a service class 
            				 other than T and D. Note that this field is not applicable 
            				 if Practice Management licence is not installed.</span>
            				    - 
        - Workflow 
            				 Template <span class="hcp3">- If you want 
            				 to pre-link a Workflow template&nbsp;to the activity profile, 
            				 you can select the Workflow Template in this field.</span>
            				    - 
        - Day 
            				 Actionable Before Due <span class="hcp3">- 
            				 This specifies the number of days before the due date 
            				 of creating the Workflow record. This field is mandatory.</span>
            				    - 
        - Note 
            				 <span class="hcp3">- Users can add a remark 
            				 in this field to provide additional guidance for each 
            				 template created. The note field will be displayed in 
            				 the Activities screen when a new activity record is being 
            				 created.</span>
            				    - 
        - Tag 
            				 Values <span class="hcp3">- Additional 
            				 tag values can be added in this field to configure Activities 
            				 record, if necessary. Note that as of now, there are no 
            				 tag values that can be added and this will be updated 
            				 in future development.</span>
            				    - 
        - Invoice 
            				 Separately <span class="hcp3">- Tick this 
            				 option if you want to generate the invoice separately 
            				 for Time and Disbursement. If this field is left unticked, 
            				 the draft invoice for Time and Disbursement will be generated 
            				 along with the Product Service Class via the Posting of 
            				 WIP screen.</span>
            				    - 
        - ESP 
            				 Shared <span class="hcp3">- Tick this 
            				 to publish the Activities record in Viewpoint Engage if 
            				 the Activities record is linked to an entity file.</span>
            				    - 
        - Customised 
            				 <span class="hcp3">- Tick this to indicate 
            				 that the value has been customised and prevent the change 
            				 from being overwritten during an upgrade.</span>
            				    - 
        - <span class="hcp8">Active -</span> Tick this to 
            				 activate the activity profile.
            			
        		
    		
        			    1. Click Update
        		
     </div>

	

- Edit - <span class="hcp3">Click 
    	 to edit an existing activity profile.</span>

	

- Delete <span class="hcp3">- 
    	 Click this to remove an existing activity profile.</span>

	

- <span class="hcp8">Attributes</span> - Click this to prompt 
    	 the Attributes Configuration screen. This allows you to set the attributes 
    	 for the Activity Profile. This is to control access to the selected 
    	 Activity Profile and have it available only to the Master File(s) 
    	 or user(s) specified in the attribute configuration.

	

- Budget <span class="hcp3">- 
    	 Click this to go to the [Budget Template](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Budget_Template.htm) 
    	 screen.</span>

	

- <span class="hcp8">Import</span> - Click this to import the 
    	 activity profile. This will include the Budget Template defined for 
    	 the Activity Profiles.

	

- <span class="hcp8">Export</span> - Click this to export activity 
    	 profile. This will include the Budget Template defined for the Activity 
    	 Profiles.

See also:

	

- [Activities](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Activities.htm)

	

- [Activity Explorer](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Activity_Explorer.htm)

	

- [Budget Template](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Budget_Template.htm) 

	

- [Activity Budget](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Activty_Budget.htm)

&nbsp;

 
&nbsp;

You are here:[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; [Viewpoint - Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Overview.htm) &gt; [Configuration](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Configuration.htm) &gt; [Business Parameters](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Lookup_Values.htm) &gt; [General](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Lookup_Values.htm) &gt; Activities Profiles
 
&nbsp;
 
(c) Viewpoint Software for 
 Business Ltd
 
Version: 8.0.2022.09.20




