# Meridian Ribbon - 网站内容大纲

## a. Hypothesis / Research Question（一句话）

**content：**
```
What if blind users could 'see' through sound and touch instead of vision?
```

---

## b. Project Description（至少100字）

**内容：**
```
Meridian Ribbon is an AI-assisted sound-to-touch wearable interface inspired by Traditional Chinese Medicine.
The system listens to environmental sound, analyzes rhythm, intensity, and emotional tone through AI, and translates these qualities into vibration and heat patterns along meridian-inspired points on the wrist.

Designed for blind and low-vision users, the project explores how sound and touch can become alternative pathways for spatial awareness, emotional sensing, and non-visual communication.
```

**要点：**
- 至少100字
- 说明项目的意义（What is at stake?）
- 说明项目为建筑环境带来的新实践
- 说明项目探索的尺度和维度

---

## c. Computational Methods（100字）

**内容：**
```
I'm using Arduino and Python to connect sound input with vibration output. Arduino controls the small motors on the wristband, while Python helps process sound features like pitch, rhythm, and emotion using audio-analysis tools. Later, I plan to try TouchDesigner to see how sound energy could move across the wrist like a map or light pattern. These tools help me turn invisible sound data into something that can be felt and understood through space. The wrist becomes a small area where sound and data travel through the body. For me, computation here is not just technical—it's a way to translate sound into a physical and emotional experience. The workflow affords real-time translation between auditory and haptic domains, enabling users to perceive spatial and emotional information through embodied interaction rather than visual representation.
```

**要点：**
- 至少100字
- 不只是列出软件和数据
- 说明工作流程相对于所解决问题提供的优势（affordances）

---

## d. Design Methods（至少100字）

**内容：**
```
still thinking...
```

**要点：**
- 至少100字
- 说明设计方法使哪些实践成为可能
- 明确说明项目是：activist, analytic, critical, decolonizing, entrepreneurial, experimental, narrative, participatory, speculative 中的哪些（或组合）

---

## e. Precedents（每个50-100字，带图片）

### 1. MIT Tangible Media Group - inFORM

**图片：** inFORM项目照片

**描述：**
```
MIT's inFORM is a shape-changing table that reacts to human gestures, making data physical. The system uses actuator grids and computational mapping to translate digital input into haptic output. Its audience includes designers, accessibility researchers, and people needing embodied interaction. The methodology combines actuator arrays with computational mapping of input to haptic output. 

This precedent is relevant because it demonstrates how physical interfaces can translate abstract data into tangible experiences. However, my project differs by focusing on wearable, portable devices rather than table-scale installations, and by integrating sound-to-touch translation specifically for blind users. I expand on this idea by making it palm-sized, embedding sound cues, and integrating with wearables or IoT systems, creating a better world where abstract data becomes everyday sensory companionship.
```

**链接：** https://tangible.media.mit.edu/project/inform/


### 2. Replika (AI Companion)

**图片：** Replika应用截图

**描述：**
```
Replika is a chatbot app with adaptive, emotionally supportive voice/text interactions. Its audience includes general users seeking companionship and the mental health community. The methodology uses machine learning trained on dialogue, with feedback loops for tone adaptation.

This precedent shows how AI can provide emotional support through voice interaction. My project differs by focusing specifically on blind users' needs, prioritizing transparency and ethical voice design rather than commercial therapy-like chat. Instead of a general companion, I'm building an open-source, accessible, and transparent voice UI that gives blind users emotionally attuned, trustworthy digital partners.
```

**链接：** https://replika.com/

---

### 4. Wearable Pulse Sensor Based on Traditional Chinese Medicine

**图片：** TCM脉搏传感器研究图片

**描述：**
```
This research created a soft wearable wristband that measures pulse at three key TCM points (Cun, Guan, Chi) on the wrist. It uses air cushions and pressure sensors to detect pulse changes and convert them into digital data. The system consists of sensor arrays, signal processing, and three-dimensional signal fitting.

My project takes this idea further but in reverse: instead of measuring the body, I design a way for the body to feel the world—turning sound and emotion into vibration along the same meridian points. While their system tracks energy flow for diagnosis, mine uses energy flow for perception and interaction, creating a new sensory language between sound, body, and space.
```

**链接：** https://www.nature.com/articles/s41378-022-00349-3

---

### 5. SubPac (Haptic Audio)

