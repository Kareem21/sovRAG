




# Meetings, Filings, Reviews - Tags
For the Meetings, Filings and Reviews screens, tags are available to 
 check on the type, record and action for these three screens. The tags 
 are similar for all three screens. Refer to [File 
 Review Function](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/File_Review_Function.htm) to see where the tags can be added.

In the Type, Record and Action topics below, replace &lt;Screen&gt; 
 with the two-character code below to specify which screen the type/record/action 
 tag affects.

	

- FL - Filing

	

- MG - Meeting

	

- RV - Review

The use of the tags allows for the following scenarios:

<table class="Table1" style="border-collapse: separate;" cellspacing="0px" border="1">
	<colgroup><col width="95">
	<col width="165">
	<col width="165">
	<col width="165">
	<col width="165">
	</colgroup><tbody><tr class="t1st">
		<td>

&nbsp;

</td>
		<td>

Scenario 
		 1

</td>
		<td>

Scenario 
		 2

</td>
		<td>

Scenario 
		 3

</td>
		<td>

Scenario 
		 4

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

Type

</td>
		<td class="t2Col">

Auto-created by File Review on first run

</td>
		<td class="t1Col">

User create manually

</td>
		<td class="t2Col">

User create manually

</td>
		<td class="t1Col">

Auto-created by File Review on first run

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">

Record

</td>
		<td class="t2Col">

Auto-created by File Review on first run

</td>
		<td class="t1Col">

Auto-created by File Review on first run

</td>
		<td class="t2Col">

User create manually

</td>
		<td class="t1Col">

User create manually

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

Action

</td>
		<td class="t2Col">

Auto-created by File Review on first run

</td>
		<td class="t1Col">

Auto-created by File Review on first run

</td>
		<td class="t2Col">

Auto-created by File Review on first run

</td>
		<td class="t1Col">

Auto-created by File Review on second run

</td>
	</tr>
</tbody></table>

&nbsp;

[Click here for 
 example of tag configuration to the scenarios above.](javascript:TextPopup(this))
