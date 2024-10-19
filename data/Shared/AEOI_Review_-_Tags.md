



# AEOI Review - Tags
Similar to tags for Compliance review, these tags are also to be entered in the relevant AEOI review rules.

&nbsp;
## FATCA/CRS Classification [CRSENTCLF/CRSENTCLS]
These two rules are similar in that they will create first the FATCA/CRS Classification record in the Classification and Indicia screen, if none exists. The rules apply to non-individual Master Files that are flagged for Entity Administration by default.

Tags are available to:

- 
    
    Specify the Master File to include in the review based on this review rule.

- 
    
    Specify values for the FATCA Classification record.

- 
    
    Specify values for creation of other records based on conditions for existing records.


<table class="Table1" cellspacing="0px" width="100%">
<colgroup><col style="width: 26.203%;">
<col style="width: 73.797%;">
</colgroup><tbody><tr class="t1st">
<td>
Purpose
</td>
<td>
Syntax
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
This defines the classification record to be created in the Classification and Indicia screen with the tags defining:

- 
    The code for the record.

- 
    The values for the fields of the record.

- 
    The message to be displayed as in the File Review result.


</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.IDREG.C.IdType:&lt;IdRegType&gt;]
[RVW.IDREG.&lt;Field&gt;=&lt;Value&gt;]
[RVW.IDREG.MSG=&lt;Message to display&gt;]
&nbsp;
where:

- 
    &lt;IdRegType&gt; refers to the code of the Identity Register type:

- 
        
    - 
        FCSC - for FATCA Classification
        
    - 
        FCSR - for CRS Classification
        
    

- 
    &lt;Field&gt; refers to the fields of the classification record and they are:

- 
        
    - 
        Description - Description field
        
    - 
        LookupValue - Reporting Status field
        
    - 
        FromDate - Date Classified field
        
    - 
        Active - Active checkbox
        
    

- 
    &lt;Value&gt; refers to the default values for the field.

- 
    &lt;Message to display&gt; is the message for the File Review result.


&nbsp;
Example:
[RVW.IDREG.C.IdType:FCSC]
[RVW.IDREG.Description=FATCA Classification]
[RVW.IDREG.LookupValue=C]
[RVW.IDREG.FromDate=#NOW]
[RVW.IDREG.Active=-1]
[RVW.IDREG.MSG=Create FATCA Classification &amp; Reporting Status record]
&nbsp;
The tags above will create the FCSC record if none exists for non-individual Master Files where the Reporting Status field defaults to 'Pre-Classification [C]' and the Date Classified defaults to today's date.
&nbsp;
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
This will restrict the rule according to the Master File flags and is an optional tag. Master File flags are options seen in the Master File Setup screen.
&nbsp;
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.CONTROL.MFFLAGS=&lt;Value&gt;]
&nbsp;
where &lt;Value&gt; can be:

- 
    CS - For Entity Administration option

- 
    RM - For Time &amp; Billing (Sales Ledger) option

- 
    TR - For Supplier (Purchase Ledger) option

- 
    CA - For Accounting option

- 
    CP - Identity Details/Register option

- 
    KY - CDD Required option

- 
    CL - Client/Group option

- 
    SH - Shareholder/UBO option

- 
    OC - Statutory/Trust Officer option

- 
    PR - Relation option

- 
    BA - Bank option

- 
    SI - Bank Signatory option

- 
    MfChk1 - For User Defined - 1

- 
    MfChk2 - For User Defined - 2

- 
    MfChk3 - For User Defined - 3

- 
    MfChk4 - For User Defined - 4

- 
    MfChk5 - For User Defined - 5


&nbsp;
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
This is to create a FATCA or CRS Reporting FI if a specified record type already exists. For example, create a FATCA Reporting FI if there is a FATCA Classification record where its Reporting Status = 'R' .
For the fields of the FATCA or CRS Reporting FI record, you can:

- 
    Specify default values.

- 
    Configure the values to be based on field from existing record.


&nbsp;
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.RFI.IDREGCODE=&lt;ConditionIdRegType&gt;]
[RVW.RFI.WITHFIELD=&lt;ConditionField&gt;]
[RVW.CONTROL.WithRFI=&lt;ConditionValue&gt;]
[RVW.RFI.IdType:&lt;IdRegType&gt;]
[RVW.RFI.MATCHFIELD=&lt;ExistingField&gt;]
[RVW.RFI.VALUE:&lt;ExistingValue&gt;=&lt;RFIValue&gt;]
[RVW.RFI.&lt;Field&gt;=&lt;Value&gt;]
[RVW.RFI.MSG=&lt;Message to display&gt;]
&nbsp;
where:

- 
    &lt;ConditionIdRegType&gt; is the code of the existing record that will create the FATCA or CRS Reporting FI record.

- 
    &lt;ConditionField&gt; is the field of the existing record that will create the FATCA or CRS Reporting FI record.

- 
    &lt;ConditionValue&gt; is the value for the &lt;ConditionField&gt;.

- 
    &lt;IdRegType&gt; is the code for the Reporting FI record:

- 
        
    - 
        FRFI - for FATCA Reporting FI
        
    - 
        CRFI - for CRS Reporting FI
        
    

- 
    &lt;ExistingField&gt; refers to the field of the existing record that will determine the value for the FATCA or CRS Reporting FI record.

- 
    &lt;ExistingValue&gt; refers to the value of the existing record.

- 
    &lt;RFIValue&gt; refers to the value for the &nbsp;FATCA or CRS Reporting FI record.

- 
    &lt;Field&gt; refers to the fields of the Reporting FI record and they are:

- 
        
    - 
        Description - Description field
        
    - 
        Country - Reporting Country field (FATCA Reporting FI), Country/Jurisfiction field (CRS Reporting FI)
        
    - 
        MasterFileLink - FATCA/CRS Reporting FI field
        
    - 
        UdCode - Reporting FI Category field (only for FATCA Reporting FI)
        
    

- 
    &lt;Value&gt; refers to the default values for the field.

- 
    &lt;Message to display&gt; is the message for the File Review result.


&nbsp;
Example:
[RVW.RFI.IDREGCODE=FCSC]
[RVW.RFI.WITHFIELD=LookupValue]
[RVW.RFI.MATCHFIELD=UdCode]
[RVW.RFI.VALUE:0001=FATCA602:0002=FATCA604:0019=FATCA601:0024=FATCA606]
[RVW.CONTROL.WithRFI=R]
[RVW.RFI.IdType:FRFI]
[RVW.RFI.Country=(-CNTR.FIC-)]
[RVW.RFI.Description=FATCA Reporting FI]
[RVW.RFI.MasterFileLink=(-FileCode-)]
[RVW.RFI.UdCode=(-RVW.RFI.Value-)]
[RVW.RFI.MSG=Click Post Updates to create FATCA Reporting FI record]
&nbsp;
The tags above will create a FATCA Reporting FI record:

- 
    If there is an existing FATCA Classification record where the Reporting Status = 'Reporting [R]'.

- 
    With the Reporting Country field for the FATCA Reporting FI defaulting to the &nbsp;value of the Country field from the Tax Residence and Identification No. (TIN) record.

- 
    With the Description field being defined as 'FATCA Reporting FI'.

- 
    With the FATCA Reporting FI field defaulting to the selected Master File code.

- 
    With the Reporting FI Category field defaulting to configuration of the [RVW.RFI.VALUE:] tag which will based it on the value of the FATCA Classification field for the FATCA Classification record.


&nbsp;
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
This is similar to the above except that it will create a FATCA Sponsoring Entity (FSPR) record if a specified record already exists.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.SPR.IDREGCODE=&lt;ConditionIdRegType&gt;]
[RVW.SPR.WITHFIELD=&lt;ConditionField&gt;]
[RVW.CONTROL.WithSPR=&lt;ConditionValue&gt;]
[RVW.SPR.IdType:&lt;IdRegType&gt;]
[RVW.SPR.MATCHFIELD=&lt;ExistingField&gt;]
[RVW.SPR.VALUE:&lt;ExistingValue&gt;=&lt;RFIValue&gt;]
[RVW.SPR.&lt;Field&gt;=&lt;Value&gt;]
[RVW.SPR.MSG=&lt;Message to display&gt;]
where

