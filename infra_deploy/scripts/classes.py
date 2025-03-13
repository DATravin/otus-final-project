import pandas as pd
import numpy as np
#import lightgbm as lgb
import datetime
import math
from random import random
from sklearn.model_selection import cross_validate
from sklearn.metrics import roc_auc_score,fbeta_score,classification_report,log_loss,roc_curve,auc
from tqdm.autonotebook import tqdm
from sklearn.model_selection import cross_val_score, KFold
from catboost import CatBoostClassifier, Pool
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LinearRegression
# from fbprophet import Prophet
#import seaborn as sns
#from matplotlib import pyplot as plt

    
class Features:
    
    def __init__(self, config_btc,time_frame,bit_functions):
        
        #config_btc=reload(config_btc)
        self.config = config_btc
        self.bit_functions=bit_functions
        self.time_frame=time_frame
        #config_btc.MODEL_PARAMS_UP_4H
        #config_btc.MODEL_PARAMS_UP_4H
        
        
    def unic_date(timestamp):
        
        timestamp=str(timestamp)

        timestamp=int(timestamp[:-3])
        value = datetime.datetime.fromtimestamp(timestamp)
        new_date=value.strftime('%Y-%m-%d %H:%M:%S')
        return new_date
        
    def _first_prep(self,data):
        
        '''
        первая обработка, на вход дата фрейм минутный
        1) схлопывание до нужного дата фрейма
        2) расчет порядкого номера
        3) форматирование даты
        4) отсечение столбцов
        5) заполнение пустых значений
        
        '''
        
        data['time_key_m'] =  pd.to_datetime(data['Timestamp'], dayfirst=True)
        data = data.rename(columns={"Volume_(BTC)": "Volume"})

        #data =data.drop(['Unnamed: 0','Volume_(Currency)','Weighted_Price','Timestamp'], 1) 
        
        data=data[['Open', 'High', 'Low', 'Close', 'Volume','time_key_m']]

        data=data[data.time_key_m>='2017-06-01']
        
        if self.time_frame=='4H':

            data2=self.bit_functions.min_to_4h(data)
        
        elif self.time_frame=='1H':
            
            data2=self.bit_functions.min_to_hour(data)
            
        elif self.time_frame=='15M':
            
            data=data[data.time_key_m>='2019-01-01']
            
            data2=self.bit_functions.min_to_15min(data)
            
            
        
        

        return data2
    
    
    def _first_prep_1m(self,data_base):
        
        '''
        первая обработка, на вход дата фрейм минутный
        1) схлопывание до нужного дата фрейма
        2) расчет порядкого номера
        3) форматирование даты
        4) отсечение столбцов
        5) заполнение пустых значений
        
        '''
        data=data_base.copy()
        #print(data)
        
        data['Timestamp'] = data.apply(lambda x: self.bit_functions.unic_date(x.close_time),axis=1)



        data.rename(columns={'open': 'Open',
                           'high': 'High',
                           'low': 'Low',
                           'close': 'Close',
                            'volume':'Volume'

                          }, inplace=True)

        data['Open'] = [x.replace(',', '.') for x in data['Open']]
        data['Low'] = [x.replace(',', '.') for x in data['Low']]
        data['High'] = [x.replace(',', '.') for x in data['High']]
        data['Volume'] = [x.replace(',', '.') for x in data['Volume']]
        data['Close'] = [x.replace(',', '.') for x in data['Close']]

        data['Open']  = data['Open'] .astype(float)
        data['Low']  = data['Low'] .astype(float)
        data['High']  = data['High'] .astype(float)
        data['Volume']  = data['Volume'] .astype(float)
        data['Close']  = data['Close'] .astype(float)

        data['time_key_h2'] =  pd.to_datetime(data['Timestamp'], dayfirst=True)

        data=data[['Open','High','Low','Close','Volume','time_key_h2']]

        data=data[data.time_key_h2>='2017-06-01']
        
        data=data.set_index(data.time_key_h2)
        
        data =data.drop(['time_key_h2'], 1)  
        
#         if self.time_frame=='4H':

#             data2=self.bit_functions.min_to_4h(data)
        
#         elif self.time_frame=='1H':
            
