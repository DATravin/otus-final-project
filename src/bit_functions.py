import math
import numpy as np
from datetime import datetime, timedelta
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import roc_auc_score,fbeta_score,classification_report,log_loss,roc_curve,auc
from sklearn.metrics import average_precision_score,accuracy_score,r2_score
from scipy.optimize import curve_fit
import pandas as pd
from random import random
from sklearn.model_selection import cross_validate
# import matplotlib.pyplot as plt
# import seaborn as sns
# import lightgbm as lgb
from sklearn.metrics import precision_recall_curve,PrecisionRecallDisplay
from catboost import CatBoostClassifier, Pool
from sklearn.inspection import permutation_importance
import config_btc
import classes
# import bit_functions
import config_btc

#import datetime

#функция, чтобы минутынй дата фрейм превратить в часовой


def test_df2(df):
    df_new=df.tail(100)
    return df_new


def tt():
    print('yes')
    return 1

def min_to_hour(df):

    df2= df.copy()

    df2['time_key_h2']=df2.time_key_m.dt.floor('h')

    df2[f'High2'] = df2.groupby(['time_key_h2'])['High'].transform('max')
    df2[f'Low2'] = df2.groupby(['time_key_h2'])['Low'].transform('min')
    df2[f'Open2'] = df2.groupby(['time_key_h2'])['Open'].transform('first')
    df2[f'Close2'] = df2.groupby(['time_key_h2'])['Close'].transform('last')
    df2[f'Volume2'] = df2.groupby(['time_key_h2'])['Volume'].transform('sum')

    df2=df2[['High2','Low2','Open2','Close2','Volume2','time_key_h2']].drop_duplicates()
    df2=df2.set_index(df2.time_key_h2)
    df2 =df2.drop(['time_key_h2'], 1)

    df2.rename(columns={'High2': 'High',
                       'Low2': 'Low',
                       'Open2': 'Open',
                   'Close2': 'Close',
                   'Volume2': 'Volume'
                  }, inplace=True)
    return df2


def min_to_5min(df):

    '''

     свертка минутного df до 5минуток


    '''


    df2= df.copy()
    #df2['time_key_h']=df2.index

    df2['time_key_h2']=df2.time_key_m.dt.floor('5min')

    df2[f'High2'] = df2.groupby(['time_key_h2'])['High'].transform('max')
    df2[f'Low2'] = df2.groupby(['time_key_h2'])['Low'].transform('min')
    df2[f'Open2'] = df2.groupby(['time_key_h2'])['Open'].transform('first')
    df2[f'Close2'] = df2.groupby(['time_key_h2'])['Close'].transform('last')
    df2[f'Volume2'] = df2.groupby(['time_key_h2'])['Volume'].transform('sum')

    df2=df2[['High2','Low2','Open2','Close2','Volume2','time_key_h2']].drop_duplicates()
    df2=df2.set_index(df2.time_key_h2)
    df2 =df2.drop(['time_key_h2'], 1)

    df2.rename(columns={'High2': 'High',
                       'Low2': 'Low',
                       'Open2': 'Open',
                   'Close2': 'Close',
                   'Volume2': 'Volume'
                  }, inplace=True)
    return df2


def min_to_15min(df):

    '''

     свертка минутного df до 5минуток


    '''


    df2= df.copy()
    #df2['time_key_h']=df2.index

    df2['time_key_h2']=df2.time_key_m.dt.floor('15min')

    df2[f'High2'] = df2.groupby(['time_key_h2'])['High'].transform('max')
    df2[f'Low2'] = df2.groupby(['time_key_h2'])['Low'].transform('min')
    df2[f'Open2'] = df2.groupby(['time_key_h2'])['Open'].transform('first')
    df2[f'Close2'] = df2.groupby(['time_key_h2'])['Close'].transform('last')
    df2[f'Volume2'] = df2.groupby(['time_key_h2'])['Volume'].transform('sum')

    df2=df2[['High2','Low2','Open2','Close2','Volume2','time_key_h2']].drop_duplicates()
    df2=df2.set_index(df2.time_key_h2)
    df2 =df2.drop(['time_key_h2'], 1)

    df2.rename(columns={'High2': 'High',
                       'Low2': 'Low',
                       'Open2': 'Open',
                   'Close2': 'Close',
                   'Volume2': 'Volume'
                  }, inplace=True)
    return df2



def min_to_4h(df):


    '''

     свертка минутного df до 4H


    '''
    df2= df.copy()
    #df2['time_key_h']=df2.index

    df2['time_key_h2']=df2.time_key_m.dt.floor('4h')

    df2[f'High2'] = df2.groupby(['time_key_h2'])['High'].transform('max')
    df2[f'Low2'] = df2.groupby(['time_key_h2'])['Low'].transform('min')
    df2[f'Open2'] = df2.groupby(['time_key_h2'])['Open'].transform('first')
    df2[f'Close2'] = df2.groupby(['time_key_h2'])['Close'].transform('last')
    df2[f'Volume2'] = df2.groupby(['time_key_h2'])['Volume'].transform('sum')

    df2=df2[['High2','Low2','Open2','Close2','Volume2','time_key_h2']].drop_duplicates()
    df2=df2.set_index(df2.time_key_h2)
    df2 =df2.drop(['time_key_h2'], 1)

    df2.rename(columns={'High2': 'High',
                       'Low2': 'Low',
                       'Open2': 'Open',
                   'Close2': 'Close',
                   'Volume2': 'Volume'
                  }, inplace=True)
    return df2



def test_df(df):
    df_new=df.tail(20)
    return df_new


def test_df2(df):
    df_new=df.tail(100)
    return df_new



def f1_test(df,first_row_num,period,type_var):

    first_row_num=int(first_row_num)
    df=df[first_row_num:first_row_num+period+1][['High', 'Low', 'Open', 'Close', 'Volume','ROW_NUM']]

    max_high=df[1:].High.max()
    min_low=df[1:].Low.min()

    if type_var=='High':
        return max_high
    else:
        return min_low


## расчет упращенных таргетов

def target_extrem_future(df,first_row_num,period,type_var):

    '''

    поиск минимума и максимума на period свечей вперед


    '''


    first_row_num=int(first_row_num)
    df=df[first_row_num:first_row_num+period+1][['High', 'Low', 'Open', 'Close', 'Volume','ROW_NUM']]

    max_high=df[1:].High.max()
    min_low=df[1:].Low.min()

    if type_var=='High':
        return max_high
    else:
        return min_low


def f1_test(df,first_row_num,period,type_var):

    first_row_num=int(first_row_num)
    df=df[first_row_num:first_row_num+period+1][['High', 'Low', 'Open', 'Close', 'Volume','ROW_NUM']]

    max_high=df[1:].High.max()
    min_low=df[1:].Low.min()

    if type_var=='High':
        return max_high
    else:
        return min_low


def target_extrem_future2(df,first_row_num,period,cl_price,per):


    '''

     получение категории роста или падения на period свечей вперед


    '''

    first_row_num=int(first_row_num)
    #df=df[first_row_num+1:first_row_num+period+1][['High', 'Low', 'Open', 'Close', 'Volume','ROW_NUM']]
    df=df[(df.ROW_NUM>first_row_num)&(df.ROW_NUM<first_row_num+period+1)][['High', 'Low', 'Open', 'Close', 'Volume','ROW_NUM']]

#     max_high=df[1:].High.max()
#     min_low=df[1:].Low.min()

    max_high=df[:].High.max()
    min_low=df[:].Low.min()

    up=math.fabs(max_high/cl_price-1)
    down=math.fabs(cl_price/min_low-1)

    #print(df)

    #print(cl_price)

    for index1, row1 in df.iterrows():

        max_loc=row1['High']
        min_loc=row1['Low']

#         up_loc=math.fabs(max_loc/cl_price-1)
#         down_loc=math.fabs(min_loc/min_low-1)

        up_loc=max_loc/cl_price-1
        down_loc=cl_price/min_loc-1

        #print(cl_price,max_loc,min_loc,up_loc,down_loc)

        if up_loc>=per and down_loc<per:
            #print(1)
            return 1
        elif up_loc<per and down_loc>=per:
            #print(-1)
            return -1
        elif up_loc>=per and down_loc>=per and up_loc>=down_loc:
            #print(1)
            return 0 #было 2
        elif up_loc>=per and down_loc>=per and up_loc<down_loc:
            #print(-1)
            return 0 #было 2

    return 0


#для каждого столбца сначала делаем просто щифтт на n шагов, потом для разных окон (по умолчанию 3) еще усредненный шифт

def compute_roll_shift_stat(df, cols, WINDOWS, SHIFTS, func):

    '''

     шифты и усредненные шифты


    '''

    for col in cols:
        for shift in SHIFTS:
            df[f'{col}_shift{shift}'] = df[col].shift(shift)
        for window in WINDOWS:
            df[f'{col}_roll_{func}{window}'] = (
                    getattr(df[col].rolling(window=window,min_periods=1), func)().values
                )
            for shift in SHIFTS:
                df[f'{col}_roll_{func}{window}_shift{shift}'] = (
                    df[f'{col}_roll_{func}{window}'].shift(shift).values
                )

    return df



#расчет различных индекаторов, при запуске, передаем ей название индикатора и окно, по которому считаем там, где это актуально

def compute_indicates(df, type_ind, WINDOWS):

    '''

     общая функция для расчета разных индикаторов


    '''

    if type_ind=='EMA':

        for window in WINDOWS:
            df[f'EMA{window}'] = df['Close'].ewm(span=window, adjust=False).mean()

    elif type_ind == 'MA':

        for window in WINDOWS:
            df[f'MA{window}'] = df['Close'].rolling(window=window,min_periods=1).mean()

    elif type_ind == 'RSI':  ############################################# поправил
        #https://fooobar.com/questions/491811/relative-strength-index-in-python-pandas
        #https://av-finance.ru/texnicheskij-analiz/indikator-rsi.html#formula-rascheta-indikatora-rsi

        df['up']=np.where(df.Close>df.Open,df.Close-df.Open,0)
        df['down']=np.where(df.Close<df.Open,df.Open-df.Close,0)

        for window in WINDOWS:

            #df['up_roll'] = df['up'].ewm(span=window, adjust=False).mean()
            #df['down_roll'] = df['down'].ewm(span=window, adjust=False).mean()

            df['up_roll'] = df['up'].rolling(window=window,min_periods=1).mean()
            df['down_roll'] = df['down'].rolling(window=window,min_periods=1).mean()


            df['RS1'] = df['up_roll'] / df['down_roll']
            df[f'RSI{window}'] = 100-(100/(1+df['RS1']))

        #df =df.drop(['up','down','up_roll','down_roll','RS1'], 1)

    elif type_ind == 'MACD':
        #https://coincase.ru/blog/47567/

        df['exp12_t'] = df['Close'].ewm(span=12, adjust=False).mean()
        df['exp26_t']  = df['Close'].ewm(span=26, adjust=False).mean()
        df['MACD']= df['exp12_t']-df['exp26_t']
        df['Signal']= df['MACD'].ewm(span=9, adjust=False).mean()
        df['MACDHist']=df['MACD']-df['Signal']
        df['MACDHist_std_30'] = df['MACDHist'].rolling(window=30,min_periods=1).std()
        df['MACDHist_corr']=df['MACDHist']/df['MACDHist_std_30']
        #df =df.drop(['exp26_t','exp12_t','MACDHist_std_30'], 1)

    elif type_ind=='Awesome':  ############################################# поправил
        #https://www.azbukatreydera.ru/awesome-oscillator.html
        df['median_price']=(df['High']+df['Low'])/2
        df['ma5_t'] = df['median_price'].rolling(window=5,min_periods=1).mean()
        df['ma34_t'] = df['median_price'].rolling(window=34,min_periods=1).mean()
        df['AweOs']= df['ma5_t']-df['ma34_t']
        df['AweOs_std_30'] = df['AweOs'].rolling(window=30,min_periods=1).std()
        df['AweOs_cor']= df['AweOs']/df['AweOs_std_30']
        #df =df.drop(['ma34_t','ma5_t','median_price','AweOs_std_30'], 1)


    elif type_ind=='Boll':
        #https://stackoverflow.com/questions/42114381/bollinger-bands-in-python-where-how-rm-and-rstd-get-defined-in-code-below
        df['ma20_t'] = df['Close'].rolling(window=20,min_periods=1).mean()
        df['std_20'] = df['Close'].rolling(window=20,min_periods=1).std()
        df['Boll_up'] = df['ma20_t']+df['std_20']*2
        df['Boll_down'] = df['ma20_t']-df['std_20']*2
        #df =df.drop(['std_20','ma20_t'], 1)


    elif type_ind=='ROC': ######################################################хуета
        #https://quantrum.me/2059-indikator-sily-trendy-tsi-na-python/
        df['Close200']=df['Close'].shift(200).values
        df['ROC200']=np.where(df['Close200']>0,((df['Close']/df['Close200'])-1)*100,0)
        df['ROC200sm']=df['ROC200'].ewm(span=4, adjust=False).mean()


        #df =df.drop(['Close200'], 1)

    elif type_ind=='TCI':  ############### вроде +/- корректно
        df['ATR_d']=abs(df['Close']-df['Open'])
        df['ATR_10'] = df['ATR_d'].rolling(window=10,min_periods=1).mean()
        df['Close10']=df['Close'].shift(10).values
        df['ratio']=np.where(df['ATR_10']>0,abs(df['Close']-df['Close10'])/df['ATR_10'],1)

        df['TSI'] = df['ratio'].rolling(window=10,min_periods=1).mean().rolling(window=50,min_periods=1).mean()-1

        #df =df.drop(['ATR_d','ATR_10','Close10','ratio'], 1)


    return df