**图片：** SubPac产品照片

**描述：**
```
SubPac is a wearable haptic audio system that translates sound into body sensations through vibration. It's used by musicians, audio professionals, and Deaf/hard-of-hearing users to experience music and audio through tactile feedback rather than just hearing.

This precedent demonstrates the value of vibroacoustic communication and shows that mainstream acceptance of non-visual audio interfaces is growing. My project builds on this by focusing specifically on spatial perception and environmental awareness for blind users, rather than just music appreciation. The technology validates the approach of using vibration to convey information that would otherwise be visual or auditory.
```

**链接：** https://subpac.com/

---

### 6. Ear Seeds (TCM Auriculotherapy)

**图片：** Ear Seeds产品/应用照片

**描述：**
```
Ear Seeds are a gentle, non-invasive practice from Traditional Chinese Medicine ear therapy (auriculotherapy). Small metal or crystal beads are taped onto specific points on the ear, providing light pressure and stimulating related meridian points. The ear is seen as a "mini map" of the whole body, with each point linking to certain body parts and emotions.

This precedent is relevant because it shows how TCM concepts of energy points and meridian pathways can be applied to wearable, non-invasive devices. My project adapts this concept to the wrist meridian points, using modern technology (vibration motors) instead of physical beads, but maintaining the principle of stimulating specific energy points to affect perception and well-being.
```

**链接：** https://www.earseeds.com/

---

## f. Proof of Concept（重点展示）

### 需要包含的内容：

1. **原型演示视频/GIF**
   - 设备工作演示
   - 用户测试视频
   - 系统工作流程动画

2. **开发时间线**
   - Phase 1: Concept Sketches（草图）
   - Phase 2: Hardware Prototype（硬件原型照片）
   - Phase 3: Software Integration（代码截图、界面截图）
   - Phase 4: User Testing（测试照片、反馈）

3. **三种模式可视化**
   - ORIENT模式：环境感知和导航
   - EXPLORE模式：数据探索和理解
   - CARE模式：情感支持和日常反思

4. **系统架构图**
   - Sound Input → Analysis → Mapping → Bluetooth → Wristband → Vibration

5. **材料实验**
   - 不同材料的照片和对比
   - 材料特性表格

6. **电路图和硬件连接**
   - 系统连接示意图

---

## g. Audience

**主要内容：**

### Primary Audience
```
Blind and low-vision users who need non-visual ways to perceive space, navigate environments, and understand data. These users face daily challenges with visual interfaces and seek alternative sensory modalities for interaction and information access.
```

### Secondary Audience
```
Artists, musicians, sensory researchers, accessibility advocates, and designers exploring embodied interaction. The system could also appeal to anyone interested in alternative sensory experiences or cultural fusion of traditional knowledge with modern technology.
```

### Inclusivity Considerations
```
• Different wrist sizes - adjustable design with flexible materials
• Alternative placements - device can be adapted for arm, leg, or torso placement
• Cost considerations - open-source approach to keep costs accessible
• Cultural sensitivity - respectful integration of TCM concepts, clearly positioned as inspiration rather than medical application
• Multiple language support - interface should support multiple languages for global accessibility
• Physical limitations - design should accommodate users with limited hand mobility
```

### User Testing
- 测试参与者照片（需获得授权）
- 用户反馈引用
- 测试结果摘要

---

## h. Data

**数据类型：**

1. **Audio Data**
   - Pitch（音高）
   - Rhythm（节奏）
   - Volume（音量）
   - Direction（方向）
   - Distance（距离）

2. **Emotion Recognition Data**
   - 情感分析结果
   - 语调特征

3. **Spatial Audio Data**
   - 环境声音的空间信息
   - 移动检测数据

4. **User Feedback Data**
   - 用户交互数据
   - 使用模式数据

**数据可视化：**
- 音频波形图
- 情感分析图表
- 振动模式映射图
- 用户交互数据可视化

**数据示例代码：**
```json
{
  "timestamp": "2024-11-15T10:30:00Z",
  "audio_features": {
    "pitch": 440,
    "rhythm": 120,
    "volume": 0.7,
    "direction": 45,
    "distance": 5.2
  },
  "emotion": "calm",
  "vibration_pattern": [0.2, 0.5, 0.8, 0.5, 0.2],
  "meridian_points": {
    "shaohai": 0.2,
    "lingdao": 0.5,
    "tongli": 0.8,
    "shenmen": 0.5,
    "shaofu": 0.2
  }
}
```