#             data2=self.bit_functions.min_to_hour(data)
            
#         elif self.time_frame=='15M':
            
#             data=data[data.time_key_m>='2019-01-01']
            
#             data2=self.bit_functions.min_to_15min(data)
            

        return data
    
    
    
    
    def _first_prep_no_d(self,data_base):
        
        '''
        первая обработка, на вход дата фрейм минутный
        1) схлопывание до нужного дата фрейма
        2) расчет порядкого номера
        3) форматирование даты
        4) отсечение столбцов
        5) заполнение пустых значений
        
        '''
        data=data_base.copy()
        #print(data)
        
        data['time_key_h2'] =  pd.to_datetime(data['TimeKey'], dayfirst=True)


        data=data.set_index(data.time_key_h2)
        

        data=data[['Open','High','Low','Close','Volume']]
        
        return data
        
        

    
    
    def _first_prep_new(self,data):
        
        '''
        первая обработка, на вход дата фрейм минутный
        1) схлопывание до нужного дата фрейма
        2) расчет порядкого номера
        3) форматирование даты
        4) отсечение столбцов
        5) заполнение пустых значений
        
        '''
        
        data['Timestamp'] = data.apply(lambda x: self.bit_functions.unic_date(x.close_time),axis=1)



        data.rename(columns={'open': 'Open',
                           'high': 'High',
                           'low': 'Low',
                           'close': 'Close',
                            'volume':'Volume'

                          }, inplace=True)

        data['Open'] = [x.replace(',', '.') for x in data['Open']]
        data['Low'] = [x.replace(',', '.') for x in data['Low']]
        data['High'] = [x.replace(',', '.') for x in data['High']]
        data['Volume'] = [x.replace(',', '.') for x in data['Volume']]
        data['Close'] = [x.replace(',', '.') for x in data['Close']]

        data['Open']  = data['Open'] .astype(float)
        data['Low']  = data['Low'] .astype(float)
        data['High']  = data['High'] .astype(float)
        data['Volume']  = data['Volume'] .astype(float)
        data['Close']  = data['Close'] .astype(float)

        data['time_key_m'] =  pd.to_datetime(data['Timestamp'], dayfirst=True)

        data=data[['Open','High','Low','Close','Volume','time_key_m']]

        data=data[data.time_key_m>='2017-06-01']
        
        
        
        if self.time_frame=='4H':

            data2=self.bit_functions.min_to_4h(data)
        
        elif self.time_frame=='1H':
            
            data2=self.bit_functions.min_to_hour(data)
            
        elif self.time_frame=='15M':
            
            data=data[data.time_key_m>='2019-01-01']
            
            data2=self.bit_functions.min_to_15min(data)
            
            
        
        

        return data2    
    
    
    def _ffild_data(self,data):
        
        
        data['High'] = data['High'].fillna(method='ffill')
        data['Low'] = data['Low'].fillna(method='ffill')
        data['Open'] = data['Open'].fillna(method='ffill')
        data['Close'] = data['Close'].fillna(method='ffill')
        data['Volume'] = data['Volume'].fillna(method='ffill')
        
        data['ROW_NUM'] = data.reset_index().index
        data['ROW_NUM'] = data['ROW_NUM'].astype(int)
   
        data['date_for_ind']=data.index
        data['ROWNUM'] = data['date_for_ind'].rank(method='min')
        data['ROWNUM'] = data['ROWNUM'].astype(int)
        
        data['date_key']=data.index
        data['date_key']= pd.to_datetime(data['date_key'])

        data['date_key_h'] = data['date_key'].dt.hour
        data['date_key_d'] = data['date_key'].dt.dayofweek
        
        return data
    
    
    def _compute_traget(self,data):
        
        '''
        расчет таргетов, несколько вариантов,
        возможно нужно будет обновлять. Подумать, тоже нужно будет обновлять!!!!!!!!!!!!!!
        
        
        '''
        
        par1=self.config.target_var_par.get(self.time_frame)[0]
        par2=self.config.target_var_par.get(self.time_frame)[1]
        
        data['fut_8_stps_high'] = data.apply(lambda x:self.bit_functions.target_extrem_future(data,x.ROW_NUM,8,'High'),axis=1)
        data['fut_8_stps_low'] = data.apply(lambda x:self.bit_functions.target_extrem_future(data,x.ROW_NUM,8,'Low'),axis=1)
        data['fut_10_stps_high'] = data.apply(lambda x:self.bit_functions.target_extrem_future(data,x.ROW_NUM,10,'High'),axis=1)
        data['fut_10_stps_low'] = data.apply(lambda x:self.bit_functions.target_extrem_future(data,x.ROW_NUM,10,'Low'),axis=1)


        data['fut_8_stps_all_2'] = data.apply(lambda x:self.bit_functions.target_extrem_future2(data,x.ROW_NUM,8,x.Close,0.02),axis=1)
        data['fut_10_stps_all_2'] = data.apply(lambda x:self.bit_functions.target_extrem_future2(data,x.ROW_NUM,10,x.Close,0.02),axis=1)
        data['fut_8_stps_all_3'] = data.apply(lambda x:self.bit_functions.target_extrem_future2(data,x.ROW_NUM,8,x.Close,0.03),axis=1)
        data['fut_10_stps_all_3'] = data.apply(lambda x:self.bit_functions.target_extrem_future2(data,x.ROW_NUM,10,x.Close,0.03),axis=1)
        
        data['fut_8_stps_all_1'] = data.apply(lambda x:self.bit_functions.target_extrem_future2(data,x.ROW_NUM,8,x.Close,0.01),axis=1)
        data['fut_10_stps_all_1'] = data.apply(lambda x:self.bit_functions.target_extrem_future2(data,x.ROW_NUM,10,x.Close,0.01),axis=1)
        
        data['fut_3_stps_all_2'] = data.apply(lambda x:self.bit_functions.target_extrem_future2(data,x.ROW_NUM,par1,x.Close,par2),axis=1)
        
        
        
        
        if self.time_frame=='4H':
        
            data['target_var4_up']=np.where((data.fut_3_stps_all_2==1)|(data.fut_3_stps_all_2==2),1,0)
            data['target_var4_dw']=np.where((data.fut_3_stps_all_2==-1)|(data.fut_3_stps_all_2==2),1,0)
        
        elif self.time_frame=='1H':
            
            data['target_var4_up']=np.where((data.fut_3_stps_all_2==1)|(data.fut_3_stps_all_2==2),1,0)
            data['target_var4_dw']=np.where((data.fut_3_stps_all_2==-1)|(data.fut_3_stps_all_2==2),1,0)
            
        elif self.time_frame=='15M':
            
            data['target_var4_up']=np.where(data.fut_10_stps_all_1==1,1,0)
            data['target_var4_dw']=np.where(data.fut_10_stps_all_1==-1,1,0)
            

        return data
    
    def _compute_index(self,data):
        
        '''
        расчет базовых индексов, и фичей поверх базовых индексов
        
        
        '''
    
        #базовые индексы
        WINDOWS = [8,12, 14, 20, 26, 32, 38, 44, 50, 60, 75, 100, 150, 200]
        data = self.bit_functions.compute_indicates(data,'EMA', WINDOWS)
        WINDOWS = [5, 10, 15, 20 , 25, 50, 75, 100, 150, 200]
        data = self.bit_functions.compute_indicates(data,'MA', WINDOWS)
        WINDOWS = [9, 14, 20, 27]
        data = self.bit_functions.compute_indicates(data,'RSI', WINDOWS)
        WINDOWS = [0]
        data = self.bit_functions.compute_indicates(data,'MACD', WINDOWS)
        WINDOWS = [0]
        data = self.bit_functions.compute_indicates(data,'Awesome', WINDOWS)
        WINDOWS = [0]
        data = self.bit_functions.compute_indicates(data,'Boll', WINDOWS)
        WINDOWS = [0]
        data = self.bit_functions.compute_indicates(data,'ROC', WINDOWS)
        WINDOWS = [0]
        data = self.bit_functions.compute_indicates(data,'TCI', WINDOWS)
        

        #return data

    #def _compute_index_t(self,data):

        
        # относительные 
        SHIFTS = [1,6, 12,24]
        VAR_LIST=['EMA8', 'EMA12',
               'EMA14', 'EMA20', 'EMA26', 'EMA32', 'EMA38', 'EMA44', 'EMA50', 'EMA60',
               'EMA75', 'EMA100', 'EMA150', 'EMA200', 'MA5', 'MA10', 'MA15', 'MA20',
               'MA25', 'MA50', 'MA75', 'MA100', 'MA150', 'MA200']

        data=self.bit_functions.create_rel(data,VAR_LIST,SHIFTS,'gliding')

        SHIFTS = [0,1,3,5,7,10]
        VAR_LIST=['MACDHist','Signal']

        data=self.bit_functions.create_rel(data,VAR_LIST,SHIFTS,'two')

        VAR_LIST=['RSI9','RSI14','RSI20','RSI27']
        SHIFTS = [0]

        data=self.bit_functions.create_rel(data,VAR_LIST,SHIFTS,'RSI')
        
        
        # запуск расчета кол-ва часов непрерывного пребывания RSI выше/ниже уровней
        VAR_LIST=['RSI9','RSI14','RSI20','RSI27']
        data=self.bit_functions.rsi_perman(data,VAR_LIST)
        
        # запуск расчета этих суммарных пересечений

        SHIFTS = [1,6, 12,24]
        VAR_LIST=['EMA8', 'EMA12',
               'EMA14', 'EMA20', 'EMA26', 'EMA32', 'EMA38', 'EMA44', 'EMA50', 'EMA60',
               'EMA75', 'EMA100', 'EMA150', 'EMA200']

        data=self.bit_functions.create_rel_cross(data,'EMA',VAR_LIST,SHIFTS,'cross_all')

        SHIFTS = [1,6, 12,24]
        VAR_LIST=[ 'MA5', 'MA10', 'MA15', 'MA20',
               'MA25', 'MA50', 'MA75', 'MA100', 'MA150', 'MA200']

        df_test=self.bit_functions.create_rel_cross(data,'MA',VAR_LIST,SHIFTS,'cross_all')
        
        
        # стандартные отклонения
        data['std_20'] = data['Close'].rolling(window=20,min_periods=1).std()
        data['std_20_rel'] = np.where(data['Close']>0,data['std_20']/data['Close'],0)

        data['std_100'] = data['Close'].rolling(window=100,min_periods=1).std()
        data['std_100_rel'] = np.where(data['Close']>0,data['std_100']/data['Close'],0)
        
        data['std_500'] = data['Close'].rolling(window=500,min_periods=1).std()
        data['std_500_rel'] = np.where(data['Close']>0,data['std_500']/data['Close'],0)
        
    
        return data
    
    
    def _naklon(self,data):
        
        '''
        наклонов и диверов
        
        
        '''
        
        
        windowsRSI14 = [10,20,30]
        self.bit_functions.coef_nak(data,'RSI14',windowsRSI14,np.max(windowsRSI14)+1)
        #data['RSI14_coef_nak'] = data.apply(lambda x:self.bit_functions.coef_nak(data,'RSI14',windowsRSI14,x.ROW_NUM),axis=1)


        #df_test['RSI_coef_nak'] = df_test.apply(lambda x:target_value(df_test,x.ROW_NUM,x.Close,0.03),axis=1)
        #print(0)
