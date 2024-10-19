




# File Review Function
<div>
<p style="font-weight: bold; font-style: italic; color: rgb(51, 71, 150);">This 
 feature requires you to have Entity Administration component.</p>
</div>
&nbsp;

The File Review feature is used to check on Master Files in your database 
 and depending on how it is configured, can be used to:

	

- Notify you of exceptions in the file.

	

- Notify you of certain information in the file.

	

- Assist in creation of new records or update of existing information.

When running File Review, the results include the following:

	

- Review Scope - This displays the type of review item.

	

- Review Rule - This shows the Review Rule resulting in the review 
    	 item along with the icon to indicate if it is an error, a warning 
    	 or an update.

	

- Messages - This shows messages or notifications for the review 
    	 item.

<span lang="EN-US" xml:lang="EN-US" class="hcp2">For errors and warnings, you need to manually 
 check and make the necessary corrections for the Master File.</span>

<span lang="EN-US" xml:lang="EN-US" class="hcp3">For 
 updates, you can have the system perform these automatically, for instance:</span>

	

- Create missing items; or

	

- Updating field value (applicable only to compliance review status 
    	 fields in CDD screen).

You can run File Review from:

	

- [Viewpoint 
    	 - Home](javascript:TextPopup(this)) - The review can be on more than one file.
    
    	<div class="droptext" id="POPUP379027987" style="display: none;">
    		This can be set up in Viewpoint - Home &gt; To Do &gt; Jobs 
    		 &gt; [File Review](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/File_Review.htm) or as a job type 
    		 to be run by [Task 
    		 Scheduler and Notification Agent](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Task_Scheduler/Task_Scheduler.htm).
    		&nbsp;
     </div>

	

- [File 
    	 Maintenance or File Enquiry](javascript:TextPopup(this)) - The review will 
    	 only be on the Master File.
    
    	<div class="droptext" id="POPUP379138282" style="display: none;">
    		In the File Maintenance or File Enquiry screen, the review will 
    		 be only for the Master File.
    		
        			    1. Click File Review button from the Ribbon or section 
        			 menu to start the review.
        			    1. Select the review scope.
        			    1. When the review is complete, the File Review results 
        			 screen will appear at the bottom of the screen.
        		
    		&nbsp;
    		<span class="hcp6">Results 
    		 Screen</span>
    		The results screen contains:
    		
        			    - Filters
        			    - 
        - 
            				        - Types - You can select the type of review result 
            				 e.g. view only updates, warnings, errors or all.
            				        - Areas - You can select the area of the review item 
            				 such as General/Compliance or Entity Administration.
            			
        			    - Options
        			        - 
            				        - Refresh - Click to re-run the File Review.
            				        - Go to Screen - Click to open the screen for the 
            				 selected review result.
            				        - Select All - Click this to tick all checkboxes in 
            				 the Select column for the review results.
            				        - Deselect All - Click this to un-tick all checkboxes 
            				 in the Select column for the review results.
            				        - Post Updates - Click this to post selected updates.
            				        - Open in Window - Click this to open the results 
            				 screen in a separate window.
            			
        			    - Review results
        		
    		&nbsp;
    		<span lang="EN-US" xml:lang="EN-US" style="">Right-clicking 
    		 in the review results will also allow you to copy, export to Excel 
    		 or preview the review results before printing (similar to the 
    		 Results screen for File Review in Viewpoint – Home screen).</span>
    		&nbsp;
    		Post 
    		 all updates
    		By default, all updates are selected and will be posted when 
    		 you click Post Updates.
    		&nbsp;
    		Post selected 
    		 updates
    		To de-select an update item, click to uncheck the checkbox before 
    		 you click Post Updates.
    		&nbsp;
    		File 
    		 Review Post Update
    		After selecting Post Updates, the review result will show only 
    		 updates that were posted and the Select column is replaced by 
    		 the Posted column.
    		&nbsp;
    		<span class="hcp7" style="font-weight: bold; font-style: italic;">Note</span>: 
    		 The ability to post updates can be configured to be based on the 
    		 authority of the user or can be ignored by adding the tag +CheckAuth.
     </div>

	