- 
    &lt;ConditionIdRegType&gt; is the code of the existing record that will create the FATCA Sponsoring Entity record.

- 
    &lt;ConditionField&gt; is the field of the existing record that will create the FATCA Sponsoring Entity record.

- 
    &lt;ConditionValue&gt; is the value for the &lt;ConditionField&gt;.

- 
    &lt;IdRegType&gt; is the code for the FATCA Sponsoring Entity record.

- 
    &lt;ExistingField&gt; refers to the field of the existing record that will determine the value for the FATCA Sponsoring Entity record.

- 
    &lt;ExistingValue&gt; refers to the value of the existing record.

- 
    &lt;RFIValue&gt; refers to the value for the &nbsp;FATCA Sponsoring Entity record.

- 
    &lt;Field&gt; refers to the fields of the FATCA Sponsoring Entity record and they are:

- 
        
    - 
        Description - Description field
        
    - 
        UdCode - Sponsoring Entity Category
        
    

- 
    &lt;Value&gt; refers to the default values for the field.

- 
    &lt;Message to display&gt; is the message for the File Review result.


Example:
[RVW.SPR.IDREGCODE=FCSC]
[RVW.SPR.WITHFIELD=UdCode]
[RVW.SPR.MATCHFIELD=UdCode]
[RVW.SPR.VALUE:0008=FATCA607:0013=FATCA607:0025=FATCA608:0026=FATCA609]
[RVW.CONTROL.WithSPR=0008,0013,0025,0026]
[RVW.SPR.IdType:FSPR]
[RVW.SPR.Description=FATCA Spnsoring Entity]
[RVW.SPR.UdCode=(-RVW.SPR.Value-)]
[RVW.SPR.MSG=Click Post Updates to create Sponsoring Entity record]
The tags above will create a Sponsoring Entity record:

- 
    If there is an existing FATCA Classification record where the FATCA Classification is 0008,0013,0025 or 0026.

- 
    With the Description field being defined as 'FATCA Reporting FI'.

- 
    With the Sponsoring Entity Category field defaulting to configuration of the [RVW.SPR.VALUE:] tag which will based it on the value of the FATCA Classification field for the FATCA Classification record.


</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
This will review the creation of CRS/FATCA Reporting FI for a Trust.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.RFI.CHECK=&lt;Value&gt;:&lt;IdType&gt;]
where:

- 
    &lt;Value&gt; is either Y or N. Y refers to Yes and N refers to No.

- 
    &lt;IdType&gt; is the Identity Register Type. This is not required if &nbsp;&lt;Value&gt; is N.


Example:
[RVW.RFI.CHECK=Y:FIC]
[RVW.RFI.CHECK=Y:FIC,GIIN]
[RVW.RFI.CHECK=N]
&nbsp;
When &lt;Value&gt; is Y, the system will loop through the list of active officers of the entity's Trust in the following order:

1. 
    Non-individual Officer that with earlier Appointment Date.

1. 
    Non-individual Officer that with later Appointment Date.

1. 
    Individual Officer that with earlier Appointment Date.

1. 
    Individual Officer that with later Appointment Date.


When &lt;Value&gt; is Y, for example [RVW.RFI.CHECK=Y:FIC,GIIN], it will review the creation of CRS/FATCA Reporting FI in the following order:

- 
    Check if there is any officer type as stated in [RVW.CONTROL.TRUST=&lt;OfficerType&gt;].

- 
        
    - 
        If yes, it will check the list of active officers whether any officer has Identity Register Type 'FIC' or ‘GIIN’ as stated.
        
    - 
            
        - 
            If yes, the system will prompt to create RFI.
            
        - 
            If there is no officer under the Trust / no officer has either the Identity Register 'FIC' OR 'GIIN', then it will check the Trust whether it has the Identity Register stated in [RVW.RFI.Country=(-CNTR.FIC-)].
            
        - 
                
            - 
                If the Trust itself has the Identity Register and it is 'Parent Relations' of another files (for example: the Trust is Beneficial Owner of another file) then prompt to create RFI.
                
            - 
                Otherwise, it will not prompt to create RFI.
                
            
            
        
        
    


When &lt;Value&gt; is N, the system will refer to the first active officer (earliest appointed officer that is still active) for the Trust.
For example if the tag [RVW.RFI.CHECK=N] is used, it will review the creation of CRS/FATCA Reporting FI in the following order:

- 
    Check if there is any officer type stated in [RVW.CONTROL.TRUST=&lt;OfficerType&gt;].

- 
        
    - 
        If yes, the system will check the first active officer whether the officer has Identity Register Type stated in [RVW.RFI.Country=(-CNTR.FIC-)].
        
    - 
            
        - 
            If there is officer with the Identity Register, it will prompt to create RFI.
            
        
        
    - 
        If there is no officer under the Trust or there is no officer with Identity Register, it will proceed to check the Trust itself whether it has the Identity Register.
        
    - 
            
        - 
            If the Trust has the Identity Register and it is 'Parent Relations' of another files (for example: the Trust is Beneficial Owner of another file) then prompt to create RFI.
            
        - 
            Otherwise, it will not prompt to create RFI.
            
        
        
    


</td>
</tr>
</tbody></table>

&nbsp;

Sample Tag Configuration - CRSENTCLF

[RVW.IDREG.C.IdType:FCSC] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

[RVW.IDREG.Description=FATCA Classification &amp; Reporting Status]

[RVW.IDREG.LookupValue=C] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

