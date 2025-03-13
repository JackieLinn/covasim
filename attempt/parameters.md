# 流行病学模型参数说明

## 人口参数
- `pop_size` = 20e3  
  ​**人口规模** - 易感SARS-CoV-2的个体数量（智能体数量）
- `pop_infected` = 20  
  ​**初始感染人数** - 模拟起始时的感染个体数
- `pop_type` = 'random'  
  ​**人口类型** - 可选值:  
  `random`（最快生成速度） | `synthpops`（最佳真实性） | `hybrid`（平衡方案）
- `location` = None  
  ​**地理数据** - 加载特定地区的人口数据（默认西雅图）

## 模拟参数
- `start_day` = '2020-03-01'  
  ​**模拟起始日期**
- `end_day` = None  
  ​**模拟终止日期**
- `n_days` = 60  
  ​**模拟天数** - 当未指定终止日期时生效
- `rand_seed` = 1  
  ​**随机数种子** - 设为`None`时不重置种子
- `verbose` = cvo.verbose  
  ​**信息输出等级**:  
  0（静默） | 0.1（部分输出） | 1（标准） | 2（详细调试）

## 人口缩放参数
- `pop_scale` = 1  
  ​**人口缩放因子** - 实际人口规模 = 智能体数 × 缩放因子
- `scaled_pop` = None  
  ​**缩放后总人口** - 智能体数 × 缩放因子
- `rescale` = True  
  ​**动态缩放开关** - 根据疫情发展自动调整人口规模
- `rescale_threshold` = 0.05  
  ​**动态缩放阈值** - 易感人群比例触发条件
- `rescale_factor` = 1.2  
  ​**动态缩放系数** - 每次调整的乘数因子
- `frac_susceptible` = 1.0  
  ​**基础易感比例** - 人群中对感染具有基础易感性的比例

## 接触网络参数
- `contacts` = None  
  ​**分层接触数** - 各网络层的平均接触数（通过`reset_layer_pars()`初始化）
- `dynam_layer` = None  
  ​**动态网络层标识** - 各层是否支持动态调整（通过`reset_layer_pars()`初始化）
- `beta_layer` = None  
  ​**分层传播系数** - 各网络层的传播能力（通过`reset_layer_pars()`初始化）

