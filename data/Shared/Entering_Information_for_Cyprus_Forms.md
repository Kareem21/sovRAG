



# Entering Information for Cyprus Forms
To complete Cyprus statutory forms where certain information needs to 
 be in Greek, use the following features:

	

- Local Address Card

	

- Alternative Description field

	

- User Fields - Identity Details

&nbsp;
## Local Address Card
This is to record the address detail in both English and Greek. You 
 need to:

	

- Tick the Enable 'Local Address Cards' option in [System 
    	 Defaults &gt; General/Master File](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/System_Defaults_-_General_Master_File.htm).

	

- Enter the address details in Greek for the Address Card.

&nbsp;
### Entering address details in Greek
Once you have enabled the Local Address Cards feature, when you create 
 or edit an Address Card, you will be able to see:

	

- A new Local Address field.

	

- Duplicate fields for each address details.

Select Greek for Local Address and enter the address details in English 
 for the fields on the left and in Greek for the fields on the right.

&nbsp;
## Alternative Description Field
This field is for a relationship type and allows for the relationship 
 description to be entered in Greek. This normally applies to relationship 
 types like Director and Secretary. If necessary, you can also enter the 
 description in Greek for other relationship types.

	

1. In Configuration &gt; Business Parameters &gt; Entity Administration 
    	 &gt; Relationship Types, select the relationship type you want to 
    	 add the description to.

	

1. Click Edit.

	

1. In the Alternative Description field, enter the description 
    	 in Greek.

	

1. Click Update.

&nbsp;
## User Fields - Identity Details
This is used to enter the Nationality and Occupation details in Greek.

&nbsp;
### Create Category

	

1. In Configuration &gt; Business Parameters &gt; General, select 
    	 Lookup Values.

	

1. Select the Master File Category [MCAT] lookup table.

	

1. Click New.

	

1. Enter the following information:
    
    	
        		
        
    - Element Code - CYF
        
        
        		
    - Name - Cyprus Greek Fields
        
        
        		
    - Long Name -&nbsp;Cyprus Greek Fields
        
        
        	

	

1. Click Update.

&nbsp;
### Create User Fields

	

1. In Configuration &gt; Business Parameters &gt; General &gt; 
    	 User Fields &gt; Identity Details.

	

1. Click New.

	

1. Enter the following information:
    
    	
        		
        
    - Category - CYF
        
        
        		
    - Key - CYNAT
        
        
        		
    - Field Type - Text [11]
        
        
        		
    - Caption - Nationality (Greek)
        
        
        	

	

1. Click Update.

	

1. Click New again.

	

1. Enter the following information:
    
    	
        		
        
    - Category - CYF
        
        
        		
    - Key - CYOCC
        
        
        		
    - Field Type - Text [11]
        
        
        		
    - Caption - Occupation (Greek)
        
        
        	

	

1. Click Update.

For all Master Files that require the Nationality and Occupation to 
 be entered in Greek, retrieve these two user fields and enter the information.

&nbsp;

&nbsp;

See also:

	

- [Local Address Card](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Local_Address_Card.htm)

	

- [User 
    	 Fields](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/User_Fields_(Configuration).htm)

&nbsp;

You are here:[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; [Additional Information](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Confidential_Database.htm) &gt; [Entity Administration](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Administrator/Change_Ownership_Structure.htm) &gt; Entering Information for Cyprus Forms

&nbsp;

(c) Viewpoint Software for 
 Business Ltd

Version: 8.0.2022.09.20


