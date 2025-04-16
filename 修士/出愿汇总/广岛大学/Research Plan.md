## Estimation of Bicycle Front Wheel Steering Angle and Cyclist Orientation Using LiDAR Data

1.Introduction
-Background:
自动驾驶是目前受到广泛关注的研究领域，在交通事故中，行人和自行车是更容易出现死亡风险的对象，所以对行人、自行车骑行者的行动方向预测是自动驾驶的一个重要课题，而自行车骑行者相对于行人又有着更高的移速，所以对于自动驾驶系统，对自行车的方向预测就尤为重要。
本文在“Cyclist Orientation Estimation Using LiDAR Data”^[1] 的基础上，对于在现实交通环境中，有时无法有效获取骑行者头部和身体的LiDAR数据（比如骑行者佩戴头盔、雨衣）的情形为背景提出对 “Bicycle Front Wheel Steering Angle”的估计来补充对骑行者方向的判断，自行车前轮与车身的偏转角度与自行车的行进方向是直接相关的，所以可以根据前轮偏转角度判断出骑行者行动方向， 在此基础上还可以根据骑行者的已有轨迹来预测骑行轨迹。从自行车本身的数据出发也可以减少骑行者本人的干扰，无论是小孩还是成人，通勤还是运动，车轮的控制逻辑是一样的，更方便于标准化建模。

2.描述方法
-convert from a packet file of the LiDAR sensor to Point Cloud Data format, PCD.  (和 “Cyclist Orientation Estimation Using LiDAR Data” 一样的方法)
-choose reflectivity information, - 这里的数据可以根据不同的自行车类型进行分类优化训练
-input to the point clound data classification model for Bicycle Front Wheel Steering Angle and Cyclist Orientation which is ResNet50
-评估角度预测准确率

3.Discussions
本文的重点在于如何利用LiDAR数据训练CNN来识别前轮与车身的偏转角度，评估不用的骑行状态（直行、左转、右转）区分度。我会通过网络课程系统的学习深度学习，来进一步评估和优化研究的可行性。