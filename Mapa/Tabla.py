# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:25:03 2019

@author: jinnkay
"""

import pandas as pd
    
#%%
def exportar_tablas(df):
    writer = pd.ExcelWriter('Tablas/Tabla.xlsx' , engine='xlsxwriter')

    for i in range(len(df)):
        df[i].to_excel(writer , sheet_name = "Mapa_" + str(i) , index = False)
        print("Tabla de Mapa_" + str(i)+" Exportado")
      
    writer.save()    