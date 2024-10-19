[]()




# Security Master
The Security Master is where you maintain the records of all securities 
 that will be used in Viewpoint. Securities are globally defined for the 
 database and allows global updates and/or interface prices for portfolio 
 valuation. The Security Master can be accessed in the Entity Administration 
 and Accounting components. It is available in Viewpoint - Home screen. 
 To access it:

	

- Using Ribbon - Click EA Global Ribbon button, select Global 
    	 Change &gt; Security Master

	

- Using Section Menu - Click Home &gt; Entity Administration &gt; 
    	 Security Master

Data maintenance can be done in three ways:

	

- Manually;

	

- Via an Excel spreadsheet; or

	

- Using an interface to data providers, e.g. Reuters 
    	 Data Stream.

You can access the function through Viewpoint - Home screen whereby 
 you will first filter the listing by:

	

- Selecting the [status](javascript:TextPopup(this))
    
    	<div class="droptext" id="POPUP405544349" style="display: none;">
    		Active - Click this to view securities that are active.
    		Inactive - Click this to view inactive securities.
    		All - Click to view both active and inactive securities.
     </div>

	

- Specifying the search criteria

Once you have done that, you can click Apply to view all securities 
 that fulfil the search criteria.

&nbsp;

Filter

The filter applies to the security list.

&nbsp;

Select button

This allows for additional criteria to apply to the security list.

&nbsp;

Security list

This shows all the securities that have been set up.

&nbsp;

Command buttons

Click on the relevant command button to perform the necessary.

	

- <span class="hcp2">New</span> - Click this &nbsp;to 
    	 [add](javascript:TextPopup(this)) 
    	 new record to the Security Master.
    
    	<div class="droptext" id="POPUP405676541" style="display: none;">
    		
        			    1. Enter the details of the new security:
        		
    		
        			
            				    - 
        - <span class="hcp2">Code</span> - Enter 
            				 a unique code for the security. This field is mandatory.
            				    - 
        - <span class="hcp2">Security Type</span> 
            				 - Select the security type from the list which is maintained 
            				 in the Security Types [SECT] lookup table. This field 
            				 is mandatory.
            				    - 
        - Name <span class="hcp5">- 
            				 Enter the name of the security. This field is mandatory.</span>
            				    - 
        - Long Name<span class="hcp5"> 
            				 - Enter the name of the security in full. This field is 
            				 mandatory.</span>
            				    - 
        - Currency<span class="hcp5">&nbsp;- 
            				 Select the currency of the security.&nbsp;This field is 
            				 mandatory.</span>
            				    - 
        - Nominal Value<span class="hcp5"> 
            				 - Enter the nominal value of the security. This field 
            				 is mandatory.</span>
            				    - 
        - SEDOL Code<span class="hcp5"> 
            				 - Enter the Stock Exchange Daily Official List seven digit 
            				 identification code assigned to the security if it is 
            				 traded on the London Stock Exchange and other small exchanges 
            				 in the United Kingdom.</span>
            				    - 
        - ISIN Code<span class="hcp5"> 
            				 - Enter the International Securities Identification Number 
            				 for the security, if applicable.</span>
            				    - 
        - CUSIP Code<span class="hcp5"> 
            				 - Enter the Committee on Uniform Security Identification 
            				 Procedures nine-character alphanumeric code for the security, 
            				 if applicable. </span>
            				    - 
        - Data Vendor Code<span class="hcp5"> - This field can be used 
            				 to record the code of the data vendor used.</span>
            				    - 
        - Update Source<span class="hcp5"> 
            				 - Select the method of updating the security prices. This 
            				 list is maintained in the Update Source Securities [SUDS] 
            				 lookup table. The selection here does not have any functional 
            				 impact on the system. This field is mandatory.</span>
            				    - 
        - Last Price<span class="hcp5"> 
            				 - Enter the last published price for the security.</span>
            				    - 
        - Price Multiplier<span class="hcp5"> - Enter the price multiplier 
            				 if applicable. The retrieved security price either in 
            				 journal script or valuation, must be multiplied by the 
            				 Price Multiplier. For example, if the Last Price is EUR119.75 
            				 and the Price Multiplier is 0.01, the price that will 
            				 be retrieved is EUR119.75 x 0.01 = EUR1.1975.</span>
            				    - 
        - Date Last Price <span class="hcp5">- Enter the date when the 
            				 price was last updated.</span>
            				    - 
        - Valuation Method<span class="hcp5"> - Select the method of valuating 
            				 the security prices.</span>
            				    - 
        - Interest Percentage<span class="hcp5"> - This field is activated 
            				 if the valuation method selected in the Valuation Method 
            				 field in Interest/Coupon.</span>
            				    - 
        - Div./Unt Frequency<span class="hcp5"> - Select the frequency that 
            				 dividends or interest is paid on the security. This field 
            				 is for reference purpose only.</span>
            				    - 
        - Stockbroker<span class="hcp5"> 
            				 - Select the stock broker, if applicable.</span>
            				    - 
        - Category SCAT1<span class="hcp5"> 
            				 - Select the industry of the security. this list is maintained 
            				 in the [SCAT1] user table in Configuration.</span>
            				    - 
        - Category SCAT2<span class="hcp5"> 
            				 - Select an item. This list is maintained in the [SCAT2] 
            				 user table in Configuration.</span>
            				    - 
        - Nature of Business<span class="hcp5"> - Enter the nature of business 
            				 of the company issuing the security.</span>
            				    - 
        - <span class="hcp2">Note</span><span> 
            				 - Enter any additional information on the security.</span>
            			
        		
    		
        			    1. Click Update to save the information.
        		
    		<span style="font-weight: bold; font-style: italic;">Note</span>: 
    		 There are four checkbox fields that are available for recording 
    		 purposes only. By default, these are set to 'FIELD NOT USED [99]'.
     </div>

	

