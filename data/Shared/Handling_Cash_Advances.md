



# Handling Cash Advances using Matters
Cash advances from clients typically come in three forms: retainer fees, 
 client monies and unidentified/unallocated receipts.

<table class="Table1" style="border-top-color: rgb(0, 0, 0); border-top-style: solid; border-top-width: 2px; border-right-color: rgb(0, 0, 0); border-right-style: solid; border-right-width: 2px; border-bottom-color: rgb(0, 0, 0); border-bottom-style: solid; border-bottom-width: 2px; border-left-color: rgb(0, 0, 0); border-left-style: solid; border-left-width: 2px;" cellspacing="0px" width="800">
	<colgroup><col width="200">
	<col width="500">
	</colgroup><tbody><tr class="t1st">
		<td>

Type of Advance

</td>
		<td>

Description

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

Retainer 
		 Fee

</td>
		<td class="t2Col">

These funds are paid in 
		 advance by your client, for future services to be supplied by 
		 the Revenue Company, e.g. to retain/secure the services of a consultant/professional.

		

These 
		 fees belong to you once the payment is made and can be used immediately 
		 for costs incurred.

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">

Client 
		 Monies

</td>
		<td class="t2Col">

These are advances which 
		 do not belong to you, and will be used to make client payments 
		 such as government fees.

		

Depending 
		 on regulatory requirements, these monies are commonly kept in 
		 a segregated trust bank account in the Revenue Entity’s name.

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

Unidentified/Unallocated 
		 Receipts

</td>
		<td class="t2Col">

You 
		 have either not identified who you received the advance from; 
		 or you have not allocated the advance to the works being performed 
		 for the client.

</td>
	</tr>
</tbody></table>

&nbsp;

This section will explain how you can manage cash advances from clients 
 by using the Matters feature in Practice Management, and assumes the following:

	

- <span lang="EN-GB" xml:lang="EN-GB">That you are familiar with 
    	 Practice Management features such as Matters and the settlement of 
    	 sales invoices;</span>

	

- <span lang="EN-GB" xml:lang="EN-GB">That you have set up Bank 
    	 Accounts for the Revenue Entity; and</span>

	

- <span lang="EN-GB" xml:lang="EN-GB">That you have completed 
    	 the Account Mapping for Matters and Bank Accounts in Configuration 
    	 &gt; Business Parameters &gt; Practice Management.</span>

&nbsp;
### []()Recording Cash Advances
You can create as many Matters as required based on the types of cash 
 advances you have received from the client. For instance, if the advance 
 you have received is a retainer fee, then create a Matter in the Client 
 Entity’s Billing File for the project or job that is being undertaken 
 for the client. The funds are then recorded as a Matter receipt.

In the following example, we will enter a retainer fee of EUR2,000.00 
 into the Accounting [AC] Matter for Capria Ltd.

	

1. In the Sales Ledger, select Accounts Receivable &gt; Settlements 
    	 &gt; Matters folder.

	

1. Choose the matter Accounting [AC] Matter.

	

1. Click Receipt.

	

1. Complete the Matter Receipt details and click Update.

![](../image27.jpg)

&nbsp;

The following is a sample of the Revenue Entity’s accounts for the cash 
 advance received:

![](../image37.png)

&nbsp;

<span class="hcp7">Note</span>: The 
 'Matter' account shown above is a notional account in Practice Management. 
 Each Matter has a notional account and all the notional accounts are summed 
 into one Nominal Account in Accounting. This Nominal Account is specified 
 in the Account Mapping for Practice Management.

![](../image6.jpg)

&nbsp;
### Settling Sales Invoices for the Same Matter
The sales invoices raised on a Matter can be settled using the cash 
 advance previously received for the same Matter. To allocate the cash 
 advance to sales invoices, settle the sales invoices to the Matter. In 
 the following example, we will settle a EUR300.00 sales invoice to the 
 Accounting [AC] Matter.

	

1. In the Sales Ledger, select Accounts Receivable &gt; Settlements 
    	 &gt; Invoice folder.

	

1. <span lang="EN-GB" xml:lang="EN-GB">Choose the sales invoice 
    	 you wish to settle.</span>

	

1. Click Settle to Matter.

	

1. Complete the Settlement details and click Update.

![](../image28.jpg)

&nbsp;

The following is a sample of the Revenue Entity’s accounts for the settlement 
 of the sales invoice:

![](../image40.png)

&nbsp;

<span class="hcp7">Note</span>: As 
 cash advances in the Matter account are used to settle the sales invoice, 
 there is no movement in the Revenue Entity’s Bank Account.