[RVW.IDREG.FromDate=#NOW] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

[RVW.IDREG.Active=-1] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

[RVW.IDREG.MSG=Create FATCA Classification &amp; Reporting Status record under Classification and Indicia]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

This tag will create and populate the FRFI record based on the Reporting Status and Classification assigned in the FCSC record

[RVW.RFI.IDREGCODE=FCSC]

[RVW.RFI.WITHFIELD=LookupValue]

[RVW.CONTROL.WithRFI=R]

[RVW.RFI.MATCHFIELD=UdCode]

[RVW.RFI.VALUE:0001=FATCA602:0002=FATCA604:0019=FATCA601:0024=FATCA606:0003=:0004=:0005=:0006=:0007=:0008=:0009=:0010=:0011=:0012=:0013=:0014=:0015=:0016=:0017=:0018=:0020=:0021=:0022=:0023=:0025=:0026=]

[RVW.CONTROL.WithRFI=R]

[RVW.RFI.IdType:FRFI] &nbsp;&nbsp;&nbsp;

[RVW.RFI.Country=(-CNTR.FIC-)]

[RVW.RFI.Description=FATCA Reporting FI] &nbsp;&nbsp;&nbsp;

[RVW.RFI.MasterFileLink=(-FileCode-)]

[RVW.RFI.UdCode=(-RVW.RFI.Value-)] &nbsp;

[RVW.RFI.MSG=Create FATCA Reporting FI record]

&nbsp;

This tag will create the Sponsoring Entity record and assign the Sponsor Category based on the Reporting Status and Classification assigned in the FCSC record

[RVW.SPR.IDREGCODE=FCSC]

[RVW.SPR.WITHFIELD=UdCode]

[RVW.SPR.MATCHFIELD=UdCode]

[RVW.SPR.VALUE:0008=FATCA607:0013=FATCA607:0025=FATCA608:0026=FATCA609] Matches the FCSC classification to the relevant sponsor category

[RVW.CONTROL.WithSPR= 0008,0013,0025,0026] &nbsp;&nbsp;Lists the FCSC classifications to prompt the creation of a sponsoring entity record

[RVW.SPR.IdType:FSPR] &nbsp;&nbsp;&nbsp;

[RVW.SPR.Description=FATCA Sponsoring Entity] &nbsp;

[RVW.SPR.UdCode=(-RVW.SPR.Value-)] &nbsp;

[RVW.SPR.MSG= Click 'Post Update' to create the Sponsoring Entity record]

&nbsp;

&nbsp;

<span class="hcp5">Sample Tag Configuration - CRSENTCLS</span>

[RVW.IDREG.C.IdType:FCRS]

[RVW.IDREG.Description= CRS Classification and Reporting Status]

[RVW.IDREG.LookupValue=C]

[RVW.IDREG.FromDate=#NOW]

[RVW.IDREG.Active=-1]

[RVW.IDREG.MSG=Create CRS Classification record under Classification and Indicia]

&nbsp;

[RVW.CONTROL.WithRFI=R]

[RVW.RFI.IdType:CRFI]

[RVW.RFI.Description=CRS Reporting FI]

[RVW.RFI.Country=(-CNTR.FIC-)]

[RVW.RFI.MasterFileLink=(-FileCode-)]

[RVW.RFI.MSG=Create CRS Reporting Financial Institution record]

&nbsp;

&nbsp;
## Indicia and Curing Review [CRSREVIEW]
This rule will check on relevant relations for the selected Master File and where applicable, create an indicia record. Tags are available for you to:

- 
    
    Specify parameters for the relations.

- 
    
    Set reminder dates for the mediation.

- 
    
    Specify conditions for Master Files to be included in the review.

- 
    
    Specify the values of the indicia records.


<table class="Table1" cellspacing="0px" width="100%">
<colgroup><col style="width: 24.086%;">
<col style="width: 75.914%;">
</colgroup><tbody><tr class="t1st">
<td>
Purpose
</td>
<td>
Syntax
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
Specify the reporting period. Only relevant relations that are active within this defined period will be included.
&nbsp;
&nbsp;
&nbsp;
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.DateStart=&lt;Date&gt;]
[RVW.DateEnd=&lt;Date&gt;]
&nbsp;
where &lt;Date&gt; must be in yyyyMMdd format.
&nbsp;
Example:
[RVW.DateStart=20160101]
[RVW.DateEnd=20161231]
&nbsp;
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
Specify reminder date for the curing.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.IDREG.ReminderDate=(-DATECALC-)]
[RVW.DateCalc=&lt;Value&gt;]
&nbsp;
where &lt;Value&gt; is #NOW+&lt;Number of days&gt; e.g. #NOW+90 means 90 days after the creation of the indicia record.
&nbsp;
If different reminder dates are required for different jurisdictions, then a reminder date can be set per jurisdiction by including the country code. This will take precedence over the one without country code.
[RVW.DateCalc.&lt;CountryCode&gt;=&lt;Value&gt;]
&nbsp;
where &lt;CountryCode&gt; is the 2-character ISO country code e.g. US for United States of America.
&nbsp;
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
Specify the Master File options to include in the review. This tag is optional and if not specified, then will include files where the Entity Administration option is ticked.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.CONTROL.MFFLAGS=&lt;Value&gt;]
&nbsp;
where &lt;Value&gt; can be:

- 
    CS - For Entity Administration option

- 
    RM - For Time &amp; Billing (Sales Ledger) option

- 
    TR - For Supplier (Purchase Ledger) option

- 
    CA - For Accounting option

- 
    CP - Identity Details/Register option

- 
    KY - CDD Required option

- 
    CL - Client/Group option

- 
    SH - Shareholder/UBO option

- 
    OC - Statutory/Trust Officer option

- 
    PR - Relation option

- 
    BA - Bank option

- 
    SI - Bank Signatory option

- 
    MfChk1 - For User Defined - 1

- 
    MfChk2 - For User Defined - 2

- 
    MfChk3 - For User Defined - 3

- 
    MfChk4 - For User Defined - 4

- 
    MfChk5 - For User Defined - 5


&nbsp;
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
This will populate the Reporting Country for the CRFI or FRFI record using the Tax Residence (Country field for the FIC record) of the defined relationship type when the Reporting FI (RFI) is a trust.
If there is more than one instance of the relationship type, then the details of the first identified one is used. Where a Trust is a relevant relation on another RFI, then an INDC record will be created. Otherwise, no INDC record.
This tag is optional.
&nbsp;
&nbsp;
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.CONTROL.TRUST=&lt;RelType&gt;]
&nbsp;
where &lt;RelType&gt; refers to the code of the relationship type. For multiple relationship types, separate with a comma. If the first relationship type is not available, then it will take the second one.
&nbsp;
Example:
[RVW.CONTROL.TRUST=TRU]
The above will look for Tax Residence from the FIC record of the TRU relationship type.
&nbsp;
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
Specify the relevant relations to be included e.g. settlor, foundation council member.
&nbsp;
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.CONTROL.RTYPE=&lt;RelType&gt;]
&nbsp;
where &lt;RelType&gt; refers to the code of the relationship type. For multiple relationship types, separate with a comma. The relationship types can be from any Relation class i.e. Master File relations [M], Entity Relations [E], Statutory Officers [O] and Trust Officers [T].
&nbsp;
Example:
[RVW.CONTROL.RTYPE=TRU,ADM,FDR,FCM]
The above includes the relationship types TRU (trustee), ADM (settlor), FDR (founder) and FCM (foundation council member) as relevant relations.
&nbsp;
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
Specify the substantial owner and controlling person to be included.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.CONTROL.CPTYPE=&lt;RelType&gt;]
&nbsp;
Example:
[RVW.CONTROL.CPTYPE=SOW,CNP]
&nbsp;
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
Specify conditions for inclusion or exclusion of trust beneficiaries. This is optional. If not defined, then all trust beneficiaries where the Date Ceased is empty or greater than the Start Date will be included.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.CONTROL.BENEF.EXCL=&lt;Type&gt;]
&nbsp;
where &lt;Type&gt; is the code of the Beneficiary type that you want to exclude.
&nbsp;
[RVW.CONTROL.BENST.INCL=&lt;Status&gt;]
&nbsp;
where &lt;Status&gt; is the code of the Beneficiary Status you want to include.
&nbsp;
Exanple:
[RVW.CONTROL.BENEF.EXCL=X]
[RVW.CONTROL.BENST.INCL=A]
&nbsp;
The above tags will exclude beneficiary type 'X' and include all other types where the status is set to 'A'.
&nbsp;
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
Specify interest types to include.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.CONTROL.OWNINT=&lt;Type&gt;]
&nbsp;
where &lt;Type&gt; refers to the code of the interest type.
&nbsp;
Example:
[RVW.CONTROL.OWNINT=BEO]
The above will include Interest Type 'BEO'.
&nbsp;
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
Specify option for shareholders/partners to include.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.CONTROL.OWNSHARE=&lt;Option&gt;]
&nbsp;
where &lt;Option&gt; can be:

- 
    B - Beneficial owner (if linked), otherwise, the registered shareholder/partner. This is the default.

- 
    A - Both registered shareholder/partner and beneficial owner (if linked).

- 
    R - Registered shareholder/partner only.


