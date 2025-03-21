import pandas as pd
import numpy as np

import bit_functions
import config_btc
import classes

from pyspark.sql import SparkSession, DataFrame, functions as F
from pyspark.sql.types import IntegerType,LongType,DoubleType,StringType
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

def get_spark():

    spark = (
            SparkSession
            .builder
            .appName("OTUS")
            .getOrCreate()
            )
    return spark

final_cols = ['MA10_REL_shift6_cross',
 'EMA100_REL',
 'EMA60_REL_shift12_cross',
 'MACDHist_REL_shift7',
 'Close_15_to_MA15',
 'MA10_REL_shift1_cross',
 'MA15_REL_shift1',
 'MA100_REL_shift12',
 'EMA200_REL_shift12_cross',
 'Close_9_to_10',
 'MACDHist_REL',
 'EMA32_REL_shift1',
 'RSI9_up_70_perman',
 'EMA20_REL_shift6_cross',
 'MA10_REL_shift6',
 'EMA26_REL_shift24_cross',
 'EMA75_REL_shift24',
 'EMA200_REL_shift24_cross',
 'RSI9_dw_20_perman',
 'EMA75_REL_shift6',
 'EMA75_REL_shift1_cross',
 'MA20_REL_shift12_cross',
 'EMA12_REL_shift12',
 'ROC200sm',
 'EMA32_REL_shift6',
 'MA75_REL_shift6_cross',
 'MACDHist_corr_roll_mean3_shift1',
 'Close_10_to_MA15',
 'Close_0_to_4',
 'RSI14_up_80',
 'MA150_REL_shift1',
 'EMA26_REL',
 'EMA26_REL_shift12',
 'std_20_rel',
 'Close_4_to_MA15',
 'RSI14_dw_30',
 'EMA20_REL_shift24',
 'Close_3_to_4',
 'MA50_REL_shift24_cross',
 'EMA14_REL_shift24_cross',
 'MA10_REL_shift1',
 'AweOs_cor_roll_mean3',
 'AweOs_corr_1_to_3',
 'MA150_REL_shift6_cross',
 'RSI20_up_70_perman',
 'MACDHist_corr_roll_mean3_shift6',
 'Close_5_to_MA15',
 'EMA150_REL_shift6',
 'RSI27_dw_20',
 'MA10_REL_shift12_cross',
 'EMA38_REL_shift6',
 'EMA32_REL_shift1_cross',
 'RSI20_up_80',
 'Close_m3_2_to_MA15',
 'Close_m3_6_to_MA15',
 'RSI27_dw_30',
 'AweOs_corr_3_to_6',
 'EMA32_REL_shift12_cross',
 'MA5_REL_shift24_cross',
 'EMA12_REL',
 'MACDHist_corr_1_to_3',
 'EMA44_REL_shift6_cross',
 'MACDHist_corr',
 'AweOs_cor_roll_mean3_shift6',
 'level_close_act_w',
 'RSI14_dw_20_perman',
 'MA5_REL_shift24',
 'MA20_REL_shift6',
 'Close_6_to_MA15',
 'EMA38_REL_shift12',
 'MA5_REL_shift12',
 'Close_8_to_MA15',
 'EMA100_REL_shift24',
 'EMA8_REL_shift24_cross',
 'MA5_REL_shift6_cross',
 'Close_7_to_8',
 'MA20_REL_shift1',
 'MA5_REL_shift12_cross',
 'EMA_gor_1_REL_cross_all',
 'RSI20_dw_20_perman',
 'AweOs_cor',
 'MA200_REL_shift12',
 'RSI9_up_80',
 'MACDHist_REL_shift3',
 'EMA200_REL_shift1_cross',
 'RSI9_dw_30_perman',
 'EMA44_REL_shift24',
 'MA5_REL',
 'MA100_REL_shift12_cross',
 'EMA8_REL',
 'RSI14_up_70_perman',
 'MA10_REL_shift24',
 'Close_13_to_MA15',
 'MACDHist_corr_3_to_6',
 'MA5_REL_shift6',
 'RSI27_up_70_perman',
 'MA_gor_6_REL_cross_all',
 'EMA100_REL_shift24_cross',
 'EMA14_REL_shift6_cross',
 'RSI20_dw_30',
 'Close_2_to_3',
 'EMA20_REL_shift1_cross',
 'RSI27_up_80',
 'MACDHist_corr_roll_mean3_shift3',
 'Close_5_to_6',
 'Close_6_to_7',
 'MACDHist_corr_roll_mean3',
 'AweOs_corr_0_to_6',
 'MA25_REL_shift1',
 'Close_2_to_MA15',
 'EMA12_REL_shift6',
 'Close_0_to_3',
 'step_to_fiba',
 'Close_9_to_MA15',
 'EMA200_REL_shift24',
 'AweOs_corr_0_to_1',
 'MA_gor_24_REL_cross_all',
 'Close_1_to_2',
 'Close_0_to_6',
 'MA50_REL_shift1',
 'EMA14_REL_shift12',
 'MA20_REL',
 'MA15_REL_shift1_cross',
 'MACDHist_corr_0_to_1',
 'EMA_gor_12_REL_cross_all',
 'MACDHist_corr_0_to_6',
 'Close_8_to_9',
 'Close_11_to_12',
 'EMA12_REL_shift12_cross',
 'EMA50_REL_shift24_cross',
 'MA15_REL',
 'Close_4_to_5',
 'EMA50_REL_shift1_cross',
 'EMA44_REL',
 'Close_0_to_1',
 'MA150_REL_shift1_cross',
 'Close_0_to_12',
 'MA100_REL_shift6_cross',
 'EMA200_REL_shift6_cross',
 'EMA44_REL_shift12_cross',
 'MA100_REL_shift1_cross',
 'MACDHist_REL_shift10',
 'level_close_old_w',
 'EMA75_REL_shift12',
 'std_100_rel',
 'MA75_REL_shift1_cross',
 'EMA20_REL',
 'Close_10_to_11',
 'MA75_REL_shift1',
 'AweOs_cor_shift3',
 'EMA12_REL_shift1',
 'MA75_REL_shift12_cross',
 'MA10_REL_shift12',
 'MA200_REL',
 'RSI14',
 'MA5_REL_shift1_cross',
 'MA75_REL_shift24_cross',
 'EMA26_REL_shift1',
 'MA150_REL_shift12_cross',
 'EMA12_REL_shift24',
 'EMA150_REL_shift1_cross',
 'EMA60_REL_shift6_cross',
 'EMA150_REL_shift6_cross',
 'Close_coef_nak',
 'TSI',
 'MA200_REL_shift1_cross',
 'Close_12_to_MA15',
 'EMA100_REL_shift6',
 'MA25_REL_shift6',
 'Close_11_to_MA15',
 'RSI20',
 'Close_m3_4_to_MA15',
 'Close_0_to_9',
 'RSI27',
 'EMA26_REL_shift6_cross',
 'RSI9',
 'EMA12_REL_shift1_cross',
 'MA25_REL_shift1_cross',
 'EMA60_REL_shift1',
 'MA100_REL',
 'AweOs_cor_roll_mean3_shift1',
 'MA50_REL_shift1_cross',
 'MACDHist_corr_shift3',
 'EMA32_REL',
 'EMA100_REL_shift1_cross',
 'EMA100_REL_shift12_cross',
 'MA25_REL',
 'MACDHist_REL_shift5',
 'MA150_REL_shift24_cross',
 'EMA100_REL_shift6_cross',
 'MACDHist_corr_shift6',
 'MA50_REL_shift12_cross',
 'MA100_REL_shift24_cross',
 'MA200_REL_shift6',
 'MA200_REL_shift6_cross',
 'MA200_REL_shift12_cross',
 'EMA50_REL_shift6',
 'EMA150_REL',
 'EMA20_REL_shift12',
 'EMA44_REL_shift24_cross',
 'EMA150_REL_shift24',
 'MA15_REL_shift6_cross',
 'Close_m3_3_to_MA15',
 'MA25_REL_shift6_cross',
 'EMA75_REL_shift24_cross',
 'MA50_REL_shift6_cross',
 'MA25_REL_shift24_cross',
 'Close_7_to_MA15',
 'EMA20_REL_shift1',
 'MA20_REL_shift6_cross',
 'MA_gor_1_REL_cross_all',
 'EMA50_REL_shift12',
 'Close_m3_9_to_MA15',
 'Close_3_to_MA15',
 'MA20_REL_shift1_cross',
 'Close_0_to_5',
 'MA200_REL_shift24_cross',
 'AweOs_cor_roll_mean3_shift3',
 'EMA75_REL_shift1',
 'MA25_REL_shift12_cross',
 'EMA200_REL',
 'MA150_REL_shift12',
 'MACDHist_REL_shift1',
 'EMA150_REL_shift24_cross',
 'EMA50_REL_shift1',
 'MA50_REL',
 'EMA_gor_6_REL_cross_all',
 'EMA75_REL_shift6_cross',
 'AweOs_cor_shift6',
 'EMA75_REL_shift12_cross',
 'EMA150_REL_shift12_cross',
 'EMA32_REL_shift24',
 'EMA20_REL_shift12_cross',
 'MA15_REL_shift24_cross',
 'Close_m3_0_to_MA15',
 'MA10_REL',
 'MA20_REL_shift24_cross',
 'MA15_REL_shift12_cross',
 'Close_14_to_MA15',
 'Close_m3_5_to_MA15',
 'MA_gor_12_REL_cross_all',
 'EMA60_REL',
 'EMA60_REL_shift1_cross',
 'target_new',
 'ROWNUM',
 'ROW_NUM'
 ]


