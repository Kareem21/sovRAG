




# Design Statement
This is where you edit an existing Excel Statement or create a new one 
 and you can access it by ticking the Design Statement checkbox.

&nbsp;

Account File, CoA Template, Global, All

Click an option to list statements for a selected category. This is 
 only available for Accounting Excel Statements seen in File Maintenance 
 screen. Note that your authority level will result in the following:

<table class="Table1" style="border-collapse: separate;" cellspacing="0px" border="1">
	<colgroup><col style="width: 28.122%;">
	<col style="width: 71.878%;">
	</colgroup><tbody><tr class="t1st">
		<td class="hcp1">

Authority 
		 Level

</td>
		<td class="hcp1">

Explanation

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

8 - Power User

</td>
		<td class="t2Col" style="vertical-align: top;">

Can modify and 
		 copy all Excel Statement templates.

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="vertical-align: top;">

6 - Regular User

</td>
		<td class="t2Col" style="vertical-align: top;">

Can modify Excel 
		 Statement templates for Account File category, can copy templates 
		 to Account File category.

</td>
	</tr>
</tbody></table>

&nbsp;

Command buttons

Click on the relevant command button to perform the necessary.

	

- <span class="hcp4">Excel</span> - Click to open 
    	 the statement in Microsoft Excel so that you can edit it.

	

- <span class="hcp4">Check In - </span><span lang="EN-US" xml:lang="EN-US">The Check In button is only visible when users are 
    	 connected via the Cloud Solution. The button is disabled when there 
    	 are no templates being checked out locally in the client-side. When 
    	 you open a template file, the Check In button will be enabled. Once 
    	 completed, close the document and click <b style="">Check 
    	 In</b>. The template will be uploaded to the server-side and the local 
    	 copy in client-side will be deleted.</span>

	

- <span class="hcp4">Properties</span> - Click to 
    	 display the properties of the selected statement which you can amend 
    	 if necessary. Ensure that the report output is not affected by the 
    	 amendments.

	

- <span class="hcp4">Copy</span> - Click to create 
    	 a copy of the selected statement. Enter the properties for the copied 
    	 statement.

	