- [Relations 
    	 Enquiry or Ownership Enquiry screen](javascript:TextPopup(this)) - The review 
    	 can be on one Master File or multiple Master Files.
    
    	<div class="droptext" id="POPUP379139276" style="display: none;">
    		In Ownership and Relations screen, you can also choose the type 
    		 of review. When you click File Review from the Ribbon, the system 
    		 will prompt you to select the review scopes.
    		To review for one Master File, click to select the Master File 
    		 in the screen before you click File Review. Otherwise, the review 
    		 will be performed on all Master Files listed in the screen.
    		Once the review is complete, the Score column is added to the 
    		 screen. This refers to the number of items that require your attention. 
    		 Click on any of the Master File to see the details in the File 
    		 Review screen at the bottom.
    		&nbsp;
    		<span lang="X-NONE" xml:lang="X-NONE">Results 
    		 Screen</span>
    		<span lang="EN-GB" xml:lang="EN-GB">The results screen is similar 
    		 to what you see in File Maintenance and File Enquiry screen.</span>
    		&nbsp;
    		<span class="hcp7" style="font-weight: bold; font-style: italic;">Note</span>: 
    		 The ability to post updates can be configured to be based on the 
    		 authority of the user or can be ignored by adding the tag +CheckAuth.
     </div>

	

- [within 
    	 a workflow](javascript:TextPopup(this)) - The design of the workflow will determine 
    	 if the review is on one Master File or multiple Master Files.
    
    	<div class="droptext" id="POPUP444179778" style="display: none;">
    		The workflow step item must be set to File Review. For details, 
    		 refer to [Configuring 
    		 Checklist Items](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Configuring_Checklist_Item.htm).
     </div>

&nbsp;
## File Review Tags and Rules
The File Review feature works based on review rules and tags which will 
 be used to customise the review. Depending on the scope of the review, 
 it may require the review rule, review tag or both.

&nbsp;
### Review Rules
For File Review, the Compliance and AEOI review rules are those that 
 accept review tags. Other review rules support review tags that are entered 
 in other areas.

These review rules can be set to active or inactive depending on whether 
 or not you required them. To deactivate a rule, do the following:

	

1. In Viewpoint – Home screen, go to Configuration &gt; Settings 
    	 &gt; Customise &gt; [Review 
    	 Rules](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Review_Rules.htm).

	

1. Select the review rule and click Edit.

	

1. Tick the Deactivate option.

	

1. Click Update.

Note that if you deactivate a review rule that supports a review tag, 
 that tag will no longer work.

&nbsp;

Viewpoint will check for the tags in the user field first, followed 
 by Entity Type, <span class="hcp6">User Roles/Service Provided,</span> 
 CDD Profile, Lookup Table and the Master File Type Lookup Table. If the 
 same tag is specified twice, the program will apply the first instance 
 and ignore the second one.

&nbsp;
### Review Tags
These are additional codes that you add to specify certain parameters 
 and values for the file review. Where the tags are added will depend on 
 the type of tags and its function. For the following review scopes, the 
 tags are to be added to the Tag Values field of the relevant review rules:

	

- AEOI review

	

- Compliance review

	

- Data Validation review

For the other scopes, the tags can be specified in:

	

- The Note field of the User Field with the key ‘TAGMFR’ to apply 
    	 only to Master Files that contain this user field. Refer to [User 
    	 Fields](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/User_Fields.htm) for details on retrieving the user field.

	

- The Tag Values field of a value in User Roles [URLS] Lookup 
    	 Table to apply to all Master Files with the User Role added in Services 
    	 Provided screen (this requires the User Role to have 'SP' in the Electronic 
    	 Filing Code field).

	

- The Tag Values field of an Entity Type to apply to all Entity 
    	 Files of the entity type.

	

- The Tag Values field of a value in CDD Profile [KYCP] Lookup 
    	 Table to apply to all Master Files with the CDD profile.

	

- The Tag Values field of a value in Master File Type [ADTP] Lookup 
    	 Table to apply to all Master Files of the Master File type.

Viewpoint will check for the tags in the user field first, followed 
 by Entity Type,<span class="hcp6"> </span>CDD Profile Lookup 
 Table and the Master File Type Lookup Table. If the same tag is specified 
 twice, the program will apply the first instance and ignore the second 
 one.

