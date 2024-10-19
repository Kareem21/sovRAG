



# Confidential Database
Confidential database refers to the ability to encrypt sensitive information 
 in Viewpoint. It is essentially a separate database that contains the 
 true values of the fields for an encrypted Master File or Address Cards. 
 These values will be replaced by encrypted tags in the Viewpoint database. 
 Thus, for users without access to the confidential database, they will 
 only see meaningless tags instead of the actual information when they 
 view the Master File or Address Card.

Setting up of Confidential Database is done in ViewPointDbMgt.exe.

&nbsp;
## Connecting to Confidential Database
The confidential database needs to be set up before Master Files and 
 Address Cards can be encrypted. For users to be able to view the actual 
 value, the user must be connected to the confidential database and have 
 access to the encrypted Master File and Address Card.

To connect to confidential database, do the following:

	

1. In Viewpoint, go to [User Options](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/User_Options.htm).

	

1. Select the Confidential Database tab.

	

1. Select the confidential database to connect. If more than one 
    	 confidential database has been set up, you will see multiple options 
    	 in the Connect to Confidential Data field.

	

1. Click OK.

&nbsp;
## Disconnecting from Confidential Database

	

1. In Viewpoint, go to [User Options](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/User_Options.htm).

	

1. Select the Confidential Database tab.

	

1. Select the option 'Disconnect [DISCN]' in the Connect to Confidential 
    	 Data field.

	

1. Click OK.

&nbsp;
## Encrypting a Master File
When confidential database has been set up, you can choose to encrypt 
 a Master File by doing the following:

	

1. Connect to the confidential database.

	

1. Select and open the File Maintenance screen of the Master File 
    	 you wish to encrypt.

	

1. Go to [Setup](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/MF_-_Setup.htm).

	

1. Tick the option Confidential Master File.

	

1. Click Update.

When encrypting a Master File, by default, access to the encrypted Master 
 File will be given to users in the same User Group as the user who encrypted 
 the Master File. If access is to be given to other users, click Access.

To undo the encryption, untick the Confidential Master File option in 
 Setup screen.

&nbsp;
## Encrypting an Address Card
Encrypting an Address Card is done by ticking the Encrypt option in 
 [Edit/New Address](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Address_-_Edit_New_Address.htm) while being 
 connected to the confidential database. When encrypting the Address Card, 
 by default, access to the encrypted Address Card will be given to users 
 in the same User Group as the user who encrypted the Address Card. If 
 access is to be given to other users, click Access in Edit/New Address.

To undo the encryption, untick the option.

&nbsp;

&nbsp;
## Translating Word and Excel Reports
Details for encrypted Master Files and Address Cards in Word and Excel 
 reports require translation to have the tags replaced by actual information.

	

1. Ensure you are connected to the confidential database.

	

1. In Microsoft Word or Excel, go to Viewpoint add-ins.

	

1. Click Translate Confidential Tags.

&nbsp;
## Translating XML Reports
<span lang="EN-GB" xml:lang="EN-GB">Encrypted details for reports in 
 XML viewer require translation similar to Word and Excel Reports.</span>

	

1. Ensure you are connected to the confidential database.

	

1. <span lang="EN-GB" xml:lang="EN-GB">In XML Viewer of the generated/previewed 
    	 report, click Translate Confidential Tags.</span>

&nbsp;
## File Review in Confidential Database
The File Review feature applies also to encrypted Master Files and Address 
 Cards. This requires the user performing the file review to be connected 
 to the confidential database during the review and the user must have 
 access to the encrypted Master File and Address Card. Otherwise, the result 
 will be a warning message to inform user that there is no access to the 
 confidential data.

&nbsp;

&nbsp;

See also:

	

- [Add-ins](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Document_Manager/Add-ins.htm)

	

- [User Options](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/User_Options.htm)

&nbsp;

&nbsp;

You are here:[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; [Additional Information]() &gt; [General]() &gt; Confidential Database

&nbsp;

(c) Viewpoint Software for 
 Business Ltd

Version: 8.0.2022.09.20