def create_rel(df,list_var,shifts,type_var):

    # функция, которая превращает ряд индикаторов в относительные величиын, типа отношение скользящей к цене Close
# кроме того, для EMA и MA мы ищем метки пересечения цены Close

    if type_var=='gliding':

        for var in list_var:

            df[f'{var}_REL']=np.where(df.Close>0,df[f'{var}']/df.Close,1)

            for shift in shifts:

                df[f'{var}_REL_shift{shift}'] = df[f'{var}_REL'].shift(shift).values

                df['tech_up']=np.where((df[f'{var}_REL']>=1)&(df[f'{var}_REL_shift{shift}']<1),1,0)
                df['tech_down']=np.where((df[f'{var}_REL']<1)&(df[f'{var}_REL_shift{shift}']>=1),1,0)
                df['tech_test']=np.where(df['tech_up']==df['tech_down'],1,0)

                df[f'{var}_REL_shift{shift}_cross']=np.where(df['tech_test']==1,0,np.where(df['tech_up']==1,1,np.where(df['tech_down']==1,-1,0)))

                #df =df.drop(['tech_up','tech_down','tech_test'], 1)




    elif type_var=='two':

        var1=list_var[0]
        var2=list_var[1]

        #print(var1,var2)

        df['MAX_MOD']=np.where(abs(df[f'{var1}'])>abs(df[f'{var2}']),abs(df[f'{var1}']),abs(df[f'{var2}']))

        df[f'{var1}_REL']=np.where(df[f'{var1}'].notnull(),(df[f'{var1}']-df[f'{var2}'])/df['MAX_MOD'],1)


        for shift in shifts:

            df[f'{var1}_REL_shift{shift}'] = df[f'{var1}_REL'].shift(shift).values

        #df =df.drop(['MAX_MOD'], 1)

    elif type_var=='RSI':

        for var in list_var:

            df[f'{var}_up_70']=np.where(df[f'{var}']>70,1,0)
            df[f'{var}_dw_30']=np.where(df[f'{var}']<30,1,0)

            df[f'{var}_up_80']=np.where(df[f'{var}']>80,1,0)
            df[f'{var}_dw_20']=np.where(df[f'{var}']<20,1,0)






    return df







def rsi_perman(df,list_var):

    # функция для расчета кол-ва свечей непрерывного пребывания RSI выше/ниже уровней 70,80,20,30


    list_sh=[]

    for var in list_var:

        df[f'{var}_up_70_perman']=0
        df[f'{var}_dw_30_perman']=0

        df[f'{var}_up_80_perman']=0
        df[f'{var}_dw_20_perman']=0

        list_sh.append(0)
        list_sh.append(0)
        list_sh.append(0)
        list_sh.append(0)



    #for index1, row1 in df[(df.ROW_NUM>=255)&(df.ROW_NUM<265)].iterrows():
    for index1, row1 in df.iterrows():

        num_list=0

        for var in list_var:


            if row1[f'{var}_up_70']==1:
                #df.loc[index1, f'{var}_up_70_perman'] = df.loc[index1, f'{var}_up_70_perman']+1
                df.loc[index1, f'{var}_up_70_perman'] =list_sh[num_list] +1
                list_sh[num_list]+=1
            else:
                df.loc[index1, f'{var}_up_70_perman'] =0
                list_sh[num_list]=0

            num_list=num_list+1

            #print('1',list_sh[1])
            #print('num_list',num_list)

            if row1[f'{var}_dw_30']==1:

                #print(list_sh[num_list],num_list)
                #df.loc[index1, f'{var}_up_70_perman'] = df.loc[index1, f'{var}_up_70_perman']+1
                df.loc[index1, f'{var}_dw_30_perman'] =list_sh[num_list] +1
                list_sh[num_list]+=1
                #print('2',list_sh[1])
                #print(list_sh[num_list],num_list)
            else:
                df.loc[index1, f'{var}_dw_30_perman'] =0
                list_sh[num_list]=0

            num_list=num_list+1

            #print('2',list_sh[1])
            #print('num_list',num_list)

            if row1[f'{var}_up_80']==1:
                #df.loc[index1, f'{var}_up_70_perman'] = df.loc[index1, f'{var}_up_70_perman']+1
                df.loc[index1, f'{var}_up_80_perman'] =list_sh[num_list] +1
                list_sh[num_list]+=1
            else:
                df.loc[index1, f'{var}_up_80_perman'] =0
                list_sh[num_list]=0

            num_list=num_list+1

            #print('3',list_sh[1])
            #print('num_list',num_list)

            if row1[f'{var}_dw_20']==1:
                #df.loc[index1, f'{var}_up_70_perman'] = df.loc[index1, f'{var}_up_70_perman']+1
                df.loc[index1, f'{var}_dw_20_perman'] =list_sh[num_list] +1
                list_sh[num_list]+=1
            else:
                df.loc[index1, f'{var}_dw_20_perman'] =0
                list_sh[num_list]=0

            num_list=num_list+1

            #print('4',list_sh[1])

            #print(index1,list_sh,row1['ROW_NUM'])

                #df[f'{var}_up_70_shift1'] = df[f'{var}_up_70'].shift(1).values
                #df[f'{var}_up_80_shift1'] = df[f'{var}_up_80'].shift(1).values
                #df[f'{var}_dw_30_shift1'] = df[f'{var}_dw_30'].shift(1).values
                #df[f'{var}_dw_20_shift1'] = df[f'{var}_dw_20'].shift(1).values

    return df





def create_rel_cross(df,target_var,list_var,shifts,type_var):

# ну это мутная фича, что-то типа общее кол-во пересечений цены close с EMA или MA за один и тот же период
# логика в том, что чем больше за время T прошло пересечений, тем сильнее сигнал к логнг или шорт
# и тут мы берем метки пересечений по всем EMA или MA и делим на кол-во скольщящих. Типа если все пересекли, то будет 10/10,
# типа 1, а если только 2 из 10, будет 0,2

    if type_var=='cross_all':



        for shift in shifts:

            df[f'{target_var}_gor_{shift}_REL_cross_all']=0

            for var in list_var:

             df[f'{target_var}_gor_{shift}_REL_cross_all']=df[f'{target_var}_gor_{shift}_REL_cross_all']+df[f'{var}_REL_shift{shift}_cross']

            df[f'{target_var}_gor_{shift}_REL_cross_all']=df[f'{target_var}_gor_{shift}_REL_cross_all']/len(list_var)
    return df










def coef_nak(df_orig,col,windows,cur_row):

    '''
    расчет коэф наклона
    Внутри нескольких окон мы нормируем данные, после чего строим регрессии.
    Коэф. - это наклон. Берем средний коэф, чем лучше регрессия описывает данные (чистый тренд), тем
    больший вес именно этого коэффициента

    '''

    #print(cur_row,np.max(windows))

    if cur_row<=np.max(windows):
        #print('gg')
        return 0

    list_of_stab=[]
    list_of_coef=[]

    #print(1)

    df_orig['SQ']=df_orig[col].rolling(window=1,min_periods=1).mean()
    #print(1)

    for w in windows:

        #print(w)

#         if w==30:

        df=df_orig[(df_orig.ROWNUM>cur_row-w)&(df_orig.ROWNUM<=cur_row)]

#         if w==30:
            #print(2)

        scaler = StandardScaler()
        model = LinearRegression()
        x=df.ROWNUM.values.reshape(-1, 1)

        #df['SQ']=df[col].rolling(window=5,min_periods=1).mean() #,center=True
        y=df['SQ'].values.reshape(-1, 1)

#         if w==30:
            #print(3)

        model.fit(x, y)
        y_pred = model.predict(x)
        std=np.std(y_pred-y)
        coef_stab=float(std)

        if coef_stab==0:
            coef_stab=0
        else:
            coef_stab=1/coef_stab
        #coef_stab=coef_stab/w

#         if w==30:
#             #print(4)

        if np.max(x)==np.min(x):
            x=x-np.min(x)
        else:
            x=(x-np.min(x))/(np.max(x)-np.min(x))

        if np.max(y)==np.min(y):
            y=y-np.min(y)
        #y=(y-np.mean(y))/np.std(y)
        else:
            y=(y-np.min(y))/(np.max(y)-np.min(y))


#         if w==30:
#             #print(5)

        model.fit(x, y)
        y_pred = model.predict(x)
        r2=r2_score(y, y_pred,multioutput='variance_weighted')
        #std=np.std(y_pred-y)
        #coef_stab=float(r2)
        coef_nak=math.atan(model.coef_) * 180 /math.pi


        list_of_stab.append(coef_stab)
        list_of_coef.append(coef_nak)

        #print(coef_stab,coef_nak)

#         if w==30:
            #print(6)

    w_coef=0
    for i in range(0,len(list_of_coef)):
        w_coef=w_coef+list_of_coef[i]*list_of_stab[i]/sum(list_of_stab)

        #print(list_of_coef[i],list_of_stab[i])
        #print(list_of_stab[i]/sum(list_of_stab))

    #print(w_coef)

    #df_orig =df_orig.drop(['SQ'], 1)

#     if w==30:
        #print(7)
    #print(round(float(w_coef),4))
    #nom_min=np.argmin(list_of_stab)
    return round(float(w_coef),4)



def diver(df,target_var,list_var):

# расчет своеобразного дивера. Передаем две фичи с коэф.наклона. если у коэф. разный знак, значит есть дивер.
# и дальше мы из берем модуль разницы углов, типа сила дивера


    for var in list_var:

        #df['sign_target']=np.sign(df[f'{target_var}'])
        #df['sign_target2']=np.sign(df[f'{var}'])
        df[f'{target_var}_div_{var}']=np.where((df[f'{target_var}']>0)&(df[f'{var}']<0),df[f'{target_var}']-df[f'{var}'],
                                               np.where((df[f'{target_var}']<0)&(df[f'{var}']>0),df[f'{target_var}']-df[f'{var}'],0))


    return df





