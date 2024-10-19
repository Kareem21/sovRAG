



# Checklist Item - Tags
For certain field types where the Browse button is available in the 
 Values/Default column, there is also the Tag Values section so that tags 
 can be entered.

<table class="Table1" cellspacing="0px" width="100%">
	<colgroup><col style="width: 15.689%;">
	<col style="width: 29.318%;">
	<col style="width: 17.652%;">
	<col style="width: 38.186%;">
	</colgroup><tbody><tr class="t1st" style="height: 31px;">
		<td class="hcp1">

Purpose

</td>
		<td class="hcp1">

Tag

</td>
		<td class="hcp1">

Field Type

</td>
		<td class="hcp1">

Explanation

</td>
	</tr>
	<tr class="t2Row" style="height: 134px;">
		<td rowspan="2" class="t1Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Retrieves 
		 score of the checklist item

</td>
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

[SCORE_GET=UF.&lt;Key&gt;]

</td>
		<td class="t1Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Applies to the following field types:

		
			

- Number

			

- Amount

		</td>
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This retrieves the score of the user 
		 field for the checklist item where &lt;Key&gt; refers to the key 
		 of the user field e.g. [SCORE_GET=UF.KY100] will get the score 
		 for the user field with the key KY100.

</td>
	</tr>
	<tr class="t1Row" style="height: 134px;">
		<td class="t2Col" style="vertical-align: top;">

[SCORE_GET=&lt;Score&gt;]

</td>
		<td class="t1Col" style="vertical-align: top;">

Applies to the 
		 following field types:

		
			

- Number

			

- Amount

		</td>
		<td class="t2Col" style="vertical-align: top;">

This will set 
		 the score of the checklist item to specified score where &lt;Score&gt; 
		 is the score e.g. [SCORE_GET=1] will set the score to 1.

</td>
	</tr>
	<tr class="t2Row" style="height: 107px;">
		<td rowspan="2" class="t1Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Specify 
		 if the value of the checklist item is editable or not

</td>
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

[ROW.RO]

</td>
		<td class="t1Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Can be used for field types that 
		 can contain information.

</td>
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This sets the checklist item as non-editable 
		 so users cannot change its value. In this case, the checklist 
		 item may be configured to retrieve the value from somewhere and 
		 display it for user to see only.

		

&nbsp;

		

<span class="hcp4">Note</span>: 
		 This tag will also work on workflows published to Viewpoint Engage.

</td>
	</tr>
	<tr class="t1Row" style="height: 92px;">
		<td class="t2Col" style="vertical-align: top;">

[ROW.RW]

</td>
		<td class="t1Col" style="vertical-align: top;">

Can be used for 
		 field types that can contain information.

</td>
		<td class="t2Col" style="vertical-align: top;">

This sets the 
		 checklist item as editable so that it can still be changed if 
		 necessary. This overrides the read-only mode for fields that do 
		 not contain the [ROW.RO] tag. 

		

&nbsp;

		

<span class="hcp4">Note</span>: 
		 This tag will also work on workflows published to Viewpoint Engage.

</td>
	</tr>
	<tr class="t2Row" style="height: 46px;">
		<td class="t1Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Specify if the value of the checklist 
		 item will be refreshed or not

</td>
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

[ROW.RV]

</td>
		<td class="t1Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Can be used for field types that 
		 can contain information.

</td>
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This sets the checklist item as read-only 
		 and refreshes the checklist item if it is in an in progress workflow 
		 step. This overwrites the default value when the source of information 
		 is updated elsewhere or when the users navigate to other places.

		

&nbsp;

		

<span class="hcp4">Note</span>: 
		 This tag will also work on workflows published to Viewpoint Engage.

</td>
	</tr>
	<tr class="t1Row" style="height: 46px;">
		<td class="t1Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Specify if the value of the checklist 
		 will be editable or non-editable according to the default value 
		 retrieved

</td>
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

[ROW.OV]

</td>
		<td class="t1Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Can be used for field types that 
		 can contain information.

</td>
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This sets the checklist item as editable 
		 or non-editable according to the default value retrieved. This 
		 tag must be used with items that is configured with default value. 
		 

		

If the default value retrieved has a value, this tag will be 
		 replaced with the [ROW.RO] tag and the item will become non-editable.

		

If the default value retrieved does not has a value, this tag 
		 will be replaced with the [ROW.RW] tag and the item will become 
		 editable.

		

&nbsp;

		

<span class="hcp4">Note</span>: 
		 This tag will also work on workflows published to Viewpoint Engage.

