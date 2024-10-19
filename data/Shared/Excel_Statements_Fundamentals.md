



# Excel Statements - Fundamentals
An Excel statement consists of:

	

- Codes,

	

- SQL query statements, and

	

- Excel features such as formulas, formatting and graphs.

All codes used for Excel statements are placed in square brackets [ 
 ]. The following codes are essential when preparing an Excel statement:

	

- [$GEN] - This must be placed in cell A1 to indicate to the program 
    	 that the spreadsheet includes codes for statement generation. See 
    	 also [$GEN\SET:{$IMPORT:&lt;SHEET&gt;}] below.

	

- [$GEN\SET:{$IMPORT:&lt;SHEET&gt;}] - This code is placed in 
    	 cell A1 instead of [$GEN] on import sheets that are used to retrieved 
    	 information from Viewpoint so that they can be re-imported at a later 
    	 time, or imported to another environments. After generation. the code 
    	 in cell A1 changes to {$IMPORT:&lt;SHEET&gt;} and the Excel statement 
    	 can then be used as an import sheet. For example: [$GEN\SET:{$IMPORT:JOURNAL}].

	

- [$END] - This must be placed in the last row of column A and 
    	 the last column of Row 1 to define the area where the codes are placed.

The first five columns are normally reserved for action codes, i.e. 
 codes that retrieve data that is subsequently used in the spreadsheet. 
 The following codes are used to hide columns and rows in the final, generated 
 statement:

	

- [$CHIDE-9] - Use this to hide the first nine columns. In the 
    	 example above, [$CHIDE-2] will hide the first two columns. Hence in 
    	 the generated statement, the report starts from column C.

	

- [$COLHIDE] - Use this to hide the column where this code is 
    	 placed. This can be used, for instance, when your query returns a 
    	 field that you do not want displayed in the generated statement.

	

- [$ROWHG-99] - Use this to set the row height to 99 points.

	

- [$ROWHIDE] - Use this to hide the row.

	

- [$RHV] - Use this to hide the row if all values in the row are 
    	 zeroes.

	

- [$RHR] - Use this to hide the row if it does not contain any 
    	 numerical value.

	

- [$PAGEBREAK] - Use this to insert a horizontal page break above 
    	 the cell containing the code.

&nbsp;
### SQL query statements
You may use SQL queries to retrieve information from a table or view 
 in the database. The queries can be defined anywhere in the statement, 
 but the statement used to execute the query must be on the same row or 
 below the query definition. Thus, if your query is placed in cell A5, 
 the execution query must be placed in row 5 or below.

You may refer to the Key Assist feature in the [Custom 
 Reports - Design Folder](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Custom_Reports.htm) for help in creating a SQL query.

&nbsp;
###### SELECT statement
[=SQL:QNAME=SELECT ... WHERE ...'(-VARNAME-)' ... '(-C:VARNAME-)' AND 
 (-%SPECIAL-)]

where: QNAME = Query name

&nbsp;
###### Query execution

	

- [@QNAME\Format]

	

- [@QNAME.FieldName\Format]

&nbsp;
###### Variables

	

- [%VARNAME=Value] &nbsp;- Use this to set the variable.

	

- [%C:VARNAME=VALUE] - Use this to set the variable specific for 
    	 the column.

	

- [%CLEAR] - Use this to clear all variables set within the report.

&nbsp;
###### Special codes
Special codes can be used in Billing Excel statements for invoices, 
 receipts, and time and disbursements, and can be replaced with one of 
 the following:

<table class="Table1" style="border-collapse: separate;" cellspacing="0px" width="88.852%" border="2" bordercolorlight="#000000" bordercolordark="#000000">
	<colgroup><col style="width: 25.965%;">
	<col style="width: 74.035%;">
	</colgroup><tbody><tr class="t1st">
		<td>

Code

</td>
		<td>

Where

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

DJ:PBE

</td>
		<td rowspan="6" class="t2Col">

DJ 
		 = Date Journal (Draft) Invoice Header and Receipts

		

DI = Date Invoice (Draft) Invoice 
		 Header and Receipts

		