- <span class="hcp4">New</span> - Click to [create](javascript:TextPopup(this)) 
    	 a new statement. Enter the statement properties in the Statement Properties 
    	 window.
    
    	<div class="droptext" id="POPUP370148481" style="display: none;">
    		
        			    1. In the Statement Properties window, enter the statement 
        			 properties:
        			
            				        - Global, CoA Template or Account File - Select the 
            				 usage of the template. This is only for Accounting Excel 
            				 Statements.
            				        - 
            - 
                					            - Global templates are used by all Account Files.
                					            - CoA Templates are used by Account Files using 
                					 the selected Chart of Accounts template. If you select 
                					 this, specify which Chart of Accounts template in 
                					 CoA Template field.
                					            - Account Files template are specific to the selected 
                					 Account File. If you select this, specify which Chart 
                					 of Accounts template in Account File field.
                				
            				        - Statement Code - Enter a unique code for the template.
            				        - Category - Select the category.
            				        - Description - Enter a description for the template. 
            				 This will appear in the statement table.
            				        - File Name - Browse to the location of the Excel 
            				 (.xls) template.
            				        - Language - Select the language for the template. 
            				 This does not have any effect and is used only for informational 
            				 purposes.
            				        - Help Text - Enter a descriptive text relating to 
            				 how the statement is to be used, or information about 
            				 the selection criteria.
            				        - Customised - don't overwrite on import - Tick this 
            				 to prevent the template from being overwritten if you 
            				 import a template with the same code.
            				        - Generate using Open XML technology - Tick this to 
            				 use OpenXML technology to generate Excel statements. This 
            				 applies only to Excel templates in .xlsx format on Microsoft 
            				 Office 2007 and newer. If the template is in .xls, the 
            				 following will happen when you tick the option:
            				            - 
                					            - Conversion of the template to .xlsx format.
                					            - The Path and File Name will point to the .xlsx 
                					 template.
                					            - The tag [GENMETHOD=OPENXML/] will be added to 
                					 the Tag Values section of the template.
                				
            				        - Statement Type - Select the statement type. This 
            				 is only available for Accounting Excel Statements.
            				            - 
                					            - Account Selection - When you select this type, 
                					 you need to select the default account type. Tick 
                					 the Select on Default Only checkbox if you do not 
                					 want to allow users to change the default selection 
                					 when they generate the statement.
                					            - Define with 'Tag Values' - When you select this, 
                					 you can use tags to:
                					                - 
                    						                - Enable the statement for selection when 
                    						 generating a report in the Statement Import &amp; 
                    						 Processing screen. Click [here](javascript:TextPopup(this)) 
                    						 for an example of the tag configuration.
                    						<div class="droptext" id="POPUP411646880" style="display: none;">
                    							[SELECT=STIMP]
                    							[SRCH1.TYPE=AS]
                    							[SRCH1.CAPTION=Statement No]
                    							[SRCH1. MANDATORY=Y]
                    							[SRCH1.CODE=STATNO]
                    							&nbsp;
                    							[SRCH2.TYPE=AL.E,B]
                    							[SRCH2.CAPTION=Bank/Security A/C]
                    							[SRCH2.MANDATORY=N]
                    							[SRCH2.CODE=ACCTNO]
                    							&nbsp;
                    							<span class="hcp7">Note</span>: 
                    							 In the statement, the fields (-STATNO-) and 
                    							 (-ACCTNO-) are to be used for selection criteria 
                    							 in the WHERE clauses.
                          </div>
                    						                - Enable the statement for selection when 
                    						 generating a report in the Payments Release (use 
                    						 the tag [SELECT=PAYMENT]) and Banks &amp; Export 
                    						 Batches (use the tag [SELECT=PAYBATCH]) screens. 
                    						 Click [here](javascript:TextPopup(this)) 
                    						 for an example of the tag configuration.
                    						<div class="droptext" id="POPUP411644360" style="display: none;">
                    							[SELECT=PAYBATCH]
                    							[SRCH1.TYPE=PX]
                    							[SRCH1.CAPTION=Batch Number]
                    							[SRCH1. MANDATORY=Y]
                    							[SRCH1.CODE=BATCHNR]
                    							&nbsp;
                    							<span class="hcp7">Note</span>: 
                    							 In the statement, the field (-BATCHNR-) is 
                    							 to be used for selection criteria in the WHERE 
                    							 clauses.
                          </div>
                    					
                				
            				        - Selection on - This is only available for Accounting 
            				 Excel Statements and together with Selection Range determines 
            				 the selection criteria made available to users on generation. 
            				 The available options are:
            				            - 
                					            - Dates
                					            - Periods
                					            - Journal No.
                					            - Transaction No.
                					            - No selection
                				
            				        - Selection Criteria setting - This is not available 
            				 for Accounting Excel Statements. Together with Selection 
            				 Range, it determines the selection criteria made available 
            				 to users on generation. You can:
            				            - 
                					            - select from the available fields; or
                					            - define your own criteria by ticking the option 
                					 Tag Values and specifying the criteria using [SRCH tags](javascript:TextPopup(this)); 
                					 or
                					<div class="droptext" id="POPUP411637851" style="display: none;">
                						<h6 class="Heading8">[SRCHx.TYPE=...]</h6>
                						This points the field to the information you 
                						 are looking for. Valid values are:
                						
                    							                - MF or MF.TYPE - User will need to select 
                    							 a Master File. MF will display all Master 
                    							 Files, while MF.TYPE will display the Master 
                    							 File of the type specified. The type refers 
                    							 to the database table field: for instance, 
                    							 MF.CS will display Master Files enabled for 
                    							 Entity Statutory while MF.TU will show only 
                    							 Trust files.
                    							                - LV.TABLECODE - User needs to select 
                    							 a value from the lookup value table specified 
                    							 by TABLECODE. For instance, LV.MTTR to retrieve 
                    							 a value from the Matter Type Codes [MTTR] 
                    							 &nbsp;lookup table.
                    							                - UT.TABLECODE - User needs to select 
                    							 a value from the user table specified by TABLECODE. 
                    							 For instance, UT.ORGUNITS to retrieve a value 
                    							 from the Organizational Units [ORGUNITS] user 
                    							 table.
                    							                - AL.SLTYPE,SLTYPE - User needs to select 
                    							 a sub-ledger account from the ones listed. 
                    							 For instance, AL.E,B will display all Securities 
                    							 (E) and Bank (B) sub-ledgers for selection. 
                    							 This type can be used for Accounting only.
                    							                - PF - User need to specify the portfolio 
                    							 code. This type can be used for Accounting 
                    							 only.
                    							                - AS - This is used for Statement Import 
                    							 &amp; Processing only, and retrieves the available 
                    							 statements for selection. This type can be 
                    							 used for Accounting only .
                    							                - PX - This is used for Payment Export 
                    							 Batches only, and retrieves the available 
                    							 statements for selection. This type can be 
                    							 used for Accounting only .
                    							                - PY - This is used for Payments (released), 
                    							 and retrieves the available statements for 
                    							 selection. This type can be used for Accounting 
                    							 only .
                    						
                						&nbsp;
                						<h6 class="Heading8">[SRCHx.CAPTION=...]</h6>
                						Enter a caption for the field.
                						&nbsp;
                						<h6 class="Heading8">[SRCHx.MANDATORY=...]</h6>
                						Enter Y to make the field mandatory for complete, 
                						 N otherwise. If nothing is entered, the default 
                						 value is Y.
                						&nbsp;
                						<h6 class="Heading8">[SRCHx.CODE=...]</h6>
                						This field is used to pass the selection from 
                						 SRCHx.TYPE into the Excel statement as a variable. 
                						 For instance, MTRC is passed to the Excel statement 
                						 as (-MTRC-). If no value is assigned, the value 
                						 will be TVXX, where XX is the TYPE code. For example: 
                						 TVMF is passed through if your [SRCHx.TYPE=MF].
                						&nbsp;
                						<span class="hcp7">Note</span>: 
                						 You can have up to five search criteria. Replace 
                						 the x with 1, 2, 3, 4 or 5.
                     </div>
                					            - you can use both system-defined and user-defined 
                					 selection criteria by adding the Tag Values when configuring 
                					 the Excel Statement. The default setting of the selection 
                					 criteria is set to a maximum of 5.
                				
            				        - ![](../image486.gif)
            				        - [Selection 
            				 Range](javascript:TextPopup(this)) - Determines the selection criteria 
            				 on generation.
            				<div class="droptext" id="POPUP411660245" style="display: none;">
            					For Accounting Excel Statements:
            					
                						            - From / To - Requires completion of a Begin 
                						 and End Date/Period for the generation of the 
                						 statement. The data retrieved will be based on 
                						 these two dates.
                						            - From / C. Period / To - Requires the completion 
                						 of a Begin, Start and End Date/Period for the 
                						 generation of the statement. The statement is 
                						 designed to retrieve data based on the three dates/periods.
                						            - Number - Requires a Journal No. or Date.
                					
                </div>
            			
        			    1. Click Update.
        			    1. Click Excel.
        		
    		<span class="hcp7">Note</span>: 
    		 OpenXML technology does not support cell dependency as recalculation 
    		 is not possible while generating Excel Statements. Pivot table 
    		 is also not supported.
       </div>

	

