# FIFA18-Player-data-analysis
对sofifa网站上的球员数据进行分析,数据集为18年球员数据，可从sofifa官网对数据进行更新，代码可以复用。

说明： 
本文所有数据均来自sofifa官方网站，网站收录了包括奥地利、比利时、丹麦、英格兰、法国、德国、爱尔兰、意大利、荷兰、挪威、波兰、葡萄牙、苏格兰、西班牙、瑞典、瑞士、土耳其、阿根廷、巴西、智利、哥伦比亚、墨西哥、美国、中国、日本、韩国、沙特、澳大利亚等国家的主流联赛数据，总共有超过28个国家的36个高级别联赛； 
数据提取时间：2018年下半年； 
数据内容说明：本数据源共提取了球员超过90个属性信息，包括姓名、年龄、国籍、综合能力、潜力值、签约俱乐部、周薪、身价、惯用脚、逆足能力、各个位置的评分值、各种足球技术的评分值、违约金等等； 
报告主要内容：本报告是对球员数据进行的描述性分析，大部分内容为描述性统计，有少量采用机器学习的回归分析；暂未涉及球员具体的技术能力。报告大部分内容是对五大联赛和中超的分析。

全球球员地域分布
从世界各大洲范围内来看，主流职业联赛球员分布，欧洲最多，占比超过50%，其次是南美洲，占比17.5%，亚洲球员占比10.7%，其余各大洲均低于10%。

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/all_players/1-各大洲球员数量分布.png) ![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/all_players/2-各大洲球员数量分布.png) 

从球员的国家分布来看，球员数量排名前三的分别是英格兰、德国和西班牙，这与FIFA收录的联赛有一定关系，其中英格兰就收录了英超、英冠、英甲和英乙，而非顶级联赛基本为本国球员效力，外援较少； 
但日本球员数量居然排进了前十，值得注意；

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/all_players/3-FIFA记录球员最多的前二十个国家球员数量.png) 

不过中国也不差，排名第12，可是中国国家队成绩怎么这么差，接下来，看一下球员平均身价！ 
很明显，在这二十个国家中，中国队身价最低，平均身价仅有35.5万欧元！身价最高的为巴西，平均460万欧元。

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/all_players/4-各国球员平均身价排行（FIFA中所列全部球员）.png) 

以上是概况统计，接下来，我们从球员个人的角度来看一下：
球员薪水和能力分析
前几天，关于贝尔加盟苏宁的消息不胫而走，天价周薪更是引起热议，有国外热心网友计算了贝尔的收入：周薪超过100万镑，每日收入高达112万人民币，一秒就赚13块！
那先看一下球员收入情况吧！

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/all_players/5-球员收入分布直方图.png) ![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/all_players/6-球员收入分布散布图.png) 

超过14000名球员周薪低于1.2万欧元，从散布图来看，10万欧元以上周薪的球员就屈指可数了，看来贫富差距也挺大的。 
经统计，周薪10万欧元以上的球员共有185个。

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/all_players/9-周薪10万欧以下球员收入分布直方图.png) 

即便我们只看周薪低于10万欧以下的球员，发现低收入球员仍然占大多数，超过7500名球员的周薪低于3000欧。（貌似3000欧也不少了！）
球员吃的是青春饭，看一看收入随年龄的散布情况！

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/all_players/7-球员收入与年龄的关系散布图.png) 

从散布图上可以看出，梅西收入一骑绝尘，周薪超过20万欧的球员年龄基本在26岁-33岁，这也是职业球员最好的时光！

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/all_players/8-10万欧以下球员收入与年龄的关系散布图.png) 

上图是周薪收入在10万欧以下的球员分布散布图，从这个图上能看到分布还是比较平均的，但36岁之后的收入会迅速下落。
最后，我们再看一下球员收入、球员实力以及球员潜力随年龄的变化趋势。

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/all_players/11-球员收入随年龄的变化情况.png) 

26岁-33岁是球员平均薪水最高的年纪，也符合正值当打之年的价值（在40岁和45岁出现了一个高峰，这是因为有异常值，40岁的布冯小将周薪拉高了整个年龄段的收入水平）。 
看看各年龄段球员实力评分情况：

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/all_players/10-球员实力评分随年龄的变化情况.png) 

球员实力基本随着年龄的增长而增加，到30岁达到顶峰，之后数据有波动，这和大龄球员保持状态的能力不同有关系，基本上，各个年龄段的实力和收入呈正相关关系。 
接下来看一下球员的潜力分析：

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/all_players/12-球员潜力评分随年龄的变化情况.png) 

