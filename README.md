# Popup-about-caring-for-friends（关心朋友弹窗提醒工具）

<div align="center">

**中文** | [English](README.en.md)

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Star](https://img.shields.io/github/stars/Qiongkura/Popup-about-caring-for-friends.svg)](https://github.com/Qiongkura/Popup-about-caring-for-friends/stargazers)
[![Issues](https://img.shields.io/github/issues/Qiongkura/Popup-about-caring-for-friends.svg)](https://github.com/Qiongkura/Popup-about-caring-for-friends/issues)

</div>

这是一个 Python 小工具，可以在屏幕上同时弹出 150 个温馨的提示窗口，向朋友表达关心和问候。每个窗口显示不同的暖心话语，随机分布在屏幕上，按空格键即可全部关闭。

- **批量弹窗**：一次性生成 150 个弹窗，营造满满的关心氛围；
- **随机位置**：窗口随机分布在屏幕上，减少重叠，视觉效果更佳；
- **个性化问候**：支持自定义人名，让每条消息都更贴心；
- **一键退出**：按空格键即可关闭所有弹窗。

## 功能

| 功能 | 说明 |
| --- | --- |
| 批量弹窗生成 | 一次性创建 150 个弹出窗口，显示关心和问候信息 |
| 随机位置分布 | 窗口随机分布在屏幕各处，智能减少重叠 |
| 随机背景颜色 | 每个窗口随机选择柔和的背景色，视觉效果更温馨 |
| 个性化人名 | 支持自定义人名，让问候更加个性化 |
| 一键退出 | 按空格键可立即关闭所有弹窗 |

## 技术实现

本项目基于 Python 的 tkinter 图形界面库实现。核心逻辑包括：

1. **窗口创建**：使用 `tk.Toplevel()` 创建子窗口，设置置顶属性
2. **内容渲染**：每个窗口显示随机选择的温馨话语，使用微软雅黑字体
3. **位置计算**：通过算法计算随机位置，确保窗口之间重叠度不超过 30%
4. **渲染优化**：使用 `update_idletasks()` 和 `update()` 强制即时渲染，避免延迟显示
5. **批量生成**：循环创建 150 个窗口，每个间隔 0.05 秒，实现逐个显示效果

## 📦 环境依赖

```bash
Python 3.x
tkinter（通常随 Python 一起安装）
```

## 安装与使用

1. 克隆仓库或下载 `main.py` 文件

```bash
git clone https://github.com/Qiongkura/Popup-about-caring-for-friends.git
cd Popup-about-caring-for-friends
```

2. 运行脚本

```bash
python main.py
```

3. 等待弹窗逐个显示，按空格键退出

## 📝 使用示例

```python
# 直接运行即可看到效果
python main.py
```

运行后，屏幕上会逐个弹出 150 个温馨的提示窗口，每个窗口显示不同的关心话语，背景颜色随机变化。

## ⚙️ 配置说明

| 配置项 | 说明 | 默认 |
| --- | --- | --- |
| person_name | 自定义人名，显示在问候语中 | "happy" |
| tips | 提示内容列表，可自行添加或修改 | 内置 30 条暖心话语 |
| bg_colors | 背景颜色列表，可自定义颜色 | 内置 11 种柔和颜色 |
| num_windows | 生成弹窗的数量 | 150 |
| overlap_threshold | 窗口重叠阈值（0-1） | 0.3（30%） |

## 🧪 测试

暂无自动化测试。可手动运行脚本，观察弹窗是否正常显示。

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建你的功能分支 (`git checkout -b feature/xxx`)
3. 提交你的修改 (`git commit -m 'feat: 新增xxx功能'`)
4. 推送到分支 (`git push origin feature/xxx`)
5. 打开 Pull Request

## 📄 许可证

本项目采用 [MIT](LICENSE) 许可证。

## 📮 联系方式

- GitHub：https://github.com/Qiongkura
- 微信：Qiongkura

## 已知限制

- 仅支持 Windows 系统（依赖 tkinter）
- 弹窗数量固定为 150 个，无法动态调整
- 无法单独关闭某个弹窗，只能全部关闭
- 部分系统可能需要管理员权限才能正常显示窗口

## 与相关项目的关系

- 本项目为独立工具，无关联项目