#         data['RSI14_coef_nak'] = data.apply(lambda x:self.bit_functions.coef_nak(data,'RSI14',[10,20,30],x.ROW_NUM),axis=1)
#         #print(1)
        data['Close_coef_nak'] = data.apply(lambda x:self.bit_functions.coef_nak(data,'Close',[10,20,30,40],x.ROW_NUM),axis=1)
#         #print(2)
#         data['Volume_coef_nak'] = data.apply(lambda x:self.bit_functions.coef_nak(data,'Volume',[10,20,30,40],x.ROW_NUM),axis=1)
#         #print(3)
#         data['EMA14_coef_nak'] = data.apply(lambda x:self.bit_functions.coef_nak(data,'EMA14',[10,20,30,40],x.ROW_NUM),axis=1)
#         #print(4)
#         data['MA100_coef_nak'] = data.apply(lambda x:self.bit_functions.coef_nak(data,'MA100',[10,20,30,40],x.ROW_NUM),axis=1)
#         #print(5)
#         data['std_20_coef_nak'] = data.apply(lambda x:self.bit_functions.coef_nak(data,'std_20',[10,20,30],x.ROW_NUM),axis=1)
#         #print(6)
#         data['MACDHist_nak'] = data.apply(lambda x:self.bit_functions.coef_nak(data,'MACDHist',[10,20,30],x.ROW_NUM),axis=1)
#         #print(7)
#         data['Close_coef_nak2'] = data.apply(lambda x:self.bit_functions.coef_nak(data,'Close',[150,200,250],x.ROW_NUM),axis=1)
        
