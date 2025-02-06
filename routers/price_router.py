from fastapi import APIRouter, HTTPException
import requests
from fastapi import Query

# Define the APIRouter object
price_router = APIRouter()

@price_router.get("/electric-price")
async def get_electric_price(
    year: int = Query(..., description="Year of the price data"),
    month: int = Query(..., description="Month of the price data"),
    day: int = Query(..., description="Day of the price data")
):
    # Build the URL based on the input date
    url = f"https://www.sahkonhintatanaan.fi/api/v1/prices/{year}/{month:02d}-{day:02d}.json"
    
    try:
        # Make the request to the external API
        response = requests.get(url)
        
        # If the response status code is not 200 (OK), raise an exception
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching data from API")
        
        # Return the data received from the API
        data = response.json()
        price_list = [list(item.values())[0] for item in data]
        
        return price_list
    
    except requests.exceptions.RequestException as e:
        # Handle request exceptions (network issues, invalid URL, etc.)
        raise HTTPException(status_code=500, detail="Error connecting to the external service")
