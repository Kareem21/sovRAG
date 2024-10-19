




# Intercompany Invoicing and Settlements
## Intercompany Invoicing
This allows users to combine invoice items from different revenue entities 
 into a single (Sales/Purchase) invoice. As such, it recognises the income/expenses 
 of invoice lines in different revenue entities from the invoice header's 
 revenue entity. To enable this, do the following:

	

- Tick the option 'Enable Intercompany Invoice Line Allocations' 
    	 in Configuration &gt; Settings &gt; [System 
    	 Defaults &gt; Practice Management.](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/System_Defaults_-_Practice_Management.htm)

	

- Enable the Revenue Entity field in Detail Lines for Sales/Purchase 
    	 Invoice. For more information, please click [here](javascript:TextPopup(this)).
    
    	<div class="droptext" id="POPUP590815829" style="display: none;">
    		For Sales Invoice, please follow the steps below:
    		
        			    1. In Viewpoint - Home screen, 
        			 click on the Configuration Ribbon button and proceed to Settings 
        			 &gt; Customise &gt; Field Settings.
        			    1. In Field Settings screen, 
        			 select File [8] for Menu Group field, Windows Menus [2] for 
        			 Use In field and Sales Ledger [FABSALES] for Section field.
        			    1. Click Find and the Select 
        			 Menu will be displayed.
        			    1. Head over to Invoicing (Sales) 
        			 and select Create/Edit Invoice.
        			    1. Scroll down towards Detail 
        			 Lines and select Revenue Entity.
        			    1. Click Edit and proceed to 
        			 change both Auth. Req. for Update and Auth. Req. for New fields 
        			 to Regular User.
        			    1. Click Update.
        		
    		For Purchase Invoice, please follow the steps below:
    		
        			    1. In Viewpoint - Home screen, 
        			 click on the Configuration Ribbon button and proceed to Settings 
        			 &gt; Customise &gt; Field Settings.
        			    1. In Field Settings screen, 
        			 select File [8] for Menu Group field, Windows Menus [2] for 
        			 Use In field and Purchase Ledger [FPPURCLG] for Section field.
        			    1. Click Find and the Select 
        			 Menu will be displayed.
        			    1. Head over to Invoicing and 
        			 select Create/Edit Purchase Orders.
        			    1. Scroll down towards Detail 
        			 Lines and select Revenue Entity.
        			    1. Click Edit and proceed to 
        			 change both Auth. Req. for Update and Auth. Req. for New fields 
        			 to Regular User.
        			    1. Click Update.
        		
     </div>

&nbsp;
### Define Revenue Entity for Sales Invoice Line
In a draft invoice, the default revenue entity for an invoice line is:

	

- The revenue entity of the invoice Matter if the invoice line 
    	 was created using Posting of WIP.

	

- The revenue entity seen in the invoice header if the invoice 
    	 line is an administrative mark-up added from Posting of WIP.

	

- The revenue entity seen in the invoice header if the invoice 
    	 line is an additional charge created using tags defined for the revenue 
    	 entity of the invoice header.

For the latter two, you can change the default revenue entity to a different 
 revenue entity. If you add a new invoice line through the Create/Edit 
 Invoice screen, then you can also specify a different revenue entity for 
 this line. When the draft invoice is posted, the amounts of each service, 
 administrative mark-up and additional charges will be posted to its own 
 revenue entity.

&nbsp;
### Posting Sales Invoice with Multiple Revenue Entities
The income lines for a revenue entity that is different from the invoice 
 header are posted to the following:

	

- The account of the revenue entity for the invoice line.

	

- The Intercompany sub-ledger account for both the Intercompany 
    	 Account - R.GI ledger and the account of the revenue entity of the 
    	 invoice header. The sub-ledger is created based on the configuration 
    	 of the ledger in the Account Mapping. The sub-ledger account is created 
    	 only when the revenue entity of the invoice line is different from 
    	 the invoice header.

The following is a sample posting:

&nbsp;
#### Client Account Posting
<table class="Table1" style="border-collapse: separate;" cellspacing="0px" border="1">
	<colgroup><col style="width: 25%;">
	<col style="width: 25%;">
	<col style="width: 25%;">
	<col style="width: 25%;">
	</colgroup><tbody><tr class="t1st">
		<td>&nbsp;</td>
		<td>

Invoice Currency (EUR)

</td>
		<td>

VAT

</td>
		<td>

Revenue Entity

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">Service 1</td>
		<td class="t2Col">

50.00

</td>
		<td class="t1Col">

5.00

</td>
		<td class="t2Col">

B

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">Service 2</td>
		<td class="t2Col">

100.00

</td>
		<td class="t1Col">

10.00

</td>
		<td class="t2Col">

C

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">Service 3</td>
		<td class="t2Col">

