from sanic import Sanic
from sanic.response import json, text
import aiohttp
import os
import pangea.exceptions as pe
from pangea.config import PangeaConfig
from pangea.services import Embargo
from pangea.tools import logger_set_pangea_config
from sanic import Sanic

# Sanic.start_method = "fork"

app = Sanic(__name__)

EMBARGO_TOKEN = os.getenv("EMBARGO_TOKEN")
embargo = Embargo(token=EMBARGO_TOKEN)

@app.route('/embargo-check/<ip>')
async def perform_embargo_check(request, ip : str) -> str:
    """
    Perform an embargo check on the given IP address.

    Args:
        request (Request): The Sanic request object.
        ip (str): The IP address to check for embargo.

    Returns:
        str: A JSON string with embargo details or an error message.
    """
    # ip = "213.24.238.26"
    print(f"Checking Embargo IP: {ip}")
    try:
        embargo_response = embargo.ip_check(ip=ip)
        print(f"Response: {embargo_response.result}")
        return text(str(embargo_response))
    except pe.PangeaAPIException as e:
        print(f"Embargo Request Error: {e.response.summary}")
        for err in e.errors:
            print(f"\t{err.detail} \n")

if __name__ == "__main__":
    app.run(single_process=True, port=5500)