#         #диверы    
#         VARIBLES=['Volume_coef_nak','RSI14_coef_nak','MACDHist_nak']

#         data=self.bit_functions.diver(data,'Close_coef_nak',VARIBLES)

        return data
    
    def _calculate_fiba(self,data):
        
        '''
        расчет уровней фибоначи, а также шага до ближайшей фибы
        
        
        '''
        
        
        df_orig2=self.bit_functions.fiba1(data)

        list_columns=['date_for_ind', 'ROWNUM', 'fiba1618_w',
               'fiba1000_w', 'fiba764_w', 'fiba610_w', 'fiba500_w', 'fiba382_w',
               'fiba236_w', 'fiba000_w', 'fiba236m_w', 'level_close_old_w',
               'level_close_act_w']


        list_of_drops=['fiba1618_w',
               'fiba1000_w', 'fiba764_w', 'fiba610_w', 'fiba500_w', 'fiba382_w',
               'fiba236_w', 'fiba000_w', 'fiba236m_w', 'level_close_old_w',
               'level_close_act_w']

        for f in list_of_drops:
            #print(f)
            if f in data.columns:
                #print('yes')
                data =data.drop([f], 1) 

        data=pd.merge(data, df_orig2[list_columns], on=['date_for_ind','ROWNUM'], how='left')

        data['step_to_fiba'] = data.apply(lambda x: self.bit_functions.close_fiba(data,x.ROWNUM),axis=1)    
        
        
        
        return data
    
    
    
    def _calculate_sinus(self,data):
        
        '''
        расчет прогноза через синосоиды,
        возвращает прогноз апроксимирующей синусойды
        
        
        '''
        
        #короткий прогноз
        
        windows=[20,30,40]
        df_orig=self.bit_functions.segmoid_predict(data,windows)
        
     
        df_orig.rename(columns={'down': 'down_near',
                  'up': 'up_near',
                  'mae_opt': 'mae_opt_near'
                 }, inplace=True)
        
        
        list_columns=['date_for_ind', 'ROWNUM', 'down_near','up_near','mae_opt_near']
        list_of_drops=['down_near','up_near','mae_opt_near']

        for f in list_of_drops:
            #print(f)
            if f in data.columns:
                #print('yes')
                data =data.drop([f], 1) 

        data=pd.merge(data, df_orig[list_columns], on=['date_for_ind','ROWNUM'], how='left')
        print("короткий готов")
        
        #короткий прогноз
        
        windows=[75,100]
        df_orig=self.bit_functions.segmoid_predict(data,windows)
        
     
        df_orig.rename(columns={'down': 'down_far',
                  'up': 'up_far',
                  'mae_opt': 'mae_opt_far'
                 }, inplace=True)
        
        
        list_columns=['date_for_ind', 'ROWNUM', 'down_far','up_far','mae_opt_far']
        list_of_drops=['down_far','up_far','mae_opt_far']

        for f in list_of_drops:
            #print(f)
            if f in data.columns:
                #print('yes')
                data =data.drop([f], 1) 

        data=pd.merge(data, df_orig[list_columns], on=['date_for_ind','ROWNUM'], how='left')
        
        
        
        return data
    
    
    def _calculate_svechi(self,data):
        
        '''
        расчет свечных паттернов
        
        
        '''
        
        # бычие/медвежие свечи
        data['SV_DIR']=np.where(data.Close>data.Open,1,-1)

        # полнота свечи
        data['PER_OPEN']=np.where(data.Low!=data.High,(data.Open-data.Low)/(data.High-data.Low),1)
        data['PER_CLOSE']=np.where(data.Low!=data.High,(data.Close-data.Low)/(data.High-data.Low),1)
        data['POLNOTA']=np.where(data['SV_DIR']==1,data['PER_CLOSE']-data['PER_OPEN'],data['PER_OPEN']-data['PER_CLOSE'])

        # метки молота
        data['type_molot'] = data.apply(lambda x:self.bit_functions.molot(x.PER_OPEN,x.PER_CLOSE),axis=1)

        WINDOWS = [3,6]
        SHIFTS = [0,1,2,3,4,5,6,7,8,9,10,11]

        # шифты
        data= self.bit_functions.compute_roll_shift_stat(data, ['High', 'Low', 'Open', 'Close','SV_DIR','PER_OPEN','PER_CLOSE','type_molot','POLNOTA'], WINDOWS, SHIFTS, 'mean')

        data=self.bit_functions.create_rel_shifts2(data)
        
        
        # 20 паттернов
        df_orig2=self.bit_functions.svechi(data)
        
        
        list_columns=['date_for_ind', 'ROWNUM', 'EVENT22','EVENT21','EVENT20','EVENT19','EVENT18','EVENT17','EVENT16','EVENT15','EVENT14',
               'EVENT13','EVENT12','EVENT11','EVENT10','EVENT9',
              'EVENT8','EVENT7','EVENT6','EVENT5','EVENT4','EVENT3','EVENT2','EVENT1']


        list_of_drops=['EVENT22','EVENT21','EVENT20','EVENT19','EVENT18','EVENT17','EVENT16','EVENT15','EVENT14',
                       'EVENT13','EVENT12','EVENT11','EVENT10','EVENT9',
                      'EVENT8','EVENT7','EVENT6','EVENT5','EVENT4','EVENT3','EVENT2','EVENT1']

        for f in list_of_drops:
            #print(f)
            if f in data.columns:
                #print('yes')
                data =data.drop([f], 1) 

        data=pd.merge(data, df_orig2[list_columns], on=['date_for_ind','ROWNUM'], how='left')

        
        return data
    
    
    def _shifts(self,data):
        
        # шифты 
        WINDOWS = [3, 6]
        SHIFTS = [-8,-1,0, 1, 2, 3,4,5, 6,7,8, 9,10,11, 12,13,14,15]

        data= self.bit_functions.compute_roll_shift_stat(data, ['Close'], WINDOWS, SHIFTS, 'mean')

        WINDOWS = [3]
        SHIFTS = [0,1,3,6]

        data= self.bit_functions.compute_roll_shift_stat(data, ['MACDHist_corr','MACDHist','AweOs','AweOs_cor'], WINDOWS, SHIFTS, 'mean')
        data=self.bit_functions.create_rel_shifts(data)
        
        
        return data
    
    
    def _ffilna(self,data):
        
        # заполнение пустых

        for col in data.columns:
            data[col]=data[col].fillna(method="ffill")
        
        return data
    
    
    def _freak_succes(self,df,par1,par2):
        
        df['freq_up_all_300'] = df.apply(lambda x: self.bit_functions.event_freaq(df,x.ROW_NUM,300,'up','all',par1,par2),axis=1)
        df['freq_dw_all_300'] = df.apply(lambda x: self.bit_functions.event_freaq(df,x.ROW_NUM,300,'dw','all',par1,par2),axis=1)
        df['freq_up_ch_300'] = df.apply(lambda x: self.bit_functions.event_freaq(df,x.ROW_NUM,300,'up','chain',par1,par2),axis=1)
        df['freq_dw_ch_300'] = df.apply(lambda x: self.bit_functions.event_freaq(df,x.ROW_NUM,300,'dw','chain',par1,par2),axis=1)
        
        df['freq_up_all_100'] = df.apply(lambda x: self.bit_functions.event_freaq(df,x.ROW_NUM,100,'up','all',par1,par2),axis=1)
        df['freq_dw_all_100'] = df.apply(lambda x: self.bit_functions.event_freaq(df,x.ROW_NUM,100,'dw','all',par1,par2),axis=1)
        df['freq_up_ch_100'] = df.apply(lambda x: self.bit_functions.event_freaq(df,x.ROW_NUM,100,'up','chain',par1,par2),axis=1)
        df['freq_dw_ch_100'] = df.apply(lambda x: self.bit_functions.event_freaq(df,x.ROW_NUM,100,'dw','chain',par1,par2),axis=1)
        
        df['freq_up_all_50'] = df.apply(lambda x: self.bit_functions.event_freaq(df,x.ROW_NUM,50,'up','all',par1,par2),axis=1)
        df['freq_dw_all_50'] = df.apply(lambda x: self.bit_functions.event_freaq(df,x.ROW_NUM,50,'dw','all',par1,par2),axis=1)
        df['freq_up_ch_50'] = df.apply(lambda x: self.bit_functions.event_freaq(df,x.ROW_NUM,50,'up','chain',par1,par2),axis=1)
        df['freq_dw_ch_50'] = df.apply(lambda x: self.bit_functions.event_freaq(df,x.ROW_NUM,50,'dw','chain',par1,par2),axis=1)
        
        df['plotnost_300_all']=df['freq_up_all_300']+df['freq_dw_all_300'] 
        df['plotnost_300_ch']=df['freq_up_ch_300']+df['freq_dw_ch_300'] 
        df['plotnost_100_all']=df['freq_up_all_100']+df['freq_dw_all_100'] 
        df['plotnost_100_ch']=df['freq_up_ch_100']+df['freq_dw_ch_100'] 
        df['plotnost_50_all']=df['freq_up_all_50']+df['freq_dw_all_50'] 
        df['plotnost_50_ch']=df['freq_up_ch_50']+df['freq_dw_ch_50'] 

        df['balance_300_all']=df['freq_up_all_300']-df['freq_dw_all_300'] 
        df['balance_300_ch']=df['freq_up_ch_300']-df['freq_dw_ch_300'] 
        df['balance_100_all']=df['freq_up_all_100']-df['freq_dw_all_100'] 
        df['balance_100_ch']=df['freq_up_ch_100']-df['freq_dw_ch_100'] 
        df['balance_50_all']=df['freq_up_all_50']-df['freq_dw_all_50'] 
        df['balance_50_ch']=df['freq_up_ch_50']-df['freq_dw_ch_50'] 
        
        return df
    
    def _compute_multi_target(self,df):
        
        df['target_multi']=df['fut_3_stps_all_2']
        
        mask=(df['fut_3_stps_all_2']==2)&(df['Close_shift0']>=df['Close_shift1'])
        df.loc[mask, 'target_multi'] = 1
        
        mask=(df['fut_3_stps_all_2']==2)&(df['Close_shift0']<df['Close_shift1'])
        df.loc[mask, 'target_multi'] = -1

        return df
    
    def _compute_fiba_trends(self,df):
        
        df['direction_local_window']=None
        df['rel_for_local_window']=None
        df['direction_global_window']=None
        df['rel_for_global_window']=None
        df['position_of_global_min']=None
        df['position_of_global_max']=None
        df['position_of_local_min']=None
        df['position_of_local_max']=None
        df['engel_min_trend']=None
        df['engel_max_trend']=None
        df['engel_close_trend']=None
        df['engel_vol_trend']=None
        df['rel_to_min_trend']=None
        df['rel_to_max_trend']=None
        df['prophet_max_rel']=None
        df['prophet_fct_rel']=None
        df['prophet_min_rel']=None
        
        
        
        df['date_for_prophet'] = df.apply(lambda x : self.bit_functions.change_date2(x.date_for_ind),axis=1) 
        
        list_of_clumns=[
        'direction_local_window',
        'rel_for_local_window',
        'direction_global_window',
        'rel_for_global_window',
        'position_of_global_min',
        'position_of_global_max',
        'position_of_local_min',
        'position_of_local_max',
        'engel_min_trend',
        'engel_max_trend',
        'engel_close_trend',
        'engel_vol_trend',
        'rel_to_min_trend',
        'rel_to_max_trend',
        'prophet_max_rel',
        'prophet_min_rel',
        'prophet_fct_rel'

        ]

        for index1, row1 in tqdm(df.iterrows()):
            rn = row1['ROWNUM']
            if self.time_frame == '4H':
                dict_features = Fibo_trends_class(df,rn,prophet_active = True).get_features()
            elif self.time_frame == '1H':
                #dict_features = Fibo_trends_class(df,rn,prophet_active = False).get_features()
                dict_features = Fibo_trends_class(df,rn,prophet_active = True).get_features()
            for col in list_of_clumns:
                df.loc[(df['ROWNUM'] == rn), col] = dict_features.get(col)
                
        return df
    
    def _compute_target_new(self,df,n_bord = 0.01):
        
        df['Close_sm_5'] = df['Close'].rolling(window=5,min_periods=1).mean()
        df['Close_sm_53'] = df['Close_sm_5'].rolling(window=3,min_periods=1).mean()
        
        
        df['direction_idl']=None
        df['max_take_idl']=None
        df['step_to_idl']=None
        df['rn_of_next_take']=None
        df['max_stop_idl']=None
        df['target_value_idl']=None
        df['maximum_value_for_take_idl']=None
        df['minimum_value_for_stop_idl']=None


        list_of_clumns=[
            'direction_idl',
            'max_take_idl',
            'step_to_idl',
            'rn_of_next_take',
            'max_stop_idl',
            'target_value_idl',
            'maximum_value_for_take_idl',
            'minimum_value_for_stop_idl'


        ]
        
        #print('n_board1:', n_bord)

        for index1, row1 in tqdm(df.iterrows()):
            rn = row1['ROWNUM']
            
            dict_features = self.bit_functions.find_min_max3(df,rn,rn+1,rn+10,step_add=3,n_bord=n_bord)
            for col in list_of_clumns:
                df.loc[(df['ROWNUM'] == rn), col] = dict_features.get(col)


        
        min_dif = self.config.target_var_par_new.get(self.time_frame)[0]
        max_dlin = self.config.target_var_par_new.get(self.time_frame)[1]
        min_rel = self.config.target_var_par_new.get(self.time_frame)[2]
        df['target_new'] = df.apply(lambda x: self.bit_functions.target_new(df,x.ROWNUM,min_dif,max_dlin,min_rel),axis=1)
    
        return df
    
    def transform(self, data_base):
        
        '''
        весь pipeline
        

        '''
        
        par1=self.config.target_var_par.get(self.time_frame)[0]
        par2=self.config.target_var_par.get(self.time_frame)[1]
        
        data = data_base.copy()
        
