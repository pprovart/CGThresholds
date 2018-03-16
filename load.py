import urllib2
import Tkinter as tk
import sys
import ttk
import requests

this = sys.modules[__name__]
this.msg = " "

def plugin_start():
    	print ('CGPlugin Starting')
	return ('CGThresholds')

def plugin_end():
    print('Closing')


def journal_entry(cmdr, is_beta, system, station, entry, state):
	#print ('Starting Journal')
	if entry['event'] == 'CommunityGoal':
		#print ('CG updating')		
		for goal in entry['CurrentGoals']:
	
			if not goal['IsComplete']: #v0.2Collect Active CG only
				"""
  			 	First Extract CG Data
 				"""
   				communitygoalID = goal['CGID']
				communitygoalName = goal['Title']
        			contributionsTotal= goal['CurrentTotal']
        			contributorsNum = goal['NumContributors']
        			contribution = goal['PlayerContribution']
        			percentileBand = goal['PlayerPercentileBand']
				#print ('CG Variables Calculated')
				"""
  				 Build the Data Set to Submit, based on the Entry field number from the form.
 				"""
				form_data = {
					'entry.1465819909' : communitygoalID,
					'entry.2023048714' : communitygoalName,
        				'entry.617265888' : contributionsTotal,
       					'entry.1469183421' : contributorsNum,
        				'entry.2011125544' : contribution,
        				'entry.1759162752' : percentileBand
        				}
				url = "https://docs.google.com/forms/d/e/1FAIpQLScJHvd9MNKMMNGpjZtlcT74u6Wnhcgesqz38a8JWBC94Se2Dg/formResponse"
				"""
  			 	Request URl as a POST with the Form URL plus send the Form Data to each entry.
 				"""
				try:				
					r = requests.post(url, data=form_data)
    					if r.status_code == 200:
        					#print ('URL Success')
						this.msg = 'CG Post Success'
    					else:
						print ('URL Fail' + str(r.status_code))
						this.msg = 'CG Post Failed'
				except:
					this.msg = 'CG Post Exception'
	return (this.msg)
