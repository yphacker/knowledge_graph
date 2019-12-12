# coding=utf-8
# author=yphacker

import tushare as ts
from conf import config
from utils.utils import retry


class TsUtils(object):
    def __init__(self):
        self.api = ts.pro_api(config.ts_token)

    @retry(max_retries=3)
    def concept(self):
        return self.api.concept()

    @retry(max_retries=3)
    def concept_detail(self, id):
        return self.api.concept_detail(id=id)

    @retry(max_retries=3)
    def hs_const(self, hs_type):
        return self.api.hs_const(hs_type=hs_type)


ts_utils = TsUtils()
