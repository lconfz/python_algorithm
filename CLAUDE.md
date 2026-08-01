# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目定位

本仓库是 **Python 数据结构与算法** 学习项目，基于 learn-anything 技能体系（`.claude/skills/learn-anything-*`）运行。目前不含业务代码。

- **`.learn/` 是主要学习目录（核心资产）**：学习数据全部存放在这里。虽然它名称以点开头，但它的地位是主目录而非隐藏/次要目录——所有学习相关操作都从这里读写，任何学习任务的起点都是检查 `.learn/topics/`。
- **`.claude/` 是工具支撑**：存放 learn-anything 技能（SKILL.md + 脚本）与 `/learn` 系列命令定义，一般不需要手动改动。

所有与用户交互请使用中文。

## 目录结构

```
python_algorithm/
├── .learn/                              ← 主要学习目录（核心资产）
│   └── topics/
│       └── python数据结构与算法/        # 目录名可为中文；state.json 内 slug 为 python-data-structures-and-algorithms
│           ├── state.json               # 唯一数据源（v1 schema）
│           ├── knowledge-map.md         # 生成物，禁止手写
│           └── sessions/                # 学习会话文件，按 domain 的 slug 分目录
│               ├── data-structures/
│               ├── fundamentals/
│               ├── algorithm-paradigms/
│               └── graph-algorithms/
├── .claude/
│   ├── commands/                        # /learn 系列命令（learn-topic/explain/practice/quiz/review/status.md）
│   └── skills/
│       ├── learn-anything-topic/        # SKILL.md + scripts/{render,init-sessions,utils}.mjs
│       ├── learn-anything-explain/      # SKILL.md + scripts/{render,utils}.mjs
│       ├── learn-anything-practice/     # SKILL.md + scripts/{render,utils}.mjs
│       ├── learn-anything-quiz/         # SKILL.md + scripts/{render,validate-quiz,utils}.mjs
│       ├── learn-anything-review/       # 仅 SKILL.md，无脚本
│       └── learn-anything-status/       # SKILL.md + scripts/{status,utils}.mjs
├── CLAUDE.md
└── README.md
```

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

脚本位置固定（`.claude/skills/learn-anything-topic/scripts/`）：

```bash
# 校验 state.json 并生成知识地图（新建/修改主题后必跑）
node .claude/skills/learn-anything-topic/scripts/render.mjs .learn/topics/<topic>

# 初始化/补齐 domain 会话目录（幂等）
node .claude/skills/learn-anything-topic/scripts/init-sessions.mjs .learn/topics/<topic>
```

各技能（explain / practice / quiz / review / status / topic）各自携带专用脚本（如 `status.mjs`、`validate-quiz.mjs`），使用时按对应 SKILL.md 中的方式调用。

## 注意事项

- **`.learn/` 是主要学习目录，始终用显式点路径访问**：点目录会被 glob 和多数搜索工具默认跳过（`**/state.json` 这类模式会返回空），这会让工具误以为它不重要——不要因此忽略它。学习数据全部在 `.learn/` 里，必须用显式点路径（Read/Write）或 Bash（`ls -d .learn/topics/*/`）读写。
- **主题目录名与 slug 不同**：目录名可为中文（如 `python数据结构与算法`），state.json 内的 `slug` 才是 kebab-case 标识符（脚本按 slug 建目录、存状态）。
- 用户可调用 `/learn <topic>` 初始化或加载主题；`/learn-explain`、`/learn-practice`、`/learn-quiz`、`/learn-review`、`/learn-status` 对应各学习环节。
- 本仓库没有测试、lint、构建配置——"运行"即指执行上述 node 脚本。