<span class="hcp9">Note</span>: If 
 the security model is Services Provided Model [5], then Viewpoint will 
 check for the tags in the user field, followed by the services in the 
 Services Provided screen and then only in Entity Type, CDD Profile lookup 
 table and Master File Type lookup table.

&nbsp;
#### Configuring File Review Tags in Lookup Tables

	

1. <span lang="EN-US" xml:lang="EN-US" class="hcp3">The 
    	 two lookup tables are Master File Types [ADTP] and CDD Profile [KYCP]. 
    	 Adding review tags here means that you want a file of a certain Master 
    	 File type or set to a specific CDD profile to have information specified 
    	 by the review tags.</span>

	

1. In Viewpoint – Home, go to Configuration &gt; Business Parameters 
    	 &gt; General &gt; Lookup Values.

	

1. Select the value the review tags are for.

	

1. Click Edit.

	

1. Enter the review tags in Tag Values field.

	

1. Click Update.

&nbsp;
#### Configuring File Review Tags for Entity Type
If the review is to check on Entity File setup, then you might want 
 to specify the review tags in Entity Type instead.

	

1. In Viewpoint – Home, go to Configuration &gt; Business Parameters 
    	 &gt; Entity Administration &gt; Entity Types.

	

1. Select the entity type.

	

1. Click Edit.

	

1. Enter the review tags in Tag Values field.

	

1. Click Update.

&nbsp;
#### Configuring File Review Tags using User Fields
In the event that you need the review tags to apply to selected files 
 as and when relevant, you can use User Field with the key ‘TAGMFR’ and 
 enter the review tags in the Note field.

&nbsp;
## File Review Scopes
Essentially, the feature is to check on your Master Files but you can 
 select what to check by selecting the relevant scopes which are:

	

