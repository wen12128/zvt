# -*- coding: utf-8 -*-
# this file is generated by gen_quote_domain function, dont't change it
from sqlalchemy.ext.declarative import declarative_base

from zvdata.contract import register_schema
from zvt.domain.quotes import CoinKdataCommon

KdataBase = declarative_base()


class Coin1wkKdata(KdataBase, CoinKdataCommon):
    __tablename__ = 'coin_1wk_kdata'


register_schema(providers=['ccxt'], db_name='coin_1wk_kdata', schema_base=KdataBase)

__all__ = ['Coin1wkKdata']
