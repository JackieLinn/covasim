### **总结：Covasim 教程 T3 核心内容**

---

#### **概括要点**
1. **MultiSim 多模拟运行**  
   • 支持运行多个模拟（相同参数不同随机种子，或不同参数），用于生成不确定性区间或参数扫描。  
   • 提供统计方法（均值、中位数、合并结果）和可视化工具。

2. **Scenarios 情景模拟**  
   • 基于同一基准模拟，通过修改参数批量生成不同情景的模拟。  
   • 简化多参数场景的配置与运行。

3. **高级功能**  
   • 并行运行（`cv.parallel()`）加速模拟。  
   • 合并多个 MultiSim 对象，支持复杂分析。

4. **注意事项**  
   • 运行 MultiSim 后，原模拟对象会被修改，需从 MultiSim 中获取结果。

---

#### **详细要点**

---

### **1. MultiSim 多模拟运行**

**核心用途**  
• **不确定性分析**：通过不同随机种子生成结果的波动区间。  
• **参数扫描**：探索不同参数（如传播率 `beta`）对结果的影响。

**操作方法**  
• **基本使用**：  
  ```python
  sim = cv.Sim()
  msim = cv.MultiSim(sim)        # 创建 MultiSim 对象
  msim.run(n_runs=5)             # 运行 5 次（不同随机种子）
  msim.plot()                    # 绘制所有模拟结果
  ```

• **统计与可视化**：  
  ```python
  msim.mean()                    # 计算所有模拟的均值
  msim.plot_result('new_infections')  # 绘制均值曲线及波动区间
  msim.median()                  # 计算中位数
  msim.combine()                 # 合并所有模拟结果（总和）
  ```

• **参数扫描示例**：  
  ```python
  betas = np.linspace(0.01, 0.02, 5)  # 定义不同 beta 值
  sims = [cv.Sim(beta=beta, label=f'Beta={beta}') for beta in betas]
  msim = cv.MultiSim(sims)
  msim.run()
  msim.plot_result('cum_infections')  # 绘制不同 beta 的累计感染
  ```

• **并行加速**：  
  ```python
  # 使用 cv.parallel() 快速运行并绘图
  cv.parallel(sim1, sim2).plot(['cum_deaths', 'cum_infections'])
  ```

**注意事项**  
• **对象一致性**：运行 `msim.run()` 后，原 `sim` 对象会被修改，需通过 `msim.sims` 获取结果。  
• **合并 MultiSim**：  
  ```python
  merged = cv.MultiSim.merge([msim1, msim2])  # 合并多个 MultiSim
  merged.plot(color_by_sim=True)              # 按模拟来源着色
  ```

---

### **2. Scenarios 情景模拟**

**核心用途**  
• 基于同一基准模拟，快速生成不同参数配置的模拟集合。  
• 支持批量管理参数修改，适用于政策对比或假设分析。

**操作方法**  
• **定义情景**：  
  ```python
  scenarios = {
      'baseline': {'name': '基准情景', 'pars': {}},  
      'high_beta': {'name': '高传播率', 'pars': {'beta': 0.02}},  
      'low_beta': {'name': '低传播率', 'pars': {'beta': 0.012}}  
  }
  ```

• **运行与绘图**：  
  ```python
  scens = cv.Scenarios(basepars=basepars, scenarios=scenarios)
  scens.run()       # 运行所有情景
  scens.plot()      # 自动对比不同情景结果
  ```

**优势**  
• **简化配置**：无需手动创建多个 `Sim` 对象。  
• **统一管理**：支持自动添加不确定性（通过 `n_runs` 参数）。

---

### **3. 高级功能与技巧**

• **动态干预**：  
  ```python
  def protect_elderly(sim):
      if sim.t == sim.day('2021-04-01'):
          elderly = sim.people.age > 70
          sim.people.rel_sus[elderly] = 0.0  # 降低老年人易感性

  sim = cv.Sim(interventions=protect_elderly)
  ```

• **结果合并**：  
  ```python
  msim1 = cv.MultiSim([sim1, sim2])
  msim2 = cv.MultiSim([sim3, sim4])
  merged = cv.MultiSim.merge([msim1, msim2])  # 合并多个 MultiSim
  ```

• **元数据保存**：  
  ```python
  sim.save('my-sim.sim')           # 保存模拟对象（不含人群数据）
  sim.save('my-sim.sim', keep_people=True)  # 包含人群数据
  ```

---

### **4. 常见问题与解决**

• **结果不一致**：  
  • 确保从 `msim.sims` 中获取结果，而非原 `sim` 对象。  
  • 使用 `msim.run()` 后，原 `sim` 的随机种子会被修改。

• **性能优化**：  
  • 使用 `cv.parallel()` 并行运行，显著加速多核环境下的模拟。

---

#### **核心价值**
• **灵活性**：MultiSim 支持任意参数组合的批量模拟。  
• **易用性**：Scenarios 提供快速配置多情景的标准化流程。  
• **可扩展性**：支持动态干预、复杂参数扫描及结果合并，满足科研与政策分析需求。