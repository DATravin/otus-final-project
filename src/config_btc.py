





'''

тут лежат списки фичей и параметры моделей

col_fin_full - общий

col_fin_up_4h - для модели 4H long
col_fin_dw_4h - для модели 4H short
col_fin_up_1h - для модели 1H long
col_fin_dw_1h - для модели 1H short


MODEL_PARAMS_UP_4H - параметры модельки для long 4H
MODEL_PARAMS_DW_4H - параметры модельки для short 4H 
MODEL_PARAMS_UP_1H - параметры модельки для long 1H
MODEL_PARAMS_DW_1H - параметры модельки для short 1H 



версии

25.06.2020 - база
28.06.2020 - добавлены набор эвентов, посчитано на до 12.2020
07.07.2020 - добавлены 1 синусойды, посчитано на до 12.2020
08.07.2020 - добавлены 2 синусойды, посчитано на до 12.2020



'''

#параметры для таргетной переменной

target_var_par={
                '1H':[3,0.015],#[3,0.02]
               '4H':[3,0.03]
               }


#параметры скользящего стопа

target_var_par={
                '1H':[3,0.015],#[3,0.02]
               '4H':[3,0.03]
               }

slide_stop={
                'shift_stop':0.003,
               'shift_check':0.003,
                'first_stop':0.002,
                'first_check':0.012
               }


slide_stop_take={'window':12,
                 'step':7,
                 'q_level':0.8
                }


params_trade ={
                'l_c': 3,
              'move': 8,
              'freez': 10,
              'par1': 0.1,
              'par2': 0.16,
                'perev':0
            }


target_var_par_new={
                '1H':[0.01,20,1],#[3,0.02]
               '4H':[0.015,30,1]
               }


hold_period = 150


back_check_par=168



# для сделок LONG
#     take_r=find_corr_stop(df_4G_model2,num_row,10,5,'dw','mean',q=0.8)
#     stop_r=find_corr_stop(df_4G_model2,num_row,10,5,'up','quantile',q=0.8)
#     для сделок SHORT
#     take_r=find_corr_stop(df_4G_model2,num_row,10,5,'up','mean',q=0.8)
#     stop_r=find_corr_stop(df_4G_model2,num_row,10,5,'dw','quantile',q=0.8)


col_fin_full=[
   #'Boll_up',
    #'Boll_down', 
    #'MACDHist',
    #'AweOs',
    'MACDHist_corr',
    'AweOs_cor',
    
    'ROC200', 'ROC200sm', 
    'TSI',
    
    'EMA8_REL', 'EMA8_REL_shift1',
      'EMA8_REL_shift1_cross', 
    
    'EMA8_REL_shift6', 'EMA8_REL_shift6_cross',
       'EMA8_REL_shift12', 'EMA8_REL_shift12_cross', 'EMA8_REL_shift24',
       #'EMA8_REL_shift24_cross', 
    
    'EMA12_REL', 'EMA12_REL_shift1',
       'EMA12_REL_shift1_cross', 'EMA12_REL_shift6', 'EMA12_REL_shift6_cross',
       'EMA12_REL_shift12', 'EMA12_REL_shift12_cross', 'EMA12_REL_shift24',
       #'EMA12_REL_shift24_cross', 
    
    'EMA14_REL',
    'EMA14_REL_shift1', 'EMA14_REL_shift1_cross', 'EMA14_REL_shift6',
       'EMA14_REL_shift6_cross', 'EMA14_REL_shift12',
       'EMA14_REL_shift12_cross', 'EMA14_REL_shift24',
       #'EMA14_REL_shift24_cross', 
    
    'EMA20_REL', 'EMA20_REL_shift1',
       'EMA20_REL_shift1_cross', 'EMA20_REL_shift6', 'EMA20_REL_shift6_cross',
       'EMA20_REL_shift12', 'EMA20_REL_shift12_cross', 'EMA20_REL_shift24',
      # 'EMA20_REL_shift24_cross', 
    
    'EMA26_REL', 'EMA26_REL_shift1',
       'EMA26_REL_shift1_cross', 'EMA26_REL_shift6', 'EMA26_REL_shift6_cross',
       'EMA26_REL_shift12', 'EMA26_REL_shift12_cross', 'EMA26_REL_shift24',
      # 'EMA26_REL_shift24_cross', 
    
    'EMA32_REL', 'EMA32_REL_shift1',
       'EMA32_REL_shift1_cross', 'EMA32_REL_shift6', 'EMA32_REL_shift6_cross',
       'EMA32_REL_shift12', 'EMA32_REL_shift12_cross','EMA32_REL_shift24',
      # 'EMA32_REL_shift24_cross',
    
    'EMA38_REL', 'EMA38_REL_shift1',
       'EMA38_REL_shift1_cross', 'EMA38_REL_shift6', 'EMA38_REL_shift6_cross',
       'EMA38_REL_shift12', 'EMA38_REL_shift12_cross', 'EMA38_REL_shift24',
      # 'EMA38_REL_shift24_cross', 
    
    'EMA44_REL', 'EMA44_REL_shift1',
       'EMA44_REL_shift1_cross', 'EMA44_REL_shift6', 'EMA44_REL_shift6_cross',
       'EMA44_REL_shift12', 'EMA44_REL_shift12_cross','EMA44_REL_shift24',
      #'EMA44_REL_shift24_cross', 
    
    'EMA50_REL', 'EMA50_REL_shift1',
     'EMA50_REL_shift1_cross', 'EMA50_REL_shift6', 'EMA50_REL_shift6_cross',
       'EMA50_REL_shift12', 'EMA50_REL_shift12_cross', 'EMA50_REL_shift24',
      # 'EMA50_REL_shift24_cross',
    
    'EMA60_REL', 'EMA60_REL_shift1',
       'EMA60_REL_shift1_cross', 'EMA60_REL_shift6', 'EMA60_REL_shift6_cross',
       'EMA60_REL_shift12', 'EMA60_REL_shift12_cross', 'EMA60_REL_shift24',
  # 'EMA60_REL_shift24_cross', 
    
    'EMA75_REL', 'EMA75_REL_shift1',
       'EMA75_REL_shift1_cross', 'EMA75_REL_shift6', 'EMA75_REL_shift6_cross',
       'EMA75_REL_shift12', 'EMA75_REL_shift12_cross', 'EMA75_REL_shift24',
     # 'EMA75_REL_shift24_cross', 
    
    'EMA100_REL', 'EMA100_REL_shift1',
       'EMA100_REL_shift1_cross', 'EMA100_REL_shift6',
       'EMA100_REL_shift6_cross', 'EMA100_REL_shift12',
       'EMA100_REL_shift12_cross', 'EMA100_REL_shift24',
      # 'EMA100_REL_shift24_cross', 
    
    'EMA150_REL', 'EMA150_REL_shift1',
   'EMA150_REL_shift1_cross', 'EMA150_REL_shift6',
       'EMA150_REL_shift6_cross', 'EMA150_REL_shift12',
       'EMA150_REL_shift12_cross', 'EMA150_REL_shift24',
       #'EMA150_REL_shift24_cross', 
    
    'EMA200_REL', 'EMA200_REL_shift1',
    'EMA200_REL_shift1_cross', 'EMA200_REL_shift6',
       'EMA200_REL_shift6_cross', 'EMA200_REL_shift12',
       'EMA200_REL_shift12_cross', 'EMA200_REL_shift24',
       #'EMA200_REL_shift24_cross', 
    
    'MA5_REL', 'MA5_REL_shift1',
       'MA5_REL_shift1_cross', 'MA5_REL_shift6', 'MA5_REL_shift6_cross',
      'MA5_REL_shift12', 'MA5_REL_shift12_cross', 'MA5_REL_shift24',
      'MA5_REL_shift24_cross', 
    
    'MA10_REL', 'MA10_REL_shift1',
 'MA10_REL_shift1_cross', 'MA10_REL_shift6', 'MA10_REL_shift6_cross',
       'MA10_REL_shift12',# 'MA10_REL_shift12_cross', 'MA10_REL_shift24',
      # 'MA10_REL_shift24_cross', 
    
    'MA15_REL', 'MA15_REL_shift1',
       'MA15_REL_shift1_cross', 'MA15_REL_shift6', 'MA15_REL_shift6_cross',
       'MA15_REL_shift12',# 'MA15_REL_shift12_cross', 'MA15_REL_shift24',
     #  'MA15_REL_shift24_cross', 
    
   'MA20_REL', 'MA20_REL_shift1',
       'MA20_REL_shift1_cross', 'MA20_REL_shift6', 'MA20_REL_shift6_cross',
       'MA20_REL_shift12',# 'MA20_REL_shift12_cross', #'MA20_REL_shift24',
      # 'MA20_REL_shift24_cross',
    
    'MA25_REL', 'MA25_REL_shift1',
       'MA25_REL_shift1_cross', 'MA25_REL_shift6', 'MA25_REL_shift6_cross',
       'MA25_REL_shift12',# 'MA25_REL_shift12_cross', 'MA25_REL_shift24',
      # 'MA25_REL_shift24_cross', 
    
    'MA50_REL', 'MA50_REL_shift1',
       'MA50_REL_shift1_cross', 'MA50_REL_shift6', 'MA50_REL_shift6_cross',
       'MA50_REL_shift12',# 'MA50_REL_shift12_cross', 'MA50_REL_shift24',
      # 'MA50_REL_shift24_cross',
    
    'MA75_REL', 'MA75_REL_shift1',
       'MA75_REL_shift1_cross', 'MA75_REL_shift6', 'MA75_REL_shift6_cross',
       'MA75_REL_shift12',# 'MA75_REL_shift12_cross', 'MA75_REL_shift24',
       #'MA75_REL_shift24_cross', 
    
    'MA100_REL', 'MA100_REL_shift1',
      'MA100_REL_shift1_cross', 'MA100_REL_shift6', 'MA100_REL_shift6_cross',
    'MA100_REL_shift12',# 'MA100_REL_shift12_cross', 'MA100_REL_shift24',
      #'MA100_REL_shift24_cross', 
    
'MA150_REL', 'MA150_REL_shift1',
       'MA150_REL_shift1_cross', 'MA150_REL_shift6', 'MA150_REL_shift6_cross',
       'MA150_REL_shift12',# 'MA150_REL_shift12_cross', 'MA150_REL_shift24',
     #  'MA150_REL_shift24_cross', 
    
    'MA200_REL', 'MA200_REL_shift1',
       'MA200_REL_shift1_cross', 'MA200_REL_shift6', 'MA200_REL_shift6_cross',
       'MA200_REL_shift12',# 'MA200_REL_shift12_cross', 'MA200_REL_shift24',
     # 'MA200_REL_shift24_cross', 
    
    'MACDHist_REL', 'MACDHist_REL_shift0',
      'MACDHist_REL_shift1', 'MACDHist_REL_shift3', 'MACDHist_REL_shift5','MACDHist_REL_shift7',
    
    

       'MACDHist_REL_shift10', 'RSI9_up_70', 'RSI9_dw_30', 'RSI9_up_80',
       'RSI9_dw_20', 'RSI14_up_70', 'RSI14_dw_30', 'RSI14_up_80',
       'RSI14_dw_20', 'RSI20_up_70', 'RSI20_dw_30', 'RSI20_up_80',
       'RSI20_dw_20', 'RSI27_up_70', 'RSI27_dw_30', 'RSI27_up_80',
    'RSI27_dw_20', 'EMA_gor_1_REL_cross_all', 'EMA_gor_6_REL_cross_all',
       'EMA_gor_12_REL_cross_all', 'EMA_gor_24_REL_cross_all',
     'MA_gor_1_REL_cross_all', 'MA_gor_6_REL_cross_all',
       'MA_gor_12_REL_cross_all', 'MA_gor_24_REL_cross_all',
    
    
    
       'date_key_h', 'date_key_d',  #(вообще норм, но )
    #'std_20',
    'std_20_rel',
    'std_100_rel',
    'RSI14_coef_nak', 
    'Close_coef_nak', 
    'Volume_coef_nak', 
    'EMA14_coef_nak',
    'MA100_coef_nak', 
    'std_20_coef_nak',
    'MACDHist_nak',
    


    
     'Close_coef_nak_div_Volume_coef_nak',
       'Close_coef_nak_div_RSI14_coef_nak', 
    
       'Close_coef_nak_div_MACDHist_nak',
    
      'Close_0_to_1', 'Close_1_to_2', 'Close_2_to_3',
       'Close_3_to_4', 'Close_4_to_5', 'Close_5_to_6', 'Close_6_to_7',
       'Close_7_to_8', 'Close_8_to_9', 'Close_9_to_10', 'Close_10_to_11',
       'Close_11_to_12',
    
    
    'Close_0_to_3', 'Close_0_to_4', 'Close_0_to_5',
       'Close_0_to_6', 'Close_0_to_9', 'Close_0_to_12',
    
     'Close_m3_0_to_MA15',
       'Close_m3_1_to_MA15', 'Close_m3_2_to_MA15', 'Close_m3_3_to_MA15',
       'Close_m3_4_to_MA15', 'Close_m3_5_to_MA15', 'Close_m3_6_to_MA15',
       'Close_m3_9_to_MA15', 'Close_m3_12_to_MA15',
    
    'Close_0_to_MA15',
       'Close_1_to_MA15', 'Close_2_to_MA15', 'Close_3_to_MA15',
       'Close_4_to_MA15', 'Close_5_to_MA15', 'Close_6_to_MA15',
       'Close_7_to_MA15', 'Close_8_to_MA15', 'Close_9_to_MA15',
       'Close_10_to_MA15', 'Close_11_to_MA15', 'Close_12_to_MA15',
       'Close_13_to_MA15', 'Close_14_to_MA15', 'Close_15_to_MA15',
    
    
     'RSI9_up_70_perman',
       'RSI9_dw_30_perman',# 'RSI9_up_80_perman', 'RSI9_dw_20_perman',
       'RSI14_up_70_perman', 'RSI14_dw_30_perman', #'RSI14_up_80_perman',
       'RSI14_dw_20_perman', 
    'RSI20_up_70_perman', 'RSI20_dw_30_perman',
      #'RSI20_up_80_perman', 'RSI20_dw_20_perman', 
    'RSI27_up_70_perman',
       'RSI27_dw_30_perman',# 'RSI27_up_80_perman', 'RSI27_dw_20_perman',
    
    
#     'RSI9_up_70',
#        'RSI9_dw_30', 'RSI9_up_80', 'RSI9_dw_20', 'RSI14_up_70', 'RSI14_dw_30',
#        'RSI14_up_80', 'RSI14_dw_20', 'RSI20_up_70', 'RSI20_dw_30',
#        'RSI20_up_80', 'RSI20_dw_20', 'RSI27_up_70', 'RSI27_dw_30',
#        'RSI27_up_80', 'RSI27_dw_20',

    
    #'MACD',
   # 'Signal',
    'RSI9',
    'RSI14',
    'RSI20',
    'RSI27',

    'level_close_old_w',
     'level_close_act_w',
    'step_to_fiba',
    
    
    
    'MACDHist_corr_shift0','MACDHist_corr_shift1', 'MACDHist_corr_shift3', 'MACDHist_corr_shift6',
      
    #'MACDHist_shift0', 'MACDHist_shift1','MACDHist_shift3', 'MACDHist_shift6', 
    
    #'AweOs_shift0', 'AweOs_shift1', 'AweOs_shift3', 'AweOs_shift6',
       
    'AweOs_cor_shift0', 'AweOs_cor_shift1','AweOs_cor_shift3', 'AweOs_cor_shift6',
     
    'MACDHist_corr_0_to_1','MACDHist_corr_1_to_3', 'MACDHist_corr_3_to_6',
    
    'MACDHist_0_to_1','MACDHist_1_to_3', 'MACDHist_3_to_6',
    
    'AweOs_0_to_1', 'AweOs_1_to_3','AweOs_3_to_6', 
    
    'AweOs_corr_0_to_1', 'AweOs_corr_1_to_3','AweOs_corr_3_to_6',
    
    #'Close8_plus_100','Close8_minus_100','Close8_dif_100',
    'Close_coef_nak2',
    
        'SV_DIR_shift0',
       'SV_DIR_shift1', 'SV_DIR_shift2', 'SV_DIR_shift3', 'SV_DIR_shift4',
       'SV_DIR_shift5', 'SV_DIR_shift6',
     'SV_DIR_shift7', 'SV_DIR_shift8',
#        'SV_DIR_shift9', 'SV_DIR_shift10', 'SV_DIR_shift11',
    
     'PER_OPEN_shift0', 'PER_OPEN_shift1', 'PER_OPEN_shift2',
       'PER_OPEN_shift3', 'PER_OPEN_shift4', 'PER_OPEN_shift5',
       'PER_OPEN_shift6',
    'PER_OPEN_shift7', 'PER_OPEN_shift8',
#        'PER_OPEN_shift9', 'PER_OPEN_shift10', 'PER_OPEN_shift11',
    
    'PER_CLOSE_shift0', 'PER_CLOSE_shift1',
       'PER_CLOSE_shift2', 'PER_CLOSE_shift3', 'PER_CLOSE_shift4',
       'PER_CLOSE_shift5',# 'PER_CLOSE_shift6', 
#     'PER_CLOSE_shift7',
#        'PER_CLOSE_shift8', 'PER_CLOSE_shift9', 'PER_CLOSE_shift10',
#        'PER_CLOSE_shift11',
    
    'type_molot_shift0', 'type_molot_shift1',
       'type_molot_shift2', 'type_molot_shift3', 'type_molot_shift4',
       'type_molot_shift5', #'type_molot_shift6', 
    'type_molot_shift7',
#        'type_molot_shift8', 'type_molot_shift9', 'type_molot_shift10',
#        'type_molot_shift11',
    
    
    'POLNOTA_shift0', 'POLNOTA_shift1', 'POLNOTA_shift2',
       'POLNOTA_shift3', 'POLNOTA_shift4', #'POLNOTA_shift5',# 'POLNOTA_shift6',
       'POLNOTA_shift7', 'POLNOTA_shift8', 'POLNOTA_shift9', 'POLNOTA_shift10',
       'POLNOTA_shift11',
    
    'Close_0_to_b', 'Close_1_to_b',
       'Close_2_to_b', 'Close_3_to_b', 'Close_4_to_b', 'Close_5_to_b',
       'Open_0_to_b', 'Open_1_to_b', 'Open_2_to_b', 'Open_3_to_b',
       'Open_4_to_b', 'Open_5_to_b', 'Low_0_to_b', 'Low_1_to_b', 'Low_2_to_b',
       'Low_3_to_b', 'Low_4_to_b', 'Low_5_to_b', 'High_0_to_b', 'High_1_to_b',
       'High_2_to_b', 'High_3_to_b', 'High_4_to_b', 'High_5_to_b',
    
    'EVENT22',
       'EVENT21', 'EVENT20', 'EVENT19', 'EVENT18', 'EVENT17', 'EVENT16',
       'EVENT15', 'EVENT14', 'EVENT13', 'EVENT12', 'EVENT11', 'EVENT10',
       'EVENT9', 'EVENT8', 'EVENT7', 'EVENT6', 'EVENT5', 'EVENT4', 'EVENT3',
       'EVENT2', 'EVENT1',
        'down_near',
    'up_near',
    'mae_opt_near',
    'down_far',
    'up_far',
    'mae_opt_far',
    
    
#     'x0_0',
#        'x0_1', 'x0_2', 'x0_3', 'x0_4', 'x0_5', 'x0_6', 'x0_7', 'x0_8', 'x0_9',
#        'x0_10', 'x0_11',
    
    'freq_up_all_300', 'freq_dw_all_300', 'freq_up_ch_300',
       'freq_dw_ch_300', 'freq_up_all_100', 'freq_dw_all_100',
       'freq_up_ch_100', 'freq_dw_ch_100', 'freq_up_all_50', 'freq_dw_all_50',
       'freq_up_ch_50', 'freq_dw_ch_50', 'plotnost_300_all', 'plotnost_300_ch',
       'plotnost_100_all', 'plotnost_100_ch', 'plotnost_50_all',
       'plotnost_50_ch', 'balance_300_all', 'balance_300_ch',
       'balance_100_all', 'balance_100_ch', 'balance_50_all', 'balance_50_ch',
    
    
    'EMA8_REL_shift24_cross', 'EMA12_REL_shift24_cross', 'EMA14_REL_shift24_cross',
'EMA20_REL_shift24_cross', 'EMA26_REL_shift24_cross', 'EMA32_REL_shift24_cross',
'EMA38_REL_shift24_cross', 'EMA44_REL_shift24_cross', 'EMA50_REL_shift24_cross',
'EMA60_REL_shift24_cross', 'EMA75_REL_shift24_cross', 'EMA100_REL_shift24_cross',
'EMA150_REL_shift24_cross',
'EMA200_REL_shift24_cross', 'MA10_REL_shift12_cross',
 'MA15_REL_shift24_cross', 'MA20_REL_shift12_cross', 'MA20_REL_shift24', 'MA20_REL_shift24_cross',
    'MA25_REL_shift12_cross', 'MA25_REL_shift24', 'MA25_REL_shift24_cross', 'MA50_REL_shift12_cross',
    'MA50_REL_shift24', 'MA50_REL_shift24_cross', 'MA75_REL_shift12_cross',
    'MA75_REL_shift24', 'MA75_REL_shift24_cross', 'MA100_REL_shift12_cross', 'MA100_REL_shift24', 'MA100_REL_shift24_cross',
    'MA150_REL_shift12_cross', 'MA150_REL_shift24', 'MA150_REL_shift24_cross', 'MA200_REL_shift12_cross',
    'MA200_REL_shift24', 'MA200_REL_shift24_cross', 'RSI9_up_80_perman', 'RSI9_dw_20_perman', 'RSI14_up_80_perman', 'RSI20_up_80_perman', 'RSI20_dw_20_perman', 'RSI27_up_80_perman',
    'RSI27_dw_20_perman', # 'std_500_rel',
     'MACDHist_corr_roll_mean3', 'MACDHist_corr_roll_mean3_shift0', 'MACDHist_corr_roll_mean3_shift1',
'MACDHist_corr_roll_mean3_shift3', 'MACDHist_corr_roll_mean3_shift6',
'AweOs_cor_roll_mean3', 'AweOs_cor_roll_mean3_shift0', 'AweOs_cor_roll_mean3_shift1', 'AweOs_cor_roll_mean3_shift3',
'AweOs_cor_roll_mean3_shift6'

    
]







###########################################################################################################################
###############################################    4H     #################################################################
###########################################################################################################################




####################       4H      ВЕРСИЯ 25.06



# версия 25.06
# col_fin_up_4h=['MACDHist_corr', 'AweOs_cor', 'ROC200', 'ROC200sm', 'TSI', 'EMA8_REL', 'EMA8_REL_shift1', 'EMA8_REL_shift12', 'EMA8_REL_shift24', 'EMA12_REL_shift12', 'EMA12_REL_shift24', 'EMA14_REL_shift24', 'EMA20_REL', 'EMA20_REL_shift6', 'EMA20_REL_shift24', 'EMA26_REL', 'EMA26_REL_shift6', 'EMA26_REL_shift12', 'EMA32_REL_shift24', 'EMA38_REL_shift6', 'EMA38_REL_shift24', 'EMA44_REL_shift1', 'EMA50_REL', 'EMA50_REL_shift12', 'EMA50_REL_shift24', 'EMA60_REL', 'EMA60_REL_shift1', 'EMA60_REL_shift6', 'EMA60_REL_shift12', 'EMA60_REL_shift24', 'EMA75_REL_shift1_cross', 'EMA75_REL_shift24', 'EMA100_REL', 'EMA100_REL_shift6', 'EMA100_REL_shift12', 'EMA100_REL_shift24', 'EMA150_REL', 'EMA150_REL_shift6', 'EMA150_REL_shift12', 'EMA150_REL_shift24', 'EMA150_REL_shift24_cross', 'EMA200_REL', 'EMA200_REL_shift1', 'EMA200_REL_shift6', 'EMA200_REL_shift12', 'EMA200_REL_shift24', 'MA5_REL', 'MA5_REL_shift1', 'MA5_REL_shift6', 'MA5_REL_shift12', 'MA5_REL_shift24', 'MA10_REL', 'MA10_REL_shift6', 'MA10_REL_shift12', 'MA10_REL_shift24', 'MA15_REL', 'MA15_REL_shift6', 'MA15_REL_shift12', 'MA15_REL_shift24', 'MA20_REL', 'MA20_REL_shift6', 'MA20_REL_shift24', 'MA25_REL', 'MA25_REL_shift6', 'MA25_REL_shift12', 'MA25_REL_shift12_cross', 'MA25_REL_shift24', 'MA50_REL', 'MA50_REL_shift1', 'MA50_REL_shift6', 'MA50_REL_shift12', 'MA50_REL_shift12_cross', 'MA50_REL_shift24', 'MA75_REL', 'MA75_REL_shift1', 'MA75_REL_shift6', 'MA75_REL_shift12', 'MA75_REL_shift24', 'MA100_REL', 'MA100_REL_shift1', 'MA100_REL_shift6', 'MA100_REL_shift12', 'MA100_REL_shift12_cross', 'MA100_REL_shift24', 'MA150_REL', 'MA150_REL_shift1', 'MA150_REL_shift6', 'MA150_REL_shift12', 'MA150_REL_shift24', 'MA200_REL', 'MA200_REL_shift1', 'MA200_REL_shift6', 'MA200_REL_shift12', 'MA200_REL_shift24', 'MACDHist_REL', 'MACDHist_REL_shift1', 'MACDHist_REL_shift3', 'MACDHist_REL_shift5', 'MACDHist_REL_shift7', 'MACDHist_REL_shift10', 'EMA_gor_6_REL_cross_all', 'EMA_gor_12_REL_cross_all', 'EMA_gor_24_REL_cross_all', 'MA_gor_24_REL_cross_all', 'date_key_h', 'date_key_d', 'std_20_rel', 'std_100_rel', 'RSI14_coef_nak', 'Close_coef_nak', 'Volume_coef_nak', 'EMA14_coef_nak', 'MA100_coef_nak', 'std_20_coef_nak', 'MACDHist_nak', 'Close_coef_nak_div_Volume_coef_nak', 'Close_coef_nak_div_RSI14_coef_nak', 'Close_coef_nak_div_MACDHist_nak', 'Close_0_to_1', 'Close_1_to_2', 'Close_2_to_3', 'Close_3_to_4', 'Close_4_to_5', 'Close_5_to_6', 'Close_6_to_7', 'Close_7_to_8', 'Close_8_to_9', 'Close_9_to_10', 'Close_10_to_11', 'Close_11_to_12', 'Close_0_to_3', 'Close_0_to_4', 'Close_0_to_5', 'Close_0_to_6', 'Close_0_to_9', 'Close_0_to_12', 'Close_m3_0_to_MA15', 'Close_m3_1_to_MA15', 'Close_m3_2_to_MA15', 'Close_m3_3_to_MA15', 'Close_m3_4_to_MA15', 'Close_m3_5_to_MA15', 'Close_m3_6_to_MA15', 'Close_m3_9_to_MA15', 'Close_m3_12_to_MA15', 'Close_2_to_MA15', 'Close_3_to_MA15', 'Close_4_to_MA15', 'Close_5_to_MA15', 'Close_6_to_MA15', 'Close_7_to_MA15', 'Close_8_to_MA15', 'Close_9_to_MA15', 'Close_10_to_MA15', 'Close_11_to_MA15', 'Close_12_to_MA15', 'Close_13_to_MA15', 'Close_14_to_MA15', 'Close_15_to_MA15', 'RSI20_up_70_perman', 'RSI27_dw_30_perman', 'RSI9', 'RSI14', 'RSI20', 'RSI27', 'level_close_old_w', 'level_close_act_w', 'step_to_fiba', 'MACDHist_corr_shift1', 'MACDHist_corr_shift3', 'MACDHist_corr_shift6', 'AweOs_cor_shift1', 'AweOs_cor_shift3', 'AweOs_cor_shift6', 'MACDHist_corr_0_to_1', 'MACDHist_corr_1_to_3', 'MACDHist_corr_3_to_6', 'MACDHist_0_to_1', 'MACDHist_1_to_3', 'MACDHist_3_to_6', 'AweOs_0_to_1', 'AweOs_1_to_3', 'AweOs_3_to_6', 'AweOs_corr_0_to_1', 'Close_coef_nak2']




