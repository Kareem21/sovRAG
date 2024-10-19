




# Unit Codes
This screen allows you to define Unit Codes that you can use for journal analyses. There is a total of ten Unit Codes and each comprises of the following:

- 
    
    <span class="hcp2">Unit Code</span> - This field is used to segregate journal entries, depending on the selection made from the [standard values](javascript:TextPopup(this)). The field then activates in the journal entry screen.
    
    <div class="droptext" id="POPUP311730801" style="display: none;">
        
    - 
        
        Not Used [0]
        
    - 
        
        Optional [1] - If you select this, the Table Code field (see below) becomes a mandatory field.
        
    - 
        
        Mandatory [2] - If you select this, the Table Code field (see below) becomes a mandatory field.
        
    - 
        
        B[ank] Sub Ledgers Only [3] - If you select this, the Table Code field (see below) becomes a mandatory field. If you select this option, the unit code field will be enabled for Bank Account sub-ledger journal lines.
        
    
    </div>

- 
    
    <span class="hcp2">Table Code</span> - This field activates depending on the selection made for the Unit Code field. Enter the user table where the available options will be taken from.

- 
    
    <span class="hcp2">Default Code</span> - Select a default code from the user table specified in the Table Code field, if required.


&nbsp;
### Unit Code 1
Unit Code 1 is used to specify the Organisational Unit when the Account File is the Revenue Entity. It is to be linked to the Organisational Units [ORGUNITS] user table. If the Account File is not for the Revenue Entity, you can use Unit Code 1 to record other information.

&nbsp;
### Unit Code 2
Unit Code 2 can be used to specify the user table for the Project code for supplier invoices and have the information flow through to the Revenue Entity's journals. Values for this field is to be set up using a User Table with the table code [PROJECTS]. However, if another table is specified for Unit Code 2 for a Revenue Entity of the purchase order, then the values will be retrieved from this table to populate all related accounting transactions. Note that the Revenue Entity must be an Account File and journals are posted from Practice Management to Accounting. Unit Code 2 is used for 'Expense Accounts-Supplier Invoices-R.PA' only.

&nbsp;
### Unit Code 3
The Unit Code 3 fields are used if you want to add a service line description to invoices posted from Practice Management. This feature uses the Service Line [SERVLINE] user table, and is only for the Revenue Entity. Account Files will use the Default Code (see below).

- 
    
    Invoice lines and WIP accrual entries will use the service line specified for the service code in the Service Master.

- 
    
    All other lines will use the Default Code.


Unit Code 3 is used for 'Income Accounts-Sales Invoices-R.SA' and 'Expense Accounts-Supplier Invoices-R.PA' only.

&nbsp;
### Unit Code 4
The Unit Code 4 fields are used if you want to select organisational code for a Billing File Matter or a Supplier File. This feature uses the Organisational Codes [ORGCODES] user table. In order to utilise this, you need to ensure that you do the following:

- 
    
    Enable the field in Billing File &gt; Matter screen or Supplier File &gt; General.

- 
    
    Set up the Organisational Codes [ORGCODES] user table.

- 
    
    Set Table Code for Unit Code 4 to [ORGCODES].


### &nbsp;
### Unit Code 5
The Unit Code 5 fields are used if you want to select intercompany code for a Billing File Matter or a Supplier File. This feature uses the Intercompany [INTERCO] user table. In order to utilise this, you need to ensure that you do the following:

- 
    
    Enable the field in Billing File or Supplier File Invoicing screen (File Maintenance &gt; Sales Ledger &gt; Invoicing &gt; Create/Edit Invoice &gt; Draft Line screen or File Maintenance &gt; Purchase Ledger &gt; Invoicing &gt; Create/Edit Purchase Orders &gt; Draft Line screen).

- 
    
    Set up the Intercompany [INTERCO] user table.

- 
    
    Set Table Code for Unit Code 5 to [INTERCO].


### &nbsp;
### Unit Code 6 - Unit Code 10
Unit Code 6 to 10 are used for CA Journal purpose only (for example in Invoice posting).

&nbsp;

&nbsp;

See also:

- 
    
    [Matters](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Practice_Manager/Matters.htm)

- 
    
    [Supplier File - General](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Practice_Manager/Supplier_File_-_General.htm)

- 
    
    [Create/Edit Purchase Orders](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Practice_Manager/Create_Edit_Purchase_Orders.htm)



&nbsp;

You are here:[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; [File Maintenance](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/File_Maintenance_screen.htm) &gt; [Accounting](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Client_Accountant/Accounting.htm) &gt; [Account File](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Client_Accountant/Account_File_-_Setup.htm) &gt; Unit Codes

&nbsp;

(c) Viewpoint Software for 
 Business Ltd

Version: 8.0.2022.09.20