def fiba1(df_test):

    '''
    расчет уровней фибы. В 3-х окнах смотрим уровни фибы,
    усредням, и получаем уровни

    '''

    col='Close'
    windows=[50,75,100]
    df_orig=df_test[['date_for_ind','Close','High','Low','ROWNUM']].copy()


    df_orig['fiba1618_w'] = 0
    df_orig['fiba1000_w'] = 0
    df_orig['fiba764_w'] = 0
    df_orig['fiba610_w'] = 0
    df_orig['fiba500_w'] = 0
    df_orig['fiba382_w'] = 0
    df_orig['fiba236_w'] = 0
    df_orig['fiba000_w'] = 0
    df_orig['fiba236m_w'] = 0
    df_orig['level_close_old_w'] = 0
    df_orig['level_close_act_w'] = 0

    for index1, row1 in df_orig.iterrows():

        cur_row=row1['ROWNUM']
        #print(cur_row)
        close_now=row1['Close']

        #print(cur_row)

        if cur_row<=np.max(windows):
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'fiba1618_w'] = 0
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'fiba1000_w'] = 0
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'fiba764_w'] = 0
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'fiba610_w'] =  0
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'fiba500_w'] = 0
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'fiba382_w'] = 0
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'fiba236_w'] = 0
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'fiba000_w'] = 0
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'fiba236m_w'] = 0
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'level_close_old_w'] = 0
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'level_close_act_w'] = 0

        else:

            list_of_stab=[]
            list_of_coef=[]

            list_fiba1618=[]
            list_fiba1000=[]
            list_fiba764=[]
            list_fiba610=[]
            list_fiba500=[]
            list_fiba382=[]
            list_fiba236=[]
            list_fiba000=[]
            list_fiba236m=[]
            list_level_close_old=[]
            list_level_close_act=[]

            df_orig['SQ']=df_orig[col].rolling(window=1,min_periods=1).mean()

            for w in windows:



                df=df_orig[(df_orig.ROWNUM>cur_row-w)&(df_orig.ROWNUM<=cur_row)]


                coef_stab=1
                coef_nak=1

                list_of_stab.append(coef_stab)
                list_of_coef.append(coef_nak)




                max_high=df[1:].High.max()
                min_low=df[1:].Low.min()
                close_start=float(df[0:1].Close)

                dif=max_high-min_low

                fiba1618=min_low+dif*1.618
                fiba1000=min_low+dif
                fiba764=min_low+dif*0.764
                fiba764=min_low+dif*0.764
                fiba610=min_low+dif*0.61
                fiba500=min_low+dif*0.5
                fiba382=min_low+dif*0.382
                fiba236=min_low+dif*0.236
                fiba000=min_low-dif*0
                fiba236m=min_low-dif*0.236


                level_close_old=(close_start-min_low)/dif
                level_close_act=(close_now-min_low)/dif

                list_fiba1618.append(fiba1618)
                list_fiba1000.append(fiba1000)
                list_fiba764.append(fiba764)
                list_fiba610.append(fiba610)
                list_fiba500.append(fiba500)
                list_fiba382.append(fiba382)
                list_fiba236.append(fiba236)
                list_fiba000.append(fiba000)
                list_fiba236m.append(fiba236m)
                list_level_close_old.append(level_close_old)
                list_level_close_act.append(level_close_act)



            w_coef=0
            fiba1618_w=0
            fiba1000_w=0
            fiba764_w=0
            fiba610_w=0
            fiba500_w=0
            fiba382_w=0
            fiba236_w=0
            fiba000_w=0
            fiba236m_w=0
            level_close_old_w=0
            level_close_act_w=0

            for i in range(0,len(list_of_coef)):
                w_coef=w_coef+list_of_coef[i]*list_of_stab[i]/sum(list_of_stab)

                fiba1618_w=fiba1618_w+list_fiba1618[i]*list_of_stab[i]/sum(list_of_stab)
                fiba1000_w=fiba1000_w+list_fiba1000[i]*list_of_stab[i]/sum(list_of_stab)
                fiba764_w=fiba764_w+list_fiba764[i]*list_of_stab[i]/sum(list_of_stab)
                fiba610_w=fiba610_w+list_fiba610[i]*list_of_stab[i]/sum(list_of_stab)
                fiba500_w=fiba500_w+list_fiba500[i]*list_of_stab[i]/sum(list_of_stab)
                fiba382_w=fiba382_w+list_fiba382[i]*list_of_stab[i]/sum(list_of_stab)
                fiba236_w=fiba236_w+list_fiba236[i]*list_of_stab[i]/sum(list_of_stab)
                fiba000_w=fiba000_w+list_fiba000[i]*list_of_stab[i]/sum(list_of_stab)
                fiba236m_w=fiba236m_w+list_fiba236m[i]*list_of_stab[i]/sum(list_of_stab)
                level_close_old_w=level_close_old_w+list_level_close_old[i]*list_of_stab[i]/sum(list_of_stab)
                level_close_act_w=level_close_act_w+list_level_close_act[i]*list_of_stab[i]/sum(list_of_stab)

                #print(list_of_coef[i],list_of_stab[i])
                #print(list_of_stab[i]/sum(list_of_stab))

            #print(w_coef)

            #df_orig =df_orig.drop(['SQ'], 1)


            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'fiba1618_w'] = fiba1618_w
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'fiba1000_w'] = fiba1000_w
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'fiba764_w'] = fiba764_w
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'fiba610_w'] =  fiba610_w
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'fiba500_w'] = fiba500_w
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'fiba382_w'] = fiba382_w
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'fiba236_w'] = fiba236_w
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'fiba000_w'] = fiba000_w
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'fiba236m_w'] = fiba236m_w
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'level_close_old_w'] = level_close_old_w
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'level_close_act_w'] = level_close_act_w
    return df_orig





def close_fiba(df,rn_target):


    '''
    расчетываем ближайшие уровни, к которому мы стремимся по фибе. Смотрим, сколько нам еще идти к ближайшему

    '''



    act_value_sh=df[df.ROWNUM==rn_target].level_close_act_w.values
    Close_coef_nak=df[df.ROWNUM==rn_target].Close_coef_nak.values
    act_value_close=df[df.ROWNUM==rn_target].Close.values
    f1000=df[df.ROWNUM==rn_target].fiba1000_w.values
    f764=df[df.ROWNUM==rn_target].fiba764_w.values
    f610=df[df.ROWNUM==rn_target].fiba610_w.values
    f500=df[df.ROWNUM==rn_target].fiba500_w.values
    f382=df[df.ROWNUM==rn_target].fiba382_w.values
    f236=df[df.ROWNUM==rn_target].fiba236_w.values
    f000=df[df.ROWNUM==rn_target].fiba000_w.values

    #

    if act_value_sh>0 and act_value_sh<=0.236 and Close_coef_nak<0:
        move=-act_value_close/f000
    elif act_value_sh>0 and act_value_sh<=0.236 and Close_coef_nak>0:
        move=f236/act_value_close

    elif act_value_sh>0.236 and act_value_sh<=0.382 and Close_coef_nak<0:
        move=-act_value_close/f236
    elif act_value_sh>0.236 and act_value_sh<=0.382 and Close_coef_nak>0:
        move=f382/act_value_close

    elif act_value_sh>0.382 and act_value_sh<=0.500 and Close_coef_nak<0:
        move=-act_value_close/f382
    elif act_value_sh>0.382 and act_value_sh<=0.500 and Close_coef_nak>0:
        move=f500/act_value_close

    elif act_value_sh>0.500 and act_value_sh<=0.610 and Close_coef_nak<0:
        move=-act_value_close/f500
    elif act_value_sh>0.500 and act_value_sh<=0.610 and Close_coef_nak>0:
        move=f610/act_value_close

    elif act_value_sh>0.610 and act_value_sh<=0.764 and Close_coef_nak<0:
        move=-act_value_close/f610
    elif act_value_sh>0.610 and act_value_sh<=0.764 and Close_coef_nak>0:
        move=f764/act_value_close

    elif act_value_sh>0.764 and act_value_sh<=1 and Close_coef_nak<0:
        move=-act_value_close/f764
    elif act_value_sh>0.764 and act_value_sh<=1 and Close_coef_nak>0:
        move=f1000/act_value_close
    else:
        move=0

    #print(rn_target,float(move))

    return float(move)






def create_rel_shifts(df):

    # здесь собираются метрики, связанные с отношением одних периодов к другим



    #для геоюнита среднего факты
    df['Close_next']=np.where(df.Close_shift0>0,df['Close_shift-8']/df.Close_shift0,1)
    df['Close_0_to_1']=np.where(df.Close_shift1>0,df.Close_shift0/df.Close_shift1,1)
    df['Close_1_to_2']=np.where(df.Close_shift2>0,df.Close_shift1/df.Close_shift2,1)
    df['Close_2_to_3']=np.where(df.Close_shift3>0,df.Close_shift2/df.Close_shift3,1)
    df['Close_3_to_4']=np.where(df.Close_shift4>0,df.Close_shift3/df.Close_shift4,1)
    df['Close_4_to_5']=np.where(df.Close_shift5>0,df.Close_shift4/df.Close_shift5,1)
    df['Close_5_to_6']=np.where(df.Close_shift6>0,df.Close_shift5/df.Close_shift6,1)
    df['Close_6_to_7']=np.where(df.Close_shift7>0,df.Close_shift6/df.Close_shift7,1)
    df['Close_7_to_8']=np.where(df.Close_shift8>0,df.Close_shift7/df.Close_shift8,1)
    df['Close_8_to_9']=np.where(df.Close_shift9>0,df.Close_shift8/df.Close_shift9,1)
    df['Close_9_to_10']=np.where(df.Close_shift10>0,df.Close_shift9/df.Close_shift10,1)
    df['Close_10_to_11']=np.where(df.Close_shift11>0,df.Close_shift10/df.Close_shift11,1)
    df['Close_11_to_12']=np.where(df.Close_shift12>0,df.Close_shift11/df.Close_shift12,1)


    df['Close_0_to_MA15']=np.where(df.Close_shift0>0,df.Close_shift0/df.MA15,1)
    df['Close_1_to_MA15']=np.where(df.Close_shift1>0,df.Close_shift1/df.MA15,1)
    df['Close_2_to_MA15']=np.where(df.Close_shift2>0,df.Close_shift2/df.MA15,1)
    df['Close_3_to_MA15']=np.where(df.Close_shift3>0,df.Close_shift3/df.MA15,1)
    df['Close_4_to_MA15']=np.where(df.Close_shift4>0,df.Close_shift4/df.MA15,1)
    df['Close_5_to_MA15']=np.where(df.Close_shift5>0,df.Close_shift5/df.MA15,1)
    df['Close_6_to_MA15']=np.where(df.Close_shift6>0,df.Close_shift6/df.MA15,1)
    df['Close_7_to_MA15']=np.where(df.Close_shift7>0,df.Close_shift7/df.MA15,1)
    df['Close_8_to_MA15']=np.where(df.Close_shift8>0,df.Close_shift8/df.MA15,1)
    df['Close_9_to_MA15']=np.where(df.Close_shift9>0,df.Close_shift9/df.MA15,1)
    df['Close_10_to_MA15']=np.where(df.Close_shift10>0,df.Close_shift10/df.MA15,1)
    df['Close_11_to_MA15']=np.where(df.Close_shift11>0,df.Close_shift11/df.MA15,1)
    df['Close_12_to_MA15']=np.where(df.Close_shift12>0,df.Close_shift12/df.MA15,1)
    df['Close_13_to_MA15']=np.where(df.Close_shift13>0,df.Close_shift13/df.MA15,1)
    df['Close_14_to_MA15']=np.where(df.Close_shift14>0,df.Close_shift14/df.MA15,1)
    df['Close_15_to_MA15']=np.where(df.Close_shift15>0,df.Close_shift15/df.MA15,1)



    df['Close_0_to_3']=np.where(df.Close_shift3>0,df.Close_shift1/df.Close_shift3,1)
    df['Close_0_to_4']=np.where(df.Close_shift4>0,df.Close_shift1/df.Close_shift4,1)
    df['Close_0_to_5']=np.where(df.Close_shift5>0,df.Close_shift1/df.Close_shift5,1)
    df['Close_0_to_6']=np.where(df.Close_shift6>0,df.Close_shift1/df.Close_shift6,1)
    df['Close_0_to_9']=np.where(df.Close_shift9>0,df.Close_shift1/df.Close_shift9,1)
    df['Close_0_to_12']=np.where(df.Close_shift12>0,df.Close_shift1/df.Close_shift12,1)


    df['Close_m3_0_to_MA15']=np.where(df.MA15>0,df.Close_roll_mean3_shift0/df.MA15,1)
    df['Close_m3_1_to_MA15']=np.where(df.MA15>0,df.Close_roll_mean3_shift1/df.MA15,1)
    df['Close_m3_2_to_MA15']=np.where(df.MA15>0,df.Close_roll_mean3_shift2/df.MA15,1)
    df['Close_m3_3_to_MA15']=np.where(df.MA15>0,df.Close_roll_mean3_shift3/df.MA15,1)
    df['Close_m3_4_to_MA15']=np.where(df.MA15>0,df.Close_roll_mean3_shift4/df.MA15,1)
    df['Close_m3_5_to_MA15']=np.where(df.MA15>0,df.Close_roll_mean3_shift5/df.MA15,1)
    df['Close_m3_6_to_MA15']=np.where(df.MA15>0,df.Close_roll_mean3_shift6/df.MA15,1)
    df['Close_m3_9_to_MA15']=np.where(df.MA15>0,df.Close_roll_mean3_shift9/df.MA15,1)
    df['Close_m3_12_to_MA15']=np.where(df.MA15>0,df.Close_roll_mean3_shift12/df.MA15,1)


    df['MACDHist_corr_0_to_1']=df.MACDHist_corr_shift0-df.MACDHist_corr_shift1
    df['MACDHist_corr_1_to_3']=df.MACDHist_corr_shift1-df.MACDHist_corr_shift3
    df['MACDHist_corr_3_to_6']=df.MACDHist_corr_shift3-df.MACDHist_corr_shift6
    df['MACDHist_corr_0_to_6']=df.MACDHist_corr_shift0-df.MACDHist_corr_shift6

#     df['MACDHist_0_to_1']=np.where(df.MACDHist_shift0>0,df.MACDHist_shift0-df.MACDHist_shift1,0)
#     df['MACDHist_1_to_3']=np.where(df.MACDHist_shift3>0,df.MACDHist_shift1-df.MACDHist_shift3,0)
#     df['MACDHist_0_to_6']=np.where(df.MACDHist_shift0>0,df.MACDHist_shift0-df.MACDHist_shift6,0)
#     df['MACDHist_3_to_6']=np.where(df.MACDHist_shift6>0,df.MACDHist_shift3-df.MACDHist_shift6,0)

#     df['AweOs_0_to_1']=np.where(df.AweOs_shift1>0,df.AweOs_shift0-df.AweOs_shift1,0)
#     df['AweOs_1_to_3']=np.where(df.AweOs_shift1>3,df.AweOs_shift1-df.AweOs_shift3,0)
#     df['AweOs_3_to_6']=np.where(df.AweOs_shift1>6,df.AweOs_shift3-df.AweOs_shift6,0)

    df['AweOs_corr_0_to_1']=df.AweOs_cor_shift0-df.AweOs_cor_shift1
    df['AweOs_corr_1_to_3']=df.AweOs_cor_shift1-df.AweOs_cor_shift3
    df['AweOs_corr_3_to_6']=df.AweOs_cor_shift3-df.AweOs_cor_shift6
    df['AweOs_corr_0_to_6']=df.AweOs_cor_shift0-df.AweOs_cor_shift6


    return df