def main(input_path,output_path):


    spark = get_spark()


    sdf = spark.read.json(input_path)

    btcusdt_4h = sdf.toPandas()

    agregate_4h=classes.Features(config_btc,'4H',bit_functions)._first_prep_no_d(btcusdt_4h)

    data_set_4h=classes.Features(config_btc,'4H',bit_functions).transform(agregate_4h)

    data_set_4h = data_set_4h[final_cols]

    schema = StructType([
        StructField("MA10_REL_shift6_cross", IntegerType(), True),
        StructField("EMA100_REL", FloatType(), True),
        StructField("EMA60_REL_shift12_cross", IntegerType(), True),
        StructField("MACDHist_REL_shift7", FloatType(), True),
        StructField("Close_15_to_MA15", FloatType(), True),
        StructField("MA10_REL_shift1_cross", IntegerType(), True),
        StructField("MA15_REL_shift1", FloatType(), True),
        StructField("MA100_REL_shift12", FloatType(), True),
        StructField("EMA200_REL_shift12_cross", IntegerType(), True),
        StructField("Close_9_to_10", FloatType(), True),
        StructField("MACDHist_REL", FloatType(), True),
        StructField("EMA32_REL_shift1", FloatType(), True),
        StructField("RSI9_up_70_perman", IntegerType(), True),
        StructField("EMA20_REL_shift6_cross", IntegerType(), True),
        StructField("MA10_REL_shift6", FloatType(), True),
        StructField("EMA26_REL_shift24_cross", IntegerType(), True),
        StructField("EMA75_REL_shift24", FloatType(), True),
        StructField("EMA200_REL_shift24_cross", IntegerType(), True),
        StructField("RSI9_dw_20_perman", IntegerType(), True),
        StructField("EMA75_REL_shift6", FloatType(), True),
        StructField("EMA75_REL_shift1_cross", IntegerType(), True),
        StructField("MA20_REL_shift12_cross", IntegerType(), True),
        StructField("EMA12_REL_shift12", FloatType(), True),
        StructField("ROC200sm", FloatType(), True),
        StructField("EMA32_REL_shift6", FloatType(), True),
        StructField("MA75_REL_shift6_cross", IntegerType(), True),
        StructField("MACDHist_corr_roll_mean3_shift1", FloatType(), True),
        StructField("Close_10_to_MA15", FloatType(), True),
        StructField("Close_0_to_4", FloatType(), True),
        StructField("RSI14_up_80", IntegerType(), True),
        StructField("MA150_REL_shift1", FloatType(), True),
        StructField("EMA26_REL", FloatType(), True),
        StructField("EMA26_REL_shift12", FloatType(), True),
        StructField("std_20_rel", FloatType(), True),
        StructField("Close_4_to_MA15", FloatType(), True),
        StructField("RSI14_dw_30", IntegerType(), True),
        StructField("EMA20_REL_shift24", FloatType(), True),
        StructField("Close_3_to_4", FloatType(), True),
        StructField("MA50_REL_shift24_cross", IntegerType(), True),
        StructField("EMA14_REL_shift24_cross", IntegerType(), True),
        StructField("MA10_REL_shift1", FloatType(), True),
        StructField("AweOs_cor_roll_mean3", FloatType(), True),
        StructField("AweOs_corr_1_to_3", FloatType(), True),
        StructField("MA150_REL_shift6_cross", IntegerType(), True),
        StructField("RSI20_up_70_perman", IntegerType(), True),
        StructField("MACDHist_corr_roll_mean3_shift6", FloatType(), True),
        StructField("Close_5_to_MA15", FloatType(), True),
        StructField("EMA150_REL_shift6", FloatType(), True),
        StructField("RSI27_dw_20", IntegerType(), True),
        StructField("MA10_REL_shift12_cross", IntegerType(), True),
        StructField("EMA38_REL_shift6", FloatType(), True),
        StructField("EMA32_REL_shift1_cross", IntegerType(), True),
        StructField("RSI20_up_80", IntegerType(), True),
        StructField("Close_m3_2_to_MA15", FloatType(), True),
        StructField("Close_m3_6_to_MA15", FloatType(), True),
        StructField("RSI27_dw_30", IntegerType(), True),
        StructField("AweOs_corr_3_to_6", FloatType(), True),
        StructField("EMA32_REL_shift12_cross", IntegerType(), True),
        StructField("MA5_REL_shift24_cross", IntegerType(), True),
        StructField("EMA12_REL", FloatType(), True),
        StructField("MACDHist_corr_1_to_3", FloatType(), True),
        StructField("EMA44_REL_shift6_cross", IntegerType(), True),
        StructField("MACDHist_corr", FloatType(), True),
        StructField("AweOs_cor_roll_mean3_shift6", FloatType(), True),
        StructField("level_close_act_w", FloatType(), True),
        StructField("RSI14_dw_20_perman", IntegerType(), True),
        StructField("MA5_REL_shift24", FloatType(), True),
        StructField("MA20_REL_shift6", FloatType(), True),
        StructField("Close_6_to_MA15", FloatType(), True),
        StructField("EMA38_REL_shift12", FloatType(), True),
        StructField("MA5_REL_shift12", FloatType(), True),
        StructField("Close_8_to_MA15", FloatType(), True),
        StructField("EMA100_REL_shift24", FloatType(), True),
        StructField("EMA8_REL_shift24_cross", IntegerType(), True),
        StructField("MA5_REL_shift6_cross", IntegerType(), True),
        StructField("Close_7_to_8", FloatType(), True),
        StructField("MA20_REL_shift1", FloatType(), True),
        StructField("MA5_REL_shift12_cross", IntegerType(), True),
        StructField("EMA_gor_1_REL_cross_all", FloatType(), True),
        StructField("RSI20_dw_20_perman", IntegerType(), True),
        StructField("AweOs_cor", FloatType(), True),
        StructField("MA200_REL_shift12", FloatType(), True),
        StructField("RSI9_up_80", IntegerType(), True),
        StructField("MACDHist_REL_shift3", FloatType(), True),
        StructField("EMA200_REL_shift1_cross", IntegerType(), True),
        StructField("RSI9_dw_30_perman", IntegerType(), True),
        StructField("EMA44_REL_shift24", FloatType(), True),
        StructField("MA5_REL", FloatType(), True),
        StructField("MA100_REL_shift12_cross", IntegerType(), True),
        StructField("EMA8_REL", FloatType(), True),
        StructField("RSI14_up_70_perman", IntegerType(), True),
        StructField("MA10_REL_shift24", FloatType(), True),
        StructField("Close_13_to_MA15", FloatType(), True),
        StructField("MACDHist_corr_3_to_6", FloatType(), True),
        StructField("MA5_REL_shift6", FloatType(), True),
        StructField("RSI27_up_70_perman", IntegerType(), True),
        StructField("MA_gor_6_REL_cross_all", FloatType(), True),
        StructField("EMA100_REL_shift24_cross", IntegerType(), True),
        StructField("EMA14_REL_shift6_cross", IntegerType(), True),
        StructField("RSI20_dw_30", IntegerType(), True),
        StructField("Close_2_to_3", FloatType(), True),
        StructField("EMA20_REL_shift1_cross", IntegerType(), True),
        StructField("RSI27_up_80", IntegerType(), True),
        StructField("MACDHist_corr_roll_mean3_shift3", FloatType(), True),
        StructField("Close_5_to_6", FloatType(), True),
        StructField("Close_6_to_7", FloatType(), True),
        StructField("MACDHist_corr_roll_mean3", FloatType(), True),
        StructField("AweOs_corr_0_to_6", FloatType(), True),
        StructField("MA25_REL_shift1", FloatType(), True),
        StructField("Close_2_to_MA15", FloatType(), True),
        StructField("EMA12_REL_shift6", FloatType(), True),
        StructField("Close_0_to_3", FloatType(), True),
        StructField("step_to_fiba", FloatType(), True),
        StructField("Close_9_to_MA15", FloatType(), True),
        StructField("EMA200_REL_shift24", FloatType(), True),
        StructField("AweOs_corr_0_to_1", FloatType(), True),
        StructField("MA_gor_24_REL_cross_all", FloatType(), True),
        StructField("Close_1_to_2", FloatType(), True),
        StructField("Close_0_to_6", FloatType(), True),
        StructField("MA50_REL_shift1", FloatType(), True),
        StructField("EMA14_REL_shift12", FloatType(), True),
        StructField("MA20_REL", FloatType(), True),
        StructField("MA15_REL_shift1_cross", IntegerType(), True),
        StructField("MACDHist_corr_0_to_1", FloatType(), True),
        StructField("EMA_gor_12_REL_cross_all", FloatType(), True),
        StructField("MACDHist_corr_0_to_6", FloatType(), True),
        StructField("Close_8_to_9", FloatType(), True),
        StructField("Close_11_to_12", FloatType(), True),
        StructField("EMA12_REL_shift12_cross", IntegerType(), True),
        StructField("EMA50_REL_shift24_cross", IntegerType(), True),
        StructField("MA15_REL", FloatType(), True),
        StructField("Close_4_to_5", FloatType(), True),
        StructField("EMA50_REL_shift1_cross", IntegerType(), True),
        StructField("EMA44_REL", FloatType(), True),
        StructField("Close_0_to_1", FloatType(), True),
        StructField("MA150_REL_shift1_cross", IntegerType(), True),
        StructField("Close_0_to_12", FloatType(), True),
        StructField("MA100_REL_shift6_cross", IntegerType(), True),
        StructField("EMA200_REL_shift6_cross", IntegerType(), True),
        StructField("EMA44_REL_shift12_cross", IntegerType(), True),
        StructField("MA100_REL_shift1_cross", IntegerType(), True),
        StructField("MACDHist_REL_shift10", FloatType(), True),
        StructField("level_close_old_w", FloatType(), True),
        StructField("EMA75_REL_shift12", FloatType(), True),
        StructField("std_100_rel", FloatType(), True),
        StructField("MA75_REL_shift1_cross", IntegerType(), True),
        StructField("EMA20_REL", FloatType(), True),
        StructField("Close_10_to_11", FloatType(), True),
        StructField("MA75_REL_shift1", FloatType(), True),
        StructField("AweOs_cor_shift3", FloatType(), True),
        StructField("EMA12_REL_shift1", FloatType(), True),
        StructField("MA75_REL_shift12_cross", IntegerType(), True),
        StructField("MA10_REL_shift12", FloatType(), True),
        StructField("MA200_REL", FloatType(), True),
        StructField("RSI14", FloatType(), True),
        StructField("MA5_REL_shift1_cross", IntegerType(), True),
        StructField("MA75_REL_shift24_cross", IntegerType(), True),
        StructField("EMA26_REL_shift1", FloatType(), True),
        StructField("MA150_REL_shift12_cross", IntegerType(), True),
        StructField("EMA12_REL_shift24", FloatType(), True),
        StructField("EMA150_REL_shift1_cross", IntegerType(), True),
        StructField("EMA60_REL_shift6_cross", IntegerType(), True),
        StructField("EMA150_REL_shift6_cross", IntegerType(), True),
        StructField("Close_coef_nak", FloatType(), True),
        StructField("TSI", FloatType(), True),
        StructField("MA200_REL_shift1_cross", IntegerType(), True),
        StructField("Close_12_to_MA15", FloatType(), True),
        StructField("EMA100_REL_shift6", FloatType(), True),
        StructField("MA25_REL_shift6", FloatType(), True),
        StructField("Close_11_to_MA15", FloatType(), True),
        StructField("RSI20", FloatType(), True),
        StructField("Close_m3_4_to_MA15", FloatType(), True),
        StructField("Close_0_to_9", FloatType(), True),
        StructField("RSI27", FloatType(), True),
        StructField("EMA26_REL_shift6_cross", IntegerType(), True),
        StructField("RSI9", FloatType(), True),
        StructField("EMA12_REL_shift1_cross", IntegerType(), True),
        StructField("MA25_REL_shift1_cross", IntegerType(), True),
        StructField("EMA60_REL_shift1", FloatType(), True),
        StructField("MA100_REL", FloatType(), True),
        StructField("AweOs_cor_roll_mean3_shift1", FloatType(), True),
        StructField("MA50_REL_shift1_cross", IntegerType(), True),
        StructField("MACDHist_corr_shift3", FloatType(), True),
        StructField("EMA32_REL", FloatType(), True),
        StructField("EMA100_REL_shift1_cross", IntegerType(), True),
        StructField("EMA100_REL_shift12_cross", IntegerType(), True),
        StructField("MA25_REL", FloatType(), True),
        StructField("MACDHist_REL_shift5", FloatType(), True),
        StructField("MA150_REL_shift24_cross", IntegerType(), True),
        StructField("EMA100_REL_shift6_cross", IntegerType(), True),
        StructField("MACDHist_corr_shift6", FloatType(), True),
        StructField("MA50_REL_shift12_cross", IntegerType(), True),
        StructField("MA100_REL_shift24_cross", IntegerType(), True),
        StructField("MA200_REL_shift6", FloatType(), True),
        StructField("MA200_REL_shift6_cross", IntegerType(), True),
        StructField("MA200_REL_shift12_cross", IntegerType(), True),
        StructField("EMA50_REL_shift6", FloatType(), True),
        StructField("EMA150_REL", FloatType(), True),
        StructField("EMA20_REL_shift12", FloatType(), True),
        StructField("EMA44_REL_shift24_cross", IntegerType(), True),
        StructField("EMA150_REL_shift24", FloatType(), True),
        StructField("MA15_REL_shift6_cross", IntegerType(), True),
        StructField("Close_m3_3_to_MA15", FloatType(), True),
        StructField("MA25_REL_shift6_cross", IntegerType(), True),
        StructField("EMA75_REL_shift24_cross", IntegerType(), True),
        StructField("MA50_REL_shift6_cross", IntegerType(), True),
        StructField("MA25_REL_shift24_cross", IntegerType(), True),
        StructField("Close_7_to_MA15", FloatType(), True),
        StructField("EMA20_REL_shift1", FloatType(), True),
        StructField("MA20_REL_shift6_cross", IntegerType(), True),
        StructField("MA_gor_1_REL_cross_all", FloatType(), True),
        StructField("EMA50_REL_shift12", FloatType(), True),
        StructField("Close_m3_9_to_MA15", FloatType(), True),
        StructField("Close_3_to_MA15", FloatType(), True),
        StructField("MA20_REL_shift1_cross", IntegerType(), True),
        StructField("Close_0_to_5", FloatType(), True),
        StructField("MA200_REL_shift24_cross", IntegerType(), True),
        StructField("AweOs_cor_roll_mean3_shift3", FloatType(), True),
        StructField("EMA75_REL_shift1", FloatType(), True),
        StructField("MA25_REL_shift12_cross", IntegerType(), True),
        StructField("EMA200_REL", FloatType(), True),
        StructField("MA150_REL_shift12", FloatType(), True),
        StructField("MACDHist_REL_shift1", FloatType(), True),
        StructField("EMA150_REL_shift24_cross", IntegerType(), True),
        StructField("EMA50_REL_shift1", FloatType(), True),
        StructField("MA50_REL", FloatType(), True),
        StructField("EMA_gor_6_REL_cross_all", FloatType(), True),
        StructField("EMA75_REL_shift6_cross", IntegerType(), True),
        StructField("AweOs_cor_shift6", FloatType(), True),
        StructField("EMA75_REL_shift12_cross", IntegerType(), True),
        StructField("EMA150_REL_shift12_cross", IntegerType(), True),
        StructField("EMA32_REL_shift24", FloatType(), True),
        StructField("EMA20_REL_shift12_cross", IntegerType(), True),
        StructField("MA15_REL_shift24_cross", IntegerType(), True),
        StructField("Close_m3_0_to_MA15", FloatType(), True),
        StructField("MA10_REL", FloatType(), True),
        StructField("MA20_REL_shift24_cross", IntegerType(), True),
        StructField("MA15_REL_shift12_cross", IntegerType(), True),
        StructField("Close_14_to_MA15", FloatType(), True),
        StructField("Close_m3_5_to_MA15", FloatType(), True),
        StructField("MA_gor_12_REL_cross_all", FloatType(), True),
        StructField("EMA60_REL", FloatType(), True),
        StructField("EMA60_REL_shift1_cross", IntegerType(), True),
        StructField("target_new", IntegerType(), True),
        StructField("ROWNUM", IntegerType(), True),
        StructField("ROW_NUM", IntegerType(), True)
    ])


    sdf_final= spark.createDataFrame(data_set_4h, schema=schema)

    mode ="overwrite"
    fmt= "parquet"

    num_out_partitions=1

    if num_out_partitions:
        sdf_final = sdf_final.repartition(num_out_partitions)

    (
    sdf_final
     .write
     .format(fmt)
     .mode(mode)
     .save(output_path)
    )



if __name__ == "__main__":

 #   parser = ArgumentParser()
 #   parser.add_argument("--bucket", required=True, help="S3 bucket name")
 #   args = parser.parse_args()
 #   bucket_name = args.bucket

    bucket_name = 'cold-s3-bucket'

    input_path =  f"s3a://{bucket_name}/btc/btcusdt_4h.json"
    output_path = f"s3a://{bucket_name}/btc_prepaired_data.parquet"


    main(input_path,output_path)
