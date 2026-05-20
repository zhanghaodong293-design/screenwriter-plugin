# Mode Registry — 子命令登记(单一事实源)

本文件是 `screenwriter` 全部子命令的唯一权威清单。新增/修改子命令时**先改这里**,SKILL.md 只引用本表。

创作 = **类型(1) × 时长(1) × 阶段(1)** 的组合。三轴各选一个。

---

## A. 类型模式(8)— 基于影片类型

决定惯例、母题、节拍侧重与雷区。详见 `references/genre_conventions.md`。

| 代号 | 类型 | 核心引擎 | 触发词 |
|------|------|---------|--------|
| `drama` | 剧情 | 人物在压力下的抉择与转变 | 剧情片, 文艺片, 写实, 生活流 |
| `comedy` | 喜剧 | 落差 / 错位 / 自嘲 | 喜剧, 搞笑, 喜剧片, 闹剧, 讽刺 |
| `romance` | 爱情 | 两人之间的引力与障碍 | 爱情, 爱情片, 言情, 浪漫, 暗恋 |
| `action` | 动作冒险 | 外部目标 + 物理险境 + 倒计时 | 动作, 冒险, 打斗, 追逐, 爆破, 任务 |
| `crime` | 悬疑犯罪 | 谜题 / 真相 / 道德灰度 | 悬疑, 犯罪, 推理, 凶案, 反转, 烧脑 |
| `scifi` | 科幻奇幻 | 一个"假如"前提推到极致 | 科幻, 奇幻, 末世, 赛博, 异世界, 设定 |
| `horror` | 恐怖惊悚 | 威胁逼近 + 失控 + 恐惧具象 | 恐怖, 惊悚, 鬼, 怪物, 心理惊悚 |
| `biopic` | 历史传记 | 真实人物/事件的戏剧化取舍 | 历史, 传记, 真人真事, 年代, 改编 |

## B. 时长模式(4)— 基于时长

决定结构蓝图、场数、节拍密度与信息容量。详见 `references/duration_blueprints.md`。

| 代号 | 时长 | 篇幅参考 | 结构要点 | 触发词 |
|------|------|---------|---------|--------|
| `micro` | 微电影 1-5 min | ~1-5 页 / 3-8 场 | **单一事件、单一转折、一个"扣"**;结尾即点题 | 微电影, 一分钟, 三分钟, 短视频剧情 |
| `short` | 短片 5-30 min | ~5-30 页 / 8-30 场 | 一条主线、一个核心冲突;三幕压缩,转折快 | 短片, 短剧情片, 学生作业短片 |
| `feature` | 院线长片 90-120 min | ~90-120 页 / 40-60 场 | 完整三幕 + 中点 + 副线;Save the Cat 15 拍 | 长片, 电影, 院线, 大电影, 长篇 |
| `episode` | 剧集单集 40-50 min | ~40-50 页 / 25-40 场 | 单集闭环 + 季度悬念;A/B/C 故事线;幕间钩子 | 剧集, 单集, 一集, 网剧, 连续剧, 美剧式 |

## C. 阶段模式(6)— 开发流程

决定本次产出物。可单步,也可连贯推进(详见 SKILL.md 流程图)。

| 代号 | 阶段 | 产出 | 触发词 | 参考/模板 |
|------|------|------|--------|----------|
| `logline` | 创意/Logline | logline + 主题句 + 3 个升级方向 | 一句话故事, logline, 写个创意, 立意 | `templates/logline_template.md` |
| `character` | 人物 | 人物小传(主角/对手/配角)+ 关系网 | 人物小传, 人物设定, 角色弧光, 人物关系 | `references/character.md` · `templates/character_bio_template.md` |
| `outline` | 大纲/节拍表 | 节拍表 + 一段式梗概 | 故事大纲, 节拍表, 大纲, beat sheet, 分幕 | `references/story_structure.md` · `templates/beat_sheet_template.md` |
| `scenelist` | 分场 | 分场表(场号/景/时/内外 + 目标/转折) | 分场, 分场表, 场次表, 场景清单 | `references/scene_craft.md` · `templates/scene_list_template.md` |
| `draft` | 成稿 | 中式剧本格式成稿 | 写成稿, 写出来, 写剧本, 出剧本, 成片剧本 | `references/screenplay_format_cn.md` · `templates/screenplay_template_cn.md` |
| `critique` | 评析/诊断 | 体检报告 + 优先级修改单 | 评析, 诊断, 改剧本, 看看我的剧本, 给意见 | `references/revision_diagnostics.md` |

---

## 路由规则

1. **三轴缺项处理**:`logline/character/outline/scenelist/draft` 需要类型+时长;缺了**先问**(题材模糊给候选)。`critique` 可只凭用户文本(类型/时长从文本推断)。
2. **一步到位**:用户给一句创意又说"直接写出来",依次走 `logline→outline→draft`;在 `outline` 处停下确认方向再续。
3. **跨类型**:可声明主类型 + 次类型(如"科幻悬疑"=`scifi` 为主、借 `crime` 的谜题节拍)。
4. **范例对照**:任何阶段需要"参考某类型经典怎么做",查 `references/reference_library_index.md` 调取片库文件。

## 统计
- 类型 8 / 时长 4 / 阶段 6。理论组合 8×4×6 = 192 种创作配置。
