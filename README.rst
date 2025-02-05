=======
Covasim
=======

About Covasim
=============

Covasim is a stochastic agent-based simulator for performing COVID-19 analyses. These include projections of indicators such as numbers of infections and peak hospital demand. Covasim can also be used to explore the potential impact of different interventions, including social distancing, school closures, testing, contact tracing, quarantine, and vaccination.

Covasim 是一种基于随机代理的模拟器，用于执行 COVID-19 分析。其中包括对感染人数和医院需求高峰等指标的预测。Covasim 还可用于探索不同干预措施的潜在影响，包括社会隔离、学校关闭、检测、接触追踪、隔离和疫苗接种。

The original scientific paper describing Covasim is available at http://paper.covasim.org. The recommended citation is:

介绍 Covasim 的原始科学论文可在 http://paper.covasim.org 上查阅。建议的引用格式为:

    **Covasim: an agent-based model of COVID-19 dynamics and interventions**. Kerr CC, Stuart RM, Mistry D, Abeysuriya RG, Rosenfeld R, Hart G, Núñez RC, Cohen JA, Selvaraj P, Hagedorn B, George L, Jastrzębski M, Izzo A, Fowler G, Palmer A, Delport D, Scott N, Kelly S, Bennette C, Wagner B, Chang S, Oron AP, Wenger E, Panovska-Griffiths J, Famulare M, Klein DJ (2021). *PLOS Computational Biology* **17** (7): e1009149. doi: https://doi.org/10.1371/journal.pcbi.1009149.

Covasim's immunity module (including vaccines and variants) is described here:

此处介绍了 Covasim 的免疫模块（包括疫苗和变体）:

    **Mechanistic modeling of SARS-CoV-2 immune memory, variants, and vaccines**. Cohen JA, Stuart RM, Núñez RC, Wagner B, Chang ST, Rosenfeld K, Kerr CC, Famulare M, Klein DJ (under review; posted 2021-06-01). *medRxiv* 2021.05.31.21258018; doi: https://doi.org/10.1101/2021.05.31.21258018.

The Covasim webapp is available at https://app.covasim.org, and the repository for it is available `here <https://github.com/institutefordiseasemodeling/covasim_webapp>`__.

Covasim 网络应用程序可在 https://app.covasim.org 上获取，其资源库可在此处获取。

Covasim was developed by the `Institute for Disease Modeling <https://idmod.org/>`__, with additional contributions from the `University of Copenhagen <https://www.math.ku.dk/english>`__, the `Burnet Institute <https://www.burnet.edu.au/>`__, `GitHub <https://github.com/>`__, and `Microsoft <https://www.microsoft.com/en-us/ai/ai-for-health-covid-data>`__.

Covasim 由疾病建模研究所开发，哥本哈根大学、伯内特研究所、GitHub 和微软公司也为其做出了贡献。

Questions or comments can be directed to info@covasim.org, or on this project's
GitHub_ page. Full information about Covasim is provided in the documentation_.

如有问题或意见，请发送电子邮件至 info@covasim.org 或本项目的 GitHub 页面。有关 Covasim 的详细信息，请参阅文档。

.. _GitHub: https://github.com/institutefordiseasemodeling/covasim
.. _documentation: https://docs.covasim.org


.. contents:: **Contents**
   :local:
   :depth: 2


Background
==========

Covasim has been used for analyses in over a dozen countries, both to inform policy decisions (including in the US, UK, and Australia), and as part of research studies. Some key papers that have been written using Covasim include:

Covasim 已在十多个国家用于分析，既为政策决策提供信息（包括美国、英国和澳大利亚），也作为研究的一部分。使用 Covasim 撰写的一些重要论文包括

1. **Controlling COVID-19 via test-trace-quarantine**. Kerr CC, Mistry D, Stuart RM, Rosenfeld R, Hart G, Núñez RC, Selvaraj P, Cohen JA, Abeysuriya RG, George L, Hagedorn B, Jastrzębski M, Fagalde M, Duchin J, Famulare M, Klein DJ (2021). *Nature Communications* 12:2993. doi: https://doi.org/10.1038/s41467-021-23276-9.

2. **Determining the optimal strategy for reopening schools, the impact of test and trace interventions, and the risk of occurrence of a second COVID-19 epidemic wave in the UK: a modelling study**. Panovska-Griffiths J, Kerr CC, Stuart RM, Mistry D, Klein DJ, Viner R, Bonnell C (2020-08-03). *Lancet Child and Adolescent Health* S2352-4642(20) 30250-9. doi: https://doi.org/10.1016/S2352-4642(20)30250-9.

3. **Estimating and mitigating the risk of COVID-19 epidemic rebound associated with reopening of international borders in Vietnam: a modelling study**. Pham QD, Stuart RM, Nguyen TV, Luong QC, Tran DQ, Phan LT, Dang TQ, Tran DN, Mistry D, Klein DJ, Abeysuriya RG, Oron AP, Kerr CC (2021-04-12). *Lancet Global Health* S2214-109X(21) 00103-0; doi: https://doi.org/10.1016/S2214-109X(21)00103-0.

