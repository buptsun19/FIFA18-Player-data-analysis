import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures #进行多项式拟合
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
matplotlib.rcParams['axes.unicode_minus'] = False    # 解决保存图像是负号'-'显示为方块的问题

filepath = './dataset/data-big6.csv'
big6_data = pd.read_csv(filepath, index_col=[0])
# big6_data.info()

# club_player_value = big6_data[['Club', 'Value_u']]
# club_player_value_gro = club_player_value.groupby('Club')['Value_u'].agg([np.sum])
# club_player_value_gro.sort_values(by='sum', ascending=True, inplace=True)
# club_player_value_gro = club_player_value_gro[-15:]
# club_player_value_gro.plot(kind='barh', color='r')
# plt.title('球员身价最高的十五大俱乐部')
# plt.tight_layout()
# plt.show()
# print(club_player_value_gro.index)
#
# player_count = big6_data.groupby('league').size()
# print(player_count)
# player_count.plot(kind='bar', rot=0, color='y')
# plt.title("六大联赛球员数量")
# plt.show()
#
# player_count = big6_data.groupby('Nationality').size()
# player_count.sort_values(inplace=True, ascending=True)
# player_count = player_count[-20:]
# print(player_count)
# player_count.plot(kind='barh', rot=0, color='g')
# plt.title("贡献六大联赛球员最多的前二十个国家")
# plt.tight_layout()
# plt.show()
#
# player_count = big6_data.groupby('continent').size()
# print(player_count)
# player_count.plot(kind='bar', rot=0)
# plt.title("六大联赛球员各大洲分布")
# plt.show()
#
# sns.boxplot(x='league', y='Overall', data=big6_data)
# plt.title('六大联赛球员能力积分情况')
# plt.show()
#
# league_wage = big6_data.groupby('league')['Wage_u'].agg([np.mean])
# print(league_wage)
# league_wage.sort_values(by='mean', inplace=True, ascending=False)
# league_wage.plot(kind='bar', rot=0)
# plt.title('六大联赛球员周薪情况')
# plt.show()
#
#
# sns.violinplot(y=big6_data['Wage_u'], x=big6_data['league'], data=big6_data)
# plt.title('六大联赛球员周薪分布图-小提琴图')
# plt.show()
#
# sns.jointplot(x='Overall', y='Wage_u', data=big6_data, kind='scatter')
# plt.title('球员能力值与周薪的关系')
# plt.show()
#
# # 球员能力值与周薪的关系探索
# plt.figure(figsize=(4, 4))
# sns.reg(x='Overall', y='Wage_u', data=big6_data)
# plt.title('球员能力值与周薪的线性拟合关系')
# plt.show()
#
# overall_wage_rela= big6_data[['Overall', 'Wage_u']]
# X = overall_wage_rela['Overall'].values
# y = overall_wage_rela['Wage_u'].values
# X = X.reshape(X.shape[0], 1)
# y = y.reshape(y.shape[0], 1)
#
# # 2次线性回归进行预测
# poly_feature = PolynomialFeatures(degree=2)
# X_train_poly = poly_feature.fit_transform(X)
# # 建立模型预测
# regressor_model = LinearRegression()
# regressor_model.fit(X_train_poly, y)
#
# xx = np.linspace(40, 100, 100)  # 能力值从40到100，取100个点
# xx = xx.reshape(xx.shape[0], 1)
# # 画出2次线性回归的图
# xx_poly2 = poly_feature.transform(xx)
# yy_poly2 = regressor_model.predict(xx_poly2)
# plt.figure(figsize=(4, 4))
# plt.scatter(X, y)
# plt.plot(xx, yy_poly2, 'r-', label='二次回归拟合', lw=2)
# plt.legend()
# plt.title('球员能力与周薪二次回归拟合关系')
# plt.xlabel('球员能力值')
# plt.ylabel('球员周薪（K)')
# plt.show()
#

club_wage = big6_data.groupby('Club')['Wage_u'].agg([np.mean])
club_wage.sort_values(by='mean', ascending=True, inplace=True)
club_wage = club_wage[-10:]
club_wage.plot(kind='barh', rot=0)
plt.title("平均周薪最高的十个俱乐部")
plt.tight_layout()
plt.xlim([60, 160])
plt.show()
print(club_wage)