def molot(PER_OPEN,PER_CLOSE):

    # метка молота

    if PER_CLOSE>0.75 and PER_OPEN>0.75:
        return 1
    elif PER_CLOSE<0.25 and PER_OPEN<0.25:
        return -1
    else:
        return 0


def create_rel_shifts2(df):

    # относительные фичи, заготовка для формаций

    df['BENCH']=df.Close_shift0

    #для геоюнита среднего факты

    df['Close_0_to_b']=np.where(df.BENCH>0,df.Close_shift0/df.BENCH,1)
    df['Close_1_to_b']=np.where(df.BENCH>0,df.Close_shift1/df.BENCH,1)
    df['Close_2_to_b']=np.where(df.BENCH>0,df.Close_shift2/df.BENCH,1)
    df['Close_3_to_b']=np.where(df.BENCH>0,df.Close_shift3/df.BENCH,1)
    df['Close_4_to_b']=np.where(df.BENCH>0,df.Close_shift4/df.BENCH,1)
    df['Close_5_to_b']=np.where(df.BENCH>0,df.Close_shift5/df.BENCH,1)

    df['Open_0_to_b']=np.where(df.BENCH>0,df.Open_shift0/df.BENCH,1)
    df['Open_1_to_b']=np.where(df.BENCH>0,df.Open_shift1/df.BENCH,1)
    df['Open_2_to_b']=np.where(df.BENCH>0,df.Open_shift2/df.BENCH,1)
    df['Open_3_to_b']=np.where(df.BENCH>0,df.Open_shift3/df.BENCH,1)
    df['Open_4_to_b']=np.where(df.BENCH>0,df.Open_shift4/df.BENCH,1)
    df['Open_5_to_b']=np.where(df.BENCH>0,df.Open_shift5/df.BENCH,1)

    df['Low_0_to_b']=np.where(df.BENCH>0,df.Low_shift0/df.BENCH,1)
    df['Low_1_to_b']=np.where(df.BENCH>0,df.Low_shift1/df.BENCH,1)
    df['Low_2_to_b']=np.where(df.BENCH>0,df.Low_shift2/df.BENCH,1)
    df['Low_3_to_b']=np.where(df.BENCH>0,df.Low_shift3/df.BENCH,1)
    df['Low_4_to_b']=np.where(df.BENCH>0,df.Low_shift4/df.BENCH,1)
    df['Low_5_to_b']=np.where(df.BENCH>0,df.Low_shift5/df.BENCH,1)

    df['High_0_to_b']=np.where(df.BENCH>0,df.High_shift0/df.BENCH,1)
    df['High_1_to_b']=np.where(df.BENCH>0,df.High_shift1/df.BENCH,1)
    df['High_2_to_b']=np.where(df.BENCH>0,df.High_shift2/df.BENCH,1)
    df['High_3_to_b']=np.where(df.BENCH>0,df.High_shift3/df.BENCH,1)
    df['High_4_to_b']=np.where(df.BENCH>0,df.High_shift4/df.BENCH,1)
    df['High_5_to_b']=np.where(df.BENCH>0,df.High_shift5/df.BENCH,1)


    return df






def svechi(df_test):

    '''
    расчет меток разных формаций

    '''
    eps=0.0000001

    columns_list=['High_shift0', 'High_shift1', 'High_shift2',
       'High_shift3', 'High_shift4', 'High_shift5', 'High_shift6',
       'High_shift7', 'High_shift8', 'High_shift9', 'High_shift10',
       'High_shift11','Low_shift0', 'Low_shift1', 'Low_shift2',
       'Low_shift3', 'Low_shift4', 'Low_shift5', 'Low_shift6', 'Low_shift7',
       'Low_shift8', 'Low_shift9', 'Low_shift10', 'Low_shift11',
              'Open_shift0',
       'Open_shift1', 'Open_shift2', 'Open_shift3', 'Open_shift4',
       'Open_shift5', 'Open_shift6', 'Open_shift7', 'Open_shift8',
       'Open_shift9', 'Open_shift10', 'Open_shift11',
              'Close_shift0',
       'Close_shift1', 'Close_shift2', 'Close_shift3', 'Close_shift4',
       'Close_shift5', 'Close_shift6', 'Close_shift7', 'Close_shift8',
       'Close_shift9', 'Close_shift10', 'Close_shift11',
              'SV_DIR_shift0',
       'SV_DIR_shift1', 'SV_DIR_shift2', 'SV_DIR_shift3', 'SV_DIR_shift4',
       'SV_DIR_shift5', 'SV_DIR_shift6', 'SV_DIR_shift7', 'SV_DIR_shift8',
       'SV_DIR_shift9', 'SV_DIR_shift10', 'SV_DIR_shift11',
              'PER_OPEN_shift0', 'PER_OPEN_shift1', 'PER_OPEN_shift2',
       'PER_OPEN_shift3', 'PER_OPEN_shift4', 'PER_OPEN_shift5',
       'PER_OPEN_shift6', 'PER_OPEN_shift7', 'PER_OPEN_shift8',
       'PER_OPEN_shift9', 'PER_OPEN_shift10', 'PER_OPEN_shift11',
              'PER_CLOSE_shift0', 'PER_CLOSE_shift1',
       'PER_CLOSE_shift2', 'PER_CLOSE_shift3', 'PER_CLOSE_shift4',
       'PER_CLOSE_shift5', 'PER_CLOSE_shift6', 'PER_CLOSE_shift7',
       'PER_CLOSE_shift8', 'PER_CLOSE_shift9', 'PER_CLOSE_shift10',
       'PER_CLOSE_shift11',
              'type_molot', 'type_molot_shift0', 'type_molot_shift1',
       'type_molot_shift2', 'type_molot_shift3', 'type_molot_shift4',
       'type_molot_shift5', 'type_molot_shift6', 'type_molot_shift7',
       'type_molot_shift8', 'type_molot_shift9', 'type_molot_shift10',
       'type_molot_shift11','ROWNUM','date_for_ind' #'target_var4_up','target_var4_dw',


             ]


    df_orig=df_test[columns_list].copy()

    df_orig['EVENT1'] = 0
    df_orig['EVENT2'] = 0
    df_orig['EVENT3'] = 0
    df_orig['EVENT4'] = 0
    df_orig['EVENT5'] = 0
    df_orig['EVENT6'] = 0
    df_orig['EVENT7'] = 0
    df_orig['EVENT8'] = 0
    df_orig['EVENT9'] = 0
    df_orig['EVENT10'] = 0
    df_orig['EVENT11'] = 0
    df_orig['EVENT12'] = 0
    df_orig['EVENT13'] = 0
    df_orig['EVENT14'] = 0
    df_orig['EVENT15'] = 0
    df_orig['EVENT16'] = 0
    df_orig['EVENT17'] = 0
    df_orig['EVENT18'] = 0
    df_orig['EVENT19'] = 0
    df_orig['EVENT20'] = 0
    df_orig['EVENT21'] = 0
    df_orig['EVENT22'] = 0
    df_orig['EVENT23'] = 0
    df_orig['EVENT24'] = 0
    df_orig['EVENT25'] = 0


    for index1, row1 in df_orig.iterrows():

        #print(row1.type_molot)

        cur_row=row1['ROWNUM']

        #бычий молот
        if row1.SV_DIR_shift0==1 and row1.SV_DIR_shift1==1 and row1.SV_DIR_shift2==-1 and row1.SV_DIR_shift3==-1\
         and row1.type_molot_shift1!=0:
            event1=1
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT1'] = event1
        else:
            event1=0

        if row1.SV_DIR_shift0==1 and row1.SV_DIR_shift1==-1 and row1.SV_DIR_shift2==-1 and row1.SV_DIR_shift3==-1\
         and row1.type_molot_shift1!=0:
            event2=1
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT2'] = event2
        else:
            event2=0

        ######################################### Комбы на рост  #################################

         # бычье поглощение
        if row1.SV_DIR_shift0==1 and row1.SV_DIR_shift1==1 and row1.SV_DIR_shift2==-1 and row1.SV_DIR_shift3==-1\
        and row1.High_shift1>row1.High_shift2 and row1.Low_shift1<row1.Low_shift2:
            event9=1
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT9'] = event9
        else:
            event9=0

        # бычье поглощение  cut version
        if row1.SV_DIR_shift0==1 and row1.SV_DIR_shift1==-1\
        and row1.High_shift0>row1.High_shift1 and row1.Low_shift0<row1.Low_shift1:
            event10=1
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT10'] = event10
        else:
            event10=0

        # нижний молот

        if row1.SV_DIR_shift2==-1 and row1.type_molot_shift1!=0 and row1.SV_DIR_shift0==1 :
            event7=1
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT7'] = event7
        else:
            event7=0


    #      # просвет в облаках
    #     if row1.SV_DIR_shift0==1 and row1.SV_DIR_shift1==-1\
    #     and row1.High_shift0<row1.High_shift1 and row1.Low_shift0<row1.Low_shift1 and row1.Close_shift0<row1.Open_shift1:
    #         event11=1
    #         df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT11'] = event11
    #     else:
    #         event4=0

        # просвет в облаках
        if row1.SV_DIR_shift1==1 and row1.SV_DIR_shift2==-1 and row1.SV_DIR_shift0==1\
        and row1.High_shift1<row1.High_shift2 and row1.Low_shift1<row1.Low_shift2 and row1.Close_shift1<row1.Open_shift2:
            event11=1
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT11'] = event11
        else:
            event11=0


        # пинцет снизу, донья пинцета
        # and row1.SV_DIR_shift2==-1
        if row1.SV_DIR_shift0==1 and row1.SV_DIR_shift1==-1\
        and row1.PER_CLOSE_shift0<0.5 and row1.PER_CLOSE_shift1<0.5:

            event12=1
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT12'] = event12
        else:
            event12=0


        # 3 белых солдата
        # and row1.SV_DIR_shift2==-1
        if row1.SV_DIR_shift0==1 and row1.SV_DIR_shift1==1 and row1.SV_DIR_shift2==1\
        and row1.Close_shift1>row1.Close_shift2 and row1.Close_shift0>row1.Close_shift1\
        and row1.Open_shift0>row1.Open_shift1 and  row1.Open_shift1>row1.Open_shift2:

            event13=1
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT13'] = event13
        else:
            event13=0

        # утренняя звезда
        #and row1.SV_DIR_shift1==1

        if row1.SV_DIR_shift0==1  and row1.SV_DIR_shift2==-1\
        and row1.PER_CLOSE_shift0-row1.PER_OPEN_shift0>0.35 and row1.PER_OPEN_shift2-row1.PER_CLOSE_shift2>0.35:
        #and (row1.High_shift1-row1.Low_shift1)/(row1.High_shift2-row1.Low_shift2)<1:
        #and row1.Open_shift0>row1.Open_shift1 and  row1.Open_shift1>row1.Open_shift2:

            event15=1
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT15'] = event15
        else:
            event15=0

         # бычий харами
        #and row1.SV_DIR_shift1==1

    #     if row1.SV_DIR_shift0==1  and row1.SV_DIR_shift1==-1\
    #     and row1.Open_shift0>row1.Open_shift0 and row1.PER_OPEN_shift2-row1.PER_CLOSE_shift2>0.35:
    #     #and (row1.High_shift1-row1.Low_shift1)/(row1.High_shift2-row1.Low_shift2)<1:
    #     #and row1.Open_shift0>row1.Open_shift1 and  row1.Open_shift1>row1.Open_shift2:

    #         event17=1
    #         df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT15'] = event17
    #     else:
    #         event17=0

    # двойной толчек


        if row1.SV_DIR_shift0==1 and row1.SV_DIR_shift1==-1 and row1.SV_DIR_shift2==1 and row1.SV_DIR_shift3==-1\
        and row1.Low_shift2<row1.Low_shift3 and row1.Low_shift1<row1.Low_shift2:


            event18=1
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT18'] = event18
        else:
            event18=0



        # пинцет снизу2, донья пинцета
        # and row1.SV_DIR_shift2==-1
        if row1.SV_DIR_shift0==1 and row1.SV_DIR_shift1==-1 and row1.SV_DIR_shift2==-1\
        and row1.Low_shift1-row1.Low_shift2!=0\
        and math.fabs(row1.Low_shift0-row1.Low_shift1)/math.fabs(row1.Low_shift1-row1.Low_shift2+eps)<0.8:

            event19=1
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT19'] = event19
        else:
            event19=0

        # много лоу, рост
        if row1.SV_DIR_shift0==1 and row1.SV_DIR_shift1==-1 and row1.SV_DIR_shift1==-1\
        and row1.SV_DIR_shift2==-1 and row1.SV_DIR_shift3==-1 and row1.SV_DIR_shift4==-1\
        and row1.Low_shift1<row1.Low_shift2 and row1.Low_shift2<row1.Low_shift3\
        and row1.Low_shift3<row1.Low_shift4:

            event21=1
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT21'] = event21
        else:
            event21=0


        ###################################### Комбы на снижение ##############################

         # верхгний молот

        if row1.SV_DIR_shift2==1 and row1.type_molot_shift1!=0 and row1.SV_DIR_shift0==-1 :
            event8=1
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT8'] = event8
        else:
            event8=0



        # медвежье поглощение
    #     if row1.SV_DIR_shift0==-1 and row1.SV_DIR_shift1==-1 and row1.SV_DIR_shift2==1 and row1.SV_DIR_shift3==1\
    #     and row1.High_shift1>row1.High_shift2 and row1.Low_shift1<row1.Low_shift2:
    #         event3=1
    #         df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT3'] = event3
    #     else:
    #         event3=0

        # медвежье поглощение 2
        if row1.SV_DIR_shift0==-1 and row1.SV_DIR_shift1==1\
        and row1.High_shift0>row1.High_shift1 and row1.Low_shift0<row1.Low_shift1:
            event3=1
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT3'] = event3
        else:
            event3=0


    #     # темная завеса
    #     if row1.SV_DIR_shift0==-1 and row1.SV_DIR_shift1==-1 and row1.SV_DIR_shift2==1 and row1.SV_DIR_shift3==1\
    #     and row1.High_shift1>row1.High_shift2 and row1.Open_shift1<row1.Close_shift2:
    #         event4=1
    #         df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT4'] = event4
    #     else:
    #         event4=0

        # темная завеса
        if row1.SV_DIR_shift0==-1 and row1.SV_DIR_shift1==1\
        and row1.High_shift0>row1.High_shift1 and row1.Low_shift0>row1.Low_shift1 and row1.Close_shift0>row1.Open_shift1:
            event4=1
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT4'] = event4
        else:
            event4=0

        # крепость сверху
        if row1.SV_DIR_shift0==-1 and row1.SV_DIR_shift1==1 and row1.SV_DIR_shift2==-1\
        and row1.SV_DIR_shift3==1 and row1.SV_DIR_shift4==1 and row1.Close_shift1<row1.High_shift0 \
        and row1.Open_shift1>row1.Close_shift0\
        and row1.Close_shift1< row1.High_shift3 and row1.Close_shift1< row1.High_shift0\
        and row1.Open_shift2< row1.High_shift3 and row1.Open_shift2< row1.High_shift0\
        and row1.Open_shift1> row1.Open_shift3 and row1.Open_shift1> row1.Close_shift0\
        and row1.Close_shift2> row1.Open_shift3 and row1.Close_shift2> row1.Close_shift0:

            event5=1
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT5'] = event5
        else:
            event5=0


        # пинцет сверху
        if row1.SV_DIR_shift0==-1 and row1.SV_DIR_shift1==1 and row1.SV_DIR_shift2==1\
        and row1.PER_CLOSE_shift0<0.5 and row1.PER_CLOSE_shift1<0.5:

            event6=1
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT6'] = event6
        else:
            event6=0


        # 3 вороны
        # and row1.SV_DIR_shift2==-1
        if row1.SV_DIR_shift0==-1 and row1.SV_DIR_shift1==-1 and row1.SV_DIR_shift2==-1\
        and row1.Close_shift1<row1.Close_shift2 and row1.Close_shift0<row1.Close_shift1\
        and row1.Open_shift0<row1.Open_shift1 and  row1.Open_shift1<row1.Open_shift2:

            event14=1
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT14'] = event14
        else:
            event14=0

        #вечерняя звезда

        if row1.SV_DIR_shift0==-1  and row1.SV_DIR_shift2==1\
        and row1.PER_CLOSE_shift0-row1.PER_OPEN_shift0<0.3 and row1.PER_OPEN_shift2-row1.PER_CLOSE_shift2<0.3\
        and (row1.High_shift1-row1.Low_shift1)/(row1.High_shift0-row1.Low_shift0+eps)<1:
        #and row1.Open_shift0>row1.Open_shift1 and  row1.Open_shift1>row1.Open_shift2:

            event16=1
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT16'] = event16
        else:
            event16=0


        # пинцет сверху 2, донья пинцета
        # and row1.SV_DIR_shift2==-1
        if row1.SV_DIR_shift0==-1 and row1.SV_DIR_shift1==1 and row1.SV_DIR_shift2==1\
        and row1.High_shift1-row1.High_shift2!=0\
        and math.fabs(row1.High_shift0-row1.High_shift1)/math.fabs(row1.High_shift1-row1.High_shift2+eps)<0.9:

            event20=1
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT20'] = event20
        else:
            event20=0


       # много лоу, рост
        if row1.SV_DIR_shift0==-1 and row1.SV_DIR_shift1==1 and row1.SV_DIR_shift1==1\
        and row1.SV_DIR_shift2==1 and row1.SV_DIR_shift3==1 and row1.SV_DIR_shift4==1\
        and row1.High_shift1>row1.High_shift2 and row1.High_shift2>row1.High_shift3\
        and row1.High_shift3>row1.High_shift4:

            event22=1
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'EVENT22'] = event22
        else:
            event22=0



        #cur_row=row1['ROWNUM']
    return df_orig