17岁小将的潜力值达到峰值，之后随年龄的增长不断下降。 
注：45岁出现的异常值，是因为45的年龄段只有一个球员，此球员为墨西哥甲级联赛帕丘卡的门将，名字叫奥斯卡-佩雷，估计是个老妖。
正常情况下，应该在预处理阶段忽略这些异常值，但为了保持真实性暂且保留。
下面，我们关注一下五大联赛的情况！ 
对了，前段时间有一个中国足协的主席说要把中超打造成第六大联赛，这里也顺便看一下中超和五大联赛的对比情况！


六大联赛分析
说明：除了传统的五大联赛之外，增加了中超。由于数据取的是2018年FIFA的数据，到目前为止可能会有一些转会的变化。
球员分布概况

从球员数量来看，六大联赛共有注册球员3321名。 
各个联赛的球员数量： 

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/big6_league/1-六大联赛球员数量分布.png) 

其中，中超球员445名最少，英超共有球员679名最多，当然这与各个联赛的球队数量有一定关系。 
接下来看这3321名球员的国家分布： 

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/big6_league/2-贡献六大联赛球员最多的前二十个国家.png) 

西班牙输出的球员最多，共426名，接下来是中国，共386名，由于国内没有在五大联赛效力的（就一个武磊可以忽略不计了），因此能算出中超共有外援59名（445-386）。 
英超虽然球员最多（679名），但是英格兰在六大联赛输出的球员并不多，仅有277名。 
六大联赛之外，最受欢迎的是巴西的球员，共有135名，其次是阿根廷，但仅有85名，这也解释了为何美洲杯上有很多生面孔，因为阿根廷国家队很多球员来自于阿根廷国内联赛。 
葡萄牙共输出了59名球员，这么少的数量能够拿到首届欧国联的冠军，实属不易。超过50名球员的还有一个国家是荷兰，向六大联赛输出了55名球员。
豪门俱乐部

先来看一下豪门俱乐部（球员身价最高），球员身价最高的前十五支俱乐部分别为：[‘Real Madrid’, ‘FC Barcelona’, ‘Manchester City’, ‘Juventus’,’FC Bayern München’, ‘Atlético Madrid’, ‘Paris Saint-Germain’, ‘Tottenham Hotspur’, ‘Chelsea’, ‘Manchester United’, ‘Liverpool’,’Napoli’, ‘Inter’,’Arsenal’, ‘Borussia Dortmund’] 

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/big6_league/18-球员身价最高的二十大俱乐部.png) 

皇马首当其冲，总身价将近9亿欧，虽然今年颗粒无收，这主要是前几年欧冠冠军加成，球员身价水涨船高；接下来的四支球队均是今年的联赛冠军，排名第六的是马德里竞技，之后法甲冠军巴黎圣日耳曼排在第七； 
热刺、切尔西、曼联、利物浦四支英超球队紧随其后，这里面诞生了欧冠决赛的两支队伍和欧联的冠军，利物浦第十一名的身价能拿到联赛第二和欧冠冠军，实属不易。这也从侧面说明了一个好的教练对球队的重要性！ 
最后四支分别为那不勒斯、国际米兰、阿森纳和多特蒙德。
而周薪最高的十支俱乐部分别为：[‘Real Madrid’, ‘FC Barcelona’, ‘Juventus’, ‘Manchester City’, ‘Manchester United’, ‘Chelsea’, ‘Liverpool’, ‘Tottenham Hotspur’, ‘FC Bayern München’, ‘Arsenal’] 

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/big6_league/10-周薪前十的俱乐部箱线图.png) 

皇马以平均周薪15.2万夺魁，考虑到这批球员拿了几个欧冠，是配得上这个周薪的。而曼联的平均周薪也超过了10.2万欧元，但踢成这个样子实在说不过去。比较意外的是阿森纳居然排名第十（7.8万欧元），看来穷的没有转会费买人，都是用来发工资了。
看一下球员能力和潜力比较高的俱乐部： 
球员平均能力值最高的前十五个俱乐部分别为： [‘Juventus’, ‘Napoli’,’Inter’, ‘Real Madrid’, ‘Milan’, ‘FC Barcelona’,’ParisSaint-Germain’,’Roma’, ‘Manchester United’, ‘FC Bayern München’,’Chelsea’, ‘Manchester City’, ‘Tottenham Hotspur’, ‘Liverpool’, ‘Bayer 04 Leverkusen’] 

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/big6_league/12-球员能力最高的俱乐部箱线图.png) 

