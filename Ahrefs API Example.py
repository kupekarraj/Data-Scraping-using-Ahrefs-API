#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Importing all the necessary libraries
import requests
import json
import pandas as pd
import schedule 
import time


# In[ ]:


#List of input domains
text=['blog.ahrefs.com','ahrefs.com']


# In[ ]:


#Creating a output dataframe to store all the results
output_data=pd.DataFrame(columns=["domain","domain_rating","backlinks","ref_domain","traffic"])


# In[ ]:


#defining a function to pull the metrics details for a domain
def metrics_details(element):
    response=requests.get("https://apiv2.ahrefs.com?from=metrics_extended&target=element&mode=domain&select=backlinks,refdomains&token=de424520b7b2e5a57f9fff6085e1071177ff9564").json()
    backlinks=response#['metrics']['backlinks']
    ref_domain=response#['metrics']['refdomains']
    return backlinks,ref_domain
    


# In[ ]:


#defining a function to pull the domain details for a domain
def domain_details(element):
    dr_response=requests.get("https://apiv2.ahrefs.com?from=domain_rating&target=element&mode=domain&select=domain_rating&token=de424520b7b2e5a57f9fff6085e1071177ff9564").json()
    domain_rating=dr_response#['domain']['domain_rating']
    return domain_rating


# In[ ]:


#defining a function to pull the traffic details for a domain
def traffic_details(element):
    traffic_response=requests.get("https://apiv2.ahrefs.com?from=positions_metrics&target=element&mode=domain&select=domain_rating&token=de424520b7b2e5a57f9fff6085e1071177ff9564").json()
    traffic=traffic_response#['positions_metrics']['traffic']
    return traffic


# In[ ]:


#looping through to fetch all the backlink, domain and metrics data for the input domains
for element in text:
    #collecting backlinks and referring domain metrics
    backlinks,ref_domain = metrics_details(element)
    
    #collecting domain rating for each fo the entries
    domain_rating = domain_details(element)
    
    #collecting traffic metrics
    traffic = traffic_details(element)
    
    #saving the data
    output_data=output_data.append({"domain":element,"domain_rating":domain_rating,"backlinks":backlinks,"ref_domain":ref_domain},ignore_index=True)
    
     


# In[ ]:


#displaying the top few outputs
output_data.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