def std_border(data,num_row):

    '''
    Это расчет границ для обучения. Смысл в том, что в разные периоды разная валатильность (а многие индексы не чувствительны,
    к примеру RCI или MACD). Поэтому мы смотрим текущее значение std_500 и берем 80% дата сета, наиболее близкое к этому std_500
    На практике, при низкой валатильности, отсекаем экстримальные значения сверху, и наоборот.

    '''

    std_moment=data[data.ROW_NUM==num_row].std_500_rel.values[0]
    shape_base=data.shape[0]

    i = 0.01
    while data[(data.std_500_rel>std_moment-i)&(data.std_500_rel<std_moment+i)].shape[0]/shape_base<0.8:
        #print(i)
        i = i + 0.001

    r_border = std_moment+i
    l_border = std_moment-i
    if l_border<0:
        l_border=0

    return l_border,r_border


def opt_f(x,am, al, om, fa):
    return 1*np.exp(-al*x)*np.cos(om*x+fa)



def segmoid_predict(data,windows):

    df_orig=data[['Close','ROWNUM','date_for_ind']].copy()


    df_orig['down']=0
    df_orig['up']=0
    df_orig['mae_opt']=0
    down=0
    up=0
    mae_opt2=0

    for index1, row1 in df_orig.iterrows():

        cur_row=row1['ROWNUM']



        #print(cur_row)

        if cur_row<=np.max(windows):

            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'down'] = 0
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'up'] = 0
            df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'mae_opt'] = 0


        else:

            res=[]

            mae_opt=999999

            for w in windows:

                df=df_orig[(df_orig.ROWNUM>cur_row-w)&(df_orig.ROWNUM<=cur_row)]
                df['ROWNUM_LOC'] = df['ROWNUM'].rank(method='min')

                avg_value=df.Close.mean()
                std=df.Close.std()
                #max_value=df.Close.max()
                #min_value=df.Close.min()
                #delta=max_value-min_value




                #print(avg_value,std)

                df['Close_norm']=(df.Close-avg_value)/std

                model = LinearRegression()
                x=df.ROWNUM_LOC.values.reshape(-1, 1)
                y=df.Close_norm.values.reshape(-1, 1)
#                 print(df)
#                 print(x)
#                 print(y)
                model.fit(x, y)
                df['line'] = model.predict(x)
                df['Close_norm2']=df['Close_norm']-df['line']

            #     df['Close_norm'].plot()
            #     df['Close_norm2'].plot()
            #     df['line'].plot()

                xdata=df.ROWNUM_LOC.values#.reshape(-1, 1)
                ydata=df.Close_norm2.values#.reshape(-1, 1)

                try:
                    popt, pcov = curve_fit(opt_f, xdata, ydata,maxfev=1000)
                except RuntimeError:
                    popt=[1,0,1,0]


                Amp=1#popt[0]
                alfa=popt[1]
                omega=popt[2]
                faze=popt[3]

                df['aproks']=Amp*np.exp(-alfa*df.ROWNUM_LOC)*np.cos(omega*df.ROWNUM_LOC+faze)

                df['dif2']=(df.Close_norm2-df.aproks)**2

                mae_norm2=df['dif2'].sum()/df.shape[0]


                if mae_norm2<mae_opt:
                    mae_opt=mae_norm2
                    mae_opt2=mae_norm2
                    Amp_opt=1#popt[0]
                    alfa_opt=popt[1]
                    omega_opt=popt[2]
                    faze_opt=popt[3]
                    w_opt=w
                    model_opt=model
                    avg_value_opt=avg_value
                    std_opt=std
                    df_opt=df[['ROWNUM_LOC','ROWNUM','line','Close_norm2','aproks','Close_norm','Close']].copy()

            #print(w_opt,Amp_opt,alfa_opt,omega_opt,faze_opt,mae_opt)

            df=df_opt


            df['aproks2']=df['aproks']+df['line']

#             df['Close_norm'].plot()
#             #df['Close_norm2'].plot()
#             df['aproks2'].plot()
#             #df['aproks'].plot()




            df_prom=df[['ROWNUM_LOC','Close']].copy()


            last_v=df_prom.tail(1).Close.values[0]

            max_r=int(df['ROWNUM_LOC'].max())
            new_r=range(max_r+1,max_r+10)


            rownums = pd.DataFrame(new_r)
            rownums=rownums.rename(columns={0: 'ROWNUM_LOC'})
            rownums['Close']=-1

            df_prom = pd.concat([df_prom, rownums]).reset_index(drop=True)
            x=df_prom.ROWNUM_LOC.values.reshape(-1, 1)
            df_prom['line'] = model_opt.predict(x)

            df_prom['aproks']=Amp_opt*np.exp(-alfa_opt*df_prom.ROWNUM_LOC)*np.cos(omega_opt*df_prom.ROWNUM_LOC+faze_opt)
            df_prom['aproks2']=df_prom['aproks']+df_prom['line']

            df_prom['Close_vost']=(df_prom['aproks2'])*std+avg_value

            min_f=df_prom[df_prom['ROWNUM_LOC']>max_r]['Close_vost'].min()
            max_f=df_prom[df_prom['ROWNUM_LOC']>max_r]['Close_vost'].max()



            if last_v>min_f and last_v>max_f:
                down=min_f/last_v-1
                up=0
            elif last_v<min_f and last_v<max_f:
                down=0
                up=max_f/last_v-1
            else:
                down=min_f/last_v-1
                up=max_f/last_v-1



        df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'down'] = down
        df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'up'] = up
        df_orig.loc[(df_orig['ROWNUM'] == cur_row), 'mae_opt'] = mae_opt2


    return df_orig



def unic_date(timestamp):
    timestamp=str(timestamp)

    timestamp=int(timestamp[:-3])
    #value = datetime.datetime.fromtimestamp(timestamp)
    value = datetime.fromtimestamp(timestamp)
    new_date=value.strftime('%Y-%m-%d %H:%M:%S')
    return new_date



def event_freaq(df,first_row_num,period,direct,event_type,par,par2):


    '''

     получение категории роста или падения на period свечей вперед

     par - параметр шагов, на сколько у нас таргентная переменная шагает вперед
     par2 - на сколько процентов.

     Т.е. таргет 4 и 0.03 будет per и par2


    '''



    list_var=['High', 'Low', 'Open', 'Close', 'Volume','ROW_NUM','target_var4_up','target_var4_dw']

    first_row_num=int(first_row_num)

    if first_row_num<=period+par:

        #df=df[:first_row_num-par][list_var]
        df = df[df.ROW_NUM <= first_row_num - par]

    else:

        #df=df[first_row_num-period-par:first_row_num-par][list_var]
        df = df[(df.ROW_NUM > first_row_num - par - period) & (df.ROW_NUM <= first_row_num - par)][list_var]




    shape = df.shape[0]

    sum_up=df.target_var4_up.sum()
    sum_dw=df.target_var4_dw.sum()

    freq_up=sum_up/shape

    freq_dw=sum_dw/shape




    df['Close_1']=df['Close'].shift(1).values
    df['High_1']=df['High'].shift(1).values
    df['Low_1']=df['Low'].shift(1).values
    df['target_var4_up_1']=df['target_var4_up'].shift(1).values
    df['target_var4_dw_1']=df['target_var4_dw'].shift(1).values


    df['Chain_up']=df['target_var4_up']

    df['Chain_up']=np.where((df['target_var4_up']==1)\
                                 &(df['target_var4_up_1']==1)\
                                 &(df['High']/df['Close_1']<1+par2),0,df['Chain_up'])


    df['Chain_dw']=df['target_var4_dw']

    df['Chain_dw']=np.where((df['target_var4_dw']==1)\
                                 &(df['target_var4_dw_1']==1)\
                                 &(df['Close_1']/df['Low']<1+par2),0,df['Chain_dw'])


    sum_up_ev=df.Chain_up.sum()
    sum_dw_ev=df.Chain_dw.sum()

    freq_up_event=sum_up_ev/shape

    freq_dw_event=sum_dw_ev/shape


    if direct=='up' and event_type=='all':
        return freq_up
    elif direct=='up' and event_type=='chain':
        return freq_up_event
    elif direct=='dw' and event_type=='all':
        return freq_dw
    elif direct=='dw' and event_type=='chain':
        return freq_dw_event