---

## i. Materials/Sensors

### Hardware Components

1. **Arduino/ESP32**
   - 微控制器
   - 用于控制振动电机和传感器

2. **FSR Sensors (Force Sensitive Resistors)**
   - 压力传感器
   - 检测触摸和压力

3. **Vibration Motors**
   - 小型振动电机
   - 沿手腕经络点放置

4. **IMU Sensor (Inertial Measurement Unit)**
   - 运动传感器
   - 检测方向和运动

5. **Bluetooth Module**
   - 蓝牙模块
   - 与移动应用通信

6. **Battery Module**
   - 电池模块
   - 为设备供电

### Materials

| Material | Properties | Tactile Sensation | Application |
|----------|------------|-------------------|-------------|
| Silicone | Soft, flexible | Smooth, cushioned | Calming mode, gentle pulse |
| Fabric/Felt | Breathable, form-fitting | Warm, skin-friendly | Long wear, emotional mode |
| Metal Mesh | Cool, rigid, heat-conductive | Clear, instant response | Precise signal feedback, directional mode |
| Leather/PU | Textured, warm to touch | Natural, authentic | Everyday use, emotional expression |
| Thermochromic Material | Temperature-responsive | Subtle tactile changes | "Energy flow" metaphor |
| 3D-Printed TPU/Flex Resin | Customizable softness | Adjustable damping | Experimental vibration mapping |

### System Connection Diagram
- 硬件连接示意图
- 电路图（如适用）

---

## j. Research/Bibliography（至少8个资源）

### 1. 可访问性设计
**[作者] "Title" (Year)**
[1-2句话说明与项目的关系]

### 2. 触觉界面研究
**[作者] "Title" (Year)**
[1-2句话说明与项目的关系]

### 3. 数据声化
**[作者] "Title" (Year)**
[1-2句话说明与项目的关系]

### 4. 中医理论
**[作者] "Title" (Year)**
[1-2句话说明与项目的关系]

### 5. 情感计算
**[作者] "Title" (Year)**
[1-2句话说明与项目的关系]

### 6. 可穿戴技术
**[作者] "Title" (Year)**
[1-2句话说明与项目的关系]

### 7. 空间感知
**[作者] "Title" (Year)**
[1-2句话说明与项目的关系]

### 8. 多感官交互
**[作者] "Title" (Year)**
[1-2句话说明与项目的关系]

**建议搜索的关键词：**
- Haptic interfaces for blind users
- Data sonification
- Traditional Chinese Medicine meridian theory
- Wearable haptic devices
- Spatial audio perception
- Affective computing
- Accessible design
- Embodied interaction

---

## k. Data Sources

**如果使用大量数据，需要列出：**

### 1. NYC Open Data
- **311 Complaints** - 时间和位置数据
- **Air Quality Data** - 空气质量数据
- **Subway Delays** - 地铁延误数据
- **来源说明：** 公开数据，由纽约市政府提供
- **政治考量：** 数据收集可能存在社区偏见，需要批判性分析

### 2. User-Generated Audio Data
- **收集方法：** 通过移动应用收集（需用户同意）
- **伦理考虑：** 隐私保护、数据匿名化、用户同意书

### 3. Public Audio Datasets
- **来源：** [具体数据集名称]
- **许可：** [使用许可说明]

**如果项目不主要依赖数据：**
可以说明项目主要使用实时音频输入，而非预存数据集。

---

## 首页项目图片要求

**规格：**
- 尺寸：1200x800px（16:10比例）
- 格式：JPG/PNG
- 内容：设备佩戴在手腕上的清晰照片
- 备用：项目logo或概念图

**建议：**
- 高质量照片，清晰展示设备
- 良好的光线和背景
- 展示设备实际使用场景

---

## 额外建议

1. **视频内容：**
   - 原型演示视频（2-3分钟）
   - 用户测试视频片段
   - 系统工作流程动画

2. **交互式元素：**
   - 可点击的经络图（显示穴位信息）
   - 音频播放器（演示声音到振动的映射）
   - 数据可视化交互图表

3. **时间线：**
   - 项目开发时间线
   - 从概念到原型的演进过程

4. **致谢：**
   - 感谢参与测试的用户
   - 感谢提供指导的导师
   - 感谢提供资源的机构