- [Data 
    	 Validation review](javascript:TextPopup(this))
    
    	<div class="droptext" id="POPUP3715169251" style="display: none;">
    		<span lang="EN-US" xml:lang="EN-US" class="hcp2">This review checks on the Master 
    		 File data to ensure that the data is valid. If data migration 
    		 was performed or changes made incorrectly, running this review 
    		 will alert users of the following:</span>
    		
        			    - <span lang="EN-US" xml:lang="EN-US" class="hcp2">Mandatory fields without 
        			 any value</span>
        			    - <span lang="EN-US" xml:lang="EN-US" class="hcp2">Values in fields that 
        			 are not active</span>
        			    - <span lang="EN-US" xml:lang="EN-US" class="hcp2">Values of incorrect field 
        			 type</span>
        			    - <span lang="EN-US" xml:lang="EN-US" class="hcp2">Invalid relations</span>
        		
    		Additionally, this review can also be used to check on standard 
    		 Viewpoint fields and user fields:
    		
        			    - check if the field is empty
        			    - check if the field value is valid
        		
    		However, this is not supported for [custom 
    		 fields](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Custom_Fields.htm).
    		<span lang="EN-US" xml:lang="EN-US" class="hcp3">The 
    		 checking is based on Data Validation review rules which applies 
    		 to a specific screen and can be activated or deactivated according 
    		 to your needs.</span> <span lang="EN-US" xml:lang="EN-US" class="hcp2">At the moment, 
    		 the following Data Validation review rules are active by default:</span>
    		<table class="Table1" cellspacing="0px" width="100%">
    			<colgroup><col style="width: 23.551%;">
    			<col style="width: 76.449%;">
    			</colgroup><tbody><tr class="t1st">
    				<td>Code</td>
    				<td>Description and Explanation</td>
    			</tr>
    			<tr class="t2Row">
    				<td class="t1Col">
    
    R_FMDINREL
    
    </td>
    				<td class="t2Col">
    
    <span lang="EN-US" xml:lang="EN-US" class="hcp2">Master 
    				 File &gt; Internal Relations - Data Validation</span>
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp10">This 
    				 review rule checks on records in the Internal Relations 
    				 screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t1Row">
    				<td class="t1Col">
    
    R_FMDRELAT
    
    </td>
    				<td class="t2Col">
    
    <span lang="EN-US" xml:lang="EN-US" class="hcp2">Master 
    				 File &gt; Relations (Master File) - Data Validation</span>
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp10">This 
    				 review rule checks on records in the Master File Relations 
    				 screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t2Row">
    				<td class="t1Col">
    
    R_FMMCOMPR
    
    </td>
    				<td class="t2Col">
    
    <span lang="EN-US" xml:lang="EN-US" class="hcp2">Master 
    				 File &gt; Compliance &gt; Identity Register - Data Validation</span>
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp10">This 
    				 review rule checks on records in the Identity Register 
    				 screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t1Row">
    				<td class="t1Col">
    
    R_FSEOPOFF
    
    </td>
    				<td class="t2Col">
    
    <span lang="EN-US" xml:lang="EN-US" class="hcp2">Entity 
    				 Administration &gt; Statutory Officers - Data Validation</span>
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp10">This 
    				 review rule checks on records in the Statutory Officers 
    				 screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t2Row">
    				<td class="t1Col">
    
    R_FSRELAT
    
    </td>
    				<td class="t2Col">
    
    <span lang="EN-US" xml:lang="EN-US" class="hcp2">Entity 
    				 Administration &gt; Relations (Entity) &nbsp;- Data Validation</span>
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp10">This 
    				 review rule checks on records in the Entity File Relations 
    				 screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t1Row">
    				<td class="t1Col">
    
    R_FSETROFF
    
    </td>
    				<td class="t2Col">
    
    <span lang="EN-US" xml:lang="EN-US" class="hcp2">Entity 
    				 Administration &gt; Trust Officers - Data Validation</span>
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp10">This 
    				 review rule checks on records in the Trust Officers screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t2Row">
    				<td class="t1Col">
    
    R_FMMUSRFC
    
    </td>
    				<td class="t2Col">
    
    Master File &gt; Compliance &gt; User 
    				 Fields - Identity Details - Data Validation
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp10">This 
    				 review rule checks on User Fields in the User Fields - 
    				 Identity Details screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t1Row">
    				<td class="t1Col">
    
    R_FMMUSRFM
    
    </td>
    				<td class="t2Col">
    
    Master File &gt; General &gt; User 
    				 Fields - Master File - Data Validation
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp10">This 
    				 review rule checks on User Fields in the User Fields - 
    				 Master File screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t2Row">
    				<td class="t1Col">
    
    R_FMMUSRFO
    
    </td>
    				<td class="t2Col">
    
    Master File &gt; General &gt; User 
    				 Fields - Tax Details - Data Validation
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp10">This 
    				 review rule checks on User Fields in the User Fields - 
    				 Tax Details screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t1Row">
    				<td class="t1Col">
    
    R_FBBUSRFB
    
    </td>
    				<td class="t2Col">
    
    Sales Ledgers &gt; Billing File &gt; 
    				 User Fields - Billing File - Data Validation
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp10">This 
    				 review rule checks on User Fields in the User Fields - 
    				 Billing File screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t2Row">
    				<td class="t1Col">
    
    R_FIAUSRFD
    
    </td>
    				<td class="t2Col">
    
    Accounting &gt; Account File &gt; 
    				 Functions &gt; User Fields - Account File - Data Validation
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp12">This review rule checks on User 
    				 Fields in the User Fields - Account File screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t1Row">
    				<td class="t1Col">
    
    R_FIJASSET
    
    </td>
    				<td class="t2Col">
    
    Accounting &gt; Journals &gt; Fixed 
    				 Assets &gt; User Fields - Data Validation
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp12">This review rule checks on User 
    				 Fields in the Fixed Assets sub-ledger screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t2Row">
    				<td class="t1Col">
    
    R_FIJBACCT
    
    </td>
    				<td class="t2Col">
    
    Accounting &gt; Journals &gt; Bank 
    				 Account &gt; User Fields - Data Validation
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp14">This review rule checks on User 
    				 Fields in the</span></i> <i><span lang="EN-US" xml:lang="EN-US" class="hcp14">&nbsp;Bank 
    				 Account sub-ledger screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t1Row">
    				<td class="t1Col">
    
    R_FIJCRETR
    
    </td>
    				<td class="t2Col">
    
    Accounting &gt; Journals &gt; Creditor 
    				 &gt; User Fields - Data Validation
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp14">This review rule checks on User 
    				 Fields in the</span></i> <i><span lang="EN-US" xml:lang="EN-US" class="hcp14">Credit 
    				 sub-ledger screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t2Row">
    				<td class="t1Col">
    
    R_FIJDEBTR
    
    </td>
    				<td class="t2Col">
    
    Accounting &gt; Journals &gt; Debtor 
    				 &gt; User Fields - Data Validation
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp14">This review rule checks on User 
    				 Fields in the</span></i> <i><span lang="EN-US" xml:lang="EN-US" class="hcp14">&nbsp;Debtor 
    				 sub-ledger screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t1Row">
    				<td class="t1Col">
    
    R_FIJINVES
    
    </td>
    				<td class="t2Col">
    
    Accounting &gt; Journals &gt; Investment 
    				 &gt; User Fields - Data Validation
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp15">This review rule checks on User 
    				 Fields in the Investment sub-ledger</span></i> <i><span lang="EN-US" xml:lang="EN-US" class="hcp15">screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t2Row">
    				<td class="t1Col">
    
    R_FIJPRODT
    
    </td>
    				<td class="t2Col">
    
    Accounting &gt; Journals &gt; Products/Services 
    				 &gt; User Fields - Data Validation
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp12">This review rule checks on User 
    				 Fields in the Products/Services</span> <span lang="EN-US" xml:lang="EN-US" class="hcp14">sub-ledger</span></i> <i><span lang="EN-US" xml:lang="EN-US" class="hcp12">screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t1Row">
    				<td class="t1Col">
    
    R_FIJSECUR
    
    </td>
    				<td class="t2Col">
    
    Accounting &gt; Journals &gt; Securities 
    				 &gt; User Fields - Data Validation
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp12">This review rule checks on User 
    				 Fields in the Securities</span> <span lang="EN-US" xml:lang="EN-US" class="hcp14">sub-ledger</span></i> 
    				 <i><span lang="EN-US" xml:lang="EN-US" class="hcp12">screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t2Row">
    				<td class="t1Col">
    
    R_FIJSHARE
    
    </td>
    				<td class="t2Col">
    
    Accounting &gt; Journals &gt; Share/Unit 
    				 Holder &gt; User Fields - Data Validation
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp12">This review rule checks on User 
    				 Fields in the Share/Unit Holder</span> <span lang="EN-US" xml:lang="EN-US" class="hcp14">sub-ledger</span></i> <i><span lang="EN-US" xml:lang="EN-US" class="hcp12">screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t1Row">
    				<td class="t1Col">
    
    R_FIJTAXAC
    
    </td>
    				<td class="t2Col">
    
    Accounting &gt; Journals &gt; Tax 
    				 Account &gt; User Fields - Data Validation
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp12">This review rule checks on User 
    				 Fields in the Tax Account</span> <span lang="EN-US" xml:lang="EN-US" class="hcp14">sub-ledger</span></i> 
    				 <i><span lang="EN-US" xml:lang="EN-US" class="hcp12">screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t2Row">
    				<td class="t1Col">
    
    R_FSEPAPOS
    
    </td>
    				<td class="t2Col">
    
    Entity Administration &gt; Partners 
    				 &gt; Classes &gt; User Fields - Data Validation
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp17">This 
    				 review rule checks on User Fields in the Partners - Classes</span></i> 
    				 <i><span lang="EN-US" xml:lang="EN-US" class="hcp17">screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t1Row">
    				<td class="t1Col">
    
    R_FSESHCAP
    
    </td>
    				<td class="t2Col">
    
    Entity Administration &gt; Shares 
    				 &gt; Capital &gt; User Fields - Data Validation
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp17">This 
    				 review rule checks on User Fields in the Shares - Capital 
    				 &nbsp;</span></i><i><span lang="EN-US" xml:lang="EN-US" class="hcp17">screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t2Row">
    				<td class="t1Col">
    
    R_FSEUSRFC
    
    </td>
    				<td class="t2Col">
    
    Entity Administration &gt; User Fields 
    				 - Company - Data Validation
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp10">This 
    				 review rule checks on User Fields in the User Fields - 
    				 Company screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t1Row">
    				<td class="t1Col">
    
    R_FSEUSRFF
    
    </td>
    				<td class="t2Col">
    
    Entity Administration &gt; User Fields 
    				 - Fund - Data Validation
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp10">This 
    				 review rule checks on User Fields in the User Fields - 
    				 Fund screen.</span></i>
    
    </td>
    			</tr>
    			<tr class="t2Row">
    				<td class="t1Col">
    
    R_FSEUSRFT
    
    </td>
    				<td class="t2Col">
    
    Entity Administration &gt; User Fields 
    				 - Trust - Data Validation
    
    				
    
    <i><span lang="EN-US" xml:lang="EN-US" class="hcp10">This 
    				 review rule checks on User Fields in the User Fields - 
    				 Trust screen.</span></i>
    
    </td>
    			</tr>
    		</tbody></table>
    		
    
    &nbsp;
     </div>

	

