import asyncio
import json

from netsuite import NetSuite, Config, TokenAuth

config = Config(
    account="3374911",
    auth=TokenAuth(consumer_key="adb62c969e3de81813105bcbdf1371f9741671ccfc7909ab162e24f1588ad4ad", consumer_secret="d537386d481f643eed5aea50b509a7af94977e610b5028143613d9bad58726e4", token_id="8b3f30d99c0fd7775a1532adbf9cbe1cbd9110b0902134091402817e6f1a274b", token_secret="abee94967d0834e36f560cf636badf9beb0df0b082b8e2e3275cb41134731746"),
)

ns = NetSuite(config)


async def async_main():
    rest_api_results = await ns.rest_api.get("/record/v1/salesOrder")

    postdata = {
        "recordtype": "N/A",
        "id": 554445
}

    restlet_results = await ns.restlet.post(2446, deploy=1, data=json.dumps(postdata))

    print(restlet_results)

    # NOTE: SOAP needs `pip install netsuite[soap_api]`
    # soap_api_results = await ns.soap_api.getList('customer', internalIds=[1337])

    # Multiple requests, using the same underlying connection
    #async with ns.soap_api:
    #    customers = await ns.soap_api.getList('customer', internalIds=[1, 2, 3])
    #    sales_orders = await ns.soap_api.getList('salesOrder', internalIds=[1, 2])

if __name__ == "__main__":
    asyncio.run(async_main())
