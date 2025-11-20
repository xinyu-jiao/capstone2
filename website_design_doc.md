# Meridian Ribbon - GitHub Pages 网站设计稿

## 整体设计概念

**设计风格：**
- 简洁、现代、可访问性优先
- 深色模式友好（考虑盲人用户）
- 高对比度文字
- 清晰的层次结构
- 响应式设计（移动端和桌面端）

**色彩方案：**
- 主色：深蓝/黑色背景（#0a0e27 或rgb(136, 201, 233)）
- 强调色：温暖的金色/琥珀色（#f4a261 或rgb(168, 160, 175)）- 代表能量流动
- 文字：高对比度白色/浅灰色（#ffffff / #e0e0e0）
- 辅助色：柔和的紫色/蓝色渐变（代表声音和振动）

**字体：**
- 标题：无衬线字体（如 Inter, Helvetica Neue）
- 正文：易读的无衬线字体（如 Open Sans, Roboto）
- 代码/技术内容：等宽字体（如 Fira Code, Monaco）

---

## 页面结构

### 1. 首页/导航栏

**顶部导航栏：**
```
[Logo/项目名称: Meridian Ribbon]  |  [About] [Prototype] [Research] [Contact]
```

**Hero Section（首屏大图区域）：**
- **左侧：** 项目标题 + 一句话假设
  - 大标题：**Meridian Ribbon**
  - 副标题：A Sound-to-Touch Wearable Interface Inspired by Traditional Chinese Medicine
  - 假设（Hypothesis）：**"What if blind users could 'see' through sound and touch instead of vision?"**
  - 简短描述（1-2句话）
  
- **右侧：** 
  - 主视觉图片：手腕佩戴设备的照片/渲染图
  - 或者：动态演示图（GIF/视频缩略图）
  - 图片说明：设备原型照片

**快速导航卡片（3个）：**
```
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│   ORIENT    │  │   EXPLORE   │  │    CARE     │
│  模式说明    │  │  模式说明    │  │  模式说明    │
│  [图标]      │  │  [图标]      │  │  [图标]      │
└─────────────┘  └─────────────┘  └─────────────┘
```

---

### 2. About / Project Description 页面

**布局：单栏，带侧边栏目录**

**a. Hypothesis / Research Question**
```
┌─────────────────────────────────────────┐
│  RESEARCH QUESTION                       │
│  ─────────────────────────────────────  │
│                                          │
│  What if blind users could 'see'        │
│  through sound and touch instead of     │
│  vision?                                 │
│                                          │
└─────────────────────────────────────────┘
```

**b. Project Description（至少100字）**
```
┌─────────────────────────────────────────┐
│  PROJECT DESCRIPTION                    │
│  ─────────────────────────────────────  │
│                                          │
│  This project develops a vision-        │
│  substitution system that uses the      │
│  Heart Meridian pathway on the arm as   │
│  a tactile channel for sensing space.   │
│  Five tactile modules are placed along  │
│  key acupuncture points — Shaohai,      │
│  Lingdao, Tongli, Shaofu, and Shenmen  │
│  — forming a continuous line of          │
│  perception from the wrist to the        │
│  elbow.                                 │
│                                          │
│  [继续完整描述...]                       │
│                                          │
│  At stake is the possibility of          │
│  transforming sound into a tactile      │
│  form of vision, using the body itself  │
│  as an interface across micro (skin),    │
│  limb (meridian), and environmental     │
│  (urban sound) scales.                  │
│                                          │
└─────────────────────────────────────────┘
```

**视觉元素：**
- 手腕经络图（标注5个穴位点）
- 设备佩戴示意图
- 系统架构流程图

---

### 3. Computational Methods 页面

**c. Computational Methods（100字）**
```
┌─────────────────────────────────────────┐
│  COMPUTATIONAL METHODS                  │
│  ─────────────────────────────────────  │
│                                          │
│  I'm using Arduino and Python to        │
│  connect sound input with vibration     │
│  output. Arduino controls the small     │
│  motors on the wristband, while Python │
│  helps process sound features like      │
│  pitch, rhythm, and emotion using       │
│  audio-analysis tools...                │
│                                          │
│  [完整100字描述]                         │
│                                          │
└─────────────────────────────────────────┘
```

**技术栈可视化：**
```
┌──────────┐    ┌──────────┐    ┌──────────┐
│  Python  │───▶│  Arduino │───▶│ Hardware │
│ (Audio   │    │  (Motor  │    │ (Motors, │
│ Analysis)│    │ Control) │    │ Sensors) │
└──────────┘    └──────────┘    └──────────┘
     │                │                │
     └────────────────┴────────────────┘
              Web Audio API
```

**代码示例区域（可选）：**
- 音频处理代码片段
- 振动映射算法示例

---

### 4. Design Methods 页面