## 基础传播参数
- `beta_dist` = dict(dist='neg_binomial', par1=1.0, par2=0.45, step=0.01)  
  ​**个体传播性分布** - 负二项分布参数，基于[研究数据](https://www.researchsquare.com/article/rs-29548/v1)
- `viral_dist` = dict(frac_time=0.3, load_ratio=2, high_cap=4)  
  ​**时变病毒载量参数** - 基于[Lescure et al. 2020](https://doi.org/10.1016/S1473-3099(20)30200-0)
- `beta` = 0.016  
  ​**症状接触传播率** - 经校准的基准值
- `asymp_factor` = 1.0  
  ​**无症状传播修正因子** - 无症状病例传播能力调整系数，基于[研究结论](https://www.sciencedirect.com/science/article/pii/S1201971220302502)

## 多病毒变体参数
- `n_imports` = 0  
  ​**日均输入病例** - 服从泊松分布的实际输入数
- `n_variants` = 1  
  ​**流行病毒变体数**

## 免疫参数
- `use_waning` = True  
  ​**动态免疫衰减开关**
- `nab_init` = dict(dist='normal', par1=0, par2=2)  
  ​**初始中和抗体分布** - 基于[实验数据](https://doi.org/10.1101/2021.03.09.21252641)
- `nab_decay` = dict(form='nab_growth_decay', growth_time=21, decay_rate1=np.log(2)/50, decay_time1=150, decay_rate2=np.log(2)/250, decay_time2=365)  
  ​**抗体衰减动力学参数**
- `nab_kin` = None  
  ​**抗体动力学参数构造** - 初始化时生成
- `nab_boost` = 1.5  
  ​**再感染抗体增强因子** - 假设值
- `nab_eff` = dict(...)  
  ​**抗体效力参数** - 包含多个回归系数
- `rel_imm_symp` = dict(asymp=0.85, mild=1, severe=1.5)  
  ​**症状依赖性免疫增强因子** - 理论假设
- `immunity` = None  
  ​**免疫矩阵** - 通过`init_immunity()`初始化
- `trans_redux` = 0.59  
  ​**突破性感染传播衰减** - 基于[研究数据](https://www.medrxiv.org/content/10.1101/2021.07.13.21260393v1)

## 病毒变体特异性参数
- `rel_beta` = 1.0  
  ​**相对传播系数** - 不同变体间的传播能力差异

## 病程时长参数（单位：天）
- `dur['exp2inf']` = dict(dist='lognormal_int', par1=4.5, par2=1.5)  
  ​**暴露至感染期** - 基于[Lauer et al.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7081172/)
- `dur['inf2sym']` = dict(dist='lognormal_int', par1=1.1, par2=0.9)  
  ​**感染至症状期** - 基于[Linton et al.](https://doi.org/10.3390/jcm9020538)
- `dur['sym2sev']` = dict(dist='lognormal_int', par1=6.6, par2=4.9)  
  ​**症状至重症期** - 综合[Linton et al.]及[Wang et al.](https://jamanetwork.com/journals/jama/fullarticle/2761044)
- `dur['sev2crit']` = dict(dist='lognormal_int', par1=1.5, par2=2.0)  
  ​**重症至危重症期** - 综合[Chen et al.](https://www.sciencedirect.com/science/article/pii/S0163445320301195)及[Wang et al.]

## 恢复周期参数
- `dur['asym2rec']` = dict(dist='lognormal_int', par1=8.0, par2=2.0)  
  ​**无症状恢复期** - 基于[Wölfel et al.](https://www.nature.com/articles/s41586-020-2196-x)
- `dur['mild2rec']` = dict(dist='lognormal_int', par1=8.0, par2=2.0)  
  ​**轻症恢复期** - 同无症状恢复期
- `dur['sev2rec']` = dict(dist='lognormal_int', par1=18.1, par2=6.3)  
  ​**重症恢复期** - 基于[Verity et al.](https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(20)30243-7/fulltext)
- `dur['crit2rec']` = dict(dist='lognormal_int', par1=18.1, par2=6.3)  
  ​**危重症恢复期** - 同重症恢复期
- `dur['crit2die']` = dict(dist='lognormal_int', par1=10.7, par2=4.8)  
  ​**危重症致死期** - 基于[Verity et al.]

## 疾病进展概率参数
- `rel_symp_prob` = 1.0  
  ​**症状发生比例修正因子**
- `rel_severe_prob` = 1.0  
  ​**重症转化修正因子**
- `rel_crit_prob` = 1.0  
  ​**危重症转化修正因子**
- `rel_death_prob` = 1.0  
  ​**病死率修正因子**
- `prog_by_age` = prog_by_age  
  ​**年龄依赖性进展开关**
- `prognoses` = None  
  ​**年龄特异性预后矩阵** - 初始化时生成

## 防控措施参数
- `iso_factor` = None  
  ​**隔离传播衰减因子** - 通过`reset_layer_pars()`初始化
- `quar_factor` = None  
  ​**隔离易感性衰减因子** - 通过`reset_layer_pars()`初始化
- `quar_period` = 14  
  ​**标准隔离周期**

## 干预与分析参数
- `interventions` = []  
  ​**干预措施列表** - 用户自定义
- `analyzers` = []  
  ​**自定义分析器** - 用户扩展功能
- `timelimit` = None  
  ​**模拟时间限制（秒）​**
- `stopping_func` = None  
  ​**模拟提前终止条件函数**

## 医疗系统参数
- `n_beds_hosp` = None  
  ​**普通病床容量** - 重症患者收治能力
- `n_beds_icu` = None  
  ​**ICU病床容量** - 危重症患者收治能力
- `no_hosp_factor` = 2.0  
  ​**病床饱和时重症转危重风险乘数**
- `no_icu_factor` = 2.0  
  ​**ICU饱和时危重转死亡风险乘数**

## 疫苗与变体参数
- `vaccine_pars` = {}  
  ​**疫苗参数库** - 初始化时加载
- `vaccine_map` = {}  
  ​**疫苗编号映射** - 反向索引表
- `variants` = []  
  ​**病毒变体库** - 用户自定义扩展
- `variant_map` = {0:'wild'}  
  ​**变体编号映射** - 基础毒株索引
- `variant_pars` = dict(wild={})  
  ​**变体参数库** - 初始化时扩展