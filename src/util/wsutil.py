#encoding:utf-8

from suds.client import Client
from src.config.netcfg import wsdlUrl

client = Client(wsdlUrl)