**d. Design Methods（至少100字）**
```
┌─────────────────────────────────────────┐
│  DESIGN METHODS                         │
│  ─────────────────────────────────────  │
│                                          │
│  My project is experimental,            │
│  participatory, and a bit speculative.   │
│  It's experimental because I'm testing  │
│  new ways to map sound and touch on     │
│  the body...                            │
│                                          │
│  [完整描述，包括：                        │
│   - Experimental                        │
│   - Participatory                        │
│   - Speculative                         │
│   - Decolonizing]                       │
│                                          │
└─────────────────────────────────────────┘
```

**设计方法标签云：**
```
[Experimental] [Participatory] [Speculative] 
[Decolonizing] [Accessible] [Embodied]
```

**A/B对比图：**
- 展示从传统设计到推测性设计的转变
- 视觉化对比图

---

### 5. Precedents 页面

**e. Precedents（每个50-100字，带图片）**

**布局：卡片网格（每行2-3个）**

```
┌──────────────────┐  ┌──────────────────┐
│  [项目图片]       │  │  [项目图片]       │
│                  │  │                  │
│  MIT inFORM      │  │  Shape of Data   │
│  ──────────────  │  │  ──────────────  │
│  描述文字...      │  │  描述文字...      │
│  [链接]           │  │  [链接]           │
└──────────────────┘  └──────────────────┘

┌──────────────────┐  ┌──────────────────┐
│  [项目图片]       │  │  [项目图片]       │
│                  │  │                  │
│  Replika AI      │  │  TCM Pulse       │
│  ──────────────  │  │  Sensor          │
│  描述文字...      │  │  ──────────────  │
│  [链接]           │  │  描述文字...      │
└──────────────────┘  └──────────────────┘
```

**应包括的先例：**
1. MIT Tangible Media Group - inFORM
2. The Shape of Data (MIT Media Lab)
3. Replika (AI Companion)
4. Wearable Pulse Sensor Based on TCM
5. SubPac (Haptic Audio)
6. Ear Seeds (TCM Therapy)

---

### 6. Proof of Concept 页面（重点展示）

**f. Proof of Concept**

**布局：全宽，突出视觉内容**

**顶部：项目视频/演示**
```
┌─────────────────────────────────────────┐
│                                          │
│      [视频播放器/演示GIF]                 │
│      或交互式原型                         │
│                                          │
└─────────────────────────────────────────┘
```

**原型开发时间线：**
```
Phase 1: Concept Sketches
  └─ [草图图片1] [草图图片2] [草图图片3]

Phase 2: Hardware Prototype
  └─ [原型照片1] [原型照片2] [电路图]

Phase 3: Software Integration
  └─ [代码截图] [界面截图] [测试视频]

Phase 4: User Testing
  └─ [测试照片] [反馈图表] [迭代版本]
```

**三种模式的可视化：**
```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   ORIENT     │  │   EXPLORE    │  │    CARE      │
│              │  │              │  │              │
│  [模式图]     │  │  [模式图]     │  │  [模式图]     │
│              │  │              │  │              │
│  环境感知     │  │  数据探索     │  │  情感支持     │
│  导航辅助     │  │  信息理解     │  │  日常反思     │
└──────────────┘  └──────────────┘  └──────────────┘
```

**系统架构图：**
```
Sound Input → Analysis → Mapping → Bluetooth → Wristband → Vibration
     ↓           ↓          ↓          ↓           ↓           ↓
  [麦克风]    [Python]   [算法]    [传输]      [硬件]      [触觉反馈]
```

**材料实验：**
- 不同材料的照片（硅胶、织物、金属网等）
- 材料对比表

---

### 7. Audience 页面

**g. Audience**

```
┌─────────────────────────────────────────┐
│  PRIMARY AUDIENCE                       │
│  ─────────────────────────────────────  │
│                                          │
│  Blind and low-vision users             │
│  [用户画像/描述]                         │
│                                          │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  SECONDARY AUDIENCE                     │
│  ─────────────────────────────────────  │
│                                          │
│  Artists, musicians, sensory         │
│  researchers, accessibility advocates   │
│                                          │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  INCLUSIVITY CONSIDERATIONS              │
│  ─────────────────────────────────────  │
│                                          │
│  • How to make it accessible for        │
│    different wrist sizes                │
│  • Alternative placements (arm, leg)    │
│  • Cost considerations                  │
│  • Cultural sensitivity (TCM context)  │
│                                          │
└─────────────────────────────────────────┘
```

**用户测试照片/引用：**
- 测试参与者照片（需授权）
- 用户反馈引用

---

### 8. Data 页面

**h. Data**

```
┌─────────────────────────────────────────┐
│  DATA TYPES                             │
│  ─────────────────────────────────────  │
│                                          │
│  • Audio data (pitch, rhythm, volume)   │
│  • Emotion recognition data             │
│  • Spatial audio data (direction,       │
│    distance)                            │
│  • User feedback data                   │
│                                          │
└─────────────────────────────────────────┘
```

**数据可视化：**
- 音频波形图
- 情感分析图表
- 振动模式映射图
- 用户交互数据

