




# Activity Budget
Activity Budget feature is introduced for administrative and financial 
 planning purposes. The Activity Budget screen can be used to record any 
 budget that is related to the selected activity as well as verify it for 
 invoicing. It can be accessed by clicking on the 'Budget' command button 
 under the Activities screen in Viewpoint - Home or File Maintenance. As 
 such, you can review and update the info on this screen.

<span style="font-weight: bold; font-style: italic;">Note:</span> To 
 use Activity Budget, you must have valid Viewpoint Practice Management 
 and Time and Disbursement component licenses apart from the Viewpoint 
 Entity Administration license. Likewise, a valid Viewpoint Workflow license 
 is required if you are also using workflows.

&nbsp;

Activity Description

This will display the activity record description.

&nbsp;

Date Due

This will display the due date of the activity record.

&nbsp;

Matter Currency

This will display the matter currency for the activity record.

&nbsp;

Services list

This shows the [services](javascript:TextPopup(this)) 
 that have been created; including services created in the Activities Profiles 
 screen's Budget Template.
<div class="droptext" id="POPUP608850297" style="display: none;">
	<p>Fields listed in the table below are the defaults for the Activity 
	 Budget screen. </p>
	<p>&nbsp;</p>
	<table style="left: 0px; top: 46px;" cellspacing="0" width="749">
		<colgroup><col style="width: 38.652%;">
		<col style="width: 61.348%;">
		</colgroup><tbody><tr style="height: 33px;">
			<td style="border-top-color: rgb(128, 128, 128); border-top-style: solid; border-top-width: 1px; border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px; border-left-color: rgb(128, 128, 128); border-left-style: solid; border-left-width: 1px;" bgcolor="#C0C0C0"><p><span class="hcp1">Fields</span></p></td>
			<td style="border-top-color: rgb(128, 128, 128); border-top-style: solid; border-top-width: 1px; border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px;" bgcolor="#C0C0C0"><p><span class="hcp1">Explanation</span></p></td>
		</tr>
		<tr style="height: 81px;">
			<td class="hcp2"><p>Code</p></td>
			<td class="hcp3"><p>This 
			 field will display the Service Code. Add/Edit budget lines 
			 by entering a Service Code. Alternatively, you can press F12 
			 to select the available services. This field will default 
			 to the template's Service Code if applicable. </p></td>
		</tr>
		<tr style="height: 83px;">
			<td class="hcp2"><p>Service Description</p></td>
			<td class="hcp3"><p>This 
			 field will display the description for the service. Add/Edit 
			 budget lines by entering the service description. <span class="hcp4">Alternatively, 
			 you can press F12 to select the available services. This field 
			 will default to the template's description for the service 
			 if applicable.</span> </p></td>
		</tr>
		<tr style="height: 47px;">
			<td class="hcp2"><p>Fee Type</p></td>
			<td class="hcp3"><p>This 
			 field displays the Service Class of the service. This field 
			 will default to the template's Service Class of the service 
			 if applicable.</p></td>
		</tr>
		<tr style="height: 55px;">
			<td class="hcp2"><p>Selected</p></td>
			<td class="hcp3"><p><span class="hcp3">This field will default to the template's 'Default 
			 Selected' field and can be changed if necessary. Note that 
			 this field will be non-editable if the 'Required' field is 
			 ticked in Budget Template screen. </span>&nbsp;</p></td>
		</tr>
		<tr style="height: 64px;">
			<td class="hcp2"><p>Budget Units</p></td>
			<td class="hcp3"><p><span class="hcp3">Fill in this field to record budget units for 
			 the service.</span> Note that this field will not be applicable 
			 for Time Service Class and will be disabled. This field will 
			 default to the template's 'Budget Units' field if applicable.</p></td>
		</tr>
		<tr style="height: 75px;">
			<td class="hcp2"><p>Book Time</p></td>
			<td class="hcp3"><p><span class="hcp3">Tick this field if time entries are applicable 
			 for the service. Note that this field will not be applicable 
			 for Disbursement Service Class and will be disabled. This 
			 field will default to the template's 'Book Time' field if 
			 applicable.</span> </p></td>
		</tr>
		<tr style="height: 62px;">
			<td class="hcp2"><p>Time Budget</p></td>
			<td class="hcp3"><p><span class="hcp3">Fill in this field to record time budget units 
			 for the service. If 'Book Time' field is unticked, it will 
			 be disabled.</span> This field will default to the template's 
			 'Time Budget' field if applicable.</p></td>
		</tr>
		<tr style="height: 62px;">
			<td class="hcp2"><p>Charge</p></td>
			<td class="hcp3"><p><span class="hcp3">Tick this field to indicate whether or not the 
			 service is chargeable. Note that this field is always enabled. 
			 This field will default to the template's 'Charge' field if 
			 applicable.</span></p></td>
		</tr>
		<tr style="height: 81px;">
			<td class="hcp2"><p>Charge to Rec. Fee</p></td>
			<td class="hcp3"><p>Tick 
			 this field to charge the service as a Recurring Fee. Note 
			 that this field is unticked by default. This field will be 
			 enabled when there is an active Running Fee with the same 
			 Service Code and the 'Allow Rec. Fee' is ticked in the Budget 
			 Template screen. </p></td>
		</tr>
		<tr style="height: 50px;">
			<td class="hcp2"><p>CCY</p></td>
			<td class="hcp3"><p>This 
			 field displays the Matter currency and it is always disabled.</p></td>
		</tr>
		<tr style="height: 63px;">
			<td class="hcp2"><p>Unit Price</p></td>
			<td class="hcp3"><p><span class="hcp3">Fill in this field to record unit prices for 
			 the service. For Product and Disbursement Service Class, this 
			 field will default to the service fee using the related Matter 
			 currency.</span> It will be disabled for Time Service Class.</p></td>
		</tr>
		<tr style="height: 47px;">
			<td class="hcp2"><p>Discount</p></td>
			<td class="hcp3"><p><span class="hcp3">Fill in this field to record the discount for 
			 the service. Note that this field is defaulted to 0 (zero) 
			 and will only be enabled for the Product Service Class.</span></p></td>
		</tr>
		<tr style="height: 47px;">
			<td class="hcp2"><p>Budget</p></td>
			<td class="hcp3"><p><span class="hcp3">This field is calculated as (Budget Units x Unit 
			 Price) x (1 - Discount) and will always be disabled.</span> 
			 </p></td>
		</tr>
		<tr style="height: 47px;">
			<td class="hcp2"><p>User Guidance</p></td>
			<td class="hcp3"><p>This 
			 field will display the guidance text included in the template's 
			 'User Guidance' field. It is a read-only field.</p></td>
		</tr>
	</tbody></table>