80.00

</td>
		<td class="t1Col">

-

</td>
		<td class="t2Col">

A

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">Service 4</td>
		<td class="t2Col">

200.00

</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

&nbsp;

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">&nbsp;</td>
		<td class="t2Col">

&nbsp;

</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">&nbsp;</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">Invoice Header</td>
		<td class="t2Col">

&nbsp;

</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

A

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">Rounding difference</td>
		<td class="t2Col">

&nbsp;

</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">&nbsp;</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">Debit note - total</td>
		<td class="t2Col">

445.00

</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">&nbsp;</td>
	</tr>
</tbody></table>

&nbsp;
#### Header - Revenue Entity A Posting
<table class="Table1" style="border-collapse: separate;" cellspacing="0px" border="1">
	<colgroup><col style="width: 25%;">
	<col style="width: 25%;">
	<col style="width: 25%;">
	<col style="width: 25%;">
	</colgroup><tbody><tr class="t1st">
		<td>&nbsp;</td>
		<td>&nbsp;</td>
		<td>

DR

</td>
		<td>

CR

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">R.GI + Serv Code 1 (B)</td>
		<td class="t2Col">R.GI</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

50.00

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">R.GI + Serv Code (C)</td>
		<td class="t2Col">R.GI</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

100.00

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">R.SA + Serv Code 3</td>
		<td class="t2Col">Income Accounts</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

80.00

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">R.GI + Serv Code 4 (B)</td>
		<td class="t2Col">R.GI</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

200.00

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">&nbsp;</td>
		<td class="t2Col">&nbsp;</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

&nbsp;

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">R.SV</td>
		<td class="t2Col">VAT</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

15.00

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">&nbsp;</td>
		<td class="t2Col">&nbsp;</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

&nbsp;

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">R.SR</td>
		<td class="t2Col">Rounding Difference</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

&nbsp;

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">R.SC</td>
		<td class="t2Col">Debtors</td>
		<td class="t1Col">

445.00

</td>
		<td class="t2Col">

&nbsp;

</td>
	</tr>
</tbody></table>

&nbsp;
#### Revenue Entity B Posting
<table class="Table1" style="border-collapse: separate;" cellspacing="0px" border="1">
	<colgroup><col style="width: 25%;">
	<col style="width: 25%;">
	<col style="width: 25%;">
	<col style="width: 25%;">
	</colgroup><tbody><tr class="t1st">
		<td>&nbsp;</td>
		<td>&nbsp;</td>
		<td>

DR

</td>
		<td>

CR

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">R.SA + Serv Code 1</td>
		<td class="t2Col">Income Accounts</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

50.00

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">R.GI (A)</td>
		<td class="t2Col">R.GI</td>
		<td class="t1Col">

50.00

</td>
		<td class="t2Col">

&nbsp;

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">R.SA + Serv Code 4</td>
		<td class="t2Col">Income Accounts</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

200.00

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">R.GI (A)</td>
		<td class="t2Col">R.GI</td>
		<td class="t1Col">

200.00

</td>
		<td class="t2Col">

&nbsp;

</td>
	</tr>
</tbody></table>

&nbsp;
#### Revenue Entity C Posting
<table class="Table1" style="border-collapse: separate;" cellspacing="0px" border="1">
	<colgroup><col style="width: 25%;">
	<col style="width: 25%;">
	<col style="width: 25%;">
	<col style="width: 25%;">
	</colgroup><tbody><tr class="t1st">
		<td>&nbsp;</td>
		<td>&nbsp;</td>
		<td>

DR

</td>
		<td>

CR

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">R.SA + Serv Code 2</td>
		<td class="t2Col">Income Accounts</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

100.00

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">R.GI (A)</td>
		<td class="t2Col">R.GI</td>
		<td class="t1Col">

100.00

</td>
		<td class="t2Col">

&nbsp;

</td>
	</tr>
</tbody></table>

&nbsp;

&nbsp;
### Define Revenue Entity for Purchase Invoice Line
For purchase invoices, you can set a revenue entity for each invoice 
 line, allowing selection of the nominal account from the other revenue 
 entity.

&nbsp;
### Posting Purchase Invoice with Multiple Revenue Entities
The expense lines for a Revenue Entity that is different from the header 
 are posted to the following:

	

- The account of the revenue entity of the line.

	

- The Intercompany sub-ledger account for both the Intercompany 
    	 Account - R.GI ledger and the account of the revenue entity of the 
    	 purchase order header. The sub-ledger is created based on the configuration 
    	 of the ledger in the Account Mapping. The sub-ledger account is created 
    	 only when the revenue entity of a service line is different from the 
    	 purchase order header.

The following is a sample posting:

&nbsp;
#### Client Account Posting
<table class="Table1" style="border-collapse: separate;" cellspacing="0px" border="1">
	<colgroup><col style="width: 20%;">
	<col style="width: 20%;">
	<col style="width: 20%;">
	<col style="width: 20%;">
	<col style="width: 20%;">
	</colgroup><tbody><tr class="t1st">
		<td>&nbsp;</td>
		<td>

Invoice Currency (EUR)

</td>
		<td>

VAT

</td>
		<td>

Revenue Entity

</td>
		<td>

Nominal Account

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

Service 1

</td>
		<td class="t2Col">

10.00

</td>
		<td class="t1Col">

1.00

</td>
		<td class="t2Col">

A

</td>
		<td class="t1Col">

8430

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">

Service 2

</td>
		<td class="t2Col">

100.00

</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

B

</td>
		<td class="t1Col">

8490

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

&nbsp;

</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

&nbsp;

</td>
		<td class="t1Col">

&nbsp;

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">

VAT

</td>
		<td class="t2Col">

1.00

</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

&nbsp;

</td>
		<td class="t1Col">

&nbsp;

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

Invoice Header Revenue Entity

</td>
		<td class="t2Col">

&nbsp;

</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

A

</td>
		<td class="t1Col">

&nbsp;

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">

Rounding difference

</td>
		<td class="t2Col">

&nbsp;

</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

&nbsp;

</td>
		<td class="t1Col">

&nbsp;

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

Credit note - total

</td>
		<td class="t2Col">

111.00

</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

&nbsp;

</td>
		<td class="t1Col">

&nbsp;

</td>
	</tr>
</tbody></table>

&nbsp;
#### Header - Revenue Entity A Posting
<table class="Table1" style="border-collapse: separate;" cellspacing="0px" border="1">
	<colgroup><col style="width: 25%;">
	<col style="width: 25%;">
	<col style="width: 25%;">
	<col style="width: 25%;">
	</colgroup><tbody><tr class="t1st">
		<td>&nbsp;</td>
		<td>&nbsp;</td>
		<td>

DR

</td>
		<td>

CR

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

R.GI + Serv Code 1

</td>
		<td class="t2Col">

8430

</td>
		<td class="t1Col">

10.00

</td>
		<td class="t2Col">

&nbsp;

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">

R.GI + Serv Code 2 (B)

</td>
		<td class="t2Col">

R.GI

</td>
		<td class="t1Col">

100.00

</td>
		<td class="t2Col">

&nbsp;

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

&nbsp;

</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

&nbsp;

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">

R.PV

</td>
		<td class="t2Col">

VAT

</td>
		<td class="t1Col">

1.00

</td>
		<td class="t2Col">

&nbsp;

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

R.PE

</td>
		<td class="t2Col">

Exchange difference

</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

&nbsp;

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">

R.PR

</td>
		<td class="t2Col">

Rounding difference

</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

&nbsp;

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

R.PC

</td>
		<td class="t2Col">

Creditors

</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

111.00

</td>
	</tr>
</tbody></table>

&nbsp;
#### Revenue Entity B Posting
<table class="Table1" style="border-collapse: separate;" cellspacing="0px" border="1">
	<colgroup><col style="width: 25%;">
	<col style="width: 25%;">
	<col style="width: 25%;">
	<col style="width: 25%;">
	</colgroup><tbody><tr class="t1st">
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

DR

</td>
		<td>

CR

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

R.PA + Serv Code 2

</td>
		<td class="t2Col">

8490

</td>
		<td class="t1Col">

100.00

</td>
		<td class="t2Col">

&nbsp;

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">

R.GI (A)

</td>
		<td class="t2Col">

R.GI

</td>
		<td class="t1Col">

&nbsp;

</td>
		<td class="t2Col">

100.00

</td>
	</tr>
</tbody></table>

&nbsp;
## Intercompany Settlement
Intercompany settlement allows settlement of invoices for one revenue 
 entity to the bank account of another revenue entity. To enable this, 
 tick the option 'Allow Intercompany Settlements' in Configuration &gt; 
 Settings &gt; [System 
 Defaults &gt; Practice Management](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/System_Defaults_-_Practice_Management.htm) and ensure that account mapping 
 is done for Intercompany Account - R.GI in [Account 
 Mapping](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Account_Mapping.htm) for the revenue entity.

&nbsp;
### Performing Intercompany Settlement
For sales invoices, in Receivables and Settlements screen, you can choose 
 active bank accounts of all available revenue entities.

For purchase orders, in Payables screen, when you select multiple purchase 
 orders with different revenue entities, you can click Settle Multiple 
 and select the relevant bank account. If intercompany settlement is not 
 enabled, selecting more than one purchase orders with different revenue 
 entities will result in the message 'Selected records are for different 
 revenue entities' when you click Settle Multiple.