</td>
	</tr>
	<tr class="t2Row" style="height: 46px;">
		<td rowspan="3" class="t1Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Specify 
		 if the checklist item is seen or not

</td>
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

[ROW.Close]

</td>
		<td class="t1Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Can be used for any field type.

</td>
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This will collapse the checklist 
		 item's sub-items by default. To see the sub-items, click on the 
		 plus sign.

</td>
	</tr>
	<tr class="t1Row" style="height: 46px;">
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

[ROW.Close=E]

</td>
		<td class="t1Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Can be used for any field type.

</td>
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This will hide all sub-items by default 
		 unless the sub-items contain values.

</td>
	</tr>
	<tr class="t2Row" style="height: 76px;">
		<td class="t2Col" style="vertical-align: top;">

[ROW.HideBlanks]

</td>
		<td class="t1Col" style="vertical-align: top;">

Can be used for 
		 field types that can contain information.

</td>
		<td class="t2Col" style="vertical-align: top;">

This will hide 
		 the checklist item and all its sub-items if there is no value. 
		 You can use this if the checklist item and its sub-items are set 
		 to retrieve information from the database so for Master File where 
		 the information is not available, the checklist items are hidden.

</td>
	</tr>
	<tr class="t1Row" style="height: 244px;">
		<td rowspan="4" class="t1Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Repeat 
		 grouped checklist items

</td>
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

[COPY:&lt;QueryName&gt;]

		

&nbsp;

		

where &lt;QueryName&gt; refers to the SQL query name.

</td>
		<td class="t1Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Can be used for field types that 
		 can contain information.

</td>
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This tag is used to repeat a single 
		 checklist item or a group of checklist items in the workflow step, 
		 based on the number of records retrieved by an SQL query. 

		

Usage of this tag requires:

		
			

- the SQL query to be specified in the checklist/workflow 
    			 step record

			

- a single instance of the checklist item/group in the 
    			 workflow step

			

- the tag to be added to the Tag Values of the checklist 
    			 item if only a single checklist item requires repeating, or 
    			 in the Tag Vaues of the parent item if a group requires repeating

		
		
<span class="hcp4">Note</span>: 
		 This tag will also work on workflows published to Viewpoint Engage.

</td>
	</tr>
	<tr class="t2Row" style="height: 229px;">
		<td class="t2Col" style="vertical-align: top;">

[COPY.STEP:&lt;StepKey&gt;]

		

&nbsp;

		

where &lt;StepKey&gt; is the Key of the earlier workflow step.

</td>
		<td class="t1Col" style="vertical-align: top;">

Can be used for 
		 field types that can contain information.

</td>
		<td class="t2Col" style="vertical-align: top;">

This tag is used 
		 to repeat a single checklist item or a group of checklist item 
		 in the workflow step, based on the number of time an earlier workflow 
		 step is copied.

		

Usage of this tag requires:

		
			

- the earlier workflow step to have 'Allow Copy Step' 
    			 option ticked

			

- a single instance of the checklist item/group in the 
    			 workflow step

			

- the tag to be added to the Tag Values of the checklist 
    			 item if only a single checklist item requires repeating, or 
    			 in the Tag Vaues of the parent item if a group requires repeating

		</td>
	</tr>
	<tr class="t1Row" style="height: 274px;">
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

[COPY.GROUP:&lt;StepKey&gt;.&lt;ItemKey&gt;]

		

where

		
			

- &lt;StepKey&gt; is the Key of the &nbsp;step containing 
    			 the items to be retrieved.

			

- &lt;ItemKey&gt; is the Key of the duplicated item or 
    			 duplicated group's parent item.

		</td>
		<td class="t1Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Can be used for field types that 
		 can contain information.

		

&nbsp;

</td>
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This tag is used to repeat a single 
		 checklist item or a group of checklist item in the workflow step, 
		 based on the number of times that item/group is duplicated in 
		 an earlier workflow step.

		

Usage of this tag requires:

		
			

- the items/group in the earlier workflow step have the 
    			 Duplicate option enabled

			

- a single instance of the checklist item/group in the 
    			 workflow step

			

- the tag to be added to the Tag Values of the checklist 
    			 item if only a single checklist item requires repeating, or 
    			 in the Tag Vaues of the parent item if a group requires repeating

		
		
<span class="hcp4">Note</span>: 
		 If there is more than one group, the tag must be added to each 
		 group's parent item.

</td>
	</tr>
	<tr class="t2Row" style="height: 1596px;">
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

[COPY.&lt;Type&gt;]

		

[COPY.&lt;Type&gt;:&lt;Sub-Type&gt;]

