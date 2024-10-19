



# Referencing Tags
Referencing Tags enable better maintenance of tag configuration and 
 allow for an item to have multiple tag configurations. These items can 
 be:

	

- [Entity types](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Entity_Types.htm)

	

- [Identity 
    	 Register types](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Identity_AEOI_Register_Types.htm)

	

- [Relationship 
    	 types](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Relationship_Types.htm) (only for Statutory Officers and Master File Relations)

	

- [Lookup table](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Lookup_Tables.htm) 
    	 and lookup table values - for lookup table values, this applies only 
    	 to values of certain lookup tables. Refer to [Lookup 
    	 Tables](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Lookup_Tables.htm).

	

- [User table](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/User_Tables.htm) and 
    	 user table values

	

- [Review Rules](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Review_Rules.htm)

	

- [Change Codes](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Changes_Codes.htm)

	

- [Excel Statements](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Excel_Statements_-_Design_Statement.htm) 
    	 (but only General Referencing Tags)

	

- [Payment 
    	 type and export batches](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Client_Accountant/Payment_Types_&_Export_Batches.htm) (but only General Referencing Tags)

&nbsp;
## Types of Referencing Tags
There are two types of referencing tag values:

	

- General

	

- Conditional

If both types of referencing tag values are found for an item, the conditional 
 referencing tag values will take precedence over the general referencing 
 tag.

In order to implement referencing tag values, you need to:

	

1. Set up the reference tag values as User Tables.

	

1. Insert the relevant reference tags to the Tag Values field of 
    	 the entity type, lookup table value or review rule.

&nbsp;
## Setting up Reference Tag Values
You can have multiple reference tag values to cater for the different 
 tag configurations that you require. However, each of these must be set 
 up as User Table value therefore, ensure that you first create the User 
 Table.

	

1. In Viewpoint – Home, go to Configuration &gt; Business Parameters 
    	 &gt; General &gt; User Tables/Values.

	

1. Click New.

	

1. Enter the code and name for this User Table.

	

1. Click Update.

	

1. Select the table that you have created previously and click 
    	 New in the lower grid.

	

1. Enter the following:
    
    	
        		
        
    - Code - Enter a code for the referencing tag value.
        
        
        		
    - Name - Enter a description for the referencing tag value.
        
        
        		
    - Tag Values - Enter the tag configuration.
        
        
        	

	

1. Click Update.

	

1. Repeat steps 5 to 7 for each referencing tag value that you 
    	 require.

<span style="font-weight: bold; font-style: italic;">Note</span>: You 
 can have more than one User Table for Reference Tag Values, if applicable.

&nbsp;
## Inserting the Referencing Tag
The referencing tag is to be entered in the Tag Values field of the 
 item so you need to do this in the relevant screen.

For example, if the referencing tag is for a Reporting Authority type, 
 then select the Reporting Authorities [RARC] Lookup Table in Configuration 
 &gt; Business Parameters &gt; General &gt; Lookup Values. Select the type 
 and add in the referencing tag values in the Tag Values field

The syntax for referencing tag differs depending on whether it is general 
 referencing tag value or conditional referencing tag value.

&nbsp;
### General Referencing Tag Value
For this type, the syntax is as follows:

[CODEREF:&lt;UserTableCode&gt;.&lt;Value1&gt;,&lt;Value2&gt;,&lt;Value...n&gt;,&lt;UserTableCode&gt;.&lt;Value1&gt;,&lt;Value2&gt;,&lt;Value...n&gt;]

&nbsp;

where

	

- &lt;UserTableCode&gt; is the code of the User Table for the 
    	 reference tag values.

	

- &lt;Value&gt; is the code of the reference tag value.

&nbsp;

Example:

[CODEREF:RATAGS.F_M1]

– the system will apply the tag configuration for the reference tag 
 value ‘F_M1’ from the User Table ‘RATAGS’.

&nbsp;

[CODEREF:RATAGS.F_M1,RTAG.IMSC]

or

[CODEREF:RATAGS.F_M1,

RTAG.IMSC]

– the system will apply the tag configuration from:

	

- The reference tag value ‘F_M1’ from the User Table ‘RATAGS’; 
    	 and

	

- The reference tag value ‘IMSC’ from the User Table ‘RTAG’.

There are limitations for line break function in CODEREF.

