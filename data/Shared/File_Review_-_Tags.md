



# File Review - Tags
File Review tags are utilised in File Review function and it tells Viewpoint 
 Connect program what to do. These tags may work on their own or together 
 with a corresponding review rule. Where the tags are added depend on the 
 type of tag and its function.

&nbsp;
## Bypass Authority Checking for Posting Updates
This tag is used to allow users to post updates from the File Review 
 results even when ordinarily, the user is not able to create records manually.

	

- For Compliance review and AEOI review, add this tag to the relevant 
    	 review rule - <span class="hcp2">[RVW.UPD.CheckAuth:N]</span>

	

- For updates related to Meetings, Filings and Reviews screens, 
    	 the tag is to be added to the tag configuration in the relevant section 
    	 - <span class="hcp2">+CheckAuth=N  
    &#13;&#10;	</span>  
    &#13;&#10;	Example:  
    &#13;&#10;	  
    &#13;&#10;	[FL.RC.AR:  
    &#13;&#10;	FlDescription=Annual Return  
    &#13;&#10;	PeriodFrom=01/01  
    &#13;&#10;	PeriodTo=31/12  
    &#13;&#10;	+CheckAuth=N]  
    &#13;&#10;	  
    &#13;&#10;	  
    &#13;&#10;	The above will allow users running the File Review to post update to 
    	 create the Record for the Annual Return Filing Type.

&nbsp;
## Specify Selection of Update Items
This tag is to ensure that an update item in the File Review results 
 is ticked for posting all the time. When this tag is not defined, the 
 default is 'N', allowing user to tick/un-tick an update item.

	

- For AEOI review, this tag is to be added to the relevant review 
    	 rule except CRSREPACC2 - <span class="hcp2">[RVW.UPD.MustSelect=Y]</span>

	

- For 
    	 AEOI review, this tag is to be added for CRSREPACC2 review rule - 
    	 <span class="hcp2">+MustSelect=Y</span>

	

- For updates related to Meetings, Filings and Reviews screen, 
    	 the tag is to be added in the tag configuration - <span class="hcp2">+MustSelect=Y</span>  
    &#13;&#10;	  
    &#13;&#10;	[FL.RC.AR:  
    &#13;&#10;	FlDescription=Annual Return  
    &#13;&#10;	PeriodFrom=01/01  
    &#13;&#10;	PeriodTo=31/12  
    &#13;&#10;	+MustSelect=Y]  
    &#13;&#10;	  
    &#13;&#10;	The above will automatically select the Filing Record for posting.

&nbsp;
## Tags for Setup/Statutory Review
Setup review will check on information entered for a Master File while 
 Statutory review will check on information for an Entity File (where Entity 
 Administration is ticked). Refer to [Setup/Statutory 
 Review - Tags](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Setup_Statutory_Review_-_Tags.htm)

&nbsp;
## Tags for Compliance Review
Compliance review will check on compliance-related information. Refer 
 to [Compliance 
 Review - Tags](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Compliance_Review_-_Tags.htm).

&nbsp;
## Tags for AEOI Review
AEOI review will assist users on getting the relevant Master Files up-to-date 
 for CRS and FATCA reporting by ensuring records for Identity Register, 
 Classification and Indicia; and Reportable Accounts are created. Refer 
 to [AEOI Review - Tags](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/AEOI_Review_-_Tags.htm).

&nbsp;
## Tags for Data Validation Review
Data Validation tags is used to review user fields. Refer to [Data 
 Validation Review - Tags](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Data_Validation_Review_-_Tags.htm).

&nbsp;
## Tags for Meetings/Filings/Reviews Review
The Meetings, Filings and Reviews scopes check on the contents of the 
 Meetings, Filings and Reviews screens. Tags are available to check for 
 missing types and also to create the records for the user. Refer to [Meetings, Filings, 
 Reviews - Tags](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Meetings,_Filings,_Reviews_-_Tags.htm).

&nbsp;

&nbsp;

See also:

	

- [File Review](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/File_Review_Function.htm)

	

- [Review Rules](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Review_Rules.htm)

&nbsp;

[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; File Review -Tags

&nbsp;

(c) Viewpoint Software for 
 Business Ltd

Version: 8.0.2022.09.20


