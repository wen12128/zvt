# -*- coding: utf-8 -*-
# this file is generated by gen_kdata_schema function, dont't change it
from sqlalchemy.ext.declarative import declarative_base

from zvt.contract.register import register_schema
from zvt.schemas.quotes import IndexKdataCommon

KdataBase = declarative_base()


class Index1dKdata(KdataBase, IndexKdataCommon):
    __tablename__ = 'index_1d_kdata'


register_schema(providers=['sina'], db_name='index_1d_kdata', schema_base=KdataBase)

__all__ = ['Index1dKdata']
