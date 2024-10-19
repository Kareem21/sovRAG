



# Setup/Statutory Review - Tags
These tags check on information entered or missed out for a Master File 
 or Entity File. Refer to [File Review 
 Function](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/File_Review_Function.htm) to see where the tags can be added.

&nbsp;
## Check Information in Addresses Screen
These tags can be used to check if a specific address type has been 
 created. These tags can be used for both Setup review and Statutory review.

<table class="Table1" style="border-collapse: separate;" cellspacing="0px" width="100%" border="1">
	<colgroup><col style="width: 23.825%;">
	<col style="width: 28.799%;">
	<col style="width: 47.376%;">
	</colgroup><tbody><tr class="t1st">
		<td>Purpose</td>
		<td>Syntax</td>
		<td>Example </td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

Specify required 
		 Master File address.

</td>
		<td class="t2Col" style="vertical-align: top;">

[AD.&lt;MasterFileType&gt;.Required:&lt;AddressType&gt;]

</td>
		<td class="t1Col" style="vertical-align: top;">

[AD.C.Required:BA,MA]

		

This looks for the address type BA and MA for the Master File 
		 type 'Company'.

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="vertical-align: top;">

Specify required 
		 statutory location.

</td>
		<td class="t2Col" style="vertical-align: top;">

[AD.ST.Required:&lt;AddressType&gt;]

</td>
		<td class="t1Col" style="vertical-align: top;">

[AD.ST.Required:SR]

		

This looks for the address type SR in the Statutory screen.

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

Check that the 
		 address is in a specific country.

</td>
		<td class="t2Col" style="vertical-align: top;">

[AD.&lt;AddressType&gt;.Country:&lt;CountryCode&gt;]

</td>
		<td class="t1Col" style="vertical-align: top;">

[AD.SR.Country:CY]

		

This will check if the ‘SR’ address type is in Cyprus (Country 
		 code: CY).

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="vertical-align: top;">

Check that the 
		 address is in the same country as the incorporation country.

</td>
		<td class="t2Col" style="vertical-align: top;">

[AD.&lt;AddressType&gt;.Country:@INCORP]

</td>
		<td class="t1Col" style="vertical-align: top;">

[AD.SR.Country:@INCORP]

</td>
	</tr>
</tbody></table>

&nbsp;

<span class="hcp1">Note</span>: In 
 the table above, the syntax shows a single value. If it is necessary to 
 define multiple values, use comma (,) to separate the values e.g. [AD.C.Required:BA,MA]

&nbsp;
## Check Information in Identity Register Screen
Identity Register tags can be used to check on the Identity/AEOI Register 
 Types that have been set up for the Master File.

<table class="Table1" style="border-collapse: separate;" cellspacing="0px" width="100%" border="1">
	<colgroup><col style="width: 23.95%;">
	<col style="width: 29.303%;">
	<col style="width: 46.746%;">
	</colgroup><tbody><tr class="t1st">
		<td>Purpose</td>
		<td>Syntax</td>
		<td>Example</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

Check that the 
		 required Identity Register type has been set up.

</td>
		<td class="t2Col" style="vertical-align: top;">

[IDREG.&lt;Type&gt;.Required:&lt;IDCode&gt;]

		

where:

		
			

- &lt;Type&gt; refers to the Master File type with I for 
    			 individual and C for non-individual Master File type.

			

- &lt;IDCode&gt; refers to the code of the Identity Register 
    			 type.

		</td>
		<td class="t1Col" style="vertical-align: top;">

[IDREG.I.Required:PSP,BCT]

		

This looks for the Identity Register type ‘PSP’ and ‘BCT’ for 
		 individual Master Files.

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="vertical-align: top;">

Check on individual 
		 Identity Register types that has been set up.

</td>
		<td class="t2Col" style="vertical-align: top;">

[FILTER:IDREGI.Type=&lt;IDCode&gt;]

</td>
		<td class="t1Col" style="vertical-align: top;">

[FILTER:IDREGI.Type=PSP,BCT]

		