&nbsp;
### Settling Sales Invoices for a Different Matter
The sales invoices raised on a Matter can be settled using the cash 
 advance received for a different Matter. In the following example, we 
 will settle a EUR800.00 sales invoice on the Consultancy [CS] Matter to 
 the Accounting [AC] Matter.

	

1. In the Sales Ledger, select Accounts Receivable &gt; Settlements 
    	 &gt; Invoice folder.

	

1. Choose the sales invoice you wish to settle.

	

1. Click Settle to Matter.

	

1. Complete the Settlement details and click Update.

![](../image29.jpg)

&nbsp;

The following is a sample of the Revenue Entity’s accounts for the Sales 
 Invoice settlement:

![](../image42.png)

&nbsp;

<span style="font-weight: bold;">Note</span>:

	

- The cash advance (if any) in the Consultancy Matter account 
    	 will remain unaffected by this transaction.

	

- As cash advances in the Matter account are used to settle the 
    	 Sales Invoice, there is no movement in the Revenue Entity’s Bank Account.

&nbsp;
### Making Client Payments Using Client Monies
Client payments can be for client expenses such as repairs and maintenance 
 on a client’s fixed asset; or for Sales Invoices incurred by the client 
 for services provided by the Revenue Entity.

To make client payments using Client Monies, create a Matter Payment. 
 In the following example, we will pay EUR1,200.00 out of Client Monies.

	

1. In the Sales Ledger, select Accounts Receivable &gt; Settlements 
    	 &gt; Matters folder.

	

1. Choose Client Monies [CM] Matter.

	

1. Click Payment.

	

1. Complete the Matter Payment details and click Update.

![](../image30.jpg)

&nbsp;

The following is a sample of the Revenue Entity’s accounts for the client 
 payment transaction:

![](../image44.png)

&nbsp;

Note: <span style="font-weight: normal; font-style: normal;">If the client payment is for Sales Invoices incurred 
 by the client for services provided by the Revenue Entity, an Invoice 
 Receipt transaction would be recorded.</span>

&nbsp;
### Transferring Funds between Matters
A transfer of funds between Matters will need to be done if you had 
 originally recorded an advance as an Unidentified/Unallocated Receipt 
 while awaiting information on the purpose of the cash advance. Once you 
 find out the purpose of the advance, you should transfer the funds to 
 the appropriate Matter.

The original receipt of the funds could be to the Unidentified/Unallocated 
 Receipt Matter of either the Revenue Entity, OR, if you know which client 
 you received it from but not the purpose of the funds, you could temporarily 
 park it in the Unidentified/Unallocated Receipt Matter of the Client Entity’s 
 Billing File. This is done using Matter Receipt, which has been described 
 above.

&nbsp;

Important note:

As there is no movement in the Revenue Entity’s Bank Account when balances 
 are transferred between Matters, you need to create a notional Clearing/Suspense 
 Account, which will be used to transfer the balances.

&nbsp;

In the following example, we have recorded EUR4,000.00 as an Unidentified/Unallocated 
 Receipt in the Revenue Entity’s Billing File and will now transfer the 
 funds to the Consultancy [CS] Matter of Capria Ltd.

The first step is to perform a Matter Payment out of the Revenue Entity’s 
 Unidentified/ Unallocated Receipts [UR] Matter account:

	

1. Select the Revenue Entity’s Billing File.

	

1. In the Sales Ledger, select Accounts Receivable &gt; Settlements 
    	 &gt; Matters folder.

	

1. Choose the Unidentified/ Unallocated Receipts [UR] Matter.

	

1. Click Payment.

	

1. Complete the Matter Payment details and click Update.

![](../image31.jpg)

&nbsp;

Subsequently, allocate the funds to the Consultancy [CS] Matter for 
 Capria Ltd by performing a Matter Receipt.

	

1. Select Capria Ltd’s Billing File.

	

1. In the Sales Ledger, select Accounts Receivable &gt; Settlements 
    	 &gt; Matters folder.

	

1. Choose the Consultancy [CS] Matter.

	

1. Click Receipt.

	

1. Complete the Matter Receipt details and click Update.

![](../image32.jpg)

&nbsp;

&nbsp;

See also:

	

- [Matters](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Practice_Manager/Matters.htm)

&nbsp;

You are here:[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; [Additional Information](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Confidential_Database.htm) &gt; [Practice Management](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Client_Accountant/Approval_Cards_for_Payees_and_Payments.htm) &gt; Handling Cash Advances

&nbsp;

(c) Viewpoint Software for 
 Business Ltd

Version: 8.0.2022.09.20