</td>
		<td class="t1Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Can be used for field types that 
		 can contain information.

</td>
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This is to be used when:

		
			

- Information is retrieved from the database according 
    			 to the specified type or sub-type.

			

- Information is retrieved as value of checklist item 
    			 (and sub-items).

		
		
The tag allows for just one instance of the checklist item (and 
		 sub-items) that will be repeated according to the number of records 
		 returned by the type/sub-type which refers to:

		
			

- Relations - This retrieves records from the CR_Officer 
    			 view in the database and DateAppoint field is used as the 
    			 date filter.
    
    			
        				
        
    - &lt;Type&gt; can be:
        
        				
            					
            
        - RT = Trust Officers
            
            
            					
        - RE = Entity Relations
            
            
            					
        - RO = Statutory Officers
            
            
            					
        - RM = Master File Relations
            
            
            				
        
        				
    - &lt;Sub-Type&gt; depends on the &lt;Type&gt; e.g. 
        				 if &lt;Type&gt; is RO, &lt;Sub-Type&gt; can be D* to retrieve 
        				 all types of Directors or D*,S*,A* to retrieve all D,S 
        				 and A officer types.  
        &#13;&#10;				  
        &#13;&#10;				Example: [COPY.RO:D*]
        
        
        			

			

- Beneficiaries - This retrieves records from the CR_Beneficiaries 
    			 view in the database and DateAppoint field is used as the 
    			 date filter.
    
    			
        				
        
    - &lt;Type&gt; can only be BE = Beneficiaries
        
        
        				
    - &lt;Sub-Type&gt; can be any value from the Beneficiary 
        				 Type [BEFT] lookup table.  
        &#13;&#10;				  
        &#13;&#10;				Example: [COPY.BE:I]
        
        
        			

			

- Bank Signatories - This retrieves records from the CR_BankSign 
    			 view in the database and DateResolution field is used for 
    			 the date filter.
    
    			
        				
        
    - &lt;Type&gt; can only be SI = Bank Signatories
        
        
        				
    - &lt;Sub-Type&gt; can be any value from the Signing 
        				 Auth. Group [SIGR] lookup table.  
        &#13;&#10;				  
        &#13;&#10;				Example: [COPY.SI]
        
        
        			

			

- Shareholders/Partners - This retrieves records from 
    			 the CR_Shareholders view in the database and there is no date 
    			 field for comparison. There is only one &lt;Type&gt; - SH 
    			 - and no sub-type.  
    &#13;&#10;			  
    &#13;&#10;			Example: [COPY.SH]

			

- Interests - This retrieves records from the Share_Interests 
    			 table in the database and DateStart is used as the date filter.
    
    			
        				
        
    - &lt;Type&gt; can only be IN = Interests
        
        
        				
    - &lt;Sub-Type. can be any value from the Interests 
        				 Type [INTP] lookup table.  
        &#13;&#10;				  
        &#13;&#10;				Example: [COPY.IN:BEI,BCI,BEO,UBO]
        
        
        			

			

- Addresses - This retrieves records from the CR_RefAddresses 
    			 view in the database and Effective field is used as the date 
    			 filter.
    
    			
        				
        
    - &lt;Type&gt; can only be AD = Addresses
        
        
        				
    - &lt;Sub-Type. can be any value from the Address 
        				 Types [ADRT] lookup table.  
        &#13;&#10;				  
        &#13;&#10;				Example: [COPY.AD=RO,AR,MA]
        
        
        			

		
		
If required, you can also filter according to a date value specified 
		 in another checklist item. In this case, the format is [COPY.&lt;Type&gt;|&lt;Operator&gt;&lt;Key&gt;] 
		 or [COPY.&lt;Type&gt;:&lt;Sub-Type&gt;|&lt;Operator&gt;&lt;Key&gt;] 
		 where:

		
			

- &lt;Operator&gt; can be =, &lt;,&gt;,&lt;= or &gt;=.

			

- &lt;Key&gt; refers to the key of the checklist item 
    			 that holds the date value. If the key refers to a checklist 
    			 item without a date, then all active records for the specified 
    			 Type and Sub-Type will be shown if the operator is &gt; or 
    			 &gt;=. If the operator is &lt; or &lt;=, then no record will 
    			 be shown.

		
		
To filter based on the Date Resigned, the format is [COPY.&lt;Type&gt;:&lt;Sub-Type&gt;|DR&lt;Operator&gt;=&lt;Key&gt;] 
		 where:

		
			

- DR refers to the Date Resign.

			

