




# Tax Batching
Accounting journals involving Type W (Tax Account) sub-ledgers can be linked to a Filing in General or Entity Administration modules and batch them according to tax period of when the transactions were reported in. Accounting transactions can be moved in or out of the batch to an earlier or later Filing date, as long as the Filing is active.

The ‘Batch Assign’ screen can be launched from the <span class="hcp1">Batch Maintenance</span> button in the Filings section of the [Filings](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Filings.htm) screen in General or Entity Administration module.

This screen allows user to:

- 
    
    Assign and unassign Accounting journals to a Filing instance from the General or Entity Administration module.

- 
    
    Review Accounting journals added to the Filing instance.


<span class="hcp3">Note</span>: This feature requires Client Accounting licence.

&nbsp;
## Batch Assign Screen
This screen consists of Filter pane, Records pane and Summary pane.

&nbsp;

Filter Pane

- 
    
    <span class="hcp1">Filing</span> - This search box allows user to select the active Filings. The value defaults to the Filing that is selected in the General/Entity Administration screen. When this is updated, the ‘From Date’ and ‘To Date’ will be updated as well.

- 
    
    <span class="hcp1">From Date</span> - This allows the user to enter the ‘from’ date to load the Journal list. The value defaults to the ‘From’ date of the Filing that is selected. When the ‘Filing’ filter is updated, this will be updated according to the date range of the selected Filing.

- 
    
    <span class="hcp1">To Date</span> - This allows the user to enter the ‘to’ date to load the Journal list. The value defaults to the ‘To’ date of the Filing that is selected. When the ‘Filing’ filter is updated, this will be updated according to the date range of the selected Filing.

- 
    
    <span class="hcp1">Journal Type</span> - User can select either ‘Draft’, ‘Posted’ or ‘Draft and Posted’ to load the Journal list.

- 
    
    <span class="hcp1">Show</span> - User can select either ‘Assigned’, ‘Not Assigned’ or ‘All’ to load the Journal list.

- 
    
    <span class="hcp1">Refresh</span> - Click this button to refresh the Records pane and Summary pane each time the filter is updated.


&nbsp;

Records Pane

The Records pane is divided into upper grid and bottom grid.

The upper grid displays the list of Journals that met the filter’s criteria and the Tax Account sub-ledger codes that are configured in the Filing ‘Reference’ field .

By default, the first column shows the ‘Batch’ number. For example, if the Filing Sub Type is assigned to ‘Batch=2’ in the lookup table ‘Filing Sub Type [FLTS]’, the Batch column will display as 'Batch 2'.

The assigned Filing number for each Journal is displayed in this column. The zero value ‘0’ indicates that the Journal is not assigned to any Filing instance.

There are four buttons in the upper grid:

- 
    
    <span class="hcp1">Select All</span> - Click this to select all records in the grid.

- 
    
    <span class="hcp1">Deselect All</span> - Click this to deselect all records in the grid.

- 
    
    <span class="hcp1">Assign</span> - Click this to [assign Filing instance](javascript:TextPopup(this)) to the selected Journal(s).
    
    <div class="droptext" id="POPUP582710735" style="display: none;">
    
    The Journal(s) will be assigned to the Filing instance as selected in the ‘Filing’ at the Filter pane.
    
    It is possible to include transactions from the previous period to the current period by changing the dates for retrieval (‘From Date’ and ‘To Date’ at the Filter pane) and assign the transaction to the correct batch.
    
    Warning message will be prompted if the user:
        
    - 
        
        assigns a Journal that is assigned to another Filing.
        
    - 
        
        assigns a Journal that is outside of the Filing date range.
        
    
    </div>

- 
    
    <span class="hcp1">Undo Assign</span> - Click this to[ unassign Filing instance](javascript:TextPopup(this)) from the selected Journal(s). Filing number will become ‘0’ upon unassigned.
    
    <div class="droptext" id="POPUP582914954" style="display: none;">
    
    Warning message will be prompted if the user:
        
    - 
        
        unassigns a Journal that is within the Filing date range.
        
    
    </div>

The bottom grid displays the Journal lines of the selected Journal in upper grid.

<span class="hcp3">Note</span>: When the tax is zero percentage (0 %), the journal lines will be displayed as 0.0% in this grid.

&nbsp;

Summary Pane

The Summary pane shows the Account code movement details. When user assigns or unassigns the Journals, the amount for the tax account will be updated accordingly. However, user is required to click the Refresh button to load the updated amount in this pane.

The amount is displayed according to:

- 
    
    Included in Batch &lt;Filing number&gt; - this shows the total amount that belongs to the selected filing number.

- 
    
    Other Batch(es) - this shows the total amount that does not belong to the selected filing number and is assigned to other filing number(s). This section is hidden when there is no journal assigned to other tax filing number within the same batch.

- 
    
    Unassigned – this shows the total amount that does not belong to any filing number.


<span class="hcp3">Note</span>: The ‘Included in Batch &lt;Filing number&gt;’ amounts are the same as in the Sub-ledger Analyses in File Maintenance &gt; Accounting &gt; Journals &gt; Tax Account.

&nbsp;

&nbsp;

You are here:[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; [Additional Information](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Confidential_Database.htm) &gt; [Accounting](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Client_Accountant/Account_Settlement.htm) &gt; Tax Batching

&nbsp;

(c) Viewpoint Software for 
 Business Ltd

Version: 8.0.2022.09.20