&nbsp;
### Postings to Client Accountant
#### Sample 1 - Settlement on Client Invoice 1 - Partly Paid
<table cellspacing="0" border="1" class="hcp5">
	<colgroup><col style="width: 8.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 12%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	</colgroup><tbody><tr>
		<td rowspan="2" colspan="4">

<span class="hcp6">Invoice/Receipt details</span>

</td>
		<td colspan="8">

Rate @0.12345

</td>
		
	</tr>
	<tr>
		<td colspan="2">

Posting 
		 Bank Entity

</td>
		<td colspan="2">

(i) CCY = Inv. CCY

</td>
		<td colspan="2">

(II) CCY = Base 
		 CCY

</td>
		<td colspan="2">

(iii) Neither (i) 
		 nor (ii)

</td>
		
	</tr>
	<tr>
		<td>&nbsp;</td>
		<td>

Inv. CCY

</td>
		<td>

Exch. Rate

</td>
		<td>

Base CCY

</td>
		<td colspan="2">&nbsp;</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
	</tr>
	<tr>
		<td>

Invoice Amount

</td>
		<td>

1,250.00

</td>
		<td>

0.24

</td>
		<td>

300.00

</td>
		<td>

R.GB + Account No.

</td>
		<td>

Bank Account

</td>
		<td>

750.00

</td>
		<td>

&nbsp;

</td>
		<td>

187.50

</td>
		<td>

&nbsp;

</td>
		<td>

92.59

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td>

Amount Received

</td>
		<td>

750.00

</td>
		<td>

0.25

</td>
		<td>

187.50

</td>
		<td>

R.SH

</td>
		<td>

Bank Charges

</td>
		<td>

&nbsp;

</td>
		<td>

25.00

</td>
		<td>

&nbsp;

</td>
		<td>

6.25

</td>
		<td>

&nbsp;

</td>
		<td>

3.09

</td>
	</tr>
	<tr>
		<td>

Bank Charges

</td>
		<td>

25.00

</td>
		<td>

0.25

</td>
		<td>

6.25

</td>
		<td>

R.GI

</td>
		<td>

Intercompany

</td>
		<td>

&nbsp;

</td>
		<td>

725.00

</td>
		<td>

&nbsp;

</td>
		<td>

181.25

</td>
		<td>

&nbsp;

</td>
		<td>

89.50

</td>
	</tr>
	<tr>
		<td>

Written Off

</td>
		<td>

15.00

</td>
		<td>

0.25

</td>
		<td>

3.75

</td>
		<td rowspan="4" colspan="8">&nbsp;</td>
		
	</tr>
	<tr>
		<td>

Nett Settled

</td>
		<td>

740.00

</td>
		<td>

0.25

</td>
		<td>

185.00

</td>
		
	</tr>
	<tr>
		<td>

Exchange Gain/Loss

</td>
		<td>&nbsp;</td>
		<td>&nbsp;</td>
		<td>

7.40

</td>
		
	</tr>
	<tr>
		<td>

Outstanding

</td>
		<td>

510.00

</td>
		<td>

0.24

</td>
		<td>

122.40

</td>
		
	</tr>
	<tr>
		<td colspan="4" rowspan="8">&nbsp;</td>
		<td colspan="8">

&nbsp;&nbsp;Rate@0.12345

</td>
		
	</tr>
	<tr>
		<td colspan="2">

<span class="hcp6">Posting 
		 Revenue Entity</span>

</td>
		<td colspan="2">

(i) CCY = Inv. CCY

</td>
		<td colspan="2">

(II) CCY = Base 
		 CCY

</td>
		<td colspan="2">

(iii) Neither (i) 
		 nor (ii)

</td>
		
	</tr>
	<tr>
		<td>&nbsp;</td>
		<td>&nbsp;</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
	</tr>
	<tr>
		<td>

R.GI

</td>
		<td>

Intercompany

</td>
		<td>

725.00

</td>
		<td>

&nbsp;

</td>
		<td>

181.25

</td>
		<td>

&nbsp;

</td>
		<td>

89.50

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td>

R.SW

</td>
		<td>

Written Off

</td>
		<td>

15.00

</td>
		<td>

&nbsp;

</td>
		<td>

3.75

</td>
		<td>

&nbsp;

</td>
		<td>

1.85

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td>

R.SC

</td>
		<td>

Debtors

</td>
		<td>

&nbsp;

</td>
		<td>

740.00

</td>
		<td>

&nbsp;

</td>
		<td>

185.00

</td>
		<td>

&nbsp;

</td>
		<td>

91.35

</td>
	</tr>
	<tr>
		<td>

R.SE

</td>
		<td>

Exchange Diff.

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

7.40

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td>

R.SC

</td>
		<td>

Debtors

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

7.40

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
	</tr>
