words = """
mywords:6
翻盘
啊呀呀呀
哎哟哟哟
哎唷唷唷
嗯哼哼哼
哎呀
哟哟哟
哦哦
哇噻
哗啦啦
嘟嘟嘟嘟
咔嚓
呼啸
咯咯咯咯
叮当叮当
呱呱
喵喵
咚咚咚

weird words: 5
隐形斗篷
电动雨伞
紫色独角兽
呼啦圈
海马爸爸
跆拳道
马达加斯加
超现实
植物系
碳排放
隐身术
FBI
国税局
安全第一
五块钱三个
垃圾分类

互联网: 7
吃瓜
摸鱼
躺平
内卷
上头
硬核
拿捏
干饭
真香
热搜
点赞
粉丝
直播带货
自媒体
网红
翻车
打工人
小丑

四字成语: 7
四海为家
九牛二虎之力
临时抱佛脚
麻雀虽小，五脏俱全
三人行必有我师 
千钧一发
十万火急
心平气和
嬉皮笑脸
春光明媚
春暖花开
生龙活虎
三分天下
前无古人
欢天喜地
东张西望
千家万户
妙手回春
眼明手快
目不转睛
一心一意
二话不说
三心二意
四海为家
五湖四海
七上八下
十全十美
风吹雨打
有气无力
一穷二白




tech: 4
区块链
人工智能助手
智能路障
云计算
大数据
5G

scifi: 3
星际飞船
时间机器
平行宇宙
智能机器人
虚拟现实
外星生物
光速旅行
量子力学

movies: 1
魔法药水
巫师学院
丛林迷宫
神秘洞穴
金字塔

lit: 2
爱丽丝梦游仙境
哈利波特
科学怪人
鲁宾逊漂流记
美国伟大的盖茨比
东方快车谋杀案
查理与巧克力工厂
战争与和平
蝙蝠侠
哆啦A梦
超人
蜘蛛侠
绿巨人
钢铁侠
神奇女侠
蜘蛛侠
超级闪电侠

bio: 3
葡萄糖
红蓝色盲
光合作用
血红蛋白
淋巴细胞
心脏骤停
碳水化合物
Ω-3脂肪酸
卡路里
膳食纤维
钙吸收
心血管健康
细胞膜

ast: 1
行星轨道
宇宙微波背景辐射
恒星形成
天体物理学
臭氧层
仙女座星系

math: 5
钝角
绝对值
临界点
抛物线
微积分
勾股定理
圆周率
十亿
八千三百二十五
四维空间

computers: 1
PPT
保存文件
数据库
关机
重新启动
CPU
移动电源
移动硬盘
许可证
搜索引擎

biz: 5
人力资源外包
员工持股计划
供应链
多米诺效应 
倒金字塔管理
绿色营销
个性化营销
时间管理
货币贬值
通货膨胀
上市公司
分期付款
经济形势
长期投资
批发商

polisci: 5
贿赂
律师
罚款
外交官
武装部队
竞选活动
最高统治者
世界和平

sports: 1
双截棍
空手道
三分球

food: 4
酸辣披萨
番茄冰沙
咖喱味的冰棒
鲷鱼蛋糕
鳗鱼寿司
鳄鱼肉
带有黑松露酱的烤鸡
一只非常可爱的猫
麻婆豆腐
宫保鸡丁
梅干菜烧肉
麻辣火锅
香蕉味的咖啡

uoft: 2
考试
毕业
实习
学霸
夜宵
室友
MAT135

fashion: 2
潮牌
时装周
联名款
复古风
运动风

music: 2
独奏
萨克斯管
和弦
节拍器
贝多芬的第五交响曲
莫扎特的安魂曲
乡村音乐
Kpop

animals: 3
鸭嘴兽
格陵兰袋鼠
独角鲸
穿山甲
"""
other = """
units:
54072个
32只
40条
300张
10本
20杯
3支
1000000件
14双
37块
98盒
90瓶
65米
71厘米
2千米
1千克
5吨
5毫升
2平方米
9立方米
1斤
7米
5页

adj:
史诗般
至高无上
匪夷所思
深情
欢快
讨厌
焦虑
痛苦
悲痛
甜蜜
忧伤
激动人心
壮观
超凡
震撼
宏伟
惊世骇俗
轰动
卓越非凡
悲伤
喜悦
热情
恐怖
温柔
绝望
狂喜
恶毒
甜蜜
狂野
忧郁
振奋
焦虑
愤怒
浪漫
寂寞
欣喜
痛苦
迷茫
温暖

v:
挠脚丫
蹦跳
爆炸
跳进水里
舔冰淇淋
翻跟头
摇晃
熔化
挤牛奶
抖动
"""
N=3
weights = {}
def split_by_separator(input_list, separator=':'):
    global weights
    result = {}
    current_sublist = []
    num = None
    for item in input_list:
        if separator in item :
            num = int(item[-1])
            current_sublist = []
            weights[item] = num
            result[item] = current_sublist

        else:
            current_sublist.append(item)

    return result
def sample_word(dictionary):
    # Normalize weights
    total_weight = sum(dictionary.values())
    normalized_weights = {word: weight / total_weight for word, weight in dictionary.items()}    
    cumulative_distribution = {}
    cumulative_sum = 0
    for word, weight in normalized_weights.items():
        cumulative_sum += weight
        cumulative_distribution[word] = cumulative_sum
    rand_num = random.random()    
    for word, cumulative_weight in cumulative_distribution.items():
        if rand_num <= cumulative_weight:
            return word

words =[w for w in words.strip().split("\n") if len(w)>0]
words = split_by_separator(words)
other = [w for w in other.strip().split("\n") if len(w)>0 and ":" not in w]

import random
random.shuffle( other)

appeared = set()
for i in range(100):
	j=0
	appeared_class = set()
	while j!=N:
		t = sample_word(weights)
		while t in appeared_class:
			t = sample_word(weights)
		appeared_class.add(t)
		random.shuffle(words[t])
		if words[t][0] not in appeared:
			appeared.add(words[t][0])
			j+=1
			print(words[t][0], end=" ")

	print(other[i])
"""
光合作用
三分天下
一只非常可爱的猫
宏伟

海马爸爸
长期投资
智能路障
喜悦

东张西望
个性化营销
世界和平
绝望

眼明手快
咖喱味的冰棒
鸭嘴兽
1斤


巫师学院
麻辣火锅
嘟嘟嘟
激动人心

带有黑松露酱的烤鸡
抛物线
摸鱼
武装部队

麻雀虽小，五脏俱全
时间管理
翻盘
细胞膜

隐身术
春暖花开
吃瓜
货币贬值

钝角
莫扎特的安魂曲
员工持股计划
浪漫

碳水化合物
外交官
喵喵喵
三分天下
恐怖
"""
