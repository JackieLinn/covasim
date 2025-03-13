主要用于评估各种干预措施对流行病的影响
预装了每个国家的人口统计数据，且用户可以自定义人口和联系网络（可细化到城市，社区，大学等），内置了常见的COVID-19的干预措施，并且可以自定义干预措施。
通过创建Agent模拟个体状态，运行逻辑如下：
1. 创建仿真对象，加载参数并验证内部一致性
2. 创建agents群组，包括年龄，性别，并存病症（从特定位置的数据分布中提取）
3. 根据其他统计特性将Agents连接到关联网络并开始整合循环。
### 模型中个体的疾病发展模型：
![[Pasted image 20250202131735.png]]
不同的症状，轻度症状和严重症状的人的恢复时间不同。 死亡的概率随着年龄的增长而增加

### 疾病传播：

**传播概率β**需根据现实情况，接触类型，其他干预措施定义
viral load是个体携带病毒的水平


![[Pasted image 20250202133146.png]]

### 联系网络：
如家庭，学校，社区，公司等充斥人群联系的环境下，又或是多个联系网络的集成网络
![[Pasted image 20250202134525.png]]

### 干预措施：
Covasim模型具备内置常见的干预措施，并可以通过用户自定义干预措施。
论文中对模型内置的干预措施做了部分解释：
- 物理距离，口罩和卫生的影响。
- 检测并诊断。在传播网络中一般很难注意到无症状者对于病毒传播的影响，在加入检测诊断的干预措施后可以诊断出无症状者的病毒携带情况，从而可以降低病毒传播
- 跟踪接触路径。以一个病毒携带者的角度出发，追踪其接触的个体，从而制定有效的隔离措施。
- 不同的隔离措施（针对确诊个体的隔离与接触个体的隔离）
- 药物干预（疫苗）。
[T5 - 使用干预措施 — Covasim 3.1.6 文档](https://docs.idmod.org/projects/covasim/en/latest/tutorials/tut_interventions.html)

### 代码部分
#### covasim包结构
![[Pasted image 20250203101717.png]]



```
import covasim as cv

  

# Custom intervention -- see Tutorial 5

def protect_elderly(sim):

    if sim.t == sim.day('2020-04-01'):

        elderly = sim.people.age>70

        sim.people.rel_sus[elderly] = 0.0

  

pars = dict(

    pop_type = 'hybrid', # Use a more realistic population model

    location = 'japan', # Use population characteristics for Japan

    pop_size = 50e3, # Have 50,000 people total in the population

    pop_infected = 100, # Start with 100 infected people

    n_days = 90, # Run the simulation for 90 days

    verbose = 0, # Do not print any output

)

  

# Running with multisims -- see Tutorial 3

s1 = cv.Sim(pars, label='Default')

s2 = cv.Sim(pars, interventions=protect_elderly, label='Protect the elderly')

msim = cv.MultiSim([s1, s2])

msim.run()

fig = msim.plot(['cum_deaths', 'cum_infections'])
```

	校准不理解






