</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
Specify share classes to be excluded e.g. partners.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.CONTROL.CLASSEXCL=&lt;Code&gt;]
&nbsp;
where &lt;Code&gt; is the first two characters of the class code e.g. /G for /G01, OR for OR01.
&nbsp;
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
Specify Sub-ledger types to include. File Review will look for Sub-ledger Master File with the specified sub-ledger type.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.CONTROL.SLTYPE=&lt;Code&gt;]
&nbsp;
where &lt;Code&gt; refers to the code of the sub-ledger type and can be obtained from the Sub-ledger Type Values [SLTP] lookup table.
&nbsp;
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
Specify Distribution types to include. File Review will retrieve the Related Party Master File with the specified distribution type.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.CONTROL.DSTYPE=&lt;Code&gt;]
&nbsp;
where &lt;Code&gt; refers to the code of the distribution type and can be obtained from the Distribution Types [DIST] lookup table.
&nbsp;
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
Specify status of the relevant relations to include. This is an optional tag and if not defined, all status will be included in the review..
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.CONTROL.REFSTATUS=&lt;Status&gt;]
&nbsp;
where &lt;Status&gt; is the Master File status.
&nbsp;
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
Specify Entity File status to include. This is an optional tag and if not defined, all status will be included in the review.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.CONTROL.ENTSTATUS=&lt;Status&gt;]
&nbsp;
where &lt;Status&gt; is the Entity File status.
&nbsp;
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
Specify which relevant relations (of non-individual Master File type) to exclude based on the status of the CRS and FATCA Classification record. This is an optional tag. If not defined, then all relevant relations will be included.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.CONTROL.ENTCLASS.IdType=&lt;IdRegType&gt;]
[RVW.CONTROL.ENTCLASS.NFI.LookValue=&lt;Code&gt;]
&nbsp;
where

- 
    &lt;IdRegType&gt; refers to the code for CRS and FATCA Classification record.

- 
    &lt;Code&gt; refers to the status code for CRS and FATCA Classification.


&nbsp;
Example:
[RVW.CONTROL.ENTCLASS.IdType=FCSC, FCRS]
[RVW.CONTROL.ENTCLASS.NFI.LookValue:Q,N,C]
The above will look at FCSC and FCRS records for relevant relations and if the status is set to Q, N or C, these will not be included in the review.
&nbsp;
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
Specify address types to exclude.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.Address.Exclude:&lt;Code&gt;]
&nbsp;
where &lt;Code&gt; refers to the address type code.
&nbsp;
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
Specify the Identity Register types to include.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.IdReg.Type:&lt;IdRegType&gt;]
&nbsp;
where &lt;IdRegType&gt; is the code of the Identity Register type.
&nbsp;
Example:
[RVW.IdReg.Type:PSP,BCT,INC,IDC,CTZ]
The above tag includes Identity Register types 'PSP, 'BCT', 'INC', 'IDC' and 'CTZ'.
&nbsp;
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
Specify the contact types to include.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.Contact.Type:&lt;Code&gt;]
&nbsp;
where &lt;Code&gt; refers to the code of the Contact Type and can be obtained from Contact Types [ADRC] lookup table.
&nbsp;
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
Specify the countries to include. This tag is optional and cannot be used with the [RVW.CNTR.EXCL=] tag.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.CNTR.INCL=&lt;Code&gt;]
&nbsp;
where &lt;Code&gt; refers to country code.
&nbsp;
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
Specify the countries to exclude countried that are not reciprocal. This tag is optional and cannot be used with the [RVW.CNTR.INCL=] tag.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.CNTR.EXCL=&lt;Code&gt;]
&nbsp;
where &lt;Code&gt; refers to country code.
&nbsp;
Example:
[RVW.CNTR.EXCL=BM,KY,MS,TC]
The above excludes Bermuda, Cayman Islands, Montserrat and Turks and Caicos Islands.
&nbsp;
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
This is to create the Indicia and Curing Status record in Classification and Indicia screen and defines values for the record fields.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.IDREG.I.IdType:&lt;IdRegType&gt;]
[RVW.IDREG.C.IdType:&lt;IdRegType&gt;]
[RVW.IDREG.&lt;Field&gt;=&lt;Value&gt;]
&nbsp;
where

- 
    &lt;IdRegType&gt; refers to the code of the Identity Register type.

- 
    &lt;Field&gt; refers to the fields of the record and they are:

- 
        
    - 
        Description - Description field
        
    - 
        Country - Country/Jurisdiction field
        
    - 
        LookupValue - Indicia Status field
        
    - 
        Note - Note field
        
    - 
        Active - Active checkbox
        
    

- 
    &lt;Value&gt; refers to the default values for the field.


&nbsp;
Example:
[RVW.IDREG.I.IdType:INDI]
[RVW.IDREG.C.IdType:INDC]
[RVW.IDREG.Description=Indicia and Curing Status]
[RVW.IDREG.Country=(-CNTR-)]
[RVW.IDREG.LookupValue=C]
[RVW.IDREG.Note=(-MSG-)]
[RVW.IDREG.Active=-1]
&nbsp;
The above tags will:

- 
    Create an INDI record if the selected Master File is an Individual Master File type.

- 
    Create an INDC record if the selected Master File is a non-individual Master File type.

- 
    With the Description as 'Indicia and Curing Status'.

- 
    With Country/Jurisdiction being the country of the information.

- 
    With the From Date being the effective date of the information.


&nbsp;
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
Set From Date as blank. This is an optional tag which can be added if you do not require any date in the From Date field.
&nbsp;
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.IDREG.NOFROMDATEVALUE=Y]
</td>
</tr>
</tbody></table>

&nbsp;

Example

<span class="hcp5">[</span>RVW.DateStart=20160101]

[RVW.DateEnd=20161231]

[RVW.IDREG.ReminderDate=(-DATECALC-)]

[RVW.DateCalc=#NOW+90]

[RVW.DateCalc.SG=#NOW+60]

&nbsp;

[RVW.CONTROL.TRUST=TRU]

[RVW.CONTROL.RTYPE=TRU,ADM,FDR,FCM]

[RVW.CONTROL.CPTYPE=SOW,CNP]

[RVW.CONTROL.BENEF.EXCL=X]

[RVW.CONTROL.BENST.INCL=A]

[RVW.CONTROL.OWNINT=BEO,UBO,UOW,UHC]

[RVW.CONTROL.OWNSHARE=B]

[RVW.CONTROL.CLASSEXCL=]

[RVW.CONTROL.SLTYPE=BMGD,BOTH,COTH,DOTH]

[RVW.CONTROL.DSTYPE=B,C,D,E,F,I]

[RVW.CONTROL.REFSTATUS=0,1,3]

[RVW.CONTROL.ENTSTATUS=0,3]

[RVW.CONTROL.ENTCLASS.IdType=FCSC, FCRS]

[RVW.CONTROL.ENTCLASS.NFI.LookValue:N]

[RVW.IdReg.Type:PSP,BCT,INC,IDC,CTZ]

[RVW.Contact.Type:T,F]

[RVW.CNTR.INCL=]

[RVW.CNTR.EXCL=]

&nbsp;

[RVW.IDREG.I.IdType:INDI]

[RVW.IDREG.C.IdType:INDC]

[RVW.IDREG.Description= Indicia and Curing Status]

[RVW.IDREG.Country=(-CNTR-)]

[RVW.IDREG.LookupValue=C]

[RVW.IDREG.Note=(-MSG-)]

[RVW.IDREG.Active=-1]

&nbsp;

&nbsp;
## Indicia and Curing Status – Expiration of Curing Deadline [CRSINDUPD]
This rule will update the status for the indicia record where the curing deadline for receipt of the Self-Certification/Consent has expired. Once posted, the Reminder Date will be cleared. Tags are used to specify the status.

<table class="Table1" cellspacing="0px" width="100%">
<colgroup><col style="width: 20.943%;">
<col style="width: 79.057%;">
</colgroup><tbody><tr class="t1st">
<td>
Purpose
</td>
<td>
Syntax
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
This will update the Indicia Status field for the Indicia and Curing Status record where the curing deadline (Reminder Date) has expired.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.IDREG.TYPE=&lt;IdRegType&gt;]
[RVW.IDREG.LookupValue=&lt;Status&gt;]
&nbsp;
where:

- 
    &lt;IdRegType&gt; refers to the code of the Indicia and Curing Status record.

- 
    &lt;Status&gt; refers to the code for the Indicia Status.


&nbsp;
Example:
[RVW.IDREG.IdType=INDC,INDI]
[RVW.IDREG.LookupValue=Q]
&nbsp;
The above will update the Indicia Status for INDC and INDI records to 'Uncured - Non-Consenting [Q]'.
&nbsp;
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
Specify the message to show in File Review.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.IDREG.MSG=&lt;Message to display&gt;]
&nbsp;
where &lt;Message to display&gt; can be text or codes such as:

