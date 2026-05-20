# Screenwriter — 编剧大师

一个以「世界经典电影剧本」为师的编剧工作台,带你**像专业编剧那样分阶段开发**剧本:从一句话创意,逐步打磨到可拍摄的中式格式成稿,并能做评析诊断。

> 核心信念:**好剧本是改出来的,不是写出来的。** 结构先行、人物为王、对白见人、每场有转折。

---

## 三轴(子命令)

每次创作 = **类型 × 时长 × 阶段** 的组合。

- **类型 (8)**:剧情 / 喜剧 / 爱情 / 动作冒险 / 悬疑犯罪 / 科幻奇幻 / 恐怖惊悚 / 历史传记
- **时长 (4)**:微电影(1-5min) / 短片(5-30min) / 院线长片(90-120min) / 剧集单集(40-50min)
- **阶段 (6)**:创意/logline → 人物 → 大纲(节拍表) → 分场 → 成稿 → 评析

完整登记见 `skills/screenwriter/MODE_REGISTRY.md`。

## Slash 命令

| 命令 | 阶段 |
|------|------|
| `/sw` | 入口:自由描述,自动解析类型/时长/阶段 |
| `/sw-logline` | ① 创意 / Logline |
| `/sw-character` | ② 人物小传 |
| `/sw-outline` | ③ 故事大纲 / 节拍表 |
| `/sw-scenelist` | ④ 分场表 |
| `/sw-draft` | ⑤ 成稿(中式剧本格式) |
| `/sw-critique` | ⑥ 评析 / 诊断 |

也可直接用自然语言触发,如「写一个悬疑短片的故事大纲」「这是我的剧本,评析一下」。

---

## 安装

### 方式一:作为插件(可分发)
```
/plugin marketplace add <你的GitHub仓库>      # 如 yourname/screenwriter-plugin
/plugin install screenwriter
```

### 方式二:作为个人技能(手动)
把 `skills/screenwriter/` 整个文件夹拷到 `~/.claude/skills/screenwriter/` 即可(无需插件层)。

---

## 关于经典剧本范例库

技能可调取一座本地经典剧本库作为**范例对照**(见 `skills/screenwriter/references/reference_library_index.md`)。

- **范例库本身不随插件分发**(版权 + 体积原因)。索引里记录的是本机路径。
- 没有范例库时技能**照常工作**——库仅用于"向经典学结构"的可选增强。
- 若你有自己的剧本库,改 `reference_library_index.md` 里的路径与片单即可。

---

## 结构

```
screenwriter-plugin/
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── commands/              # 7 个 /sw-* slash 命令
├── skills/
│   └── screenwriter/      # 技能本体(SKILL.md + references + templates + examples)
└── README.md
```

## 设计要点(向 academic-research-skills 范式学习)
- 路由式 `SKILL.md` + `MODE_REGISTRY.md` 单一事实源
- 按需加载的 `references/`(craft/结构/人物/对白/格式/类型/时长/诊断)与 `templates/`
- IRON RULES + Anti-Patterns 固化创作纪律
- 片库做成"可调取的范例语料",学其骨不抄其肉

## License
MIT(技能提示词与文档)。经典剧本范例库版权归原作者,不包含于本包。
