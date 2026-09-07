# 文档检索找回

![GitHub stars](https://img.shields.io/github/stars/ninggui/document-content-search)
![License](https://img.shields.io/github/license/ninggui/document-content-search)
[![SkillHub](https://img.shields.io/badge/SkillHub-在线安装-blue)](https://skillhub.cn/skills/document-content-search)

按内容片段找回用户文档：ima 检索+飞书全文检索+下载提取正文。

## 这是什么

一个可复用的 AI Agent 技能（Skill），来自真实业务场景沉淀，含完整执行流程、避坑清单与验证步骤。

## 快速使用

将本仓库放入 Agent 技能目录后，用对应触发词调用（见 SKILL.md），Agent 会自动加载并执行完整流程。

## 核心能力

| 能力 | 说明 |
|------|------|
| 内容片段→文档定位 |
| 飞书全文检索 |
| PPTX/文档正文提取 |

## 使用方式（安装）

- **Hermes**: 放入 `skills/` 目录
- **Claude**: 放入 `~/.claude/skills/`
- **其他 Agent**: 按对应 SKILL.md 格式放入技能目录
- **SkillHub 一键安装**: https://skillhub.cn/skills/document-content-search

## 优势

- 忘了文件名也能找回
- 多渠道检索兜底
- 提取脚本开箱即用

## 内容结构

- `SKILL.md` — 核心技能定义（触发条件、执行流程、避坑清单）
- `references/` — 可选参考文件

## 许可

MIT