- &lt;Operator&gt; can be =, &lt;,&gt;,&lt;= or &gt;=.

			

- &lt;Key&gt; refers to the key of the checklist item that 
    			 holds the date value.

		</td>
	</tr>
	<tr class="t1Row" style="height: 199px;">
		<td class="t1Col" style="vertical-align: top;">

Specify template 
		 for generation

</td>
		<td class="t2Col" style="vertical-align: top;">

[FC=&lt;Code&gt;]

</td>
		<td class="t1Col" style="vertical-align: top;">
			- Excel Statement
			- Go to Screen when the screen is Correspondence Creation 
    			 [$CORRES]
			- Standard Report
			- Word Report
		</td>
		<td class="t2Col" style="vertical-align: top;">

This is to specify 
		 the template code for generating a correspondence, Excel Statement, 
		 Standard Report or Word Report. You can also retrieve the code 
		 from another checklist item by using a Workflow Field Key (+&lt;Key&gt;+).

		

&nbsp;

		

<span class="hcp4">Note</span>: 
		 This tag will also work on workflows published to Viewpoint Engage.

</td>
	</tr>
	<tr class="t2Row" style="height: 231px;">
		<td class="t1Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Specify the Complete Fields caption 
		 for Excel Statement, Standard Report, and Word Report

</td>
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

[DisplayName=] 

</td>
		<td class="t1Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">
			- Excel Statement
			- Standard Report
			- Word Report
		
		&nbsp;

</td>
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This is to rename the caption in 
		 the Complete Field column. The default value for this captions 
		 is 'Word/PDF/XML Report Creation'. 

</td>
	</tr>
	<tr class="t1Row" style="height: 231px;">
		<td class="t1Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Specify the addressee

</td>
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

[Addressee=&lt;Key&gt;]

</td>
		<td class="t1Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Can be used only for Go to Screen 
		 field type when the screen is Correspondence Creation [$CORRES].

</td>
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This is to specify the addressee 
		 (if it is not the Master File of the workflow) when generating 
		 a Correspondence document and requires the following:

		
			

- Checklist item for generating the Correspondence document 
    			 with field type 'Go to Screen' and the screen set to &nbsp;Correspondence 
    			 Creation [$CORRES].

			

- Checklist item for the Master File of the addressee 
    			 with a key and the field type 'Master File' with &lt;Key&gt; 
    			 being the key of the item.

		
		
The tag is optional and is not required if the addressee is 
		 the Master File of the workflow.

</td>
	</tr>
	<tr class="t2Row" style="height: 76px;">
		<td class="t1Col" style="vertical-align: top;">

Embed the screen 
		 in the workflow

</td>
		<td class="t2Col" style="vertical-align: top;">

[Embed=Y]

</td>
		<td class="t1Col" style="vertical-align: top;">

Can be used only 
		 for Go to Screen field type when the screen is not Correspondence 
		 Creation [$CORRES].

</td>
		<td class="t2Col" style="vertical-align: top;">

This is used 
		 when the field type for the checklist item is 'Go to Screen' and 
		 you want the screen to be opened within the workflow instead of 
		 separately in the File Maintenance.

</td>
	</tr>
	<tr class="t1Row" style="height: 134px;">
		<td class="t1Col" rowspan="2" style="border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Perform a copy to Viewpoint Clipboard

</td>
		<td class="t2Col" style="vertical-align: top;">

[CLIP.Set=Y]

</td>
		<td class="t1Col" style="vertical-align: top;">

Applies to the 
		 following field types:

		
			

- Go to Screen

			

- Master File

		</td>
		<td class="t2Col" style="vertical-align: top;">

This copy values 
		 from the workflow step's checklist items and paste them automatically 
		 to the specified screen.

		

<span class="hcp4">Note</span>: 
		 The checklist items must have the relevant database fields defined 
		 in Clipboard Field.

</td>
	</tr>
	<tr class="t2Row" style="height: 134px;">
		<td class="t2Col" style="border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

[CLIP.Source=&lt;StepKey&gt;]

		

[CLIP.Source=&lt;StepKey&gt;.{REF}]

		

&nbsp;

</td>
		<td class="t1Col" style="border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Applies 
		 to the following field types:

		
			

- Go to Screen

			

- Master File

		</td>
		<td class="t2Col" style="border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This 
		 is similar to the above, except that the items to copy are from 
		 a specified earlier workflow step identified using &lt;StepKey&gt; 
		 which refers to the Key of the workflow step.

		

If the steps is repeatable, then add {REF} to copy and paste 
		 values of the same instance of the step.

