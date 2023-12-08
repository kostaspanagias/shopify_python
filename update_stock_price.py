# -*- coding: utf-8 -*-
"""
Created on Thu May 25 10:36:21 2023

@author: Kostas Panagias
"""

import pandas as pd
import requests
import json

uploadfile = r'C:\materials_upload.xlsx' # Replace with the path of your file / See the sample file: sample_update_stock_price.xlsx


# Read the Excel file
df = pd.read_excel(uploadfile)

# Create a new DataFrame with only the columns you're interested in
update_df = df[['variant_id', 'inventory_item_id', 'inventory_Qty', 'price']]

store_url = "blablabla.myshopify.com"  # Replace with your store URL
access_token = 'blablabla' # Replace with your Access-Token
location_id = blablabla  # Replace with your location ID


for index, row in update_df.iterrows():
    variant_id = int(row['variant_id'])
    inventory_item_id = int(row['inventory_item_id'])
    inventory_quantity = int(row['inventory_Qty'])
    price = row['price']

    # Update the inventory
    data = {
        "location_id": location_id,
        "inventory_item_id": inventory_item_id,
        "available": inventory_quantity
    }
    response_inventory = requests.post(
        f'https://{store_url}/admin/api/2021-07/inventory_levels/set.json',
        headers={'X-Shopify-Access-Token': access_token, 'Content-Type': 'application/json'},
        data=json.dumps(data)
    )

    # Update the price
    data = {
        "variant": {
            "id": variant_id,
            "price": price
        }
    }
    response_price = requests.put(
        f'https://{store_url}/admin/api/2021-07/variants/{variant_id}.json',
        headers={'X-Shopify-Access-Token': access_token, 'Content-Type': 'application/json'},
        data=json.dumps(data)
    )

    # Check if the requests were successful
    if response_inventory.status_code != 200 or response_price.status_code != 200:
        print(f"Error updating variant {variant_id}: {response_inventory.content}, {response_price.content}")
