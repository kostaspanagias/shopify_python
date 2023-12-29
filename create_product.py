# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 20:57:20 2023

@author: kpanagias
"""

import requests
import json
import pandas as pd

# read the Excel file
newproducts = r'C:\new_products.xlsx' # Replace with the path of your file / See the sample file: new_products_template.xlsx

df = pd.read_excel(newproducts, converters={'barcode':str, 'sku':str})

store_url = "blablablab.myshopify.com"  # Replace with your store URL
access_token = 'blablabla' # Replace with your Access-Token

headers = {
    'X-Shopify-Access-Token': access_token,
    'Content-Type': 'application/json'
}

for index, row in df.iterrows():
    product_data = {
        "product": {
            "title": row['product_name'],
            "vendor": row['vendor'],
            "product_type": row['product_type'],
            "status": row['status'],
            "variants": [
                {
                    "barcode": str(row['barcode']),
                    "sku": str(row['sku']),
                    "title": row['variant_name'],
                    "inventory_quantity": row['inventory_Qty'],
                    "price": str(row['price']),
                    "inventory_management": "shopify"
                }
            ]
        }
    }

    response = requests.post(
        f'https://{store_url}/admin/api/2023-04/products.json',
        headers=headers,
        data=json.dumps(product_data)
    )

    # Check if the request was successful
    if response.status_code != 201:
        print(f"Error occurred: {response.content}")
    else:
        print(f"Product created successfully: {response.json()}")
        