**数据示例：**
```
[代码块显示数据格式]
{
  "timestamp": "2024-11-15T10:30:00Z",
  "audio_features": {
    "pitch": 440,
    "rhythm": 120,
    "volume": 0.7
  },
  "emotion": "calm",
  "vibration_pattern": [0.2, 0.5, 0.8, 0.5, 0.2]
}
```

---

### 9. Materials/Sensors 页面

**i. Materials/Sensors**

**硬件清单（带图片）：**
```
┌──────────────────┐  ┌──────────────────┐
│  [Arduino图片]    │  │  [传感器图片]     │
│  Arduino/ESP32   │  │  FSR Sensors     │
│  微控制器         │  │  压力传感器       │
└──────────────────┘  └──────────────────┘

┌──────────────────┐  ┌──────────────────┐
│  [电机图片]      │  │  [蓝牙模块图片]    │
│  Vibration      │  │  Bluetooth       │
│  Motors         │  │  Module          │
│  振动电机         │  │  蓝牙模块         │
└──────────────────┘  └──────────────────┘
```

**材料对比表：**
- 硅胶、织物、金属网等材料的对比
- 每种材料的特性和应用场景

**系统连接图：**
- 硬件连接示意图
- 电路图（如适用）

---

### 10. Research/Bibliography 页面

**j. Research/Bibliography（至少8个资源）**

**布局：有序列表，带注释**

```
1. [作者] "Title" (Year)
   [1-2句话说明与项目的关系]

2. [作者] "Title" (Year)
   [1-2句话说明与项目的关系]

3. [作者] "Title" (Year)
   [1-2句话说明与项目的关系]

... (至少8个)
```

**应包括的类别：**
- 可访问性设计
- 触觉界面研究
- 数据声化
- 中医理论
- 情感计算
- 可穿戴技术
- 空间感知

---

### 11. Data Sources 页面

**k. Data Sources**

```
┌─────────────────────────────────────────┐
│  DATA SOURCES                           │
│  ─────────────────────────────────────  │
│                                          │
│  1. NYC Open Data                       │
│     • 311 complaints                    │
│     • Air quality data                  │
│     • Subway delays                     │
│     [来源说明和政治考量]                 │
│                                          │
│  2. User-Generated Audio Data           │
│     [收集方法和伦理考虑]                 │
│                                          │
│  3. Public Audio Datasets               │
│     [来源和许可]                         │
│                                          │
└─────────────────────────────────────────┘
```

---

## 页面底部（Footer）

```
┌─────────────────────────────────────────┐
│  Meridian Ribbon                        │
│  Capstone Project 2024                  │
│                                          │
│  [GitHub链接] [Email] [其他链接]         │
│                                          │
│  © 2024 Xinyu (Shireen) Jiao           │
└─────────────────────────────────────────┘
```

---

## 交互元素

**1. 滚动动画：**
- 内容淡入效果
- 图片加载动画

**2. 导航：**
- 固定顶部导航栏
- 侧边栏目录（长页面）
- 返回顶部按钮

**3. 可访问性：**
- 键盘导航支持
- 屏幕阅读器友好
- 高对比度模式切换
- 字体大小调整

**4. 媒体：**
- 图片懒加载
- 视频嵌入（YouTube/Vimeo）
- 交互式原型（如适用）

---

## 移动端适配

- 单栏布局
- 汉堡菜单
- 触摸友好的按钮大小
- 响应式图片
- 简化导航

---

## 特殊页面元素

**1. 首页项目图片：**
- 尺寸：1200x800px（16:10比例）
- 格式：JPG/PNG
- 内容：设备佩戴在手腕上的清晰照片
- 备用：项目logo或概念图

**2. 视频嵌入：**
- 原型演示视频
- 用户测试视频
- 系统工作流程动画

**3. 交互式元素：**
- 可点击的经络图（显示穴位信息）
- 音频播放器（演示声音到振动的映射）
- 数据可视化交互图表

---

## 技术实现建议

**框架选择：**
- Jekyll（GitHub Pages原生支持）
- 或：纯HTML/CSS/JavaScript
- 或：React/Vue（需构建部署）

**必需功能：**
- Markdown支持（用于内容管理）
- 图片优化和懒加载
- 响应式设计
- SEO优化
- 可访问性检查

---

## 内容优先级

**高优先级（必须完成）：**
1. Hypothesis
2. Project Description
3. Proof of Concept（重点）
4. Computational Methods
5. Design Methods

**中优先级：**
6. Precedents
7. Materials/Sensors
8. Audience

**低优先级（如有时间）：**
9. Data（如果数据收集有限）
10. Research/Bibliography（可以逐步完善）
11. Data Sources（如果数据使用有限）

---

## 设计稿总结

这是一个**内容驱动、视觉辅助**的网站设计，重点展示：
- **项目的创新性**（声音到触觉的转换）
- **文化融合**（中医与现代技术）
- **可访问性**（为盲人用户设计）
- **原型开发过程**（从概念到实现）

整体风格应该**专业但温暖**，体现项目的**人文关怀**和**技术深度**。