#import datetime
#agregate_4h_first['new_data'] = agregate_4h_first.apply(lambda x: unic_date(x.date_for_ind),axis=1)




def prec_dict(df,gbm,current_row,min_row,max_row,y_name,col_list,params,window,use_cut=0):

    '''

    функция, которая возвращает словарь, в котором описаны вероятности успеха, по каждому скору
    параметры:
    df - дата фрейм
    current_row - для какой строки считаем
    min_row - от какой строки вообще смотрим
    max_row - обычно совпадает с текущей

    direct - 'up'/'down'
    col_list - текущий набор фичей, для которого считаем
    params_opt_dw - словарь параметров для модели
    window - окно, какими кусками берем. Для 1H фрейма 3000-4000, для 4H - 1000
    чтобы получить 5-10 батчей


    '''



    # получить базовые границы

    #bord_low,bord_high=std_border_activity(df,current_row)

    if use_cut==1:

        if y_name =='target_var4_dw':
            bord_low,bord_high=std_border_activity(df,current_row,'freq_dw_all_300',sh=0.8)
            var_bord='freq_dw_all_300'

        elif y_name =='target_var4_up':
            bord_low,bord_high=std_border_activity(df,current_row,'freq_up_all_300',sh=0.8)
            var_bord='freq_up_all_300'
        else:
            bord_low=0
            bord_high=1

    else:

        if y_name =='target_var4_dw':
            var_bord='freq_dw_all_300'
            bord_low=0
            bord_high=1

        elif y_name =='target_var4_up':
            var_bord='freq_up_all_300'
            bord_low=0
            bord_high=1
        else:
            bord_low=0
            bord_high=1



        bord_low=0
        bord_high=1


    #bord_low=0
    #bord_high=1

    #print(bord_low,bord_high)

    if use_cut==1:
        mask_time = (df.ROW_NUM>min_row) & (df.ROW_NUM<max_row)
        mask_activity = (df[var_bord]>=bord_low) & (df[var_bord]<=bord_high)

        mask=mask_time&mask_activity
    else:
        mask_time = (df.ROW_NUM>min_row) & (df.ROW_NUM<max_row)
        mask=mask_time