# версия 25.06
# col_fin_dw_4h=['MACDHist_corr', 'AweOs_cor', 'ROC200', 'ROC200sm', 'TSI', 'EMA8_REL_shift12', 'EMA8_REL_shift24', 'EMA12_REL', 'EMA20_REL_shift6', 'EMA20_REL_shift24', 'EMA26_REL', 'EMA26_REL_shift1', 'EMA32_REL', 'EMA32_REL_shift6', 'EMA38_REL_shift6', 'EMA44_REL_shift12', 'EMA50_REL_shift12', 'EMA50_REL_shift24', 'EMA60_REL', 'EMA60_REL_shift6', 'EMA100_REL', 'EMA100_REL_shift1', 'EMA100_REL_shift12', 'EMA100_REL_shift24', 'EMA150_REL', 'EMA150_REL_shift12', 'EMA150_REL_shift24', 'EMA200_REL', 'EMA200_REL_shift1', 'EMA200_REL_shift6', 'EMA200_REL_shift12', 'EMA200_REL_shift24', 'EMA200_REL_shift24_cross', 'MA5_REL', 'MA5_REL_shift1', 'MA5_REL_shift6', 'MA5_REL_shift12', 'MA5_REL_shift24', 'MA10_REL', 'MA10_REL_shift12', 'MA10_REL_shift24', 'MA15_REL', 'MA15_REL_shift6', 'MA15_REL_shift12', 'MA15_REL_shift24', 'MA20_REL_shift12', 'MA20_REL_shift24', 'MA25_REL', 'MA25_REL_shift6', 'MA25_REL_shift12', 'MA25_REL_shift24', 'MA50_REL', 'MA50_REL_shift1', 'MA50_REL_shift6', 'MA50_REL_shift12', 'MA50_REL_shift24', 'MA75_REL', 'MA75_REL_shift6', 'MA75_REL_shift12', 'MA75_REL_shift24', 'MA100_REL', 'MA100_REL_shift1', 'MA100_REL_shift6', 'MA100_REL_shift12', 'MA100_REL_shift24', 'MA150_REL', 'MA150_REL_shift1', 'MA150_REL_shift6', 'MA150_REL_shift12', 'MA150_REL_shift24', 'MA200_REL', 'MA200_REL_shift1', 'MA200_REL_shift6', 'MA200_REL_shift12', 'MA200_REL_shift12_cross', 'MA200_REL_shift24', 'MA200_REL_shift24_cross', 'MACDHist_REL', 'MACDHist_REL_shift3', 'MACDHist_REL_shift5', 'MACDHist_REL_shift7', 'MACDHist_REL_shift10', 'EMA_gor_6_REL_cross_all', 'EMA_gor_12_REL_cross_all', 'EMA_gor_24_REL_cross_all', 'MA_gor_24_REL_cross_all', 'date_key_d', 'std_20_rel', 'std_100_rel', 'RSI14_coef_nak', 'Close_coef_nak', 'Volume_coef_nak', 'EMA14_coef_nak', 'MA100_coef_nak', 'std_20_coef_nak', 'MACDHist_nak', 'Close_coef_nak_div_Volume_coef_nak', 'Close_coef_nak_div_RSI14_coef_nak', 'Close_coef_nak_div_MACDHist_nak', 'Close_0_to_1', 'Close_1_to_2', 'Close_3_to_4', 'Close_4_to_5', 'Close_6_to_7', 'Close_7_to_8', 'Close_8_to_9', 'Close_9_to_10', 'Close_10_to_11', 'Close_0_to_4', 'Close_0_to_5', 'Close_0_to_6', 'Close_0_to_9', 'Close_m3_0_to_MA15', 'Close_m3_2_to_MA15', 'Close_m3_3_to_MA15', 'Close_m3_4_to_MA15', 'Close_m3_5_to_MA15', 'Close_m3_6_to_MA15', 'Close_m3_9_to_MA15', 'Close_m3_12_to_MA15', 'Close_3_to_MA15', 'Close_4_to_MA15', 'Close_5_to_MA15', 'Close_6_to_MA15', 'Close_7_to_MA15', 'Close_8_to_MA15', 'Close_9_to_MA15', 'Close_10_to_MA15', 'Close_11_to_MA15', 'Close_12_to_MA15', 'Close_13_to_MA15', 'Close_15_to_MA15', 'RSI20_up_70_perman', 'RSI27_dw_30_perman', 'RSI9', 'RSI14', 'RSI20', 'RSI27', 'level_close_old_w', 'level_close_act_w', 'step_to_fiba', 'MACDHist_corr_shift1', 'MACDHist_corr_shift3', 'MACDHist_corr_shift6', 'AweOs_cor_shift1', 'AweOs_cor_shift3', 'AweOs_cor_shift6', 'MACDHist_corr_0_to_1', 'MACDHist_corr_1_to_3', 'MACDHist_corr_3_to_6', 'MACDHist_0_to_1', 'MACDHist_3_to_6', 'AweOs_0_to_1', 'AweOs_1_to_3', 'AweOs_3_to_6', 'AweOs_corr_0_to_1', 'Close_coef_nak2']



#версия 25.06
# MODEL_PARAMS_DW_4H = {

# #     'boosting_type':'dart',
#       'num_leaves': 80, 
#       'max_depth': 8, 
# #      'learning_rate': 0.1,
#       'n_estimators': 100,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7, 
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
# #      'reg_lambda': 50,
# #      'random_state': 42, 
#     'scale_pos_weight': 1,
#       'n_jobs': 10
# }


#версия 25.06
# MODEL_PARAMS_UP_4H = {

#  #    'boosting_type':'goss',
#       'num_leaves': 80, 
# #      'max_depth': 9, 
# #      'learning_rate': 0.13,
#       'n_estimators': 200,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7, 
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
# #      'reg_lambda': 0,
# #      'random_state': 42, 
# #    'scale_pos_weight': 4,
#       'n_jobs': 10
# }



####################       4H      ВЕРСИЯ 28.06


# #версия 28.06  добавлены эвенты
# col_fin_up_4h=['MACDHist_corr', 'AweOs_cor', 'ROC200', 'ROC200sm', 'TSI', 'EMA8_REL_shift12', 'EMA8_REL_shift24', 'EMA12_REL_shift6', 'EMA12_REL_shift24', 'EMA20_REL_shift6', 'EMA26_REL', 'EMA26_REL_shift6', 'EMA26_REL_shift12', 'EMA26_REL_shift24', 'EMA50_REL_shift6', 'EMA50_REL_shift24', 'EMA60_REL', 'EMA60_REL_shift24', 'EMA75_REL', 'EMA75_REL_shift1_cross', 'EMA75_REL_shift6', 'EMA100_REL', 'EMA100_REL_shift12', 'EMA100_REL_shift24', 'EMA150_REL', 'EMA150_REL_shift6', 'EMA150_REL_shift12', 'EMA150_REL_shift24', 'EMA200_REL', 'EMA200_REL_shift1', 'EMA200_REL_shift6', 'EMA200_REL_shift12', 'EMA200_REL_shift24', 'MA5_REL_shift6', 'MA5_REL_shift12', 'MA5_REL_shift24', 'MA10_REL', 'MA10_REL_shift12', 'MA10_REL_shift24', 'MA15_REL', 'MA15_REL_shift12', 'MA15_REL_shift24', 'MA20_REL_shift12', 'MA20_REL_shift24', 'MA25_REL', 'MA25_REL_shift6', 'MA25_REL_shift12', 'MA25_REL_shift24', 'MA50_REL', 'MA50_REL_shift1', 'MA50_REL_shift6', 'MA50_REL_shift12', 'MA50_REL_shift24', 'MA75_REL', 'MA75_REL_shift1', 'MA75_REL_shift6', 'MA75_REL_shift12', 'MA75_REL_shift24', 'MA100_REL', 'MA100_REL_shift1', 'MA100_REL_shift6', 'MA100_REL_shift12', 'MA100_REL_shift24', 'MA150_REL', 'MA150_REL_shift1', 'MA150_REL_shift6', 'MA150_REL_shift12', 'MA150_REL_shift24', 'MA200_REL', 'MA200_REL_shift1', 'MA200_REL_shift6', 'MA200_REL_shift12', 'MA200_REL_shift24', 'MACDHist_REL', 'MACDHist_REL_shift1', 'MACDHist_REL_shift3', 'MACDHist_REL_shift5', 'MACDHist_REL_shift7', 'MACDHist_REL_shift10', 'EMA_gor_12_REL_cross_all', 'MA_gor_24_REL_cross_all', 'date_key_h', 'date_key_d', 'std_20_rel', 'std_100_rel', 'RSI14_coef_nak', 'Close_coef_nak', 'Volume_coef_nak', 'EMA14_coef_nak', 'MA100_coef_nak', 'std_20_coef_nak', 'MACDHist_nak', 'Close_coef_nak_div_Volume_coef_nak', 'Close_coef_nak_div_RSI14_coef_nak', 'Close_coef_nak_div_MACDHist_nak', 'Close_1_to_2', 'Close_3_to_4', 'Close_4_to_5', 'Close_5_to_6', 'Close_6_to_7', 'Close_7_to_8', 'Close_9_to_10', 'Close_10_to_11', 'Close_11_to_12', 'Close_0_to_4', 'Close_0_to_6', 'Close_0_to_9', 'Close_m3_1_to_MA15', 'Close_m3_3_to_MA15', 'Close_m3_4_to_MA15', 'Close_m3_5_to_MA15', 'Close_m3_6_to_MA15', 'Close_m3_9_to_MA15', 'Close_m3_12_to_MA15', 'Close_4_to_MA15', 'Close_6_to_MA15', 'Close_7_to_MA15', 'Close_8_to_MA15', 'Close_9_to_MA15', 'Close_10_to_MA15', 'Close_11_to_MA15', 'Close_12_to_MA15', 'Close_13_to_MA15', 'Close_14_to_MA15', 'Close_15_to_MA15', 'RSI27_dw_30_perman', 'RSI9', 'RSI14', 'RSI20', 'RSI27', 'level_close_old_w', 'level_close_act_w', 'step_to_fiba', 'MACDHist_corr_shift1', 'MACDHist_corr_shift3', 'MACDHist_corr_shift6', 'AweOs_cor_shift1', 'AweOs_cor_shift3', 'AweOs_cor_shift6', 'MACDHist_corr_0_to_1', 'MACDHist_corr_1_to_3', 'MACDHist_3_to_6', 'AweOs_0_to_1', 'AweOs_1_to_3', 'AweOs_3_to_6', 'AweOs_corr_0_to_1', 'Close_coef_nak2', 'PER_OPEN_shift0', 'PER_OPEN_shift1', 'PER_OPEN_shift2', 'PER_OPEN_shift3', 'PER_OPEN_shift4', 'PER_OPEN_shift6', 'PER_CLOSE_shift0', 'PER_CLOSE_shift1', 'PER_CLOSE_shift2', 'PER_CLOSE_shift3', 'PER_CLOSE_shift5', 'PER_CLOSE_shift6', 'POLNOTA_shift0', 'POLNOTA_shift1', 'POLNOTA_shift2', 'POLNOTA_shift3', 'POLNOTA_shift4', 'POLNOTA_shift5', 'POLNOTA_shift6', 'Close_2_to_b', 'Close_3_to_b', 'Close_4_to_b', 'Open_0_to_b', 'Open_5_to_b', 'Low_0_to_b', 'Low_1_to_b', 'Low_2_to_b', 'Low_3_to_b', 'Low_4_to_b', 'High_1_to_b', 'High_4_to_b', 'High_5_to_b', 'EVENT20', 'EVENT19', 'EVENT16', 'EVENT15', 'EVENT14', 'EVENT13', 'EVENT11', 'EVENT10', 'EVENT9', 'EVENT4', 'EVENT3']




# #версия 28.06
# col_fin_dw_4h=['MACDHist_corr', 'AweOs_cor', 'ROC200', 'ROC200sm', 'TSI', 'EMA8_REL', 'EMA8_REL_shift12', 'EMA8_REL_shift24', 'EMA12_REL_shift12', 'EMA20_REL_shift6', 'EMA26_REL_shift6', 'EMA26_REL_shift12', 'EMA26_REL_shift24', 'EMA32_REL', 'EMA32_REL_shift6', 'EMA38_REL_shift24', 'EMA44_REL_shift6', 'EMA60_REL', 'EMA60_REL_shift12', 'EMA75_REL_shift6', 'EMA75_REL_shift24', 'EMA100_REL', 'EMA100_REL_shift12', 'EMA100_REL_shift24', 'EMA150_REL', 'EMA150_REL_shift12', 'EMA150_REL_shift24', 'EMA200_REL', 'EMA200_REL_shift1', 'EMA200_REL_shift6', 'EMA200_REL_shift12', 'EMA200_REL_shift24', 'MA5_REL_shift12', 'MA5_REL_shift24', 'MA10_REL', 'MA10_REL_shift1', 'MA10_REL_shift6', 'MA10_REL_shift12', 'MA10_REL_shift24', 'MA15_REL_shift6', 'MA15_REL_shift24', 'MA20_REL', 'MA20_REL_shift12', 'MA20_REL_shift24', 'MA25_REL_shift12', 'MA25_REL_shift24', 'MA50_REL', 'MA50_REL_shift1', 'MA50_REL_shift6', 'MA50_REL_shift12', 'MA50_REL_shift24', 'MA75_REL', 'MA75_REL_shift1', 'MA75_REL_shift6', 'MA75_REL_shift12', 'MA75_REL_shift24', 'MA100_REL', 'MA100_REL_shift1', 'MA100_REL_shift6', 'MA100_REL_shift12', 'MA100_REL_shift24', 'MA150_REL', 'MA150_REL_shift1', 'MA150_REL_shift6', 'MA150_REL_shift12', 'MA150_REL_shift24', 'MA200_REL', 'MA200_REL_shift1', 'MA200_REL_shift12', 'MA200_REL_shift12_cross', 'MA200_REL_shift24', 'MA200_REL_shift24_cross', 'MACDHist_REL', 'MACDHist_REL_shift1', 'MACDHist_REL_shift3', 'MACDHist_REL_shift5', 'MACDHist_REL_shift7', 'MACDHist_REL_shift10', 'EMA_gor_24_REL_cross_all', 'MA_gor_6_REL_cross_all', 'MA_gor_12_REL_cross_all', 'date_key_d', 'std_20_rel', 'std_100_rel', 'RSI14_coef_nak', 'Close_coef_nak', 'Volume_coef_nak', 'EMA14_coef_nak', 'MA100_coef_nak', 'std_20_coef_nak', 'MACDHist_nak', 'Close_coef_nak_div_Volume_coef_nak', 'Close_coef_nak_div_RSI14_coef_nak', 'Close_coef_nak_div_MACDHist_nak', 'Close_0_to_1', 'Close_1_to_2', 'Close_4_to_5', 'Close_5_to_6', 'Close_6_to_7', 'Close_7_to_8', 'Close_8_to_9', 'Close_9_to_10', 'Close_10_to_11', 'Close_11_to_12', 'Close_0_to_3', 'Close_0_to_4', 'Close_0_to_9', 'Close_m3_1_to_MA15', 'Close_m3_2_to_MA15', 'Close_m3_3_to_MA15', 'Close_m3_4_to_MA15', 'Close_m3_5_to_MA15', 'Close_m3_6_to_MA15', 'Close_m3_9_to_MA15', 'Close_m3_12_to_MA15', 'Close_2_to_MA15', 'Close_3_to_MA15', 'Close_4_to_MA15', 'Close_5_to_MA15', 'Close_7_to_MA15', 'Close_8_to_MA15', 'Close_9_to_MA15', 'Close_10_to_MA15', 'Close_11_to_MA15', 'Close_12_to_MA15', 'Close_13_to_MA15', 'Close_14_to_MA15', 'Close_15_to_MA15', 'RSI20_up_70_perman', 'RSI27_dw_30_perman', 'RSI9', 'RSI14', 'RSI20', 'RSI27', 'level_close_old_w', 'level_close_act_w', 'step_to_fiba', 'MACDHist_corr_shift1', 'MACDHist_corr_shift3', 'MACDHist_corr_shift6', 'AweOs_cor_shift1', 'AweOs_cor_shift3', 'AweOs_cor_shift6', 'MACDHist_corr_0_to_1', 'MACDHist_corr_1_to_3', 'MACDHist_corr_3_to_6', 'MACDHist_0_to_1', 'MACDHist_1_to_3', 'MACDHist_3_to_6', 'AweOs_0_to_1', 'AweOs_1_to_3', 'AweOs_3_to_6', 'AweOs_corr_0_to_1', 'Close_coef_nak2', 'PER_OPEN_shift0', 'PER_OPEN_shift1', 'PER_OPEN_shift2', 'PER_OPEN_shift3', 'PER_OPEN_shift4', 'PER_OPEN_shift5', 'PER_OPEN_shift6', 'PER_CLOSE_shift0', 'PER_CLOSE_shift1', 'PER_CLOSE_shift2', 'PER_CLOSE_shift3', 'PER_CLOSE_shift4', 'PER_CLOSE_shift5', 'PER_CLOSE_shift6', 'POLNOTA_shift0', 'POLNOTA_shift1', 'POLNOTA_shift2', 'POLNOTA_shift3', 'POLNOTA_shift4', 'POLNOTA_shift5', 'POLNOTA_shift6', 'Close_2_to_b', 'Close_3_to_b', 'Close_4_to_b', 'Close_5_to_b', 'Open_0_to_b', 'Open_1_to_b', 'Open_5_to_b', 'Low_0_to_b', 'Low_1_to_b', 'Low_2_to_b', 'Low_3_to_b', 'Low_4_to_b', 'Low_5_to_b', 'High_0_to_b', 'High_1_to_b', 'High_2_to_b', 'High_3_to_b', 'High_4_to_b', 'High_5_to_b', 'EVENT19', 'EVENT16', 'EVENT15', 'EVENT14', 'EVENT13', 'EVENT10', 'EVENT4', 'EVENT3']





# #версия 28.06
# MODEL_PARAMS_DW_4H = {

#      'boosting_type':'dart',
# #      'num_leaves': 90, 
# #      'max_depth': 8, 
# #      'learning_rate': 0.1,
#       'n_estimators': 100,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7, 
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
#       'reg_lambda': 90,
# #      'random_state': 42, 
#     'scale_pos_weight': 1,
#       'n_jobs': 10
# }




# #версия 28.06
# MODEL_PARAMS_UP_4H = {

#     'boosting_type':'dart',
# #      'num_leaves': 80, 
# #      'max_depth': 9, 
# #      'learning_rate': 0.13,
# #      'n_estimators': 200,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7, 
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
#       'reg_lambda': 75,
# #      'random_state': 42, 
# #    'scale_pos_weight': 4,
#       'n_jobs': 10
# }






####################       4H      ВЕРСИЯ 07.07





# #версия 07.07  добавлены синусойды 1
# col_fin_up_4h=['MACDHist_corr', 'AweOs_cor', 'ROC200', 'ROC200sm', 'TSI', 'EMA8_REL_shift12', 'EMA8_REL_shift24', 'EMA12_REL', 'EMA12_REL_shift6', 'EMA12_REL_shift24', 'EMA14_REL_shift12', 'EMA20_REL_shift6', 'EMA20_REL_shift24', 'EMA26_REL_shift6', 'EMA26_REL_shift12', 'EMA26_REL_shift24', 'EMA38_REL_shift6', 'EMA38_REL_shift24', 'EMA50_REL', 'EMA50_REL_shift6', 'EMA50_REL_shift24', 'EMA60_REL_shift12', 'EMA60_REL_shift24', 'EMA75_REL', 'EMA75_REL_shift1_cross', 'EMA75_REL_shift6', 'EMA75_REL_shift12', 'EMA100_REL', 'EMA100_REL_shift6', 'EMA100_REL_shift12', 'EMA150_REL', 'EMA150_REL_shift1', 'EMA150_REL_shift6', 'EMA150_REL_shift12', 'EMA150_REL_shift24', 'EMA200_REL', 'EMA200_REL_shift1', 'EMA200_REL_shift6', 'EMA200_REL_shift12', 'EMA200_REL_shift24', 'MA5_REL', 'MA5_REL_shift6', 'MA5_REL_shift12', 'MA5_REL_shift24', 'MA10_REL', 'MA10_REL_shift6', 'MA10_REL_shift12', 'MA10_REL_shift24', 'MA15_REL', 'MA15_REL_shift12', 'MA15_REL_shift24', 'MA20_REL', 'MA20_REL_shift6', 'MA20_REL_shift12', 'MA20_REL_shift24', 'MA25_REL', 'MA25_REL_shift6', 'MA25_REL_shift12', 'MA25_REL_shift12_cross', 'MA25_REL_shift24', 'MA50_REL', 'MA50_REL_shift1', 'MA50_REL_shift6', 'MA50_REL_shift12', 'MA50_REL_shift12_cross', 'MA50_REL_shift24', 'MA75_REL', 'MA75_REL_shift1', 'MA75_REL_shift6', 'MA75_REL_shift12', 'MA75_REL_shift12_cross', 'MA75_REL_shift24', 'MA100_REL', 'MA100_REL_shift1', 'MA100_REL_shift6', 'MA100_REL_shift12', 'MA100_REL_shift24', 'MA150_REL', 'MA150_REL_shift1', 'MA150_REL_shift6', 'MA150_REL_shift12', 'MA150_REL_shift24', 'MA200_REL', 'MA200_REL_shift1', 'MA200_REL_shift6', 'MA200_REL_shift12', 'MA200_REL_shift24', 'MACDHist_REL', 'MACDHist_REL_shift1', 'MACDHist_REL_shift3', 'MACDHist_REL_shift5', 'MACDHist_REL_shift7', 'MACDHist_REL_shift10', 'EMA_gor_24_REL_cross_all', 'MA_gor_24_REL_cross_all', 'date_key_d', 'std_20_rel', 'std_100_rel', 'RSI14_coef_nak', 'Close_coef_nak', 'Volume_coef_nak', 'EMA14_coef_nak', 'MA100_coef_nak', 'std_20_coef_nak', 'MACDHist_nak', 'Close_coef_nak_div_Volume_coef_nak', 'Close_coef_nak_div_RSI14_coef_nak', 'Close_coef_nak_div_MACDHist_nak', 'Close_0_to_1', 'Close_1_to_2', 'Close_3_to_4', 'Close_4_to_5', 'Close_5_to_6', 'Close_7_to_8', 'Close_8_to_9', 'Close_9_to_10', 'Close_11_to_12', 'Close_0_to_3', 'Close_0_to_4', 'Close_0_to_5', 'Close_0_to_6', 'Close_0_to_9', 'Close_m3_0_to_MA15', 'Close_m3_1_to_MA15', 'Close_m3_3_to_MA15', 'Close_m3_4_to_MA15', 'Close_m3_5_to_MA15', 'Close_m3_6_to_MA15', 'Close_m3_9_to_MA15', 'Close_m3_12_to_MA15', 'Close_2_to_MA15', 'Close_5_to_MA15', 'Close_6_to_MA15', 'Close_7_to_MA15', 'Close_8_to_MA15', 'Close_9_to_MA15', 'Close_10_to_MA15', 'Close_11_to_MA15', 'Close_12_to_MA15', 'Close_13_to_MA15', 'Close_14_to_MA15', 'Close_15_to_MA15', 'RSI27_dw_30_perman', 'RSI9', 'RSI14', 'RSI20', 'RSI27', 'level_close_old_w', 'level_close_act_w', 'step_to_fiba', 'MACDHist_corr_shift1', 'MACDHist_corr_shift3', 'MACDHist_corr_shift6', 'AweOs_cor_shift1', 'AweOs_cor_shift3', 'AweOs_cor_shift6', 'MACDHist_corr_0_to_1', 'MACDHist_corr_1_to_3', 'MACDHist_1_to_3', 'MACDHist_3_to_6', 'AweOs_0_to_1', 'AweOs_1_to_3', 'AweOs_3_to_6', 'AweOs_corr_0_to_1', 'Close_coef_nak2', 'PER_OPEN_shift0', 'PER_OPEN_shift1', 'PER_OPEN_shift2', 'PER_OPEN_shift3', 'PER_OPEN_shift4', 'PER_OPEN_shift5', 'PER_OPEN_shift6', 'PER_CLOSE_shift0', 'PER_CLOSE_shift1', 'PER_CLOSE_shift2', 'PER_CLOSE_shift3', 'PER_CLOSE_shift5', 'PER_CLOSE_shift6', 'POLNOTA_shift0', 'POLNOTA_shift1', 'POLNOTA_shift2', 'POLNOTA_shift3', 'POLNOTA_shift4', 'POLNOTA_shift5', 'POLNOTA_shift6', 'Close_2_to_b', 'Close_3_to_b', 'Close_4_to_b', 'Close_5_to_b', 'Open_0_to_b', 'Open_5_to_b', 'Low_0_to_b', 'Low_1_to_b', 'Low_2_to_b', 'Low_3_to_b', 'Low_4_to_b', 'Low_5_to_b', 'High_0_to_b', 'High_1_to_b', 'High_3_to_b', 'High_4_to_b', 'High_5_to_b', 'EVENT20', 'EVENT19', 'EVENT16', 'EVENT15', 'EVENT14', 'EVENT13', 'EVENT11', 'EVENT10', 'EVENT9', 'EVENT6', 'EVENT4', 'EVENT3', 'down_near', 'up_near', 'mae_opt_near']





