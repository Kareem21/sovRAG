



# MFSEC Tag for Reports and Widgets
When access to Master Files is restricted and you would like this to 
 be applied to reports and widgets, the MFSEC tag must be added to the 
 report templates and widget. The syntax and location of the tag differs 
 depending on the item, but it requires the following information:

	

- <span lang="EN-GB" xml:lang="EN-GB">&lt;Dataset Name&gt; - refers 
    	 to the SQL query used to retrieve the Master File field to check on 
    	 for the access</span>

	

- <span lang="EN-GB" xml:lang="EN-GB">&lt;ID&gt; - refers to the 
    	 identifier used in the SQL query for the database table or view containing 
    	 the Master File field</span>

	

- <span lang="EN-GB" xml:lang="EN-GB">&lt;MFField&gt; - refer 
    	 to the field code of the Master File field to check for user’s accessibility</span>

<table class="Table1" style="border-left-width: 2px; border-right-width: 2px; border-top-width: 2px; border-bottom-width: 2px;" cellspacing="0px" width="1216">
	<colgroup><col style="width: 8.33%;">
	<col style="width: 32.072%;">
	<col style="width: 30.281%;">
	<col style="width: 29.317%;">
	</colgroup><tbody><tr class="t1st">
		<td>

Item

</td>
		<td>

Syntax

</td>
		<td>

Location

</td>
		<td>

Example

</td>
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

Word Report

</td>
		<td class="t2Col" rowspan="3">

[/&lt;Dataset 
		 Name&gt;.MFSEC=&lt;ID&gt;.&lt;MFFIeld&gt;/]

</td>
		<td class="t1Col">

The 
		 tag is to be defined in the Key Information of the template.

</td>
		<td rowspan="3" class="t2Col">

<span class="hcp3">[/REGDETAILS.MFSEC=Officers.EntCode/]</span>

</td>
	</tr>
	<tr class="t1Row">
		<td class="t1Col">

SSRS Report

</td>
		<td class="t1Col">

The 
		 tag is to be defined in the Tag Values field of the SSRS Report.

</td>
		
	</tr>
	<tr class="t2Row">
		<td class="t1Col">

Widget

</td>
		<td class="t1Col">

The 
		 tag is to be defined in the Tag Values field of the widget.

</td>
		
	</tr>
	<tr class="t1Row">
		<td class="t1Col">

Excel Statement

</td>
		<td class="t2Col">

[=MFS:&lt;Dataset 
		 Name&gt;.MFSEC=&lt;Table&gt;.&lt;MFFIeld&gt;]

</td>
		<td class="t1Col">

The 
		 tag is to be defined in the Excel file template

</td>
		<td class="t2Col">

<span class="hcp3">[=MFS.CHANGE1.MFSEC=RefStatus.RefCode]</span>

</td>
	</tr>
</tbody></table>

&nbsp;

<span lang="EN-GB" xml:lang="EN-GB" class="hcp4">Note</span><span lang="EN-GB" xml:lang="EN-GB">:</span><span class="hcp4"> 
 </span><span lang="EN-GB" xml:lang="EN-GB">If the tag is added to the 
 report or widget but the option 'Apply Master File Security to Reports 
 and Widgets' is not ticked, then Master Files that user cannot access 
 will not be excluded.</span>

&nbsp;

&nbsp;

<span lang="EN-GB" xml:lang="EN-GB">S</span>ee also:

	

- [System 
    	 Defaults - Security](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/System_Defaults_-_Security.htm)

	

- [Key Information](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Key_Information.htm)

	

- [Document 
    	 Management Tags](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Document_Manager/Document_Management_Tags.htm)

	

- [Action 
    	 Management - Tags](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Practice_Manager/Action_Management_-_Tags.htm)

	

- [Excel Statements 
    	 - Fundamentals](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Excel_Statements_Fundamentals.htm)

	

- [Dashboard Widgets](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Dashboard_Widgets.htm)

&nbsp;

[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; MFSEC Tag for Reports and Widgets

&nbsp;

(c) Viewpoint Software for 
 Business Ltd

Version: 8.0.2022.09.20