For example:

[CODEREF:&lt;UserTableCode&gt;.&lt;Value1&gt;,

&lt;Value2&gt;,

&lt;UserTableCode&gt;.&lt;Value1&gt;,

&lt;Value2&gt;]

or

[CODEREF:&lt;UserTableCode&gt;.&lt;Value1&gt;,&lt;Value2&gt;,

&lt;UserTableCode&gt;.&lt;Value1&gt;,&lt;Value2&gt;,

<span class="hcp4">&lt;UserTableCode&gt;.&lt;Value1&gt;,&lt;Value2&gt;</span>]

&nbsp;

Empty space and line break <span class="hcp4">are not 
 allowed</span> between '[CODEREF:' tag and the first User Table value.

For example: 

[CODEREF:

<span class="hcp4">&lt;UserTableCode&gt;.&lt;Value1&gt;</span>]

or

[CODEREF: &lt;UserTableCode&gt;.&lt;Value1&gt;]

&nbsp;

Empty space and line break <span class="hcp4">are not 
 allowed</span> between last User Table value and end bracket.

For example:

[CODEREF:&lt;UserTableCode&gt;.&lt;Value1&gt;

]

or

[CODEREF:&lt;UserTableCode&gt;.&lt;Value1&gt; 
 ]

&nbsp;

&nbsp;

&nbsp;
### Conditional Referencing Tag Values
For this type, condition can be set so the syntax is as follows:

<span class="hcp4">[CODEREF+&lt;Condition&gt;=&lt;Value&gt;:&lt;UserTableCode&gt;.&lt;Value1&gt;,&lt;Value2&gt;,&lt;Value...n&gt;,&lt;UserTableCode&gt;,&lt;Value1&gt;,&lt;Value2&gt;,&lt;Value...n&gt;]</span>

&nbsp;

where:

	

- &lt;Condition&gt; is the condition for this referencing tag 
    	 to be applied. The condition can be equal to (=) or not equal to (&lt;&gt;) 
    	 a specified value.

	

- &lt;UserTableCode&gt; is the code of the User Table for the 
    	 reference tag values.

	

- &lt;Value&gt; is the code of the reference tag value.

&nbsp;

<table class="Table1" cellspacing="0px" width="100%">
	<colgroup><col style="width: 33.333%;">
	<col style="width: 33.333%;">
	<col style="width: 33.333%;">
	</colgroup><tbody><tr class="t1st" style="height: 26px;">
		<td>

&nbsp;

</td>
		<td>

Specify as..

</td>
		<td>

Example Condition

</td>
	</tr>
	<tr class="t2Row" style="height: 48px;">
		<td class="t1Col">

Master File type

</td>
		<td class="t2Col">

MF.RefType

</td>
		<td class="t1Col">

MF.RefType=I,C

		

MF.RefType&lt;&gt;I,C

</td>
	</tr>
	<tr class="t1Row" style="height: 50px;">
		<td class="t1Col">

Master File Administrator Group

</td>
		<td class="t2Col">

MF.AdminGroup

</td>
		<td class="t1Col">

MF.AdminGroup=GROUP1,GROUP2

		

MF.AdminGroup&lt;&gt;GROUP1,GROUP2

</td>
	</tr>
	<tr class="t2Row" style="height: 48px;">
		<td class="t1Col">

Master File Team

</td>
		<td class="t2Col">

MF.TeamCode

</td>
		<td class="t1Col">

MF.TeamCode=T1,T2

		

MF.TeamCode&lt;&gt;T1,T2

</td>
	</tr>
	<tr class="t1Row" style="height: 50px;">
		<td class="t1Col">

Master File Organisational Unit

</td>
		<td class="t2Col">

MF.OrgUnit1

</td>
		<td class="t1Col">

MF.OrgUnit1=ORG1,ORG2

		

MF.OrgUnit1&lt;&gt;ORG1,ORG2

</td>
	</tr>
	<tr class="t2Row" style="height: 252px;">
		<td class="t1Col">

Master File Identity Register Type

</td>
		<td class="t2Col">

IDREG.&lt;IdType&gt;.&lt;DbField&gt;

		

&nbsp;

		

where

		
			

- &lt;IdType&gt; refers to the Identity Register Type 
    			 code

			

