# Project: Deal Timing Assistant (prototype)

Online shopping in China often comes with stacked promotions—coupons, limited-time sales, membership discounts, and platform subsidies. The hard part is not *finding* a deal, but deciding:

**Is this the right moment to buy, given what the item is and how you’ll use it?**

This repository is an early-stage prototype that combines:

- **Pricing signals** (list price / discount / current price, and later: historical price context)
- **Product intent** (necessity vs. convenience vs. “treat yourself” vs. luxury)
- **Brand-aware assumptions** (e.g., durability / resale value / repairability as a placeholder score for now)

The output is intentionally **human-readable**: **Buy / Wait / Skip** with brief reasons.

---

## Status: Early Prototype (Learning Project)

I’m new to machine learning, so the current goal is to validate the workflow:

- define the problem clearly  
- design a feature schema that makes sense  
- build a minimal training + inference pipeline  
- keep outputs explainable  

---

## About the Dataset

The current dataset is **synthetic (AI-generated)** and used only for:

- testing the pipeline end-to-end
- validating feature engineering and scoring logic
- showcasing reproducible experiments

It is **not** a real-world benchmark and should not be used to claim market-level insights.

---

## What This Repo Provides (MVP)

- a simple feature schema for “purchase timing”
- training and inference scripts
- an explainable decision output format
- room for future integration of real price history data

---

## Roadmap (High Level)

- add historical price features (30/90/180-day low, volatility, promotion patterns)
- replace brand “placeholder scores” with data-driven signals
- ship a small interactive demo (CLI/Web)
- expand beyond China to international products once the framework stabilizes

---

## Contributing

If you’re interested, contributions are welcome—especially around:

better feature definitions for purchase intent

explainable scoring logic

lightweight demo UX

compliant ways to obtain or build real datasets

## Disclaimer

This is a learning and prototyping project. Outputs are not financial advice and should not be treated as authoritative shopping guidance.

# 项目：买入时机助手（原型）

在中国电商环境里，“优惠”经常是叠加的：优惠券、限时折扣、会员价、平台补贴……真正难的不是**找到便宜**，而是判断：

**结合商品本身的属性，以及你实际的使用方式，现在到底是不是一个适合买的时机？**

这个仓库是一个早期原型，尝试把下面三类信息放到同一个决策框架里：

- **价格信号**（标价 / 折扣 / 现价；后续可加入：历史价格背景）
- **购买动机**（必需品 vs. 生活便利品 vs. 取悦自己 vs. 奢侈品等）
- **品牌相关的经验假设**（例如耐用性 / 保值率 / 维修便利性——当前阶段先用占位评分表示）

输出会尽量保持**人类可读、可解释**：**买 / 等一等 / 不建议**，并给出简短理由。

---

## 当前状态：早期原型（学习项目）

我刚开始学习机器学习，所以当前阶段的重点是把整个流程跑通并可复现：

- 把问题定义清楚  
- 设计一个合理的特征字段（schema）  
- 搭建最小可用的训练 + 推理流程  
- 让输出保持可解释，而不是“黑箱分数”  

---

## 关于数据集

目前使用的数据集是 **AI 生成的合成数据（synthetic / fake data）**，主要用于：

- 端到端验证项目流程（从数据到输出建议）
- 测试特征工程与评分/模型逻辑
- 保证实验可复现、方便协作与迭代

这些数据**不是真实世界的价格/促销记录**，不应被用于得出“市场规律”或“实战最优策略”的结论。

---

## 这个仓库当前提供什么（MVP）

- 一套用于“购买时机判断”的基础字段设计（可扩展）
- 训练与推理脚本（便于复现）
- 可解释的建议输出格式（买/等/不建议 + 简短理由）
- 为后续接入真实历史价格数据预留结构空间

---

## 规划路线（高层）

- 引入历史价格特征（近 30/90/180 天最低价、波动、促销周期等）
- 将品牌“占位评分”逐步替换为可更新、可验证的数据指标
- 上线一个轻量可用的交互 Demo（命令行/网页）
- 框架稳定后扩展到海外商品（多币种、多平台、多促销节奏）

---

## 参与贡献

如果你也对这个方向感兴趣，欢迎参与（Issue / PR 都可以），尤其是：

- 更合理的“购买动机/商品属性”定义方式  
- 更可解释的评分逻辑与输出格式  
- 轻量 Demo 的交互设计（让普通用户能用）  
- 合规获取或构建真实数据集的思路（避免踩线）  

---

## 免责声明

本项目是学习与原型验证用途。输出结果不构成任何消费建议或财务建议，请结合个人需求与预算做决策。

