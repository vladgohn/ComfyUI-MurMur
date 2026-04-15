<div align="right">
  <a href="#english">English</a> | <a href="#简体中文">简体中文</a> | <a href="./README.zh-CN.md">中文文件</a>
</div>

<div align="center">

# 🦄 MurMur

### Candy-grade color styling for ComfyUI nodes and groups

</div>

## English

`MurMur` is a tiny ComfyUI custom-node package made for one unapologetically simple job:
decorate your graph fast.

No giant utility pack. No “install 80 extra nodes for one picker” nonsense.
Just a lightweight floating picker for color, a small emoji strip for node labels,
and a workflow that stays out of your way.

![MurMur screenshot](./img/murmur_screen.png)

### ✦ Why MurMur Exists

Most color pickers in the ComfyUI ecosystem arrive as side features inside big packs.
That is a bad trade if the only thing you actually want is:

1. Select a node or group
2. Open a picker instantly
3. Color it
4. Continue working

`MurMur` exists specifically for that exact use case.

### ✦ What It Does

- Opens a floating color picker with `Tab`
- Colors selected nodes
- Colors selected groups
- Adds emoji prefixes to selected node titles
- Remembers picker position when dragged by the header
- Keeps a quick-access slot for the last used color
- Resets color back to the default theme color

### ✦ Important Behavior

- Emoji labels apply to selected nodes only
- Groups can be colored, but emoji are not inserted into group titles
- Clicking outside the picker closes it
- The package includes only one simple registered node, because the UI tool is the real point

### ✦ Installation

1. Copy this folder into `ComfyUI/custom_nodes/`
2. Restart ComfyUI
3. Search for `MurMur`

### ✦ Usage

1. Select a node or a group
2. Press `Tab`
3. Pick a color, reuse the last-used slot, or reset color
4. Optionally click an emoji to prefix selected node titles
5. Click outside the picker to close it

### ✦ Files

- [__init__.py](./__init__.py): ComfyUI package registration
- [murmur_picker.py](./murmur_picker.py): the single registered node
- [js/murmur.js](./js/murmur.js): floating picker UI, color logic, emoji palette

### ✦ README Language Note

GitHub README files do not support real interactive language tabs.
This repository uses an in-page language switcher at the top of `README.md`
and also provides a dedicated [README.zh-CN.md](./README.zh-CN.md).

---

## 简体中文

`MurMur` 是一个非常小的 ComfyUI 自定义节点包，只做一件事：
让你的工作流更快、更顺手地“装饰起来”。

不需要安装一个庞大的节点包，不需要为了一个颜色选择器顺带背上一堆没用的功能。
它就是一个轻量悬浮颜色面板，加上一小排 emoji 标签，专门服务于节点和分组的快速美化。

![MurMur 截图](./img/murmur_screen.png)

### ✦ 为什么会有 MurMur

ComfyUI 里很多颜色相关功能都只是大包里的附带功能。
如果你真正想要的只是下面这件事：

1. 选中节点或分组
2. 秒开颜色面板
3. 改一下颜色
4. 继续工作

那装整包并不划算。

`MurMur` 就是专门为这个场景做的。

### ✦ 功能

- 按 `Tab` 打开悬浮颜色选择器
- 给已选中的节点上色
- 给已选中的分组上色
- 给已选中的节点标题加 emoji 前缀
- 可以拖动标题栏移动面板，并记住位置
- 调色板里保留“最近一次使用的颜色”
- 可以恢复为主题默认颜色

### ✦ 重要说明

- Emoji 只会写入已选中的节点标题
- 分组可以上色，但不会写入 emoji 到分组标题
- 点击面板外部即可关闭
- 这个包只注册了一个简单节点，因为真正的重点是这个 UI 工具

### ✦ 安装

1. 把整个目录复制到 `ComfyUI/custom_nodes/`
2. 重启 ComfyUI
3. 在节点列表中搜索 `MurMur`

### ✦ 使用方法

1. 选中节点或分组
2. 按 `Tab`
3. 选择颜色、使用最近颜色，或恢复默认颜色
4. 如有需要，点击 emoji 给已选中节点标题加前缀
5. 点击面板外部关闭

### ✦ 文件

- [__init__.py](./__init__.py)：ComfyUI 包注册
- [murmur_picker.py](./murmur_picker.py)：唯一注册的节点
- [js/murmur.js](./js/murmur.js)：悬浮选择器 UI、颜色逻辑、emoji 调色板

### ✦ 语言切换说明

GitHub 的 README 不支持真正可交互的语言标签页。
所以这个仓库采用：

- `README.md` 顶部页内语言切换入口
- 单独的 [README.zh-CN.md](./README.zh-CN.md) 中文文件