print(club_wage.index)
club_wage_10 = ['Real Madrid', 'FC Barcelona', 'Juventus', 'Manchester City',
       'Manchester United', 'Chelsea', 'Liverpool', 'Tottenham Hotspur',
       'FC Bayern München', 'Arsenal']
club_wage_data = big6_data[big6_data['Club'].isin(club_wage_10)]
sns.boxplot(x='Club', y='Wage_u', data=club_wage_data)
plt.title("周薪最高的十个俱乐部箱线图")
plt.tight_layout()
plt.tick_params(axis='x', labelsize=8)    # 设置x轴标签大小
plt.show()

# club_total_stats = big6_data.groupby('Club')['Overall'].agg([np.mean])
# club_total_stats.sort_values(by='mean', ascending=True, inplace=True)
# club_total_stats = club_total_stats[-15:]
# club_total_stats.plot(kind='barh', rot=0, color='m')
# #print(club_total_stats)
# plt.xlim([70, 85])
# plt.title('球员能力值最高的俱乐部')
# plt.tight_layout()
# plt.show()
#
# club_overall = ['Juventus', 'Napoli', 'Inter', 'Real Madrid', 'Milan', 'FC Barcelona',
#        'Paris Saint-Germain', 'Roma', 'Manchester United', 'FC Bayern München',
#        'Chelsea', 'Manchester City', 'Tottenham Hotspur', 'Liverpool',
#        'Bayer 04 Leverkusen']
# club_overall_data = big6_data[big6_data['Club'].isin(club_overall)]
# print(club_overall_data)
# ax = sns.boxplot(x='Club', y='Overall', data=club_overall_data)
# ax.set_xticklabels(ax.get_xticklabels(), rotation=60)
# plt.title("球员能力值最高的俱乐部的箱线图")
# plt.tight_layout()
# plt.show()
#
# club_potential = big6_data.groupby('Club')['Potential'].agg([np.mean])
# club_potential.sort_values(by='mean', ascending=True, inplace=True)
# club_potential = club_potential[-15:]
# club_potential.plot(kind='barh', rot=0, color='g')
# print(club_potential)
# plt.xlim([80, 86])
# plt.title('球员潜力值最高的俱乐部')
# plt.tight_layout()
# plt.show()
#
# print(club_potential.index)
# club_poten = ['Juventus', 'FC Barcelona', 'Real Madrid', 'Manchester City',
#        'FC Bayern München', 'Paris Saint-Germain', 'Napoli',
#        'Manchester United', 'Chelsea', 'Milan', 'Atlético Madrid', 'Liverpool',
#        'Borussia Dortmund', 'Roma', 'Tottenham Hotspur']
# club_poten_data = big6_data[big6_data['Club'].isin(club_poten)]
# ax = sns.boxplot(x='Club', y='Potential', data=club_poten_data)
# ax.set_xticklabels(ax.get_xticklabels(), rotation=30)
# plt.title("球员潜力值最高的俱乐部箱线图")
# plt.tight_layout()
# plt.show()
#
# age_overall_poten = big6_data.groupby('Age').agg({'Overall' : np.mean, 'Potential' : np.mean})
# age_overall_poten.reset_index(inplace=True)
# print(age_overall_poten)
# ax1 = age_overall_poten.plot(x='Age', y='Overall', legend='Overall', style='-', color='y', marker='o', lw=3)
# age_overall_poten.plot(x='Age', y='Potential', legend='Potential', style='--', color='b', marker='+', lw=2, ax=ax1)
# plt.title('球员能力值和潜力值随年龄的变化情况')
# plt.ylabel('能力和潜力值')
# plt.show()

# big6_data_1000 = big6_data[big6_data['Value_u'] >= 1]
# age_value = big6_data_1000.groupby('Age')['Value_u'].mean()
# x1 = list(age_value.index)
# x2 = list(age_value.index + 0.4)
# y1 = age_value.values
# y2 = age_value.values
# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# ax1.bar(x1, y1, color='y')
# plt.ylabel('身价(M)')
# ax2 = ax1.twinx()
# ax2.plot(x2, y1, 'bo-', linewidth=3)
# plt.title('身价随着年龄的变化情况')
# plt.show()
#
#
# age_wage = big6_data.groupby('Age')['Wage_u'].mean()
# print(age_wage)
# ax = age_wage.plot(kind='line', style='-', color='y', marker='o', lw=3)
# plt.title('周薪随着年龄的变化情况')
# plt.ylabel('周薪(K)')
# plt.show()