# #версия 07.07
# col_fin_dw_4h=['MACDHist_corr', 'AweOs_cor', 'ROC200', 'ROC200sm', 'TSI', 'EMA8_REL', 'EMA8_REL_shift1', 'EMA8_REL_shift6', 'EMA8_REL_shift12', 'EMA8_REL_shift24', 'EMA12_REL', 'EMA12_REL_shift1', 'EMA12_REL_shift6', 'EMA12_REL_shift12', 'EMA12_REL_shift24', 'EMA14_REL_shift6', 'EMA14_REL_shift12', 'EMA20_REL', 'EMA20_REL_shift6', 'EMA20_REL_shift24', 'EMA26_REL', 'EMA26_REL_shift1', 'EMA26_REL_shift6', 'EMA26_REL_shift12', 'EMA32_REL', 'EMA32_REL_shift6', 'EMA32_REL_shift24', 'EMA38_REL', 'EMA38_REL_shift1', 'EMA38_REL_shift6', 'EMA38_REL_shift12', 'EMA38_REL_shift24', 'EMA38_REL_shift24_cross', 'EMA44_REL_shift1', 'EMA44_REL_shift6', 'EMA44_REL_shift12_cross', 'EMA50_REL', 'EMA50_REL_shift6', 'EMA50_REL_shift12', 'EMA50_REL_shift24', 'EMA60_REL', 'EMA60_REL_shift1', 'EMA60_REL_shift6', 'EMA60_REL_shift12', 'EMA60_REL_shift24', 'EMA75_REL', 'EMA75_REL_shift1', 'EMA75_REL_shift1_cross', 'EMA75_REL_shift6', 'EMA75_REL_shift12', 'EMA75_REL_shift24', 'EMA100_REL', 'EMA100_REL_shift1', 'EMA100_REL_shift6', 'EMA100_REL_shift12', 'EMA100_REL_shift24', 'EMA150_REL', 'EMA150_REL_shift6', 'EMA150_REL_shift12', 'EMA150_REL_shift24', 'EMA200_REL', 'EMA200_REL_shift1', 'EMA200_REL_shift6', 'EMA200_REL_shift12', 'EMA200_REL_shift24', 'EMA200_REL_shift24_cross', 'MA5_REL', 'MA5_REL_shift1', 'MA5_REL_shift6', 'MA5_REL_shift12', 'MA5_REL_shift24', 'MA10_REL', 'MA10_REL_shift1', 'MA10_REL_shift6', 'MA10_REL_shift12', 'MA10_REL_shift24', 'MA15_REL', 'MA15_REL_shift6', 'MA15_REL_shift12', 'MA15_REL_shift24', 'MA20_REL', 'MA20_REL_shift1', 'MA20_REL_shift12', 'MA20_REL_shift24', 'MA25_REL', 'MA25_REL_shift1', 'MA25_REL_shift6', 'MA25_REL_shift12', 'MA25_REL_shift24', 'MA50_REL', 'MA50_REL_shift1', 'MA50_REL_shift6', 'MA50_REL_shift12', 'MA50_REL_shift12_cross', 'MA50_REL_shift24', 'MA75_REL', 'MA75_REL_shift1', 'MA75_REL_shift6', 'MA75_REL_shift12', 'MA75_REL_shift24', 'MA75_REL_shift24_cross', 'MA100_REL', 'MA100_REL_shift1', 'MA100_REL_shift6', 'MA100_REL_shift12', 'MA100_REL_shift12_cross', 'MA100_REL_shift24', 'MA150_REL', 'MA150_REL_shift1', 'MA150_REL_shift6', 'MA150_REL_shift12', 'MA150_REL_shift24', 'MA200_REL', 'MA200_REL_shift1', 'MA200_REL_shift6', 'MA200_REL_shift6_cross', 'MA200_REL_shift12', 'MA200_REL_shift12_cross', 'MA200_REL_shift24', 'MA200_REL_shift24_cross', 'MACDHist_REL', 'MACDHist_REL_shift1', 'MACDHist_REL_shift3', 'MACDHist_REL_shift5', 'MACDHist_REL_shift7', 'MACDHist_REL_shift10', 'EMA_gor_1_REL_cross_all', 'EMA_gor_6_REL_cross_all', 'EMA_gor_12_REL_cross_all', 'EMA_gor_24_REL_cross_all', 'MA_gor_6_REL_cross_all', 'MA_gor_12_REL_cross_all', 'date_key_h', 'date_key_d', 'std_20_rel', 'std_100_rel', 'RSI14_coef_nak', 'Close_coef_nak', 'Volume_coef_nak', 'EMA14_coef_nak', 'MA100_coef_nak', 'std_20_coef_nak', 'MACDHist_nak', 'Close_coef_nak_div_Volume_coef_nak', 'Close_coef_nak_div_RSI14_coef_nak', 'Close_coef_nak_div_MACDHist_nak', 'Close_0_to_1', 'Close_1_to_2', 'Close_2_to_3', 'Close_4_to_5', 'Close_5_to_6', 'Close_6_to_7', 'Close_7_to_8', 'Close_8_to_9', 'Close_9_to_10', 'Close_10_to_11', 'Close_11_to_12', 'Close_0_to_3', 'Close_0_to_4', 'Close_0_to_5', 'Close_0_to_6', 'Close_0_to_9', 'Close_m3_0_to_MA15', 'Close_m3_1_to_MA15', 'Close_m3_2_to_MA15', 'Close_m3_3_to_MA15', 'Close_m3_4_to_MA15', 'Close_m3_5_to_MA15', 'Close_m3_6_to_MA15', 'Close_m3_9_to_MA15', 'Close_m3_12_to_MA15', 'Close_2_to_MA15', 'Close_3_to_MA15', 'Close_4_to_MA15', 'Close_5_to_MA15', 'Close_6_to_MA15', 'Close_7_to_MA15', 'Close_8_to_MA15', 'Close_9_to_MA15', 'Close_10_to_MA15', 'Close_11_to_MA15', 'Close_12_to_MA15', 'Close_13_to_MA15', 'Close_14_to_MA15', 'Close_15_to_MA15', 'RSI9_up_70_perman', 'RSI14_up_70_perman', 'RSI20_up_70_perman', 'RSI20_dw_30_perman', 'RSI27_dw_30_perman', 'RSI9', 'RSI14', 'RSI20', 'RSI27', 'level_close_old_w', 'level_close_act_w', 'step_to_fiba', 'MACDHist_corr_shift1', 'MACDHist_corr_shift3', 'MACDHist_corr_shift6', 'AweOs_cor_shift1', 'AweOs_cor_shift3', 'AweOs_cor_shift6', 'MACDHist_corr_0_to_1', 'MACDHist_corr_1_to_3', 'MACDHist_corr_3_to_6', 'MACDHist_0_to_1', 'MACDHist_1_to_3', 'MACDHist_3_to_6', 'AweOs_0_to_1', 'AweOs_1_to_3', 'AweOs_3_to_6', 'AweOs_corr_0_to_1', 'Close_coef_nak2', 'SV_DIR_shift1', 'SV_DIR_shift6', 'PER_OPEN_shift0', 'PER_OPEN_shift1', 'PER_OPEN_shift2', 'PER_OPEN_shift3', 'PER_OPEN_shift4', 'PER_OPEN_shift5', 'PER_OPEN_shift6', 'PER_CLOSE_shift0', 'PER_CLOSE_shift1', 'PER_CLOSE_shift2', 'PER_CLOSE_shift3', 'PER_CLOSE_shift4', 'PER_CLOSE_shift5', 'PER_CLOSE_shift6', 'POLNOTA_shift0', 'POLNOTA_shift1', 'POLNOTA_shift2', 'POLNOTA_shift3', 'POLNOTA_shift4', 'POLNOTA_shift5', 'POLNOTA_shift6', 'Close_2_to_b', 'Close_3_to_b', 'Close_4_to_b', 'Close_5_to_b', 'Open_0_to_b', 'Open_1_to_b', 'Open_2_to_b', 'Open_3_to_b', 'Open_4_to_b', 'Open_5_to_b', 'Low_0_to_b', 'Low_1_to_b', 'Low_2_to_b', 'Low_3_to_b', 'Low_4_to_b', 'Low_5_to_b', 'High_0_to_b', 'High_1_to_b', 'High_2_to_b', 'High_3_to_b', 'High_4_to_b', 'High_5_to_b', 'EVENT20', 'EVENT19', 'EVENT16', 'EVENT15', 'EVENT14', 'EVENT13', 'EVENT11', 'EVENT10', 'EVENT9', 'EVENT4', 'EVENT3', 'down_near', 'up_near', 'mae_opt_near']



# #версия 07.07
# MODEL_PARAMS_DW_4H = {

#      'boosting_type':'gbdt',
# #      'num_leaves': 90, 
# #      'max_depth': 8, 
#       'learning_rate': 0.06,
#       'n_estimators': 100,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7, 
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
#       'reg_lambda': 80,
# #      'random_state': 42, 
#     'scale_pos_weight': 1,
#       'n_jobs': 10
# }




# #версия 07.07
# MODEL_PARAMS_UP_4H = {

#     'boosting_type':'dart',
#       'num_leaves': 150, 
#       'max_depth': 7, 
# #      'learning_rate': 0.13,
# #      'n_estimators': 200,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7, 
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
#       'reg_lambda': 50,
# #      'random_state': 42, 
# #    'scale_pos_weight': 4,
#       'n_jobs': 10
# }




# ####################       4H      ВЕРСИЯ 08.07



# #версия 08.07  + синосойды, посчитано до 12.2020
# col_fin_up_4h=['MACDHist_corr', 'AweOs_cor', 'ROC200', 'ROC200sm', 'TSI', 'EMA8_REL', 'EMA8_REL_shift1', 'EMA8_REL_shift6', 'EMA8_REL_shift12', 'EMA8_REL_shift24', 'EMA12_REL', 'EMA12_REL_shift6', 'EMA12_REL_shift12', 'EMA12_REL_shift24', 'EMA14_REL', 'EMA14_REL_shift1', 'EMA14_REL_shift6', 'EMA14_REL_shift12', 'EMA14_REL_shift12_cross', 'EMA14_REL_shift24', 'EMA20_REL_shift12', 'EMA20_REL_shift24', 'EMA26_REL_shift1', 'EMA26_REL_shift6', 'EMA26_REL_shift12', 'EMA26_REL_shift12_cross', 'EMA26_REL_shift24', 'EMA32_REL', 'EMA32_REL_shift6', 'EMA32_REL_shift24', 'EMA38_REL_shift1', 'EMA38_REL_shift6', 'EMA38_REL_shift12', 'EMA38_REL_shift24', 'EMA44_REL', 'EMA44_REL_shift1', 'EMA44_REL_shift6', 'EMA44_REL_shift12', 'EMA44_REL_shift24', 'EMA44_REL_shift24_cross', 'EMA50_REL', 'EMA50_REL_shift1', 'EMA50_REL_shift6', 'EMA50_REL_shift12', 'EMA50_REL_shift24', 'EMA60_REL', 'EMA60_REL_shift6', 'EMA60_REL_shift12', 'EMA60_REL_shift24', 'EMA75_REL', 'EMA75_REL_shift1', 'EMA75_REL_shift6', 'EMA75_REL_shift12', 'EMA75_REL_shift24', 'EMA100_REL', 'EMA100_REL_shift1', 'EMA100_REL_shift6', 'EMA100_REL_shift12', 'EMA100_REL_shift12_cross', 'EMA100_REL_shift24', 'EMA150_REL', 'EMA150_REL_shift1', 'EMA150_REL_shift6', 'EMA150_REL_shift12', 'EMA150_REL_shift24', 'EMA200_REL', 'EMA200_REL_shift1', 'EMA200_REL_shift6', 'EMA200_REL_shift12', 'EMA200_REL_shift24', 'EMA200_REL_shift24_cross', 'MA5_REL', 'MA5_REL_shift1', 'MA5_REL_shift6', 'MA5_REL_shift12', 'MA5_REL_shift12_cross', 'MA5_REL_shift24', 'MA10_REL', 'MA10_REL_shift1', 'MA10_REL_shift6', 'MA10_REL_shift12', 'MA10_REL_shift24', 'MA15_REL', 'MA15_REL_shift6', 'MA15_REL_shift12', 'MA15_REL_shift24', 'MA15_REL_shift24_cross', 'MA20_REL', 'MA20_REL_shift1', 'MA20_REL_shift6', 'MA20_REL_shift12', 'MA20_REL_shift24', 'MA25_REL', 'MA25_REL_shift1', 'MA25_REL_shift6', 'MA25_REL_shift12', 'MA25_REL_shift24', 'MA50_REL', 'MA50_REL_shift1', 'MA50_REL_shift6', 'MA50_REL_shift12', 'MA50_REL_shift12_cross', 'MA50_REL_shift24', 'MA75_REL', 'MA75_REL_shift1', 'MA75_REL_shift6', 'MA75_REL_shift12', 'MA75_REL_shift24', 'MA75_REL_shift24_cross', 'MA100_REL', 'MA100_REL_shift1', 'MA100_REL_shift6', 'MA100_REL_shift12', 'MA100_REL_shift12_cross', 'MA100_REL_shift24', 'MA150_REL', 'MA150_REL_shift1', 'MA150_REL_shift6', 'MA150_REL_shift12', 'MA150_REL_shift12_cross', 'MA150_REL_shift24', 'MA150_REL_shift24_cross', 'MA200_REL', 'MA200_REL_shift1', 'MA200_REL_shift1_cross', 'MA200_REL_shift6', 'MA200_REL_shift6_cross', 'MA200_REL_shift12', 'MA200_REL_shift12_cross', 'MA200_REL_shift24', 'MA200_REL_shift24_cross', 'MACDHist_REL', 'MACDHist_REL_shift1', 'MACDHist_REL_shift3', 'MACDHist_REL_shift5', 'MACDHist_REL_shift7', 'MACDHist_REL_shift10', 'EMA_gor_1_REL_cross_all', 'EMA_gor_6_REL_cross_all', 'EMA_gor_12_REL_cross_all', 'EMA_gor_24_REL_cross_all', 'MA_gor_6_REL_cross_all', 'MA_gor_24_REL_cross_all', 'std_20_rel', 'std_100_rel', 'RSI14_coef_nak', 'Close_coef_nak', 'Volume_coef_nak', 'EMA14_coef_nak', 'MA100_coef_nak', 'std_20_coef_nak', 'MACDHist_nak', 'Close_coef_nak_div_Volume_coef_nak', 'Close_coef_nak_div_RSI14_coef_nak', 'Close_coef_nak_div_MACDHist_nak', 'Close_0_to_1', 'Close_1_to_2', 'Close_2_to_3', 'Close_3_to_4', 'Close_4_to_5', 'Close_5_to_6', 'Close_7_to_8', 'Close_8_to_9', 'Close_9_to_10', 'Close_10_to_11', 'Close_11_to_12', 'Close_0_to_3', 'Close_0_to_4', 'Close_0_to_5', 'Close_0_to_6', 'Close_0_to_9', 'Close_0_to_12', 'Close_m3_0_to_MA15', 'Close_m3_1_to_MA15', 'Close_m3_2_to_MA15', 'Close_m3_3_to_MA15', 'Close_m3_4_to_MA15', 'Close_m3_5_to_MA15', 'Close_m3_6_to_MA15', 'Close_m3_9_to_MA15', 'Close_m3_12_to_MA15', 'Close_3_to_MA15', 'Close_4_to_MA15', 'Close_5_to_MA15', 'Close_6_to_MA15', 'Close_7_to_MA15', 'Close_8_to_MA15', 'Close_9_to_MA15', 'Close_10_to_MA15', 'Close_11_to_MA15', 'Close_12_to_MA15', 'Close_13_to_MA15', 'Close_14_to_MA15', 'Close_15_to_MA15', 'RSI9_dw_30_perman', 'RSI14_up_70_perman', 'RSI20_up_70_perman', 'RSI20_dw_30_perman', 'RSI27_up_70_perman', 'RSI27_dw_30_perman', 'RSI9', 'RSI14', 'RSI20', 'RSI27', 'level_close_old_w', 'level_close_act_w', 'step_to_fiba', 'MACDHist_corr_shift1', 'MACDHist_corr_shift3', 'MACDHist_corr_shift6', 'AweOs_cor_shift1', 'AweOs_cor_shift3', 'AweOs_cor_shift6', 'MACDHist_corr_0_to_1', 'MACDHist_corr_1_to_3', 'MACDHist_corr_3_to_6', 'MACDHist_0_to_1', 'MACDHist_1_to_3', 'MACDHist_3_to_6', 'AweOs_0_to_1', 'AweOs_1_to_3', 'AweOs_3_to_6', 'AweOs_corr_0_to_1', 'AweOs_corr_1_to_3', 'Close_coef_nak2', 'PER_OPEN_shift0', 'PER_OPEN_shift1', 'PER_OPEN_shift2', 'PER_OPEN_shift3', 'PER_OPEN_shift4', 'PER_OPEN_shift5', 'PER_OPEN_shift6', 'PER_CLOSE_shift0', 'PER_CLOSE_shift1', 'PER_CLOSE_shift2', 'PER_CLOSE_shift3', 'PER_CLOSE_shift4', 'PER_CLOSE_shift5', 'PER_CLOSE_shift6', 'POLNOTA_shift0', 'POLNOTA_shift1', 'POLNOTA_shift2', 'POLNOTA_shift3', 'POLNOTA_shift4', 'POLNOTA_shift5', 'POLNOTA_shift6', 'Close_2_to_b', 'Close_3_to_b', 'Close_4_to_b', 'Close_5_to_b', 'Open_0_to_b', 'Open_1_to_b', 'Open_2_to_b', 'Open_4_to_b', 'Open_5_to_b', 'Low_0_to_b', 'Low_1_to_b', 'Low_2_to_b', 'Low_3_to_b', 'Low_4_to_b', 'Low_5_to_b', 'High_0_to_b', 'High_1_to_b', 'High_2_to_b', 'High_3_to_b', 'High_4_to_b', 'High_5_to_b', 'EVENT20', 'EVENT19', 'EVENT18', 'EVENT16', 'EVENT15', 'EVENT14', 'EVENT13', 'EVENT11', 'EVENT10', 'EVENT7', 'EVENT3', 'down_near', 'up_near', 'mae_opt_near', 'down_far', 'up_far', 'mae_opt_far']


# #версия 08.07
# col_fin_dw_4h=['MACDHist_corr', 'AweOs_cor', 'ROC200', 'ROC200sm', 'TSI', 'EMA8_REL_shift6', 'EMA8_REL_shift12', 'EMA8_REL_shift24', 'EMA12_REL_shift24', 'EMA14_REL_shift12', 'EMA14_REL_shift24', 'EMA20_REL', 'EMA20_REL_shift12', 'EMA20_REL_shift24', 'EMA26_REL', 'EMA26_REL_shift6', 'EMA26_REL_shift12', 'EMA38_REL_shift6', 'EMA38_REL_shift24', 'EMA44_REL_shift24', 'EMA50_REL_shift12', 'EMA60_REL', 'EMA60_REL_shift12', 'EMA60_REL_shift24', 'EMA75_REL', 'EMA75_REL_shift12', 'EMA100_REL', 'EMA100_REL_shift1', 'EMA100_REL_shift1_cross', 'EMA100_REL_shift6', 'EMA100_REL_shift12', 'EMA100_REL_shift12_cross', 'EMA100_REL_shift24', 'EMA150_REL', 'EMA150_REL_shift6', 'EMA150_REL_shift12', 'EMA150_REL_shift24', 'EMA200_REL', 'EMA200_REL_shift1', 'EMA200_REL_shift6', 'EMA200_REL_shift12', 'EMA200_REL_shift24', 'MA5_REL', 'MA5_REL_shift6', 'MA5_REL_shift12', 'MA5_REL_shift24', 'MA10_REL', 'MA10_REL_shift1', 'MA10_REL_shift12', 'MA10_REL_shift24', 'MA15_REL_shift6', 'MA15_REL_shift12', 'MA15_REL_shift24', 'MA20_REL', 'MA20_REL_shift12', 'MA20_REL_shift24', 'MA25_REL', 'MA25_REL_shift1', 'MA25_REL_shift12', 'MA25_REL_shift24', 'MA50_REL', 'MA50_REL_shift1', 'MA50_REL_shift6', 'MA50_REL_shift12', 'MA50_REL_shift12_cross', 'MA50_REL_shift24', 'MA75_REL', 'MA75_REL_shift1', 'MA75_REL_shift6', 'MA75_REL_shift12', 'MA75_REL_shift24', 'MA75_REL_shift24_cross', 'MA100_REL', 'MA100_REL_shift1', 'MA100_REL_shift6', 'MA100_REL_shift12', 'MA100_REL_shift12_cross', 'MA100_REL_shift24', 'MA150_REL', 'MA150_REL_shift1', 'MA150_REL_shift6', 'MA150_REL_shift12', 'MA150_REL_shift24', 'MA200_REL', 'MA200_REL_shift1', 'MA200_REL_shift6', 'MA200_REL_shift12', 'MA200_REL_shift12_cross', 'MA200_REL_shift24', 'MACDHist_REL', 'MACDHist_REL_shift1', 'MACDHist_REL_shift3', 'MACDHist_REL_shift5', 'MACDHist_REL_shift7', 'MACDHist_REL_shift10', 'EMA_gor_1_REL_cross_all', 'EMA_gor_6_REL_cross_all', 'EMA_gor_12_REL_cross_all', 'EMA_gor_24_REL_cross_all', 'MA_gor_6_REL_cross_all', 'MA_gor_24_REL_cross_all', 'std_20_rel', 'std_100_rel', 'RSI14_coef_nak', 'Close_coef_nak', 'Volume_coef_nak', 'EMA14_coef_nak', 'MA100_coef_nak', 'std_20_coef_nak', 'MACDHist_nak', 'Close_coef_nak_div_Volume_coef_nak', 'Close_coef_nak_div_RSI14_coef_nak', 'Close_coef_nak_div_MACDHist_nak', 'Close_0_to_1', 'Close_1_to_2', 'Close_2_to_3', 'Close_4_to_5', 'Close_5_to_6', 'Close_6_to_7', 'Close_7_to_8', 'Close_8_to_9', 'Close_9_to_10', 'Close_10_to_11', 'Close_11_to_12', 'Close_0_to_4', 'Close_0_to_5', 'Close_0_to_6', 'Close_0_to_9', 'Close_0_to_12', 'Close_m3_1_to_MA15', 'Close_m3_2_to_MA15', 'Close_m3_3_to_MA15', 'Close_m3_4_to_MA15', 'Close_m3_5_to_MA15', 'Close_m3_6_to_MA15', 'Close_m3_9_to_MA15', 'Close_m3_12_to_MA15', 'Close_0_to_MA15', 'Close_2_to_MA15', 'Close_3_to_MA15', 'Close_4_to_MA15', 'Close_5_to_MA15', 'Close_6_to_MA15', 'Close_7_to_MA15', 'Close_8_to_MA15', 'Close_9_to_MA15', 'Close_11_to_MA15', 'Close_12_to_MA15', 'Close_13_to_MA15', 'Close_14_to_MA15', 'Close_15_to_MA15', 'RSI14_up_70_perman', 'RSI27_dw_30_perman', 'RSI9', 'RSI14', 'RSI20', 'RSI27', 'level_close_old_w', 'level_close_act_w', 'step_to_fiba', 'MACDHist_corr_shift1', 'MACDHist_corr_shift3', 'MACDHist_corr_shift6', 'AweOs_cor_shift1', 'AweOs_cor_shift3', 'AweOs_cor_shift6', 'MACDHist_corr_0_to_1', 'MACDHist_corr_1_to_3', 'MACDHist_corr_3_to_6', 'MACDHist_0_to_1', 'MACDHist_1_to_3', 'MACDHist_3_to_6', 'AweOs_1_to_3', 'AweOs_3_to_6', 'AweOs_corr_0_to_1', 'Close_coef_nak2', 'PER_OPEN_shift0', 'PER_OPEN_shift1', 'PER_OPEN_shift2', 'PER_OPEN_shift3', 'PER_OPEN_shift4', 'PER_OPEN_shift5', 'PER_OPEN_shift6', 'PER_CLOSE_shift0', 'PER_CLOSE_shift1', 'PER_CLOSE_shift2', 'PER_CLOSE_shift3', 'PER_CLOSE_shift4', 'PER_CLOSE_shift5', 'PER_CLOSE_shift6', 'POLNOTA_shift0', 'POLNOTA_shift1', 'POLNOTA_shift2', 'POLNOTA_shift3', 'POLNOTA_shift4', 'POLNOTA_shift5', 'POLNOTA_shift6', 'Close_2_to_b', 'Close_5_to_b', 'Open_0_to_b', 'Open_1_to_b', 'Open_2_to_b', 'Open_3_to_b', 'Open_5_to_b', 'Low_0_to_b', 'Low_1_to_b', 'Low_2_to_b', 'Low_3_to_b', 'Low_4_to_b', 'Low_5_to_b', 'High_0_to_b', 'High_1_to_b', 'High_2_to_b', 'High_3_to_b', 'High_4_to_b', 'High_5_to_b', 'EVENT19', 'EVENT16', 'EVENT15', 'EVENT14', 'EVENT13', 'EVENT11', 'EVENT10', 'EVENT3', 'down_near', 'up_near', 'mae_opt_near', 'down_far', 'up_far', 'mae_opt_far']


# #версия 08.07
# MODEL_PARAMS_UP_4H = {

#     'boosting_type':'gbdt',
#       'num_leaves': 100, 
# #      'max_depth': 7, 
#       'learning_rate': 0.05,
# #      'n_estimators': 200,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7, 
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
#       'reg_lambda': 50,
# #      'random_state': 42, 
# #    'scale_pos_weight': 4,
#       'n_jobs': 10
# }





# #версия 08.07
# MODEL_PARAMS_DW_4H = {

#      'boosting_type':'dart',
#       'num_leaves': 200, 
#       'max_depth': 6, 
#       'learning_rate': 0.1,
#       'n_estimators': 100,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7, 
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
#       'reg_lambda': 200,
# #      'random_state': 42, 
#     'scale_pos_weight': 1,
#       'n_jobs': 10
# }





####################       4H      ВЕРСИЯ 28.08.21



#версия 08.07  + синосойды, посчитано до 12.2020
col_fin_up_4h=['EMA12_REL', 'EMA150_REL_shift1_cross', 'MA200_REL_shift6_cross', 'Open_2_to_b', 'RSI14_dw_20_perman', 'Low_3_to_b', 'up_far', 'EMA200_REL_shift24', 'AweOs_1_to_3', 'EMA20_REL_shift1_cross', 'Close_15_to_MA15', 'down_far', 'plotnost_50_ch', 'EMA38_REL_shift6_cross', 'EMA75_REL_shift12_cross', 'Close_11_to_12', 'EMA38_REL_shift1', 'mae_opt_far', 'Close_m3_1_to_MA15', 'Close_1_to_b', 'Close_0_to_12', 'EMA50_REL_shift1', 'date_key_d', 'MA15_REL_shift6_cross', 'MACDHist_0_to_1', 'RSI27_up_70_perman', 'RSI27', 'plotnost_50_all', 'RSI20_up_80', 'type_molot_shift2', 'MA20_REL_shift6_cross', 'MACDHist_REL_shift7', 'up_near', 'Low_0_to_b', 'EMA60_REL_shift1', 'MA_gor_24_REL_cross_all', 'Close_m3_5_to_MA15', 'EMA14_REL_shift1', 'MA10_REL', 'High_0_to_b', 'EMA20_REL_shift1', 'EMA60_REL_shift1_cross', 'EMA14_REL_shift6_cross', 'EMA60_REL_shift12_cross', 'SV_DIR_shift4', 'Open_3_to_b', 'EMA32_REL_shift1', 'EVENT10', 'date_key_h', 'EVENT22', 'Close_0_to_1', 'RSI9_dw_30_perman', 'Close_2_to_MA15', 'MACDHist_1_to_3', 'EMA60_REL', 'Close_5_to_6', 'POLNOTA_shift9', 'EMA44_REL_shift12', 'EMA32_REL_shift1_cross', 'EVENT5', 'freq_up_all_100', 'EMA44_REL', 'EMA20_REL_shift12_cross', 'MACDHist_corr_1_to_3', 'Close_m3_3_to_MA15', 'High_3_to_b', 'Open_4_to_b', 'MA50_REL', 'MA_gor_12_REL_cross_all', 'RSI20_dw_30', 'EMA75_REL_shift12', 'EMA12_REL_shift12', 'Close_14_to_MA15', 'MA100_REL_shift1_cross', 'level_close_old_w', 'MA10_REL_shift12', 'Close_coef_nak_div_MACDHist_nak', 'High_4_to_b', 'MA150_REL_shift1', 'EMA200_REL_shift12_cross', 'EVENT17', 'PER_CLOSE_shift0', 'AweOs_cor', 'EMA50_REL_shift12_cross', 'EMA12_REL_shift1', 'MA10_REL_shift6', 'RSI9_dw_20', 'EMA150_REL_shift6_cross', 'MA25_REL_shift12', 'AweOs_corr_1_to_3', 'MA10_REL_shift1_cross', 'MA5_REL_shift1_cross', 'EMA12_REL_shift24', 'EMA38_REL_shift12_cross']