- 
    (-CODE-) which will be replaced with the actual Identity Register type code.

- 
    (-CNTR-) which will be replaced with the actual country information.


&nbsp;
</td>
</tr>
</tbody></table>

&nbsp;

<span class="hcp5">Example</span>:

[RVW.IDREG.IdType=INDC,INDI]

[RVW.IDREG.LookupValue=Q]

[RVW.IDREG.MSG=(-CODE-) - (-CNTR-): Update Indicia and Curing Status to 'Uncured - Non-Consenting)']

&nbsp;

&nbsp;
## Create Global Intermediary Identification and Indicia [CRSGIIN]
This will create a GIIN record if applicable. Tags are available to specify what to check and define information for the record.

<table class="Table1" cellspacing="0px" width="100%">
<colgroup><col style="width: 21.071%;">
<col style="width: 78.929%;">
</colgroup><tbody><tr class="t1st">
<td>
Purpose
</td>
<td>
Syntax
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
This will create a GIIN record based on the status for the specified existing record.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.GIN.IDREGCODE=&lt;ExistIdRegType&gt;]
[RVW.GIN.WITHFIELD=&lt;ExistField&gt;]
[RVW.CONTROL.WithGIN=&lt;Code&gt;]
[RVW.GIN.IdType:&lt;IdRegType&gt;]
[RVW.IDREG.&lt;Field&gt;=&lt;Value&gt;]
&nbsp;
where

- 
    &lt;ExistIdRegType&gt; refers to the code of existing record.

- 
    &lt;ExistField&gt; refers to the field of the existing record to be reviewed.

- 
    &lt;Code&gt; refers to the value for &lt;ExistField&gt; that will create the GIIN record.

- 
    &lt;IdRegType&gt; refers to the code for the GIIN record.

- 
    &lt;Field&gt; refers to the fields of the GIIN record and they are:

- 
        
    - 
        Description - Description field
        
    - 
        Note - Note field
        
    

- 
    &lt;Value&gt; refers to the default values for the field.


&nbsp;
Example:
[RVW.GIN.IDREGCODE=FCSC]
[RVW.GIN.WITHFIELD=UdCode]
[RVW.CONTROL.WithGIN= 0001,0002,0008,0019]
[RVW.GIN.IdType:GIIN]
[RVW.GIN.Description= Global Intermediary Identification Number]
&nbsp;
The above will create a GIIN record if there is an existing FCSC record where the FATCA Classification field is set to 0001, 0002, 0008 or 0019
&nbsp;
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
Specify the message to show in File Review.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.GIN.MSG=&lt;Message to display&gt;]
&nbsp;
where &lt;Message to display&gt; can be text.
&nbsp;
</td>
</tr>
</tbody></table>

&nbsp;

<span class="hcp5">Example</span>:

[RVW.GIN.IDREGCODE=FCSC]

[RVW.GIN.WITHFIELD=UdCode]

[RVW.CONTROL.WithGIN= 0001,0002,0008,0019]

[RVW.GIN.IdType:GIIN]

[RVW.GIN.Description= Global Intermediary Identification Number]

[RVW.GIN.MSG=Create GIIN Record]

[RVW.GIN.Note= A GIIN is required if the FATCA classification is Deemed Compliant – Sponsored Investment Entity and the FRFI reporting country is on one of these jurisdictions - Bermuda, Denmark, France, Germany, Spain, Hong Kong, Switzerland or United Kingdom]

&nbsp;

&nbsp;
## Tax Residence and TIN [CRSINDTXRD]
This will create a Tax Residence and TIN record if applicable for reportable Master Files with an indicia record. Tags are available to specify what to check and define the information for the record.

<table class="Table1" cellspacing="0px" width="100%">
<colgroup><col style="width: 21.392%;">
<col style="width: 78.608%;">
</colgroup><tbody><tr class="t1st">
<td>
Purpose
</td>
<td>
Syntax
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
This will create a Tax Residence and Identification No. (TIN) record based on the status for the specified existing record.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.IDREG.Type:&lt;ExistIdRegType&gt;]
[RVW.IDREG.Status:&lt;ExistStatus&gt;]
[RVW.IDREG.I.IdType:&lt;IdRegType&gt;]
[RVW.IDREG.C.IdType:&lt;IdRegType&gt;]
[RVW.IDREG.&lt;Field&gt;=&lt;Value&gt;]
&nbsp;
where

- 
    &lt;ExistIdRegType&gt; refers to the code of existing record.

- 
    &lt;ExistStatus&gt; refers to the status of the existing record.

- 
    &lt;IdRegType&gt; refers to the code for the Tax Residence and Identification No. (TIN) record.

- 
    &lt;Field&gt; refers to the fields of the Tax Residence and Identification No. (TIN) &nbsp;record and they are:

- 
        
    - 
        Description - Description field
        
    - 
        Country - Tax Residence/Issuing TIN Country field
        
    

- 
    &lt;Value&gt; refers to the default values for the field.


&nbsp;
Example:
[RVW.IDREG.Type:INDC,INDI]
[RVW.IDREG.Status:R,Q]
[RVW.IDREG.I.IdType:FIN]
[RVW.IDREG.C.IdType:FIC]
[RVW.IDREG.Description=Tax Residence and Identification No (TIN)]
[RVW.IDREG.Country=(-CNTR-)]
&nbsp;
The above will:

- 
    create a 'FIC' - Tax Residence and Identification No (TIN) &nbsp;record if the existing INDC record has a status of R or Q.

- 
    create a 'FIN' - Tax Residence and Identification No (TIN) &nbsp;record if the existing INDI record has a status of R or Q.


&nbsp;
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
Specify the message to show in File Review.
</td>
<td class="t2Col" style="vertical-align: top;">
[RVW.IDREG.MSG=&lt;Message to display&gt;]
where &lt;Message to display&gt; can be text or codes such as (-CNTR-) which will be replaced with the actual country information
</td>
</tr>
</tbody></table>

&nbsp;

Example:

[RVW.IDREG.Type:INDC,INDI]

[RVW.IDREG.Status:R,Q]

[RVW.IDREG.I.IdType:FIN]

[RVW.IDREG.C.IdType:FIC]

[RVW.IDREG.Description=Tax Residence and Identification No (TIN)]

[RVW.IDREG.Country=(-CNTR-)]

[RVW.IDREG.MSG=Create Tax Residence and TIN record for country: (-CNTR-)]

&nbsp;
## Reportable Account [CRSREPACC2]
This will create Reportable Account records for the specified reporting authority if the record does not yet exist.

<table class="Table1" cellspacing="0px" width="99.153%">
<colgroup><col style="width: 44.111%;">
<col style="width: 55.889%;">
</colgroup><tbody><tr class="t1st">
<td>
Purpose
</td>
<td>
Syntax
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
This Review will create the Reportable Account record where it does not exist&nbsp;for the specified Reporting Authority.
</td>
<td class="t2Col" style="vertical-align: top;">
[REGIMES=&lt;Value&gt;]
&nbsp;
where &lt;Value&gt; can be:

- 
    C for CRS

- 
    F for FATCA

- 
    G for UK FATCA


&nbsp;
Example:
[REGIMES=C,F]
The above specifies two reporting regimes.
&nbsp;
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
Defines the AEOI Classification and Status register entries to be queried to ascertain the reporting status of the Managed Entity.
</td>
<td class="t2Col" style="vertical-align: top;">
[&lt;ReportingRegime&gt;.IDREG=&lt;IdType&gt;]
&nbsp;
where

- 
    &lt;ReportingRegime&gt; can be C, F or G.

- 
    &lt;IdType&gt; is the code of the Identity Register type.