</td>
	</tr>
	<tr class="t1Row" style="height: 134px;">
		<td class="t1Col" style="border-left-color: rgb(0, 0, 0); border-left-style: solid; border-left-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Delete previous instances of Viewpoint 
		 Clipboard

</td>
		<td class="t2Col" style="border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

[CLIP.Clear=Y]

</td>
		<td class="t1Col" style="border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Applies to the following field types:

		
			

- Go to Screen

			

- Master File

		</td>
		<td class="t2Col" style="border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 1px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

This will automatically delete all 
		 other instances of Viewpoint Clipboard so only values from the 
		 current workflow step is there.

</td>
	</tr>
	<tr class="t2Row" style="height: 61px;">
		<td rowspan="3" class="t1Col" style="vertical-align: top;">

Enable 
		 or disable linking changes performed

</td>
		<td class="t2Col" style="vertical-align: top;">

[LinkChanges=N]

</td>
		<td class="t1Col" style="vertical-align: top;">

Can be used only 
		 for Go to Screen and Macros field type.

</td>
		<td class="t2Col" style="vertical-align: top;">

By default, changes 
		 performed in the embedded screen will be linked automatically 
		 and appear as items under the embedded screen item in the workflow 
		 step. Adding this tag will stop the auto-linking so the changes 
		 will not be added.

</td>
	</tr>
	<tr class="t1Row" style="height: 61px;">
		<td class="t2Col" style="vertical-align: top;">

[LinkChanges=F]

</td>
		<td class="t1Col" style="vertical-align: top;">

Can be used only 
		 for Go to Screen and Macros field type.

</td>
		<td class="t2Col" style="vertical-align: top;">

This tag is to 
		 show the change link item only if linked forms are selected and 
		 queued. If no forms are selected and queued, the change link item 
		 will not be seen in the workflow step.

</td>
	</tr>
	<tr class="t2Row" style="height: 46px;">
		<td class="t2Col" style="vertical-align: top;">

[LinkChanges=L]

</td>
		<td class="t1Col" style="vertical-align: top;">

Can be used only 
		 for Go to Screen and Macros field type.

</td>
		<td class="t2Col" style="vertical-align: top;">

This is to show 
		 the change only but hide the '+' sign for the change link item 
		 if no linked forms are selected and queued.

</td>
	</tr>
	<tr class="t1Row" style="height: 76px;">
		<td class="t1Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Disable linking of document holders

</td>
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

[LinkHolders=N]

</td>
		<td class="t1Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

Can be used only for Go to Screen 
		 and Change Link field type.

</td>
		<td class="t2Col" style="border-bottom-style: solid; border-bottom-width: 1px; vertical-align: top;">

By default, documents that are generated 
		 and stored from the workflow will be linked to the workflow automatically 
		 and appear as Document Holder items in the workflow step. Adding 
		 this tag will stop the auto-linking of the holders to the workflow.

</td>
	</tr>
	<tr class="t2Row" style="height: 46px;">
		<td rowspan="2" class="t1Col" style="vertical-align: top; border-bottom-width: 1px; border-bottom-style: solid;">

Set change codes that will 
		 be linked

</td>
		<td class="t2Col" style="vertical-align: top; border-bottom-width: 1px; border-bottom-style: solid;">

[ChangeCode=&lt;ChangeCode&gt;]

</td>
		<td class="t1Col" style="vertical-align: top; border-bottom-width: 1px; border-bottom-style: solid;">

Can be used only for Change 
		 Link field type

</td>
		<td class="t2Col" style="vertical-align: top; border-bottom-width: 1px; border-bottom-style: solid;">

This tag is to specify the 
		 change code that you want to link to the workflow. Doing so will 
		 add it as a Link item in the workflow step.

</td>
	</tr>
	<tr class="t1Row" style="height: 187px;">
		<td class="t2Col" style="vertical-align: top; border-bottom-style: solid; border-bottom-width: 1px;">

[KeyCode=&lt;Key&gt;]

		

&nbsp;

</td>
		<td class="t1Col" style="vertical-align: top; border-bottom-style: solid; border-bottom-width: 1px;">

Can be used only for Change 
		 Link field type.

</td>
		<td class="t2Col" style="vertical-align: top; border-bottom-style: solid; border-bottom-width: 1px;">

This is to specify the Master 
		 File the change is for and requires the following:

		
			

- Checklist item for the change&nbsp;with field type 'Change 
    			 Link'.

			

- Checklist item for the Master File of the addressee 
    			 with a key and the field type 'Master File' with &lt;Key&gt; 
    			 being the key of the item.

		
		
Without this tag, the Master File for the change will be the 
		 Master File the workflow is for.

</td>
	</tr>
	<tr class="t2Row" style="height: 242px;">
		<td class="t1Col" style="vertical-align: top; border-bottom-width: 1px; border-bottom-style: solid;">

Specify another Master File

</td>
		<td class="t2Col" style="vertical-align: top; border-bottom-width: 1px; border-bottom-style: solid;">

[FileCode=&lt;Key&gt;]

		

&nbsp;

</td>
		<td class="t1Col" style="vertical-align: top; border-bottom-width: 1px; border-bottom-style: solid;">

Applies to the following field 
		 types:

		
			

- Excel Statement

			

- File Review

			

- Go to Screen

			

- Macros

			

- Standard Report

			

- Word Report

		</td>
		<td class="t2Col" style="vertical-align: top; border-bottom-width: 1px; border-bottom-style: solid;">

This can be added when you 
		 would like the item to apply to another Master File specified 
		 in another checklist item where &lt;Key&gt; is the key of the 
		 checklist item.

		

Without the tag, the item will apply to the default Master File 
		 which is the Master File of the workflow.

		

&nbsp;

		

<span class="hcp4">Note</span>: 
		 This tag will also work on workflows published to Viewpoint Engage.

</td>
	</tr>
	<tr class="t1Row" style="height: 380px;">
		<td class="t1Col" style="vertical-align: top; border-bottom-style: solid; border-bottom-width: 1px;">

Specify review scope

</td>
		<td class="t2Col" style="vertical-align: top; border-bottom-style: solid; border-bottom-width: 1px;">

[Selection=&lt;Value&gt;]

</td>
		<td class="t1Col" style="vertical-align: top; border-bottom-style: solid; border-bottom-width: 1px;">

Can be used only for File Review 
		 field type.

</td>
		<td class="t2Col" style="vertical-align: top; border-bottom-style: solid; border-bottom-width: 1px;">

This is to specify the scope 
		 of the review where &lt;Value&gt; can be:

		<div>

	- 0 - All review scope
	- 1 - Setup review
	- 4 - Compliance review
	- 8 - Statutory review of managed entities
	- 64 - Meetings review
	- 128 - Filings review
	- 256 - Reviews review
	- 512 - Data Validation review
	- 1024 - AEOI review
	- 2048 - AEOI review of managed entities

</div>
		

For multiple review scope, add the value e.g. Setup review and 
		 Compliance review will have a value of 5.

</td>
	</tr>
	<tr class="t2Row" style="height: 207px;">
		<td class="t1Col" style="vertical-align: top; border-bottom-style: solid; border-bottom-width: 1px;">

Specify the selection criteria 
		 for Word Report generation

</td>
		<td class="t2Col" style="vertical-align: top; border-bottom-style: solid; border-bottom-width: 1px;">

[HD-SEL=&lt;Criterion&gt;]

</td>
		<td class="t1Col" style="vertical-align: top; border-bottom-style: solid; border-bottom-width: 1px;">

Can be used only for Word Report 
		 field type.

</td>
		<td class="t2Col" style="vertical-align: top; border-bottom-style: solid; border-bottom-width: 1px;">

This is to define the selection 
		 criteria for the document generation. The &lt;Criterion&gt; can 
		 be any field returned by the header statement for the report with 
		 a specific value. 

		

For example: [HD-SEL=WflowNr=(+DF.WflowNr+)].

		

&nbsp;

		

For multiple selection criteria, the tag is:

		

&nbsp;[HD-SEL=&lt;Criterion&gt; AND &lt;Criterion&gt;]

		

&nbsp;

		

For example: 

		

[HD-SEL=WflowNr=(+DF.WflowNr+) AND EntityAdminCode=(+DF.USERWF.Ucode+)]

</td>
	</tr>
	<tr class="t1Row" style="height: 221px;">
		<td class="t1Col" style="vertical-align: top; border-bottom-width: 1px; border-bottom-style: solid;">

Specify the selection criteria 
		 for Standard Report generation

</td>
		<td class="t2Col" style="vertical-align: top; border-bottom-width: 1px; border-bottom-style: solid;">

[/Parameters=&lt;Criterion&gt;/]

</td>
		<td class="t1Col" style="vertical-align: top; border-bottom-width: 1px; border-bottom-style: solid;">

Can be used only for Standard 
		 Report field type.

</td>
		<td class="t2Col" style="vertical-align: top; border-bottom-width: 1px; border-bottom-style: solid;">