#версия 08.07
col_fin_dw_4h=['MA100_coef_nak', 'Open_2_to_b', 'EMA50_REL_shift24', 'MA75_REL_shift12', 'EMA20_REL_shift1_cross', 'EMA75_REL_shift1', 'plotnost_50_ch', 'EMA75_REL_shift12_cross', 'Close_1_to_b', 'MA15_REL_shift6_cross', 'MACDHist_corr_3_to_6', 'EVENT7', 'MA25_REL_shift1_cross', 'Close_8_to_MA15', 'EMA44_REL_shift1_cross', 'MA50_REL_shift6_cross', 'MA25_REL', 'Low_0_to_b', 'EMA44_REL_shift6', 'EMA60_REL_shift1', 'MA5_REL_shift24_cross', 'PER_OPEN_shift0', 'MACDHist_REL_shift10', 'PER_CLOSE_shift2', 'Close_m3_6_to_MA15', 'SV_DIR_shift7', 'EMA26_REL_shift6_cross', 'Close_m3_12_to_MA15', 'MA50_REL_shift6', 'EMA14_REL_shift6', 'balance_100_ch', 'EVENT3', 'Open_3_to_b', 'EMA14_REL_shift12_cross', 'freq_up_ch_50', 'EMA200_REL_shift6', 'Close_5_to_b', 'EMA26_REL_shift1', 'Close_0_to_1', 'EMA75_REL_shift6_cross', 'RSI9_dw_30_perman', 'MA150_REL_shift6_cross', 'Close_2_to_MA15', 'POLNOTA_shift11', 'MA5_REL_shift1', 'MA10_REL_shift1', 'RSI14_coef_nak', 'type_molot_shift3', 'EMA32_REL_shift1_cross', 'AweOs_cor_shift6', 'EMA38_REL_shift1_cross', 'EMA200_REL_shift12', 'EMA44_REL', 'RSI27_dw_30_perman', 'EMA150_REL_shift6', 'EMA20_REL_shift12', 'EMA20_REL_shift12_cross', 'Close_10_to_MA15', 'EVENT19', 'Close_0_to_9', 'MACDHist_REL_shift5', 'High_3_to_b', 'RSI14_dw_30', 'Close_12_to_MA15', 'MA50_REL', 'EMA12_REL_shift12', 'Close_14_to_MA15', 'MACDHist_3_to_6', 'RSI14_up_80', 'EMA60_REL_shift6_cross', 'MA50_REL_shift12', 'EMA44_REL_shift6_cross', 'EMA38_REL_shift24', 'type_molot_shift7', 'Close_4_to_b']


#версия 08.07
MODEL_PARAMS_UP_4H = {

    'boosting_type':'gbdt',
      'num_leaves': 100, 
      'max_depth': 4, 
      'learning_rate': 0.07,
#      'n_estimators': 200,
#      'min_child_samples': 20,
#      'subsample': 0.7,
#      'colsample_bytree': 0.7, 
#      'min_child_weight': 5,
#      'reg_alpha': 0,
      'reg_lambda': 50,
#      'random_state': 42, 
#    'scale_pos_weight': 4,
      'n_jobs': 10
}



#версия 08.07
MODEL_PARAMS_DW_4H = {

#     'boosting_type':'dart',
#      'num_leaves': 200, 
#      'max_depth': 6, 
      'learning_rate': 0.1,
      'n_estimators': 100,
#      'min_child_samples': 20,
#      'subsample': 0.7,
#      'colsample_bytree': 0.7, 
#      'min_child_weight': 5,
#      'reg_alpha': 0,
      'reg_lambda': 5,
#      'random_state': 42, 
    'scale_pos_weight': 1,
      'n_jobs': 10
}




# ####################       4H      ВЕРСИЯ 28.09.21



# #версия 08.07  + синосойды, посчитано до 12.2020
# col_fin_up_4h=['EMA38_REL', 'EMA14_REL_shift6', 'plotnost_100_all', 'RSI14_up_70_perman', 'MA75_REL_shift1', 'MA50_REL_shift6', 'EMA12_REL', 'EMA75_REL_shift1', 'EMA32_REL_shift6', 'MA10_REL_shift6_cross', 'MA75_REL_shift1_cross', 'Open_3_to_b', 'RSI9_dw_30_perman', 'Close_m3_9_to_MA15', 'MA_gor_1_REL_cross_all', 'Close_0_to_MA15', 'plotnost_50_ch', 'MA150_REL', 'Close_15_to_MA15', 'Close_m3_2_to_MA15', 'MA_gor_6_REL_cross_all', 'MA5_REL_shift6', 'MA15_REL_shift6_cross', 'EMA44_REL_shift12', 'Close_m3_5_to_MA15', 'Close_m3_3_to_MA15', 'POLNOTA_shift0', 'EMA50_REL', 'EMA26_REL_shift12_cross', 'plotnost_300_ch', 'EMA75_REL_shift24', 'RSI9_up_70_perman', 'EMA14_REL', 'Open_2_to_b', 'EMA32_REL_shift12_cross', 'Close_5_to_MA15', 'MACDHist_1_to_3', 'PER_OPEN_shift7', 'Close_1_to_MA15', 'MA10_REL_shift12', 'Close_10_to_MA15', 'RSI14_dw_20_perman', 'Close_12_to_MA15', 'RSI27_dw_20', 'EMA60_REL_shift24', 'EVENT21', 'MA10_REL_shift1', 'Close_4_to_MA15', 'RSI9_dw_20', 'Open_0_to_b', 'EVENT18', 'MA5_REL', 'SV_DIR_shift6', 'MA150_REL_shift6_cross', 'Close_0_to_9', 'Low_1_to_b', 'MA5_REL_shift24', 'EMA12_REL_shift24', 'Low_2_to_b', 'Close_7_to_8', 'High_0_to_b', 'balance_50_ch', 'MACDHist_corr_1_to_3', 'mae_opt_far', 'EVENT8', 'MA150_REL_shift1_cross', 'Close_m3_6_to_MA15', 'Low_4_to_b', 'EVENT2', 'Close_3_to_4', 'MACDHist_corr']


# #версия 08.07
# col_fin_dw_4h=['step_to_fiba', 'SV_DIR_shift4', 'EMA8_REL', 'EVENT14', 'AweOs_corr_1_to_3', 'MA150_REL_shift6', 'Close_2_to_MA15', 'PER_CLOSE_shift1', 'MA15_REL', 'EVENT13', 'EMA75_REL_shift1_cross', 'SV_DIR_shift3', 'PER_OPEN_shift5', 'Close_0_to_4', 'Close_m3_3_to_MA15', 'EMA26_REL', 'Close_6_to_7', 'High_5_to_b', 'EMA44_REL_shift1_cross', 'EMA14_coef_nak', 'MA100_REL_shift1_cross', 'RSI14_up_70', 'EMA26_REL_shift6_cross', 'EMA200_REL_shift12', 'Close_10_to_MA15', 'EMA8_REL_shift6', 'Close_14_to_MA15', 'EMA60_REL_shift6_cross', 'RSI27_dw_20', 'Close_1_to_2', 'Close_coef_nak_div_RSI14_coef_nak', 'MA10_REL_shift1', 'MA5_REL_shift1', 'RSI9_up_80', 'MA15_REL_shift12', 'EMA8_REL_shift1_cross', 'RSI27_up_70_perman', 'MACDHist_corr_shift6', 'MA_gor_24_REL_cross_all', 'SV_DIR_shift5', 'MA75_REL_shift6', 'EMA12_REL_shift6', 'freq_up_ch_50', 'MA20_REL', 'EMA12_REL_shift24', 'freq_dw_ch_300', 'Close_7_to_8', 'High_0_to_b', 'MA25_REL_shift12', 'EVENT20', 'EMA8_REL_shift6_cross', 'PER_OPEN_shift1', 'RSI20_up_70', 'MA150_REL_shift1_cross', 'Close_m3_6_to_MA15', 'freq_up_ch_100', 'MACDHist_corr_shift1']


# #версия 08.07
# MODEL_PARAMS_UP_4H = {

#     'boosting_type':'gbdt',
#       'num_leaves': 100, 
# #      'max_depth': 4, 
#       'learning_rate': 0.1,
# #      'n_estimators': 200,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7, 
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
#       'reg_lambda': 50,
# #      'random_state': 42, 
# #    'scale_pos_weight': 4,
#       'n_jobs': 10
# }



# #версия 08.07
# MODEL_PARAMS_DW_4H = {

# #     'boosting_type':'dart',
# #      'num_leaves': 200, 
# #      'max_depth': 6, 
#       'learning_rate': 0.1,
#       'n_estimators': 100,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7, 
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
#       'reg_lambda': 25,
# #      'random_state': 42, 
#     'scale_pos_weight': 1,
#       'n_jobs': 10
# }








###########################################################################################################################
###############################################    1H     #################################################################
###########################################################################################################################


####################       1H      ВЕРСИЯ 25.06



#версия 25.06
# col_fin_up_1h=['MACDHist_corr', 'AweOs_cor', 'ROC200', 'ROC200sm', 'TSI', 'EMA8_REL', 'EMA8_REL_shift1', 'EMA8_REL_shift6', 'EMA8_REL_shift24', 'EMA12_REL', 'EMA12_REL_shift12', 'EMA12_REL_shift24', 'EMA14_REL', 'EMA14_REL_shift6', 'EMA14_REL_shift24', 'EMA20_REL', 'EMA20_REL_shift6', 'EMA20_REL_shift12', 'EMA26_REL', 'EMA26_REL_shift6', 'EMA26_REL_shift12', 'EMA26_REL_shift24', 'EMA32_REL', 'EMA32_REL_shift24', 'EMA38_REL', 'EMA38_REL_shift1', 'EMA38_REL_shift12', 'EMA38_REL_shift24', 'EMA44_REL', 'EMA44_REL_shift1', 'EMA44_REL_shift6', 'EMA44_REL_shift12', 'EMA44_REL_shift24', 'EMA44_REL_shift24_cross', 'EMA50_REL', 'EMA50_REL_shift6', 'EMA50_REL_shift12', 'EMA50_REL_shift24', 'EMA60_REL', 'EMA60_REL_shift24', 'EMA75_REL', 'EMA75_REL_shift6', 'EMA75_REL_shift12', 'EMA75_REL_shift24', 'EMA100_REL', 'EMA100_REL_shift1', 'EMA100_REL_shift6', 'EMA100_REL_shift12', 'EMA100_REL_shift24', 'EMA150_REL', 'EMA150_REL_shift1', 'EMA150_REL_shift6', 'EMA150_REL_shift12', 'EMA150_REL_shift12_cross', 'EMA150_REL_shift24', 'EMA200_REL', 'EMA200_REL_shift1', 'EMA200_REL_shift6', 'EMA200_REL_shift12', 'EMA200_REL_shift24', 'EMA200_REL_shift24_cross', 'MA5_REL', 'MA5_REL_shift1', 'MA5_REL_shift6', 'MA5_REL_shift12', 'MA5_REL_shift24', 'MA10_REL', 'MA10_REL_shift1', 'MA10_REL_shift6', 'MA10_REL_shift12', 'MA10_REL_shift12_cross', 'MA10_REL_shift24', 'MA15_REL', 'MA15_REL_shift6', 'MA15_REL_shift6_cross', 'MA15_REL_shift12', 'MA15_REL_shift24', 'MA15_REL_shift24_cross', 'MA20_REL', 'MA20_REL_shift1', 'MA20_REL_shift6', 'MA20_REL_shift12', 'MA20_REL_shift12_cross', 'MA20_REL_shift24', 'MA25_REL', 'MA25_REL_shift1', 'MA25_REL_shift6', 'MA25_REL_shift6_cross', 'MA25_REL_shift12', 'MA25_REL_shift12_cross', 'MA25_REL_shift24', 'MA25_REL_shift24_cross', 'MA50_REL', 'MA50_REL_shift1', 'MA50_REL_shift6', 'MA50_REL_shift12', 'MA50_REL_shift24', 'MA75_REL', 'MA75_REL_shift1', 'MA75_REL_shift6', 'MA75_REL_shift6_cross', 'MA75_REL_shift12', 'MA75_REL_shift12_cross', 'MA75_REL_shift24', 'MA75_REL_shift24_cross', 'MA100_REL', 'MA100_REL_shift1', 'MA100_REL_shift1_cross', 'MA100_REL_shift6', 'MA100_REL_shift12', 'MA100_REL_shift24', 'MA150_REL', 'MA150_REL_shift1', 'MA150_REL_shift6', 'MA150_REL_shift12', 'MA150_REL_shift12_cross', 'MA150_REL_shift24', 'MA150_REL_shift24_cross', 'MA200_REL', 'MA200_REL_shift1', 'MA200_REL_shift6', 'MA200_REL_shift12', 'MA200_REL_shift24', 'MA200_REL_shift24_cross', 'MACDHist_REL', 'MACDHist_REL_shift1', 'MACDHist_REL_shift3', 'MACDHist_REL_shift5', 'MACDHist_REL_shift7', 'MACDHist_REL_shift10', 'EMA_gor_6_REL_cross_all', 'EMA_gor_12_REL_cross_all', 'MA_gor_6_REL_cross_all', 'MA_gor_12_REL_cross_all', 'MA_gor_24_REL_cross_all', 'date_key_h', 'date_key_d', 'std_20_rel', 'std_100_rel', 'std_500_rel', 'RSI14_coef_nak', 'Close_coef_nak', 'Volume_coef_nak', 'EMA14_coef_nak', 'MA100_coef_nak', 'std_20_coef_nak', 'MACDHist_nak', 'Close_coef_nak_div_Volume_coef_nak', 'Close_coef_nak_div_RSI14_coef_nak', 'Close_coef_nak_div_MACDHist_nak', 'Close_0_to_1', 'Close_1_to_2', 'Close_2_to_3', 'Close_3_to_4', 'Close_4_to_5', 'Close_6_to_7', 'Close_8_to_9', 'Close_9_to_10', 'Close_10_to_11', 'Close_11_to_12', 'Close_0_to_3', 'Close_0_to_4', 'Close_0_to_5', 'Close_0_to_6', 'Close_0_to_9', 'Close_0_to_12', 'Close_m3_0_to_MA15', 'Close_m3_1_to_MA15', 'Close_m3_2_to_MA15', 'Close_m3_3_to_MA15', 'Close_m3_4_to_MA15', 'Close_m3_5_to_MA15', 'Close_m3_6_to_MA15', 'Close_m3_9_to_MA15', 'Close_m3_12_to_MA15', 'Close_0_to_MA15', 'Close_1_to_MA15', 'Close_2_to_MA15', 'Close_3_to_MA15', 'Close_4_to_MA15', 'Close_5_to_MA15', 'Close_6_to_MA15', 'Close_7_to_MA15', 'Close_8_to_MA15', 'Close_9_to_MA15', 'Close_11_to_MA15', 'Close_12_to_MA15', 'Close_14_to_MA15', 'Close_15_to_MA15', 'RSI9_dw_20_perman', 'RSI14_up_70_perman', 'RSI14_dw_30_perman', 'RSI20_up_70_perman', 'RSI20_dw_30_perman', 'RSI20_up_80_perman', 'RSI27_up_70_perman', 'RSI27_dw_30_perman', 'RSI9', 'RSI14', 'RSI20', 'RSI27', 'level_close_old_w', 'level_close_act_w', 'step_to_fiba', 'MACDHist_corr_shift1', 'MACDHist_corr_shift3', 'MACDHist_corr_shift6', 'AweOs_cor_shift1', 'AweOs_cor_shift3', 'AweOs_cor_shift6', 'MACDHist_corr_0_to_1', 'MACDHist_corr_1_to_3', 'MACDHist_corr_3_to_6', 'MACDHist_0_to_1', 'MACDHist_1_to_3', 'MACDHist_3_to_6', 'AweOs_0_to_1', 'AweOs_1_to_3', 'AweOs_3_to_6', 'AweOs_corr_0_to_1', 'AweOs_corr_1_to_3', 'Close_coef_nak2']




#версия 25.06
# col_fin_dw_1h=['MACDHist_corr', 'AweOs_cor', 'ROC200', 'ROC200sm', 'TSI', 'EMA8_REL', 'EMA8_REL_shift1', 'EMA8_REL_shift6', 'EMA8_REL_shift6_cross', 'EMA8_REL_shift12', 'EMA8_REL_shift24', 'EMA12_REL', 'EMA12_REL_shift6', 'EMA12_REL_shift12', 'EMA12_REL_shift24', 'EMA12_REL_shift24_cross', 'EMA14_REL', 'EMA14_REL_shift1', 'EMA14_REL_shift12', 'EMA14_REL_shift24', 'EMA20_REL', 'EMA20_REL_shift1', 'EMA20_REL_shift6', 'EMA20_REL_shift12', 'EMA20_REL_shift24', 'EMA20_REL_shift24_cross', 'EMA26_REL', 'EMA26_REL_shift1', 'EMA26_REL_shift6', 'EMA26_REL_shift12', 'EMA26_REL_shift24', 'EMA32_REL', 'EMA32_REL_shift1', 'EMA32_REL_shift6', 'EMA32_REL_shift12', 'EMA32_REL_shift24', 'EMA38_REL', 'EMA38_REL_shift1', 'EMA38_REL_shift6', 'EMA38_REL_shift12', 'EMA38_REL_shift24', 'EMA38_REL_shift24_cross', 'EMA44_REL', 'EMA44_REL_shift1', 'EMA44_REL_shift6', 'EMA44_REL_shift12', 'EMA44_REL_shift24', 'EMA50_REL', 'EMA50_REL_shift1', 'EMA50_REL_shift6', 'EMA50_REL_shift12', 'EMA50_REL_shift24', 'EMA60_REL', 'EMA60_REL_shift1', 'EMA60_REL_shift6', 'EMA60_REL_shift12', 'EMA60_REL_shift24', 'EMA75_REL', 'EMA75_REL_shift1', 'EMA75_REL_shift6', 'EMA75_REL_shift6_cross', 'EMA75_REL_shift12', 'EMA75_REL_shift24', 'EMA75_REL_shift24_cross', 'EMA100_REL', 'EMA100_REL_shift1', 'EMA100_REL_shift6', 'EMA100_REL_shift6_cross', 'EMA100_REL_shift12', 'EMA100_REL_shift12_cross', 'EMA100_REL_shift24', 'EMA100_REL_shift24_cross', 'EMA150_REL', 'EMA150_REL_shift1', 'EMA150_REL_shift6', 'EMA150_REL_shift12', 'EMA150_REL_shift12_cross', 'EMA150_REL_shift24', 'EMA150_REL_shift24_cross', 'EMA200_REL', 'EMA200_REL_shift1', 'EMA200_REL_shift6', 'EMA200_REL_shift6_cross', 'EMA200_REL_shift12', 'EMA200_REL_shift12_cross', 'EMA200_REL_shift24', 'EMA200_REL_shift24_cross', 'MA5_REL', 'MA5_REL_shift1', 'MA5_REL_shift6', 'MA5_REL_shift12', 'MA5_REL_shift12_cross', 'MA5_REL_shift24', 'MA5_REL_shift24_cross', 'MA10_REL', 'MA10_REL_shift1', 'MA10_REL_shift6', 'MA10_REL_shift6_cross', 'MA10_REL_shift12', 'MA10_REL_shift12_cross', 'MA10_REL_shift24', 'MA15_REL', 'MA15_REL_shift6', 'MA15_REL_shift12', 'MA15_REL_shift24', 'MA15_REL_shift24_cross', 'MA20_REL', 'MA20_REL_shift1', 'MA20_REL_shift6', 'MA20_REL_shift12', 'MA20_REL_shift12_cross', 'MA20_REL_shift24', 'MA25_REL', 'MA25_REL_shift1', 'MA25_REL_shift6', 'MA25_REL_shift12', 'MA25_REL_shift12_cross', 'MA25_REL_shift24', 'MA50_REL', 'MA50_REL_shift1', 'MA50_REL_shift6', 'MA50_REL_shift6_cross', 'MA50_REL_shift12', 'MA50_REL_shift12_cross', 'MA50_REL_shift24', 'MA50_REL_shift24_cross', 'MA75_REL', 'MA75_REL_shift1', 'MA75_REL_shift6', 'MA75_REL_shift12', 'MA75_REL_shift24', 'MA75_REL_shift24_cross', 'MA100_REL', 'MA100_REL_shift1', 'MA100_REL_shift6', 'MA100_REL_shift12', 'MA100_REL_shift12_cross', 'MA100_REL_shift24', 'MA150_REL', 'MA150_REL_shift1', 'MA150_REL_shift6', 'MA150_REL_shift6_cross', 'MA150_REL_shift12', 'MA150_REL_shift12_cross', 'MA150_REL_shift24', 'MA150_REL_shift24_cross', 'MA200_REL', 'MA200_REL_shift1', 'MA200_REL_shift6', 'MA200_REL_shift12', 'MA200_REL_shift12_cross', 'MA200_REL_shift24', 'MA200_REL_shift24_cross', 'MACDHist_REL', 'MACDHist_REL_shift1', 'MACDHist_REL_shift3', 'MACDHist_REL_shift5', 'MACDHist_REL_shift7', 'MACDHist_REL_shift10', 'RSI14_up_70', 'EMA_gor_1_REL_cross_all', 'EMA_gor_6_REL_cross_all', 'EMA_gor_12_REL_cross_all', 'EMA_gor_24_REL_cross_all', 'MA_gor_1_REL_cross_all', 'MA_gor_6_REL_cross_all', 'MA_gor_12_REL_cross_all', 'MA_gor_24_REL_cross_all', 'date_key_h', 'date_key_d', 'std_20_rel', 'std_100_rel', 'std_500_rel', 'RSI14_coef_nak', 'Close_coef_nak', 'Volume_coef_nak', 'EMA14_coef_nak', 'MA100_coef_nak', 'std_20_coef_nak', 'MACDHist_nak', 'Close_coef_nak_div_Volume_coef_nak', 'Close_coef_nak_div_RSI14_coef_nak', 'Close_coef_nak_div_MACDHist_nak', 'Close_0_to_1', 'Close_1_to_2', 'Close_2_to_3', 'Close_3_to_4', 'Close_4_to_5', 'Close_5_to_6', 'Close_6_to_7', 'Close_7_to_8', 'Close_8_to_9', 'Close_9_to_10', 'Close_10_to_11', 'Close_11_to_12', 'Close_0_to_3', 'Close_0_to_4', 'Close_0_to_5', 'Close_0_to_6', 'Close_0_to_9', 'Close_0_to_12', 'Close_m3_0_to_MA15', 'Close_m3_1_to_MA15', 'Close_m3_2_to_MA15', 'Close_m3_3_to_MA15', 'Close_m3_4_to_MA15', 'Close_m3_5_to_MA15', 'Close_m3_6_to_MA15', 'Close_m3_9_to_MA15', 'Close_m3_12_to_MA15', 'Close_0_to_MA15', 'Close_2_to_MA15', 'Close_3_to_MA15', 'Close_4_to_MA15', 'Close_5_to_MA15', 'Close_6_to_MA15', 'Close_7_to_MA15', 'Close_8_to_MA15', 'Close_9_to_MA15', 'Close_10_to_MA15', 'Close_12_to_MA15', 'Close_13_to_MA15', 'Close_14_to_MA15', 'Close_15_to_MA15', 'RSI9_dw_30_perman', 'RSI9_up_80_perman', 'RSI9_dw_20_perman', 'RSI14_up_70_perman', 'RSI14_dw_30_perman', 'RSI20_up_70_perman', 'RSI20_dw_30_perman', 'RSI20_up_80_perman', 'RSI20_dw_20_perman', 'RSI27_up_70_perman', 'RSI27_dw_30_perman', 'RSI9', 'RSI14', 'RSI20', 'RSI27', 'level_close_old_w', 'level_close_act_w', 'step_to_fiba', 'MACDHist_corr_shift1', 'MACDHist_corr_shift3', 'MACDHist_corr_shift6', 'AweOs_cor_shift1', 'AweOs_cor_shift3', 'AweOs_cor_shift6', 'MACDHist_corr_0_to_1', 'MACDHist_corr_1_to_3', 'MACDHist_corr_3_to_6', 'MACDHist_0_to_1', 'MACDHist_1_to_3', 'MACDHist_3_to_6', 'AweOs_0_to_1', 'AweOs_1_to_3', 'AweOs_3_to_6', 'AweOs_corr_0_to_1', 'AweOs_corr_1_to_3', 'Close_coef_nak2']



#версия 25.06
# MODEL_PARAMS_DW_1H = {

#      'boosting_type':'dart',
#       'num_leaves': 100, 
# #      'max_depth': 9, 
#       'learning_rate': 0.1,
#       'n_estimators': 100,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7, 
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
#       'reg_lambda': 50,
# #      'random_state': 42, 
#     'scale_pos_weight': 1,
#       'n_jobs': 10
# }


#версия 25.06
# MODEL_PARAMS_UP_1H = {

#      'boosting_type':'goss',
# #      'num_leaves': 31, 
# #      'max_depth': 9, 
# #      'learning_rate': 0.13,
#       'n_estimators': 200,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7, 
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
#       'reg_lambda': 0,
# #      'random_state': 42, 
#     'scale_pos_weight': 4,
#       'n_jobs': 10
# }




####################       1H      ВЕРСИЯ 28.06


# #версия 28.06
# col_fin_up_1h=['MACDHist_corr', 'AweOs_cor', 'ROC200', 'ROC200sm', 'TSI', 'EMA14_REL_shift24', 'EMA20_REL_shift12', 'EMA26_REL_shift12', 'EMA32_REL_shift24', 'EMA38_REL', 'EMA38_REL_shift24', 'EMA44_REL', 'EMA44_REL_shift6', 'EMA60_REL', 'EMA60_REL_shift24', 'EMA75_REL', 'EMA75_REL_shift12', 'EMA100_REL', 'EMA100_REL_shift6', 'EMA100_REL_shift12', 'EMA100_REL_shift24', 'EMA150_REL', 'EMA150_REL_shift6', 'EMA150_REL_shift12', 'EMA150_REL_shift24', 'EMA200_REL', 'EMA200_REL_shift1', 'EMA200_REL_shift6', 'EMA200_REL_shift12', 'EMA200_REL_shift24', 'MA5_REL_shift1', 'MA5_REL_shift12', 'MA5_REL_shift24', 'MA10_REL', 'MA10_REL_shift1', 'MA10_REL_shift12', 'MA10_REL_shift24', 'MA15_REL', 'MA15_REL_shift6', 'MA15_REL_shift12', 'MA15_REL_shift24', 'MA20_REL', 'MA20_REL_shift6', 'MA20_REL_shift12', 'MA20_REL_shift24', 'MA25_REL', 'MA25_REL_shift6', 'MA25_REL_shift12', 'MA25_REL_shift12_cross', 'MA25_REL_shift24', 'MA50_REL', 'MA50_REL_shift1', 'MA50_REL_shift6', 'MA50_REL_shift12', 'MA50_REL_shift24', 'MA75_REL', 'MA75_REL_shift6', 'MA75_REL_shift12', 'MA75_REL_shift24', 'MA100_REL', 'MA100_REL_shift1', 'MA100_REL_shift6', 'MA100_REL_shift12', 'MA100_REL_shift24', 'MA150_REL', 'MA150_REL_shift6', 'MA150_REL_shift12', 'MA150_REL_shift24', 'MA200_REL', 'MA200_REL_shift1', 'MA200_REL_shift6', 'MA200_REL_shift12', 'MA200_REL_shift24', 'MACDHist_REL', 'MACDHist_REL_shift1', 'MACDHist_REL_shift3', 'MACDHist_REL_shift5', 'MACDHist_REL_shift7', 'MACDHist_REL_shift10', 'EMA_gor_6_REL_cross_all', 'EMA_gor_24_REL_cross_all', 'MA_gor_6_REL_cross_all', 'MA_gor_12_REL_cross_all', 'MA_gor_24_REL_cross_all', 'date_key_h', 'date_key_d', 'std_20_rel', 'std_100_rel', 'std_500_rel', 'RSI14_coef_nak', 'Close_coef_nak', 'Volume_coef_nak', 'EMA14_coef_nak', 'MA100_coef_nak', 'std_20_coef_nak', 'MACDHist_nak', 'Close_coef_nak_div_Volume_coef_nak', 'Close_coef_nak_div_RSI14_coef_nak', 'Close_coef_nak_div_MACDHist_nak', 'Close_0_to_1', 'Close_1_to_2', 'Close_5_to_6', 'Close_8_to_9', 'Close_9_to_10', 'Close_11_to_12', 'Close_0_to_6', 'Close_0_to_9', 'Close_0_to_12', 'Close_m3_0_to_MA15', 'Close_m3_1_to_MA15', 'Close_m3_2_to_MA15', 'Close_m3_6_to_MA15', 'Close_m3_9_to_MA15', 'Close_m3_12_to_MA15', 'Close_3_to_MA15', 'Close_6_to_MA15', 'Close_8_to_MA15', 'Close_10_to_MA15', 'Close_12_to_MA15', 'Close_13_to_MA15', 'Close_14_to_MA15', 'Close_15_to_MA15', 'RSI14_dw_30_perman', 'RSI20_up_70_perman', 'RSI27_dw_30_perman', 'RSI9', 'RSI14', 'RSI20', 'RSI27', 'level_close_old_w', 'level_close_act_w', 'step_to_fiba', 'MACDHist_corr_shift1', 'MACDHist_corr_shift3', 'MACDHist_corr_shift6', 'AweOs_cor_shift1', 'AweOs_cor_shift3', 'AweOs_cor_shift6', 'MACDHist_corr_3_to_6', 'MACDHist_0_to_1', 'AweOs_0_to_1', 'AweOs_1_to_3', 'AweOs_3_to_6', 'AweOs_corr_0_to_1', 'AweOs_corr_1_to_3', 'Close_coef_nak2', 'PER_OPEN_shift0', 'PER_OPEN_shift3', 'PER_CLOSE_shift0', 'PER_CLOSE_shift1', 'PER_CLOSE_shift3', 'PER_CLOSE_shift6', 'POLNOTA_shift0', 'POLNOTA_shift1', 'POLNOTA_shift3', 'POLNOTA_shift5', 'POLNOTA_shift6', 'Close_5_to_b', 'Open_0_to_b', 'Open_1_to_b', 'Low_0_to_b', 'Low_3_to_b', 'Low_4_to_b', 'Low_5_to_b', 'High_0_to_b', 'High_1_to_b', 'High_2_to_b', 'High_3_to_b', 'High_4_to_b', 'High_5_to_b', 'EVENT20', 'EVENT16', 'EVENT15', 'EVENT14', 'EVENT13', 'EVENT10', 'EVENT3']


