# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 02:50:26 2023

@author: kpanagias
"""

import requests
import json


def status_update(product_id, status):
    store_url = "blablabla.myshopify.com"  # Replace with your store URL
    access_token = 'blablabla' # Replace with you Access Token
    
    # Validate status
    if status not in ['active', 'archive', 'draft']:
        print(f"Invalid status: {status}")
        return

    # Data for the API request
    data = {
        "product": {
            "id": product_id,
            "status": status
        }
    }

    # Send a PUT request to update the product
    response = requests.put(
        f'https://{store_url}/admin/api/2023-04/products/{product_id}.json',
        headers={'X-Shopify-Access-Token': access_token, 'Content-Type': 'application/json'},
        data=json.dumps(data)
    )

    if response.status_code == 200:
        print(f"Product {product_id} status updated to {status}")
    else:
        print(f"Failed to update product {product_id} status: {response.content}")