This is to define the selection 
		 criteria for the Standard Report generation and is optional. The 
		 &lt;Criterion&gt; can be any field available as selection criteria 
		 for the report and you can specify more than one.

		

&nbsp;

		

For example:

		

[/Parameters=

		

[PeriodFrom=2012-01-01]

		

[PeriodTo=2013-01-01]

		

[User=SM]

		

/]

		

&nbsp;

		

You can specify the selection criteria based on another checklist 
		 item by using a Workflow Field Key (+&lt;Key&gt;+).

		

&nbsp;

		

For example:

		

[/Parameters=

		

[PeriodFrom=(+StartDate+)]

		

[PeriodTo=(+EndDate+)]

		

[User=(+Administrator+)]

		

/]

		

&nbsp;

		

<span class="hcp4">Note</span>: 
		 When specifying the selection criteria based on a checklist item 
		 of ‘Date’ field type, users will have to use the (+WF.&lt;Key&gt;+) 
		 tag.

</td>
	</tr>
	<tr class="t2Row" style="height: 76px;">
		<td class="t1Col" style="vertical-align: top; border-bottom-style: solid; border-bottom-width: 1px;">

Refresh the following items

</td>
		<td class="t2Col" style="vertical-align: top; border-bottom-style: solid; border-bottom-width: 1px;">

[InputRefresh=1]

</td>
		<td class="t1Col" style="vertical-align: top; border-bottom-style: solid; border-bottom-width: 1px;">

Can be used only for Input Field

</td>
		<td class="t2Col" style="vertical-align: top; border-bottom-style: solid; border-bottom-width: 1px;">

This is used for grouped items 
		 where the parent item is set to Input Fields for displaying only 
		 relevant sub-items. Refer to [Checklist 
		 Item - Field Type: Input Field](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Checklist_Item_-_Field_Type__Input_Field.htm).

</td>
	</tr>
	<tr class="t1Row" style="height: 67px;">
		<td class="t1Col" style="vertical-align: top; border-bottom-width: 1px; border-bottom-style: solid;">

Specify the item containing 
		 the determining value

</td>
		<td class="t2Col" style="vertical-align: top; border-bottom-width: 1px; border-bottom-style: solid;">

[SourceInput=&lt;Key&gt;]

</td>
		<td class="t1Col" style="vertical-align: top; border-bottom-width: 1px; border-bottom-style: solid;">

Can be used only for Input 
		 Field

</td>
		<td class="t2Col" style="vertical-align: top; border-bottom-width: 1px; border-bottom-style: solid;">

This is used for grouped items 
		 where the parent item is set to Input Fields for displaying only 
		 relevant sub-items. Refer to [Checklist 
		 Item - Field Type: Input Field](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Checklist_Item_-_Field_Type__Input_Field.htm)

</td>
	</tr>
</tbody></table>

&nbsp;

<span class="hcp4">Note</span>: These 
 tags are different from the tags for checklist/workflow step. For the 
 field type 'Workflow Link' please refer to [Workflow 
 Link - Tags](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Checklist_Item_-_Field_Type__Workflow_Link.htm).

&nbsp;

<span style="font-weight: bold;">Example 
 - [COPY:&lt;QueryName&gt;]</span>

In this example, the workflow step requires information to be retrieved 
 using Workflow Field Wizard and SQL queries. Information to be retrieved 
 using SQL queries are grouped and the SQL queries are:

	

- Officers to retrieve officers:  
    &#13;&#10;	  
    &#13;&#10;	[/Officers=SELECT DateAppoint, OfficerText, AddrCode, AddrCode AS 'MF' 
    	 FROM Officers WHERE EntCode='(-MF-)' AND RelClass='O' AND Status='A' 
    	 AND (DateResign&gt;='(-KEY:DR-)' OR DateResign IS NULL) ORDER BY DateAppoint/].

	

- CDDInfo to retrieve both the KYC Status of the Entity and the 
    	 Officer:  
    &#13;&#10;	  
    &#13;&#10;	[/CDDInfo=SELECT KYC_Status FROM RefMaster WHERE RefCode=‘(-MF-)’/].

Both queries are placed in the Tag Values field of the workflow step.

&nbsp;

For the items, the items are configured as follows:

![](../image143.jpg)

&nbsp;

&nbsp;

Item 1 - Date Last Review

This is retrieved using the Workflow Field Wizard.

![](../image144.jpg)

&nbsp;

Item 2 - Entity CDD Status