Identity Register types other than ‘PSP’ and ‘BCT’ will result 
		 in a message saying the Identity Register type is not allowed.

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

Check on non-individual 
		 Identity Register types that has been set up.

</td>
		<td class="t2Col" style="vertical-align: top;">

[FILTER:IDREGC.Type=&lt;IDCode&gt;]

</td>
		<td class="t1Col" style="vertical-align: top;">

[FILTER:IDREGC.Type=GIIN,FIC]

		

Identity Register types other than ‘GIIN’ and ‘FIC’ will result 
		 in a message saying the Identity Register type is not allowed.

</td>
	</tr>
</tbody></table>

&nbsp;

&nbsp;
## Check Relations/Officers Information
Relation tags can be used to check that specific relation types have 
 been set up for the Master File or Entity File.

<table class="Table1" style="border-collapse: separate;" cellspacing="0px" width="100%" border="1">
	<colgroup><col style="width: 23.699%;">
	<col style="width: 29.618%;">
	<col style="width: 46.683%;">
	</colgroup><tbody><tr class="t1st">
		<td>Purpose</td>
		<td>Syntax</td>
		<td>Example</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

Check that the 
		 required relation has been set up.

</td>
		<td class="t2Col" style="vertical-align: top;">

[RE.&lt;RelationshipClass&gt;.Required:&lt;RelationCode&gt;]

		

where:

		
			

- &nbsp;&lt;RelationshipClass&gt; can be M (Master File 
    			 relation), I (Internal Relation). E (Entity relation), O (Statutory 
    			 Officer) or T (Trust Officer).

			

- &lt;RelationshipCode&gt; can be repeated if more than 
    			 one instance of the relation is required e.g. [RE.O.Required:DIR,DIR,SEC].

		
		
If it is required to have one director, one alternate director 
		 with a third one being director or alternate director, the * sign 
		 can be used: [RE.O.Required:DIR,DAL,D*].

</td>
		<td class="t1Col" style="vertical-align: top;">

[RE.E.Required:AGT]

		

This will check for the relation 'AGT' &nbsp;in the Entity - 
		 Relations screen.

</td>
	</tr>
</tbody></table>

&nbsp;
## Check Shareholding Information
These tags are used on managed entities only and normally placed in 
 the Tag Values field in Entity Types.

<table class="Table1" style="border-collapse: separate;" cellspacing="0px" width="100%" border="1">
	<colgroup><col style="width: 18.22%;">
	<col style="width: 35.916%;">
	<col style="width: 45.864%;">
	</colgroup><tbody><tr class="t1st">
		<td>Purpose</td>
		<td>Syntax</td>
		<td>Example</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

Check the minimum 
		 quantity of issued capital.

</td>
		<td class="t2Col" style="vertical-align: top;">

[SH.Cap.Issued.MinQnt:&lt;Number&gt;]

</td>
		<td class="t1Col" style="vertical-align: top;">

[SH.Cap.Issued.MinQnt:12500]

		

This will check that the issued capital is at least 12500.

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="vertical-align: top;">

Check the minimum 
		 quantity of authorised capital.

</td>
		<td class="t2Col" style="vertical-align: top;">

[SH.Cap.Auth.MinQnt:&lt;Number&gt;]

</td>
		<td class="t1Col" style="vertical-align: top;">

[SH.Cap.Auth.MinQnt:12500]

		

This will check that the authorised capital is at least 12500.

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

Check the minimum 
		 amount of issued capital.

</td>
		<td class="t2Col" style="vertical-align: top;">

[SH.Cap.Issued.MinAmount:&lt;Amount&gt;]

</td>
		<td class="t1Col" style="vertical-align: top;">

[SH.Cap.Issued.MinAmount:12500]

		

This will check that the amount of issued capital is at least 
		 12500.

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="vertical-align: top;">

Check the minimum 
		 amount of authorised capital.

</td>
		<td class="t2Col" style="vertical-align: top;">

[SH.Cap.Auth.MinAmount:&lt;Amount&gt;]