&nbsp;
Example:
[C.REPORTING.IDREG=FCRS]
The above indicates that the checking for the CRS Reporting Regime will be on the classification and status for the Identity Register type 'FCRS'.
&nbsp;
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
Defines the RFI Reporting Status. If selected file with Identity Register Type FCRS or FCSC has lookup value of 'R' then, it is considered reporting.
</td>
<td class="t2Col" style="vertical-align: top;">
[&lt;ReportingRegime&gt;.LVALUE=&lt;LookValueCode&gt;]
&nbsp;
where

- 
    &lt;ReportingRegime&gt; can be C, F or G.

- 
    &lt;LookValueCode&gt; is the code of the RFI Reporting Status.


&nbsp;
Example:
[C.REPORTING.LVALUE=R]
The above will only create the Reportable Account record for CRS Reporting Regime if the reporting status for the Identity Register type 'FCRS' is set to 'R'.
&nbsp;
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
Defines the Relevant Reporting status to exclude i.e. if reporting as an RFI in its own right, no Account Holder record will be created.
</td>
<td class="t2Col" style="vertical-align: top;">
[&lt;ReportingRegime&gt;.UVALUE=&lt;UserTableCode,&lt;UserTableCode&gt;]
&nbsp;
where

- 
    &lt;ReportingRegime&gt; can be C, F or G.

- 
    &lt;UserTableCode&gt; is the code of the classification for FATCA or CRS.


&nbsp;
Example:
[C.REPORTING.UVALUE=CR01,CR04+CPTYPE,CR05+CPTYPE]
The above will exclude those where:

- 
    The CRS Classification = CR01 (Reporting FI) from having a reportable account record created.

- 
    The CRS Classification = CR04 (Non-Participating Jurisdiction FI) and heir associated controlling person from having a reportable account record created.

- 
    The CRS Classification = CR05 (Passive NFE) and their associated controlling person from having a reportable account record created.


</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
Defines the AEOI Classification and Status register record(s) to be used to identify/retrieve the country(ies) of tax residence.
No Account Holder record will be created where the Tax Residence of the Relevant Relation is the same as the Reporting Country; or if the Tax Residence country does not appear in the AEOI.MATRIX
&nbsp;
</td>
<td class="t2Col" style="vertical-align: top;">
[TAXRES=&lt;IdRegType&gt;]
&nbsp;
where &lt;IdRegType&gt; is the code of the Identity Register type where the tax residence information will be retrieved from.
&nbsp;
Example:
[TAXRES=FIC,FIN]
The above will take the tax residence information from Identity Register types 'FIC' or 'FIN' for the specified reporting regime(s) using the [REGIMES=] tag.
&nbsp;
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
To check whether the dates are in the reporting period defined by the tags [RVW.DateStart=] and [RVW.DateEnd=] in Indicia and Curing Review (CRSREVIEW). If the dates are in the reporting period, then it is reportable.
</td>
<td class="t2Col" style="vertical-align: top;">
[TAXRES.CHECKDATE=&lt;Value&gt;]
&nbsp;
where &lt;Value&gt; is either N for No or Y for Yes. If tag is not defined, then the default is No. If the value is Y but the From/To dates are empty, then the account is reportable as well.
&nbsp;
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
Defines the AEOI Classification and Status register record to retrieve the Reporting Country from.
</td>
<td class="t2Col" style="vertical-align: top;">
[&lt;ReportingRegime&gt;.REPCNTR=&lt;IdRegType&gt;]
&nbsp;
where

- 
    &lt;ReportingRegime&gt; can be C, F or G.

- 
    &lt;IdRegType&gt; is the code of the Identity Register type where the reporting country information will be retrieved from.


&nbsp;
Example:
[C.REPCNTR=CRFI]
The above will take the classification and status from the Identity Register type 'CRFI' for the CRS Reporting Regime.
&nbsp;
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
Defines the relationship types to be used to identify the controlling person and substantial owner.
</td>
<td class="t2Col" style="vertical-align: top;">
[&lt;ReportingRegime&gt;.CPTYPE=&lt;RelCode&gt;]
&nbsp;
where

- 
    &lt;ReportingRegime&gt; can be C, F or G.

- 
    &lt;RelCode&gt; is the code of the relationship type to be considered as controlling person and substantial owner.


&nbsp;
Example:
[C.CPTYPE=CNP]
The above will consider Master Files entered as Relationship Type 'CNP' as Controlling Persons.
&nbsp;
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
Defines the list of countries of exchange for the Reporting Country from specified UserTable.
</td>
<td class="t2Col" style="vertical-align: top;">
[CODEREF:AEOI.MATRIX]
&nbsp;
<span style="font-weight: bold; font-style: italic;">Note</span>: AEOI is the code of the User Table and MATRIX is the code of the value in the User Table.
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
Defines the value for the Reportable Account record with the record.
&nbsp;
</td>
<td class="t2Col" style="vertical-align: top;">
[&lt;ReportingRegime&gt;.RACCT:
&lt;Field&gt;=&lt;Value&gt;
&lt;Field&gt;=&lt;Value&gt;
...
]
&nbsp;
where

- 
    &lt;ReportingRegime&gt; can be C, F or G.

- 
    &lt;Field&gt; refers to the fields for the Reportable Account record and they are:

- 
        
    - 
        FileCode - The selected Master File
        
    - 
        RepAuthority - Reporting Authority field
        
    - 
        AcctCode - Account Code field
        
    - 
        AcctName - Account Name field
        
    - 
        AcctHolder - Account Holder field
        
    - 
        AcctHolderType - Account Holder Type field
        
    - 
        AcctNote - Note field
        
    - 
        AcctStatus - Status field
        
    

- 
    &lt;Value&gt; refers to values for the fields which can include these codes:

- 
        
    - 
        (-EntCode-) - Code of the selected file
        
    - 
        (-REPCNTR-) - Reporting country value
        
    - 
        (-FileCode-) - Code of the relevant relation
        
    - 
        (-AcctHolder-) - Code of the relevant relation
        
    - 
        (-C.AHTYPE-) - Means the type will be obtained from the AHTYPE tag for CRS reporting regime
        
    - 
        (-F.AHTYPE-) - Means the type will be obtained from the AHTYPE tag for FATCA reporting regime
        
    - 
        (-ROLECODE-) - Refers to the &nbsp;code of the role of the account holder
        
    - 
        (-ROLENAME-) - Refers to the name to be displayed for the account holder based on the role
        
    


