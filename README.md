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