</td>
		<td class="t1Col" style="vertical-align: top;">

[SH.Cap.Auth.MinAmount:50000]

		

This will check that the amount of authorised capital is at 
		 least 50000.

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

Check the minimum 
		 amount of paid capital.

</td>
		<td class="t2Col" style="vertical-align: top;">

[SH.Cap.Paid.MinAmount:&lt;Amount&gt;]

</td>
		<td class="t1Col" style="vertical-align: top;">

[SH.Cap.Paid.MinAmount:12500]

		

This will check that the amount of paid up capital is at least 
		 12500.

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="vertical-align: top;">

Check the minimum 
		 amount of stated capital.

</td>
		<td class="t2Col" style="vertical-align: top;">

[SH.Cap.Stated.MinAmount:&lt;Amount&gt;]

</td>
		<td class="t1Col" style="vertical-align: top;">

[SH.Cap.Stated.MinAmount:12500]

		

This will check that the amount of stated capital is at least 
		 12500.

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

Check the number 
		 of shareholders.

</td>
		<td class="t2Col" style="vertical-align: top;">

[SH.Members.MinNumber:&lt;Number&gt;]

		

[SH.Members.MaxNumber:&lt;Number&gt;]

</td>
		<td class="t1Col" style="vertical-align: top;">

[SH.Members.MinNumber:2]

		

This will check that there are at least two shareholders.

		

[SH.Members.MaxNumber:99]

		

This will check that the number of shareholders is not more 
		 than 99.

</td>
	</tr>
</tbody></table>

&nbsp;

&nbsp;
## Check User Fields
These tags can be used to retrieve and format user fields.

&nbsp;

<table class="Table1" style="border-collapse: separate;" cellspacing="0px" width="100%" border="1">
	<colgroup><col style="width: 18.85%;">
	<col style="width: 35.726%;">
	<col style="width: 45.424%;">
	</colgroup><tbody><tr class="t1st">
		<td>Purpose</td>
		<td>Syntax</td>
		<td>Example</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col" style="vertical-align: top;">

Specify required 
		 User Fields.

</td>
		<td class="t2Col" style="vertical-align: top;">

[UF.&lt;Type&gt;.Required:&lt;UserFieldCode&gt;]

		

where:

		

&lt;Type&gt; can be M (Master File User Fields), N (Identity 
		 Details User Fields), C (Company User Fields), T (Trust User Fields), 
		 F (Fund User Fields) or B (Billing File User Fields)

</td>
		<td class="t1Col" style="vertical-align: top;">

[UF.M.Required:KYC100,KYC110,KYC120,KYC300,KYC301,KYC303,KYC304]

		

This will retrieve the specified User Fields and needs to be 
		 specified before the code for formatting the User Fields.

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col" style="vertical-align: top;">

Format the retrieved 
		 User Fields as a User Field template.

</td>
		<td class="t2Col" style="vertical-align: top;">

[UF.&lt;Type&gt;.Format:TemplateTitle

		

Heading

		

++&lt;UserFieldCode&gt;

		

…

		

]

</td>
		<td class="t1Col" style="vertical-align: top;">

[UF.M.Format:Validation 
		 and Referee

		

+Validation

		

++&lt;KYC100&gt;

		

++&lt;KYC110&gt;

		

+Referee

		

++&lt;KYC120&gt;

		

]

		

This will retrieve the User Fields KYC100, KYC110 and KYC120 
		 and format them as a User Field template with the title ‘Validation 
		 and Referee’. This template also contains the headings ‘Validation’ 
		 and ‘Referee’.

</td>
	</tr>
</tbody></table>

&nbsp;

<span class="hcp1">Note</span>: For 
 the User Field template, you can have as many headings as necessary. Use 
 the symbol (+) to add indentation.

&nbsp;

&nbsp;

See also:

	

- [Review Rules](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Review_Rules.htm)

&nbsp;

[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; Setup/Statutory Review -Tags

&nbsp;

(c) Viewpoint Software for 
 Business Ltd

Version: 8.0.2022.09.20