# #версия 28.06
# col_fin_dw_1h=['MACDHist_corr', 'AweOs_cor', 'ROC200', 'ROC200sm', 'TSI', 'EMA8_REL', 'EMA14_REL_shift1', 'EMA14_REL_shift24', 'EMA20_REL_shift24', 'EMA26_REL', 'EMA26_REL_shift12', 'EMA26_REL_shift24', 'EMA32_REL', 'EMA32_REL_shift12', 'EMA38_REL', 'EMA38_REL_shift6', 'EMA44_REL_shift24', 'EMA75_REL', 'EMA75_REL_shift12', 'EMA100_REL_shift6', 'EMA100_REL_shift24', 'EMA150_REL', 'EMA150_REL_shift24', 'EMA200_REL', 'EMA200_REL_shift1', 'EMA200_REL_shift6', 'EMA200_REL_shift12', 'EMA200_REL_shift24', 'MA5_REL_shift6', 'MA5_REL_shift12', 'MA5_REL_shift24', 'MA10_REL', 'MA10_REL_shift12', 'MA10_REL_shift24', 'MA15_REL_shift6', 'MA15_REL_shift12', 'MA15_REL_shift24', 'MA20_REL', 'MA20_REL_shift12', 'MA20_REL_shift24', 'MA25_REL', 'MA25_REL_shift6', 'MA25_REL_shift12', 'MA25_REL_shift12_cross', 'MA25_REL_shift24', 'MA50_REL', 'MA50_REL_shift1', 'MA50_REL_shift6', 'MA50_REL_shift12', 'MA50_REL_shift24', 'MA75_REL', 'MA75_REL_shift1', 'MA75_REL_shift6', 'MA75_REL_shift12', 'MA75_REL_shift24', 'MA100_REL', 'MA100_REL_shift1', 'MA100_REL_shift12', 'MA100_REL_shift24', 'MA150_REL', 'MA150_REL_shift1', 'MA150_REL_shift6', 'MA150_REL_shift12', 'MA150_REL_shift24', 'MA150_REL_shift24_cross', 'MA200_REL', 'MA200_REL_shift1', 'MA200_REL_shift6', 'MA200_REL_shift12', 'MA200_REL_shift12_cross', 'MA200_REL_shift24', 'MACDHist_REL', 'MACDHist_REL_shift1', 'MACDHist_REL_shift3', 'MACDHist_REL_shift5', 'MACDHist_REL_shift7', 'MACDHist_REL_shift10', 'EMA_gor_1_REL_cross_all', 'EMA_gor_24_REL_cross_all', 'date_key_h', 'date_key_d', 'std_20_rel', 'std_100_rel', 'std_500_rel', 'RSI14_coef_nak', 'Close_coef_nak', 'Volume_coef_nak', 'EMA14_coef_nak', 'MA100_coef_nak', 'std_20_coef_nak', 'MACDHist_nak', 'Close_coef_nak_div_Volume_coef_nak', 'Close_coef_nak_div_MACDHist_nak', 'Close_1_to_2', 'Close_3_to_4', 'Close_7_to_8', 'Close_8_to_9', 'Close_10_to_11', 'Close_11_to_12', 'Close_0_to_3', 'Close_0_to_4', 'Close_0_to_12', 'Close_m3_0_to_MA15', 'Close_m3_1_to_MA15', 'Close_m3_2_to_MA15', 'Close_m3_4_to_MA15', 'Close_m3_6_to_MA15', 'Close_m3_9_to_MA15', 'Close_m3_12_to_MA15', 'Close_3_to_MA15', 'Close_7_to_MA15', 'Close_8_to_MA15', 'Close_9_to_MA15', 'Close_13_to_MA15', 'Close_15_to_MA15', 'RSI9_dw_30_perman', 'RSI20_up_70_perman', 'RSI9', 'RSI14', 'RSI20', 'RSI27', 'level_close_old_w', 'level_close_act_w', 'step_to_fiba', 'MACDHist_corr_shift1', 'MACDHist_corr_shift3', 'MACDHist_corr_shift6', 'AweOs_cor_shift1', 'AweOs_cor_shift3', 'AweOs_cor_shift6', 'MACDHist_corr_1_to_3', 'MACDHist_corr_3_to_6', 'MACDHist_0_to_1', 'AweOs_1_to_3', 'AweOs_3_to_6', 'AweOs_corr_0_to_1', 'Close_coef_nak2', 'PER_OPEN_shift2', 'PER_OPEN_shift4', 'PER_OPEN_shift6', 'PER_CLOSE_shift1', 'PER_CLOSE_shift2', 'PER_CLOSE_shift3', 'PER_CLOSE_shift6', 'POLNOTA_shift0', 'POLNOTA_shift1', 'POLNOTA_shift3', 'POLNOTA_shift4', 'POLNOTA_shift6', 'Close_3_to_b', 'Close_5_to_b', 'Open_0_to_b', 'Open_1_to_b', 'Open_3_to_b', 'Open_5_to_b', 'Low_0_to_b', 'Low_1_to_b', 'Low_4_to_b', 'Low_5_to_b', 'High_0_to_b', 'High_1_to_b', 'High_2_to_b', 'High_4_to_b', 'EVENT20', 'EVENT19', 'EVENT16', 'EVENT15', 'EVENT14', 'EVENT13', 'EVENT9', 'EVENT3']


# #версия 28.06
# MODEL_PARAMS_DW_1H = {

#      'boosting_type':'dart',
#       'num_leaves': 31, 
# #      'max_depth': 9, 
# #      'learning_rate': 0.1,
#       'n_estimators': 300,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7, 
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
#       'reg_lambda': 220,
# #      'random_state': 42, 
#     'scale_pos_weight': 1,
#       'n_jobs': 10
# }


# #версия 28.06
# MODEL_PARAMS_UP_1H = {

#      'boosting_type':'gbdt',
#       'num_leaves': 50, 
# #      'max_depth': 9, 
# #      'learning_rate': 0.1,
#       'n_estimators': 100,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7, 
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
#       'reg_lambda': 200,
# #      'random_state': 42, 
#     'scale_pos_weight': 1,
#       'n_jobs': 10
# }




####################       1H      ВЕРСИЯ 08.07


# #версия 08.07
# col_fin_up_1h=['MACDHist_corr', 'AweOs_cor', 'ROC200', 'ROC200sm', 'TSI', 'EMA8_REL', 'EMA8_REL_shift1', 'EMA8_REL_shift6', 'EMA8_REL_shift12', 'EMA8_REL_shift24', 'EMA12_REL', 'EMA12_REL_shift1', 'EMA12_REL_shift6', 'EMA12_REL_shift12', 'EMA12_REL_shift24', 'EMA14_REL', 'EMA14_REL_shift12', 'EMA20_REL', 'EMA20_REL_shift1', 'EMA20_REL_shift6', 'EMA20_REL_shift6_cross', 'EMA20_REL_shift12', 'EMA20_REL_shift24', 'EMA26_REL', 'EMA26_REL_shift1', 'EMA26_REL_shift6', 'EMA26_REL_shift12', 'EMA26_REL_shift24', 'EMA32_REL', 'EMA32_REL_shift1', 'EMA32_REL_shift6', 'EMA32_REL_shift12', 'EMA32_REL_shift12_cross', 'EMA32_REL_shift24', 'EMA38_REL', 'EMA38_REL_shift1', 'EMA38_REL_shift6', 'EMA38_REL_shift12', 'EMA38_REL_shift24', 'EMA38_REL_shift24_cross', 'EMA44_REL', 'EMA44_REL_shift1_cross', 'EMA44_REL_shift6', 'EMA44_REL_shift12', 'EMA44_REL_shift24', 'EMA50_REL', 'EMA50_REL_shift1', 'EMA50_REL_shift6', 'EMA50_REL_shift12', 'EMA50_REL_shift24', 'EMA60_REL', 'EMA60_REL_shift1', 'EMA60_REL_shift12', 'EMA60_REL_shift12_cross', 'EMA60_REL_shift24', 'EMA75_REL', 'EMA75_REL_shift1', 'EMA75_REL_shift6', 'EMA75_REL_shift12', 'EMA75_REL_shift12_cross', 'EMA75_REL_shift24', 'EMA100_REL', 'EMA100_REL_shift1', 'EMA100_REL_shift6', 'EMA100_REL_shift6_cross', 'EMA100_REL_shift12', 'EMA100_REL_shift24', 'EMA100_REL_shift24_cross', 'EMA150_REL', 'EMA150_REL_shift1', 'EMA150_REL_shift6', 'EMA150_REL_shift12', 'EMA150_REL_shift24', 'EMA150_REL_shift24_cross', 'EMA200_REL', 'EMA200_REL_shift1', 'EMA200_REL_shift6', 'EMA200_REL_shift12', 'EMA200_REL_shift24', 'EMA200_REL_shift24_cross', 'MA5_REL', 'MA5_REL_shift1', 'MA5_REL_shift6_cross', 'MA5_REL_shift12', 'MA5_REL_shift12_cross', 'MA5_REL_shift24', 'MA10_REL', 'MA10_REL_shift1', 'MA10_REL_shift6', 'MA10_REL_shift12', 'MA10_REL_shift12_cross', 'MA10_REL_shift24', 'MA10_REL_shift24_cross', 'MA15_REL', 'MA15_REL_shift6', 'MA15_REL_shift12', 'MA15_REL_shift12_cross', 'MA15_REL_shift24', 'MA15_REL_shift24_cross', 'MA20_REL', 'MA20_REL_shift1', 'MA20_REL_shift6', 'MA20_REL_shift12', 'MA20_REL_shift24', 'MA20_REL_shift24_cross', 'MA25_REL', 'MA25_REL_shift1', 'MA25_REL_shift6', 'MA25_REL_shift6_cross', 'MA25_REL_shift12', 'MA25_REL_shift12_cross', 'MA25_REL_shift24', 'MA25_REL_shift24_cross', 'MA50_REL', 'MA50_REL_shift1', 'MA50_REL_shift6', 'MA50_REL_shift12', 'MA50_REL_shift24', 'MA50_REL_shift24_cross', 'MA75_REL', 'MA75_REL_shift1', 'MA75_REL_shift6', 'MA75_REL_shift12', 'MA75_REL_shift12_cross', 'MA75_REL_shift24', 'MA100_REL', 'MA100_REL_shift1', 'MA100_REL_shift6', 'MA100_REL_shift12', 'MA100_REL_shift12_cross', 'MA100_REL_shift24', 'MA150_REL', 'MA150_REL_shift1', 'MA150_REL_shift6', 'MA150_REL_shift12', 'MA150_REL_shift12_cross', 'MA150_REL_shift24', 'MA150_REL_shift24_cross', 'MA200_REL', 'MA200_REL_shift1', 'MA200_REL_shift6', 'MA200_REL_shift12', 'MA200_REL_shift24', 'MA200_REL_shift24_cross', 'MACDHist_REL', 'MACDHist_REL_shift1', 'MACDHist_REL_shift3', 'MACDHist_REL_shift5', 'MACDHist_REL_shift7', 'MACDHist_REL_shift10', 'EMA_gor_1_REL_cross_all', 'EMA_gor_6_REL_cross_all', 'EMA_gor_12_REL_cross_all', 'EMA_gor_24_REL_cross_all', 'MA_gor_6_REL_cross_all', 'MA_gor_12_REL_cross_all', 'MA_gor_24_REL_cross_all', 'date_key_h', 'date_key_d', 'std_20_rel', 'std_100_rel', 'RSI14_coef_nak', 'Close_coef_nak', 'Volume_coef_nak', 'EMA14_coef_nak', 'MA100_coef_nak', 'std_20_coef_nak', 'MACDHist_nak', 'Close_coef_nak_div_Volume_coef_nak', 'Close_coef_nak_div_RSI14_coef_nak', 'Close_coef_nak_div_MACDHist_nak', 'Close_1_to_2', 'Close_2_to_3', 'Close_3_to_4', 'Close_4_to_5', 'Close_6_to_7', 'Close_7_to_8', 'Close_8_to_9', 'Close_9_to_10', 'Close_10_to_11', 'Close_11_to_12', 'Close_0_to_3', 'Close_0_to_4', 'Close_0_to_5', 'Close_0_to_6', 'Close_0_to_9', 'Close_0_to_12', 'Close_m3_0_to_MA15', 'Close_m3_1_to_MA15', 'Close_m3_2_to_MA15', 'Close_m3_3_to_MA15', 'Close_m3_4_to_MA15', 'Close_m3_5_to_MA15', 'Close_m3_6_to_MA15', 'Close_m3_9_to_MA15', 'Close_m3_12_to_MA15', 'Close_0_to_MA15', 'Close_1_to_MA15', 'Close_2_to_MA15', 'Close_3_to_MA15', 'Close_4_to_MA15', 'Close_5_to_MA15', 'Close_6_to_MA15', 'Close_7_to_MA15', 'Close_8_to_MA15', 'Close_9_to_MA15', 'Close_10_to_MA15', 'Close_11_to_MA15', 'Close_12_to_MA15', 'Close_13_to_MA15', 'Close_14_to_MA15', 'Close_15_to_MA15', 'RSI9_up_70_perman', 'RSI9_dw_30_perman', 'RSI9_dw_20_perman', 'RSI14_up_70_perman', 'RSI14_dw_30_perman', 'RSI14_up_80_perman', 'RSI20_up_70_perman', 'RSI20_dw_30_perman', 'RSI20_up_80_perman', 'RSI27_up_70_perman', 'RSI27_dw_30_perman', 'RSI9', 'RSI14', 'RSI20', 'RSI27', 'level_close_old_w', 'level_close_act_w', 'step_to_fiba', 'MACDHist_corr_shift1', 'MACDHist_corr_shift3', 'MACDHist_corr_shift6', 'AweOs_cor_shift1', 'AweOs_cor_shift3', 'AweOs_cor_shift6', 'MACDHist_corr_0_to_1', 'MACDHist_corr_1_to_3', 'MACDHist_corr_3_to_6', 'MACDHist_0_to_1', 'MACDHist_1_to_3', 'MACDHist_3_to_6', 'AweOs_0_to_1', 'AweOs_1_to_3', 'AweOs_3_to_6', 'AweOs_corr_0_to_1', 'AweOs_corr_1_to_3', 'Close_coef_nak2', 'PER_OPEN_shift0', 'PER_OPEN_shift1', 'PER_OPEN_shift2', 'PER_OPEN_shift3', 'PER_OPEN_shift4', 'PER_OPEN_shift5', 'PER_OPEN_shift6', 'PER_CLOSE_shift0', 'PER_CLOSE_shift1', 'PER_CLOSE_shift2', 'PER_CLOSE_shift3', 'PER_CLOSE_shift4', 'PER_CLOSE_shift5', 'PER_CLOSE_shift6', 'POLNOTA_shift0', 'POLNOTA_shift1', 'POLNOTA_shift2', 'POLNOTA_shift3', 'POLNOTA_shift4', 'POLNOTA_shift5', 'POLNOTA_shift6', 'Close_2_to_b', 'Close_3_to_b', 'Close_5_to_b', 'Open_0_to_b', 'Open_1_to_b', 'Open_2_to_b', 'Open_3_to_b', 'Open_4_to_b', 'Open_5_to_b', 'Low_0_to_b', 'Low_1_to_b', 'Low_2_to_b', 'Low_3_to_b', 'Low_4_to_b', 'Low_5_to_b', 'High_0_to_b', 'High_1_to_b', 'High_2_to_b', 'High_3_to_b', 'High_4_to_b', 'High_5_to_b', 'EVENT20', 'EVENT19', 'EVENT16', 'EVENT15', 'EVENT14', 'EVENT13', 'EVENT10', 'EVENT9', 'EVENT7', 'EVENT3', 'down_near', 'up_near', 'mae_opt_near', 'down_far', 'up_far', 'mae_opt_far']


# #версия 08.07
# col_fin_dw_1h=['MACDHist_corr', 'AweOs_cor', 'ROC200', 'ROC200sm', 'TSI', 'EMA12_REL_shift24', 'EMA32_REL', 'EMA38_REL_shift12', 'EMA44_REL_shift24', 'EMA75_REL', 'EMA100_REL_shift1', 'EMA100_REL_shift6', 'EMA100_REL_shift12', 'EMA100_REL_shift24', 'EMA150_REL', 'EMA150_REL_shift1', 'EMA150_REL_shift12', 'EMA150_REL_shift24', 'EMA200_REL', 'EMA200_REL_shift1', 'EMA200_REL_shift6', 'EMA200_REL_shift12', 'EMA200_REL_shift24', 'EMA200_REL_shift24_cross', 'MA5_REL_shift6', 'MA5_REL_shift12', 'MA5_REL_shift24', 'MA10_REL', 'MA10_REL_shift12', 'MA10_REL_shift24', 'MA15_REL', 'MA15_REL_shift6', 'MA15_REL_shift12', 'MA15_REL_shift24', 'MA20_REL', 'MA20_REL_shift12', 'MA20_REL_shift24', 'MA25_REL', 'MA25_REL_shift6', 'MA25_REL_shift12', 'MA25_REL_shift24', 'MA50_REL', 'MA50_REL_shift1', 'MA50_REL_shift6', 'MA50_REL_shift12', 'MA50_REL_shift24', 'MA75_REL', 'MA75_REL_shift1', 'MA75_REL_shift6', 'MA75_REL_shift12', 'MA75_REL_shift24', 'MA100_REL', 'MA100_REL_shift6', 'MA100_REL_shift12', 'MA100_REL_shift24', 'MA150_REL', 'MA150_REL_shift1', 'MA150_REL_shift6', 'MA150_REL_shift12', 'MA150_REL_shift24', 'MA150_REL_shift24_cross', 'MA200_REL', 'MA200_REL_shift1', 'MA200_REL_shift6', 'MA200_REL_shift12', 'MA200_REL_shift12_cross', 'MA200_REL_shift24', 'MACDHist_REL', 'MACDHist_REL_shift1', 'MACDHist_REL_shift3', 'MACDHist_REL_shift5', 'MACDHist_REL_shift7', 'MACDHist_REL_shift10', 'EMA_gor_1_REL_cross_all', 'date_key_h', 'date_key_d', 'std_20_rel', 'std_100_rel', 'RSI14_coef_nak', 'Close_coef_nak', 'Volume_coef_nak', 'EMA14_coef_nak', 'MA100_coef_nak', 'std_20_coef_nak', 'MACDHist_nak', 'Close_coef_nak_div_Volume_coef_nak', 'Close_coef_nak_div_RSI14_coef_nak', 'Close_coef_nak_div_MACDHist_nak', 'Close_0_to_1', 'Close_1_to_2', 'Close_3_to_4', 'Close_7_to_8', 'Close_8_to_9', 'Close_10_to_11', 'Close_11_to_12', 'Close_0_to_6', 'Close_m3_0_to_MA15', 'Close_m3_1_to_MA15', 'Close_m3_2_to_MA15', 'Close_m3_4_to_MA15', 'Close_m3_6_to_MA15', 'Close_m3_9_to_MA15', 'Close_m3_12_to_MA15', 'Close_2_to_MA15', 'Close_8_to_MA15', 'Close_14_to_MA15', 'Close_15_to_MA15', 'RSI20_up_70_perman', 'RSI9', 'RSI14', 'RSI20', 'RSI27', 'level_close_old_w', 'level_close_act_w', 'step_to_fiba', 'MACDHist_corr_shift1', 'MACDHist_corr_shift3', 'MACDHist_corr_shift6', 'AweOs_cor_shift1', 'AweOs_cor_shift3', 'AweOs_cor_shift6', 'MACDHist_corr_0_to_1', 'MACDHist_corr_1_to_3', 'MACDHist_corr_3_to_6', 'MACDHist_3_to_6', 'AweOs_1_to_3', 'AweOs_3_to_6', 'AweOs_corr_0_to_1', 'Close_coef_nak2', 'PER_OPEN_shift1', 'PER_OPEN_shift2', 'PER_CLOSE_shift1', 'PER_CLOSE_shift3', 'PER_CLOSE_shift4', 'POLNOTA_shift1', 'Close_5_to_b', 'Open_0_to_b', 'Open_1_to_b', 'Open_2_to_b', 'Open_3_to_b', 'Low_0_to_b', 'Low_1_to_b', 'Low_4_to_b', 'Low_5_to_b', 'High_0_to_b', 'High_2_to_b', 'High_4_to_b', 'EVENT19', 'EVENT18', 'EVENT16', 'EVENT15', 'EVENT14', 'EVENT13', 'EVENT3', 'down_near', 'up_near', 'mae_opt_near', 'down_far', 'up_far', 'mae_opt_far']


# #версия 08.07
# MODEL_PARAMS_DW_1H = {

# #     'boosting_type':'gbdt',
# #      'num_leaves': 31, 
# #      'max_depth': 9, 
#       'learning_rate': 0.05,
# #      'n_estimators': 300,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7, 
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
#       'reg_lambda': 250,
# #      'random_state': 42, 
#     'scale_pos_weight': 1,
#       'n_jobs': 10
# }



# #версия 08.07
# MODEL_PARAMS_UP_1H = {

#      'boosting_type':'gbdt',
# #      'num_leaves': 50, 
# #      'max_depth': 9, 
# #      'learning_rate': 0.1,
# #      'n_estimators': 100,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7, 
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
#       'reg_lambda': 150,
# #      'random_state': 42, 
#     'scale_pos_weight': 1,
#       'n_jobs': 10
# }








# ####################       1H      ВЕРСИЯ 27.08


# #версия 27.08
# col_fin_up_1h=['MA75_REL_shift12', 'Low_4_to_b', 'plotnost_300_ch', 'MACDHist_corr_1_to_3', 'MA20_REL_shift12', 'AweOs_cor_shift6', 'MA5_REL', 'Close_1_to_b', 'MACDHist_REL_shift5', 'Close_8_to_MA15', 'POLNOTA_shift10', 'MACDHist_corr_shift6', 'freq_up_ch_100', 'MA50_REL_shift1_cross', 'Close_0_to_5', 'EMA20_REL_shift6', 'PER_OPEN_shift8', 'balance_100_all', 'balance_100_ch', 'EMA60_REL_shift12', 'EMA_gor_12_REL_cross_all', 'MACDHist_3_to_6', 'EMA38_REL_shift6', 'MA20_REL_shift6', 'MACDHist_corr', 'RSI27', 'MA150_REL_shift1_cross', 'EMA20_REL', 'Close_2_to_MA15', 'POLNOTA_shift4', 'AweOs_cor', 'std_20_rel', 'plotnost_100_all', 'down_far', 'Close_8_to_9', 'MA25_REL_shift6', 'PER_OPEN_shift7', 'Close_m3_12_to_MA15', 'High_1_to_b', 'EMA26_REL_shift1', 'EMA44_REL', 'Close_7_to_MA15', 'MA100_REL_shift6', 'MA50_REL_shift6_cross', 'MA50_REL_shift12', 'EMA14_REL_shift6', 'EMA100_REL_shift1_cross', 'Close_7_to_8', 'Close_11_to_MA15', 'RSI9_dw_20', 'MA5_REL_shift24_cross', 'MA200_REL_shift6_cross', 'EMA12_REL_shift12', 'freq_up_ch_50', 'High_3_to_b', 'Close_m3_6_to_MA15', 'EMA200_REL_shift6_cross', 'Close_3_to_4', 'Volume_coef_nak', 'MACDHist_REL_shift3', 'EMA150_REL', 'Open_5_to_b', 'Close_10_to_MA15', 'PER_CLOSE_shift1', 'MA25_REL_shift1_cross', 'EMA38_REL', 'EVENT16', 'RSI9_dw_30', 'EMA100_REL_shift12_cross', 'Close_0_to_3', 'date_key_d', 'EMA38_REL_shift12', 'Close_6_to_7', 'MA100_REL_shift6_cross', 'Close_0_to_9', 'EMA_gor_6_REL_cross_all', 'MA_gor_6_REL_cross_all', 'MA15_REL_shift1', 'date_key_h', 'Close_9_to_10', 'EMA200_REL_shift12', 'plotnost_300_all', 'EMA200_REL']