</tbody></table>

&nbsp;
#### Sample 2 - Settlement on Client Invoice 2 - Fully Paid
<table cellspacing="0" border="1" class="hcp5">
	<colgroup><col style="width: 8.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 12%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	</colgroup><tbody><tr>
		<td rowspan="2" colspan="4">

<span class="hcp6">Invoice/Receipt details</span>

</td>
		<td colspan="8">

Rate @0.12345

</td>
		
	</tr>
	<tr>
		<td colspan="2">

Posting 
		 Bank Entity

</td>
		<td colspan="2">

(i) CCY = Inv. CCY

</td>
		<td colspan="2">

(II) CCY = Base 
		 CCY

</td>
		<td colspan="2">

(iii) Neither (i) 
		 nor (ii)

</td>
		
	</tr>
	<tr>
		<td>&nbsp;</td>
		<td>

Inv. CCY

</td>
		<td>

Exch. Rate

</td>
		<td>

Base CCY

</td>
		<td colspan="2">&nbsp;</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
	</tr>
	<tr>
		<td>

Invoice Amount

</td>
		<td>

510.00

</td>
		<td>

0.24

</td>
		<td>

122.40

</td>
		<td>

R.GB + Account No.

</td>
		<td>

Bank Account

</td>
		<td>

520.00

</td>
		<td>

&nbsp;

</td>
		<td>

130.00

</td>
		<td>

&nbsp;

</td>
		<td>

64.19

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td>

Amount Received

</td>
		<td>

520.00

</td>
		<td>

0.25

</td>
		<td>

130.00

</td>
		<td>

R.SH

</td>
		<td>

Bank Charges

</td>
		<td>

&nbsp;

</td>
		<td>

30.00

</td>
		<td>

&nbsp;

</td>
		<td>

7.50

</td>
		<td>

&nbsp;

</td>
		<td>

3.70

</td>
	</tr>
	<tr>
		<td>

Bank Charges

</td>
		<td>

30.00

</td>
		<td>

0.25

</td>
		<td>

7.50

</td>
		<td>

R.GI

</td>
		<td>

Intercompany

</td>
		<td>

&nbsp;

</td>
		<td>

490.00

</td>
		<td>

&nbsp;

</td>
		<td>

122.50

</td>
		<td>

&nbsp;

</td>
		<td>

60.49

</td>
	</tr>
	<tr>
		<td>

Written Off

</td>
		<td>

20.00

</td>
		<td>

0.25

</td>
		<td>

5.00

</td>
		<td rowspan="4" colspan="8">&nbsp;</td>
		
	</tr>
	<tr>
		<td>

Nett Settled

</td>
		<td>

510.00

</td>
		<td>

0.25

</td>
		<td>

127.50

</td>
		
	</tr>
	<tr>
		<td>

Exchange Gain/Loss

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

5.10

</td>
		
	</tr>
	<tr>
		<td>

Outstanding

</td>
		<td>

0.00

</td>
		<td>

0.24

</td>
		<td>

0.00

</td>
		
	</tr>
	<tr>
		<td colspan="4" rowspan="8">&nbsp;</td>
		<td colspan="8">

&nbsp;&nbsp;&nbsp;Rate@0.12345

</td>
		
	</tr>
	<tr>
		<td colspan="2">

<span class="hcp6">Posting 
		 Revenue Entity</span>

</td>
		<td colspan="2">

(i) CCY = Inv. CCY

</td>
		<td colspan="2">

(II) CCY = Base 
		 CCY

</td>
		<td colspan="2">

(iii) Neither (i) 
		 nor (ii)

</td>
		
	</tr>
	<tr>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
	</tr>
	<tr>
		<td>

R.GI

</td>
		<td>

Intercompany

</td>
		<td>

490.00

</td>
		<td>

&nbsp;

</td>
		<td>

122.50

</td>
		<td>

&nbsp;

</td>
		<td>

60.49

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td>

R.SW

</td>
		<td>

Written Off

</td>
		<td>

20.00

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

5.00

</td>
		<td>

2.47

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td>

R.SC

</td>
		<td>

Debtors

</td>
		<td>

&nbsp;

</td>
		<td>

510.00

</td>
		<td>

&nbsp;

</td>
		<td>

117.50

</td>
		<td>

&nbsp;

</td>
		<td>

62.96

</td>
	</tr>
	<tr>
		<td>

R.SE

</td>
		<td>

Exchange Diff.

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

12.50

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td>

R.SC

</td>
		<td>

Debtors

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

12.50

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
	</tr>
</tbody></table>

&nbsp;
#### Sample 3 - Receipt of Money on Matter Account
<table cellspacing="0" border="1" class="hcp5">
	<colgroup><col style="width: 8.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 12%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	</colgroup><tbody><tr>
		<td rowspan="2" colspan="4">