#     total_cnt=sum(mask)

    X= df[mask].copy()
    X.reset_index(drop=True, inplace=True)
    X['NEW_ROW_NUM']=X.index
    # оставить только релевантные по граничным датам и интенсивности

    #print(X)


    kol_iter = X.shape[0]//1000
    #print(kol_iter)
    dict_prec={}
    REZ3 = pd.DataFrame(columns=['scor_cor','roll_prec','recall','iter'])

    cores=range(501,X.shape[0]-window//2,window//2)

    #print(list(cores))

    for core in cores:


        mask_test = (X.NEW_ROW_NUM>core-window//2) & (X.NEW_ROW_NUM<core+window//2)

        mask_train = ~mask_test

        X_train= X[mask_train][col_list]
        X_test= X[mask_test][col_list]

        y_train = X[mask_train][y_name]
        y_test = X[mask_test][y_name]

#         if direct=='up':
#             y_train = X[mask_train][y_name]
#             y_test = X[mask_test][y_name]
#         else:
#             y_train = X[mask_train][y_name]
#             y_test = X[mask_test][y_name]

        #gbm =lgb.LGBMClassifier(**params)
        gbm.fit(X_train,y_train)

        #roc_auc=roc_auc_score(y_test,gbm.predict_proba(X_test)[:,1])


        y_pred=gbm.predict_proba(X_test)[:,1]
        precision, recall, thresholds = precision_recall_curve(y_test, y_pred)
        #roc_auc=roc_auc_score(y_test,gbm.predict_proba(X_test)[:,1])

        #print(core,roc_auc)

        #print(thresholds)
        REZ = pd.DataFrame()
        REZ['precision'] = precision[:-1]
        REZ['recall'] = recall[:-1]
        REZ['thresholds'] = thresholds
        REZ['thresholds_r'] = round(REZ['thresholds'],2)
        REZ['roll_prec'] = REZ['precision'].rolling(window=50,min_periods=1,center = True).mean()
        REZ['precision_start']=REZ.loc[0].roll_prec

        REZ=REZ[REZ['roll_prec']>REZ['precision_start']]

        j=range(1,100)

        pivot_1=REZ[['thresholds_r','roll_prec','recall']].pivot_table(
            values=["roll_prec",'recall'], index=["thresholds_r"], aggfunc="mean")

        pivot_1['scor_cor']=pivot_1.index
        pivot_1['iter']=core

        REZ2 = pd.DataFrame()

        REZ2['scor']=j
        REZ2['scor_cor']=REZ2['scor']/100

        REZ2=pd.merge(REZ2, pivot_1,on=['scor_cor'], how='left')

        REZ2=REZ2.interpolate()
        REZ2=REZ2.bfill()

        #REZ2.roll_prec.plot(figsize=(25,7))

        REZ3=pd.concat([REZ3, REZ2[['scor_cor','roll_prec','recall','iter']]])


    #print(REZ3)


    pivot_rec=REZ3[['scor_cor','recall','iter']].pivot_table(
            values=["recall"],columns=['iter'], index=["scor_cor"], aggfunc="mean")


    pivot_rec['sum_all']=pivot_rec.sum(axis=1)

    #print(pivot_rec)

    for j in pivot_rec.columns:
        pivot_rec[j]=pivot_rec[j]/pivot_rec['sum_all']

    pivot_rec =pivot_rec.drop(['sum_all'], 1)


    #print(pivot_rec)

    pivot_rec2=pivot_rec.unstack().reset_index().rename(columns={0: 'Weight'})
    #df_bs2 =df_bs2.drop(['level_0'], 1)
    #print(pivot_rec2)

    REZ3=pd.merge(REZ3, pivot_rec2[['scor_cor','iter','Weight']],on=['scor_cor','iter'], how='left')

    REZ3['w_roll_prec']=REZ3["roll_prec"]*REZ3["Weight"]
    #print(REZ3)

    pivot_2=REZ3[['scor_cor','roll_prec','w_roll_prec']].pivot_table(
            values=["w_roll_prec"], index=["scor_cor"], aggfunc="sum")

#     pivot_2=REZ3[['scor_cor','roll_prec','w_roll_prec']].pivot_table(
#              values=["roll_prec"], index=["scor_cor"], aggfunc="mean")

    pivot_2['scor_cor2']=pivot_2.index


    for index1, row1 in pivot_2.iterrows():
        #dict_prec[row1['scor_cor2']]=row1['roll_prec']
        dict_prec[row1['scor_cor2']]=row1['w_roll_prec']

    #pivot_2.roll_prec.plot(figsize=(20,7))

    #REZ3.to_csv('dt_20210720_REZ3_1.csv', index=True)


    return dict_prec





def usil(X,y,par_1,par_2):
    '''
    функция усиливает выборку на последние значения
    par_1 - это % (к примеру 0.1) который нужно сделать x3
    par_2 - это % (к примеру 0.3) который нужно сделать x2. Считается, как 0.3 - 0.1 = 0.2 т.е. 20% после первых 10%

    '''

    red_part=1-par_1
    yellow_part=1-par_2

    last_df=X.loc[X.shape[0]*red_part:]
    prev_df=X.loc[X.shape[0]*yellow_part:X.shape[0]*red_part]
    X_new=pd.concat([X, last_df,last_df,prev_df])

    last_df=y.loc[y.shape[0]*red_part:]
    prev_df=y.loc[y.shape[0]*yellow_part:y.shape[0]*red_part]

    y_new=pd.concat([y, last_df,last_df,prev_df])

    return X_new,y_new


def roc_auc_curve(y_test,X_test,clf,min_sc=5,max_sc=80):

    REZ = pd.DataFrame()
    REZ['Y_test'] = y_test
    REZ['Y_test'] = np.where(REZ['Y_test']==1,1,0)
    REZ['probab_CK'] = clf.predict_proba(X_test)[:,1]
    REZ['Y_predict_0.5'] = clf.predict(X_test)



    Thrs = []
    Precs = []
    Recs = []

    ls_sc=[]
    for i in range(min_sc,max_sc,5):
        ls_sc.append(i/100)

    #for score in [0.05,0.1,0.15,0.2,0.25,0.3,0.35, 0.4, 0.45, 0.5, 0.55, 0.6,0.65,0.7,0.75,0.80]:
    #print(ls_sc)
    for score in ls_sc:

        #print('точность: ', 100* REZ[(REZ['probab_CK']>=score) & (REZ['Y_test']==1)].shape[0]/REZ[REZ['probab_CK']>=score].shape[0])
        #print('полнота: ', 100* REZ[(REZ['probab_CK']>=score) & (REZ['Y_test']==1)].shape[0]/REZ[REZ['Y_test']==1].shape[0])
        Thrs.append(score)
        Precs.append(100* REZ[(REZ['probab_CK']>=score) & (REZ['Y_test']==1)].shape[0]/REZ[REZ['probab_CK']>=score].shape[0])
        Recs.append(100* REZ[(REZ['probab_CK']>=score) & (REZ['Y_test']==1)].shape[0]/REZ[REZ['Y_test']==1].shape[0])


    Prec_Rec_Thr = pd.DataFrame({'thr': Thrs,'prec': Precs,'rec': Recs})
    Prec_Rec_Thr['thr'] = np.round(Thrs,2)
    Prec_Rec_Thr['prec'] = np.round(Precs,2)
    Prec_Rec_Thr['rec'] = np.round(Recs,2)
    print(Prec_Rec_Thr)

    plt.figure(figsize=(13,8))
    plt.plot(Prec_Rec_Thr['thr'], Prec_Rec_Thr['prec'], 'rx', Prec_Rec_Thr['thr'], Prec_Rec_Thr['rec'], 'b+', linestyle='solid')
    sns.set(font_scale=2)
    plt.legend(['точность', 'полнота'], loc='upper center', shadow=True)
    sns.set(font_scale=1)
    for i,j in zip(Prec_Rec_Thr['thr'] ,Prec_Rec_Thr['prec']):
        plt.annotate(str(j),xy=(i,j))
    for i,j in zip(Prec_Rec_Thr['thr'] ,Prec_Rec_Thr['rec']):
        plt.annotate(str(j),xy=(i,j))
    sns.set(font_scale=2)
    plt.xlabel('порог(score)')
    plt.show()
    return 1




def std_border_activity(data,num_row,var,sh=0.8):

    '''
    Это расчет границ для обучения. Смысл в том, что в разные периоды разная валатильность (а многие индексы не чувствительны,
    к примеру RCI или MACD). Поэтому мы смотрим текущее значение переменной var и берем 80% дата сета, наиболее близкое к текущуем
    значению
    На практике, при низкой валатильности, отсекаем экстримальные значения сверху, и наоборот.

    '''

    std_moment=data[data.ROW_NUM==num_row][var].values[0]
    shape_base=data.shape[0]

    #print(std_moment)

    i = 0.01
    while data[(data[var]>std_moment-i)&(data[var]<std_moment+i)].shape[0]/shape_base<sh:
        #print(i)
        i = i + 0.001

    r_border = std_moment+i
    l_border = std_moment-i
    if l_border<0:
        l_border=0

    return l_border,r_border


def dynamic_stop(PRICE_START, TYPE_DEAL, shift_stop, shift_check, first_stop, first_check):
    '''
    На вход:
    генерация таблицы со скользящими тейками/стопами/чекпоинтами
    Передается стартовая цена (при входе в сделку)
    Типа сделки "up"/"dw"
    и параметры скользяешего стопа
    На выходе:
    готовая таблица с конкретными значениями STOP/CHEKPOINT/TAKE
    '''


    start_stop = -0.022
    start_take = 0.1
    start_check = -1

    list_check=[]
    list_take=[]
    list_stop=[]

    list_check.append(start_check)
    list_take.append(start_take)
    list_stop.append(start_stop)

    next_stop = first_stop
    next_check = first_check

    list_check.append(next_check)
    list_take.append(start_take)
    list_stop.append(next_stop)

#     next_stop = 0.0125
#     next_check = 0.0135

#     list_check.append(next_check)
#     list_take.append(start_take)
#     list_stop.append(next_stop)




    for i in range(1,30):
        check_new = next_check+i*shift_check
        stop_new = next_stop+i*shift_stop
        if check_new>start_take:
            take_new = check_new+0.01
        else:
            take_new = start_take

        list_check.append(check_new)
        list_take.append(take_new)
        list_stop.append(stop_new)

    data = {'CHEKPOINT': list_check, 'STOP': list_stop,'TAKE': list_take}


    df = pd.DataFrame(data)

    df.sort_values(by=['CHEKPOINT'], ascending=False, inplace=True)

    if TYPE_DEAL == 'up':


        df['PRICE_CHECK']=(df['CHEKPOINT']+1)*PRICE_START
        df['PRICE_STOP']=(df['STOP']+1)*PRICE_START
        df['PRICE_TAKE']=(df['TAKE']+1)*PRICE_START
        df[f'PRICE_CHECK_SH1']=df[f'PRICE_CHECK'].shift(1).values

        df[f'PRICE_CHECK_SH1']=df[f'PRICE_CHECK_SH1'].fillna(9999999)

    elif TYPE_DEAL == 'dw':

        df['PRICE_CHECK']=(1-df['CHEKPOINT'])*PRICE_START
        df['PRICE_STOP']=(1-df['STOP'])*PRICE_START
        df['PRICE_TAKE']=(1-df['TAKE'])*PRICE_START
        df[f'PRICE_CHECK_SH1']=df[f'PRICE_CHECK'].shift(1).values
        df[f'PRICE_CHECK_SH1']=df[f'PRICE_CHECK_SH1'].fillna(0)




    return df


def check_find(TYPE_DEAL, PRICE_CURRENT, df_shift_loc):
    '''
    функция возвращает новый чекпоинт, стоп и тейк по таблице
    df_shift_loc - это результат работы функции dynamic_stop2

    на вход:
    Типа сделки "up"/"dw"
    Текущая цена
    Таблица от dynamic_stop2

    '''

    if TYPE_DEAL == 'up':
        for index1, row1 in df_shift_loc.iterrows():
            if PRICE_CURRENT >= row1['PRICE_CHECK'] and PRICE_CURRENT < row1['PRICE_CHECK_SH1']:
                return row1['PRICE_CHECK'], row1['PRICE_STOP'], row1['PRICE_TAKE']

    elif TYPE_DEAL == 'dw':
        for index1, row1 in df_shift_loc.iterrows():
            if PRICE_CURRENT <= row1['PRICE_CHECK'] and PRICE_CURRENT > row1['PRICE_CHECK_SH1']:
                return row1['PRICE_CHECK'], row1['PRICE_STOP'], row1['PRICE_TAKE']


def find_corr_stop(df,row_n,window,step,direct,regime,q=0.5):

    '''

    Поиск тейка и стопа, исходя из динамики n свечей предыдущих

    для сделок LONG
    take_r=find_corr_stop(df_4G_model2,num_row,10,5,'dw','mean',q=0.8)
    stop_r=find_corr_stop(df_4G_model2,num_row,10,5,'up','quantile',q=0.8)
    для сделок SHORT
    take_r=find_corr_stop(df_4G_model2,num_row,10,5,'up','mean',q=0.8)
    stop_r=find_corr_stop(df_4G_model2,num_row,10,5,'dw','quantile',q=0.8)


    '''

    list_var=['High', 'Low', 'Open', 'Close', 'Volume','ROW_NUM']

    mask=(df.ROW_NUM>=row_n-window)&(df.ROW_NUM<=row_n)
    df_loc=df[mask][list_var]
    if df_loc.shape[0]<5:
        return 0.015
    if direct=='up':
        df_loc['rol_low'] = df_loc['Low'].rolling(window=step,min_periods=1).min()
        df_loc['rol_low_shif']=df_loc['rol_low'].shift(-step+1)
        df_loc['Close_rel']=df_loc['Close']/df_loc['rol_low_shif']-1
        if regime=='mean':
            stop=df_loc['Close_rel'].mean()
            #return stop_low
        if regime=='quantile':
            stop=df_loc['Close_rel'].quantile(q)
            #return stop_low
    elif direct == 'dw':
        df_loc['rol_high'] = df_loc['High'].rolling(window=step,min_periods=1).max()
        df_loc['rol_high_shif']=df_loc['rol_high'].shift(-step+1)
        df_loc['Close_rel']=df_loc['rol_high_shif']/df_loc['Close']-1
        if regime=='mean':
            stop=df_loc['Close_rel'].mean()
            #return stop_high
        if regime=='quantile':
            stop=df_loc['Close_rel'].quantile(q)
            #return stop_high
    if stop<0.015: #0.015
        return 0.015 #0.015
    elif stop>0.08:
        return 0.08
    else:
        return stop

def model_check(window,current_row,df,gbm_dw,gbm_up,y_up,y_dw):

    step=3


    mask=(df.ROW_NUM<=current_row-step)&(df.ROW_NUM>current_row-window-step)
    df_loc=df[mask].copy()

    print(df[mask].ROW_NUM.min(),df[mask].ROW_NUM.max())

    if df_loc.shape[0]<window:
        return 0.2

    X_test=df_loc[config_btc.col_fin_dw_1h]
    y_test = df_loc[y_dw]

    score_dw_do=average_precision_score(y_test, gbm_dw.predict_proba(X_test)[:,1])

    X_test=df_loc[config_btc.col_fin_up_1h]
    y_test = df_loc[y_up]

    score_up_do=average_precision_score(y_test, gbm_up.predict_proba(X_test)[:,1])

    return (score_dw_do+score_up_do)/2




def eval_test(df_full,rownum,gbm_dw_l,gbm_up_l,dict_prec_dw_l,dict_prec_up_l,steps_back=72,reserv=20):
#def eval_test(df_full,rownum,steps_back=72,reserv=20):

    PRED_ROW = rownum

#     if rownum<=32000-steps_back-reserv:
#         return None


    mask = (df_full.ROW_NUM>=PRED_ROW-steps_back-reserv)&(df_full.ROW_NUM<PRED_ROW)

    df=df_full[mask].copy()

    ACT_LONG=0
    ACT_SHORT=0
    BALANCE = 100000
    BALANCE_START=100000
    PRICE_START_LONG=0
    PRICE_START_SHORT=0


    TAKE_PROF_LONG=0
    TAKE_PROF_SHORT=0
    STOP_LOSE_LONG=0
    STOP_LOSE_SHORT=0

    loos_cnt=0
    end_freez=0
    i=1

    comission=0.0008

#     take_r=0.015
#     stop_r=0.02

    moment_in_position=0


    params_dict=config_btc.params_trade



    l_c=params_dict.get('l_c')
    move=params_dict.get('move')#7
    freez=params_dict.get('freez')#7
    par1=params_dict.get('par1')#7
    par2=params_dict.get('par2')#7
    perev=params_dict.get('perev')#7



    timeout=0

    start_freez=0


    perev_cnt=0


    conf_level=0

    stops=0

    window=config_btc.slide_stop_take.get('window')
    step=config_btc.slide_stop_take.get('step')
    q_level=config_btc.slide_stop_take.get('q_level')




    for num_row in df[(df.ROW_NUM>=PRED_ROW-steps_back)&(df.ROW_NUM<PRED_ROW)].ROW_NUM.unique():



        X_test_row=df[df['ROW_NUM'] == num_row]


        # если без модели, а по рассчитанным данным
        p_short,prec_short,p_long,prec_long=classes.Estimator(config_btc,bit_functions,num_row).\
        predict_1h_loc(X_test_row,gbm_dw_l,gbm_up_l,dict_prec_dw_l,dict_prec_up_l)

        #если из истории

#         prec_long=float(df.loc[(df['ROW_NUM'] == num_row), 'PROB_LONG'].values)
#         prec_short=float(df.loc[(df['ROW_NUM'] == num_row), 'PROB_SHORT'].values)


        if  prec_long>par2 and prec_long>prec_short+par1:
                pred_cat=1
        elif prec_short>par2 and prec_long+par1<prec_short:
                pred_cat=-1
        else:
                pred_cat=0






        HIGH_PRICE=df.loc[(df['ROW_NUM'] == num_row), 'High'].values
        OPEN_PRICE=df.loc[(df['ROW_NUM'] == num_row), 'Open'].values
        CLOSE_PRICE=df.loc[(df['ROW_NUM'] == num_row), 'Close'].values
        LOW_PRICE=df.loc[(df['ROW_NUM'] == num_row), 'Low'].values
        time_key_base=list(df.loc[(df['ROW_NUM'] == num_row), 'date_for_ind'].values)[0]
        time_key_base=pd.Timestamp(time_key_base)



        event='no_event'
        event_sig='no_event'


        if ACT_LONG==1 and HIGH_PRICE>=TAKE_PROF_LONG and STOP_LOSE_LONG<LOW_PRICE : #тейк профит лонг

            AVG_P=TAKE_PROF_LONG

            BALANCE = BALANCE*(AVG_P/PRICE_START_LONG)*(1-comission)

            moment_in_position=999999999
            ACT_LONG=0
            TAKE_PROF_LONG=0
            STOP_LOSE_LONG=0
            event='take_long'
            conf_level=0
            loos_cnt=0
            #take_long_acc=take_long_acc+1


        elif ACT_SHORT==1 and LOW_PRICE<TAKE_PROF_SHORT and STOP_LOSE_SHORT>HIGH_PRICE : #тейк профит лонг

            AVG_P=TAKE_PROF_SHORT
            BALANCE = BALANCE*(PRICE_START_SHORT/AVG_P)*(1-comission)
            moment_in_position=999999999
            ACT_SHORT=0
            TAKE_PROF_SHORT=0
            STOP_LOSE_SHORT=0

            event='take_short'
            conf_level=0
            loos_cnt=0
            #take_short_acc=take_short_acc+1

        elif ACT_LONG==1 and STOP_LOSE_LONG>=LOW_PRICE : #стоп лосс по лонгу


            BALANCE = BALANCE*(STOP_LOSE_LONG/PRICE_START_LONG)*(1-comission)
            moment_in_position=999999999
            ACT_LONG=0
            ACT_SHORT=0
            TAKE_PROF_LONG=0
            STOP_LOSE_LONG=0

            event='stop_long'
            conf_level=0
            loos_cnt=loos_cnt+1
            #stop_loss_long=stop_loss_long+1

        elif ACT_SHORT==1 and STOP_LOSE_SHORT<=HIGH_PRICE : #стоп лосс по шорту

            moment_in_position=999999999
            BALANCE = BALANCE*(PRICE_START_SHORT/STOP_LOSE_SHORT)*(1-comission)

            ACT_SHORT=0
            ACT_LONG=0
            TAKE_PROF_SHORT=0
            STOP_LOSE_SHORT=0

            event='stop_short'
            conf_level=0
            loos_cnt=loos_cnt+1
            #stop_loss_short=stop_loss_short+1

        if loos_cnt>=l_c and l_c>0:

            start_freez=num_row
            end_freez = num_row+freez
            loos_cnt=0

        #выход из позици, по простою

        if ACT_LONG==1 and moment_in_position+move<=num_row:

            BALANCE = BALANCE*(CLOSE_PRICE/PRICE_START_LONG)*(1-comission)


            TAKE_PROF_SHORT=0
            STOP_LOSE_SHORT=0
            PRICE_START_SHORT=0
            PRICE_START_LONG=0
            ACT_SHORT=0
            ACT_LONG=0
            event_sig='out_long_time'
            conf_level=0
            stops+=1



        elif ACT_SHORT==1 and moment_in_position+move<=num_row:

            BALANCE = BALANCE*(PRICE_START_SHORT/CLOSE_PRICE)*(1-comission)

            TAKE_PROF_SHORT=0
            STOP_LOSE_SHORT=0
            PRICE_START_SHORT=0
            PRICE_START_LONG=0
            ACT_SHORT=0
            ACT_LONG=0

            event_sig='out_short_time'
            conf_level=0
            stops+=1


        # ПРОВЕРКА НА НА ПЕРЕВОРОТ, ЕСЛИ В СДЕЛКЕ

        elif pred_cat==-1 and conf_level+perev<prec_short and ACT_LONG==1: #войти в шорт

            ACT_LONG=0
            ACT_SHORT=1

            BALANCE = BALANCE*(CLOSE_PRICE/PRICE_START_LONG)*(1-comission)*(1-comission)

            PRICE_START_SHORT=df.loc[(df['ROW_NUM'] == num_row), 'Close'].values

            # #для сделок SHORT
            take_r=bit_functions.find_corr_stop(df,num_row,window,step,'up','mean',q=q_level)
            stop_r=bit_functions.find_corr_stop(df,num_row,window,step,'dw','quantile',q=q_level)


            TAKE_PROF_SHORT = PRICE_START_SHORT*(1-take_r)
            STOP_LOSE_SHORT = PRICE_START_SHORT*(1+stop_r)

            TAKE_PROF_LONG=0

            STOP_LOSE_LONG=0

            PRICE_START_LONG=0

            conf_level = prec_short
            moment_in_position=num_row
            event_sig='out_long_in_short'
            perev_cnt+=1



        elif pred_cat==1 and conf_level+perev<prec_long and ACT_SHORT==1: #войти в лонг

            ACT_SHORT=0

            ACT_LONG=1
            BALANCE = BALANCE*(PRICE_START_SHORT/CLOSE_PRICE)*(1-comission)*(1-comission)

            PRICE_START_LONG=df.loc[(df['ROW_NUM'] == num_row), 'Close'].values

            # #для сделок LONG
            take_r=bit_functions.find_corr_stop(df,num_row,window,step,'dw','mean',q=q_level)
            stop_r=bit_functions.find_corr_stop(df,num_row,window,step,'up','quantile',q=q_level)


            #STAKE= BALANCE*(1-comission)*(1-comission)
            TAKE_PROF_LONG = PRICE_START_LONG*(1+take_r)
            STOP_LOSE_LONG = PRICE_START_LONG*(1-stop_r)


            TAKE_PROF_SHORT=0

            STOP_LOSE_SHORT=0

            PRICE_START_SHORT=0


            conf_level = prec_long
            moment_in_position=num_row
            event_sig='out_short_in_long'


            perev_cnt+=1

        # ПРОВЕРКА НА НА УСИЛЕНИЕ, ЕСЛИ В СДЕЛКЕ

        elif pred_cat==1 and ACT_LONG==1: #войти в лонг

            if conf_level < prec_long:
                conf_level = prec_long
                event_sig='up_long_prob'


        elif pred_cat==-1 and ACT_SHORT==1: #войти в лонг

            if conf_level < prec_short:
                conf_level = prec_short
                event_sig='up_short_prob'


        # Если в сделке, но нет переворота / усиления, просто счетчик +1

        elif ACT_LONG==1 or ACT_SHORT==1:
            #moment_in_position=num_row
            event_sig='no_changes'


        # ЕСЛИ НЕ В СДЕЛКЕ, НО ЕСТЬ СИГНАЛ - ВХОД

        elif pred_cat==1 and ACT_LONG==0 and ACT_SHORT==0 and num_row>end_freez: #войти в лонг

            ACT_LONG=1
            PRICE_START_LONG=df.loc[(df['ROW_NUM'] == num_row), 'Close'].values

            # #для сделок LONG
            take_r=bit_functions.find_corr_stop(df,num_row,window,step,'dw','mean',q=q_level)
            stop_r=bit_functions.find_corr_stop(df,num_row,window,step,'up','quantile',q=q_level)


            #STAKE= BALANCE*(1-comission)
            TAKE_PROF_LONG = PRICE_START_LONG*(1+take_r)
            STOP_LOSE_LONG = PRICE_START_LONG*(1-stop_r)
            BALANCE=BALANCE*(1-comission)

            conf_level = prec_long
            moment_in_position=num_row
            event_sig='in_long'



        elif pred_cat==-1 and ACT_LONG==0 and ACT_SHORT==0 and num_row>end_freez: #войти в шорт

            # #для сделок SHORT
            take_r=bit_functions.find_corr_stop(df,num_row,window,step,'up','mean',q=q_level)
            stop_r=bit_functions.find_corr_stop(df,num_row,window,step,'dw','quantile',q=q_level)


            ACT_SHORT=1
            PRICE_START_SHORT=df.loc[(df['ROW_NUM'] == num_row), 'Close'].values
            #STAKE= BALANCE*(1-comission)
            TAKE_PROF_SHORT = PRICE_START_SHORT*(1-take_r)
            STOP_LOSE_SHORT = PRICE_START_SHORT*(1+stop_r)
            BALANCE=BALANCE*(1-comission)

            conf_level = prec_short
            moment_in_position=num_row
            event_sig='in_short'
            df.loc[(df['ROW_NUM'] == num_row), 'STATUS_RES2'] = "IN_SHORT"




        p_short_prev=prec_short
        #p_netr_prev=p_netr
        p_long_prev=prec_long

#     print(float(BALANCE),BALANCE_START)


   # return float(BALANCE),float(BALANCE)/BALANCE_START-1
    return float(BALANCE)/BALANCE_START-1


def change_date2(a):
    try:
        return datetime.strptime(str(a),'%Y-%m-%d %H:%M:%S%z').strftime('%Y-%m-%d %H:%M:%S')
    except:
        return datetime.strptime(str(a),'%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')


def target_new(df,rn,porog_min_take,porog_max_step,porog_min_balance):

    direction_idl=df[df.ROWNUM==rn].direction_idl.values[0]
    max_take_idl=df[df.ROWNUM==rn].max_take_idl.values[0]
    step_to_idl=df[df.ROWNUM==rn].step_to_idl.values[0]
    rn_of_next_take=df[df.ROWNUM==rn].rn_of_next_take.values[0]
    max_stop_idl=df[df.ROWNUM==rn].max_stop_idl.values[0]

    if direction_idl ==0:
        return direction_idl
    #print(max_take_idl,max_stop_idl)

    if max_stop_idl>0:
        rel_take_stop = max_take_idl/max_stop_idl
        #print(rel_take_stop)
    else:
        rel_take_stop=1

    if max_take_idl<porog_min_take:
        return 0
    if step_to_idl>=porog_max_step:
        return 0
    if rel_take_stop<porog_min_balance:
        return 0

    return direction_idl

def rel_value2(fig1,fig2):
    if fig1>fig2:
        return -(fig1/fig2-1)
    else:
        return (fig2/fig1-1)


def rel_value(fig1,fig2):
    if fig1>fig2:
        return fig1/fig2-1
    else:
        return fig2/fig1-1




def find_min_max3(df,rn_cur,rn_start,rn_end,step_add=3,n_bord = 0.01):

    #print(n_bord)

    loc_close = df[df.ROWNUM==rn_cur].Close.values[0]

    loc_close_sm = df[df.ROWNUM==rn_cur].Close_sm_53.values[0]
#     print(f'fact {loc_close} sm {loc_close_sm} ')

    final_rn = df.ROWNUM.max()
    if rn_end>final_rn:
        rn_end=final_rn
    if rn_end-rn_start<5:

        dict_res = {}
        dict_res['direction_idl']=0
        dict_res['max_take_idl']=0
        dict_res['step_to_idl']=0
        dict_res['rn_of_next_take']=final_rn
        dict_res['max_stop_idl']=0
        dict_res['target_value_idl'] = 0


        return dict_res

    #print('cur close ', loc_close)

    mask = (df.ROWNUM>=rn_start)&(df.ROWNUM<rn_end)
    df_loc= df[mask][['ROWNUM','High','Low','Close','Close_sm_53','Close_sm_5']].copy()


    df_loc['REL_TO_TRUE_MAX'] = df_loc.apply(lambda x: rel_value(loc_close,x.High),axis=1)
    df_loc['REL_TO_TRUE_MIN'] = df_loc.apply(lambda x: rel_value(loc_close,x.Low),axis=1)
    df_loc['REL_TO_CLOSE'] = df_loc.apply(lambda x: rel_value2(loc_close_sm,x.Close_sm_53),axis=1)
    df_loc['REL_TO_MAX'] = np.where(df_loc['REL_TO_CLOSE']>0,df_loc['REL_TO_CLOSE'],0)
    df_loc['REL_TO_MIN'] = np.where(df_loc['REL_TO_CLOSE']<0,-df_loc['REL_TO_CLOSE'],0)

    max_dif_max=df_loc['REL_TO_MAX'].max()
    max_dif_min=df_loc['REL_TO_MIN'].max()



    if max(max_dif_max,max_dif_min)<=n_bord:

        max_true_dif_max = df_loc['REL_TO_TRUE_MAX'].max()
        max_true_dif_min = df_loc['REL_TO_TRUE_MIN'].max()

        dict_res = {}
        dict_res['direction_idl']=0
        dict_res['max_take_idl']=max(max_dif_max,max_dif_min)
        dict_res['step_to_idl']=None
        dict_res['rn_of_next_take']=None
        dict_res['max_stop_idl']=max(max_dif_max,max_dif_min)
        dict_res['target_value_idl'] = None
        dict_res['maximum_value_for_take_idl']=max(max_true_dif_max,max_true_dif_min)
        dict_res['minimum_value_for_stop_idl']=max(max_true_dif_max,max_true_dif_min)


        return dict_res

    df_loc['IND_MAX'] = np.where(df_loc['REL_TO_MAX']==max_dif_max,1,0)
    df_loc['IND_MIN'] = np.where(df_loc['REL_TO_MIN']==max_dif_min,1,0)

#     df_loc['VALUE_MAX'] = np.where(df_loc['REL_TO_CLOSE']==max_dif_max,1,0)
#     df_loc['VALUE_MIN'] = np.where(df_loc['REL_TO_CLOSE']==max_dif_min,1,0)

    rn_for_max = df_loc[df_loc['IND_MAX']==1].ROWNUM.values[0]
    rn_for_min = df_loc[df_loc['IND_MIN']==1].ROWNUM.values[0]

#     value_for_max = df_loc[df_loc['IND_MAX']==1].High.values[0]
#     value_for_min = df_loc[df_loc['IND_MIN']==1].Low.values[0]
    value_for_max = df_loc[df_loc['IND_MAX']==1].Close_sm_53.values[0]
    value_for_min = df_loc[df_loc['IND_MIN']==1].Close_sm_53.values[0]

    gap_for_max=rn_end-rn_for_max
    gap_for_min=rn_end-rn_for_min




    if abs(max_dif_max)>abs(max_dif_min):


        max_true_dif_max = df_loc[df_loc.ROWNUM<=rn_for_max]['REL_TO_TRUE_MAX'].max()
        max_true_dif_min = df_loc[df_loc.ROWNUM<=rn_for_max]['REL_TO_TRUE_MIN'].max()

#         cur_max = max_dif_max
        direction = 1
        cur_rn_for_max = rn_for_max
        cur_gap_for_max = gap_for_max
        max_stop = df_loc[df_loc.ROWNUM<=rn_for_max].REL_TO_MIN.max()
        steps_to_max = rn_for_max-rn_cur
        max_take = max_dif_max
        target_value = value_for_max

        max_true_up = max_true_dif_max
        min_true_down = max_true_dif_min

    else:
#         cur_max = max_dif_min

        max_true_dif_max = df_loc[df_loc.ROWNUM<=rn_for_min]['REL_TO_TRUE_MAX'].max()
        max_true_dif_min = df_loc[df_loc.ROWNUM<=rn_for_min]['REL_TO_TRUE_MIN'].max()


        direction = -1
        cur_rn_for_max = rn_for_min
        cur_gap_for_max = gap_for_min
        max_stop = df_loc[df_loc.ROWNUM<=rn_for_min].REL_TO_MAX.max()
        steps_to_max = rn_for_min-rn_cur
        max_take = max_dif_min
        target_value = value_for_min

        max_true_up = max_true_dif_min
        min_true_down = max_true_dif_max


    dict_res = {}
    dict_res['direction_idl']=direction
    dict_res['max_take_idl']=max_take
    dict_res['step_to_idl']=steps_to_max
    dict_res['rn_of_next_take']=cur_rn_for_max
    dict_res['max_stop_idl']=max_stop
    dict_res['target_value_idl']=target_value
    dict_res['maximum_value_for_take_idl']=max_true_up
    dict_res['minimum_value_for_stop_idl']=min_true_down

    if cur_gap_for_max<=2 and rn_end<final_rn:

        dict_res=find_min_max3(df,rn_cur,rn_start,rn_end+step_add,step_add=3,n_bord=n_bord)


    return dict_res


def permutaion_list(df_loc,target_field,start_col_list, const = 1.05):

    X_train = df_loc[(df_loc.ROWNUM>=300)&(df_loc.ROWNUM<6000)][start_col_list].copy()
    y_train = df_loc[(df_loc.ROWNUM>=300)&(df_loc.ROWNUM<6000)][target_field]
    X_test = df_loc[(df_loc.ROWNUM>=6200)&(df_loc.ROWNUM<8500)][start_col_list].copy()
    y_test = df_loc[(df_loc.ROWNUM>=6200)&(df_loc.ROWNUM<8500)][target_field]
    cb_model =CatBoostClassifier(
                                   verbose=False)
    cb_model.fit(X_train,y_train)

    result = permutation_importance(cb_model,
                                X_test,
                                y_test,
                                scoring='average_precision',
                                n_repeats=10,
                                random_state=1,
                                n_jobs=3,
                               )

    data = {"feature_names": X_test.columns, "feature_importance": result['importances_mean']}
    result_df: pd.DataFrame = pd.DataFrame(data)

    result_df.sort_values("feature_importance", ascending=False, inplace=True)
    result_df.reset_index(drop=True, inplace=True)


    feature_names = result_df.feature_names.to_list()
    len(feature_names)

    best_preds = cb_model.predict_proba(X_test)[:, 1]
    best_ap = average_precision_score(y_test, best_preds)


    X_test_loc = X_test.copy()

    test_size = X_test.shape[0]


    ap_metrics = [best_ap]

    for col in feature_names:
        X_test_loc[col] = np.random.choice(X_test_loc[col], size=test_size)
        #Xts = X_test[clusters_selected_cols_08]
        Yts = y_test
        preds = cb_model.predict_proba(X_test_loc)[:, 1]

        ap = average_precision_score(Yts, preds)
        ap_metrics.append(ap)

    print('Количество метрик', len(ap_metrics))

    trh=y_test.mean()

    i=0
    tar_list=[]
    for i1 in ap_metrics:
        i+=1
        if trh>i1:
            #print(i)
            tar_list.append(i)

    if len(tar_list)==0:
        len_spis = len(feature_names)
    else:
        len_spis = min(tar_list)

    print('first_itter: ',len_spis)

    if len_spis>100:

        i=0
        tar_list=[]
        for i1 in ap_metrics:
            i+=1
            if trh*const>i1:
                #print(i)
                tar_list.append(i)

        if len(tar_list)==0:
            len_spis = len(feature_names)
        else:
            len_spis = min(tar_list)

        print('second_itter: ',len_spis)

    colls_new_list=list(result_df.head(len_spis).feature_names)

    return colls_new_list