# #версия 27.08
# col_fin_dw_1h=['ROC200', 'ROC200sm', 'TSI', 'EMA8_REL', 'EMA8_REL_shift1', 'EMA8_REL_shift6', 'EMA8_REL_shift6_cross', 'EMA8_REL_shift12', 'EMA8_REL_shift12_cross', 'EMA8_REL_shift24', 'EMA12_REL', 'EMA12_REL_shift1', 'EMA12_REL_shift1_cross', 'EMA12_REL_shift6_cross', 'EMA12_REL_shift12', 'EMA12_REL_shift24', 'EMA14_REL', 'EMA14_REL_shift1', 'EMA14_REL_shift1_cross', 'EMA14_REL_shift6_cross', 'EMA14_REL_shift12', 'EMA14_REL_shift12_cross', 'EMA14_REL_shift24', 'EMA20_REL', 'EMA20_REL_shift1', 'EMA20_REL_shift1_cross', 'EMA20_REL_shift6', 'EMA20_REL_shift12', 'EMA20_REL_shift24', 'EMA26_REL', 'EMA26_REL_shift1', 'EMA26_REL_shift1_cross', 'EMA26_REL_shift6', 'EMA26_REL_shift12', 'EMA26_REL_shift12_cross', 'EMA26_REL_shift24', 'EMA32_REL', 'EMA32_REL_shift1', 'EMA32_REL_shift6', 'EMA32_REL_shift6_cross', 'EMA32_REL_shift12', 'EMA32_REL_shift24', 'EMA38_REL', 'EMA38_REL_shift1', 'EMA38_REL_shift6', 'EMA38_REL_shift12', 'EMA38_REL_shift24', 'EMA44_REL', 'EMA44_REL_shift1', 'EMA44_REL_shift1_cross', 'EMA44_REL_shift6', 'EMA44_REL_shift6_cross', 'EMA44_REL_shift12', 'EMA44_REL_shift12_cross', 'EMA44_REL_shift24', 'EMA50_REL', 'EMA50_REL_shift1', 'EMA50_REL_shift1_cross', 'EMA50_REL_shift6', 'EMA50_REL_shift6_cross', 'EMA50_REL_shift12', 'EMA50_REL_shift24', 'EMA60_REL', 'EMA60_REL_shift1', 'EMA60_REL_shift1_cross', 'EMA60_REL_shift6', 'EMA60_REL_shift6_cross', 'EMA60_REL_shift12', 'EMA60_REL_shift12_cross', 'EMA60_REL_shift24', 'EMA75_REL', 'EMA75_REL_shift1', 'EMA75_REL_shift1_cross', 'EMA75_REL_shift6', 'EMA75_REL_shift12', 'EMA75_REL_shift12_cross', 'EMA75_REL_shift24', 'EMA100_REL', 'EMA100_REL_shift1', 'EMA100_REL_shift6', 'EMA100_REL_shift12', 'EMA100_REL_shift24', 'EMA150_REL', 'EMA150_REL_shift1', 'EMA150_REL_shift1_cross', 'EMA150_REL_shift6', 'EMA150_REL_shift12', 'EMA150_REL_shift12_cross', 'EMA150_REL_shift24', 'EMA200_REL', 'EMA200_REL_shift1', 'EMA200_REL_shift1_cross', 'EMA200_REL_shift6', 'EMA200_REL_shift6_cross', 'EMA200_REL_shift12', 'EMA200_REL_shift24', 'MA5_REL', 'MA5_REL_shift1', 'MA5_REL_shift1_cross', 'MA5_REL_shift6', 'MA5_REL_shift6_cross', 'MA5_REL_shift12', 'MA5_REL_shift12_cross', 'MA5_REL_shift24', 'MA5_REL_shift24_cross', 'MA10_REL', 'MA10_REL_shift1', 'MA10_REL_shift6', 'MA10_REL_shift12', 'MA15_REL', 'MA15_REL_shift1', 'MA15_REL_shift1_cross', 'MA15_REL_shift6', 'MA15_REL_shift6_cross', 'MA15_REL_shift12', 'MA20_REL', 'MA20_REL_shift1', 'MA20_REL_shift1_cross', 'MA20_REL_shift6', 'MA20_REL_shift6_cross', 'MA20_REL_shift12', 'MA25_REL', 'MA25_REL_shift1', 'MA25_REL_shift1_cross', 'MA25_REL_shift6', 'MA25_REL_shift6_cross', 'MA25_REL_shift12', 'MA50_REL', 'MA50_REL_shift1', 'MA50_REL_shift1_cross', 'MA50_REL_shift6', 'MA50_REL_shift6_cross', 'MA50_REL_shift12', 'MA75_REL', 'MA75_REL_shift1', 'MA75_REL_shift1_cross', 'MA75_REL_shift6', 'MA75_REL_shift6_cross', 'MA75_REL_shift12', 'MA100_REL', 'MA100_REL_shift1', 'MA100_REL_shift1_cross', 'MA100_REL_shift6', 'MA100_REL_shift6_cross', 'MA100_REL_shift12', 'MA150_REL', 'MA150_REL_shift1', 'MA150_REL_shift1_cross', 'MA150_REL_shift6', 'MA150_REL_shift12', 'MA200_REL', 'MA200_REL_shift1', 'MA200_REL_shift1_cross', 'MA200_REL_shift6', 'MA200_REL_shift12', 'MACDHist_REL_shift0', 'MACDHist_REL_shift1', 'MACDHist_REL_shift3', 'MACDHist_REL_shift5', 'MACDHist_REL_shift7', 'MACDHist_REL_shift10', 'RSI27_up_80', 'EMA_gor_1_REL_cross_all', 'EMA_gor_6_REL_cross_all', 'EMA_gor_12_REL_cross_all', 'EMA_gor_24_REL_cross_all', 'MA_gor_1_REL_cross_all', 'MA_gor_6_REL_cross_all', 'MA_gor_12_REL_cross_all', 'MA_gor_24_REL_cross_all', 'date_key_h', 'date_key_d', 'std_20_rel', 'std_100_rel', 'RSI14_coef_nak', 'Close_coef_nak', 'Volume_coef_nak', 'EMA14_coef_nak', 'MA100_coef_nak', 'std_20_coef_nak', 'MACDHist_nak', 'Close_coef_nak_div_Volume_coef_nak', 'Close_coef_nak_div_RSI14_coef_nak', 'Close_coef_nak_div_MACDHist_nak', 'Close_0_to_1', 'Close_1_to_2', 'Close_2_to_3', 'Close_3_to_4', 'Close_4_to_5', 'Close_5_to_6', 'Close_6_to_7', 'Close_7_to_8', 'Close_8_to_9', 'Close_9_to_10', 'Close_10_to_11', 'Close_11_to_12', 'Close_0_to_3', 'Close_0_to_4', 'Close_0_to_5', 'Close_0_to_6', 'Close_0_to_9', 'Close_0_to_12', 'Close_m3_0_to_MA15', 'Close_m3_1_to_MA15', 'Close_m3_3_to_MA15', 'Close_m3_4_to_MA15', 'Close_m3_5_to_MA15', 'Close_m3_6_to_MA15', 'Close_m3_9_to_MA15', 'Close_m3_12_to_MA15', 'Close_0_to_MA15', 'Close_1_to_MA15', 'Close_2_to_MA15', 'Close_3_to_MA15', 'Close_5_to_MA15', 'Close_6_to_MA15', 'Close_7_to_MA15', 'Close_8_to_MA15', 'Close_9_to_MA15', 'Close_10_to_MA15', 'Close_11_to_MA15', 'Close_12_to_MA15', 'Close_13_to_MA15', 'Close_14_to_MA15', 'Close_15_to_MA15', 'RSI9_up_70_perman', 'RSI9_dw_30_perman', 'RSI14_up_70_perman', 'RSI14_dw_30_perman', 'RSI14_dw_20_perman', 'RSI20_up_70_perman', 'RSI20_dw_30_perman', 'RSI27_up_70_perman', 'RSI27_dw_30_perman', 'RSI9', 'RSI14', 'RSI20', 'RSI27', 'level_close_act_w', 'step_to_fiba', 'MACDHist_corr_shift0', 'MACDHist_corr_shift1', 'MACDHist_corr_shift3', 'MACDHist_corr_shift6', 'AweOs_cor_shift0', 'AweOs_cor_shift1', 'AweOs_cor_shift3', 'AweOs_cor_shift6', 'MACDHist_corr_0_to_1', 'MACDHist_corr_1_to_3', 'MACDHist_corr_3_to_6', 'MACDHist_0_to_1', 'MACDHist_1_to_3', 'MACDHist_3_to_6', 'AweOs_1_to_3', 'AweOs_3_to_6', 'AweOs_corr_0_to_1', 'AweOs_corr_1_to_3', 'AweOs_corr_3_to_6', 'Close_coef_nak2', 'SV_DIR_shift3', 'SV_DIR_shift4', 'SV_DIR_shift5', 'SV_DIR_shift8', 'PER_OPEN_shift0', 'PER_OPEN_shift1', 'PER_OPEN_shift2', 'PER_OPEN_shift3', 'PER_OPEN_shift4', 'PER_OPEN_shift5', 'PER_OPEN_shift6', 'PER_OPEN_shift7', 'PER_OPEN_shift8', 'PER_CLOSE_shift0', 'PER_CLOSE_shift1', 'PER_CLOSE_shift2', 'PER_CLOSE_shift3', 'PER_CLOSE_shift4', 'PER_CLOSE_shift5', 'type_molot_shift1', 'type_molot_shift2', 'type_molot_shift3', 'type_molot_shift4', 'type_molot_shift5', 'POLNOTA_shift0', 'POLNOTA_shift1', 'POLNOTA_shift2', 'POLNOTA_shift3', 'POLNOTA_shift4', 'POLNOTA_shift7', 'POLNOTA_shift8', 'POLNOTA_shift9', 'POLNOTA_shift10', 'POLNOTA_shift11', 'Close_1_to_b', 'Close_2_to_b', 'Close_3_to_b', 'Close_4_to_b', 'Close_5_to_b', 'Open_0_to_b', 'Open_1_to_b', 'Open_2_to_b', 'Open_3_to_b', 'Open_4_to_b', 'Open_5_to_b', 'Low_0_to_b', 'Low_1_to_b', 'Low_2_to_b', 'Low_3_to_b', 'Low_4_to_b', 'Low_5_to_b', 'High_0_to_b', 'High_1_to_b', 'High_2_to_b', 'High_3_to_b', 'High_4_to_b', 'High_5_to_b', 'EVENT22', 'EVENT21', 'EVENT19', 'EVENT18', 'EVENT17', 'EVENT16', 'EVENT15', 'EVENT14', 'EVENT13', 'EVENT12', 'EVENT11', 'EVENT10', 'EVENT9', 'EVENT8', 'EVENT7', 'EVENT6', 'EVENT4', 'EVENT3', 'EVENT1', 'down_near', 'up_near', 'mae_opt_near', 'down_far', 'up_far', 'mae_opt_far', 'freq_up_all_300', 'freq_dw_all_300', 'freq_up_ch_300', 'freq_dw_ch_300', 'freq_up_all_100', 'freq_dw_all_100', 'freq_up_ch_100', 'freq_dw_ch_100', 'freq_up_all_50', 'freq_dw_all_50', 'freq_dw_ch_50', 'plotnost_300_all', 'plotnost_300_ch', 'plotnost_100_all', 'plotnost_100_ch', 'plotnost_50_all', 'plotnost_50_ch', 'balance_300_ch', 'balance_100_all', 'balance_100_ch', 'balance_50_all', 'balance_50_ch']


# #версия 27.08
# MODEL_PARAMS_DW_1H = {

# #     'boosting_type':'gbdt',
# #      'num_leaves': 31, 
# #      'max_depth': 9, 
# #      'learning_rate': 0.05,
# #      'n_estimators': 300,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7, 
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
#       'reg_lambda': 125,
# #      'random_state': 42, 
#     'scale_pos_weight': 1,
#       'n_jobs': 10
# }



# #версия 27.08
# MODEL_PARAMS_UP_1H = {

#      'boosting_type':'gbdt',
# #      'num_leaves': 50, 
# #      'max_depth': 9, 
# #      'learning_rate': 0.1,
# #      'n_estimators': 100,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7, 
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
#       'reg_lambda': 75,
# #      'random_state': 42, 
#     'scale_pos_weight': 1,
#       'n_jobs': 10
# }








####################       1H      ВЕРСИЯ 29.09


# #версия 27.08
# col_fin_up_1h=['Open_4_to_b', 'EMA50_REL_shift12', 'MA200_REL_shift1', 'EMA50_REL', 'MA_gor_1_REL_cross_all', 'PER_CLOSE_shift4', 'MA25_REL_shift1', 'MA5_REL_shift24', 'freq_dw_ch_300', 'EMA14_REL_shift6', 'POLNOTA_shift0', 'PER_OPEN_shift3', 'EVENT20', 'std_20_rel', 'Close_1_to_b', 'Close_8_to_MA15', 'Close_7_to_MA15', 'EMA200_REL_shift12', 'MA10_REL_shift1', 'balance_300_ch', 'Close_3_to_b', 'Volume_coef_nak', 'MACDHist_REL', 'EMA32_REL_shift6', 'EMA12_REL_shift1_cross', 'EVENT4', 'EMA75_REL_shift6', 'EMA75_REL_shift12', 'Close_coef_nak_div_Volume_coef_nak', 'EMA38_REL_shift1_cross', 'date_key_h', 'EVENT22', 'Close_coef_nak2', 'MA150_REL_shift1', 'Close_14_to_MA15', 'EMA38_REL_shift1', 'freq_dw_ch_100', 'MACDHist_0_to_1', 'MA50_REL_shift6_cross', 'MA20_REL_shift6_cross', 'Close_4_to_MA15', 'MA100_REL', 'Open_2_to_b', 'EMA38_REL', 'EMA12_REL_shift6', 'Close_7_to_8', 'up_far']


# #версия 27.08
# col_fin_dw_1h=['MA50_REL_shift12', 'Open_5_to_b', 'ROC200', 'MA200_REL', 'EMA44_REL_shift24', 'Close_m3_6_to_MA15', 'std_20_rel', 'SV_DIR_shift3', 'RSI14_dw_30_perman', 'plotnost_50_all', 'PER_OPEN_shift4', 'EMA200_REL_shift24', 'Close_2_to_b', 'Close_0_to_1', 'EMA38_REL_shift12', 'EMA26_REL_shift24', 'balance_100_ch', 'SV_DIR_shift5', 'MACDHist_REL_shift7', 'SV_DIR_shift0', 'date_key_h', 'AweOs_cor_shift0', 'EMA100_REL', 'EMA150_REL_shift12_cross', 'EVENT5', 'Close_4_to_MA15', 'EMA20_REL_shift24', 'MA50_REL', 'High_4_to_b', 'EMA50_REL_shift6_cross', 'EMA8_REL_shift12_cross', 'EMA8_REL_shift6_cross', 'MA5_REL_shift1_cross', 'MA50_REL_shift1_cross', 'EMA38_REL_shift24', 'Low_0_to_b', 'EMA26_REL_shift12', 'MA200_REL_shift6', 'TSI', 'EMA14_REL', 'EMA38_REL_shift6_cross', 'RSI9', 'AweOs_1_to_3', 'EMA14_REL_shift12', 'EMA50_REL_shift6', 'RSI27_up_70_perman', 'EMA14_REL_shift1', 'Close_coef_nak_div_MACDHist_nak', 'POLNOTA_shift3', 'type_molot_shift0', 'High_0_to_b', 'EMA38_REL', 'RSI27_dw_20', 'EMA50_REL', 'EMA50_REL_shift1_cross', 'POLNOTA_shift10', 'EVENT9', 'SV_DIR_shift6', 'MA15_REL_shift1', 'Close_0_to_MA15', 'EMA12_REL', 'EVENT7', 'EMA32_REL_shift6', 'MA5_REL_shift12', 'EMA60_REL_shift1_cross', 'SV_DIR_shift7', 'RSI27_up_80', 'MA75_REL_shift1', 'AweOs_0_to_1', 'Low_2_to_b', 'MACDHist_corr', 'EMA60_REL_shift1', 'EMA50_REL_shift12', 'EMA14_coef_nak', 'AweOs_corr_1_to_3', 'EMA75_REL_shift1', 'EMA200_REL_shift1', 'MA_gor_1_REL_cross_all', 'Close_3_to_4', 'MA75_REL_shift1_cross', 'MA_gor_12_REL_cross_all', 'EMA200_REL_shift6_cross', 'EMA14_REL_shift6', 'MA20_REL_shift12', 'Close_8_to_MA15', 'type_molot_shift5', 'EMA32_REL_shift12_cross', 'EMA_gor_12_REL_cross_all', 'PER_CLOSE_shift2', 'EMA150_REL_shift24', 'EMA150_REL_shift6', 'MA75_REL_shift6', 'High_1_to_b', 'Close_5_to_6', 'EMA12_REL_shift1_cross', 'balance_300_all', 'Close_m3_12_to_MA15', 'EVENT21', 'EMA20_REL_shift1', 'MA150_REL_shift1', 'Close_m3_3_to_MA15', 'freq_dw_ch_100', 'MA50_REL_shift6_cross', 'EMA26_REL_shift6', 'EMA8_REL', 'type_molot_shift2', 'MA50_REL_shift6']


# #версия 27.08
# MODEL_PARAMS_DW_1H = {

# #     'boosting_type':'gbdt',
# #      'num_leaves': 31, 
# #      'max_depth': 9, 
# #      'learning_rate': 0.05,
# #      'n_estimators': 300,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7, 
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
#       'reg_lambda': 0,
# #      'random_state': 42, 
#     'scale_pos_weight': 1,
#       'n_jobs': 10
# }



# #версия 27.08
# MODEL_PARAMS_UP_1H = {

#      'boosting_type':'gbdt',
# #      'num_leaves': 50, 
# #      'max_depth': 9, 
# #      'learning_rate': 0.1,
# #      'n_estimators': 100,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7, 
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
#       'reg_lambda': 150,
# #      'random_state': 42, 
#     'scale_pos_weight': 1,
#       'n_jobs': 10
# }





####################       1H      ВЕРСИЯ 09.11 - версия для 1 %

#### параметры торговли  6 0.05 0.0 0.02 0.1 3 10 0 баланс_ 1096961.0   
#6 0.05 0.0 0.02 0.1 3 10 0 баланс_ 1096961.0 ||| 394 5 1432 1102 _торг_мод_стоп_ 78.8 1.3 -0.31 стоп 516 122 516 || 0.004 -0.01

# #версия 27.08
# col_fin_up_1h=['POLNOTA_shift2', 'EMA20_REL_shift6_cross', 'EMA8_REL_shift6_cross', 'MA10_REL_shift12', 'AweOs_0_to_1', 'MA5_REL_shift12_cross', 'EVENT19', 'MACDHist_REL_shift0', 'EMA75_REL_shift1', 'MA10_REL_shift6', 'SV_DIR_shift3', 'type_molot_shift7', 'std_20_coef_nak', 'EMA38_REL_shift12_cross', 'MA100_REL_shift12', 'MA15_REL_shift6', 'Low_3_to_b', 'Volume_coef_nak', 'EMA50_REL_shift6_cross', 'Close_13_to_MA15', 'MA20_REL_shift1', 'MA100_REL_shift6', 'level_close_act_w', 'PER_OPEN_shift2', 'EMA32_REL_shift24', 'MA25_REL', 'EMA75_REL_shift12_cross', 'MA100_REL_shift1_cross', 'EVENT14', 'MA75_REL_shift6_cross', 'EMA20_REL_shift1', 'Close_coef_nak', 'EMA50_REL', 'EMA_gor_1_REL_cross_all', 'MACDHist_nak', 'PER_OPEN_shift7', 'Low_1_to_b', 'EMA8_REL', 'EVENT13', 'Close_10_to_11', 'Close_coef_nak_div_RSI14_coef_nak', 'Close_5_to_MA15', 'date_key_h', 'EMA14_REL_shift12_cross', 'PER_OPEN_shift8', 'EMA20_REL_shift12', 'EMA14_coef_nak', 'High_5_to_b', 'EMA12_REL_shift1', 'AweOs_corr_1_to_3', 'EMA44_REL', 'PER_OPEN_shift6', 'PER_CLOSE_shift1', 'High_2_to_b', 'High_0_to_b', 'MA200_REL_shift1_cross', 'Close_3_to_b', 'EMA100_REL_shift1', 'freq_dw_ch_50', 'EMA150_REL_shift6', 'EMA50_REL_shift24', 'MA75_REL_shift6', 'MA10_REL_shift1_cross', 'MA_gor_6_REL_cross_all', 'EVENT22', 'Close_2_to_b', 'EMA50_REL_shift1', 'MA15_REL_shift12', 'PER_CLOSE_shift3']


# #версия 27.08
# col_fin_dw_1h=['Close_0_to_12', 'MACDHist_corr_shift3', 'MA10_REL_shift12', 'AweOs_0_to_1', 'Close_4_to_b', 'MA5_REL_shift12_cross', 'EMA32_REL_shift6', 'EMA26_REL_shift24', 'AweOs_cor_shift6', 'freq_dw_ch_300', 'MA100_REL_shift12', 'SV_DIR_shift2', 'Low_0_to_b', 'MA25_REL', 'Close_m3_1_to_MA15', 'MACDHist_nak', 'Close_10_to_11', 'Close_0_to_1', 'EMA12_REL', 'Close_2_to_MA15', 'balance_50_all', 'EMA75_REL_shift6', 'MACDHist_corr_0_to_1', 'EMA200_REL_shift24', 'std_100_rel', 'PER_OPEN_shift0', 'RSI14_up_80', 'EMA150_REL_shift6', 'down_far', 'PER_OPEN_shift4', 'balance_100_all', 'EMA14_REL_shift1', 'EMA20_REL_shift6', 'MA5_REL', 'EMA20_REL_shift1_cross', 'RSI14', 'Close_m3_0_to_MA15', 'MA15_REL_shift6', 'MA100_coef_nak', 'EMA26_REL_shift12_cross', 'EMA8_REL_shift1', 'MA10_REL_shift1', 'Close_1_to_2', 'MA_gor_24_REL_cross_all', 'EVENT14', 'level_close_old_w', 'RSI14_dw_30_perman', 'EMA50_REL', 'EMA8_REL_shift1_cross', 'MA200_REL_shift6', 'Close_m3_3_to_MA15', 'MACDHist_REL', 'type_molot_shift3', 'Close_3_to_b', 'Close_m3_9_to_MA15', 'Close_11_to_MA15', 'EVENT20', 'freq_dw_ch_100', 'POLNOTA_shift9', 'Close_9_to_10', 'MA15_REL_shift1', 'RSI27_dw_30', 'PER_CLOSE_shift3', 'EMA14_REL', 'RSI27_up_70', 'EMA100_REL_shift6', 'Close_3_to_MA15', 'down_near', 'MA5_REL_shift24', 'EMA60_REL_shift1', 'EMA200_REL_shift6', 'EMA26_REL_shift6', 'Low_3_to_b', 'Close_0_to_3', 'Volume_coef_nak', 'EMA100_REL_shift12_cross', 'PER_OPEN_shift1', 'EMA100_REL_shift1_cross', 'PER_OPEN_shift5', 'EMA8_REL_shift12', 'MA75_REL_shift12', 'EMA_gor_1_REL_cross_all', 'MA200_REL_shift1', 'EMA150_REL_shift1', 'PER_OPEN_shift8', 'AweOs_cor_shift3', 'MA25_REL_shift6_cross', 'EMA200_REL_shift1', 'MA_gor_6_REL_cross_all', 'Close_0_to_5', 'Close_11_to_12', 'MA5_REL_shift6', 'EMA14_REL_shift24', 'MA75_REL_shift1', 'step_to_fiba', 'std_20_coef_nak', 'MACDHist_REL_shift1', 'AweOs_3_to_6', 'AweOs_1_to_3', 'freq_up_all_300', 'EMA75_REL_shift1_cross', 'Close_0_to_4', 'RSI9_up_80', 'PER_CLOSE_shift5', 'plotnost_50_ch', 'Close_7_to_MA15', 'POLNOTA_shift11', 'mae_opt_near', 'Close_14_to_MA15', 'RSI14_dw_20_perman', 'EMA44_REL_shift6_cross', 'EMA12_REL_shift12_cross', 'EMA14_REL_shift6_cross', 'MA75_REL', 'EMA150_REL', 'Low_1_to_b', 'AweOs_cor', 'EMA8_REL', 'EMA12_REL_shift6_cross', 'date_key_h', 'RSI9_up_70_perman', 'EVENT11', 'EMA44_REL_shift1', 'EMA150_REL_shift12_cross', 'Close_coef_nak_div_Volume_coef_nak', 'MA200_REL_shift12', 'EMA14_REL_shift12', 'type_molot_shift1', 'EMA100_REL_shift1', 'freq_dw_ch_50', 'freq_up_ch_50', 'PER_CLOSE_shift4', 'EVENT15', 'MA15_REL_shift12', 'EMA60_REL_shift24']


# #версия 27.08
# MODEL_PARAMS_DW_1H = {

# #     'boosting_type':'gbdt',
# #      'num_leaves': 31, 
# #      'max_depth': 9, 
# #      'learning_rate': 0.05,
# #      'n_estimators': 300,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7, 
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
#       'reg_lambda': 0,
# #      'random_state': 42, 
#     'scale_pos_weight': 1,
#       'n_jobs': 10
# }



# #версия 27.08
# MODEL_PARAMS_UP_1H = {

#      'boosting_type':'gbdt',
# #      'num_leaves': 50, 
#       'max_depth': 4, 
#       'learning_rate': 0.05,
# #      'n_estimators': 100,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7, 
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
# #      'reg_lambda': 150,
# #      'random_state': 42, 
#     'scale_pos_weight': 1,
#       'n_jobs': 10
# }





#
# # ####################       1H      ВЕРСИЯ 09.11 - версия для 1,5 %
#
# # #### параметры торговли  6 0.05 0.0 0.02 0.1 3 10 0 баланс_ 1096961.0
# # #4 0.04 0.0 0.015 0.1 3 10 0 баланс_ 673769.0 ||| 651 6 1274 948 _торг_мод_стоп_ 108.5 1.34 -0.44 стоп 737 100 737 || 0.003 -0.012
#
# #версия 27.08
# col_fin_up_1h=['MA10_REL_shift6_cross', 'SV_DIR_shift3', 'MA5_REL_shift12_cross', 'ROC200', 'MACDHist_1_to_3', 'MA100_REL_shift12', 'SV_DIR_shift2', 'PER_OPEN_shift2', 'MA25_REL', 'Close_m3_1_to_MA15', 'freq_up_ch_100', 'MA_gor_1_REL_cross_all', 'Close_0_to_1', 'EMA12_REL', 'Close_2_to_MA15', 'Close_0_to_b', 'RSI9_dw_30', 'MA200_REL_shift1_cross', 'Open_2_to_b', 'PER_OPEN_shift4', 'MACDHist_REL_shift7', 'balance_100_all', 'MA50_REL_shift1', 'RSI14_up_70', 'EMA200_REL_shift12', 'POLNOTA_shift2', 'EMA20_REL_shift6', 'MA5_REL', 'POLNOTA_shift1', 'High_3_to_b', 'SV_DIR_shift6', 'type_molot_shift7', 'EMA38_REL_shift12_cross', 'Close_10_to_MA15', 'MA20_REL', 'MA10_REL_shift1', 'EVENT1', 'MA5_REL_shift1', 'EMA60_REL', 'level_close_old_w', 'RSI27', 'EMA8_REL_shift1_cross', 'EVENT16', 'PER_CLOSE_shift0', 'Close_m3_2_to_MA15', 'MA25_REL_shift6', 'EMA_gor_6_REL_cross_all', 'EMA44_REL_shift1_cross', 'High_5_to_b', 'Close_3_to_b', 'Close_5_to_6', 'POLNOTA_shift3', 'Close_m3_9_to_MA15', 'EMA12_REL_shift6', 'EMA14_REL_shift6', 'RSI14_coef_nak', 'down_near', 'RSI20_dw_30', 'Close_0_to_6', 'MA5_REL_shift24', 'EMA60_REL_shift1', 'EMA200_REL_shift6', 'Close_coef_nak_div_MACDHist_nak', 'Close_m3_6_to_MA15', 'mae_opt_far', 'Volume_coef_nak', 'Close_0_to_3', 'EMA100_REL_shift1_cross', 'Close_12_to_MA15', 'EMA8_REL_shift12', 'MA150_REL_shift1_cross', 'EMA_gor_1_REL_cross_all', 'EMA44_REL_shift6', 'MACDHist_REL_shift10', 'PER_OPEN_shift8', 'up_near', 'SV_DIR_shift0', 'EMA38_REL_shift1', 'RSI20_up_80', 'EMA8_REL_shift12_cross', 'EVENT9', 'Close_0_to_5', 'AweOs_cor_shift1', 'EMA38_REL_shift1_cross', 'RSI20_up_70_perman', 'MA5_REL_shift6', 'EVENT17', 'SV_DIR_shift7', 'Close_6_to_MA15', 'Close_13_to_MA15', 'Close_7_to_MA15', 'POLNOTA_shift11', 'mae_opt_near', 'Close_2_to_3', 'EMA150_REL', 'Close_5_to_MA15', 'date_key_h', 'MACDHist_corr', 'EMA44_REL_shift1', 'EMA44_REL_shift24', 'MA150_REL_shift1', 'freq_up_ch_50', 'EMA100_REL_shift1', 'MA20_REL_shift6', 'type_molot_shift2', 'MA10_REL', 'Open_4_to_b', 'MA25_REL_shift1']
#
#
# #версия 27.08
# col_fin_dw_1h=['RSI20_dw_30_perman', 'MA10_REL_shift12', 'AweOs_0_to_1', 'plotnost_300_all', 'SV_DIR_shift2', 'EMA8_REL_shift24', 'PER_OPEN_shift2', 'High_4_to_b', 'MA75_REL_shift6_cross', 'MACDHist_REL_shift3', 'EVENT12', 'EVENT13', 'Close_coef_nak_div_RSI14_coef_nak', 'EMA20_REL_shift12', 'RSI9_dw_30', 'MACDHist_corr_0_to_1', 'EMA200_REL_shift24', 'std_100_rel', 'PER_CLOSE_shift1', 'EMA150_REL_shift6', 'balance_300_all', 'MA5_REL', 'EMA60_REL_shift1_cross', 'EMA26_REL_shift1', 'MA50_REL', 'type_molot_shift7', 'EMA38_REL_shift12_cross', 'PER_CLOSE_shift2', 'POLNOTA_shift10', 'MA100_coef_nak', 'EMA60_REL_shift6_cross', 'Close_10_to_MA15', 'EMA26_REL_shift12_cross', 'MA20_REL', 'balance_100_ch', 'freq_dw_all_50', 'EMA60_REL', 'EMA32_REL_shift24', 'MA100_REL_shift1_cross', 'Open_3_to_b', 'Close_m3_2_to_MA15', 'EMA14_coef_nak', 'AweOs_corr_1_to_3', 'type_molot_shift3', 'MA25_REL_shift12', 'Close_5_to_6', 'MA100_REL_shift6_cross', 'freq_up_ch_300', 'POLNOTA_shift9', 'POLNOTA_shift8', 'EMA_gor_24_REL_cross_all', 'down_near', 'Close_1_to_b', 'Close_0_to_6', 'Close_6_to_7', 'EMA12_REL_shift12', 'EMA26_REL_shift6_cross', 'Volume_coef_nak', 'Close_12_to_MA15', 'EMA200_REL_shift12_cross', 'EMA_gor_1_REL_cross_all', 'EVENT3', 'RSI20_dw_20', 'EMA44_REL', 'EMA32_REL_shift6_cross', 'EMA14_REL_shift1_cross', 'RSI20_up_80', 'RSI9_dw_20', 'RSI20_up_70_perman', 'EMA14_REL_shift24', 'PER_OPEN_shift3', 'Open_0_to_b', 'std_20_coef_nak', 'MA150_REL', 'PER_CLOSE_shift5', 'MA15_REL', 'RSI27_up_80', 'std_20_rel', 'MA100_REL_shift1', 'Close_14_to_MA15', 'EMA12_REL_shift12_cross', 'EMA150_REL', 'RSI27_dw_20', 'EMA32_REL_shift12_cross', 'date_key_h', 'SV_DIR_shift8', 'EMA44_REL_shift24', 'EMA50_REL_shift24', 'EMA100_REL_shift1', 'EMA200_REL', 'Open_4_to_b', 'Close_coef_nak2']
#
#
# #версия 27.08
# MODEL_PARAMS_DW_1H = {
#
# #     'boosting_type':'gbdt',
# #      'num_leaves': 31,
#       'max_depth': 5,
# #      'learning_rate': 0.05,
# #      'n_estimators': 300,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7,
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
#       'reg_lambda': 150,
# #      'random_state': 42,
#     'scale_pos_weight': 1,
#       'n_jobs': 10
# }
#
#
#
# #версия 27.08
# MODEL_PARAMS_UP_1H = {
#
#      'boosting_type':'gbdt',
# #      'num_leaves': 50,
#       'max_depth': 5,
# #      'learning_rate': 0.05,
# #      'n_estimators': 100,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7,
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
#       'reg_lambda': 100,
# #      'random_state': 42,
#     'scale_pos_weight': 1,
#       'n_jobs': 10
# }