- <span class="hcp4">Delete</span> - Click to delete 
    	 the selected statement.

	

- <span class="hcp4">Export</span> - Click to [export](javascript:TextPopup(this)) 
    	 the selected statement. Two files will be exported to the location 
    	 selected: <span class="hcp8">filename</span>.xls and 
    	 <span class="hcp8">filename</span>.dxf.
    
    	<div class="droptext" id="POPUP371445066" style="display: none;">
    		<div>
    To export selected template:
        
        	    1. Once you click Export, browse to the folder where the exported 
        	 files are to be stored.
        	    1. Click Export.
    
    &nbsp;
    To export more than one template:
        
        	    1. Once you click Export, browse to the folder where the exported 
        	 files are to be stored.
        	    1. Click Select Category/Jurisdiction.
        	    1. Tick the category or jurisdiction.
        	    1. Click Select Document to see all templates in the selected category 
        	 or jurisdiction.
        	    1. Tick the templates you want to export.
        	    1. Click Export.
    
    </div>
     </div>

	

- <span class="hcp4">Import</span> - Click to [import](javascript:TextPopup(this)) 
    	 statements. Two files are required for import: <span class="hcp8">filename</span>.xls 
    	 and <span class="hcp8">filename</span>.dxf.
    
    	<div class="droptext" id="POPUP371420600" style="display: none;">
    		<div>
        
        	    1. In the Import screen, browse to the folder containing the template 
        	 files.
        	    1. Click Import - Load List.
        	    1. Tick the templates you want to import.
        	    1. Click Import.
    
    </div>
    		&nbsp;
     </div>

	

- <span class="hcp4">Wizard</span> - Click to access 
    	 the [Statement 
    	 Field Wizard](javascript:TextPopup(this)). The codes will help you code the 
    	 statements. This is available only for Accounting Excel Statements.
    
    	<div class="droptext" id="POPUP372209392" style="display: none;">
    		The Statement Field Wizard is used to help you retrieve the 
    		 correct codes so that you can display the correct information 
    		 on your Excel Statements.
    		<h6 class="Heading8">Keep this Wizard on top of all screens</h6>
    		Tick to keep the wizard displayed on top of all your screens 
    		 for easy reference.
    		&nbsp;
    		<h6 class="Heading8">Code</h6>
    		This displays the code for the selected field.
    		&nbsp;
    		<h6 class="Heading8">Copy</h6>
    		Click to copy the code for the field that you have selected.
    		&nbsp;
    		<h6 class="Heading8">Close</h6>
    		Click to exit the wizard.
     </div>

	

- <span class="hcp4">Attributes</span> - Click this 
    	 to set up attributes for the selected template. When exporting this 
    	 template, you will also get the .dtr file which contains the attributes 
    	 information. This is only available in Viewpoint - Home screen. Refer 
    	 to [Attributes](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Attributes.htm) for more information.

&nbsp;

See also:

	

- [Excel Statements](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Excel_Statements.htm)

	

- [Excel Statements 
    	 - Fundamentals](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Excel_Statements_Fundamentals.htm)


 
&nbsp;

[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; Excel Statements - Design Statement
 
&nbsp;
 
(c) Viewpoint Software for 
 Business Ltd
 
Version: 8.0.2022.09.20