A more complete list of papers is given in ``papers.rst``.

If you've written a paper or report using Covasim, we'd love to know about it! Please write to us `here <mailto:info@covasim.org>`__.


Requirements
============

Python 3.9-3.11 (64-bit). (Note: Python 2.7 and Python 3.12 are not supported, the latter being due to `Numba <https://numba.pydata.org/>`_ not supporting Python 3.12 at the time of writing.)

We also recommend, but do not require, installing Covasim in a virtual environment. For more information, see documentation for e.g. Anaconda_.

.. _Anaconda: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.htmlCovasim


Quick start guide
==================

Install with ``pip install covasim``. If everything is working, the following Python commands should bring up a plot::

  import covasim as cv
  sim = cv.Sim()
  sim.run()
  sim.plot()


Full installation instructions
==============================

If you would rather download the source code rather than using the ``pip`` package, follow these steps:

1.  Clone a copy of the repository. If you intend to make changes to the code, we recommend that you fork it first.

2.  (Optional) Create and activate a virtual environment.

3.  Navigate to the root of the repository and install the Covasim Python package using one of the following options:

    *   For normal installation (recommended)::

          pip install -e .

    *   To install Covasim and optional dependencies (be aware this may fail since it relies on nonstandard packages)::

          pip install -e .[full]

    The module should then be importable via ``import covasim as cv``.


Usage examples
==============

There are several examples in the ``examples`` folder. These can be run as follows:

* ``python examples/simple.py``

  This example creates a figure using default parameter values.

  此示例使用默认参数值创建了一个图形。

* ``python examples/run_sim.py``

  This shows a slightly more detailed example, including creating an intervention and saving to disk.

  这显示了一个稍微详细一点的示例，包括创建干预和保存到磁盘。

* ``python examples/run_scenarios.py``

  This shows a more complex example, including running an intervention scenario, plotting uncertainty, and performing a health systems analysis.

  这是一个更复杂的示例，包括运行干预方案、绘制不确定性图以及进行卫生系统分析。

Other examples in that folder are taken from the tutorials.


Module structure
================

All core model code is located in the ``covasim`` subfolder; standard usage is ``import covasim as cv``. The ``data`` subfolder is described below.

所有核心模型代码都位于 covasim 子文件夹中；标准用法是将 covasim 导入为 cv。

The model consists of two core classes: the ``Person`` class (which contains information on health state), and the ``Sim`` class (which contains methods for running, calculating results, plotting, etc.).

该模型由两个核心类组成：``Person``类（包含健康状态信息）和``Sim``类（包含运行、计算结果、绘图等方法）。

The structure of the ``covasim`` folder is as follows, roughly in the order in which the modules are imported, building from most fundamental to most complex:

covasim "文件夹的结构如下，大致按照导入模块的顺序，从最基本的模块到最复杂的模块：

* ``version.py``: 版本号、日期及许可协议信息。
* ``requirements.py``: 用于检查模块导入是否成功的基础模块，若导入失败则关闭相关功能。
* ``utils.py``: 随机数选择函数（多数基于Numba加速）及其他辅助工具函数。
* ``misc.py``: 各类杂项辅助函数。
* ``settings.py``: Covasim用户可自定义选项（如默认字体大小）。
* ``defaults.py``: Covasim默认配置（颜色、绘图样式等）。
* ``parameters.py``: 参数字典生成函数及输入数据加载功能。
* ``plotting.py``: 绘图脚本，包含Web应用使用的Plotly交互图表（优先定义以供其他类调用）。
* ``base.py``: 基础类``ParsObj``，以及``BaseSim``和``BasePeople``类的基本方法及相关函数。
* ``people.py``: ``People``类，用于管理每个个体的状态更新。
* ``population.py``: 生成人口数据的函数（含年龄结构、接触网络等）。
* ``interventions.py``: 干预措施基类``Intervention``及其派生类，支持动态参数调整。
* ``immunity.py``: ``strain``毒株类，以及免疫力衰减和中和抗体计算函数。
* ``sim.py``: 核心类``Sim``，负责模型初始化、运行和结果可视化。
* ``run.py``: 仿真运行函数（如并行运行、``Scenarios``场景类和``MultiSim``多仿真类）。
* ``analysis.py``: 运行时分析器``Analyzers``、数据拟合类``Fit``、传播树类``TransTree``及其他分析工具。

****