# ####################       1H      ВЕРСИЯ 03.12.22 - версия для 1,5 %

# #### параметры торговли  6 0.05 0.0 0.02 0.1 3 10 0 баланс_ 1096961.0
# #4 0.04 0.0 0.015 0.1 3 10 0 баланс_ 673769.0 ||| 651 6 1274 948 _торг_мод_стоп_ 108.5 1.34 -0.44 стоп 737 100 737 || 0.003 -0.012

# #версия 03.01.22
# col_fin_up_1h=['High_1_to_b', 'High_2_to_b', 'Close_4_to_b', 'EVENT9', 'EMA20_REL_shift24', 'down_near',
#                'freq_dw_ch_300', 'freq_dw_ch_50', 'MACDHist_corr_shift0', 'Open_0_to_b', 'PER_OPEN_shift3',
#                'EMA50_REL_shift24', 'Close_11_to_12', 'POLNOTA_shift3', 'EMA150_REL', 'MA15_REL_shift6',
#                'RSI20_dw_30_perman', 'Close_0_to_MA15', 'date_key_h', 'High_0_to_b', 'RSI27_dw_30',
#                'EMA14_REL_shift1', 'EVENT21', 'Close_m3_5_to_MA15', 'EMA38_REL', 'MA15_REL',
#                'EMA32_REL_shift1_cross', 'PER_OPEN_shift7', 'Close_m3_3_to_MA15', 'EMA44_REL_shift24',
#                'EMA75_REL', 'mae_opt_near', 'MA150_REL_shift6_cross', 'EMA50_REL_shift1', 'Open_4_to_b',
#                'EMA8_REL_shift6', 'Close_m3_6_to_MA15', 'MA15_REL_shift12', 'EMA44_REL_shift6', 'RSI20_dw_20',
#                'Close_2_to_MA15', 'MA50_REL', 'PER_OPEN_shift1', 'RSI14_up_80', 'Close_0_to_5',
#                'type_molot_shift1', 'balance_100_all', 'EMA44_REL_shift1_cross', 'EMA44_REL_shift6_cross',
#                'Close_7_to_8', 'Close_3_to_b', 'MA200_REL_shift6_cross', 'EMA8_REL_shift6_cross',
#                'AweOs_cor_shift3', 'EMA_gor_6_REL_cross_all', 'EMA12_REL_shift12_cross', 'EMA75_REL_shift24',
#                'std_20_coef_nak', 'Close_9_to_10', 'EMA150_REL_shift6_cross', 'MA_gor_6_REL_cross_all',
#                'Close_3_to_4', 'MA50_REL_shift1_cross', 'PER_CLOSE_shift1', 'Volume_coef_nak', 'POLNOTA_shift10',
#                'RSI27_up_70_perman', 'EMA44_REL_shift12', 'POLNOTA_shift8', 'EMA38_REL_shift12',
#                'MACDHist_REL_shift1', 'EMA12_REL', 'MA25_REL_shift12', 'MA20_REL_shift6_cross',
#                'MA150_REL_shift1_cross', 'EVENT14', 'RSI27_dw_20', 'MA100_REL_shift1_cross',
#                'MACDHist_corr_shift3', 'Close_0_to_12', 'Close_5_to_MA15', 'MA100_REL_shift6',
#                'EMA75_REL_shift6', 'POLNOTA_shift9', 'EMA26_REL_shift6', 'PER_CLOSE_shift0',
#                'AweOs_corr_3_to_6', 'EMA20_REL_shift1', 'EMA38_REL_shift1', 'MA_gor_24_REL_cross_all',
#                'POLNOTA_shift11', 'Open_3_to_b', 'MA75_REL_shift6_cross', 'up_near']


# #версия 03.01.22
# col_fin_dw_1h=['EVENT18', 'Close_14_to_MA15', 'type_molot_shift4', 'RSI27_dw_30',\
#               'EVENT21', 'EMA200_REL_shift6', 'High_2_to_b', 'EMA12_REL_shift1_cross',\
#               'EVENT2', 'SV_DIR_shift8', 'AweOs_cor_shift3', 'EMA20_REL', 'SV_DIR_shift1',\
#               'EMA60_REL', 'MA50_REL_shift6', 'EVENT20', 'PER_CLOSE_shift5', 'EMA32_REL',\
#               'Close_2_to_3', 'EVENT3', 'plotnost_50_ch', 'RSI20_up_70', 'freq_up_ch_50',\
#               'MA20_REL_shift1', 'EMA44_REL_shift24', 'Close_coef_nak2', 'EMA150_REL_shift1',\
#               'plotnost_100_all', 'ROC200', 'PER_CLOSE_shift1', 'mae_opt_near', 'Close_9_to_MA15',\
#               'EMA200_REL_shift1', 'RSI9_up_70', 'Close_1_to_MA15', 'EMA44_REL_shift12', 'Open_4_to_b',\
#               'RSI14_dw_20_perman', 'mae_opt_far', 'EMA38_REL_shift1', 'EMA38_REL_shift12',\
#               'EMA50_REL_shift24', 'EMA20_REL_shift6_cross', 'RSI20', 'EMA50_REL_shift1_cross',\
#               'EMA32_REL_shift12', 'RSI9_up_70_perman', 'Close_2_to_MA15', 'MA10_REL_shift1',\
#               'EMA20_REL_shift12', 'freq_dw_all_300', 'Close_4_to_5', 'MA200_REL_shift1_cross',\
#               'freq_up_all_50', 'EMA26_REL', 'MA15_REL_shift6', 'EVENT8', 'Close_0_to_9',\
#               'EMA200_REL_shift24', 'Close_coef_nak_div_MACDHist_nak', 'Low_1_to_b', 'MA100_REL_shift1',\
#               'MACDHist_corr_0_to_1', 'MA150_REL_shift1', 'MA25_REL_shift6', 'RSI27', 'balance_300_all',\
#               'RSI20_dw_30_perman', 'date_key_h']

# #версия 03.01.22
# MODEL_PARAMS_DW_1H = {

#      'boosting_type':'gbdt',
# #      'num_leaves': 31,
# #      'max_depth': 5,
# #      'learning_rate': 0.05,
# #      'n_estimators': 300,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7,
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
# #      'reg_lambda': 150,
# #      'random_state': 42,
#     'scale_pos_weight': 1,
#       'n_jobs': 10
# }



# #версия 27.08
# MODEL_PARAMS_UP_1H = {

#      'boosting_type':'gbdt',
# #      'num_leaves': 50,
# #      'max_depth': 5,
# #      'learning_rate': 0.05,
# #      'n_estimators': 100,
# #      'min_child_samples': 20,
# #      'subsample': 0.7,
# #      'colsample_bytree': 0.7,
# #      'min_child_weight': 5,
# #      'reg_alpha': 0,
#       'reg_lambda': 100,
# #      'random_state': 42,
#     'scale_pos_weight': 1,
#       'n_jobs': 10
# }




# # ####################       1H      ВЕРСИЯ 21.01.22 - версия для 1,5 %

# # #### параметры торговли  6 0.05 0.0 0.02 0.1 3 10 0 баланс_ 1096961.0
# # #4 0.04 0.0 0.015 0.1 3 10 0 баланс_ 673769.0 ||| 651 6 1274 948 _торг_мод_стоп_ 108.5 1.34 -0.44 стоп 737 100 737 || 0.003 -0.012

# #версия 21.01.22
# col_fin_up_1h=col_fin_full


# #версия 21.01.22
# col_fin_dw_1h=col_fin_full

# #версия 21.02.22
# MODEL_PARAMS_DW_1H ={
#     'iterations': 2500,
#   'l2_leaf_reg': 181.40323665724992,
#   'learning_rate': 0.006539595474173904,
#   'loss_function': 'Logloss',
#   'verbose': False
# }

# #версия 21.01.22
# # {

# #      'l2_leaf_reg': 125,
# #      'loss_function': 'Logloss',
# #       'learning_rate': 0.02,
# #        'verbose': False

# # }


# #версия 21.02.22
# MODEL_PARAMS_UP_1H = {
#     'iterations': 1500,
#   'l2_leaf_reg': 166.3824686893428,
#   'learning_rate': 0.021311075988877205,
#   'loss_function': 'Logloss',
#   'verbose': False}

# #версия 21.01.22
# # {

# #      'l2_leaf_reg': 100,
# #      'loss_function': 'Logloss',
# #       'learning_rate': 0.02,
# #        'verbose': False
# # }





# ####################       1H      ВЕРСИЯ 03.06.22 - версия для 1,5 %

# #### параметры торговли  6 0.05 0.0 0.02 0.1 3 10 0 баланс_ 1096961.0
# #4 0.04 0.0 0.015 0.1 3 10 0 баланс_ 673769.0 ||| 651 6 1274 948 _торг_мод_стоп_ 108.5 1.34 -0.44 стоп 737 100 737 || 0.003 -0.012

# #версия 21.01.22
# col_fin_up_1h=['EMA12_REL', 'EMA26_REL', 'Close_coef_nak_div_Volume_coef_nak', 'EMA44_REL_shift24_cross', 'Close_1_to_b', 'MA150_REL_shift6', 'RSI20_dw_30_perman', 'mae_opt_far', 'AweOs_cor', 'POLNOTA_shift11', 'RSI27_up_70', 'EVENT14', 'EMA200_REL_shift1_cross', 'MA20_REL_shift1', 'EMA12_REL_shift1', 'MA5_REL_shift1_cross', 'EMA100_REL_shift6_cross', 'Close_2_to_MA15', 'MA10_REL_shift12_cross', 'EMA60_REL_shift12', 'EMA26_REL_shift24', 'date_key_h', 'MA150_REL', 'Close_13_to_MA15', 'RSI9_dw_20', 'PER_CLOSE_shift0', 'EMA150_REL_shift6_cross', 'EMA14_REL_shift12_cross', 'EMA44_REL_shift6_cross', 'MA15_REL_shift1', 'Close_1_to_MA15', 'freq_up_all_300', 'Low_2_to_b', 'MA20_REL_shift12', 'AweOs_cor_shift1', 'MA50_REL', 'MA25_REL_shift1_cross', 'Close_5_to_MA15', 'RSI20', 'PER_OPEN_shift0', 'Close_14_to_MA15', 'Close_0_to_9', 'EMA50_REL_shift6', 'freq_dw_ch_300', 'Close_4_to_5', 'MA25_REL_shift12', 'EMA38_REL', 'RSI14_up_80', 'Open_3_to_b', 'MA10_REL', 'MA10_REL_shift6', 'EMA8_REL_shift1', 'MA25_REL_shift6', 'type_molot_shift5', 'date_key_d', 'SV_DIR_shift5', 'TSI', 'Close_0_to_4', 'EMA14_REL_shift24_cross', 'Close_2_to_3', 'Close_m3_5_to_MA15', 'MA50_REL_shift12_cross', 'EMA44_REL_shift24', 'MA150_REL_shift12', 'Close_m3_9_to_MA15', 'PER_CLOSE_shift1', 'MA100_REL_shift24', 'MA200_REL_shift1', 'type_molot_shift2', 'MA5_REL_shift6_cross', 'RSI14_up_70_perman', 'High_3_to_b', 'EVENT3', 'plotnost_50_ch', 'EMA100_REL_shift12', 'MACDHist_corr_roll_mean3_shift6', 'MA75_REL_shift6_cross', 'POLNOTA_shift4', 'MA20_REL_shift24', 'EMA32_REL_shift1_cross', 'Close_3_to_MA15', 'Close_5_to_6', 'EMA26_REL_shift24_cross', 'MA150_REL_shift1', 'freq_dw_all_100', 'MA75_REL_shift12_cross', 'Close_coef_nak_div_RSI14_coef_nak', 'RSI14_up_70', 'EMA12_REL_shift12_cross', 'MACDHist_REL_shift5', 'MA20_REL_shift1_cross', 'Close_1_to_2', 'plotnost_50_all', 'type_molot_shift4', 'EMA_gor_6_REL_cross_all', 'RSI27_up_80_perman', 'EMA50_REL', 'EMA75_REL_shift12', 'plotnost_100_ch', 'EVENT22', 'EMA150_REL_shift6', 'type_molot_shift1', 'balance_50_ch', 'EMA38_REL_shift24_cross', 'RSI14_dw_20_perman', 'type_molot_shift7', 'RSI27_dw_30_perman', 'EMA150_REL_shift24_cross', 'EMA75_REL_shift1', 'MACDHist_corr_roll_mean3_shift1', 'std_20_rel', 'Close_10_to_MA15', 'Close_4_to_MA15', 'MA100_REL_shift6_cross', 'RSI14', 'MA20_REL_shift6', 'EMA14_REL_shift6', 'MA25_REL_shift24_cross', 'MACDHist_REL_shift1', 'EMA150_REL_shift24', 'EMA8_REL_shift6_cross', 'MA25_REL_shift12_cross', 'MA100_REL_shift6', 'Close_m3_1_to_MA15', 'EMA50_REL_shift6_cross', 'MA150_REL_shift24_cross', 'MACDHist_corr', 'EMA50_REL_shift1_cross', 'High_0_to_b', 'High_1_to_b', 'RSI27', 'MA5_REL_shift12', 'MACDHist_REL_shift7']


# #версия 21.01.22
# col_fin_dw_1h=['EVENT20', 'EMA14_REL', 'EMA100_REL_shift12_cross', 'EVENT14', 'up_far', 'Low_0_to_b', 'MA75_REL_shift6_cross', 'date_key_h', 'EMA200_REL_shift1', 'EVENT12', 'RSI9_dw_30_perman', 'mae_opt_far', 'Close_3_to_4', 'MA100_REL_shift24', 'Close_0_to_5', 'AweOs_cor_roll_mean3_shift0', 'EMA26_REL_shift6', 'PER_OPEN_shift0', 'EMA20_REL_shift24', 'RSI14_up_80', 'MA20_REL_shift24', 'EMA75_REL_shift24_cross', 'MACDHist_REL_shift10', 'step_to_fiba', 'PER_CLOSE_shift0', 'TSI', 'balance_100_ch', 'RSI9_dw_20_perman', 'Close_13_to_MA15', 'RSI20_dw_20', 'MA200_REL_shift12_cross', 'Close_7_to_8', 'MACDHist_corr_shift0', 'EMA_gor_24_REL_cross_all', 'AweOs_corr_0_to_1', 'EMA44_REL_shift12', 'POLNOTA_shift11', 'EMA8_REL', 'Open_4_to_b', 'RSI14_up_70_perman', 'Volume_coef_nak', 'MACDHist_corr_shift3', 'EMA26_REL', 'mae_opt_near', 'EMA38_REL_shift6', 'EVENT1', 'Close_m3_1_to_MA15', 'EMA75_REL_shift1_cross', 'MA15_REL_shift24_cross', 'Close_0_to_MA15', 'MA5_REL_shift1', 'Close_2_to_3', 'PER_CLOSE_shift1', 'EMA150_REL_shift6', 'EVENT13', 'MA100_REL_shift12', 'MA150_REL', 'EMA12_REL_shift12', 'EMA50_REL', 'RSI27_up_80_perman', 'ROC200sm', 'freq_up_all_300', 'EMA44_REL_shift24_cross', 'EVENT11', 'EMA44_REL_shift12_cross', 'RSI27_up_70', 'MA50_REL_shift24', 'date_key_d', 'EMA20_REL_shift6', 'MACDHist_corr_1_to_3', 'MA20_REL_shift6_cross', 'Close_coef_nak2', 'EMA100_REL_shift1', 'freq_dw_ch_100', 'plotnost_50_ch', 'Close_3_to_b', 'EMA60_REL_shift12_cross', 'balance_50_all', 'EMA38_REL_shift24_cross', 'PER_OPEN_shift1', 'AweOs_0_to_1', 'MA150_REL_shift1', 'Close_6_to_7', 'PER_OPEN_shift7', 'PER_OPEN_shift8', 'EMA100_REL_shift24_cross', 'MA5_REL_shift24', 'MA20_REL_shift6', 'Close_0_to_12', 'EMA100_REL', 'MACDHist_REL', 'EMA12_REL_shift1', 'EMA100_REL_shift6', 'Close_10_to_11', 'High_0_to_b', 'EMA60_REL_shift24_cross', 'EMA60_REL_shift6', 'EMA150_REL_shift24', 'freq_up_ch_50', 'High_3_to_b', 'MACDHist_REL_shift7', 'MA25_REL_shift1_cross', 'Close_7_to_MA15', 'MACDHist_nak', 'EMA38_REL_shift1_cross']

#версия 21.02.22
# MODEL_PARAMS_DW_1H ={
#     'iterations': 2500,
#   'l2_leaf_reg': 181.40323665724992,
#   'learning_rate': 0.006539595474173904,
#   'loss_function': 'Logloss',
#   'verbose': False
# }

#версия 21.01.22
# {

#      'l2_leaf_reg': 125,
#      'loss_function': 'Logloss',
#       'learning_rate': 0.02,
#        'verbose': False

# }


#версия 21.02.22
# MODEL_PARAMS_UP_1H = {
#         'iterations': 2500,
#       'l2_leaf_reg': 30,
#       'learning_rate': 0.006539595474173904,
#       'loss_function': 'Logloss',
#       'verbose': False
#     }

#версия 21.01.22
# {

#      'l2_leaf_reg': 100,
#      'loss_function': 'Logloss',
#       'learning_rate': 0.02,
#        'verbose': False
# }




# ####################       1H      ВЕРСИЯ 08.07.22 - версия для 1,5 %

# #### параметры торговли  6 0.05 0.0 0.02 0.1 3 10 0 баланс_ 1096961.0
# #4 0.04 0.0 0.015 0.1 3 10 0 баланс_ 673769.0 ||| 651 6 1274 948 _торг_мод_стоп_ 108.5 1.34 -0.44 стоп 737 100 737 || 0.003 -0.012

#версия 21.01.22


col_fin_up_1h=['MACDHist_corr', 'AweOs_cor', 'ROC200', 'ROC200sm', 'TSI', 'EMA8_REL', 'EMA8_REL_shift24', 'EMA12_REL', 'EMA12_REL_shift24', 'EMA20_REL', 'EMA20_REL_shift24', 'EMA26_REL', 'EMA26_REL_shift12', 'EMA32_REL', 'EMA32_REL_shift6', 'EMA32_REL_shift24', 'EMA38_REL', 'EMA50_REL', 'EMA60_REL_shift24', 'EMA75_REL', 'EMA150_REL', 'EMA150_REL_shift6', 'EMA150_REL_shift12', 'EMA200_REL', 'EMA200_REL_shift1', 'EMA200_REL_shift6', 'EMA200_REL_shift12', 'EMA200_REL_shift24', 'MA5_REL_shift1', 'MA5_REL_shift6', 'MA5_REL_shift12', 'MA5_REL_shift24', 'MA10_REL_shift12', 'MA15_REL', 'MA15_REL_shift12', 'MA20_REL', 'MA25_REL', 'MA25_REL_shift12', 'MA50_REL_shift12', 'MA75_REL', 'MA75_REL_shift6', 'MA150_REL', 'MA150_REL_shift12', 'MA200_REL', 'MA200_REL_shift6', 'MACDHist_REL', 'MACDHist_REL_shift1', 'MACDHist_REL_shift3', 'MACDHist_REL_shift5', 'MACDHist_REL_shift7', 'date_key_h', 'date_key_d', 'std_20_rel', 'std_100_rel', 'RSI14_coef_nak', 'Close_coef_nak', 'Volume_coef_nak', 'EMA14_coef_nak', 'MA100_coef_nak', 'std_20_coef_nak', 'MACDHist_nak', 'Close_coef_nak_div_Volume_coef_nak', 'Close_coef_nak_div_RSI14_coef_nak', 'Close_coef_nak_div_MACDHist_nak', 'Close_0_to_1', 'Close_1_to_2', 'Close_2_to_3', 'Close_5_to_6', 'Close_7_to_8', 'Close_10_to_11', 'Close_0_to_3', 'Close_0_to_5', 'Close_0_to_6', 'Close_m3_2_to_MA15', 'Close_m3_3_to_MA15', 'Close_m3_6_to_MA15', 'Close_m3_9_to_MA15', 'Close_m3_12_to_MA15', 'Close_3_to_MA15', 'Close_4_to_MA15', 'Close_5_to_MA15', 'Close_6_to_MA15', 'Close_9_to_MA15', 'Close_10_to_MA15', 'Close_11_to_MA15', 'Close_14_to_MA15', 'RSI9', 'RSI14', 'RSI20', 'RSI27', 'level_close_old_w', 'level_close_act_w', 'step_to_fiba', 'MACDHist_corr_shift3', 'AweOs_cor_shift1', 'AweOs_cor_shift3', 'AweOs_cor_shift6', 'MACDHist_corr_0_to_1', 'MACDHist_0_to_1', 'MACDHist_1_to_3', 'MACDHist_3_to_6', 'AweOs_0_to_1', 'AweOs_1_to_3', 'AweOs_3_to_6', 'AweOs_corr_1_to_3', 'Close_coef_nak2', 'PER_OPEN_shift0', 'PER_OPEN_shift2', 'PER_OPEN_shift3', 'PER_OPEN_shift4', 'PER_OPEN_shift6', 'PER_OPEN_shift8', 'PER_CLOSE_shift0', 'PER_CLOSE_shift1', 'PER_CLOSE_shift2', 'PER_CLOSE_shift5', 'POLNOTA_shift1', 'POLNOTA_shift2', 'POLNOTA_shift3', 'POLNOTA_shift4', 'POLNOTA_shift7', 'POLNOTA_shift8', 'POLNOTA_shift9', 'POLNOTA_shift10', 'Close_2_to_b', 'Close_3_to_b', 'Open_0_to_b', 'Open_3_to_b', 'Open_5_to_b', 'Low_0_to_b', 'Low_1_to_b', 'Low_3_to_b', 'Low_4_to_b', 'High_0_to_b', 'High_1_to_b', 'High_2_to_b', 'High_3_to_b', 'High_4_to_b', 'High_5_to_b', 'down_near', 'up_near', 'mae_opt_near', 'down_far', 'up_far', 'mae_opt_far', 'freq_up_all_300', 'freq_dw_all_300', 'freq_up_ch_300', 'freq_dw_ch_300', 'freq_up_all_100', 'freq_dw_all_100', 'freq_up_ch_100', 'freq_dw_ch_100', 'freq_up_all_50', 'freq_dw_all_50', 'plotnost_300_all', 'plotnost_300_ch', 'plotnost_100_all', 'plotnost_100_ch', 'plotnost_50_all', 'plotnost_50_ch', 'balance_300_all', 'balance_300_ch', 'balance_100_all', 'balance_50_all', 'balance_50_ch', 'MA25_REL_shift24', 'MA75_REL_shift24', 'MA150_REL_shift24', 'MACDHist_corr_roll_mean3_shift1', 'MACDHist_corr_roll_mean3_shift3', 'MACDHist_corr_roll_mean3_shift6', 'AweOs_cor_roll_mean3_shift3', 'AweOs_cor_roll_mean3_shift6']