</div>
&nbsp;

Command buttons

Click on the relevant command button to perform the necessary.

	

- <span class="hcp5">Add Line</span> - Click this 
    	 to [add](javascript:TextPopup(this)) 
    	 new service line for the activity. Note that this button will be disabled 
    	 if 'Budget Verified' checkbox is ticked. 
    
    	<div class="droptext" id="POPUP612640663" style="display: none;">
    		
        			    1. Click Add Line.
        			    1. Enter Service Code and Service Description. Alternatively, 
        			 you can press F12 to select available services.
        			    1. Click Update once complete.
        		
     </div>

	

- <span class="hcp5">Reset</span> - Click this to 
    	 reset any changes made to the original settings. Note that this button 
    	 will be disabled if 'Budget Verified' checkbox is ticked.

	

- <span class="hcp5">Update</span> - Click this 
    	 update the changes made.

	

- <span class="hcp5">Cancel</span> - Click this 
    	 to cancel the changes made.

Activity Status

This will show the activity [status](javascript:TextPopup(this)) 
 for the activity record and you can edit it, if necessary.
 
<div class="droptext" id="POPUP566057164" style="display: none;">
	

The available statuses are:

	
		

- Actionable - This indicate that the activity is still incomplete.

		

- Alert/Message - This indicate that the activity has an alert 
    		 or message.

		

- Cancelled - This indicate that the activity has been cancelled.

		

- Completed - This indicate that the activity is completed.

		

- In Progress - This indicate that the is still in progress.

		

- New - This indicate that the activity is still new.

		

- Paused - This indicate that the activity is in paused.

		

- Workflows/Forms Completed - This indicate that the activity 
    		 workflows/forms are completed.

	
 </div>

&nbsp;

Options

<span class="hcp5">Budget Verified</span> - Tick this 
 option to verify the budget for invoicing. Note that when ticked, the 
 entire Budget Grid can no longer be edited along with the 'Add Line' and 
 'Reset' command buttons being disabled.

<span class="hcp5">Invoice Separately</span> -&nbsp;Tick 
 this option if you want to generate the invoice separately for Time and 
 Disbursement. If this field is left unticked, the draft invoice for Time 
 and Disbursement will be generated along with the Product Service Class 
 via the Posting of WIP screen. Note that this option will also be updated 
 based on the Invoice Separately option in Activities Profiles.

<span class="hcp5">Open for Time &amp; Disbursement</span> 
 - Tick this option to record Time and Disbursement for this activity. 
 This option will be ticked by default if the activity created has an 'Actionable' 
 status.

<span class="hcp5">Ready for Invoicing</span> - Tick this 
 to indicate that the activities are ready to be invoiced. Click [here](javascript:TextPopup(this)) 
 for more information. 
 
<div class="droptext" id="POPUP594467703" style="display: none;">
	

This option will also be disabled unless 'Budget Verified' option 
	 is ticked. However, if 'Ready for Invoicing' option is ticked while 
	 'Budget Verified' option is unticked, a warning message will be prompted. 
	 (Selecting Yes will disable and untick the 'Ready for Invoicing' option. 
	 / Selecting No will disable the 'Ready for Invoicing' option but it 
	 will still remain ticked.) Note that invoice will not be generated 
	 via Posting of WIP if 'Invoice Separately' option is ticked. 
 </div>

&nbsp;

See also:

	

- [Activities Profiles](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Activities_Profiles.htm)

	

- [Activities](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Activities.htm)

	

- [Activity Explorer](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Activity_Explorer.htm)

	

- [Posting 
    	 of WIP](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Practice_Manager/Posting_of_Work_in_Progress.htm)

	

- [Budget Template](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Budget_Template.htm)

&nbsp;

 
&nbsp;

[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; Activity Budget
 
&nbsp;
 
(c) Viewpoint Software for 
 Business Ltd
 
Version: 8.0.2022.09.20