DA = Date Time or Disbursement Entry

		

DP = Date Paid (Payment Batches)

		

PBE = Date&gt;=Open AND Date&lt;=Close

		

PME = Date&gt;=Start AND Date&lt;=Close

		

PBM = Date&gt;=Open AND Date&lt;Start

		

P&lt;B = Date&lt;Open

		

P&gt;E = Date&gt;Close

		

P&lt;=E = Date&lt;=Close

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">

DI:PBM

</td>
		
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

DI:PME

</td>
		
	</tr>
	<tr class="t1Row">
		<td class="t1Col">

DI:P&lt;B

</td>
		
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

DI:P&gt;E

</td>
		
	</tr>
	<tr class="t1Row">
		<td class="t1Col">

DI:P&lt;=E

</td>
		
	</tr>
</tbody></table>

&nbsp;
###### Example 1
The following sample code shows how a SELECT statement is written, and 
 how variables and special codes are set up. Note the section on optional 
 codes, which takes into consideration the non-mandatory selection criteria 
 for a report. These optional returns are catered for between {o} and {/o}.

[=SQL:CLIST=SELECT DISTINCT RefCode, '[%CCODE=' &amp;RefCode &amp; ']', 
 EntClient FROM InvoiceHeader INNER JOIN RmClients ON InvoiceHeader.RefCode 
 = RmClients.AddrCode WHERE RevEntity = '(-RC-)' AND {o}EntClient = '(-CL-)'{/o} 
 AND (-%DI:P&lt;=E-) AND (WriteOffBase + PaidBase &lt;&gt; InvoiceBase) 
 ORDER BY EntClient]

where:

	

- RefCode, EntClient = FieldNames.

	

- '[%CCODE=' &amp;RefCode &amp; ']' is used to assign the variable 
    	 CCODE to the RefCode that is returned. The variable CCODE can then 
    	 be used in subsequent SQL queries.

	

- '(-RC-)' is passed through from the selection criteria.

	

- {o}EntClient = '(-CL-)'{/o} takes care of the optional selection 
    	 of the client in the selection criteria.

&nbsp;
###### Example 2
The following sample code is placed in a cell below row 6. It refers 
 to the results in cell A6 and converts it to a variable called (-USER-) 
 which can then be used further down the spreadsheet in another query:

="[%USER=" &amp; A6 &amp; "]"

&nbsp;
###### Example 3
The following sample code will reformat a date in cell B3 to d-MMM-yy, 
 and used as a variable (-SDT-):

="[%SDT=" &amp; TEXT(B3,"d-MMM-yy") &amp; "]"

&nbsp;
### Formatting
You may use standard formatting codes to format FieldNames when executing 
 the query:

[@QNAME\x:FORMAT\y:FORMAT]

where:

	

- QNAME = Query name.

	

- x,y = Field number of the code to be formatted.

	

- FORMAT = Format code.

&nbsp;

For example:

Query:

[=SQL:MFLIST=SELECT EntCode, EntClient, AdminCode FROM Entity]

Query execution:

[@MFLIST\1:#AD-1-0\3:#AD-40-0\4:#US]

&nbsp;

If returned value is empty, use the BTXT tag to generate a display statement.

[@MFLIST\1:#AD-1-0\8:BTXT:Not Available]

If the value is empty, it will display the value as 'Not Available'.

&nbsp;
###### Other codes and functions used in Billing Excel statements
<table class="Table1" style="border-collapse: separate;" cellspacing="0px" width="88.652%" border="2" bordercolorlight="#000000" bordercolordark="#000000">
	<colgroup><col style="width: 38.966%;">
	<col style="width: 70.579%;">
	</colgroup><tbody><tr class="t1st">
		<td>

Code

</td>
		<td>

Explanation

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

[@QNAME\*NR=&lt;Text to show&gt;]

</td>
		<td class="t2Col">

Can be used when there is an optional selection 
		 and the SQL query is to retrieve the name of the selected criteria. 
		 If there is no selection, '&lt;Text to show&gt;' will appear.

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">

[@QNAME\1:@DH]

</td>
		<td class="t2Col">

Can be used when retrieving a list of Billing 
		 Files, for example, where the name of the Billing File is the 
		 first column. The code @DH will hide duplicate names for that 
		 first column.

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

[@QNAME-N]

</td>
		<td class="t2Col">

N is the number of rows to which the SQL query 
		 applies.

		

This is similar to a looping in programming code.

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">

(-PB-), (-PM-) and (-PE-)

</td>
		<td class="t2Col">

Date parameter that represents the From and 
		 To Dates respectively, of the user-entered date range when generating 
		 the Excel Statement.

		

(-PB-) referred as From Date/Period

		

(-PM-) referred as Current Date/Period

		

(-PE-) referred as To Date/Period 

		

Example:

		
			1. If only a Report Date is requested, the date is referred 
    			 to as (-PE-).
			1. If the Report Date parameter with Form and To Date, then 
    			 the From Date is referred as (-PE-)
		</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

CvDate(&lt;date parameter&gt;)

</td>
		<td class="t2Col">

Use this function in the SQL query to make 
		 sure the date is correctly formatted to an international standard.

		

Example:

		

[=SQL:QNAME=SELECT … FROM …WHERE DateField &gt;= CvDate((-PB-)) 
		 AND DateField &lt;= CvDate((-PE-))]

		

Note:<span style="font-weight: normal; font-style: normal;"> Only applicable for PB, PM, and PE.</span>

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">

[$CALCRM=... ]

</td>
		<td class="t2Col">

Used for retrieving backdated information. 
		 You will need to know some of the parameters to get the result 
		 you want.

		

Example:

		

[$CALCRM=BAXD|{where clause}|DOCINC=0|DATEREP=mmm/d/yyyy]

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

[$CALCRM=BAXD...]

</td>
		<td class="t2Col">

Retrieves based on due date.

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">

[$CALCRM=BAXI...]

</td>
		<td class="t2Col">

Retrieves based on invoice date.

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

[$CALCRM=BAXJ...]

</td>
		<td class="t2Col">

Retrieves based on journal date.

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="vertical-align: top;">

[$CALCRM=WIPBIL|SELSQL=&lt;value&gt;|SELOPT=&lt;value&gt;|DATEFROM=&lt;value&gt;|DATETO=&lt;value&gt;|LIMIT=&lt;value&gt;]

</td>
		<td class="t2Col">

Retrieves based on parameters similar to settings 
		 and options in Posting of WIP screen where:

		
			

- SELSQL - this is to specify the selection to include 
    			 such as Revenue Entity or Administrator. You can specify the 
    			 value or have it retrieved from a cell in the report.

			

- SELOPT - this is to specify which options to include 
    			 and &lt;value&gt; can be:

			

- R - Recurring Fees

			

- T - Time Charges

			

- D - Disbursement Charges

			

- Y - The 'Include Time and/or 
    			 Disbursement only if Recurring Fees are due' option
    			 
    			 To use multiple options, just enter the applicable code e.g. 
    			 SELOPT=RTDY means you want to include all four options

			

- DATEFROM - this is to specify the Date From. You can 
    			 enter the date or have it retrieved from a cell in the report.

			

- DATETO - this is to specify the Date To. You can enter 
    			 the date or have it retrieved from a cell in the report.

			

- LIMIT - this is to specify limit and value can be:

			

- WIPBillAt -To use the Matter 
    			 WIP Limit e.g. LIMIT = WIPBillAt

			

- blank or a number &nbsp;- 
    			 To specify a limit e.g. LIMIT= or LIMIT=500

		
		
Example:

		

[$CALCRM=WIPBIL|SELSQL={o}(RevEntity = '" &amp; $B$2&amp; 
		 "'){/o} AND {o}(AdminCode='" &amp; $B$3&amp; "'){/o}|SELOPT=RTDY|DATEFROM=1/01/1900|DATETO=" 
		 &amp; TEXT($B$1,"d/mm/yyyy") &amp;"|LIMIT=]

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

[$CALCRM=...|DOCINC=0|...]

</td>
		<td class="t2Col">

Draft invoices will be included in the retrieval.

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">

[$CALCRM=...|DOCINC=1|...]

</td>
		<td class="t2Col">

Draft invoices will be excluded from the retrieval.

</td>
	</tr>
</tbody></table>

&nbsp;
###### Additional Codes used in Accounting Excel statements
These codes supplement those available in the Statement Field Wizard.

Use these codes to report on nominal accounts which are set as properties 
 for control accounts; and on other nominal accounts linked to sub-ledgers 
 during journal entry. A simple set of codes can be included in Excel statements 
 to extract the nominal account posting if the sub-ledger has been specified 
 in the journal line. Refer to Excel statement 'Investment Schedule with 
 Journal Details' (SECINV02) for an example of how the codes are used.

<table class="Table1" style="border-collapse: separate;" cellspacing="0px" width="99.065%" border="2" bordercolorlight="#000000" bordercolordark="#000000">
	<colgroup><col style="width: 68.615%;">
	<col style="width: 31.385%;">
	</colgroup><tbody><tr class="t1st">
		<td>

Code

</td>
		<td>

Examples

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">[.sa.?PROP.BR\2] 
		 
		where:
		
			- .sa.? sets the context to nominal account posting with 
    			 the sub-ledger specified.
			- PROP is replaced by the properties set up for <span class="hcp5">control accounts</span>, 
    			 and:
			- 
    - 
        				    - IC = Income
        				    - EX = Expenses
        				    - CG = Capital Gains
        				    - CL = Capital Losses
        				    - EG = Exchange Gains
        				    - EL = Exchange Losses
        				    - UR = Unrealised Value Revaluation, for both Account 
        				 Gains/Losses
        				    - UE = Unrealised Exchange Revaluation, for both Account 
        				 Gains/Losses
        				    - UO = Unrealised Value, for Offset Account
        				    - XL = Unrealised Exchange, for Account Loss
        				    - XO = Unrealised Exchange, for Offset Account
        			
			- .BR\2 denotes 'Sum of the Reporting Period' with the 
    			 sign reversed (negative number is shown as positive and vice 
    			 versa).
		</td>
		<td class="t2Col" style="vertical-align: top;">
			- [.sa.?CG.BR\2]
			- [.sa.?CG+CL+EG+EL.BR\2]
		</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="vertical-align: top;">

[.sa.?POST.BR\2]

		

where:

		
			

- .sa.? sets the context to nominal account posting with 
    			 the sub-ledger specified.

			

- POST is replaced by the <span class="hcp5">posting 
    			 account type</span>.

			

    - 
        				
        
    - PL = Any posting in Type 3 (expenses) or Type 4 
        				 (income) accounts with the sub-ledger specified.
        
        
        				
    - BS = Any posting in Type 1 (assets) or Type 2 (liabilities) 
        				 accounts with the sub-ledger specified.
        
        
        			

		
		
Note that these codes cannot be combined 
		 with any of the other codes.

		
			

- .BR\2 denotes 'Sum of the Reporting Period' with the 
    			 sign reversed (negative number is shown as positive and vice 
    			 versa).

		</td>
		<td class="t2Col" style="vertical-align: top;">
			- [.sa.?PL.BR\2]
		</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

[.sa.?PROP.BJL\2]

		

where:

		
			

- .sa.? sets the context to nominal account posting with 
    			 the sub-ledger specified.

			

- PROP is replaced by the properties set up for control 
    			 accounts.

			

- IC = Income

			

- EX = Expenses

			

- CG = Capital Gains

			

- CL = Capital Losses

			

- EG = Exchange Gains

			

- EL = Exchange Losses

			

- UR = Unrealised Value Revaluation, 
    			 for both Account Gains/Losses

			

- UE = Unrealised Exchange 
    			 Revaluation, for both Account Gains/Losses

			

- UO = Unrealised Value, for 
    			 Offset Account

			

- XL = Unrealised Exchange, 
    			 for Account Loss

			

- XO = Unrealised Exchange, 
    			 for Offset Account

			

- .BJL\2 gets the base currency amount of the journal 
    			 with the sign reversed (negative number is shown as positive 
    			 and vice versa).

		</td>
		<td class="t2Col" style="vertical-align: top;">
			- [.sa.?CG.BJL\2]
			- [.sa.?CG+CL+EG+EL.BJL\2]
		</td>
	</tr>
</tbody></table>

&nbsp;

Use these codes to retrieve exchange rate at different dates.

<table class="Table1" style="border-collapse: separate;" cellspacing="0px" width="99.065%" border="2" bordercolorlight="#000000" bordercolordark="#000000">
	<colgroup><col style="width: 68.615%;">
	<col style="width: 31.385%;">
	</colgroup><tbody><tr class="t1st">
		<td>

Code

</td>
		<td>

Examples

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

[=XR:CCY:PeriodDateSelection]

		

where:

		
			

- CCY is the 'from' currency of the rate to the specified 
    			 'reporting currency'

			

- PeriodDateSelection options can be:

			

- B, M or E followed by either 
    			 a + or - number. The number is a period shift if the report 
    			 is on period selection; and a date shift if the report is 
    			 on date selection.

			

- P99 = Period number where 
    			 valid values are P00 to P48.

			

- D:Date with the date entered 
    			 in a format recognized by the system.

		</td>
		<td class="t2Col" style="vertical-align: top;">
			- [=XR:USD:B25]
			- [=XR:USD:M-2]
			- [=XR:USD:E05]
		
		&nbsp;
		
			- [=XR:USD:P25]
		
		&nbsp;
		
			- [=XR:USD:D12-DEC-2012]
		</td>
	</tr>
</tbody></table>

&nbsp;

Use these codes to report on the control account movements to date, 
 grouped by movement type. A simple set of codes can be included in Excel 
 statements for the entire balance sheet or for selected balance sheet 
 control accounts to achieve this result. Refer to Excel statement 'Balance 
 Sheet Disclosure' (BSDISC01) for an example of how the codes are used 
 in a balance sheet report.

<table class="Table1" style="border-collapse: separate;" cellspacing="0px" border="2" bordercolorlight="#000000" bordercolordark="#000000">
	<colgroup><col width="59">
	<col width="155">
	<col width="264">
	<col width="253">
	</colgroup><tbody><tr class="t1st">
		<td>

Step

</td>
		<td>

Description

</td>
		<td>

Code

</td>
		<td>

Examples

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

1

</td>
		<td class="t2Col" style="vertical-align: top;">

Define the movement 
		 groups. This should be done in the report header section.

</td>
		<td class="t1Col" style="vertical-align: top;">

[$MOVEDEF.TYPE=CODE1-Text 
		 for this code:CODE2-Text for this code:CODE3,CODE4-Text for these 
		 codes]

		

where:

		
			

- TYPE is replaced by the sub-ledger type.

			

- CODE1, CODE2, CODE3 and CODE4 is replaced by the movement 
    			 types of the sub-ledger type selected.

			

- 'Text for these codes' is replaced by user-defined text 
    			 to describe this movement type in the report.

		</td>
		<td class="t2Col" style="vertical-align: top;">

[$MOVEDEF.F=FA-Acquisition 
		 cost:FD-Disposals:FE-Accumulated depreciation:FU,FV,FO,FX-Other 
		 value adjustments]

		

where:

		
			

- F is the sub-ledger type 'Fixed Asset'.

			

- FA, FD, FE, FU, FV, FO and FX are the movement types 
    			 of the sub-ledger type 'Fixed Asset'.

			

- 'Acquisition cost' describes the Acquisition movement 
    			 type [FA] in the report. 'Disposals' describes the Disposal 
    			 movement type [FD] etc.

		
		
<span style="font-weight: bold; font-style: italic;">Note:</span> 
		 The movement types have been enhanced to allow grouping of multiple 
		 movement types, separated by commas.

		

In this example, the movement types FU, FV, FO and FX have been 
		 grouped together as 'Other value adjustments'. It is possible 
		 to disclose these separately, or change the grouping.

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="vertical-align: top;">

2

</td>
		<td class="t2Col" style="vertical-align: top;">

Get the movement 
		 lines for the defined movement types.

		

This can be done at the control account level or at the sub-ledger 
		 level.

</td>
		<td class="t1Col" style="vertical-align: top;">

[.context!MoveSet-2-3]

		

where:

		
			

- .context sets the context to nominal account or to sub-ledger.

			

- !MoveSet-2-3 shows the movement-to-date within the set 
    			 context. These numbers can vary, depending on how many lines 
    			 you wish to copy or to delete.

			

    - 
        				
        
    - 2 - copies 2 lines for each defined account type 
        				 (in $MOVEDEF above);
        
        
        				
    - 3 - deletes 3 lines if the account type is not found.
        
        
        			

		</td>
		<td class="t2Col" style="vertical-align: top;">

[.na!MoveSet-2-3] 
		 OR [.sl!MoveSet-2-3]

		

where:

		
			

- .na or .sl sets the context to nominal account or to 
    			 sub-ledger.

			

- !MoveSet-2-3 shows the movement-to-date within the set 
    			 context.

		</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

3

</td>
		<td class="t2Col" style="vertical-align: top;">

Get the description 
		 of the movement type line.

</td>
		<td class="t1Col" style="vertical-align: top;">

[.context.AMSetDescr]

		

where:

		
			

- .context sets the context to nominal account or to sub-ledger.

			

- .AMSetDescr is replaced by the user-defined text for 
    			 each defined movement type (in $MOVEDEF above).

		</td>
		<td class="t2Col" style="vertical-align: top;">

[.na.AMSetDescr] 
		 OR [.sl.AMSetDescr]

		

where:

		
			

- .na or .sl sets the context to nominal account or to 
    			 sub-ledger.

			

- .AMSetDescr is replaced by 'Acquisition cost' for the 
    			 Acquisition movement type [FA] line in the report; or by 'Disposals' 
    			 for the Disposal movement type [FD] line in the report etc.

		</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="vertical-align: top;">

4

</td>
		<td class="t2Col" style="vertical-align: top;">

Get the amount/quantity 
		 balance of the movement type line.

</td>
		<td class="t1Col" style="vertical-align: top;">

[.context.BALCODE#MSET]

		

where:

		
			

- .context sets the context to nominal account or to sub-ledger.

			

- .BALCODE is replaced by the amount/ quantity balance 
    			 codes.

			

- #MSET shows the amount/quantity for each defined movement 
    			 type (in $MOVEDEF above).

		</td>
		<td class="t2Col" style="vertical-align: top;">

[.na.BR#MSET]

		

where:

		
			

- .context sets the context to nominal account.

			

- .BR is the Sum of the Reporting Period.

			

- #MSET shows the amount for each defined movement type 
    			 (in $MOVEDEF above).

		
		
OR [.sl.QR#MSET]

		

where:

		
			

- .context sets the context to sub-ledger.

			

- .QR is the Quantity Sum of the Reporting Period.

			

- #MSET shows the quantity for each defined movement type 
    			 (in $MOVEDEF above).

		</td>
	</tr>
</tbody></table>

&nbsp;

To specify accounts to be included in an Excel Statement, the directive 
 code [$AccountSelect=&lt;value&gt;] can be used. For this code, value 
 can be:

	

- U = Used - excludes 
    	 accounts that are inactive and unused. This is the default value.

	

- C = Active accounts 
    	 only - excludes accounts that are inactive.

	

- A = Active and 
    	 used accounts - excludes inactive accounts that are not used.

	

- * = All accounts 
    	 including accounts that are inactive or unused.

Note that this is valid for nominal and sub-ledger accounts.

&nbsp;

See also:

	

- [CA Statement Tutorial](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/CAStatementTutorial.xls)

	

- [Master File 
    	 Security in Reports and Widgets](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/MFSEC_Tag_for_Reports_and_Widgets.htm)

&nbsp;

[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; Excel Statements - Fundamentals

&nbsp;

(c) Viewpoint Software for 
 Business Ltd

Version: 8.0.2022.09.20