* ``version.py``: Version, date, and license information.
* ``requirements.py``: A simple module to check that imports succeeded, and turn off features if they didn't.
* ``utils.py``: Functions for choosing random numbers, many based on Numba, plus other helper functions.
* ``misc.py``: Miscellaneous helper functions.
* ``settings.py``: User-customizable options for Covasim (e.g. default font size).
* ``defaults.py``: The default colors, plots, etc. used by Covasim.
* ``parameters.py``: Functions for creating the parameters dictionary and loading the input data.
* ``plotting.py``: Plotting scripts, including Plotly graphs for the webapp (used in other Covasim classes, and hence defined first).
* ``base.py``: The ``ParsObj`` class, the fundamental class used in Covasim, plus basic methods of the ``BaseSim`` and ``BasePeople`` classes, and associated functions.
* ``people.py``: The ``People`` class, for handling updates of state for each person.
* ``population.py``: Functions for creating populations of people, including age, contacts, etc.
* ``interventions.py``: The ``Intervention`` class, for adding interventions and dynamically modifying parameters, and classes for each of the specific interventions derived from it.
* ``immunity.py``: The ``strain`` class, and functions for computing waning immunity and neutralizing antibodies.
* ``sim.py``: The ``Sim`` class, which performs most of the heavy lifting: initializing the model, running, and plotting.
* ``run.py``: Functions for running simulations (e.g. parallel runs and the ``Scenarios`` and ``MultiSim`` classes).
* ``analysis.py``: The ``Analyzers`` class (for performing analyses on the sim while it's running), the ``Fit`` class (for calculating the fit between the model and the data), the ``TransTree`` class, and other classes and functions for analyzing simulations.

The ``data`` folder within the Covasim package contains loading scripts for the epidemiological data in the root ``data`` folder, as well as data on age distributions for different countries and household sizes.

Covasim 软件包中的 ``data`` 文件夹包含根 ``data`` 文件夹中流行病学数据的加载脚本，以及不同国家和家庭规模的年龄分布数据。


Other folders
=============

Please see the readme in each subfolder for more information.


Bin
---

This folder contains a command-line interface (CLI) version of Covasim; example usage::

该文件夹包含 Covasim 的命令行界面 (CLI) 版本；示例用法::

  covasim --pars "{pop_size:20000, pop_infected:1, n_days:360, rand_seed:1}"

Note: the CLI is currently not compatible with Windows. You will need to add
this folder to your path to run from other folders.

注意：CLI 目前与 Windows 不兼容。您需要将此文件夹添加到路径中，以便从其他文件夹运行。


Data
----

Scripts to automatically scrape data (including demographics and COVID epidemiology data),
and the data files themselves (which are not part of the repository).

用于自动抓取数据（包括人口统计学和 COVID 流行病学数据）和数据文件本身（不属于资源库的一部分）的脚本。

Tutorials
---------

This folder contains Jupyter notebooks for nine tutorials that walk you through using Covasim, from absolute basics to advanced topics such as calibration and creating custom populations.

该文件夹包含九个教程的 Jupyter 笔记本，指导您使用 Covasim，从绝对基础到高级主题，如校准和创建自定义种群。

Examples
--------

This folder contains demonstrations of simple Covasim usage, with most examples taken from the tutorials. 

该文件夹包含 Covasim 的简单使用演示，其中大部分示例来自教程。

Cruise ship
~~~~~~~~~~~

An early application of Covasim to the Diamond Princess cruise ship.

钻石公主号游轮的早期 Covasim 应用。

Calibration
~~~~~~~~~~~

Examples of how to calibrate simulations, including `Optuna`_ (also covered in the tutorial) and `Weights and Biases`_.

如何校准模拟的示例，包括 “Optuna”（教程中也有涉及）和 “Weights and Biases”。

.. _Optuna: https://optuna.org/
.. _Weights and Biases: https://www.wandb.com/


Tests
-----

Integration, development, and unit tests. While not (yet) beautifully curated, these folders contain many usage examples. See README in the tests folder for more information.

集成测试、开发测试和单元测试。虽然这些文件夹尚未经过精心整理，但包含了许多使用示例。更多信息，请参阅测试文件夹中的 README。

Disclaimer
==========

The code in this repository was developed by IDM, the Burnet Institute, the University of Copenhagen, and other collaborators to support our joint research on COVID. We’ve made it publicly available under the MIT License to provide others with a better understanding of our research and an opportunity to build upon it for their own work. Note that Covasim depends on a number of user-installed Python packages that can be installed automatically via ``pip install``. We make no representations that the code works as intended or that we will provide support, address issues that are found, or accept pull requests. You are welcome to create your own fork and modify the code to suit your own modeling needs as contemplated under the MIT License. See the contributing and code of conduct READMEs for more information.

本资源库中的代码由 IDM、伯纳特研究所（Burnet Institute）、哥本哈根大学（University of Copenhagen）和其他合作者共同开发，以支持我们对 COVID 的联合研究。我们在 MIT 许可下将其公开，以便他人更好地了解我们的研究，并有机会在此基础上开展自己的工作。请注意，Covasim 依赖于许多用户安装的 Python 软件包，这些软件包可以通过 ``pip install`` 自动安装。我们不保证代码能按预期运行，也不保证我们会提供支持、解决发现的问题或接受拉取请求。我们欢迎您创建自己的分叉，并根据 MIT 许可修改代码以满足自己的建模需求。更多信息，请参阅贡献和行为准则 READMEs。