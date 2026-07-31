# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目定位

本仓库是 **Python 数据结构与算法** 学习项目，基于 learn-anything 技能体系（`.claude/skills/learn-anything-*`）运行。目前不含业务代码，核心资产是学习主题数据（`.learn/`）和技能脚本（`.claude/skills/`）。所有与用户交互请使用中文。

## 核心架构：学习数据的单向数据流

```
.learn/topics/<topic>/state.json  ← 唯一数据源（v1 schema）
        │  render.mjs 校验并渲染
        ▼
.learn/topics/<topic>/knowledge-map.md  ← 生成物，禁止手写
.learn/topics/<topic>/sessions/<domain-slug>/  ← 学习会话文件（init-sessions.mjs 创建）
```

- **state.json 是唯一事实来源**：`domains → concepts` 两级层级，每个概念有 `status`（unexplored / in_progress / mastered / needs_practice）、`confidence`、`explain_count`、`practice_count` 等字段。更新学习状态 = 直接编辑 state.json 后重跑 render.mjs。
- **knowledge-map.md 是生成物**：由 `render.mjs` 从 state.json 渲染，永远不要手动编辑；校验失败时修改 state.json 再重跑。
- **sessions/ 目录**：学习会话文件按 domain 的 slug 分子目录存放，由 `init-sessions.mjs` 创建（幂等，可重复运行）。

## 常用命令

所有脚本通过 `find` 定位（脚本位于 `.claude/skills/learn-anything-*/scripts/`）：

```bash
# 校验 state.json 并生成知识地图（新建/修改主题后必跑）
SCRIPT=$(find . -path '*/learn-anything-topic/scripts/render.mjs' -print -quit 2>/dev/null)
node "$SCRIPT" ./.learn/topics/<topic>

# 初始化/补齐 domain 会话目录（幂等）
SCRIPT=$(find . -path '*/learn-anything-topic/scripts/init-sessions.mjs' -print -quit 2>/dev/null)
node "$SCRIPT" ./.learn/topics/<topic>
```

各技能（explain / practice / quiz / review / status / topic）各自携带专用脚本（如 `status.mjs`、`validate-quiz.mjs`），使用时按对应 SKILL.md 中的方式调用。

## 注意事项

- **`.learn/` 和 `.claude/` 是隐藏目录**：glob 和多数搜索工具默认跳过点目录，`**/state.json` 这类模式会返回空。必须用显式点路径（Read/Write）或 Bash（`ls -d .learn/topics/*/`）。
- 主题目录名与 slug 不同：目录名可为中文（如 `python数据结构与算法`），state.json 内的 `slug` 才是 kebab-case 标识符（脚本按 slug 建目录、存状态）。
- 用户可调用 `/learn <topic>` 初始化或加载主题；`/learn-explain`、`/learn-practice`、`/learn-quiz`、`/learn-review`、`/learn-status` 对应各学习环节。
- 本仓库没有测试、lint、构建配置——"运行"即指执行上述 node 脚本。