- <span class="hcp2">Edit</span> - Click this &nbsp;to 
    	 edit existing security record.

	

- <span class="hcp2">Delete</span> - Click this 
    	 &nbsp;to [delete](javascript:TextPopup(this)) 
    	 the selected record.
    
    	<div class="droptext" id="POPUP405563057" style="display: none;">
    		Click Yes to confirm the deletion.
     </div>

	

- <span class="hcp2">Deactivate/Re-activate</span> 
    	 - Click this &nbsp;to de-activate/re-activate a security.

	

- <span class="hcp2">Actions</span> - Click this 
    	 to [view/enter](javascript:TextPopup(this)) 
    	 corporate actions such as the issuance of dividends and bonus issues.
    
    	<div class="droptext" id="POPUP405551698" style="display: none;">
    		This opens a new screen.
    		&nbsp;
    		<h6 class="Heading8">From and to</h6>
    		Enter the period in these fields to look for actions recorded 
    		 within the period. If you leave these blank, then all actions 
    		 will be listed.
    		&nbsp;
    		<h6 class="Heading8">Refresh</h6>
    		Click to refresh the list.
    		&nbsp;
    		<h6 class="Heading8">New</h6>
    		Click to enter a new action:
    		
        			    - Action - Select the action.
        			    - Ex-Dividend Date – Enter the appropriate date.
        			    - Record date – Enter the appropriate date.
        			    - Pay date – Enter the date where payment is made. 
        			    - Rate - Enter the rate of exchange of the action. This 
        			 field is for recording purposes only.
        			    - Note - Enter the details of the action. For instance: 
        			 bonus issue of 2 shares for every 7 held.
        			    - Update - Click to update the record.
        			    - Cancel - Click to cancel the entry.
        		
    		&nbsp;
    		<h6 class="Heading8">Edit</h6>
    		Click to edit a record.
    		&nbsp;
    		<h6 class="Heading8">Delete</h6>
    		Click to delete a record.
    		&nbsp;
    		<h6 class="Heading8">Close</h6>
    		Click to close the screen.
     </div>

	

- <span class="hcp2">Price </span>- Click this to 
    	 redirect to the [Security 
    	 Price](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/Client_Accountant/Security_Prices.htm) screen of the selected security from the Security Master 
    	 screen.


 
&nbsp;

You are here:[Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Copyright_Notice.htm) &gt; [Viewpoint - Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Overview.htm) &gt; [Home](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Overview.htm) &gt; [Entity Administration](file:///c:/temp/0457b882-c844-4314-8878-ce1a9c2207bd/input/Address_Card_Maintenance.htm) &gt; Security Master

 
&nbsp;
 
(c) Viewpoint Software for 
 Business Ltd
 
Version: 8.0.2022.09.20