<span class="hcp6">Invoice/Receipt details</span>

</td>
		<td colspan="8">

Rate @0.12345

</td>
		
	</tr>
	<tr>
		<td colspan="2">

Posting 
		 Bank Entity

</td>
		<td colspan="2">

(i) CCY = Inv. CCY

</td>
		<td colspan="2">

(II) CCY = Base 
		 CCY

</td>
		<td colspan="2">

(iii) Neither (i) 
		 nor (ii)

</td>
		
	</tr>
	<tr>
		<td>&nbsp;</td>
		<td>

Matter CCY

</td>
		<td>

Exch. Rate

</td>
		<td>

Base CCY

</td>
		<td colspan="2">&nbsp;</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
	</tr>
	<tr>
		<td>

Amount Received

</td>
		<td>

115.00

</td>
		<td>

0.25

</td>
		<td>

28.75

</td>
		<td>

R.GB + Account No.

</td>
		<td>

Bank Account

</td>
		<td>

115.00

</td>
		<td>

&nbsp;

</td>
		<td>

28.75

</td>
		<td>

&nbsp;

</td>
		<td>

14.20

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td>

Bank Charges

</td>
		<td>

5.00

</td>
		<td>

0.25

</td>
		<td>

1.25

</td>
		<td>

R.SH

</td>
		<td>

Bank Charges

</td>
		<td>

&nbsp;

</td>
		<td>

5.00

</td>
		<td>

&nbsp;

</td>
		<td>

1.25

</td>
		<td>

&nbsp;

</td>
		<td>

0.62

</td>
	</tr>
	<tr>
		<td>&nbsp;</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

R.GI

</td>
		<td>

Intercompany

</td>
		<td>

&nbsp;

</td>
		<td>

110.00

</td>
		<td>

&nbsp;

</td>
		<td>

27.50

</td>
		<td>

&nbsp;

</td>
		<td>

13.58

</td>
	</tr>
	<tr>
		<td colspan="4" rowspan="5">&nbsp;</td>
		<td colspan="8">

&nbsp;Rate@0.12345

</td>
		
	</tr>
	<tr>
		<td colspan="2">

<span class="hcp6">Posting 
		 Revenue Entity</span>

</td>
		<td colspan="2">

(i) CCY = Inv. CCY

</td>
		<td colspan="2">

(II) CCY = Base 
		 CCY

</td>
		<td colspan="2">

(iii) Neither (i) 
		 nor (ii)

</td>
		
	</tr>
	<tr>
		<td>&nbsp;</td>
		<td>&nbsp;</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
	</tr>
	<tr>
		<td>

R.GI

</td>
		<td>

Intercompany

</td>
		<td>

110.00

</td>
		<td>

&nbsp;

</td>
		<td>

27.50

</td>
		<td>

&nbsp;

</td>
		<td>

13.58

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td>

R.SC

</td>
		<td>

Debtors

</td>
		<td>

&nbsp;

</td>
		<td>

110.00

</td>
		<td>

&nbsp;

</td>
		<td>

27.50

</td>
		<td>

&nbsp;

</td>
		<td>

13.58

</td>
	</tr>
</tbody></table>
#### &nbsp;
#### Sample 4 - Multiple Document Settlement (All invoices must be for the &#13;&#10; same Revenue Entity)
<table cellspacing="0" border="1" class="hcp5">
	<colgroup><col style="width: 8.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 12%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	</colgroup><tbody><tr>
		<td rowspan="2" colspan="4">

<span class="hcp6">Receipt details</span>

</td>
		<td colspan="8">

Rate @0.12345

</td>
		
	</tr>
	<tr>
		<td colspan="2">

Posting 
		 Revenue Entity

</td>
		<td colspan="2">

(i) CCY = Inv. CCY

</td>
		<td colspan="2">

(II) CCY = Base 
		 CCY

</td>
		<td colspan="2">

(iii) Neither (i) 
		 nor (ii)

</td>
		
	</tr>
	<tr>
		<td>&nbsp;</td>
		<td>

Inv. CCY

</td>
		<td>

Exch. Rate

</td>
		<td>

Base CCY

</td>
		<td colspan="2">&nbsp;</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
	</tr>
	<tr>
		<td>

Amount Received

</td>
		<td>

320.00

</td>
		<td>

0.25

</td>
		<td>

80.00

</td>
		<td>

R.GB + Account No.

</td>
		<td>

Bank Account

</td>
		<td>

320.00

</td>
		<td>

&nbsp;

</td>
		<td>

80.00

</td>
		<td>

&nbsp;

</td>
		<td>

39.50

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td>

Bank Charges

</td>
		<td>

10.00

</td>
		<td>

0.25

</td>
		<td>

2.50