- [Setup/Statutory 
    	 review](javascript:TextPopup(this))
    
    	<div class="droptext" id="POPUP3709444631" style="display: none;">
    		<span lang="EN-US" xml:lang="EN-US" class="hcp3">This type of review 
    		 is to validate the file setup to ensure that users have entered 
    		 required information for the files. For instance, mailing address 
    		 has been entered for all Master Files, registered office address 
    		 has been entered for Entity Files and so on.</span>
    		<span lang="EN-US" xml:lang="EN-US" class="hcp2">In order to 
    		 specify the setup required, reviews tags are required. The review 
    		 tags will ‘tell’ Viewpoint what type of information to check on.</span>
    		&nbsp;
    		<h3>Review Rules for File Setup Review</h3>
    		For the review tags to work for File Setup reviews, there are 
    		 corresponding review rules. By default, the review rules have 
    		 been activated. While you cannot change the review rule, you can 
    		 choose to deactivate the rules that are not applicable.
    		
        			    1. In Viewpoint – Home, go to Configuration &gt; Settings 
        			 &gt; Customise &gt; Review Rules.
        			    1. Select the review rule you want to deactivate.
        			    1. Click Edit.
        			    1. Tick the Deactivate option.
        			    1. Click Update.
        		
    		<span class="hcp9">Note</span>: 
    		 If you deactivate a review rule, the corresponding review tag 
    		 will not be taken into account during the review.
    		&nbsp;
    		See also:
    		
        			    - [Setup/Statutory 
        			 Review - Tags](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Setup_Statutory_Review_-_Tags.htm)
        		
     </div>

	

