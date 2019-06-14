#!/usr/bin/env python3
from src.business_layer import GetData

def main():
    GetData("https://api.coinbase.com/v2/exchange-rates") #put here url of RESTfull webserver

if __name__=="__main__":
    main()