&nbsp;
Example:
[C.RACCT:
FileCode=(-ENTCODE-)
RepAuthority=C_(-REPCNTR-)
AcctCode=(-ENTCODE-)_(-FILECODE-)_(-ROLECODE-)
AcctName=(-FILECODE\#AD-40-0-)_(-ROLENAME-)
AcctHolder=(-FILECODE-)
AcctHolderType=(-C.AHTYPE-)
AcctType=
AcctNote=
AcctStatus=P]
&nbsp;
The above will create a Reportable Account record for the CRS Reporting Regime with the specified values where:

- 
    Account Code (AcctCode) will include the RoleCode. Refer to the Optional Tags for CRSREPACC2 below for more information.

- 
    Account Name (AcctName) will include the system name for the RoleCode. Refer to the Optional Tags for CRSREPACC2 below for more information.

- 
    Account Holder type (AcctHolderType) will depend on the AHTYPE. Refer to the Optional Tags for CRSREPACC2 below for more information.


&nbsp;
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
Defines the message for the &nbsp;File Review result for creation of the Reportable Account record.
</td>
<td class="t2Col" style="vertical-align: top;">
[&lt;ReportingRegime&gt;.RACCT.MSG=&lt;Message to display&gt;]
&nbsp;
where

- 
    &lt;ReportingRegime&gt; can be C, F or G.

- 
    &lt;Message to display&gt; can be text or codes.


&nbsp;
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
Defines the Account Holder Type by considering also on the reporting country.
</td>
<td class="t2Col" style="vertical-align: top;">
[&lt;ReportingRegime&gt;.AHTYPE.C.&lt;ReportingCountry&gt;=&lt;LookValueCode&gt;]
[&lt;ReportingRegime&gt;.AHTYPE.I.&lt;ReportingCountry&gt;=&lt;LookValueCode&gt;]
&nbsp;
where

- 
    &lt;ReportingRegime&gt; can be C, F or G.

- 
    &lt;LookValueCode&gt; refers to the Account Holder Type value that is being set.


Example:
[F.AHTYPE.I.GB=GB1]
When the reporting country is 'GB', this will set the Account Holder Type to 'GB1' for the created Reportable Account.
&nbsp;
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
To classify if the Master File is reportable/non-reportable for undocumented account. Undocumented account is where the individual/organisation does not return any valid TIN(FIC/FIN) to confirm their tax residency.
</td>
<td class="t2Col" style="vertical-align: top;">
[&lt;ReportingRegime&gt;.UNDOCUMENT.IDREG=&lt;AEOI Register Type&gt;]
[&lt;ReportingRegime&gt;.UNDOCUMENT.LVALUE=&lt;Status of IDREG Reportable&gt;]
[&lt;ReportingRegime&gt;.UNDOCUMENT.REPCNTR=&lt;Reporting Country&gt;]
[&lt;ReportingRegime&gt;.UNDOCUMENT.STATUS=&lt;Status of IDREG NOT Reportable&gt;]
&nbsp;
where:

- &lt;ReportingRegime&gt; can be C, F or G.

Example 1:
[F.UNDOCUMENT.IDREG=INDC,INDI]
[F.UNDOCUMENT.LVALUE=Q]
[F.UNDOCUMENT.REPCNTR=IM,GB]
[F.UNDOCUMENT.STATUS=R]
If the relevant Master File has 'INDI'/'INDC' with Country/Jurisdiction 'IM'/'GB' and status 'Q', then the Master File is reportable.
If the relevant Master File has 'INDI'/'INDC' with Country/Jurisdiction 'IM'/'GB' and status 'R', then the Master File is not reportable.
&nbsp;
Example 2:
[F.UNDOCUMENT.IDREG=INDC,INDI]
[F.UNDOCUMENT.LVALUE=Q]
[F.UNDOCUMENT.REPCNTR=HK]
[F.UNDOCUMENT.STATUS=R,C]
If the relevant Master File has 'INDI'/'INDC' with Country/Jurisdiction 'HK' and status 'Q', then the Master File is reportable.
If the relevant Master File has 'INDI'/'INDC' with Country/Jurisdiction 'HK' and status 'R' or 'C', then the Master File is not reportable.
&nbsp;
</td>
</tr>
</tbody></table>

&nbsp;

<span class="hcp5">Example</span>:

REGIMES=C,F

&nbsp;

' Define the identity register record for querying the reporting status

[C.REPORTING.IDREG=FCRS]

[F.REPORTING.IDREG=FCSC]

&nbsp;

' Define the Reporting Status of the RFI

[C.REPORTING.LVALUE=R]

[F.REPORTING.LVALUE=R]

&nbsp;

' Exclude non individual files with the defined classification from being created as account holders

[C.REPORTING.UVALUE=CR01,CR02,CR07]

[F.REPORTING.UVALUE=0001,0002,0003,0004,0005,0006,0007,0008,0009,0010,0011,0012,0013,0014,0015,0016,0017,0018,0019,0022,0024,0025,0026,0027,0029]

&nbsp;

' Identity register type to retrieve country of tax residence

[TAXRES=FIC,FIN]

&nbsp;

' Identity register type where Reporting country code is to be retrieved from

[C.REPCNTR=CRFI]

[F.REPCNTR=FRFI]

&nbsp;

' Defined relation type of the controlling person for relevant relation/account holder

[C.CPTYPE=CNP]

[F.CPTYPE=SOW]

&nbsp;

' User table containing list of the countries of excha for each Reporting Country/Authority

[CODEREF:AEOI.MATRIX]

&nbsp;

' Y will group the multiple relevant relation roles held by one individual/corporate into one account holder record, N will create each of the roles as a separate account holder record

[C.GroupRoles=Y]

[F.GroupRoles=Y]

&nbsp;

' Roles defined in CRSREVIEW can be combined using the below tags, these tags will only take effect where GroupRoles=N

[C.RoleCodeReplace:REL.COT=REL.TRU]

[F.RoleCodeReplace:REL.COT=REL.TRU]

&nbsp;

' Roles defined in CRSREVIEW can be renamed using the below tags, these tags will only take effect where GroupRoles=N

[C.RoleNameReplace:SHRHDR=Equity Interest Holder]

[F.RoleNameReplace:SHRHDR=Equity Interest Holder]

&nbsp;

' [If GroupRoles=N is entered, update AcctCode below to: AcctCode=(-ENTCODE-)_(-FILECODE-)_(-ROLECODE-) and AcctName to: AcctName=(-FILECODE\#AD-40-0-) - (-RoleName-)]

'Creation of CRS Reportable account

[C.RACCT:

FileCode=(-ENTCODE-)

RepAuthority=C_(-REPCNTR-)

AcctCode=(-ENTCODE-)_(-FILECODE-)_02

AcctName=(-FILECODE\#AD-40-0-)

AcctHolder=(-FILECODE-)

AcctHolderType=(-C.AHTYPE.VALUE-)

AcctType=

AcctNote=

AcctStatus=P

]

&nbsp;

' These tags define the Account Holder type based on the Relevant Relations CRS Classification. If no CRS Classification, it will be based on the Master File type.

[C.AHTYPE.IDREGCODE=FCRS]

[C.AHTYPE.MATCHFIELD=UDCODE]

[C.AHTYPE.VALUE:CR06=CR2:CR04=CR3:CR05=CR1:CR08=CR2]

[C.AHTYPE.I=CR2]

[C.AHTYPE.C=CR3]

[C.AHTYPE.P=CR3]

[C.AHTYPE.F=CR3]

[C.AHTYPE.T=CR1]

' CRS display message

[C.RACCT.MSG=CRS Account Holder: (-AcctHolder\#AD-40-0-)]

&nbsp;

'Creation of FATCA Reportable account

[F.RACCT:

FileCode=(-ENTCODE-)

RepAuthority=F_(-REPCNTR-)

AcctCode=(-ENTCODE-)_(-FILECODE-)_01

AcctName=(-FILECODE\#AD-40-0-)

AcctHolder=(-FILECODE-)

AcctHolderType=(-F.AHTYPE.VALUE-)

AcctType=

AcctNote=

AcctStatus=P

]

' These tags define the Account Holder type based on the Relevant Relations FATCA Classification. If no FATCA Classification, it will be based on the Master File type.

[F.AHTYPE.IDREGCODE=FCSC]

[F.AHTYPE.MATCHFIELD=UDCODE]

[F.AHTYPE.VALUE:0020=103:0023=102:0072=104]

[F.AHTYPE.I=104]

[F.AHTYPE.C=104]

[F.AHTYPE.P=104]

[F.AHTYPE.F=104]

[F.AHTYPE.T=102]

' FATCA display message

[F.RACCT.MSG=FATCA Account Holder: (-AcctHolder\#AD-40-0-)]

&nbsp;
### Optional Tags for Reportable Account [CRSREPACC2]
These applies to all regimes, example shown is for FATCA.

<table class="Table1" cellspacing="0px" width="100%">
<colgroup><col style="width: 50%;">
<col style="width: 50%;">
</colgroup><tbody><tr class="t1st">
<td>
Purpose
</td>
<td>
Syntax
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
Specify the account holder type based on the capacity of the relevant relation..
To have two records to be created for one Master File in different capacity - as Controlling Person and as Relevant Relation, you can add the CREATE=B tag. This requires you to have all three options for the AHTYPE tag.
</td>
<td class="t2Col" style="vertical-align: top;">
[&lt;ReportingRegime&gt;.AHTYPE.&lt;Option&gt;=&lt;AccountTypeCode&gt;]
[&lt;ReportingRegime&gt;.AHTYPE.CREATE=B]
&nbsp;
where:

- 
    &lt;ReportingRegime&gt; can be:

- 
        
    - 
        C for CRS
        
    - 
        F for FATCA
        
    

- 
    &lt;Option&gt; can be:

- 
        
    - 
        CP - Only the Controlling Person is reportable.
        
    - 
        RR - Only the Relevant Relations is reportable.
        
    - 
        RC - Both Controlling Persons and Relevant Relations are reportable.
        
    

- 
    &lt;AccountTypeCode&gt; refers to the code of the Account Holder type as defined in the Reportable Account Holder Type [RAHT] lookup table.


&nbsp;
Example:
[C.AHTYPE.CREATE=B]
[C.AHTYPE.CP=CR2]
[C.AHTYPE.RR=CR1]
[C.AHTYPE.RC=CR1]
&nbsp;
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
Specify the account holder type for the account holder based on the classification of the relevant relation.
If there is no classification, then it will be based on the Master File type.
&nbsp;
</td>
<td class="t2Col" style="vertical-align: top;">
[&lt;ReportingRegime&gt;.AHTYPE.IDREGCODE=&lt;IdRegType&gt;]
[&lt;ReportingRegime&gt;.AHTYPE.MATCHFIELD=UDCODE]
[&lt;ReportingRegime&gt;.AHTYPE.VALUE:&lt;ClassificationType&gt;=&lt;AccountTypeCode&gt;]
[&lt;ReportingRegime&gt;.AHTYPE.&lt;MFType&gt;=&lt;AccountTypeCode&gt;]
&nbsp;
where

- 
    &lt;ReportingRegime&gt; can be:

- 
        
    - 
        C for CRS
        
    - 
        F for FATCA
        
    

- 
    &lt;IdRegType&gt; is the code of the Identity Register type where the classification will be from.

- 
    &lt;ClassificationType&gt; is the code for the classification.

- 
    &lt;AccountTypeCode&gt; refers to the code of the Account Holder type as defined in the Reportable Account Holder Type [RAHT] lookup table.

- 
    &lt;MFType&gt; refers to the Master File type and can be:

- 
        
    - 
        I for Individual Master File type
        
    - 
        C for Company Master File type
        
    - 
        P for Partnership Master File type
        
    - 
        F for Foundation Master File type
        
    - 
        T for Trust Master File type
        
    


&nbsp;
Example:
[C.AHTYPE.IDREGCODE=FCRS]
[C.AHTYPE.MATCHFIELD=UDCODE]
[C.AHTYPE.VALUE:CR06=CR2:CR04=CR3:CR05=CR1:CR08=CR2]
[C.AHTYPE.I=CR2]
[C.AHTYPE.C=CR3]
[C.AHTYPE.P=CR3]
[C.AHTYPE.F=CR3]
[C.AHTYPE.T=CR1]
The above specifies the account holder type to be based on the classification of the Identity Register type 'FCSR' where:

- 
    If the classification is CR06, the account holder type is CR2.

- 
    If the classification is CR04, the account holder type is CR3.

- 
    If the classification is CR05, the account holder type is CR1.

- 
    If the classification is CR08, the account holder type is CR2.


If there is no classification, then the account holder type is as follows:

- 
    CR2 for Master File type 'Individual' and 'Trust'.

- 
    CR3 for Master File types 'Company', 'Partnership', 'Foundation'.


&nbsp;
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
This is to create multiple Reportable Account records for an account holder in multiple capacities.
By default, a Reportable Account record is created only if there is no existing record with the configured Account Code (AcctCode) for the reporting regime (RepAuthority).
</td>
<td class="t2Col" style="vertical-align: top;">
[&lt;ReportingRegime&gt;.GroupRoles=N]
&nbsp;
where &lt;ReportingRegime&gt; can be C, F or G.
&nbsp;
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
To combine the roles defined in the CRSREVIEW.
</td>
<td class="t2Col" style="vertical-align: top;">
[&lt;ReportingRegime&gt;.RoleCodeReplace:&lt;RoleCode1&gt;,&lt;RoleCode2&gt;=&lt;NewRoleCode&gt;:&lt;RoleCode3&gt;=&lt;NewRoleCode&gt;]
&nbsp;
where

- 
    &lt;ReportingRegime&gt; can be C, F or G.

- 
    &lt;RoleCode&gt; is the current code and can be:

- 
        
    - 
        REL.&lt;RelationTypeCode&gt;
        
    - 
        SHRHDR
        
    - 
        INT.&lt;InterestTypeCode&gt;
        
    - 
        BENF
        
    - 
        SLT.&lt;SubLedgerTypeCode&gt;
        
    

- 
    &lt;NewRoleCode&gt; is the code to replace the current code.


&nbsp;
Example:
[F.RoleCodeReplace:REL.COT=REL.TRU:SHRHDR=INT.BEO]
The above combines the role of Co-Trustee with the role of Trustee and the roles of shareholder/partner and beneficial owner for the FATCA reporting regime.
&nbsp;
[F.RoleCodeReplace:INT.UOW=INT.UBO]
The above combines the two interest roles of Ultimate Holding Company and Ultimate Beneficial Owner for the FATCA reporting regime.
&nbsp;
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
Change the display name of the RoleCode. Each RoleCode has system assigned names that will be displayed by default.
<table class="Table1" cellspacing="0px" width="88.434%">
<colgroup><col style="width: 20.06%;">
<col style="width: 79.94%;">
</colgroup><tbody><tr class="t1st">
<td bgcolor="#000080">
RoleCode
</td>
<td bgcolor="#000080">
RoleName if no defined tag
</td>
</tr>
<tr class="t2Row">
<td class="t1Col">
REL.TRU
</td>
<td class="t2Col">
Description of Relationship Type e.g. Trustee
</td>
</tr>
<tr class="t1Row">
<td class="t1Col">
SHRHDR
</td>
<td class="t2Col">
Hard-coded to: Shareholder/Partner
</td>
</tr>
<tr class="t2Row">
<td class="t1Col">
INT.UBO
</td>
<td class="t2Col">
Caption as defined in Interest Types e.g. [AddrCode.Caption=&lt;Caption&gt;]. If not defined, it will show the caption in Field Settings e.g. Ultimate Beneficial Owner
</td>
</tr>
<tr class="t1Row">
<td class="t1Col">
BENF
</td>
<td class="t2Col">
Field caption in settings of 'Beneficiary' on Beneficiary screen e.g. Beneficiary
</td>
</tr>
<tr class="t2Row">
<td class="t1Col">
SLT.DOTH
</td>
<td class="t2Col">
Name of SL Type defined in lookup value [SLTP] e.g. other debtors
</td>
</tr>
</tbody></table>
&nbsp;
</td>
<td class="t2Col" style="vertical-align: top;">
[&lt;Regime&gt;.ROLENAMREPLACE:&lt;RoleCode&gt;=&lt;RoleName&gt;:&lt;RoleCode2&gt;=&lt;RoleName2&gt;]
&nbsp;
where:

- 
    &lt;ReportingRegime&gt; can be C, F or G.

- 
    &lt;RoleCode&gt; is the code.

- 
    &lt;RoleName&gt; is the new name for the RoleCode.


&nbsp;
Example:
[F.ROLENAMEREPLACE:SLT.DOTH=Debtor:INT.UBO=Owner]
The above will display 'Debtor' for SLT.DOTH and 'Owner' for UBO Interest Type for the FATCA Reporting Regime..
&nbsp;
</td>
</tr>
</tbody></table>

&nbsp;

See also:

- 
    
    [File Review](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/File_Review_Function.htm)

- 
    
    [Review Rules](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Review_Rules.htm)


&nbsp;

[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; AEOI Review - Tags

&nbsp;

(c) Viewpoint Software for 
 Business Ltd

Version: 8.0.2022.09.20