和上面的豪门俱乐部排名有些出入，AC米兰和勒沃库森居然入选了，从上图分析，拜仁、皇马和巴萨这三支球队球员能力分布差别大，强的很强，但短板明显；尤文图斯、国际米兰、那不勒斯、罗马和AC米兰几支意甲球队倒是球员能力比较均衡，这可能和意甲没有钱买超级球星有关，但意甲的欧战成绩（除尤文图斯）太差，看来球员并不是决定因素（说的就是米兰的加图索）。
球员平均潜力值最高的前十五个俱乐部分别为：[‘Juventus’, ‘FC Barcelona’, ‘Real Madrid’, ‘Manchester City’, ‘FC Bayern München’, ‘Paris Saint-Germain’, ‘Napoli’, ‘Manchester United’, ‘Chelsea’, ‘Milan’, ‘Atlético Madrid’, ‘Liverpool’, ‘Borussia Dortmund’, ‘Roma’, ‘Tottenham Hotspur’] 

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/big6_league/14-球员潜力最高的十五大俱乐部箱线图.png) 

潜力值的排名和豪门俱乐部的排名比较一致，看来豪门俱乐部比较注意对新人的买进和培养（由于SOFIFA网站对于大龄球员将其潜力和能力值设置为相同，这对于潜力的分析有一点影响），比较意外的是AC米兰和罗马的入选，看来这两支球队需要搞个好教练了。 
目前潜力值最高的应该是巴黎的姆巴佩。
联赛球员分析

再看各大联赛的球员能力积分情况： 

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/big6_league/4-六大联赛球员能力积分箱线图.png) 

中超球员总积分1532分，远远低于五大联赛，西甲和英超积分相同为1729分，意甲1722分，其次是德甲和法甲，分别为1697分和1691分，球员能力积分高低反应了联赛吸引顶级球员的强弱，从积分来看，英超=西甲>意甲>德甲>法甲，这与一般对五大联赛精彩排名的认知基本一致。 
从球员能力箱线图分析，意甲有球员能力相比其他队员强很多，没错，这是总裁C罗。同样法甲也有几个bug球员，不出意外领军的应该是内马尔。中超有几个球员鹤立鸡群，他们分别是暴力鸟、塔利斯卡、卡拉斯科和奥斯卡。
顶级联赛的球员平均周薪情况： 

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/big6_league/5-六大联赛球员周薪情况.png) 

周薪排名和能力积分排名一致，英超平均周薪超过了五万欧，大概是中超的十倍（5千欧），这样来看，中超除了超级外援的超高薪之外，平均年薪大概为205万人民币，相当于互联网公司的总监、经理级别了。 

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/big6_league/6-六大联赛球员周薪分布图.png) 

从周薪分布来看，除却顶级球星的超高薪（西甲和意甲分别有一位bug球员），英超和西甲在各薪酬段球员分布比较平均，意甲、法甲、德甲有较多球员薪酬比较集中在低位。中超由于相对薪酬较低，从上图可以看出还是比较集中的。
球员能力和周薪有没有相关关系？通过下面的分析可以一见端倪。 

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/big6_league/7-球员能力值与周薪的关系.png) 

皮尔森相关系数为0.67，线性相关性还是比较强的。 
下面分别使用可视化seaborn库中的regplot以及机器学习中的PolynomialFeatures进行线性拟合和高次多项式拟合： 

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/big6_league/8-球员能力值与周薪的拟合关系图.png)![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/big6_league/8-2-球员能力值与周薪的二次线性拟合关系图.png) 

拟合后进行数据的可视化，线性拟合效果不太理想，二次回归拟合仅能在一定的区间进行预测； 

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/big6_league/8-1-球员能力值与周薪的三次线性拟合关系图.png) 

经过测试，三次回归拟合能够较好的反应球员能力和周薪之间的关系。由于是三次拟合关系，简单来说，球员能力较低时大家周薪不会有太大差别，但当能力提升到一定程度（超级球星），周薪会大幅度的上升。
随着年龄的增长，球员的能力值和潜力值也是在变化着的: 

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/big6_league/15-球员能力和潜力随年龄变化趋势图.png) 

潜力逐渐下降，能力不断提升，17岁时球员的潜力评分最大，这和转会市场中各大豪门俱乐部分别豪购小将的趋势一致（今年转会季马竞花费1.26亿欧元签下本菲卡20岁小将超新星菲利克斯）。
球员身价和周薪随着年龄的变化情况： 

![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/big6_league/16-身价超100万欧的球员身价随年龄的变化图.png) 
![image](https://github.com/buptsun19/FIFA18-Player-data-analysis/blob/master/image_result/big6_league/17-周薪随年龄的变化示意图.png) 

两者的趋势基本一致，但周薪相比身价能够在大龄阶段继续维持较高水平，这与目前球员能够延长运动生涯保持高竞技水平有关。 
26岁是球员身价最高的年纪，但到球员在28岁有一个明显下跌，后续需要继续观察。（40岁时周薪和身价逆势上涨，这是因为有一个小将布冯的原因）