- [Compliance 
    	 review](javascript:TextPopup(this))
    
    	<div class="droptext" id="POPUP3717382081" style="display: none;">
    		<span lang="EN-GB" xml:lang="EN-GB">Compliance review focuses 
    		 on compliance-related information for the file that are entered 
    		 in the following screens:</span>
    		
        			    - <span lang="EN-GB" xml:lang="EN-GB">Addresses</span>
        			    - <span lang="EN-GB" xml:lang="EN-GB">Identity Details</span>
        			    - <span lang="EN-GB" xml:lang="EN-GB">Identity Register</span>
        			    - <span lang="EN-GB" xml:lang="EN-GB">CDD</span>
        		
    		&nbsp;
    		<span lang="EN-GB" xml:lang="EN-GB">This review scope is used 
    		 to check on certain values and if available, to indicate and update 
    		 fields in the CDD screen. This scope depends on these types Compliance 
    		 Review Rules which are:</span>
    		
        			    - [Compliance 
        			 Review Rules with 'KYREVIEW' Review Code](javascript:TextPopup(this))
        			<div class="droptext" id="POPUP397222280" style="display: none;">
        				These check on the information of the file based on 
        				 the tag configuration of the rule and there are 6 of this 
        				 type of rule - KYREVIEWA, KYREVIEWB, KYREVIEWC, KYREVIEWD, 
        				 KYREVIEWE and KYREVIEWF. Once configured and File Review 
        				 is performed, the results will indicate items that match 
        				 the tag configuration.
        				If necessary, the Compliance Status Fields Rules can 
        				 be used to auto-update the relevant compliance review 
        				 status field.
        				<span lang="EN-GB" xml:lang="EN-GB">One application 
        				 for this can be to look for US links as per FATCA requirements.</span>
        				&nbsp;
           </div>
        			    - [Compliance 
        			 Review Rules with 'KYREVUPD' Review Code](javascript:TextPopup(this))
        			<div class="droptext" id="POPUP397617381" style="display: none;">
        				These rules complement the Compliance Information Review 
        				 Rules and allows for the update of the compliance review 
        				 status fields. Each of this rule corresponds to one of 
        				 the Compliance Information Review Rules e.g.
        				
            					        - Compliance review rules ‘KYREVIEWA’ and ‘KYREVUPDA’ 
            					 for the first compliance review status field
            					        - Compliance review rules ‘KYREVIEWB’ and ‘KYREVUPDB’ 
            					 for the second compliance review status field
            					        - Compliance review rules ‘KYREVIEWC’ and ‘KYREVUPDC’ 
            					 for the third compliance review status field, and 
            					 so on.
            				
        				By default, the first three compliance review status 
        				 fields are enabled with the captions – FATCA, EU Resident 
        				 and UK Resident. The other three are not enabled with 
        				 generic captions. However, all six fields can be identified 
        				 by their Database Field names which are KYC_ReviewA, KYC_ReviewB, 
        				 KYC_ReviewC, KYC_ReviewD, KYC_ReviewE and KYC_ReviewF.
        				You can change the caption and other field settings 
        				 if required, in Configuration &gt; Settings &gt; Customise 
        				 &gt; Field Settings.
        				
            					        1. In Viewpoint - Home, go to Configuration &gt; 
            					 Settings &gt; Customise &gt; Field Settings.
            					        1. Set the following:
            					
                						            - Menu Group = File [8]
                						            - Section = General [FTDMAINF]
                					
            					        1. Click Find and select the CDD screen.
            					        1. Select the compliance review status fields and 
            					 make the changes accordingly.
            				
        				<span class="hcp9">Note</span>: 
        				 If you are unable to view the Database Field, you can 
        				 right-click in the grid and choose Customise/Select. Then 
        				 tick the checkbox in the Show column for Database Field 
        				 and click Apply.
           </div>
        		
    		&nbsp;
    		See also:
    		
        			    - [Compliance 
        			 Review - Tags](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Compliance_Review_-_Tags.htm)
        		
      </div>

	