This is retrieved using the query CDDInfo. Since the field type for 
 this checklist item is Lookup Value, you are required to specify which 
 lookup table to use.

![](../image224.jpg)

&nbsp;

Item 3 (Parent) - Officer

This is retrieved using the query Officers. Since you want fields 3, 
 4, 5 and 6 repeated for each officer, this item is the parent item and 
 the &nbsp;COPY tag is added here. This item is a text field type, so the 
 name is retrieved using CCODE and then formatted using the #AD-40-0 format 
 option.

![](../image225.jpg)

&nbsp;

Item 4 - Position

This is retrieved using the CCODE.

![](../image226.jpg)

&nbsp;

Item 5 - Date Appoint

This is retrieved using the CCODE.

![](../image227.jpg)

&nbsp;

Item 6 - Officer CDD Status

This is retrieved using the CDDInfo query and formatted using the #LT-KYCS 
 format option. This is a text field type which requires formatting into 
 convert code to meaningful information. Compare this with 2 – Entity CDD 
 Status, which is a lookup value field type, and uses the Field/Mask to 
 convert code to meaningful information.

![](../image228.jpg)

&nbsp;
###### Result
From the result, you can see that the Entity CDD Status and the each 
 officer’s CDD Status is different, even though the same query CDDInfo 
 is used for both.

![](../image150.jpg)

&nbsp;

&nbsp;
###### Example - [COPY.&lt;Type&gt;]
In this example, the workflow step requires information on the shareholders 
 which can be retrieved using [COPY.SH] tag. There is no need for any SQL 
 query and the items are configured as follows:

![](../image272.gif)

&nbsp;

Item 1 (Parent) - Shareholder

This is retrieved using the [COPY.SH] tag added to this item as this 
 is the parent item. This item is a text field type, so the name is retrieved 
 using CCODE and then formatted using the #AD-40-0 format option.

![](../image274.gif)

&nbsp;

Item 2 - Current holding

This information is from the field 'SharesHeld' and retrieved using 
 CCODE.

![](../image275.gif)

&nbsp;

Item 3 - Share class

This information is from the field 'ShareClass' and retrieved using 
 CCODE.

![](../image276.gif)

&nbsp;

Item 4 - Effective date

This information is from the field 'FirstOfTransferDate' and retrieved 
 using CCODE.

![](../image277.gif)

&nbsp;
###### Result
![](../image278.gif)

&nbsp;
###### Example - [COPY.Step:&lt;Key&gt;]
In this example, the workflow step requires information to be retrieved 
 from an earlier step with the option 'Allow Copy Step' ticked. This means 
 that there may be one or more instances of the step. Configuration for 
 the items in this workflow step is as follows:

![](../image221.gif)

&nbsp;

Item 1 (Parent) - Surname of proposed 
 signatory

The information is to be copied from an item in an earlier workflow 
 step. This is the parent item so the COPY tag is added here to refer to 
 the earlier workflow step with the key VPWS0032 and CCODE takes the information 
 from the item with the key 'SigSurname'.

![](../image222.gif)

&nbsp;

Item 2 - Given name

This information from an item with the key 'SigName' and retrieved using 
 CCODE.

![](../image223.gif)

&nbsp;

<span style="text-decoration-line: underline;">Item 3 - Date of birth</span>

This information from an item with the key 'SigDOB' and retrieved using 
 CCODE.

![](../image225.gif)

&nbsp;

&nbsp;
###### Result
![](../image226.gif)

&nbsp;

&nbsp;

See also:

	

- [Checklist/Workflow 
    	 Step - Creation](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Checklist_Workflow_Step_Creation.htm)

	

- [Edit 
    	 Checklist/Workflow Step Editor](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Edit_Checklist_Workflow_Step_Editor.htm)

	

- [Checklist 
    	 Item - Field Types](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Checklist_Item_-_Field_Types.htm)

	

- [Checklist 
    	 Item - Field Type: Formula](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Checklist_Item_-_Field_Type__Formula.htm)

	

- [Checklist 
    	 Item - Values/Default](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Checklist_Item_-_Values_Default.htm)

	

- [Checklist 
    	 Item - Score Assignment](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Checklist_Item_-_Score_Assignment.htm)

	

- [Workflow 
    	 Link - Tags](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Checklist_Item_-_Field_Type__Workflow_Link.htm)

	

- [Configuring 
    	 Checklist Item](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Configuring_Checklist_Item.htm)

&nbsp;

[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; Checklist Item - Tags

&nbsp;

(c) Viewpoint Software for 
 Business Ltd

Version: 8.0.2022.09.20


