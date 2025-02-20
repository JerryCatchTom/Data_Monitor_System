'''
@File: parse_exchange_asset_info.py
@Description: further decouple with parse_exchange_market_data.py file (main for trading records),and
              provide an independent interface to parse asset information;
@Author: Jerry ;
@Date  : 23/1/25
Version: 1.0.0
Update Record:
-- 23/1/25: initialize version 1.0.0;
'''

from Configuration_File_Manage.Exchange_Asset_Info_Parser.binance_asset_info_parser import asset_info_parser

from typing import List, Dict


class Exchange_Asset_Info_Parser:

    def __init__(self):
        self.support_exchange = ["binance"]
        self.support_exchange_parser = {"binance": asset_info_parser().parse_data}

    def parse_data(self, exchange:str, asset_info_data:Dict, asset_type:str) -> List:
        if exchange not in self.support_exchange:
            raise ValueError(f"Exchange only support ={self.support_exchange}, but receive {exchange}.")
        try:
            parsed_asset_info_data = self.support_exchange_parser[exchange](asset_info_data=asset_info_data,
                                                                            asset_type=asset_type)
            return parsed_asset_info_data

        except Exception as e:
            print(e)


def binance_spot_info_sample():
    info_json = {'timezone': 'UTC', 'serverTime': 1734775099352,
     'rateLimits': [{'rateLimitType': 'REQUEST_WEIGHT', 'interval': 'MINUTE', 'intervalNum': 1, 'limit': 6000},
                    {'rateLimitType': 'ORDERS', 'interval': 'SECOND', 'intervalNum': 10, 'limit': 100},
                    {'rateLimitType': 'ORDERS', 'interval': 'DAY', 'intervalNum': 1, 'limit': 200000},
                    {'rateLimitType': 'RAW_REQUESTS', 'interval': 'MINUTE', 'intervalNum': 5, 'limit': 61000}],
     'exchangeFilters': [], 'symbols': [
        {'symbol': 'BTCUSDT', 'status': 'TRADING', 'baseAsset': 'BTC', 'baseAssetPrecision': 8, 'quoteAsset': 'USDT',
         'quotePrecision': 8, 'quoteAssetPrecision': 8, 'baseCommissionPrecision': 8, 'quoteCommissionPrecision': 8,
         'orderTypes': ['LIMIT', 'LIMIT_MAKER', 'MARKET', 'STOP_LOSS', 'STOP_LOSS_LIMIT', 'TAKE_PROFIT',
                        'TAKE_PROFIT_LIMIT'], 'icebergAllowed': True, 'ocoAllowed': True, 'otoAllowed': True,
         'quoteOrderQtyMarketAllowed': True, 'allowTrailingStop': True, 'cancelReplaceAllowed': True,
         'isSpotTradingAllowed': True, 'isMarginTradingAllowed': True, 'filters': [
            {'filterType': 'PRICE_FILTER', 'minPrice': '0.01000000', 'maxPrice': '1000000.00000000',
             'tickSize': '0.01000000'},
            {'filterType': 'LOT_SIZE', 'minQty': '0.00001000', 'maxQty': '9000.00000000', 'stepSize': '0.00001000'},
            {'filterType': 'ICEBERG_PARTS', 'limit': 10},
            {'filterType': 'MARKET_LOT_SIZE', 'minQty': '0.00000000', 'maxQty': '85.92497466',
             'stepSize': '0.00000000'},
            {'filterType': 'TRAILING_DELTA', 'minTrailingAboveDelta': 10, 'maxTrailingAboveDelta': 2000,
             'minTrailingBelowDelta': 10, 'maxTrailingBelowDelta': 2000},
            {'filterType': 'PERCENT_PRICE_BY_SIDE', 'bidMultiplierUp': '5', 'bidMultiplierDown': '0.2',
             'askMultiplierUp': '5', 'askMultiplierDown': '0.2', 'avgPriceMins': 5},
            {'filterType': 'NOTIONAL', 'minNotional': '5.00000000', 'applyMinToMarket': True,
             'maxNotional': '9000000.00000000', 'applyMaxToMarket': False, 'avgPriceMins': 5},
            {'filterType': 'MAX_NUM_ORDERS', 'maxNumOrders': 200},
            {'filterType': 'MAX_NUM_ALGO_ORDERS', 'maxNumAlgoOrders': 5}], 'permissions': [], 'permissionSets': [
            ['SPOT', 'MARGIN', 'TRD_GRP_004', 'TRD_GRP_005', 'TRD_GRP_006', 'TRD_GRP_009', 'TRD_GRP_010', 'TRD_GRP_011',
             'TRD_GRP_012', 'TRD_GRP_013', 'TRD_GRP_014', 'TRD_GRP_015', 'TRD_GRP_016', 'TRD_GRP_017', 'TRD_GRP_018',
             'TRD_GRP_019', 'TRD_GRP_020', 'TRD_GRP_021', 'TRD_GRP_022', 'TRD_GRP_023', 'TRD_GRP_024', 'TRD_GRP_025',
             'TRD_GRP_026', 'TRD_GRP_027', 'TRD_GRP_028', 'TRD_GRP_029', 'TRD_GRP_030', 'TRD_GRP_031', 'TRD_GRP_032',
             'TRD_GRP_033', 'TRD_GRP_034', 'TRD_GRP_035', 'TRD_GRP_036', 'TRD_GRP_037', 'TRD_GRP_038', 'TRD_GRP_039',
             'TRD_GRP_040', 'TRD_GRP_041', 'TRD_GRP_042', 'TRD_GRP_043', 'TRD_GRP_044', 'TRD_GRP_045', 'TRD_GRP_046',
             'TRD_GRP_047', 'TRD_GRP_048', 'TRD_GRP_049', 'TRD_GRP_050', 'TRD_GRP_051', 'TRD_GRP_052', 'TRD_GRP_053',
             'TRD_GRP_054', 'TRD_GRP_055', 'TRD_GRP_056', 'TRD_GRP_057', 'TRD_GRP_058', 'TRD_GRP_059', 'TRD_GRP_060',
             'TRD_GRP_061', 'TRD_GRP_062', 'TRD_GRP_063', 'TRD_GRP_064', 'TRD_GRP_065', 'TRD_GRP_066', 'TRD_GRP_067',
             'TRD_GRP_068', 'TRD_GRP_069', 'TRD_GRP_070', 'TRD_GRP_071', 'TRD_GRP_072', 'TRD_GRP_073', 'TRD_GRP_074',
             'TRD_GRP_075', 'TRD_GRP_076', 'TRD_GRP_077', 'TRD_GRP_078', 'TRD_GRP_079', 'TRD_GRP_080', 'TRD_GRP_081',
             'TRD_GRP_082', 'TRD_GRP_083', 'TRD_GRP_084', 'TRD_GRP_085', 'TRD_GRP_086', 'TRD_GRP_087', 'TRD_GRP_088',
             'TRD_GRP_089', 'TRD_GRP_090', 'TRD_GRP_091', 'TRD_GRP_092', 'TRD_GRP_093', 'TRD_GRP_094', 'TRD_GRP_095',
             'TRD_GRP_096', 'TRD_GRP_097', 'TRD_GRP_098', 'TRD_GRP_099', 'TRD_GRP_100', 'TRD_GRP_101', 'TRD_GRP_102',
             'TRD_GRP_103', 'TRD_GRP_104', 'TRD_GRP_105', 'TRD_GRP_106', 'TRD_GRP_107', 'TRD_GRP_108', 'TRD_GRP_109',
             'TRD_GRP_110', 'TRD_GRP_111', 'TRD_GRP_112', 'TRD_GRP_113', 'TRD_GRP_114', 'TRD_GRP_115', 'TRD_GRP_116',
             'TRD_GRP_117', 'TRD_GRP_118', 'TRD_GRP_119', 'TRD_GRP_120', 'TRD_GRP_121', 'TRD_GRP_122', 'TRD_GRP_123',
             'TRD_GRP_124', 'TRD_GRP_125', 'TRD_GRP_126', 'TRD_GRP_127', 'TRD_GRP_128', 'TRD_GRP_129', 'TRD_GRP_130',
             'TRD_GRP_131', 'TRD_GRP_132', 'TRD_GRP_133', 'TRD_GRP_134', 'TRD_GRP_135', 'TRD_GRP_136', 'TRD_GRP_137',
             'TRD_GRP_138', 'TRD_GRP_139', 'TRD_GRP_140', 'TRD_GRP_141', 'TRD_GRP_142', 'TRD_GRP_143', 'TRD_GRP_144',
             'TRD_GRP_145', 'TRD_GRP_146', 'TRD_GRP_147', 'TRD_GRP_148', 'TRD_GRP_149', 'TRD_GRP_150', 'TRD_GRP_151',
             'TRD_GRP_152', 'TRD_GRP_153', 'TRD_GRP_154', 'TRD_GRP_155', 'TRD_GRP_156', 'TRD_GRP_157', 'TRD_GRP_158',
             'TRD_GRP_159', 'TRD_GRP_160', 'TRD_GRP_161', 'TRD_GRP_162', 'TRD_GRP_163', 'TRD_GRP_164', 'TRD_GRP_165',
             'TRD_GRP_166', 'TRD_GRP_167', 'TRD_GRP_168', 'TRD_GRP_169', 'TRD_GRP_170', 'TRD_GRP_171', 'TRD_GRP_172',
             'TRD_GRP_173', 'TRD_GRP_174', 'TRD_GRP_175', 'TRD_GRP_176', 'TRD_GRP_177', 'TRD_GRP_178', 'TRD_GRP_179',
             'TRD_GRP_180', 'TRD_GRP_181', 'TRD_GRP_182', 'TRD_GRP_183', 'TRD_GRP_184', 'TRD_GRP_185', 'TRD_GRP_186',
             'TRD_GRP_187', 'TRD_GRP_188', 'TRD_GRP_189', 'TRD_GRP_190', 'TRD_GRP_191', 'TRD_GRP_192', 'TRD_GRP_193',
             'TRD_GRP_194', 'TRD_GRP_195', 'TRD_GRP_196', 'TRD_GRP_197', 'TRD_GRP_198', 'TRD_GRP_199', 'TRD_GRP_200',
             'TRD_GRP_201', 'TRD_GRP_202', 'TRD_GRP_203', 'TRD_GRP_204', 'TRD_GRP_205', 'TRD_GRP_206', 'TRD_GRP_207',
             'TRD_GRP_208', 'TRD_GRP_209', 'TRD_GRP_210', 'TRD_GRP_211', 'TRD_GRP_212', 'TRD_GRP_213', 'TRD_GRP_214',
             'TRD_GRP_215', 'TRD_GRP_216', 'TRD_GRP_217', 'TRD_GRP_218', 'TRD_GRP_219', 'TRD_GRP_220', 'TRD_GRP_221',
             'TRD_GRP_222', 'TRD_GRP_223', 'TRD_GRP_224', 'TRD_GRP_225', 'TRD_GRP_226', 'TRD_GRP_227', 'TRD_GRP_228',
             'TRD_GRP_229', 'TRD_GRP_230', 'TRD_GRP_231', 'TRD_GRP_232', 'TRD_GRP_233', 'TRD_GRP_234']],
         'defaultSelfTradePreventionMode': 'EXPIRE_MAKER',
         'allowedSelfTradePreventionModes': ['EXPIRE_TAKER', 'EXPIRE_MAKER', 'EXPIRE_BOTH']}]}

    return info_json

def test_parse_data():
    test_data = binance_spot_info_sample()
    test_parser = Exchange_Asset_Info_Parser()
    result = test_parser.parse_data(asset_info_data=test_data,asset_type="spot",exchange="binance")
    print(result)



if __name__ == '__main__':
    test_parse_data()