- [AEOI 
    	 review](javascript:TextPopup(this))
    
    	<div class="droptext" id="POPUP393187142" style="display: none;">
    		<span lang="EN-GB" xml:lang="EN-GB">AEOI review focuses on information 
    		 for the file that relates to CRS and FATCA. This review depends 
    		 on the following review rules:</span>
    		
        			    - [FATCA 
        			 Classification ](javascript:TextPopup(this))
        			<div class="droptext" id="POPUP4823796401" style="display: none;">
        				This review rule is to create a FATCA Classification 
        				 Identity Register Type record where none exist. Tags are 
        				 required to specify the values for this record.
           </div>
        			    - [CRS 
        			 Classification ](javascript:TextPopup(this))
        			<div class="droptext" id="POPUP4824181761" style="display: none;">
        				This review rule is to create a CRS Classification Identity 
        				 Register Type record where none exist. Tags are required 
        				 to specify the values for this record.
           </div>
        			    - [Tax 
        			 Residence and TIN](javascript:TextPopup(this))
        			<div class="droptext" id="POPUP395113680" style="display: none;">
        				This review rule is to create a Tax Residence and Identification 
        				 Number record where none exist. Tags are required to specify 
        				 the values for this record.
           </div>
        			    - [Indicia 
        			 and Curing Status - Expiration of Curing Deadline](javascript:TextPopup(this))
        			<div class="droptext" id="POPUP4813170341" style="display: none;">
        				This review rule is to notify and update the reporting 
        				 status once the curing deadline has expired.
           </div>
        			    - [Reportable 
        			 Account](javascript:TextPopup(this))
        			<div class="droptext" id="POPUP3988965591" style="display: none;">
        				This review rule will create the Reportable Account 
        				 record if it does not exist&nbsp;for the specified Reporting 
        				 Authority and where
        				
            					        - the reporting FI entity is selected for Entity 
            					 Administration (i.e. Refmaster.CS=1)
            					        - the reporting FI does not have a FATCA or CRS 
            					 Reporting status of ‘Not Reporting’
            					        - the relevant relations of the selected reporting 
            					 FI file have an ‘Indicia Review’ identity register 
            					 record and are Reportable
            				
        				This rule will use the tag values of the review rule 
        				 ‘CRSREVIEW’ to determine if the Master File is an Entity 
        				 and reportable by two tags defined below:
        				
            					        - [RVW.CONTROL.ENTCLASS.IdType=FCSC,FCRS]
            					        - [RVW.CONTROL.ENTCLASS.NFI.LookValue:N]
            				
           </div>
        			    - [Indicia 
        			 and Curing Review](javascript:TextPopup(this))
        			<div class="droptext" id="POPUP3991725851" style="display: none;">
        				This rule is used to automate indicia search. The tag 
        				 configuration for this rule specifies the relevant relations 
        				 to include for the review. Results from this review is 
        				 used by these rules:
        				
            					        - Create Reportable Account
            					        - <span lang="EN-GB" xml:lang="EN-GB">C</span>reate 
            					 FATCA Classification in the Identity Register
            					        - Create CRS Classification in the Identity Register
            				
           </div>
        		
    		&nbsp;
    		See also:
    		
        			    - [AEOI Review - Tags](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/AEOI_Review_-_Tags.htm)
        		
      </div>

	