</td>
		<td>

R.SH

</td>
		<td>

Bank Charges

</td>
		<td>

&nbsp;

</td>
		<td>

10.00

</td>
		<td>

&nbsp;

</td>
		<td>

2.50

</td>
		<td>

&nbsp;

</td>
		<td>

1.23

</td>
	</tr>
	<tr>
		<td rowspan="12" colspan="4">&nbsp;</td>
		<td>

R.GI

</td>
		<td>

Intercompany

</td>
		<td>

&nbsp;

</td>
		<td>

310.00

</td>
		<td>

&nbsp;

</td>
		<td>

77.50

</td>
		<td>

&nbsp;

</td>
		<td>

38.27

</td>
	</tr>
	<tr>
		<td colspan="8">

Rate@0.12345

</td>
		
	</tr>
	<tr>
		<td colspan="2">

Posting 
		 Revenue Entity

</td>
		<td colspan="2">

(i) CCY = Inv. CCY

</td>
		<td colspan="2">

(II) CCY = Base 
		 CCY

</td>
		<td colspan="2">

(iii) Neither (i) 
		 nor (ii)

</td>
		
	</tr>
	<tr>
		<td>&nbsp;</td>
		<td>&nbsp;</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
	</tr>
	<tr>
		<td>

R.GI

</td>
		<td>

Intercompany

</td>
		<td>

310.00

</td>
		<td>

&nbsp;

</td>
		<td>

77.50

</td>
		<td>

&nbsp;

</td>
		<td>

38.27

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td>

R.SC

</td>
		<td>

Debtors

</td>
		<td>

&nbsp;

</td>
		<td>

310.00

</td>
		<td>

&nbsp;

</td>
		<td>

77.50

</td>
		<td>

&nbsp;

</td>
		<td>

38.27

</td>
	</tr>
	<tr>
		<td colspan="8">

Rate@0.12345

</td>
		
	</tr>
	<tr>
		<td colspan="2">

<span class="hcp6">Posting 
		 Client File</span>

</td>
		<td colspan="2">

(i) CCY = Inv. CCY

</td>
		<td colspan="2">

(II) CCY = Base 
		 CCY

</td>
		<td colspan="2">

(iii) Neither (i) 
		 nor (ii)

</td>
		
	</tr>
	<tr>
		<td>&nbsp;</td>
		<td>&nbsp;</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
	</tr>
	<tr>
		<td>

C.GB

</td>
		<td>

Receipt (Clearing Account)

</td>
		<td>

&nbsp;

</td>
		<td>

320.00

</td>
		<td>

77.50

</td>
		<td>

&nbsp;

</td>
		<td>

39.50

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td>

C.GM

</td>
		<td>

Matter Account

</td>
		<td>

310.00

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td>

C.GC

</td>
		<td>

Bank Charges

</td>
		<td>

10.00

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

77.50

</td>
		<td>

&nbsp;

</td>
		<td>

39.50

</td>
	</tr>
</tbody></table>

&nbsp;
#### Sample 5 - Settle to Matter - Other Billing File
<table cellspacing="0" border="1" class="hcp5">
	<colgroup><col style="width: 8.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 12%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	<col style="width: 6.333%;">
	</colgroup><tbody><tr>
		<td rowspan="2" colspan="4">

<span class="hcp6">Invoice/Settlement details</span>

</td>
		<td colspan="8">

Rate @0.12345

</td>
		
	</tr>
	<tr>
		<td colspan="2">

Posting 
		 Revenue Entity

</td>
		<td colspan="2">

(i) CCY = Inv. CCY

</td>
		<td colspan="2">

(II) CCY = Base 
		 CCY

</td>
		<td colspan="2">

(iii) Neither (i) 
		 nor (ii)

</td>
		
	</tr>
	<tr>
		<td>&nbsp;</td>
		<td>

Inv. CCY

</td>
		<td>

Exch. Rate

</td>
		<td>

Base CCY

</td>
		<td colspan="2">

&nbsp;

</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
	</tr>
	<tr>
		<td>

Invoice Amount

</td>
		<td>

200.00

</td>
		<td>

0.24

</td>
		<td>

48.00

</td>
		<td>

R.GM

</td>
		<td>

Matter Account

</td>
		<td>

200.00

</td>
		<td>

&nbsp;

</td>
		<td>

50.00

</td>
		<td>

&nbsp;

</td>
		<td>

24.69

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td>

Amount Settled

</td>
		<td>

200.00

</td>
		<td>

0.25

</td>
		<td>

50.00

</td>
		<td>

R.SC

</td>
		<td>

Debtor

</td>
		<td>

&nbsp;

</td>
		<td>

210.00

</td>
		<td>

&nbsp;

</td>
		<td>

52.50

</td>
		<td>

&nbsp;

