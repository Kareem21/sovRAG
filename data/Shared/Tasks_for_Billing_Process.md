



# Tasks for Billing Process
To reduce the possibility of inaccuracies during a billing process, it might be useful to incorporate some checks along the way. This can be done in Viewpoint by creating and assigning tasks to relevant administrators or managers for them to review and approve the relevant steps of the process.

These tasks can also contain follow-up tasks which are created upon completion or rejection of another task. For instance, you can have a Review Invoice task for an invoice with these follow-up tasks:

- 
    
    Approve Invoice task upon completion of the Review task.

- 
    
    Redo Invoice task when assignee rejects the Review task.


Below shows possible tasks that can be created for the process:

<table class="Table1" style="border-collapse: separate;" cellspacing="0px" width="100%" border="1">
<colgroup><col style="width: 19.139%;">
<col style="width: 38.134%;">
<col style="width: 42.727%;">
</colgroup><tbody><tr class="t1st">
<td class="hcp2">
Process
</td>
<td class="hcp2">
Explanation
</td>
<td class="hcp2">
Task
</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
Draft invoice is prepared by Finance Department.
</td>
<td class="t2Col" style="vertical-align: top;">
Draft invoice is generated in Document Queue and Review Invoice task assigned to Billing File Administrator to check the draft invoice.
&nbsp;
</td>
<td class="t1Col" style="vertical-align: top;">
Review Invoice task is to be added to the draft invoice. This can be done using the Add Task button or you can also use [Document Management Index tags](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Document_Manager/Document_Management_Tags.htm) to have the task added automatically.
</td>
</tr>
<tr class="t1Row">
<td class="t1Col" style="vertical-align: top;">
Billing File Administrator checks the draft invoice.
</td>
<td class="t2Col" style="vertical-align: top;">
Draft invoice file is reviewed by the Billing File Administrator who will:

- 
    Complete the Review Invoice task if it is correct, leading to Approve Invoice task; or

- 
    Reject the Review task if the draft invoice is incorrect, leading to Redo Invoice task.


</td>
<td class="t1Col" style="vertical-align: top;">

- 
    Approve Invoice task will be created automatically following the completion of Review Invoice task.

- 
    Redo Invoice task will be created automatically following the rejection of Review Invoice task.


</td>
</tr>
<tr class="t2Row">
<td class="t1Col" style="vertical-align: top;">
Billing File Manager approves the draft invoice.
</td>
<td class="t2Col" style="vertical-align: top;">
Billing File Manager to approve the draft invoice and:

- 
    Complete the Approve Invoice task; or

- 
    Reject the Approve Invoice task,


Either option will lead to Store Invoice task as both approved and rejected invoices are to be stored.
&nbsp;
</td>
<td class="t1Col" style="vertical-align: top;">
Store Invoice task will be created automatically following the completion or rejection of Approve Invoice task.
</td>
</tr>
</tbody></table>

&nbsp;

To set up the tasks above, you can run this localise script:

&nbsp;

CAPTION:Create tasks for billing process

// Review Invoice task

DTSKADD:20+INVREV=Review invoice

DTSKVAL:20+BtTagValues=[On_Complete.Codes=INVAPR]&lt;BR&gt;[On_Complete.Default=INVAPR]&lt;BR&gt;[On_Complete.Descr=Approve draft invoice]&lt;BR&gt;[On_Complete.Assign=SM]&lt;BR&gt;[On_Complete.Due=3]&lt;BR&gt;[On_Complete.Action.ConfirmDraft=VpDocId]&lt;BR&gt;[On_Reject.Codes=INVREDO]&lt;BR&gt;[On_Reject.Default=INVREDO]&lt;BR&gt;[On_Reject.Descr=Redo draft invoice]&lt;BR&gt;[On_Reject.Caption=Redo]&lt;BR&gt;[On_Reject.Assign=SM]&lt;BR&gt;[On_Reject.Due=3]&lt;BR&gt;[On_Reject.Complete=Y]

&nbsp;

// Approve Invoice task

DTSKADD:21+INVAPR=Approve invoice

DTSKVAL:21+BtTagValues=[On_Complete.Codes=INVFILE]&lt;BR&gt;[On_Complete.Default=INVFILE]&lt;BR&gt;[On_Complete.Descr=Store approved invoice]&lt;BR&gt;[On_Complete.Assign=SM]&lt;BR&gt;[On_Complete.Due=3]&lt;BR&gt;[On_Complete.Action.ConfirmDraft=VpDocId]&lt;BR&gt;[On_Reject.Codes=INVFILE]&lt;BR&gt;[On_Reject.Default=INVFILE]&lt;BR&gt;[On_Reject.Descr=Invoice not approved]&lt;BR&gt;[On_Reject.Caption=Reject]&lt;BR&gt;[On_Reject.Assign=SM]&lt;BR&gt;[On_Reject.Due=3]&lt;BR&gt;[On_Reject.Complete=Y]

&nbsp;

// Redo Draft Invoice task

DTSKADD:22+INVREDO=Redo draft invoice

&nbsp;

// Store Invoice task

DTSKADD:23+INVStore=Store invoice

&nbsp;

&nbsp;

See also:

- 
    
    [Localise](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Localise.htm)

- 
    
    [Tasks](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Configuration/Tasks_-_Configuration.htm)


&nbsp;

[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; Tasks for Billing Process

&nbsp;

(c) Viewpoint Software for 
 Business Ltd

Version: 8.0.2022.09.20