#         data = self._first_prep(data)
#         print('00')
        data = self._ffild_data(data)
        print('step1 ffild',datetime.datetime.now())
        data = self._compute_index(data)
        print('step3 indexes',datetime.datetime.now())
        data = self._naklon(data)
        print('step4 naklon',datetime.datetime.now())
        data = self._calculate_fiba(data)
        print('step5 fiba old',datetime.datetime.now())
        data = self._shifts(data)
        print('step6 sifts',datetime.datetime.now())
        #data=self._ffilna(data)
        print('step10 ffilna',datetime.datetime.now())
        data = self._compute_target_new(data)
        print('step13 new target',datetime.datetime.now())
        print('end',datetime.datetime.now())
        
        return data

        
    def append(self,data_old,data_new):
        
        '''
        
        добавление новой свечи к общему дата сету и ресет индексов
        

        '''
        
        max_old_date=data_old.date_for_ind.max()
        add_data=data_new[data_new.date_for_ind>max_old_date]

        data_new=pd.concat([data_old, add_data], ignore_index=True)
        data_new.sort_values(by=['date_for_ind'], ascending=True, inplace=True)

        #data_new=data_new.reset_index()


        data_new['ROW_NUM'] = data_new.reset_index().index
        data_new['ROW_NUM'] = data_new['ROW_NUM'].astype(int)

        #data_new['date_for_ind']=data_new.index
        data_new['ROWNUM'] = data_new['date_for_ind'].rank(method='min')
        data_new['ROWNUM'] = data_new['ROWNUM'].astype(int)
        
        return data_new
    
    
   