col_fin_dw_1h=['MACDHist_corr', 'AweOs_cor', 'ROC200', 'ROC200sm', 'TSI', 'EMA8_REL', 'EMA8_REL_shift1', 'EMA8_REL_shift6', 'EMA8_REL_shift12', 'EMA8_REL_shift24', 'EMA12_REL', 'EMA12_REL_shift1', 'EMA12_REL_shift6', 'EMA12_REL_shift12', 'EMA12_REL_shift24', 'EMA14_REL', 'EMA14_REL_shift12', 'EMA14_REL_shift24', 'EMA20_REL', 'EMA20_REL_shift6', 'EMA20_REL_shift12', 'EMA20_REL_shift24', 'EMA26_REL', 'EMA26_REL_shift1', 'EMA26_REL_shift6', 'EMA26_REL_shift6_cross', 'EMA26_REL_shift12', 'EMA26_REL_shift24', 'EMA32_REL', 'EMA32_REL_shift1', 'EMA32_REL_shift6', 'EMA32_REL_shift6_cross', 'EMA32_REL_shift12', 'EMA32_REL_shift24', 'EMA38_REL_shift1', 'EMA38_REL_shift6', 'EMA38_REL_shift24', 'EMA44_REL', 'EMA44_REL_shift1', 'EMA44_REL_shift6', 'EMA44_REL_shift24', 'EMA50_REL', 'EMA50_REL_shift1', 'EMA50_REL_shift6', 'EMA50_REL_shift12', 'EMA50_REL_shift24', 'EMA60_REL', 'EMA60_REL_shift6', 'EMA60_REL_shift12', 'EMA60_REL_shift24', 'EMA75_REL', 'EMA75_REL_shift1', 'EMA75_REL_shift6_cross', 'EMA75_REL_shift12', 'EMA75_REL_shift24', 'EMA100_REL', 'EMA100_REL_shift1', 'EMA100_REL_shift1_cross', 'EMA100_REL_shift6', 'EMA100_REL_shift6_cross', 'EMA100_REL_shift12', 'EMA100_REL_shift12_cross', 'EMA100_REL_shift24', 'EMA150_REL', 'EMA150_REL_shift1', 'EMA150_REL_shift6', 'EMA150_REL_shift6_cross', 'EMA150_REL_shift12', 'EMA150_REL_shift24', 'EMA200_REL', 'EMA200_REL_shift1', 'EMA200_REL_shift6', 'EMA200_REL_shift12', 'EMA200_REL_shift24', 'MA5_REL', 'MA5_REL_shift1', 'MA5_REL_shift6', 'MA5_REL_shift12', 'MA5_REL_shift24', 'MA5_REL_shift24_cross', 'MA10_REL', 'MA10_REL_shift1', 'MA10_REL_shift6', 'MA10_REL_shift12', 'MA15_REL', 'MA15_REL_shift1', 'MA15_REL_shift6', 'MA15_REL_shift12', 'MA20_REL', 'MA20_REL_shift1', 'MA20_REL_shift6', 'MA20_REL_shift12', 'MA25_REL', 'MA25_REL_shift1', 'MA25_REL_shift6', 'MA25_REL_shift12', 'MA50_REL', 'MA50_REL_shift1', 'MA50_REL_shift6', 'MA50_REL_shift12', 'MA75_REL', 'MA75_REL_shift1', 'MA75_REL_shift6', 'MA75_REL_shift12', 'MA100_REL', 'MA100_REL_shift6', 'MA100_REL_shift12', 'MA150_REL', 'MA150_REL_shift1', 'MA150_REL_shift6', 'MA150_REL_shift12', 'MA200_REL', 'MA200_REL_shift1', 'MA200_REL_shift6', 'MA200_REL_shift12', 'MACDHist_REL_shift1', 'MACDHist_REL_shift3', 'MACDHist_REL_shift5', 'MACDHist_REL_shift7', 'MACDHist_REL_shift10', 'EMA_gor_1_REL_cross_all', 'EMA_gor_6_REL_cross_all', 'EMA_gor_12_REL_cross_all', 'EMA_gor_24_REL_cross_all', 'MA_gor_1_REL_cross_all', 'MA_gor_6_REL_cross_all', 'MA_gor_12_REL_cross_all', 'MA_gor_24_REL_cross_all', 'date_key_h', 'date_key_d', 'std_20_rel', 'std_100_rel', 'RSI14_coef_nak', 'Close_coef_nak', 'Volume_coef_nak', 'EMA14_coef_nak', 'MA100_coef_nak', 'std_20_coef_nak', 'MACDHist_nak', 'Close_coef_nak_div_Volume_coef_nak', 'Close_coef_nak_div_RSI14_coef_nak', 'Close_coef_nak_div_MACDHist_nak', 'Close_0_to_1', 'Close_1_to_2', 'Close_2_to_3', 'Close_3_to_4', 'Close_4_to_5', 'Close_5_to_6', 'Close_6_to_7', 'Close_7_to_8', 'Close_8_to_9', 'Close_9_to_10', 'Close_10_to_11', 'Close_11_to_12', 'Close_0_to_3', 'Close_0_to_4', 'Close_0_to_5', 'Close_0_to_6', 'Close_0_to_9', 'Close_0_to_12', 'Close_m3_0_to_MA15', 'Close_m3_1_to_MA15', 'Close_m3_2_to_MA15', 'Close_m3_3_to_MA15', 'Close_m3_4_to_MA15', 'Close_m3_5_to_MA15', 'Close_m3_6_to_MA15', 'Close_m3_9_to_MA15', 'Close_m3_12_to_MA15', 'Close_0_to_MA15', 'Close_2_to_MA15', 'Close_3_to_MA15', 'Close_4_to_MA15', 'Close_5_to_MA15', 'Close_6_to_MA15', 'Close_7_to_MA15', 'Close_8_to_MA15', 'Close_9_to_MA15', 'Close_10_to_MA15', 'Close_11_to_MA15', 'Close_12_to_MA15', 'Close_13_to_MA15', 'Close_14_to_MA15', 'Close_15_to_MA15', 'RSI14_dw_30_perman', 'RSI14_dw_20_perman', 'RSI20_up_70_perman', 'RSI27_up_70_perman', 'RSI9', 'RSI14', 'RSI20', 'RSI27', 'level_close_old_w', 'level_close_act_w', 'step_to_fiba', 'MACDHist_corr_shift1', 'MACDHist_corr_shift3', 'MACDHist_corr_shift6', 'AweOs_cor_shift1', 'AweOs_cor_shift3', 'AweOs_cor_shift6', 'MACDHist_corr_0_to_1', 'MACDHist_corr_1_to_3', 'MACDHist_corr_3_to_6', 'MACDHist_0_to_1', 'MACDHist_1_to_3', 'MACDHist_3_to_6', 'AweOs_0_to_1', 'AweOs_1_to_3', 'AweOs_3_to_6', 'AweOs_corr_0_to_1', 'Close_coef_nak2', 'PER_OPEN_shift0', 'PER_OPEN_shift1', 'PER_OPEN_shift2', 'PER_OPEN_shift3', 'PER_OPEN_shift4', 'PER_OPEN_shift5', 'PER_OPEN_shift6', 'PER_OPEN_shift7', 'PER_OPEN_shift8', 'PER_CLOSE_shift0', 'PER_CLOSE_shift1', 'PER_CLOSE_shift2', 'PER_CLOSE_shift3', 'PER_CLOSE_shift4', 'PER_CLOSE_shift5', 'POLNOTA_shift0', 'POLNOTA_shift1', 'POLNOTA_shift2', 'POLNOTA_shift3', 'POLNOTA_shift4', 'POLNOTA_shift7', 'POLNOTA_shift8', 'POLNOTA_shift9', 'POLNOTA_shift10', 'POLNOTA_shift11', 'Close_1_to_b', 'Close_2_to_b', 'Close_3_to_b', 'Close_4_to_b', 'Close_5_to_b', 'Open_0_to_b', 'Open_1_to_b', 'Open_3_to_b', 'Open_4_to_b', 'Open_5_to_b', 'Low_0_to_b', 'Low_1_to_b', 'Low_2_to_b', 'Low_3_to_b', 'Low_4_to_b', 'Low_5_to_b', 'High_0_to_b', 'High_1_to_b', 'High_2_to_b', 'High_3_to_b', 'High_4_to_b', 'High_5_to_b', 'EVENT21', 'down_near', 'up_near', 'mae_opt_near', 'down_far', 'up_far', 'mae_opt_far', 'freq_up_all_300', 'freq_dw_all_300', 'freq_up_ch_300', 'freq_dw_ch_300', 'freq_up_all_100', 'freq_dw_all_100', 'freq_up_ch_100', 'freq_dw_ch_100', 'freq_up_all_50', 'freq_dw_all_50', 'freq_up_ch_50', 'freq_dw_ch_50', 'plotnost_300_all', 'plotnost_300_ch', 'plotnost_100_all', 'plotnost_100_ch', 'plotnost_50_all', 'plotnost_50_ch', 'balance_300_all', 'balance_300_ch', 'balance_100_all', 'balance_100_ch', 'balance_50_all', 'balance_50_ch', 'EMA8_REL_shift24_cross', 'EMA150_REL_shift24_cross', 'EMA200_REL_shift24_cross', 'MA20_REL_shift24', 'MA25_REL_shift24', 'MA25_REL_shift24_cross', 'MA50_REL_shift24', 'MA75_REL_shift24', 'MA100_REL_shift24', 'MA100_REL_shift24_cross', 'MA150_REL_shift24', 'MA200_REL_shift24', 'MA200_REL_shift24_cross', 'RSI27_up_80_perman', 'MACDHist_corr_roll_mean3', 'MACDHist_corr_roll_mean3_shift1', 'MACDHist_corr_roll_mean3_shift3', 'MACDHist_corr_roll_mean3_shift6', 'AweOs_cor_roll_mean3', 'AweOs_cor_roll_mean3_shift1', 'AweOs_cor_roll_mean3_shift3', 'AweOs_cor_roll_mean3_shift6']



#версия 08.07.22
MODEL_PARAMS_UP_1H = {
        'iterations': 3000,
      'l2_leaf_reg': 600,
      'learning_rate': 0.01,
      'loss_function': 'Logloss',
      'verbose': False
    }


MODEL_PARAMS_DW_1H ={
    'iterations': 1500,
  'l2_leaf_reg': 1100,
  'learning_rate': 0.02,
  'loss_function': 'Logloss',
  'verbose': False
}


# ####################       1H      ВЕРСИЯ 08.07.22 - версия для 1,5 %

# #### параметры торговли  6 0.05 0.0 0.02 0.1 3 10 0 баланс_ 1096961.0
# #4 0.04 0.0 0.015 0.1 3 10 0 баланс_ 673769.0 ||| 651 6 1274 948 _торг_мод_стоп_ 108.5 1.34 -0.44 стоп 737 100 737 || 0.003 -0.012

# #версия 13.09.22 МУЛТИ


# col_fin_multi_1h=['MACDHist_corr', 'AweOs_cor', 'ROC200', 'ROC200sm', 'TSI', 'EMA8_REL_shift24', 'EMA12_REL', 'EMA20_REL_shift6', 'EMA26_REL', 'EMA50_REL', 'EMA60_REL_shift6', 'EMA75_REL', 'EMA150_REL', 'EMA200_REL', 'EMA200_REL_shift6', 'EMA200_REL_shift12', 'EMA200_REL_shift24', 'MA5_REL', 'MA5_REL_shift1', 'MA5_REL_shift6', 'MA5_REL_shift12', 'MA5_REL_shift24', 'MA10_REL_shift12', 'MA20_REL_shift12', 'MA25_REL', 'MA50_REL', 'MA50_REL_shift1', 'MA50_REL_shift12', 'MA75_REL', 'MA100_REL', 'MA100_REL_shift12', 'MA150_REL', 'MA150_REL_shift1', 'MA150_REL_shift6', 'MA200_REL', 'MA200_REL_shift6', 'MA200_REL_shift12', 'MACDHist_REL', 'MACDHist_REL_shift3', 'MACDHist_REL_shift5', 'MACDHist_REL_shift7', 'MACDHist_REL_shift10', 'MA_gor_24_REL_cross_all', 'date_key_h', 'date_key_d', 'std_20_rel', 'std_100_rel', 'RSI14_coef_nak', 'Close_coef_nak', 'Volume_coef_nak', 'EMA14_coef_nak', 'MA100_coef_nak', 'std_20_coef_nak', 'MACDHist_nak', 'Close_coef_nak_div_Volume_coef_nak', 'Close_coef_nak_div_RSI14_coef_nak', 'Close_coef_nak_div_MACDHist_nak', 'Close_10_to_11', 'Close_11_to_12', 'Close_0_to_6', 'Close_m3_0_to_MA15', 'Close_m3_4_to_MA15', 'Close_m3_9_to_MA15', 'Close_3_to_MA15', 'Close_4_to_MA15', 'Close_7_to_MA15', 'Close_13_to_MA15', 'Close_14_to_MA15', 'Close_15_to_MA15', 'RSI9', 'RSI14', 'RSI20', 'RSI27', 'level_close_old_w', 'level_close_act_w', 'step_to_fiba', 'MACDHist_corr_shift6', 'AweOs_cor_shift3', 'AweOs_cor_shift6', 'MACDHist_corr_0_to_1', 'MACDHist_0_to_1', 'MACDHist_1_to_3', 'MACDHist_3_to_6', 'AweOs_1_to_3', 'AweOs_3_to_6', 'AweOs_corr_0_to_1', 'Close_coef_nak2', 'PER_OPEN_shift0', 'PER_OPEN_shift1', 'PER_OPEN_shift3', 'PER_OPEN_shift6', 'PER_OPEN_shift7', 'PER_CLOSE_shift0', 'PER_CLOSE_shift1', 'PER_CLOSE_shift2', 'PER_CLOSE_shift5', 'POLNOTA_shift0', 'POLNOTA_shift1', 'POLNOTA_shift2', 'POLNOTA_shift3', 'POLNOTA_shift4', 'POLNOTA_shift7', 'POLNOTA_shift8', 'POLNOTA_shift9', 'POLNOTA_shift10', 'Close_2_to_b', 'Low_0_to_b', 'Low_1_to_b', 'Low_3_to_b', 'Low_4_to_b', 'Low_5_to_b', 'High_0_to_b', 'High_1_to_b', 'High_2_to_b', 'High_3_to_b', 'High_4_to_b', 'down_near', 'up_near', 'mae_opt_near', 'down_far', 'mae_opt_far', 'freq_up_all_300', 'freq_dw_all_300', 'freq_up_ch_300', 'freq_dw_ch_300', 'freq_up_all_100', 'freq_dw_all_100', 'freq_dw_ch_100', 'freq_up_all_50', 'freq_dw_all_50', 'plotnost_300_all', 'plotnost_300_ch', 'plotnost_100_all', 'plotnost_100_ch', 'plotnost_50_all', 'plotnost_50_ch', 'balance_300_all', 'balance_300_ch', 'balance_100_all', 'balance_50_all', 'MA20_REL_shift24', 'MA25_REL_shift24', 'MA50_REL_shift24', 'MA150_REL_shift24', 'MA200_REL_shift24', 'MACDHist_corr_roll_mean3_shift3', 'MACDHist_corr_roll_mean3_shift6', 'AweOs_cor_roll_mean3_shift3', 'AweOs_cor_roll_mean3_shift6']


# MODEL_PARAMS_MULTI_1H ={
#    'learning_rate':0.035,
#            'l2_leaf_reg':400,
#            'iterations':3500,
#             'verbose':False
# }


# #версия 25.03.23 МУЛТИ


col_fin_multi_1h=['MACDHist_corr', 'ROC200', 'ROC200sm', 'TSI', 'EMA8_REL', 'EMA8_REL_shift24', 'EMA20_REL', 'EMA50_REL', 'EMA150_REL', 'EMA200_REL_shift6', 'EMA200_REL_shift24', 'MA5_REL_shift24', 'MA10_REL_shift6', 'MA10_REL_shift12', 'MA15_REL_shift12', 'MA20_REL', 'MA20_REL_shift6', 'MA25_REL_shift12', 'MA50_REL', 'MA75_REL', 'MA150_REL', 'MA150_REL_shift12', 'MA200_REL', 'MACDHist_REL', 'MACDHist_REL_shift5', 'MACDHist_REL_shift7', 'MACDHist_REL_shift10', 'date_key_h', 'date_key_d', 'std_20_rel', 'std_100_rel', 'RSI14_coef_nak', 'Close_coef_nak', 'Volume_coef_nak', 'MA100_coef_nak', 'std_20_coef_nak', 'MACDHist_nak', 'Close_coef_nak_div_RSI14_coef_nak', 'Close_coef_nak_div_MACDHist_nak', 'Close_10_to_11', 'Close_11_to_12', 'Close_0_to_5', 'Close_m3_1_to_MA15', 'Close_3_to_MA15', 'Close_4_to_MA15', 'Close_9_to_MA15', 'Close_15_to_MA15', 'RSI14', 'RSI20', 'RSI27', 'level_close_old_w', 'level_close_act_w', 'step_to_fiba', 'MACDHist_corr_0_to_1', 'MACDHist_0_to_1', 'MACDHist_1_to_3', 'MACDHist_3_to_6', 'AweOs_0_to_1', 'AweOs_3_to_6', 'Close_coef_nak2', 'PER_OPEN_shift8', 'PER_CLOSE_shift1', 'POLNOTA_shift1', 'POLNOTA_shift2', 'POLNOTA_shift3', 'POLNOTA_shift4', 'POLNOTA_shift7', 'POLNOTA_shift9', 'POLNOTA_shift10', 'Close_2_to_b', 'Low_0_to_b', 'Low_3_to_b', 'Low_4_to_b', 'High_0_to_b', 'High_1_to_b', 'High_2_to_b', 'High_3_to_b', 'down_near', 'mae_opt_near', 'up_far', 'mae_opt_far', 'freq_up_all_300', 'freq_dw_all_300', 'freq_up_ch_300', 'freq_up_all_100', 'freq_dw_all_100', 'freq_up_all_50', 'plotnost_300_all', 'plotnost_300_ch', 'plotnost_100_all', 'plotnost_100_ch', 'plotnost_50_all', 'balance_300_all', 'balance_300_ch', 'balance_100_all', 'MA20_REL_shift24', 'MA25_REL_shift24', 'MA50_REL_shift24', 'MACDHist_corr_roll_mean3_shift6', 'AweOs_cor_roll_mean3_shift3', 'AweOs_cor_roll_mean3_shift6']


MODEL_PARAMS_MULTI_1H ={
           'l2_leaf_reg':35,
            'verbose':False
}



###########################################################################################################################
###############################################    15M     #################################################################
###########################################################################################################################


####################       15M      ВЕРСИЯ 02.07


#версия 02.07
col_fin_up_15m=['MACDHist_corr', 'AweOs_cor', 'ROC200', 'ROC200sm', 'TSI', 'EMA8_REL', 'EMA8_REL_shift6', 'EMA8_REL_shift24', 'EMA12_REL', 'EMA12_REL_shift12', 'EMA12_REL_shift24', 'EMA14_REL', 'EMA14_REL_shift12', 'EMA20_REL_shift12', 'EMA20_REL_shift24', 'EMA26_REL', 'EMA26_REL_shift12', 'EMA26_REL_shift24', 'EMA32_REL', 'EMA32_REL_shift6', 'EMA38_REL', 'EMA38_REL_shift12', 'EMA38_REL_shift24', 'EMA44_REL', 'EMA44_REL_shift12', 'EMA50_REL_shift6', 'EMA50_REL_shift12', 'EMA50_REL_shift24', 'EMA60_REL', 'EMA60_REL_shift24', 'EMA100_REL', 'EMA100_REL_shift1', 'EMA100_REL_shift12', 'EMA100_REL_shift24', 'EMA150_REL', 'EMA150_REL_shift1', 'EMA150_REL_shift6', 'EMA150_REL_shift12', 'EMA150_REL_shift24', 'EMA200_REL', 'EMA200_REL_shift1', 'EMA200_REL_shift6', 'EMA200_REL_shift6_cross', 'EMA200_REL_shift12', 'EMA200_REL_shift24', 'MA5_REL', 'MA5_REL_shift12', 'MA5_REL_shift24', 'MA10_REL', 'MA10_REL_shift12', 'MA10_REL_shift24', 'MA15_REL', 'MA15_REL_shift6', 'MA15_REL_shift12', 'MA15_REL_shift24', 'MA20_REL', 'MA20_REL_shift12', 'MA20_REL_shift24', 'MA25_REL', 'MA25_REL_shift1', 'MA25_REL_shift6', 'MA25_REL_shift12', 'MA25_REL_shift12_cross', 'MA25_REL_shift24', 'MA50_REL', 'MA50_REL_shift1', 'MA50_REL_shift6', 'MA50_REL_shift12', 'MA50_REL_shift24', 'MA75_REL', 'MA75_REL_shift1', 'MA75_REL_shift6', 'MA75_REL_shift12', 'MA75_REL_shift24', 'MA100_REL', 'MA100_REL_shift1', 'MA100_REL_shift6', 'MA100_REL_shift12', 'MA100_REL_shift24', 'MA100_REL_shift24_cross', 'MA150_REL', 'MA150_REL_shift1', 'MA150_REL_shift6', 'MA150_REL_shift12', 'MA150_REL_shift24', 'MA150_REL_shift24_cross', 'MA200_REL', 'MA200_REL_shift1', 'MA200_REL_shift6', 'MA200_REL_shift12', 'MA200_REL_shift24', 'MACDHist_REL', 'MACDHist_REL_shift1', 'MACDHist_REL_shift3', 'MACDHist_REL_shift5', 'MACDHist_REL_shift7', 'MACDHist_REL_shift10', 'EMA_gor_12_REL_cross_all', 'EMA_gor_24_REL_cross_all', 'MA_gor_12_REL_cross_all', 'MA_gor_24_REL_cross_all', 'date_key_h', 'date_key_d', 'std_20_rel', 'std_100_rel', 'RSI14_coef_nak', 'Close_coef_nak', 'Volume_coef_nak', 'EMA14_coef_nak', 'MA100_coef_nak', 'std_20_coef_nak', 'MACDHist_nak', 'Close_coef_nak_div_Volume_coef_nak', 'Close_coef_nak_div_RSI14_coef_nak', 'Close_coef_nak_div_MACDHist_nak', 'Close_0_to_1', 'Close_1_to_2', 'Close_2_to_3', 'Close_4_to_5', 'Close_6_to_7', 'Close_7_to_8', 'Close_8_to_9', 'Close_9_to_10', 'Close_10_to_11', 'Close_11_to_12', 'Close_0_to_3', 'Close_0_to_4', 'Close_0_to_5', 'Close_0_to_6', 'Close_0_to_9', 'Close_0_to_12', 'Close_m3_0_to_MA15', 'Close_m3_1_to_MA15', 'Close_m3_2_to_MA15', 'Close_m3_3_to_MA15', 'Close_m3_4_to_MA15', 'Close_m3_5_to_MA15', 'Close_m3_6_to_MA15', 'Close_m3_9_to_MA15', 'Close_m3_12_to_MA15', 'Close_0_to_MA15', 'Close_2_to_MA15', 'Close_3_to_MA15', 'Close_4_to_MA15', 'Close_5_to_MA15', 'Close_7_to_MA15', 'Close_8_to_MA15', 'Close_9_to_MA15', 'Close_10_to_MA15', 'Close_11_to_MA15', 'Close_12_to_MA15', 'Close_13_to_MA15', 'Close_14_to_MA15', 'Close_15_to_MA15', 'RSI9_up_70_perman', 'RSI14_dw_30_perman', 'RSI20_dw_30_perman', 'RSI27_up_70_perman', 'RSI27_dw_30_perman', 'RSI9', 'RSI14', 'RSI20', 'RSI27', 'level_close_old_w', 'level_close_act_w', 'step_to_fiba', 'MACDHist_corr_shift1', 'MACDHist_corr_shift3', 'MACDHist_corr_shift6', 'AweOs_cor_shift1', 'AweOs_cor_shift3', 'AweOs_cor_shift6', 'MACDHist_corr_0_to_1', 'MACDHist_corr_1_to_3', 'MACDHist_0_to_1', 'MACDHist_1_to_3', 'MACDHist_3_to_6', 'AweOs_0_to_1', 'AweOs_1_to_3', 'AweOs_3_to_6', 'AweOs_corr_0_to_1', 'Close_coef_nak2', 'PER_OPEN_shift1', 'PER_OPEN_shift3', 'PER_OPEN_shift5', 'PER_CLOSE_shift0', 'PER_CLOSE_shift1', 'PER_CLOSE_shift2', 'PER_CLOSE_shift6', 'POLNOTA_shift0', 'POLNOTA_shift1', 'POLNOTA_shift2', 'POLNOTA_shift3', 'POLNOTA_shift4', 'POLNOTA_shift5', 'POLNOTA_shift6', 'Close_1_to_b', 'Close_3_to_b', 'Close_5_to_b', 'Open_0_to_b', 'Open_4_to_b', 'Open_5_to_b', 'Low_0_to_b', 'Low_1_to_b', 'Low_2_to_b', 'Low_3_to_b', 'Low_4_to_b', 'Low_5_to_b', 'High_0_to_b', 'High_1_to_b', 'High_2_to_b', 'High_3_to_b', 'High_4_to_b', 'High_5_to_b', 'EVENT20', 'EVENT19', 'EVENT16', 'EVENT15', 'EVENT14', 'EVENT13', 'EVENT11', 'EVENT10', 'EVENT8', 'EVENT3']


#версия 02.07
col_fin_dw_15m=['MACDHist_corr', 'AweOs_cor', 'ROC200', 'ROC200sm', 'TSI', 'EMA32_REL', 'EMA100_REL', 'EMA150_REL_shift6', 'EMA150_REL_shift24', 'EMA200_REL', 'EMA200_REL_shift1', 'EMA200_REL_shift6', 'EMA200_REL_shift12', 'EMA200_REL_shift24', 'MA10_REL_shift24', 'MA15_REL_shift24', 'MA20_REL_shift12', 'MA20_REL_shift24', 'MA25_REL', 'MA25_REL_shift6', 'MA25_REL_shift12', 'MA25_REL_shift24', 'MA50_REL', 'MA50_REL_shift12', 'MA50_REL_shift24', 'MA75_REL', 'MA75_REL_shift6', 'MA75_REL_shift12', 'MA75_REL_shift24', 'MA100_REL', 'MA100_REL_shift1', 'MA100_REL_shift6', 'MA100_REL_shift12', 'MA100_REL_shift24', 'MA150_REL', 'MA150_REL_shift6', 'MA150_REL_shift24', 'MA200_REL', 'MA200_REL_shift6', 'MA200_REL_shift12', 'MA200_REL_shift24', 'MACDHist_REL', 'MACDHist_REL_shift1', 'MACDHist_REL_shift3', 'MACDHist_REL_shift5', 'MACDHist_REL_shift7', 'MACDHist_REL_shift10', 'EMA_gor_24_REL_cross_all', 'date_key_h', 'date_key_d', 'std_20_rel', 'std_100_rel', 'RSI14_coef_nak', 'Close_coef_nak', 'Volume_coef_nak', 'EMA14_coef_nak', 'MA100_coef_nak', 'std_20_coef_nak', 'MACDHist_nak', 'Close_coef_nak_div_Volume_coef_nak', 'Close_coef_nak_div_RSI14_coef_nak', 'Close_coef_nak_div_MACDHist_nak', 'Close_0_to_1', 'Close_1_to_2', 'Close_9_to_10', 'Close_11_to_12', 'Close_0_to_4', 'Close_m3_0_to_MA15', 'Close_m3_6_to_MA15', 'Close_15_to_MA15', 'RSI27_up_70_perman', 'RSI9', 'RSI14', 'RSI20', 'RSI27', 'level_close_old_w', 'level_close_act_w', 'step_to_fiba', 'MACDHist_corr_shift1', 'MACDHist_corr_shift3', 'MACDHist_corr_shift6', 'AweOs_cor_shift1', 'AweOs_cor_shift3', 'AweOs_cor_shift6', 'MACDHist_1_to_3', 'AweOs_3_to_6', 'AweOs_corr_0_to_1', 'Close_coef_nak2', 'PER_OPEN_shift5', 'Low_0_to_b', 'Low_1_to_b', 'Low_3_to_b', 'Low_4_to_b', 'High_0_to_b', 'High_1_to_b', 'High_2_to_b', 'High_3_to_b', 'EVENT19', 'EVENT16', 'EVENT15', 'EVENT14', 'EVENT13', 'EVENT4', 'EVENT3']


#версия 02.07
MODEL_PARAMS_UP_15M = {

     'boosting_type':'gbdt',
#      'num_leaves': 50, 
      'max_depth': 7, 
#      'learning_rate': 0.1,
#      'n_estimators': 100,
#      'min_child_samples': 20,
#      'subsample': 0.7,
#      'colsample_bytree': 0.7, 
#      'min_child_weight': 5,
#      'reg_alpha': 0,
      'reg_lambda': 100,
#      'random_state': 42, 
    'scale_pos_weight': 1,
      'n_jobs': 10
            }


#версия 02.07
MODEL_PARAMS_DW_15M = {

     'boosting_type':'gbdt',
#      'num_leaves': 50, 
      'max_depth': 6, 
#      'learning_rate': 0.1,
#      'n_estimators': 100,
#      'min_child_samples': 20,
#      'subsample': 0.7,
#      'colsample_bytree': 0.7, 
#      'min_child_weight': 5,
#      'reg_alpha': 0,
      'reg_lambda': 200,
#      'random_state': 42, 
    'scale_pos_weight': 1,
      'n_jobs': 10
}