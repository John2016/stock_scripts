# -*- coding:utf-8 -*-

import pandas as pd
from pathlib import *

PATH = '2019东财汇总.xlsx'

file_path = Path(PATH) 

dateparse = lambda dates: pd.datetime.striptime(dates, '%Y/%m/%d')
data_whole = pd.read_excel(file_path, 0, parse_dates = True, date_parser = dateparse)

data_whole.head()

other_stop_words = ['新股','债','配售']
def get_useful_row(data):
    stop_words_stock = ['--','债','Ｒ-001','GC001','Ｒ-002','GC002']
    return data.iloc[:,3].apply(lambda name: any([stopword in name for stopword in stop_words_stock]))

def get_useful_class(data):
    stop_words_class = ['融券','银行','红利' ]

def count_stock(data):
    # 今年操作过的股票应该是81只
    return data['证券代码'].unique().size()

# 统计并绘制交易习惯，月份，星期，上午或晚上等
# 交易时间之外的交易都是非常规交易
def stastic_operate(data):

    

