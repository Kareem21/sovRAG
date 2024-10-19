



# Master Configuration Environment (MCE) and Data Replication
Setting up a Master Configuration Environment (MCE) allows for sharing of settings and Master Files from one environment to other environments known as Subscriber environments. It differs from the use of Import/Export Settings because it allows for Master Files and different settings to be maintained in Master Configuration Environment while specific Master Files, Address Cards and relevant settings are replicated to the subscriber environments automatically using Task Scheduler and Notification Agent.

This means that:

- 
    
    there is only one MCE with Task Scheduler and Notification Agent configured and running

- 
    
    there can be multiple subscriber environments with Task Scheduler and Notification Agent configured and running


&nbsp;
## Replicating Items from MCE in Subscriber Environments
The items that can be replicated include settings, templates and Master Files where:

- 
    
    if the item can apply to both MCE and the subscriber environment, these will be maintained in the MCE. For example, lookup table values, user table values, task types, Form Library templates, etc. For Master Files, if the Master File is a Global Master File in the MCE, it will be non-editable in the subscriber environment.

- 
    
    if the item requires different configuration for MCE and the subscriber environment, these are to be added as values to the Localise Scripts [LCLS] lookup table where you are effectively defining the configuration as localise scripts. For example, the configuration for the relationship type 'Director [DIR]'.


The replication requires the Replication job types in Task Scheduler and Notification Agent which will export the items from the MCE as .xml files to a repository known as the Landing Area. The Landing Area, this must be a location that can be accessed by the MCE and the subscriber environments; and for the users setting up the replication jobs, they must have the authority 'Allow Access to API Call' in [User Group - Authorities](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/User_Group_-_Authorities.htm).

This allows for the following to take place:

- 
    
    Replication - Export [REEX] job performed in MCE where:

- 
        
    - 
        
        Two folders - NEW and BACKUP are first created in the Landing Area.
        
        
    - 
        
        Within the NEW folder, a sub-folder for the first subscriber group is created and export for this subscriber group occurs so the relevant .xml files are created. This is then repeated for other subscriber groups.
        
        
    - 
        
        After all the .xml files containing the exported information have been created, the NEW folder is renamed to USE.
        
        
    - 
        
        The BACKUP folder will remain empty until a second export job is performed - if successful, the subscriber group folders and their .xml files will be moved to the BACKUP folder and the USE folder will now have new .xml files.
        
        
    - 
        
        If information for any of the subscriber group could not be exported, the export job is considered to have failed.
        
        
    

- 
    
    Replication - Import [REIM] job performed in subscriber environments where:

- 
        
    - 
        
        .xml files contained in a subscriber group folder inside the USE folder will be applied to the subscriber environments and localise scripts contained within the [Localise Scripts [LCLS] lookup table](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Lookup_Tables.htm) will be run.
        
        
    - 
        
        If any of the .xml files for a subscriber group could not be applied, the import job is considered to have failed.
        
        
    


<span style="font-weight: bold; font-style: italic;">Note</span>: For Master Files &nbsp;and Address Cards that are replicated, if these are converted to Global Master File and Global Address Cards, they are non-editable in the subscriber environments. If not converted to Global Master File/Global Address Card, then it is possible to update in the subscriber environments. Refer to [Setup](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/MF_-_Setup.htm) and [Edit/New Address](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Address_-_Edit_New_Address.htm).

&nbsp;
## Required Configuration for Data Replication
To start using Data Replication for MCE and subscriber environments, you must make sure to define the MCE and subscriber environments.
### &nbsp;
### Setting up Master Configuration Environment (MCE)
The Viewpoint environment that is to be the MCE requires the following:

- 
    
    In Configuration &gt; Settings &gt; System Defaults &gt; Configuration Management, the 'Set as Master Configuration database' must be ticked.

- 
    
    In Configuration &gt; Business Parameters &gt; Task Scheduler &gt; Agent Job Scheduler, set up [Replication - Export [REEX]](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Task_Scheduler/Replication_Jobs.htm) job type - this will create .xml files that will be placed in relevant folders in the Landing Area folder.


In this environment, ensure that it contains all configurations, common Master Files and Address Cards that you want to export to the subscriber environments:

- 
    
    Subscriber Groups - This is used to identify what is to be applied to the subscriber and must be set up in the MCE in the Replication Subscriber [RPSB] lookup table.

- 
    
    Settings - This includes all values in the respective location e.g. lookup table values in the relevant lookup table.

- 
    
    Master File - This can be Master Files that have been converted to Global Master File or not.

- 
    
    Address Card - This can be Address Cards that have converted to Global Address Card or not.


&nbsp;
### Setting up Subscriber Environment
For a subscriber environment, do the following:

- 
    
    In Configuration &gt; Settings &gt; System Defaults &gt; Configuration Management,ensure the ‘Set as Master Configuration Database’ option is NOT ticked. Instead, specify the subscriber group(s) for the environment by entering the code of the group in the Subscriber Groups field. For multiple groups, separate each code with a semi-colon e.g. GEN;EUR.

- 
    
    To have the system generate a log file after an import job, tick the ‘Generate Replication Log File’ option. If you untick this option, then no log file will be generated.

- 
    
    In Configuration &gt; Business Parameters &gt; Task Scheduler &gt; Agent Job Scheduler, set up [Replication - Export [REIM]](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Task_Scheduler/Replication_Jobs.htm) job type.


&nbsp;

See also:

- 
    
    [Task Scheduler and Notification Agent](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Task_Scheduler/Task_Scheduler.htm)

- 
    
    [Localise](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Localise.htm)


&nbsp;

You are here:[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; [Additional Information](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Confidential_Database.htm) &gt; [General](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Confidential_Database.htm) &gt; Master Configuration Environment and Data Replication

&nbsp;

(c) Viewpoint Software for 
 Business Ltd

Version: 8.0.2022.09.20


