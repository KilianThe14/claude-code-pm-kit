# Claude Code PM Kit

Claude Code for Product Managers. 这是一个面向通用产品经理的 Claude Code 工具包，提供全局 PM 工作方式、常用 skills、slash commands、模板和轻量脚本。目标是安装后可以直接处理 PRD、用户研究、竞品分析、优先级排序、会议纪要、方案评审、实验设计和上线复盘。

## 一条命令安装

```bash
curl -fsSL https://raw.githubusercontent.com/KilianThe14/claude-code-pm-kit/main/install.sh | bash
```

升级到最新版：

```bash
curl -fsSL https://raw.githubusercontent.com/KilianThe14/claude-code-pm-kit/main/install.sh | bash
```

健康检查：

```bash
~/.claude/scripts/pm-kit-healthcheck.sh
```

卸载并恢复安装前备份：

```bash
curl -fsSL https://raw.githubusercontent.com/KilianThe14/claude-code-pm-kit/main/uninstall.sh | bash
```

本地仓库安装：

```bash
git clone https://github.com/KilianThe14/claude-code-pm-kit.git
cd claude-code-pm-kit
./install.sh
```

## 安装内容

安装脚本会写入 `~/.claude`：

- `CLAUDE.md`：全局 PM 工作规则，默认中文沟通，强调问题、目标、指标、约束、风险和下一步。
- `skills/pm-prd`：生成或重写 PRD、用户故事、验收标准、非目标和需求澄清问题。
- `skills/pm-discovery`：访谈提纲、用户研究计划、访谈分析和机会点提炼。
- `skills/pm-prioritization`：RICE、ICE、MoSCoW、Kano 排序和路线图取舍。
- `skills/pm-competitive-analysis`：竞品矩阵、功能拆解、差异化机会和风险判断。
- `skills/pm-meeting-synthesis`：会议纪要、行动项、决策记录和风险同步。
- `skills/pm-review`：对 PRD、方案、路线图进行反方评审。
- `skills/pm-launch-retro`：上线 checklist、数据观察计划和复盘模板。
- `skills/pm-stakeholder-update`：面向老板、研发、设计、销售、客服的同步稿。
- `skills/pm-experiment-design`：实验假设、指标、分组、风险和验收标准。
- `skills/pm-user-story-mapping`：用户故事、任务流、MVP 边界和版本拆分。

Slash commands：

- `/prd`：从模糊需求生成澄清问题和 PRD 草稿。
- `/review-prd`：评审 PRD 或方案，指出指标、边界、依赖和风险缺口。
- `/research-plan`：生成用户研究计划和访谈提纲。
- `/analyze-interviews`：从访谈文本提炼痛点、证据和机会。
- `/prioritize`：对需求列表做排序并说明理由。
- `/competitive-analysis`：生成竞品分析结构和矩阵。
- `/meeting-notes`：整理会议纪要、行动项和决策记录。
- `/launch-checklist`：生成上线前后检查清单和观察计划。
- `/stakeholder-update`：生成不同对象的同步稿。
- `/experiment-plan`：生成实验方案、指标和风险控制。

模板：

- `standard-prd.md`：标准 PRD。
- `light-prd.md`：轻量 PRD。
- `requirements-clarification.md`：需求澄清清单。
- `user-interview.md`：用户访谈模板。
- `competitive-analysis.md`：竞品分析模板。
- `prioritization-scorecard.md`：优先级评分表。
- `experiment-design.md`：实验设计模板。
- `launch-retro.md`：上线复盘模板。

脚本：

- `scripts/rice_prioritizer.py`：读取 CSV 并输出 RICE 排序。
- `scripts/interview_synthesizer.py`：对访谈文本做轻量主题提取，并生成可交给 Claude 的分析提示。
- `scripts/pm-kit-healthcheck.sh`：安装健康检查入口。

## 第一个工作流示例

在 Claude Code 里输入：

```text
/prd 我们想做一个给销售团队用的客户风险提醒功能，最好下个季度上线
```

Claude 应先列出关键假设和澄清问题，然后给出一版 PRD 草稿，包括用户问题、业务目标、成功指标、用户故事、范围、非目标、依赖、风险和下一步。

继续评审：

```text
/review-prd 粘贴 PRD 内容
```

对多个需求排序：

```text
/prioritize 粘贴需求列表，并说明现有团队容量
```

上线前检查：

```text
/launch-checklist 粘贴功能、目标用户、灰度范围和关键指标
```

## 设计原则

- 默认中文输出，除非用户明确指定其他语言。
- 信息不足时先澄清，不编造公司事实、用户数据、商业指标或内部系统细节。
- 重要文档必须列出假设、证据、风险和待确认项。
- 默认不改代码，除非用户明确要求。
- 产出要适合 PM 推进协作：结论明确、责任清晰、下一步可执行。

## 安全与备份

首次安装会将会被覆盖的现有文件备份到 `~/.claude-pm-kit-backups/<timestamp>`，并在 `~/.claude/.pm-kit-manifest` 记录安装项。重复安装会更新 PM kit 文件，但不会反复备份已经安装过的内容。卸载脚本会移除 PM kit 文件，并尽量恢复首次安装前的备份。

可用环境变量改变安装位置，便于测试：

```bash
CLAUDE_HOME=/tmp/claude-test ./install.sh
CLAUDE_HOME=/tmp/claude-test ./healthcheck.sh
CLAUDE_HOME=/tmp/claude-test ./uninstall.sh
```

## 许可

本仓库使用 MIT 协议。

部分 PM 框架和表达方式参考了公开产品管理实践，并参考 Apache-2.0 的 `product-on-purpose/pm-skills` 做结构化改写。`deanpeters/Product-Manager-Skills` 使用 CC BY-NC-SA 4.0，本项目仅作灵感参考，不复制其内容。
