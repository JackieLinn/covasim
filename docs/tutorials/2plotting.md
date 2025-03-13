### **总结：Covasim 教程 T2 核心内容**

---

#### **概括要点**
1. **全局绘图配置**  
   • 通过 `cv.options()` 设置全局参数（如分辨率、字体、自动显示等），适配 Jupyter 环境。

2. **对象信息打印**  
   • 提供三种信息展示方式：`brief()`（简略）、`summarize()`（详细）、`disp()`（全量）。

3. **绘图功能**  
   • 默认绘图 `sim.plot()`，支持自定义绘图内容（`to_plot` 参数）、多列布局、日期格式调整等。

4. **保存与导出**  
   • 保存模拟文件（`.sim`）、导出结果到 Excel/JSON，支持元数据记录。

5. **高级绘图定制**  
   • 通过 `style` 参数调整绘图风格（内置或 Matplotlib 样式），支持局部覆盖全局设置。

---

#### **详细要点**

1. **全局配置（`cv.options`）**  
   • **作用**：统一设置所有绘图参数（如 `dpi`, `fontsize`, `verbose` 等）。  
   • **示例**：  
     ```python
     cv.options(jupyter=True, verbose=0)  # Jupyter 优化配置（关闭冗余输出）
     ```

2. **对象信息打印方法**  
   • **`brief()`**：显示关键信息（如模拟日期、人群规模）。  
   • **`summarize()`**：列出所有结果和参数（如感染数、干预措施）。  
   • **`disp()`**：显示完整对象结构（包含所有属性和方法）。

3. **绘图功能详解**  
   • **单结果绘图**：  
     ```python
     sim.plot_result('new_infections')  # 仅绘制新增感染曲线
     ```
   • **多结果绘图**：  
     ```python
     sim.plot(to_plot=['new_infections', 'cum_infections'])  # 同时绘制新增和累计感染
     ```
   • **概览图（`to_plot='overview'`）**：  
     ◦ 展示所有核心指标（如感染、住院、检测等）。  
     ◦ 支持多列布局（`n_cols=5`）、自定义尺寸（`figsize=(20,20)`）。

4. **保存与导出选项**  
   • **保存模拟文件**：  
     ```python
     sim.save('my-sim.sim')  # 默认不保存人群数据（节省空间）
     sim.save('my-sim.sim', keep_people=True)  # 强制保存人群数据
     ```
   • **导出到 Excel/JSON**：  
     ```python
     sim.to_excel('results.xlsx')  # 导出为 Excel（兼容 Pandas）
     sim.to_json('params.json')    # 导出参数为 JSON
     ```
   • **元数据记录**：  
     ◦ 使用 `cv.savefig()` 保存图像时自动嵌入代码版本和参数（避免结果溯源问题）。

5. **绘图风格定制**  
   • **内置样式**：  
     ◦ `style='covasim'`（默认）、`style='simple'`（极简）、`style='ggplot'`（Matplotlib 风格）。  
   • **局部覆盖**：  
     ```python
     with cv.options.with_style(fontsize=6):  # 临时设置字体大小
         sim.plot()
     ```
   • **高级参数**：  
     ◦ 支持传递 Matplotlib 参数（如 `font`, `legend_args`, `style_args`）。

6. **实用技巧**  
   • **日期格式调整**：  
     ◦ `dateformat='sciris'`（默认）、`'concise'`（紧凑）、`'matplotlib'`（原生格式）。  
   • **图像元数据读取**：  
     ```python
     cv.get_png_metadata('my-fig.png')  # 查看生成图像的代码信息
     ```

---

#### **核心价值**
• **灵活性**：从全局配置到单图定制，满足不同场景需求。  
• **可追溯性**：通过元数据记录，确保结果可复现。  
• **兼容性**：支持与 Matplotlib/Pandas 无缝集成，便于扩展分析。