- &lt;DbField&gt; refers to the field of the Identity 
    			 Register type

		</td>
		<td class="t1Col">

IDREG.IDC.Country=SG,MY

		

IDREG.IDC.Country&lt;&gt;SG,MY

</td>
	</tr>
	<tr class="t1Row" style="height: 65px;">
		<td class="t1Col">

User Field

</td>
		<td class="t2Col">

UF.&lt;Key&gt;=&lt;Value1&gt;,&lt;Value2&gt;,&lt;Value&lt;n&gt;&gt;,...

		

&nbsp;

		

where 

		
			

- &lt;Key&gt; refers to the key of the User Field

			

- &lt;Value&gt; refers to the value of the User Field 
    			 key

		</td>
		<td class="t1Col">

UF.UFKEY=UFM01,UFM02

		

UF.UFKEY&lt;&gt;UFM01,UFM02

</td>
	</tr>
	<tr class="t2Row" style="height: 18px;">
		<td class="t1Col">

Logged in user’s User Group

</td>
		<td class="t2Col">

USER.UGroup

</td>
		<td class="t1Col">

USER.Ugroup=ADM,ADR

		

USER.Ugroup&lt;&gt;ADM,ADR

</td>
	</tr>
	<tr class="t1Row" style="height: 18px;">
		<td class="t1Col">

Logged in user’s Administrator Group

</td>
		<td class="t2Col">

USER.AGroup

</td>
		<td class="t1Col">

USER.AGroup=GROUP1,GROUP2

		

USER.Agroup&lt;&gt;GROUP1,GROUP2

</td>
	</tr>
	<tr class="t2Row" style="height: 18px;">
		<td class="t1Col" style="background-color: transparent;">

Logged 
		 in user’s Organisational Unit

</td>
		<td class="t2Col">

USER.TeamGroup

</td>
		<td class="t1Col">

USER.TeamGroup=TA,CA

		

USER.TeamGroup&lt;&gt;TA,CA

</td>
	</tr>
	<tr class="t1Row" style="height: 18px;">
		<td class="t1Col">

Logged in user’s Office

</td>
		<td class="t2Col">

USER.Office

</td>
		<td class="t1Col">

USER.Officer=MY,SG

		

USER.Officer&lt;&gt;MY,SG

</td>
	</tr>
	<tr class="t2Row" style="height: 18px;">
		<td class="t1Col">

Entity Status

</td>
		<td class="t2Col">

EF.Status

</td>
		<td class="t1Col">

EF.Status=0,1,3

		

EF.Status&lt;&gt;0,1,3

</td>
	</tr>
	<tr class="t1Row" style="height: 18px;">
		<td class="t1Col">

Entity Sub-Status

</td>
		<td class="t2Col">

EF.SubStatus

</td>
		<td class="t1Col">

EF.SubStatus=0A,0C

		

EF.SubStatus&lt;&gt;0A,0C

</td>
	</tr>
</tbody></table>

&nbsp;

Example:

[CODEREF+MF.AdminGroup&lt;&gt;N/D:RTAG.MNG]

- where the Master File does not belong in N/D Administrator Group, 
 the system will apply the tag configuration from the reference tag value 
 ‘MNG’ from the User Table ‘RTAG’.

&nbsp;

[CODEREF+MF.AdminGroup=N/D:RTAG.NMG]

- where the Master File belongs to N/D Administrator Group, the system 
 will apply the tag configuration from the reference tag value ‘NMG’ from 
 the User Table ‘RTAG’.

&nbsp;

[CODEREF+IDREG.IDC.Country=SG:RTAG.SGM]

- where the Country field of the IDC register identity type record for 
 the Master File &nbsp;is ‘SG’, the system will apply the tag configuration 
 from the reference tag value ‘SGM’ from the User Table ‘RTAG’.

&nbsp;

[CODEREF+USER.Office=MY:RTAG.MYM]

- where the logged in user’s is ‘MY’, the system will apply the tag 
 configuration from the reference tag value ‘MYM’ from the User Table ‘RTAG’.

&nbsp;

You are here:[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; [Additional Information](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Confidential_Database.htm) &gt; [General](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Confidential_Database.htm) &gt; Referencing Tags

&nbsp;

(c) Viewpoint Software for 
 Business Ltd

Version: 8.0.2022.09.20