</td>
		<td>

25.92

</td>
	</tr>
	<tr>
		<td>

Written Off

</td>
		<td>

10.00

</td>
		<td>

0.25

</td>
		<td>

2.50

</td>
		<td>

R.SW

</td>
		<td>

Write Off

</td>
		<td>

10.00

</td>
		<td>

&nbsp;

</td>
		<td>

2.50

</td>
		<td>

&nbsp;

</td>
		<td>

1.23

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td>

Exchange Gain/Loss

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

2.00

</td>
		<td>

R.SE

</td>
		<td>

Exchange Diff.

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

2.00

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td>

Outstanding

</td>
		<td>

&nbsp;

</td>
		<td>

0.24

</td>
		<td>

0.00

</td>
		<td>

R.SC

</td>
		<td>

Debtors

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

2.00

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td rowspan="9" colspan="4">&nbsp;</td>
		<td colspan="8">&nbsp; 
		  
<span style="font-weight: bold; font-style: italic;">Client 
		 Account</span> 
		  
&nbsp;</td>
		
	</tr>
	<tr>
		<td colspan="8">

Rate @0.12345

</td>
		
	</tr>
	<tr>
		<td colspan="2">

Posting 
		 Received Matter Account

</td>
		<td colspan="2">

(i) CCY = Inv. CCY

</td>
		<td colspan="2">

(II) CCY = Base 
		 CCY

</td>
		<td colspan="2">

(iii) Neither (i) 
		 nor (ii)

</td>
		
	</tr>
	<tr>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
	</tr>
	<tr>
		<td>

C.GM

</td>
		<td>

Matter Account

</td>
		<td>

&nbsp;

</td>
		<td>

200.00

</td>
		<td>

&nbsp;

</td>
		<td>

50.00

</td>
		<td>

&nbsp;

</td>
		<td>

24.69

</td>
	</tr>
	<tr>
		<td>

C.GB

</td>
		<td>

Clearing Account

</td>
		<td>

210.00

</td>
		<td>

&nbsp;

</td>
		<td>

52.50

</td>
		<td>

&nbsp;

</td>
		<td>

25.92

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td>

C.SW

</td>
		<td>

Write Off

</td>
		<td>

&nbsp;

</td>
		<td>

10.00

</td>
		<td>

&nbsp;

</td>
		<td>

2.50

</td>
		<td>

&nbsp;

</td>
		<td>

1.23

</td>
	</tr>
	<tr>
		<td>

C.SE

</td>
		<td>

Exchange Diff.

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

2.00

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td>

C.SC

</td>
		<td>

Creditor

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

2.00

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td colspan="4" rowspan="8">&nbsp;</td>
		<td colspan="8">

Rate@0.12345

</td>
		
	</tr>
	<tr>
		<td colspan="2">

<span class="hcp6">Posting 
		 Received Matter Account</span>

</td>
		<td colspan="2">

(i) CCY = Inv. CCY

</td>
		<td colspan="2">

(II) CCY = Base 
		 CCY

</td>
		<td colspan="2">

(iii) Neither (i) 
		 nor (ii)

</td>
		
	</tr>
	<tr>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
		<td>

DR

</td>
		<td>

CR

</td>
	</tr>
	<tr>
		<td>

C.GB

</td>
		<td>

Clearing account

</td>
		<td>

&nbsp;

</td>
		<td>

200.00

</td>
		<td>

&nbsp;

</td>
		<td>

50.00

</td>
		<td>

&nbsp;

</td>
		<td>

24.69

</td>
	</tr>
	<tr>
		<td>

C.SC

</td>
		<td>

Creditor

</td>
		<td>

210.00

</td>
		<td>

&nbsp;

</td>
		<td>

52.50

</td>
		<td>

&nbsp;

</td>
		<td>

25.92

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td>

C.SW

</td>
		<td>

Write Off

</td>
		<td>

&nbsp;

</td>
		<td>

10.00

</td>
		<td>

&nbsp;

</td>
		<td>

2.50

</td>
		<td>

&nbsp;

</td>
		<td>

1.23

</td>
	</tr>
	<tr>
		<td>

C.SE

</td>
		<td>

Exchange Diff.

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

2.00

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
	</tr>
	<tr>
		<td>

C.SC

</td>
		<td>

Creditor

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

2.00

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
		<td>

&nbsp;

</td>
	</tr>
</tbody></table>

&nbsp;

 
&nbsp;

You are here:[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; [Additional Information](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Confidential_Database.htm) &gt; [Practice Management](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Client_Accountant/Approval_Cards_for_Payees_and_Payments.htm) &gt; Intercompany Invoicing and Settlements
 
&nbsp;
 
(c) Viewpoint Software for 
 Business Ltd
 
Version: 8.0.2022.09.20