<div class="droptext" id="POPUP433366507" style="display: none;">
	<p>[FL.TP.Required:F1,F4]</p>
	<p>[FL.TP.Optional:F2,F3]</p>
	<p>&nbsp;</p>
	<p>===== F1====</p>
	<p>[FL.TP.F1:</p>
	<p>FilingType=F1</p>
	<p>FilingName=Filing Type 1</p>
	<p>FilingFreq=Y</p>
	<p>]</p>
	<p>[FL.RC.F1:</p>
	<p>FlDescription=Filing Type 1 – Record 1</p>
	<p>FlNote=Note to the accounts</p>
	<p>PeriodFrom=#NOW</p>
	<p>PeriodTo=#NOW+365</p>
	<p>DateDue=#NOW+370</p>
	<p>PreparedBy=ERNST&amp;YO</p>
	<p>]</p>
	<p>[FL.AC.F1.1:</p>
	<p>ActionCode=PR</p>
	<p>ActionDescr=Preparation</p>
	<p>ActionNote=Full Accounts</p>
	<p>AdminCode=@EN.AdminCode</p>
	<p>FileCode= ERNST&amp;YO</p>
	<p>DateSet=#NOW</p>
	<p>DateDue=#NOW+35]</p>
	<p>&nbsp;</p>
	<p>===== F4====</p>
	<p>[FL.TP.F4:</p>
	<p>FilingType=F4</p>
	<p>FilingName=Filing Type 4</p>
	<p>FilingFreq=Y</p>
	<p>]</p>
	<p>[FL.RC.F4:</p>
	<p>+AutoAddActions=Y</p>
	<p>]</p>
	<p>[FL.AC.F4.1:</p>
	<p>ActionCode=PR</p>
	<p>ActionDescr=Preparation</p>
	<p>ActionNote=Full Accounts</p>
	<p>AdminCode=@EN.AdminCode</p>
	<p>FileCode= ERNST&amp;YO</p>
	<p>DateSet=#NOW</p>
	<p>DateDue=#NOW+35]</p>
	<p>&nbsp;</p>
	<p>===== F2====</p>
	<p>[FL.RC.F2:</p>
	<p>FlDescription=Filing Type 2 – Record 1</p>
	<p>FlNote=Note to the accounts</p>
	<p>PeriodFrom=#NOW</p>
	<p>PeriodTo=#NOW+365</p>
	<p>DateDue=#NOW+370</p>
	<p>PreparedBy= ERNST&amp;YO</p>
	<p>]</p>
	<p>[FL.AC.F2.1:</p>
	<p>ActionCode=PR</p>
	<p>ActionDescr=Preparation</p>
	<p>ActionNote=Full Accounts</p>
	<p>AdminCode=@EN.AdminCode</p>
	<p>FileCode= ERNST&amp;YO</p>
	<p>DateSet=#NOW</p>
	<p>DateDue=#NOW+35]</p>
	<p>&nbsp;</p>
	<p>===== F3====</p>
	<p>[FL.RC.F3:</p>
	<p>+AutoAddActions=Y</p>
	<p>]</p>
	<p>[FL.AC.F3.1:</p>
	<p>ActionCode=PR</p>
	<p>ActionDescr=Preparation</p>
	<p>ActionNote=Full Accounts</p>
	<p>AdminCode=@EN.AdminCode</p>
	<p>FileCode= ERNST&amp;YO</p>
	<p>DateSet=#NOW</p>
	<p>DateDue=#NOW+35]</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p>&nbsp;</p>
	<p><span class="hcp4">Note</span>: 
	 Replace the Filing Type F1, F2, F3 and F4 with your own Filing type 
	 code.</p>
</div>
&nbsp;
### Type
Use these to check and create Meeting, Filing and Review types.

<table class="Table1" style="border-top-color: rgb(0, 0, 0); border-top-style: solid; border-top-width: 1px; border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; border-left-color: rgb(0, 0, 0); border-left-style: solid; border-left-width: 1px;" cellspacing="0px" width="100%">
	<colgroup><col style="width: 33.333%;">
	<col style="width: 33.333%;">
	<col style="width: 33.333%;">
	</colgroup><tbody><tr class="t1st">
		<td class="hcp5">

Tag

</td>
		<td class="hcp6">

Explanation

</td>
		<td class="hcp6">

Example

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="border-left-color: rgb(128, 128, 128); border-left-style: solid; border-left-width: 1px; border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px;">

[&lt;Screen&gt;.TP.Required:&lt;Code&gt;]

		

where &lt;Code&gt; refers to the code for the type or sub-type.

		

&nbsp;

		

<span class="hcp4">Note</span>: 
		 Sub-type is available only for Filings.

</td>
		<td class="t2Col" style="border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This tag will check for the specified 
		 type. If the type has not been created, you can use the tag in 
		 the second row to have the type created when you click Post Update 
		 after running File Review.

		

This is required for Scenario 1 and 4.

</td>
		<td class="t1Col" style="border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

[FL.TP.Required:AR]

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" rowspan="2" style="border-left-color: rgb(128, 128, 128); border-left-style: solid; border-left-width: 1px; border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px;">

[&lt;Screen&gt;.TP.&lt;Code&gt;:

		

&lt;Field&gt;=&lt;Value&gt;

		

&lt;Field&gt;=&lt;Value&gt;

		

...

		

]

		

where:

		
			

- <span class="hcp8">&lt;Field&gt;</span> 
    			 refers to mandatory fields for the type.

			

- <span class="hcp8">&lt;Value&gt;</span> 
    			 refers to the values for the fields.

		</td>
		<td class="t2Col" style="border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This tag will auto-create the type 
		 and must be used with the tag above.

		

This is required for Scenario 1 and 4.

</td>
		<td class="t1Col" style="border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

[FL.TP.AR:

		

FilingType=AR

		

FilingName=Annual Return

		

FilingFreq=Y

		

]

</td>
	</tr>
	<tr class="t2Row">
		<td class="t2Col" style="border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

If a Filing type has been deactivated 
		 but you would like the option to reactivate it during File Review, 
		 add this tag:

		

+AllowInact=N

		

With this tag, you will see a prompt during File Review enabling 
		 you to reactivate the type and have a new record for the type 
		 to be created again.

		

Without this tag, the type will stay inactive.

</td>
		<td class="t1Col" style="border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

[FL.TP.AR:

		

FilingType=AR

		

FilingName=Annual Return

		

FilingFreq=Y

		

+AllowInact=N

		

]

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="border-left-color: rgb(128, 128, 128); border-left-style: solid; border-left-width: 1px; border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px;">

[&lt;Screen&gt;.TP.Optional:&lt;Code&gt;]

		

&nbsp;

</td>
		<td class="t2Col" style="border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This tag is used if the type is not 
		 required for every file. However, if the type does apply, then 
		 user needs to manually set up the type but File Review can be 
		 used to create record and action once the type exists.

		

This is for Scenario 2 and 3.

</td>
		<td class="t1Col" style="border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

[FL.TP.Optional:AC]

</td>
	</tr>
</tbody></table>

<span class="hcp4">Note</span>: You 
 can refer to Configuration &gt; Settings &gt; Customise &gt; Field Settings 
 to see which fields are mandatory and the field name in database (Database 
 Field).

&nbsp;
### Record
Use these tags to create Meeting, Filing and Review records.

<table class="Table1" style="border-top-color: rgb(0, 0, 0); border-top-style: solid; border-top-width: 1px; border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; border-left-color: rgb(0, 0, 0); border-left-style: solid; border-left-width: 1px;" cellspacing="0px" width="95.023%">
	<colgroup><col style="width: 33.333%;">
	<col style="width: 33.333%;">
	<col style="width: 15.535%;">
	</colgroup><tbody><tr class="t1st">
		<td class="hcp5">

Tag

</td>
		<td class="hcp6">

Explanation

</td>
		<td class="hcp9">

Example

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" rowspan="3" style="border-left-color: rgb(128, 128, 128); border-left-style: solid; border-left-width: 1px; border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

[&lt;Screen&gt;.RC.&lt;Code&gt;:

		

&lt;Field&gt;=&lt;Value&gt;

		

&lt;Field&gt;=&lt;Value&gt;

		

...

		

]

		

where:

		
			

- <span class="hcp8">&lt;Field&gt;</span> 
    			 refers to mandatory fields for the record.

			

- <span class="hcp8">&lt;Value&gt;</span> 
    			 refers to the values for the fields.

		</td>
		<td class="t2Col" style="border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This tag will auto-create the first 
		 record for the specified type with the fields set to the defined 
		 values. You need this tag for Scenario 1 and 2.

		

Once the related actions have been completed, you can deactivate 
		 the record and re-run File Review to get the next record.

</td>
		<td class="t1Col" style="border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

[FL.RC.AR:

		

FlDescription=Annual Return

		

<span class="hcp10">PeriodFrom=@EN.AcctYearEnd-365</span>

		

PeriodTo=@EN.AcctYearEnd

		

DateDue=#NOW

		

PreparedBy=@REL.AUD

		

FiledBy=@REL.AUD

		

]

		

&nbsp;

</td>
	</tr>
	<tr class="t1Row">
		<td class="t2Col" style="border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

If you require more than one active 
		 record, you can add the following codes:

		<table style="border-top-color: rgb(128, 128, 128); border-top-style: solid; border-top-width: 1px; border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px; border-left-color: rgb(128, 128, 128); border-left-style: solid; border-left-width: 1px; vertical-align: top; border-collapse: separate;" cellspacing="0">
			<colgroup><col style="width: 50%;">
			<col style="width: 50%;">
			</colgroup><tbody><tr>
				<td style="border-left-color: rgb(0, 0, 0); border-left-style: solid; border-left-width: 1px; border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px; border-top-color: rgb(0, 0, 0); border-top-width: 1px;">

Code

</td>
				<td style="border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px; border-top-color: rgb(0, 0, 0); border-right-color: rgb(0, 0, 0); border-top-width: 1px; border-right-width: 1px;">

Explanation

</td>
			</tr>
			<tr>
				<td class="hcp11">

CreateDue=&lt;NumberofDays&gt;

</td>
				<td class="hcp12">

This will create the 
				 next record if it is due when you run File Review again.

</td>
			</tr>
			<tr>
				<td class="hcp11">

+RollDate=&lt;DateField1&gt;,&lt;DateField2&gt;...

</td>
				<td class="hcp12">

This is to roll the specified 
				 dates for the next record.

</td>
			</tr>
			<tr>
				<td class="hcp11">

+CopyField=&lt;Field1&gt;,&lt;Field2&gt;,..

</td>
				<td class="hcp12">

This is to copy the fields 
				 for the next record.

</td>
			</tr>
			<tr>
				<td style="border-left-color: rgb(0, 0, 0); border-left-style: solid; border-left-width: 1px; border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-width: 1px;">

+RollActions=&lt;Action 
				 Type&gt;

</td>
				<td style="border-right-color: rgb(0, 0, 0); border-bottom-color: rgb(0, 0, 0); border-bottom-width: 1px; border-right-width: 1px;">

This 
				 is to create the related actions when creating the next 
				 record. 

				

To define multiple action types, use ',' to separate 
				 the Action Type. 

				

Use '*' to create all action types.

</td>
			</tr>
		</tbody></table>
		

The next record is considered due if:

		
			

- The date in - To field for Filings and Reviews is the 
    			 same as or before <span class="hcp8">Date X</span>.

			

- The date in Date Schedule field for Meetings is the 
    			 same as or before <span class="hcp8">Date X</span>.

		
		
Date X is calculate as <span class="hcp8">[Today]</span> 
		 - <span class="hcp8">&lt;NumberofDays&gt;</span> 
		 where

		
			

- <span class="hcp8">[Today]</span> is the 
    			 date you run File Review.

			

- <span class="hcp8">&lt;NumberofDays&gt;</span> 
    			 is the value set for CreateDue.

		</td>
		<td class="t1Col" style="border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

[FL.RC.AR:

		

CreateDue=180

		

FlDescription=Annual Return

		

<span class="hcp10">PeriodFrom=@EN.AcctYearEnd-365</span>

		

PeriodTo=@EN.AcctYearEnd

		

DateDue=#NOW

		

PreparedBy=@REL.AUD

		

FiledBy=@REL.AUD

		

+RollDate=PeriodFrom,PeriodTo

		

+CopyField=FlDescription

		

+RollActions=*

		

]

</td>
	</tr>
	<tr class="t2Row">
		<td class="t2Col" style="border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

If the first record is to be manually 
		 created but you want subsequent records to be auto-created by 
		 File Review, add this tag:

		

+AutoCreate=N

</td>
		<td class="t1Col">&nbsp;</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="border-left-color: rgb(128, 128, 128); border-left-style: solid; border-left-width: 1px; border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px;">

[&lt;Screen&gt;.RC.&lt;Code&gt;:

		

+AutoAddActions=Y

		

]

</td>
		<td class="t2Col" style="border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This will not auto-create the record 
		 but checks if the record already exists. If it exists, then File 
		 Review can auto-create the actions.

		

You require this tag for Scenario 3 and 4.

</td>
		<td class="t1Col">&nbsp;</td>
	</tr>
</tbody></table>

&nbsp;
### Action
Use these tags to create Meeting, Filing and Review actions.

<table class="Table1" style="border-top-color: rgb(0, 0, 0); border-top-style: solid; border-top-width: 1px; border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; border-left-color: rgb(0, 0, 0); border-left-style: solid; border-left-width: 1px;" cellspacing="0px" width="100%">
	<colgroup><col style="width: 33.333%;">
	<col style="width: 33.333%;">
	<col style="width: 33.333%;">
	</colgroup><tbody><tr class="t1st">
		<td class="hcp5">

Tag

</td>
		<td class="hcp9">

Explanation

</td>
		<td class="hcp9">

Example

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="border-left-color: rgb(128, 128, 128); border-left-style: solid; border-left-width: 1px; border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px;">

[&lt;Screen&gt;.AC.&lt;Code&gt;.&lt;ActionNr&gt;:

		

&lt;Field&gt;=&lt;Value&gt;

		

&lt;Field&gt;=&lt;Value&gt;

		

...

		

]

		

where:

		
			

- <span class="hcp8">&lt;ActionNr&gt;</span> 
    			 refers to the number for the action.

			

- <span class="hcp8">&lt;Field&gt;</span> 
    			 refers to mandatory fields for the type.

			

- <span class="hcp8">&lt;Value&gt;</span> 
    			 refers to the values for the fields.

		</td>
		<td class="t2Col" style="border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This tag will auto-create the action 
		 for the specified type with the fields set to the defined values. 
		 If you have multiple actions, number them according to the order 
		 you want.

		

You require this tag for all scenarios.

</td>
		<td class="t1Col" style="border-right-color: rgb(128, 128, 128); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(128, 128, 128); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

[FL.AC.AR.1:

		

ActionCode=PR

		

ActionDescr=Prepare Draft

		

AdminCode=@EN.AdminCode

		

FileCode=@REL.AUD

		

DateSet=#NOW

		

DateDue=#NOW+35]

</td>
	</tr>
</tbody></table>

&nbsp;
### Function Codes
For the values, you can enter the value directly or use the following 
 function code:

<table class="Table1" cellspacing="0px" width="76.772%">
	<colgroup><col style="width: 27.463%;">
	<col style="width: 43.311%;">
	<col style="width: 29.226%;">
	</colgroup><tbody><tr class="t1st">
		<td style="border-top-color: rgb(0, 0, 0); border-top-style: solid; border-top-width: 1px; border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; border-left-color: rgb(0, 0, 0); border-left-style: solid; border-left-width: 1px;">

Function 
		 Code

</td>
		<td class="hcp13">

Explanation

</td>
		<td class="hcp13">

Example 
		 and Usage

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="border-left-color: rgb(0, 0, 0); border-left-style: solid; border-left-width: 1px; border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

@MF.&lt;Field&gt;

</td>
		<td class="t2Col" style="border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This will 
		 retrieve the specified field from the RefMaster table.

</td>
		<td class="t1Col" style="border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

@MF.RefCode

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="border-left-color: rgb(0, 0, 0); border-left-style: solid; border-left-width: 1px; border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

@EN.&lt;Field&gt;

</td>
		<td class="t2Col" style="border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This will 
		 retrieve the specified field from the Entity table.

</td>
		<td class="t1Col" style="border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

@EN.AdminCode

		

e.g.

		

AdminCode=@EN.AdminCode

		

&nbsp;

		

@EN.IncorpDate

		

e.g. PeriodTo=@EN.IncorpDate

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="border-left-color: rgb(0, 0, 0); border-left-style: solid; border-left-width: 1px; border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

@CA.&lt;Field&gt;

</td>
		<td class="t2Col" style="border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This will 
		 retrieve the specified field from the EntityAccount table.

</td>
		<td class="t1Col" style="border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

@CA.AdminCode

		

e.g.

		

AdminCode=@CA.AdminCode

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="border-left-color: rgb(0, 0, 0); border-left-style: solid; border-left-width: 1px; border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

@RM.&lt;Field&gt;

</td>
		<td class="t2Col" style="border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This will 
		 retrieve the specified field from the RmClients table.

</td>
		<td class="t1Col" style="border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

@RM.AdminCode

		

e.g.

		

AdminCode=@RM.AdminCode

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="border-left-color: rgb(0, 0, 0); border-left-style: solid; border-left-width: 1px; border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

@TR.&lt;Field&gt;

</td>
		<td class="t2Col" style="border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This will 
		 retrieve the specified field from the RmSupplier table.

</td>
		<td class="t1Col" style="border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

@TR.AdminCode

		

e.g.

		

AdminCode=@TR.AdminCode

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="border-left-color: rgb(0, 0, 0); border-left-style: solid; border-left-width: 1px; border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

@RLU.&lt;TypeCode&gt;

</td>
		<td class="t2Col" style="border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This will 
		 retrieve the user code of specified relation type.

</td>
		<td class="t1Col" style="border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

@RLU.AGT

		

e.g.

		

AdminCode=@RLU.AGT

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="border-left-color: rgb(0, 0, 0); border-left-style: solid; border-left-width: 1px; border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

@USERCODE

</td>
		<td class="t2Col" style="border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This will 
		 retrieve the user code of the user running the File Review.

</td>
		<td class="t1Col" style="border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

@USERCODE

		

e.g.

		

AdminCode=@USERCODE

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="border-left-color: rgb(0, 0, 0); border-left-style: solid; border-left-width: 1px; border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

@REL.&lt;RelCode&gt;

</td>
		<td class="t2Col" style="border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This will 
		 retrieve the specified relation type.

</td>
		<td class="t1Col" style="border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

@REL.AUD

		

e.g. &nbsp;&nbsp;

		

PreparedBy=@REL.AUD

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="border-left-color: rgb(0, 0, 0); border-left-style: solid; border-left-width: 1px; border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

#NOW

		

&nbsp;

</td>
		<td class="t2Col" style="border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This applies 
		 only to date fields and will set the value to today’s date.

		

&nbsp;

</td>
		<td class="t1Col" style="border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

e.g.

		

PeriodFrom=#NOW

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="border-left-color: rgb(0, 0, 0); border-left-style: solid; border-left-width: 1px; border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

#NOW+&lt;Number&gt;

</td>
		<td class="t2Col" style="border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This applies 
		 only to date fields and will set the value to a date in the future.

		

&nbsp;

</td>
		<td class="t1Col" style="border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

e.g.

		

PeriodTo=#NOW+365

</td>
	</tr>
</tbody></table>

&nbsp;
#### Parameters for Date Fields
For date fields, the following additional parameters can be added to 
 the function code as well:

<table class="Table1" style="border-collapse: separate;" cellspacing="0px" width="60.078%" border="1">
	<colgroup><col style="width: 17.315%;">
	<col style="width: 82.685%;">
	</colgroup><tbody><tr class="t1st">
		<td>Parameter</td>
		<td>Explanation</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

&lt;Number&gt;

</td>
		<td class="t2Col" style="vertical-align: top;">

Number of &lt;Period&gt; 
		 where 

		
			

- a positive number (with a plus sign) is for a date in 
    			 the future

			

- a negative number is for a date in the past

			

- zero represents the current &lt;Period&gt;

		
		
<span class="hcp4">Note</span>: 
		 This is to be omitted when &lt;Period&gt; refers to quarters.

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="vertical-align: top;">

&lt;Period&gt;

</td>
		<td class="t2Col" style="vertical-align: top;">

Time period where 
		 it can be 

		
			

- Standard periods such as:

			

- Y - Year

			

- M - Month

			

- W - Week

			

- D - Day

			

- Quarters with:

			

- Q referring to the current 
    			 Quarter for the same year

			

- Q1 referring to Quarter 1 
    			 (January - March) of the same year

			

- Q2 referring to Quarter 2 
    			 (April - June) of the same year

			

- Q3 referring to Quarter 3 
    			 (July - September) of the same year

			

- Q4 referring to Quarter 4 
    			 (October - December) of the same year

		
		
<span class="hcp4">Note</span>: 
		 If the &lt;Period&gt; is day, this can be omitted.

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

&lt;Code&gt;

</td>
		<td class="t2Col" style="vertical-align: top;">

Additional code 
		 to denote the first day or last day of the specified time period 
		 with:

		
			

- S - being the first day

			

- E - being the last day

		
		
This parameter is optional and where if it is not specified 
		 for standard periods, for subsequent records, the date will be 
		 rolled as follows:

		
			

- 28-Apr-2019 to 28-May-2019 (when &lt;Period&gt; is M 
    			 and frequency is Monthly)

			

- 28-Apr-2019 to 28-Apr-2020 (when &lt;Period&gt; is Y 
    			 and frequency is Annually)

			

- 28-Apr-2019 to 5-May-2019 (when &lt;Period&gt; is W 
    			 and frequency is Weekly)

		
		
If this parameter is not specified for quarters, the date will 
		 default to the last day of the quarter.

		

&nbsp;

		

<span class="hcp4">Note</span>: 
		 If the period is W (week), the start of the week will be Monday.

</td>
	</tr>
</tbody></table>

&nbsp;

The parameters are to be added as below:

&lt;Field&gt;=&lt;FunctionCode&gt;&lt;Number&gt;.&lt;Period&gt;.&lt;Code&gt;

&nbsp;

Examples:

<table class="Table1" style="border-collapse: separate;" cellspacing="0px" width="81.47%" border="1">
	<colgroup><col style="width: 59.183%;">
	<col style="width: 21.103%;">
	<col style="width: 10.323%;">
	<col style="width: 9.391%;">
	</colgroup><tbody><tr class="t1st">
		<td>Requirement</td>
		<td>Specify as</td>
		<td>Financial Year End Date</td>
		<td>Date Due</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

Set the due date 
		 for Annual Return filing to be seven months from the Financial 
		 Year End date

</td>
		<td class="t2Col" style="vertical-align: top;">

DateDue=@EN.AcctYeaEnd+7.M

</td>
		<td class="t1Col" style="vertical-align: top;">

30-Jun-2020

</td>
		<td class="t2Col" style="vertical-align: top;">

30-Jan-2020

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="vertical-align: top;">

Set the due date 
		 for Annual Return filing to be seven months from the Financial 
		 Year End date (end of the month)

</td>
		<td class="t2Col" style="vertical-align: top;">

DateDue=@EN.AcctYeaEnd+7.M.E

</td>
		<td class="t1Col" style="vertical-align: top;">

30-Jun-2020

</td>
		<td class="t2Col" style="vertical-align: top;">

31-Jan-2021

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

Set the due date 
		 for Annual Return filing to be 350 days from the Financial Year 
		 End date

</td>
		<td class="t2Col" style="vertical-align: top;">

DateDue=@EN.AcctYeaEnd+350

		

or

		

DateDue=@EN.AcctYeaEnd+350.D

</td>
		<td class="t1Col" style="vertical-align: top;">

30-Jun-2020

</td>
		<td class="t2Col" style="vertical-align: top;">

15-Jun-2021

</td>
	</tr>
</tbody></table>

&nbsp;

<table class="Table1" style="border-collapse: separate;" cellspacing="0px" width="81.47%" border="1">
	<colgroup><col style="width: 51.992%;">
	<col style="width: 25.576%;">
	<col style="width: 12.162%;">
	<col style="width: 10.27%;">
	</colgroup><tbody><tr class="t1st">
		<td>Requirement</td>
		<td>Specify as</td>
		<td>Current Date</td>
		<td>Date Due</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

Set the due date 
		 for client meeting to be at the end of the quarter of the current 
		 date

</td>
		<td class="t2Col" style="vertical-align: top;">

DateDue=#NOW.Q.E

</td>
		<td class="t1Col" style="vertical-align: top;">

8-Jun-2021

</td>
		<td class="t2Col" style="vertical-align: top;">

30-Jun-2021

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="vertical-align: top;">

Set the due date 
		 for client meeting to be three months from the current date

</td>
		<td class="t2Col" style="vertical-align: top;">

DateDue=#NOW+3.M

</td>
		<td class="t1Col" style="vertical-align: top;">

8-Jun-2021

</td>
		<td class="t2Col" style="vertical-align: top;">

8-Sep-2021

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

Set the due date 
		 for client meeting to be three months from the current date (beginning 
		 of the month)

</td>
		<td class="t2Col" style="vertical-align: top;">

DateDue=#NOW+3.M.S

</td>
		<td class="t1Col" style="vertical-align: top;">

8-Jun-2021

</td>
		<td class="t2Col" style="vertical-align: top;">

1-Sep-2021

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="vertical-align: top;">

Set the due date 
		 for client meeting to be end of the current week

</td>
		<td class="t2Col" style="vertical-align: top;">

DateDue=#NOW0.W.E

</td>
		<td class="t1Col" style="vertical-align: top;">

8-Jun-2021

</td>
		<td class="t2Col" style="vertical-align: top;">

13-Jun-2021

</td>
	</tr>
</tbody></table>

&nbsp;

<table class="Table1" style="border-collapse: separate;" cellspacing="0px" width="81.47%" border="1">
	<colgroup><col style="width: 52.311%;">
	<col style="width: 25.177%;">
	<col style="width: 12.562%;">
	<col style="width: 9.95%;">
	</colgroup><tbody><tr class="t1st">
		<td>Requirement</td>
		<td>Specify as</td>
		<td>Current Date</td>
		<td>Date Due</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

Set the Period 
		 From for Directors Meeting as 3 months ago

</td>
		<td class="t2Col" style="vertical-align: top;">

MtDateFrom=#NOW-3.M

</td>
		<td class="t1Col" style="vertical-align: top;">

8-Jun-2021

</td>
		<td class="t2Col" style="vertical-align: top;">

8-Mar-2021

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="vertical-align: top;">

Set the Period 
		 To for Directors Meeting as one month ago

</td>
		<td class="t2Col" style="vertical-align: top;">

MtDateTo=#NOW-1.M

</td>
		<td class="t1Col" style="vertical-align: top;">

8-Jun-2021

</td>
		<td class="t2Col" style="vertical-align: top;">

8-May-2021

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

Set the due date 
		 for Directors Meeting as the end of the current quarter

</td>
		<td class="t2Col" style="vertical-align: top;">

DateDue=#NOW.Q.E

</td>
		<td class="t1Col" style="vertical-align: top;">

8-Jun-2021

</td>
		<td class="t2Col" style="vertical-align: top;">

30-Jun-2021

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="vertical-align: top;">

Set the due date 
		 for Directors Meeting at the start of quarter four

</td>
		<td class="t2Col" style="vertical-align: top;">

DateDue=#NOW.Q4.S

</td>
		<td class="t1Col" style="vertical-align: top;">

8-Jun-2021

</td>
		<td class="t2Col" style="vertical-align: top;">

1-Oct-2021

</td>
	</tr>
</tbody></table>

&nbsp;

Example Tag Configuration

<table class="Table1" style="border-collapse: separate;" cellspacing="0px" width="81.405%" border="1">
	<colgroup><col style="width: 44.897%;">
	<col style="width: 55.103%;">
	</colgroup><tbody><tr class="t1st">
		<td>Tag</td>
		<td>Explanation</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

[FL.TP.Required:AR]

</td>
		<td class="t2Col" style="vertical-align: top;">

Tag to specify 
		 that Annual Return filing type is required.

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="vertical-align: top;">

[FL.TP.AR:

		

FilingType=AR

		

FilingName=Annual Return

		

FilingFreq=Y]

</td>
		<td class="t2Col" style="vertical-align: top;">

Tag to specify 
		 details for Annual Return filing type with an annual frequency.

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

[FL.RC.AR:

		

FlDescription=Annual Return

		

PeriodFrom=@EN.IncorpDate

		

PeriodTo=@EN.IncorpDate.Q4.E

		

DateDue=@EN.AcctYearEnd+7.M

		

FlStatus=NW

		

+RollDate=PeriodFrom,PeriodTo,DateDue

		

+CopyField=PreparedBy,FlDescription,FiledBy

		

+RollActions=*]

</td>
		<td class="t2Col" style="vertical-align: top;">

Tag to specify 
		 details for the instance of Annual Return filing with:

		
			

- Period From date being the entity’s Incorporation Date

			

- Period To date being end of quarter four of the Incorporation 
    			 Date

			

- Date Due being seven months after the Financial Year 
    			 End date

		</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="vertical-align: top;">

[FL.AC.AR.1:

		

DateSet=#NOW

		

ActionCode=A1

		

ActionDescr=Prepare Annual Return

		

AdminCode=@EN.AdminCode

		

DateDue=@EN.AcctYearEnd+4.M.E]

</td>
		<td class="t2Col" style="vertical-align: top;">

Tag to specify 
		 details for the action of Annual Return filing with the due date 
		 being the end of a period of four months from the Financial Year 
		 End date.

</td>
	</tr>
</tbody></table>

&nbsp;

For the first instance of the Annual Return Filing where:

	

- Incorporation Date = 3-May-2019

	

- Financial Year End = 30-Jun-2019

You will have the following:

	

- Period From = 3-May-2019 (same as the Incorporation Date)

	

- Period To = 31-Dec-2019 (last day of Quarter 4 for the year 
    	 2019)

	

- Date Due for the filing = 30-Jan-2020 (seven months after the 
    	 Financial Year End)

	

- Date Due for the Prepare Annual Return action = 31-Oct-2019 
    	 (four months after the Financial Year End on the last day)

&nbsp;

See also:

	

- [Review Rules](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Review_Rules.htm)


&nbsp;

[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; Meetings, Filings, Reviews - Tags

&nbsp;

(c) Viewpoint Software for 
 Business Ltd

Version: 8.0.2022.09.20




