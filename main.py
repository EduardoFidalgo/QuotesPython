#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import pandas as pd
from datetime import datetime
import time 

while True:
    requisition = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisition_dic = requisition.json()
    dollar_quote = requisition_dic["USDBRL"]["bid"]
    euro_quote = requisition_dic["EURBRL"]["bid"]
    btc_quote = requisition_dic["BTCBRL"]["bid"]

    table = pd.read_excel("quotes.xlsx")
    table.loc[0, "Cotação"] = float(dollar_quote)
    table.loc[1, "Cotação"] = float(euro_quote)
    table.loc[2, "Cotação"] = float(btc_quote) * 1000
    table.loc[0, "Data Última Atualização"] = datetime.now()

    table.to_excel("quotes.xlsx", index=False)
    print(f"Cotação Atualizada. {datetime.now()}")

    time.sleep(60)
# In[ ]:




