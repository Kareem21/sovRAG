



# Using Service Tax Codes
The Service Tax Codes screen allows for a service to have different 
 tax percentages for different revenue entities. To use this, you need 
 to ensure the following:

	

- Enable the option 'Use Accounting Tax Sub-ledger as Tax Codes' 
    	 in [System 
    	 Defaults &gt; Practice Management.](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/System_Defaults_-_Practice_Management.htm)

	

- Enable the [Service 
    	 Tax Codes](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Service_Tax_Codes.htm) screen.

	

- Enable the Tax Code field in Detail Lines for Sales Ledger (Create/Edit 
    	 Invoice) under Configuration &gt; Settings &gt; [Field 
    	 Settings](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Field_Settings.htm).

&nbsp;

Once the above is done, you can then map the tax codes in Service Tax 
 Codes screen.

&nbsp;
### Set up Tax Sub-ledgers
For the revenue entity, set up the relevant tax sub-ledgers.

	

1. Select the Account File of the revenue entity.

	

1. Go to Accounting &gt; Journals &gt; Tax Account.

	

1. Click New and enter details for the tax sub-ledger.

	

1. Click Update.

<span class="hcp2">Note</span>: If 
 you have Matters where tax is not applicable or is exempted, create a 
 tax sub-ledger with zero tax percentage for the options 'Not Applicable' 
 and 'Exempt'.

&nbsp;
### Mapping Tax Codes to Service

	

1. In Viewpoint - Home screen, go to Configuration &gt; Business 
    	 Parameters &gt; Practice Management &gt; Service Tax Codes.

	

1. Select the appropriate tax code.

	

1. Click Update.

	

1. Click Close

<span class="hcp2">Note</span>: Ensure 
 that you have a tax code for all the items listed including for Not Applicable 
 and Exempt.

&nbsp;

Once you have completed the mapping, when creating an invoice, you will 
 see the Tax Code and tax percentage. While Tax Code is not editable, you 
 can change the percentage if necessary.

![](../image202.jpg)

When the invoice is posted to Accounting, no entry will be posted to 
 the VAT control account. Instead, a journal is created for the tax account:

![](../image203.jpg)

&nbsp;

&nbsp;

You are here:[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; [Additional Information](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Confidential_Database.htm) &gt; [Practice Management](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Client_Accountant/Approval_Cards_for_Payees_and_Payments.htm) &gt; Using Service Tax Codes

&nbsp;

(c) Viewpoint Software for 
 Business Ltd

Version: 8.0.2022.09.20


