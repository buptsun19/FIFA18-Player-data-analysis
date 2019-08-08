"""
    说明：
    数据集：data.csv共包括90个字段信息，各个字段的含义如下所示：
            ID唯一标识 Name姓名 Age年龄 Photo照片图片链接 Nationality	国籍 Flag国旗图片链接 Overall综合能力 Potential潜力值 Club签约俱乐部
            Club Logo	俱乐部logo链接  Value身价 Wage周薪 Special总能力 Preferred Foot惯用脚 International Reputation国际声誉 Weak Foot逆足能力
            Skill Moves花式技巧 Work Rate 积极性 Body Type身体模型 Real Face真实脸型 Position	位置 Jersey Number球衣号码 Joined入队时间
            Loaned From	从哪里租借  Contract Valid Until合同到期 Height身高  Weight 体重  LS	左锋 Left Striker ST	前锋 Striker
            RS	右锋 Right Striker  LW	左边锋left wing LF	左中锋 left forward CF	中锋 centre forward RF	右中锋 right forward
            RW	右边锋right wing LAM	左攻击性前卫 left att. midfield CAM	中攻击性前卫 centre att. midfield RAM 右攻击性前卫 right att. midfield
            LM	左前卫 left midfield   LCM	左中前卫 left centre midfield CM	中前卫 centre midfield RCM	右中前卫 right centre midfield
            RM	右前卫right midfield LWB	左边后卫 left wing back  LDM	左边防守型前卫 left def. midfield  CDM 中防守型前卫 centre def. midfield
            RDM	右边防守型前卫 rigth def. midfield RWB	右边后卫 right wing back   LB	左后卫 left back LCB	左中后卫 left centre back
            CB	中后卫 centre back RCB	右中后卫 right centre back RB	右后卫 right back Crossing	传中   Finishing	射术  HeadingAccuracy
            头球精度 ShortPassing	短传 Volleys	凌空 Dribbling	盘带 Curve	弧线 FKAccuracy	任意球精度 LongPassing	长传 BallControl	控球
            Acceleration 加速 SprintSpeed	速度  Agility	敏捷 Reactions	反应  Balance	平衡  ShotPower	射门力量 Jumping	弹跳 Stamina	体能
            Strength	强壮  LongShots	远射 Aggression	侵略性  Interceptions	拦截意识 Positioning	跑位 Vision	视野  Penalties	点球
            Composure	沉着 Marking	盯人  StandingTackle	抢断  SlidingTackle	铲球  GKDiving	鱼跃 GKHandling	手型 GKKicking	开球
            GKPositioning	站位 GKReflexes	反应 Release Clause	违约金 league 联赛 continent 所属大洲
    数据来源：来源于https://sofifa.com/网站，共包括奥地利、比利时、丹麦、英格兰、法国、德国、爱尔兰、意大利、荷兰、挪威、波兰、葡萄牙、苏格兰、西班牙、瑞典、
             瑞士、土耳其、阿根廷、巴西、智利、哥伦比亚、墨西哥、美国、中国、日本、韩国、沙特、澳大利亚等国家的主流联赛数据，超过28个国家的36个高级别联赛。
    分析过程：
            国家分析：
            球员分布：从宏观上分析，全球的顶级球员分布，包括各个大洲和各个国家的球员数量分布。
            国家队实力与球员数量的关系：根据球员数量分布，观察国家队实力与球员数量是否有直接关系，考虑可以增加身价的因素。单个球员的价值（球员总身价/球员个数）
            各个洲以及各个国家的球员实力：
            国家队的潜力：
            最强国家队：国家队的球员平均全球最强

            俱乐部分析：
            最强俱乐部：俱乐部平均分最高，拥有最好的球员，
            最有潜力俱乐部：
            根据球员的身价，评估球员价值最大的十大俱乐部，以及这些俱乐部的平均薪酬支出情况。
            俱乐部薪酬分析：


            球员个人分析：
            球员年龄分布：
            最强球员：
            球员评分随年龄的变化：
            #球员收入分布，收入随年龄的变化：
            转会费：转会费随年龄的变化，
            #球员潜力值随年龄的变化：
            技巧分析，欧洲和南美球员的对比；
            不同位置的球员价值：
            #球员的价值和工资之间的关系：
            #球员的价值和年龄之间的关系：
            #球员的工资和年龄之间的关系：
            不同位置的球员价值：

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
matplotlib.rcParams['axes.unicode_minus'] = False    # 解决保存图像是负号'-'显示为方块的问题

filepath = './dataset/data.csv'
all_data = pd.read_csv(filepath, index_col=[0])

# 基本信息查看和判断
# 共18207个运动员信息，每个运动员共有90个属性，个别属性中有为空的值，经过判断不影响后续数据分析
all_data.info()
print(all_data.head(3))
print(all_data.isnull().any())


# ID经判断，为唯一值
ID_only = all_data.drop_duplicates(subset=['ID'])
print("ID去重后的行数为:", ID_only['ID'].count())

continent_nation = all_data[['Nationality', 'continent']]
continent_groby = continent_nation.groupby('continent').size()
continent_groby.sort_values(inplace=True, ascending=False)

# 各大洲分布可视化
continent_groby.name = '占比分布'
continent_groby.plot(kind='pie', autopct='%.1f%%', figsize=(4, 4))
plt.title('各大洲球员数量分布')
plt.show()

continent_groby.plot(kind='bar', rot=0, figsize=(4, 4))
plt.title('各大洲球员数量分布')
plt.xlabel('Continent')
#能够将x轴标签进行完整显示
plt.tight_layout()
plt.show()

# 各个国家分布可视化
nation_groby = continent_nation.groupby('Nationality').size()
nation_groby.sort_values(inplace=True, ascending=True)
nation_groby = nation_groby[-20:]
nation_groby.plot(kind='barh', color='g')
plt.title('FIFA记录球员最多的前二十个国家球员数量')
plt.tight_layout()
plt.show()

nation_many = {"Nationality": nation_groby.index, 'player_sum': nation_groby.values}
nation_many_merge = pd.DataFrame(nation_many)
nation_value = all_data[['Nationality', 'Value_u']].copy()    # 注意，使用.copy(),否则会报SettingWithCopyWarning
nation_value_new = pd.merge(nation_value, nation_many_merge, how='inner', on='Nationality')
# sns.boxplot(x='Nationality', y='Value_u', data=nation_value_new)
# plt.show()
nation_value_gro = nation_value_new.groupby('Nationality').mean()
nation_value_gro = nation_value_gro[['Value_u']]
print(nation_value_gro)
nation_value_gro.sort_values(by='Value_u', inplace=True, ascending=False)
nation_value_gro.plot(kind='bar', rot=20, color='r')
plt.title('各国球员平均身价排行（FIFA中所列全部球员）')
plt.tick_params(axis='x', labelsize=9)    # 设置x轴标签大小
plt.tight_layout()
plt.show()

player_week = all_data[all_data['Wage_u'] > 0]
plt.figure(figsize=(4, 4))
sns.distplot(player_week['Wage_u'], kde=False)
plt.title("球员收入分布直方图")
plt.show()

plt.figure(figsize=(4, 4))
sns.stripplot(x='Wage_u', data=player_week)
plt.title('球员收入分布散布图')
plt.tick_params(axis='x', labelsize=9)    # 设置x轴标签大小
plt.show()

ax = sns.stripplot(y='Wage_u', x='Age', data=player_week)
plt.title('球员收入与年龄的关系')
plt.tight_layout()
plt.show()

week_100K = player_week[player_week['Wage_u'] < 100000]
sns.distplot(week_100K['Wage_u'], kde=False, color='g')
plt.title('周薪10万欧以下球员收入分布直方图')
plt.show()

week_gro = player_week.groupby('Age')['Wage_u'].agg([np.mean])
print(week_gro)
week_gro.plot(kind='line', rot=0, style='-.', color='y', marker='o', lw=2)
plt.title('球员收入随年龄的变化情况')
plt.show()

total_stat = player_week.groupby('Age')['Overall'].agg([np.mean])
total_stat.plot(kind='line', rot=0, linestyle='dashed', color='c', marker='o', lw=2)
plt.title('球员实力评分随年龄的变化情况')
plt.show()

potential = player_week.groupby('Age')['Potential'].agg([np.mean])
print(potential)
potential.plot(kind='line', rot=0, linestyle='dashed', color='m', marker='o', lw=2)
plt.title('球员潜力随年龄的变化')
plt.show()