- [Filings, 
    	 Meeting, Reviews](javascript:TextPopup(this))
    
    	<div class="droptext" id="POPUP391304367" style="display: none;">
    		These refer to the Meetings, Filings and Reviews screen and 
    		 is used to check if the necessary types have been created for 
    		 the Master File. If required, tags can be used to create the records.
    		&nbsp;
    		&nbsp;
    		See also:
    		
        			    - [Meetings, 
        			 Filings, Reviews - Tags](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Meetings,_Filings,_Reviews_-_Tags.htm)
        		
     </div>

If there should be any conflict or missing items, users will be informed 
 in the File Review screen so that action can be taken to add or correct 
 the relevant items. Note that File Review will also work on encrypted 
 fields when [Confidential Database](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Confidential_Database.htm) 
 is used.

&nbsp;

&nbsp;
## Change Code for File Review
<span lang="EN-US" xml:lang="EN-US">The Change Code ‘FLRW – File Review 
 – Run’ is introduced to record when a File Review is performed. Details 
 for this change include:</span>

	

- <span lang="EN-US" xml:lang="EN-US">The Master File that is reviewed.</span>

	

- <span lang="EN-US" xml:lang="EN-US">The date and time the File Review was 
    	 performed.</span>

	

- <span lang="EN-US" xml:lang="EN-US">Where the File Review was performed:</span>

	

    - 
        		
        
    - <span lang="EN-US" xml:lang="EN-US">Global File Review - Means it was 
        		 done in Viewpoint - Home.</span>
        
        
        		
    - <span lang="EN-US" xml:lang="EN-US">File Level - Means this it was done 
        		 in File Maintenance or File Enquiry screen.</span>
        
        
        		
    - <span lang="EN-US" xml:lang="EN-US">Relations/Ownership - Means it was 
        		 done in the Relations Enquiry or Ownership Enquiry screen.</span>
        
        
        	

	

- <span lang="EN-US" xml:lang="EN-US">The user who performed the File Review.</span>

<span class="hcp9">Note</span>: When performing 
 File Review on multiple Master Files, there will be a change record for 
 each of the Master File. For example, in Relations screen, if there are 
 three Master Files that were reviewed, there will be three ‘FLRW’ change 
 records.

&nbsp;

&nbsp;

See also:

	

- [File Review - Tags](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/File_Review_-_Tags.htm)

	

- [Review Rules](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Review_Rules.htm)


 
&nbsp;

[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; File Review Function
 
&nbsp;
 
(c) Viewpoint Software for 
 Business Ltd
 
Version: 8.0.2022.09.20




