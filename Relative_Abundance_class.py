# -*- coding: utf-8 -*-
"""
created by Patrick O'Hara

Used to determine relative Abundance of Geobacter, Shewanella, Desulfo, Methano,
Methylo and Verruc prefixed bacteria and archea at depth within samples taken 
from Second Creek, MN.

Input files should be generated by Mothur before hand and should be located 
within the same folder the python script/class are located.

Mothur files need to run program: .SHARED and .TAXONOMY
    
    files should be written as strings within the Relative_Abundance.py script with
    the .SHARED file set to object named Shared and .TAXONOMY file set to object
    named Tax.

Location Should be input as a string and assigned to object named location.

example files have been provided

locations are dependent on the Mothur files. locations associated with example
file are: C3,C4,C5,C6,W3,W4,W5,W6

Description of Functions:

tab_2_csv:
    used to generate csv files from tab delimited Mothur files. generates files
    that are the stored in the same folder as script/class
    
pull_OTUs:
    this function searches the taxonomy file for the bacteria/archea that are
    listed above. Once these bacteria/archea are found, they are added to a new
    file that only contains OTUs (operational taxonomic unit) that are specific
    to the bacteria/archea. The function then takes the lists of OTUs and
    compares them to the shared file to determine which locations have which
    bacteria/archea and at what relative concentrations. Finally, this function
    generates files that are specific to each type of bacteria/archea that 
    contain the number of sequences of each OTU for a given functional group 
    for each location.
    
set_location_depth:
    this function takes the messy location code and extracts the location name
    and depth of sample and generates new columns for use later.
    
plot_relative_abundace:
    this function takes each microbe location_depth file, adds all of the OTU
    abundances for each functional group individually, then divides this total 
    by all of the microbe sequences to aquire fractional abundance of each
    functional group (geobacter,shewan,desulfo,methano,methylo,verruc) at each
    depth for the given location. It then stacks the fraction of abundace in a
    bar chart displaying relative abundace across the depth of the sample.
    
"""

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Relative_Abundance:
    
    def __init__(self,shared_file,taxonomy_file,location):
        
        self.shared_file = shared_file
        self.taxonomy_file = taxonomy_file
        self.location = location
        
    def tab_2_csv(self):

        in_txt = csv.reader(open(self.shared_file, "rb"), delimiter = '\t')
        out_csv = csv.writer(open(self.shared_file+'.csv', 'wb'))

        out_csv.writerows(in_txt)

        in_txt = csv.reader(open(self.taxonomy_file, "rb"), delimiter = '\t')
        out_csv = csv.writer(open(self.taxonomy_file+'.csv', 'wb'))

        out_csv.writerows(in_txt)
        
    def pull_OTUs(self):
        
        OTUs = pd.read_csv(self.taxonomy_file+".csv", header = 0)
        OTUs = OTUs.rename(columns=lambda x: x.strip())
        OTUs = OTUs.rename(columns={'\xef\xbb\xbfOTU': 'OTU'})
        final_OTU =  int(len(OTUs.index))+3 #column within locations file 
                                    #of final available OTU w taxonomic
                                    #data

        locations = pd.read_csv(self.shared_file+".csv", header = 0)
        locations = locations.rename(columns=lambda x: x.strip())
        locations = locations.iloc[:,1:final_OTU]
        locations = locations.drop('numOtus',axis=1)
        final_OTU = final_OTU-2 #removed two columns at begining of locations file

        geobacter = OTUs[OTUs['Taxonomy'].str.contains("Geobacter")]
        geobacter = geobacter.iloc[:,[0]]
        geobacter['OTU'] = geobacter['OTU'].map(lambda x: x.lstrip('Otu'))
        geobacter['OTU'] = geobacter['OTU'].astype(str).astype(int)
        geobacter = geobacter.reset_index(drop=True)

        i = 0

        last_tax_ind = int(len(geobacter.index))-1
        geobacter_loc= locations.iloc[:,[0]]

        while i <= last_tax_ind:
            geobacter_loc['OTU'+str(geobacter.iloc[i]['OTU'])] = locations.iloc[:,[i+1]]
            i += 1
        geobacter_loc = geobacter_loc.iloc[0:45,:]
        geobacter_loc.to_csv('geobacter_loc.csv')        
    
        shewan = OTUs[OTUs['Taxonomy'].str.contains("Shewan")]
        shewan = shewan.iloc[:,[0]]
        shewan['OTU'] = shewan['OTU'].map(lambda x: x.lstrip('Otu'))
        shewan['OTU'] = shewan['OTU'].astype(str).astype(int)
        shewan = shewan.reset_index(drop=True)

        i = 0

        last_tax_ind = int(len(shewan.index))-1
        shewan_loc= locations.iloc[:,[0]]

        while i <= last_tax_ind:
            shewan_loc['OTU'+str(shewan.iloc[i]['OTU'])] = locations.iloc[:,[i+1]]
            i += 1
        shewan_loc = shewan_loc.iloc[0:45,:]
        shewan_loc.to_csv('shewan_loc.csv') 

        desulfo = OTUs[OTUs['Taxonomy'].str.contains("Desulfo")]
        desulfo = desulfo.iloc[:,[0]]
        desulfo['OTU'] = desulfo['OTU'].map(lambda x: x.lstrip('Otu'))
        desulfo['OTU'] = desulfo['OTU'].astype(str).astype(int)
        desulfo = desulfo.reset_index(drop=True)

        i = 0

        last_tax_ind = int(len(desulfo.index))-1
        desulfo_loc= locations.iloc[:,[0]]

        while i <= last_tax_ind:
            desulfo_loc['OTU'+str(desulfo.iloc[i]['OTU'])] = locations.iloc[:,[i+1]]
            i += 1
        desulfo_loc = desulfo_loc.iloc[0:45,:]
        desulfo_loc.to_csv('desulfo_loc.csv') 

        methano = OTUs[OTUs['Taxonomy'].str.contains("Methano")]
        methano = methano.iloc[:,[0]]
        methano['OTU'] = methano['OTU'].map(lambda x: x.lstrip('Otu'))
        methano['OTU'] = methano['OTU'].astype(str).astype(int)
        methano = methano.reset_index(drop=True)

        i = 0

        last_tax_ind = int(len(methano.index))-1
        methano_loc= locations.iloc[:,[0]]

        while i <= last_tax_ind:
            methano_loc['OTU'+str(methano.iloc[i]['OTU'])] = locations.iloc[:,[i+1]]
            i += 1
        methano_loc = methano_loc.iloc[0:45,:]
        methano_loc.to_csv('methano_loc.csv')

        methylo = OTUs[OTUs['Taxonomy'].str.contains("Methylo")]
        methylo = methylo.iloc[:,[0]]
        methylo['OTU'] = methylo['OTU'].map(lambda x: x.lstrip('Otu'))
        methylo['OTU'] = methylo['OTU'].astype(str).astype(int)
        methylo = methylo.reset_index(drop=True)

        i = 0

        last_tax_ind = int(len(methylo.index))-1
        methylo_loc= locations.iloc[:,[0]]

        while i <= last_tax_ind:
            methylo_loc['OTU'+str(methylo.iloc[i]['OTU'])] = locations.iloc[:,[i+1]]
            i += 1
        methylo_loc = methylo_loc.iloc[0:45,:]
        methylo_loc.to_csv('methylo_loc.csv')

        verruc = OTUs[OTUs['Taxonomy'].str.contains("Verrucomicrobiae")]
        verruc = verruc.iloc[:,[0]]
        verruc['OTU'] = verruc['OTU'].map(lambda x: x.lstrip('Otu'))
        verruc['OTU'] = verruc['OTU'].astype(str).astype(int)
        verruc = verruc.reset_index(drop=True)

        i = 0

        last_tax_ind = int(len(verruc.index))-1
        verruc_loc= locations.iloc[:,[0]]

        while i <= last_tax_ind:
            verruc_loc['OTU'+str(verruc.iloc[i]['OTU'])] = locations.iloc[:,[i+1]]
            i += 1
        verruc_loc = verruc_loc.iloc[0:45,:]
        verruc_loc.to_csv('verruc_loc.csv')
        
    def set_location_depth(self):
        
        geobacter_loc = pd.read_csv("geobacter_loc.csv", header = 0)
        geobacter_loc = geobacter_loc.rename(columns=lambda x: x.strip())
        geobacter_loc_depth = geobacter_loc.iloc[:,[1]]
        geobacter_loc_depth['Location'] = geobacter_loc_depth['Group'].astype(str).str[3:5]
        geobacter_loc_depth['Depth (cm)'] = geobacter_loc_depth['Group'].astype(str).str[5:7]
        geobacter_loc_depth= geobacter_loc_depth.iloc[:,1:]
        geobacter_loc_depth= geobacter_loc_depth.join(geobacter_loc.iloc[:,2:])
        geobacter_loc_depth.to_csv('geobacter_loc_depth.csv')

        shewan_loc = pd.read_csv("shewan_loc.csv", header = 0)
        shewan_loc = shewan_loc.rename(columns=lambda x: x.strip())
        shewan_loc_depth = shewan_loc.iloc[:,[1]]
        shewan_loc_depth['Location'] = shewan_loc_depth['Group'].astype(str).str[3:5]
        shewan_loc_depth['Depth (cm)'] = shewan_loc_depth['Group'].astype(str).str[5:7]
        shewan_loc_depth= shewan_loc_depth.iloc[:,1:]
        shewan_loc_depth= shewan_loc_depth.join(shewan_loc.iloc[:,2:])
        shewan_loc_depth.to_csv('shewan_loc_depth.csv')

        desulfo_loc = pd.read_csv("desulfo_loc.csv", header = 0)
        desulfo_loc = desulfo_loc.rename(columns=lambda x: x.strip())
        desulfo_loc_depth = desulfo_loc.iloc[:,[1]]
        desulfo_loc_depth['Location'] = desulfo_loc_depth['Group'].astype(str).str[3:5]
        desulfo_loc_depth['Depth (cm)'] = desulfo_loc_depth['Group'].astype(str).str[5:7]
        desulfo_loc_depth= desulfo_loc_depth.iloc[:,1:]
        desulfo_loc_depth= desulfo_loc_depth.join(desulfo_loc.iloc[:,2:])
        desulfo_loc_depth.to_csv('desulfo_loc_depth.csv')
        
        methano_loc = pd.read_csv("methano_loc.csv", header = 0)
        methano_loc = methano_loc.rename(columns=lambda x: x.strip())
        methano_loc_depth = methano_loc.iloc[:,[1]]
        methano_loc_depth['Location'] = methano_loc_depth['Group'].astype(str).str[3:5]
        methano_loc_depth['Depth (cm)'] = methano_loc_depth['Group'].astype(str).str[5:7]
        methano_loc_depth= methano_loc_depth.iloc[:,1:]
        methano_loc_depth= methano_loc_depth.join(methano_loc.iloc[:,2:])
        methano_loc_depth.to_csv('methano_loc_depth.csv')
        
        methylo_loc = pd.read_csv("methylo_loc.csv", header = 0)
        methylo_loc = methylo_loc.rename(columns=lambda x: x.strip())
        methylo_loc_depth = methylo_loc.iloc[:,[1]]
        methylo_loc_depth['Location'] = methylo_loc_depth['Group'].astype(str).str[3:5]
        methylo_loc_depth['Depth (cm)'] = methylo_loc_depth['Group'].astype(str).str[5:7]
        methylo_loc_depth= methylo_loc_depth.iloc[:,1:]
        methylo_loc_depth= methylo_loc_depth.join(methylo_loc.iloc[:,2:])
        methylo_loc_depth.to_csv('methylo_loc_depth.csv')
        
        verruc_loc = pd.read_csv("verruc_loc.csv", header = 0)
        verruc_loc = verruc_loc.rename(columns=lambda x: x.strip())
        verruc_loc_depth = verruc_loc.iloc[:,[1]]
        verruc_loc_depth['Location'] = verruc_loc_depth['Group'].astype(str).str[3:5]
        verruc_loc_depth['Depth (cm)'] = verruc_loc_depth['Group'].astype(str).str[5:7]
        verruc_loc_depth= verruc_loc_depth.iloc[:,1:]
        verruc_loc_depth= verruc_loc_depth.join(verruc_loc.iloc[:,2:])
        verruc_loc_depth.to_csv('verruc_loc_depth.csv')
        
    def plot_relative_abundance(self):
        
        geobacter_loc_depth = pd.read_csv("geobacter_loc_depth.csv", header = 0)
        geobacter_loc_depth = geobacter_loc_depth.rename(columns=lambda x: x.strip())
        geobacter_loc_depth = geobacter_loc_depth[(geobacter_loc_depth['Location']==self.location)]
        geobacter_sum = geobacter_loc_depth.iloc[:,3:]
        geobacter_sum["sum"] = geobacter_sum.sum(axis=1)
        #geobacter_sum = geobacter_sum.reset_index(drop=True)
        
        
        shewan_loc_depth = pd.read_csv("shewan_loc_depth.csv", header = 0)
        shewan_loc_depth = shewan_loc_depth.rename(columns=lambda x: x.strip())
        shewan_loc_depth = shewan_loc_depth[(shewan_loc_depth['Location']==self.location)]
        shewan_sum = shewan_loc_depth.iloc[:,3:]
        shewan_sum["sum"] = shewan_sum.sum(axis=1)
        #shewan_sum = geobacter_sum.reset_index(drop=True)
        
        
        desulfo_loc_depth = pd.read_csv("desulfo_loc_depth.csv", header = 0)
        desulfo_loc_depth = desulfo_loc_depth.rename(columns=lambda x: x.strip())
        desulfo_loc_depth = desulfo_loc_depth[(desulfo_loc_depth['Location']==self.location)]
        desulfo_sum = desulfo_loc_depth.iloc[:,3:]
        desulfo_sum["sum"] = desulfo_sum.sum(axis=1)
        #desulfo_sum = geobacter_sum.reset_index(drop=True)
        
        
        methano_loc_depth = pd.read_csv("methano_loc_depth.csv", header = 0)
        methano_loc_depth = methano_loc_depth.rename(columns=lambda x: x.strip())
        methano_loc_depth = methano_loc_depth[(methano_loc_depth['Location']==self.location)]
        methano_sum = methano_loc_depth.iloc[:,3:]
        methano_sum["sum"] = methano_sum.sum(axis=1)
        #methano_sum = geobacter_sum.reset_index(drop=True)
        
        
        methylo_loc_depth = pd.read_csv("methylo_loc_depth.csv", header = 0)
        methylo_loc_depth = methylo_loc_depth.rename(columns=lambda x: x.strip())
        methylo_loc_depth = methylo_loc_depth[(methylo_loc_depth['Location']==self.location)]
        methylo_sum = methylo_loc_depth.iloc[:,3:]
        methylo_sum["sum"] = methylo_sum.sum(axis=1)
        #methylo_sum = geobacter_sum.reset_index(drop=True)
        
        
        verruc_loc_depth = pd.read_csv("verruc_loc_depth.csv", header = 0)
        verruc_loc_depth = verruc_loc_depth.rename(columns=lambda x: x.strip())
        verruc_loc_depth = verruc_loc_depth[(verruc_loc_depth['Location']==self.location)]
        verruc_sum = verruc_loc_depth.iloc[:,3:]
        verruc_sum["sum"] = verruc_sum.sum(axis=1)
        #verruc_sum = geobacter_sum.reset_index(drop=True)
        
        
        location_sum = geobacter_loc_depth.iloc[:,1:3]
        location_sum['geobacter'] = geobacter_sum['sum']
        location_sum['shewan'] = shewan_sum['sum']
        location_sum['desulfo'] = desulfo_sum['sum']
        location_sum['methano'] = methano_sum['sum']
        location_sum['methylo'] = methylo_sum['sum']
        location_sum['verruc'] = verruc_sum['sum']
        part_time_loc_sum = location_sum
        part_time_loc_sum = part_time_loc_sum.iloc[:,2:]
        location_sum["total"] = part_time_loc_sum.sum(axis=1)
        
        location_sum['geobact_frac'] = location_sum['geobacter']/location_sum['total']
        location_sum['shewn_frac'] = location_sum['shewan']/location_sum['total']
        location_sum['desulfo_frac'] = location_sum['desulfo']/location_sum['total']
        location_sum['methano_frac'] = location_sum['methano']/location_sum['total']
        location_sum['methylo_frac'] = location_sum['methylo']/location_sum['total']
        location_sum['verruc_frac'] = location_sum['verruc']/location_sum['total']
        location_sum = location_sum.reset_index(drop=True)
        
        N = int(len(location_sum.index))
        
        ind = np.arange(N)
        width = 0.5
        plt.style.use('dark_background')
        
        p1 = plt.bar(ind,location_sum.iloc[:,9],width,color='#966FD6')
        p2 = plt.bar(ind,location_sum.iloc[:,10],width,color='#779ECB',bottom=location_sum.iloc[:,9])
        p3 = plt.bar(ind,location_sum.iloc[:,11],width,color='#FDFD96',bottom=location_sum.iloc[:,9]+location_sum.iloc[:,10])
        p4 = plt.bar(ind,location_sum.iloc[:,12],width,color='#FF6961',bottom=location_sum.iloc[:,9]+location_sum.iloc[:,10]+location_sum.iloc[:,11])
        p5 = plt.bar(ind,location_sum.iloc[:,13],width,color='#FFB347',bottom=location_sum.iloc[:,9]+location_sum.iloc[:,10]+location_sum.iloc[:,11]+location_sum.iloc[:,12])
        p6 = plt.bar(ind,location_sum.iloc[:,14],width,color='#77DD77',bottom=location_sum.iloc[:,9]+location_sum.iloc[:,10]+location_sum.iloc[:,11]+location_sum.iloc[:,12]+location_sum.iloc[:,13])
        
        plt.ylabel('Fraction of Abundance')
        plt.title(self.location+" Relative Abundance at Depth")
        plt.xticks(ind,(location_sum.iloc[:,1]))
        plt.xlabel('Depth (cm)')
        (plt.legend((p1[0],p2[0],p3[0],p4[0],p5[0],p6[0]),('geobacter','shewan','desulfo',
        'methano','methylo','verruc'),bbox_to_anchor=(1.01,1),loc=2))
        
        plt.show()