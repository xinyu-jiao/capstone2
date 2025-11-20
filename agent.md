# Agent Work Log

This file tracks all modifications and work done by the AI agent.

---

## 2024-11-15 - Initial Website Creation

**Commit:** `feat: Create complete Meridian Ribbon capstone project website`

- Created `index.html` with all 11 required sections (a-k)
  - Hypothesis/Research Question
  - Project Description (100+ words)
  - Computational Methods (100+ words)
  - Design Methods (100+ words)
  - Precedents (6 projects with placeholders)
  - Proof of Concept (main focus section)
  - Audience description
  - Data types and examples
  - Materials & Sensors
  - Research/Bibliography (8+ sources)
  - Data Sources

- Created `styles.css` with dark theme styling
  - Deep blue/black background (#0a0e27)
  - Gold accent colors (#f4a261)
  - Responsive design for mobile, tablet, desktop
  - High contrast for accessibility
  - Smooth animations and transitions

- Created `script.js` for interactive features
  - Mobile navigation toggle
  - Smooth scrolling navigation
  - Active link highlighting
  - Scroll animations
  - Image lazy loading support

- Created documentation files
  - `README.md` - Usage and deployment guide
  - `images/README.md` - Image requirements
  - `videos/README.md` - Video requirements
  - `.gitignore` - Git ignore configuration

- Created design documentation
  - `website_design_doc.md` - Detailed design specifications
  - `website_wireframe.md` - Visual wireframes
  - `website_content_outline.md` - Content outline with all text

---

## 2024-11-15 - Color Palette Update (First Attempt)

**Commit:** `style: Update color palette to lighter, softer tones`

- Updated CSS variables to lighter color scheme
  - Background: #1a2332 (lighter blue-gray)
  - Accent: #d4a574 (softer gold/beige)
  - Text: Adjusted for better contrast
  - Shadows: Reduced opacity for softer appearance

---

## 2024-11-15 - Complete Color Palette Refactor

**Commit:** `refactor: Replace entire color palette with warm beige/cream theme`

### Changed Files:
- `styles.css` - Complete color system refactor
- `script.js` - Updated navbar colors and console messages

### Color System Changes:

**New CSS Variables:**
```css
--color-bg: #F6EDE1 (beige)
--color-bg-soft: #F9F3E7 (light beige)
--color-card: #FFF7EC (cream)
--color-sidebar: #F2E3CF (darker beige)
--color-primary: #F48A6A (coral orange)
--color-primary-soft: #F8A26C (light orange)
--color-accent-green: #2D6B4A (dark green)
--color-text-main: #332B24 (dark brown)
--color-text-muted: #7D6E5F (gray-brown)
--color-border: #E3D6C2 (light beige border)
--color-chip-bg: #FCE4DD (light pink)
```

**Updated Elements:**
- All background colors (page, cards, modules)
- All text colors (headings, body, muted text)
- All accent colors (links, buttons, highlights)
- All borders and shadows
- Navigation bar background and styling
- Footer styling
- Code block backgrounds
- Image placeholders
- All interactive elements

**Legacy Variable Mappings:**
- Added compatibility mappings for old variable names
- Ensures backward compatibility during transition

**JavaScript Updates:**
- Updated navbar scroll background colors
- Updated console log colors to match new theme

### Design Philosophy:
- Transformed from dark theme to light, warm beige/cream theme
- Maintains accessibility with proper contrast ratios
- Uses warm, earthy tones inspired by Traditional Chinese Medicine aesthetic
- Coral orange as primary accent provides warmth and energy

---

## 2024-11-15 - Precedents Content Planning

**Commit:** `docs: Create precedents content plan with user-provided links`

### Created File:
- `precedents_content_plan.md` - Detailed content plan for precedents section

### Changes:
- Identified 7 precedents to include:
  1. MIT inFORM (保留)
  2. Replika (保留)
  3. TCM Pulse Sensor - Nature article (保留，更新描述)
  4. SubPac X1 (保留，更新链接)
  5. Ear Seeds (保留)
  6. Feel Therapeutics (新增)
  7. Gua Sha (新增)

- Removed:
  - The Shape of Data (MIT Media Lab) - per user request

### User-Provided Links:
- https://www.nature.com/articles/s41378-022-00349-3 (TCM Pulse Sensor)
- https://www.earseeds.com/ (Ear Seeds)
- https://www.feeltherapeutics.com/ (Feel Therapeutics - new)
- https://subpac.com/x1/ (SubPac X1)
- https://www.healthline.com/health/gua-sha (Gua Sha - new)

### Content Plan Includes:
- Detailed descriptions for each precedent (50-100 words)
- Relevance explanations connecting to Meridian Ribbon project
- Key points highlighting important features
- Suggested organization by theme (TCM, Haptic Tech, Interaction Design)
- Format requirements for each precedent card

### Next Steps:
- Wait for user confirmation
- Update HTML with new precedents content
- Remove Shape of Data section

---

## 2024-11-15 - Update Precedents Section in HTML

**Commit:** `feat: Update precedents section with user-provided links and remove Shape of Data`

### Changed Files:
- `index.html` - Updated precedents section

### Changes Made:

**Removed:**
- The Shape of Data (MIT Media Lab) precedent card

**Updated:**
- **TCM Pulse Sensor** - Enhanced description based on Nature article
  - Added details about 3×3 pressure sensor arrays
  - Mentioned 3-dimensional pulse mapping
  - Emphasized similarity to doctor's fingertip sensations
  - Updated link: https://www.nature.com/articles/s41378-022-00349-3

- **SubPac** - Updated to SubPac X1
  - Added details about full-spectrum haptic feedback
  - Updated link: https://subpac.com/x1/
  - Enhanced description of haptic audio capabilities

- **Ear Seeds** - Enhanced description
  - Added more context about TCM theory
  - Mentioned specific applications (stress, sleep, mood, pain)

**Added:**
- **Feel Therapeutics** - New precedent card
  - Description of haptic therapy solutions
  - Connection to CARE mode and emotional support
  - Link: https://www.feeltherapeutics.com/

- **Gua Sha** - New precedent card
  - Description of TCM scraping therapy
  - Connection to meridian pathways and energy flow
  - Link: https://www.healthline.com/health/gua-sha

### Final Precedents List (7 total):
1. MIT inFORM
2. Replika
3. TCM Pulse Sensor (Nature)
4. SubPac X1
5. Ear Seeds
6. Feel Therapeutics (new)
7. Gua Sha (new)

### Content Improvements:
- All descriptions now 50-100+ words
- Clear relevance explanations for each precedent
- Better connection to Meridian Ribbon project's three modes
- More detailed technical information where applicable

---

## 2024-11-15 - Update Project Description

**Commit:** `docs: Update project description with concise, focused content`

### Changed Files:
- `index.html` - Updated Project Description section

### Changes Made:

**Old Description:**
- Long, detailed description (200+ words)
- Focused on technical implementation details
- Mentioned specific acupuncture points (Shaohai, Lingdao, Tongli, Shaofu, Shenmen)
- Detailed explanation of system components

**New Description:**
- Concise, focused description (3 paragraphs)
- Emphasizes AI-assisted sound-to-touch translation
- Highlights key features: rhythm, intensity, emotional tone analysis
- Mentions vibration and heat patterns
- Clear focus on blind and low-vision users
- Emphasizes alternative pathways for spatial awareness, emotional sensing, and non-visual communication

### Content Structure:
1. **Opening statement** - What Meridian Ribbon is
2. **How it works** - Sound analysis and translation to tactile patterns
3. **Purpose and audience** - Designed for blind/low-vision users and exploration goals

### Improvements:
- More accessible and easier to understand
- Better balance between technical detail and accessibility
- Clearer connection to AI and emotional sensing
- More focused on user benefits and exploration goals

---

## 2024-11-15 - Shorten Precedents Descriptions

**Commit:** `refactor: Condense precedents descriptions for better readability`

### Changed Files:
- `index.html` - Shortened all precedent descriptions

### Changes Made:

**Before:**
- Long descriptions (100-150+ words per precedent)
- Multiple sentences in both description and note sections
- Detailed technical explanations

**After:**
- Concise descriptions (30-50 words per precedent)
- Single sentence descriptions focusing on key features
- Shorter relevance notes (20-30 words)
- Maintained essential information while improving readability

### Specific Updates:

1. **MIT inFORM** - Reduced from 2 long paragraphs to 1 sentence + short note
2. **Replika** - Condensed methodology details, kept core concept
3. **TCM Pulse Sensor** - Shortened technical details, kept key points (3×3 arrays, 3D mapping)
4. **SubPac X1** - Reduced from detailed explanation to essential features
5. **Ear Seeds** - Condensed TCM theory, kept practical applications
6. **Feel Therapeutics** - Shortened to core therapeutic concept
7. **Gua Sha** - Condensed TCM explanation, kept meridian connection

### Benefits:
- Faster to read and scan
- Better visual balance on page
- Maintains all key information
- More accessible to general audience
- Easier to compare precedents

---

## 2024-11-15 - Update Research/Bibliography Section

**Commit:** `feat: Add complete bibliography with 11 research sources`

### Changed Files:
- `index.html` - Updated Research/Bibliography section

### Changes Made:

**Replaced placeholder bibliography with 11 actual research sources:**

1. **Nature TCM Pulse Sensor** - Wearable pulse monitoring system
   - Link: https://www.nature.com/articles/s41378-022-00349-3
   - Relevance: Shows meridian-based TCM ideas in wearable sensing

2. **MIT inFORM** - Shape-changing interface
   - Link: https://tangible.media.mit.edu/project/inform/
   - Relevance: Embodied interfaces, making data physical

3. **Quantizer/Shape of Data** - MIT Media Lab sonification platform
   - Link: https://www.media.mit.edu/projects/quantizer-sonification-platform-for-high-energy-physics-data/overview/
   - Relevance: Sonic-tactile data interfaces for blind users

4. **Acoustic Touch Research** - ResearchGate study
   - Link: https://www.researchgate.net/publication/374993206_An_investigation_into_the_effectiveness_of_using_acoustic_touch_to_assist_people_who_are_blind
   - Relevance: Sound-based orientation for blind users

5. **Braille Band** - ArXiv paper
   - Link: https://arxiv.org/abs/1901.03329
   - Relevance: Wrist-worn haptic communication device

6. **SAS Graphics Accelerator** - Perkins School summary
   - Link: https://www.perkins.org/resource/sas-graphics-accelerator-summary-page/
   - Relevance: Non-visual data access approaches

7. **Replika** - AI Companion
   - Link: https://replika.com/
   - Relevance: Ethical and emotional AI voice interface

8. **Ear Seeds** - TCM Auriculotherapy
   - Link: https://www.earseeds.com/
   - Relevance: TCM meridian logic in wearable devices

9. **Gua Sha** - Healthline article
   - Link: https://www.healthline.com/health/gua-sha
   - Relevance: Meridian pathways as directional flows

10. **Feel Therapeutics** - Emotion-sensing wearable
    - Link: https://www.feeltherapeutics.com/
    - Relevance: Combining sensing, emotion analysis, and wearable feedback

11. **SubPac X1** - Wearable audio system
    - Link: https://subpac.com/x1/
    - Relevance: Sound-to-touch vibroacoustic feedback

### Format:
- Each entry includes title, description, category, and link
- Descriptions explain relevance to Meridian Ribbon project
- Links are clickable and open in new tab
- Organized by category (TCM, Haptic Interfaces, Data Sonification, etc.)

### Improvements:
- All 11 sources properly cited with links
- Clear relevance explanations for each source
- Professional academic format
- Easy to navigate and reference

---

## 2024-11-15 - Fix Copyright Year

**Commit:** `fix: Update copyright year from 2024 to 2025`

### Changed Files:
- `index.html` - Updated year in footer, title, and project description

### Changes Made:
- Footer copyright: 2024 → 2025
- Footer project description: "Capstone Project 2024" → "Capstone Project 2025"
- Page title: "Capstone Project 2024" → "Capstone Project 2025"

### Reason:
- Current year is 2025, not 2024
- Ensures accurate copyright and project information

---

## 2024-11-15 - Remove Hero Image Placeholder and Mode Icons

**Commit:** `refactor: Remove hero image placeholder and emoji icons from mode cards`

### Changed Files:
- `index.html` - Removed hero image placeholder and mode card emojis

### Changes Made:

**Removed:**
- Hero section image placeholder div with "Placeholder: Device photo (1200x800px)" text
- Emoji icons (🧭, 🔍, 💚) from ORIENT, EXPLORE, and CARE mode cards in hero section
- Emoji icons from detailed mode cards in Proof of Concept section

**Updated:**
- Hero image now displays directly without placeholder fallback text
- Mode cards now show only text (ORIENT, EXPLORE, CARE) without emoji icons
- Cleaner, more minimal design

### Benefits:
- Cleaner visual design
- Less visual clutter
- More professional appearance
- Focus on text content rather than decorative elements

---

## 2024-11-15 - Fix Hero Layout and Remove Computational Methods Content

**Commit:** `fix: Reflow hero section layout and remove computational methods content`

### Changed Files:
- `index.html` - Fixed hero layout, removed computational methods content
- `styles.css` - Added hero-content-full class for centered single-column layout

### Changes Made:

**Hero Section:**
- Removed hero-image div completely
- Added `hero-content-full` class to hero-content
- Changed layout from 2-column grid to centered single-column
- Content now centered and takes full width (max 800px)
- No empty space where image used to be

**Computational Methods Section:**
- Removed all content (description, system architecture, code examples)
- Kept section title and structure
- Added placeholder text "Content to be added..."
- User will add content later

### CSS Updates:
- Added `.hero-content-full` class for centered, full-width content
- Added `.placeholder-text` style for empty sections
- Updated responsive breakpoints for hero layout

### Benefits:
- No empty space in hero section
- Better visual balance
- Cleaner layout without image
- Computational Methods section ready for future content

---

## 2024-11-15 - Remove A/B Comparison, Gua Sha, and Update Data Sources

**Commit:** `refactor: Remove A/B comparison section, Gua Sha precedent, and update data sources`

### Changed Files:
- `index.html` - Removed sections, updated data sources
- `styles.css` - Added link styling for data sources

### Changes Made:

**Removed:**
- **A/B Comparison section** - Entire "Design Approach: A/B Comparison" section removed from Design Methods
- **Gua Sha precedent** - Removed from Precedents section (now 6 precedents instead of 7)

**Updated:**
- **Data Sources section** - Completely replaced with new detailed content:
  1. Environmental Sound Data (UrbanSound Dataset)
  2. AI Emotion & Sound Classification Models (RAVDESS, CREMA-D, ESC-50)
  3. TCM Meridian Maps & Acupoint Diagrams (WHO, TCM Wiki)
  4. User Feedback & Embodied Testing
  5. Vibrotactile Pattern Libraries (SubPac, Skin-Integrated Haptics)

**New Data Sources Features:**
- Detailed source/provenance information
- Reference dataset links
- Politics/limitations analysis for each source
- Critical analysis of cultural biases and limitations
- Proper academic citations with clickable links

### CSS Updates:
- Added link styling for data source links
- Links use primary color with hover effects

### Benefits:
- More critical and transparent data source documentation
- Better acknowledgment of limitations and biases
- Professional academic format
- Cleaner design without A/B comparison section

---

## 2024-11-15 - Update TCM Meridian Source and Footer Contact Info

**Commit:** `update: Replace TCM Wiki with NCBI Bookshelf source and update footer contact information`

### Changed Files:
- `index.html` - Updated data source and footer links

### Changes Made:

**Data Sources Section:**
- Replaced TCM Wiki link with NCBI Bookshelf (NIH-published source)
- Updated description to reflect biomedical framing
- Updated politics/limitations note to address Western academic language translation

**Footer:**
- Updated email from placeholder to `xj2349@columbia.edu`
- Updated portfolio link from placeholder to `https://xinyu-jiao.github.io/`

### Benefits:
- More authoritative academic source (NIH/NCBI)
- Accurate contact information
- Working portfolio link

---

## 2024-11-15 - Add Author Info to Hero and Update Design Methods

**Commit:** `feat: Add Columbia GSAPP author information in hero section and update design methods content`

### Changed Files:
- `index.html` - Added author info section, updated design methods text
- `styles.css` - Added styling for hero info section

### Changes Made:

**Hero Section:**
- Added author information section below "Meridian Ribbon" title
- Displays:
  - Columbia GSAPP
  - Xinyu Jiao
  - Computational Design Practices: Colloquium 2 Fall 2025
- Styled with borders and appropriate typography hierarchy
- Positioned between title and subtitle

**Design Methods Section:**
- Completely replaced content with new, more concise text
- New text emphasizes:
  - Experimental approach with AI and embodied experimentation
  - Participatory design with blind/low-vision users
  - Speculative future of body-as-interface
  - Decolonizing approach through TCM
  - Alternative sensory experiences in computational design

### CSS Updates:
- Added `.hero-info` container with top/bottom borders
- Added `.hero-school`, `.hero-name`, `.hero-course` classes
- School and course use muted text color
- Name uses primary text color with medium weight
- Appropriate font sizes for hierarchy

### Benefits:
- Clear author and academic context in hero section
- More concise and focused design methods description
- Professional presentation with proper typography hierarchy

---

## 2024-11-15 - Replace Data & Materials Section with Materials & Sensors

**Commit:** `refactor: Replace entire Data & Materials section with new Materials & Sensors content`

### Changed Files:
- `index.html` - Completely replaced Data & Materials section
- `styles.css` - Added section-subtitle styling

### Changes Made:

**Section Title:**
- Changed from "Data & Materials" to "Materials & Sensors"
- Added subtitle: "How the system works without large datasets"

**New Content Structure:**
- **Three-column layout** (using existing data-grid):
  1. **Soft Materials** - Silicone, flexible fabric, thermoplastic sheets
  2. **Sound Input** - Phone microphone capturing real-time environmental sound
  3. **Tactile Modules** - Vibration motors and heat patches

- **Full-width row** (using content-box):
  - **AI Sound Analysis** - Lightweight AI model extracting emotional tone and sound features

**Removed:**
- All previous data types, visualizations, code examples
- Hardware grid with Arduino, sensors, etc.
- Materials comparison table

### CSS Updates:
- Added `.section-subtitle` class for subtitle styling
- Adjusted `.section-title` margin-bottom to accommodate subtitle
- Reused existing `.data-grid` and `.data-item` classes for three-column layout
- Used existing `.content-box` for full-width AI Sound Analysis section

### Benefits:
- Cleaner, more focused content
- Emphasizes system working without large datasets
- Better alignment with project's lightweight approach
- Maintains existing styling and layout structure

---

## 2024-11-15 - Remove Subtitle and Update Hero Subtitle Text

**Commit:** `refactor: Remove Materials & Sensors subtitle and change Interface to System in hero`

### Changed Files:
- `index.html` - Removed subtitle, updated hero subtitle text

### Changes Made:

**Materials & Sensors Section:**
- Removed subtitle "How the system works without large datasets"
- Section now only has main title

**Hero Section:**
- Changed "A Sound-to-Touch Wearable Interface Inspired by Traditional Chinese Medicine" to "A Sound-to-Touch Wearable System Inspired by Traditional Chinese Medicine"
- Changed "Interface" to "System" for more accurate terminology

### Benefits:
- Cleaner section header
- More accurate terminology (System vs Interface)

---

## 2024-11-15 - Add YouTube Video to SubPac X1 Precedent

**Commit:** `feat: Replace image placeholder with YouTube video embed for SubPac X1 precedent`

### Changed Files:
- `index.html` - Replaced image placeholder with YouTube iframe
- `styles.css` - Added video-container-small class for responsive video in precedent cards

### Changes Made:

**SubPac X1 Precedent Card:**
- Replaced image placeholder with YouTube video embed
- Video URL: https://youtu.be/xw09UUoEETM
- Embedded using responsive iframe with 16:9 aspect ratio

**CSS Updates:**
- Added `.video-container-small` class for video embeds in precedent cards
- Uses padding-bottom technique for responsive 16:9 aspect ratio
- Video scales properly within precedent card layout
- Maintains border-radius and proper overflow handling

### Benefits:
- Interactive video content instead of static placeholder
- Better demonstration of SubPac X1 functionality
- Responsive design that works on all screen sizes
- Maintains existing card layout and styling

---

## 2024-11-15 - Add Vimeo Video to MIT inFORM Precedent

**Commit:** `feat: Replace image placeholder with Vimeo video embed for MIT inFORM precedent`

### Changed Files:
- `index.html` - Replaced image placeholder with Vimeo iframe for inFORM precedent

### Changes Made:

**MIT inFORM Precedent Card:**
- Replaced image placeholder with Vimeo video embed
- Video URL: https://player.vimeo.com/video/79179138
- Uses existing `.video-container-small` class for responsive display
- Embedded using responsive iframe with 16:9 aspect ratio

### Benefits:
- Interactive video content demonstrating inFORM functionality
- Better visualization of shape-changing table interface
- Consistent with SubPac X1 precedent video implementation
- Responsive design that works on all screen sizes

---

## 2024-11-15 - Add Image to Replika Precedent

**Commit:** `feat: Replace image placeholder with actual image for Replika precedent`

### Changed Files:
- `index.html` - Replaced image placeholder with img tag for Replika precedent
- `styles.css` - Added styling for images in precedent-image containers

### Changes Made:

**Replika Precedent Card:**
- Replaced image placeholder with `<img>` tag
- Image path: `images/precedent-replika.jpg`
- Added fallback to show placeholder if image fails to load
- Image displays Replika AI Companion interface

**CSS Updates:**
- Added `.precedent-image img` styling
- Images use `object-fit: cover` for proper scaling
- Images fill the entire precedent-image container (200px height)
- Maintains aspect ratio and proper display

### Benefits:
- Visual representation of Replika interface
- Better user understanding of the precedent
- Consistent with other precedent cards
- Graceful fallback if image is missing

---

## 2024-11-15 - Add Image to Wearable Multichannel Pulse Monitoring Precedent

**Commit:** `feat: Replace image placeholder with actual image for TCM Pulse Monitoring precedent`

### Changed Files:
- `index.html` - Replaced image placeholder with img tag for TCM Pulse Monitoring precedent

### Changes Made:

**Wearable Multichannel Pulse Monitoring Precedent Card:**
- Replaced image placeholder with `<img>` tag
- Image path: `images/22.jpg`
- Added fallback to show placeholder if image fails to load
- Image displays TCM pulse sensor device

### Benefits:
- Visual representation of TCM pulse monitoring device
- Better user understanding of the precedent
- Consistent with other precedent cards
- Graceful fallback if image is missing

---

## 2024-11-15 - Add Images to Ear Seeds and Feel Therapeutics Precedents

**Commit:** `feat: Replace image placeholders with actual images for Ear Seeds and Feel Therapeutics precedents`

### Changed Files:
- `index.html` - Replaced image placeholders with img tags for two precedents

### Changes Made:

**Ear Seeds (TCM Auriculotherapy) Precedent Card:**
- Replaced image placeholder with `<img>` tag
- Image path: `images/seed.jpg`
- Added fallback to show placeholder if image fails to load

**Feel Therapeutics (Haptic Therapy) Precedent Card:**
- Replaced image placeholder with `<img>` tag
- Image path: `images/feel.jpg`
- Added fallback to show placeholder if image fails to load

### Benefits:
- Visual representation of both precedents
- Better user understanding of the projects
- Consistent with other precedent cards
- Graceful fallback if images are missing

---

## 2024-11-15 - Update Hero Section Text with New Project Concept

**Commit:** `refactor: Update hero section text to reflect new visual-to-sound-and-touch concept`

### Changed Files:
- `index.html` - Updated hero subtitle, research question, and three mode descriptions

### Changes Made:

**Hero Subtitle:**
- Changed from "A Sound-to-Touch Wearable System Inspired by Traditional Chinese Medicine"
- To: "A visual-to-sound-and-touch wearable + app system for blind and low-vision users, inspired by Traditional Chinese Medicine."
- Updated meta description tag accordingly

**Research Question:**
- Changed from "What if blind users could 'see' through sound and touch instead of vision?"
- To: "How can visual information be translated into sound and meridian-based vibration patterns on the wrist to help blind and low-vision people sense space and atmosphere through their body?"

**Three Modes - Updated Descriptions:**

**ORIENT:**
- Main text: "Environmental orientation through sound and vibration"
- Description: "Sensing nearby space, movement, and crowding in streets, corridors, and subway stations."

**EXPLORE:**
- Main text: "Exploring how different places 'feel' through non-visual cues"
- Description: "Using sound, rhythm, and wrist vibrations to notice patterns in daily routes and atmospheres."

**CARE:**
- Main text: "Body-based reflection and emotional support"
- Description: "Gentle vibration and soundscapes for checking in with mood and stress at home or in private settings."

### Benefits:
- Updated concept reflects visual-to-sound-and-touch translation
- More specific research question about visual information translation
- Enhanced mode descriptions with clearer purpose and context
- Better alignment with new project direction

---

## 2024-11-15 - Adjust Research Question Text Size

**Commit:** `style: Reduce research question font size to display in three lines`

### Changed Files:
- `styles.css` - Adjusted hypothesis-text font size and line height

### Changes Made:

**Research Question Styling:**
- Reduced font size from 1.25rem to 1.1rem
- Adjusted line height from 1.6 to 1.5 for tighter spacing
- Added max-width: 90% and margin: 0 auto for better text wrapping
- Text now displays in approximately three lines

### Benefits:
- More compact display of research question
- Better text wrapping and readability
- Maintains visual hierarchy while fitting more content

---

## 2024-11-15 - Update Project Description Section

**Commit:** `refactor: Update Project Description with new visual-to-sound-and-touch system description`

### Changed Files:
- `index.html` - Replaced Project Description content

### Changes Made:

**Project Description Section:**
- Completely replaced previous three-paragraph description
- New single-paragraph description emphasizes:
  - Visual-to-sound-and-touch translation system
  - Phone app camera reading environment
  - Interpreting states (street vs. corridor, quiet vs. crowded, calm vs. tense)
  - Translation into sound cues and meridian-inspired vibration patterns
  - Continuous tactile "ribbon" along the wrist
  - User experience: orient, sense atmosphere, reflect through hearing and touch
  - TCM meridians as body-centered interface language, not medicine

### Benefits:
- Updated description aligns with new project concept
- Clearer explanation of visual-to-sound-and-touch system
- Better understanding of camera-based environment reading
- Emphasis on TCM as interface language rather than medical application

---

## 2024-11-15 - Update Three Modes Section Details

**Commit:** `refactor: Update Purpose, Context, and Interaction text for all three modes`

### Changed Files:
- `index.html` - Updated detailed descriptions for ORIENT, EXPLORE, and CARE modes

### Changes Made:

**ORIENT Mode:**
- Purpose: "Quick environmental awareness and spatial orientation."
- Context: "Streets, corridors, subway stations, building entrances."
- Interaction: Updated to describe camera-based sensing, continuous vibration patterns (calm vs crowded), and voice command activation

**EXPLORE Mode:**
- Purpose: "Exploring how different routes and places 'feel' through non-visual cues."
- Context: "Daily commutes, repeated paths, visiting new neighborhoods."
- Interaction: Updated to describe logging states while walking, reviewing routes in app, replaying moments as sound cues and vibration patterns

**CARE Mode:**
- Purpose: "Body-based daily reflection and gentle emotional support."
- Context: "At home or in a private resting setting."
- Interaction: Updated to describe soft soundscape, replaying day as vibration sequence, voice command for summary with calming vibration pattern

### Benefits:
- More detailed and specific mode descriptions
- Better explanation of camera-based system functionality
- Clearer user interaction patterns
- Enhanced understanding of each mode's purpose and context

---

## 2024-11-15 - Update Core Interaction Cards to FLOW, SENSE, FOCUS

**Commit:** `refactor: Replace ORIENT/EXPLORE/CARE with FLOW/SENSE/FOCUS in Core Interaction section`

### Changed Files:
- `index.html` - Updated three mode cards in hero section

### Changes Made:

**CARD 1 - FLOW (replaces ORIENT):**
- Title: "FLOW"
- Subtitle: "Dynamic Navigation"
- Description: "Designed for movement. It translates the optical flow of the environment into a linear vibration that moves along the meridian. Smooth patterns indicate a clear path, while stuttered patterns signal obstruction."

**CARD 2 - SENSE (replaces EXPLORE):**
- Title: "SENSE"
- Subtitle: "Atmospheric Perception"
- Description: "Designed for stillness. It maps visual complexity and crowd density into tactile textures on the wrist. A calm environment feels like slow breathing waves, while a busy scene feels like granular noise."

**CARD 3 - FOCUS (replaces CARE):**
- Title: "FOCUS"
- Subtitle: "Active Information"
- Description: "Designed for interaction. Users point to query specific objects. The system responds with a precise haptic impulse (like an acupoint click) and provides an audio label for details."

### Benefits:
- Updated to reflect new computational design logic
- FLOW emphasizes optical flow and movement-based navigation
- SENSE focuses on atmospheric perception through tactile textures
- FOCUS enables active interaction through pointing and haptic feedback
- Better alignment with visual-to-sound-and-touch translation system

---

## 2024-11-15 - Simplify Core Interaction Cards Descriptions

**Commit:** `refactor: Simplify FLOW, SENSE, FOCUS card descriptions for clarity`

### Changed Files:
- `index.html` - Updated three mode cards with simpler, clearer descriptions

### Changes Made:

**CARD 1 - FLOW:**
- Subtitle: Changed from "Dynamic Navigation" to "Moving & Navigation"
- Description: Simplified to "Helps you move safely. The vibration feels like a smooth stream on your wrist when the path is clear. If there is an obstacle, the vibration 'stutters' to warn you."

**CARD 2 - SENSE:**
- Subtitle: Changed from "Atmospheric Perception" to "Feeling the Atmosphere"
- Description: Simplified to "Helps you feel the 'vibe' of a room. A quiet, empty space feels like slow breathing patterns. A busy, crowded place feels like rough, sandy textures."

**CARD 3 - FOCUS:**
- Subtitle: Changed from "Active Information" to "Point & Identify"
- Description: Simplified to "Helps you find specific objects. Just point your hand like a laser. The wrist gives a sharp 'click' vibration when it locks onto an object (like a sign or door), and then reads out the name."

### Benefits:
- Much simpler and clearer language
- More accessible and user-friendly descriptions
- Better understanding of each mode's function
- More intuitive explanations using everyday language

---

## 2024-11-15 - Rewrite Three Modes with Extremely Concrete Scenario-Based Descriptions

**Commit:** `refactor: Update Three Modes with extremely concrete, scenario-based descriptions for judges`

### Changed Files:
- `index.html` - Updated Three Modes cards with detailed scenario-based text
- `styles.css` - Changed `.mode-subtitle` to `.mode-scenario` for better semantic meaning

### Changes Made:

**CARD 1 - FLOW (Navigation):**
- Scenario: "Walking & Commuting"
- Metaphor: "Like a 'parking sensor' for your wrist"
- Clear Path: Smooth **water stream** flowing down arm = "Go ahead"
- Obstacle: **Stutters** or flows backward = "Stop, something is blocking the way"

**CARD 2 - SENSE (Atmosphere):**
- Scenario: "Standing still & observing"
- Metaphor: "'Touching the air' to feel the vibe"
- Busy/Crowded: **Rough textures** (like sandpaper) = chaotic place
- Quiet/Empty: **Slow, breathing waves** = calm and open space

**CARD 3 - FOCUS (Identification):**
- Scenario: "Pointing at objects"
- Metaphor: "Your finger becomes a 'scanner'"
- Action: Point hand like a laser at sign/object
- Feedback: Sharp **"Click"** (haptic impulse) + earbud reads name (e.g., "Starbucks")

**CSS Updates:**
- Renamed `.mode-subtitle` to `.mode-scenario` for semantic clarity
- Maintained existing styling for scenario, metaphor, and feeling sections
- Key sensations (water stream, stutters, rough textures, breathing waves, Click) are bolded

### Benefits:
- Extremely concrete and easy to understand for judges
- Clear scenario-based descriptions help visualize use cases
- Bolded key sensations make haptic language immediately clear
- Better visual hierarchy with Scenario/Metaphor/Feeling structure
- More accessible and user-friendly explanations

---

## 2024-11-15 - Update Audience & Users Section to Match Project Philosophy

**Commit:** `refactor: Update Audience section with improved descriptions matching project philosophy`

### Changed Files:
- `index.html` - Updated Primary and Secondary Audience cards with new titles and descriptions

### Changes Made:

**Primary Audience Card:**
- Title: Changed from "Primary Audience" to "Blind & Low-Vision Explorers"
- Description: Updated to emphasize:
  - **Intuitive spatial awareness** beyond traditional navigation
  - **Auditory fatigue** from constant screen-reader usage
  - Need for quieter, more somatic way to sense surroundings

**Secondary Audience Card:**
- Title: Changed from "Secondary Audience" to "Sensory Augmentation Enthusiasts"
- Description: Updated to emphasize:
  - **"Digital Detox"** and **Somatic Mindfulness**
  - Alternative to visual overload
  - Body as canvas for information
  - Rooted in **TCM and embodied cognition** philosophy

**Key Terms Bolded:**
- Intuitive spatial awareness
- Auditory fatigue
- Digital Detox
- Somatic Mindfulness
- TCM and embodied cognition

### Benefits:
- Better alignment with updated project philosophy
- More specific and targeted audience descriptions
- Clearer value proposition for each user group
- Emphasis on somatic and embodied interaction
- Connection to TCM and embodied cognition philosophy

---

## 2024-11-15 - Update Design Methods Section to Meet Assignment Requirements

**Commit:** `refactor: Expand Design Methods section to meet 100+ word requirement with structured content`

### Changed Files:
- `index.html` - Replaced Design Methods content with expanded, structured version

### Changes Made:

**Content Structure:**
- Split into multiple paragraphs for better readability
- Clear introduction stating the three main methods
- Three distinct paragraphs explaining each method in detail

**Method 1 - Experimental:**
- Uses AI to translate visual data (movement, crowd density) into vibration patterns
- Testing digital signals on skin to create new "tactile language" for navigation
- More specific than previous version

**Method 2 - Participatory:**
- Works directly with blind and low-vision users
- Co-design approach instead of guessing needs
- Real-world feedback to find natural and intuitive tactile patterns

**Method 3 - Speculative & Decolonizing:**
- Imagines future where bodies—not screens—are main interface
- Uses TCM concepts to explore non-Western ways
- Challenges how we normally build technology

**Key Terms Bolded:**
- experimental
- participatory
- speculative
- decolonizing

**Word Count:**
- New version exceeds 100 words requirement
- More detailed and structured than previous version
- Better explains each method with specific examples

### Benefits:
- Meets assignment requirement of at least 100 words
- More structured and easier to read
- Clearer explanation of each method
- Better connection between methods and project goals
- More specific examples and applications

---

## 2024-11-15 - Replace System Flow with Custom CSS Grid/Flexbox Diagram

**Commit:** `feat: Create custom System Flow Chart with CSS Grid/Flexbox matching warm organic theme`

### Changed Files:
- `index.html` - Replaced System Flow section with new 3-column architecture diagram
- `styles.css` - Added complete styling for system flow chart with warm organic theme

### Changes Made:

**New System Flow Chart Structure:**
- 3 main columns: INPUT (Visual Data), PROCESS (TCM Mapping Algorithm), OUTPUT (Somatic Language)
- 2 arrows with labels: "Computer Vision" and "Haptic Translation"
- Custom SVG icons for each column (Eye/Camera, Microchip/Brain, Hand/Arm)

**Column 1 - INPUT (The Eye):**
- Icon: Eye/Camera SVG (concentric circles)
- Label: "Visual Data"
- List items: Optical Flow, Entropy, Object ID

**Column 2 - PROCESS (The Bridge):**
- Icon: Microchip/Brain SVG (nested rectangles with center)
- Label: "TCM Mapping Algorithm"
- List items: Vector Logic, Density Map, Signal Locking

**Column 3 - OUTPUT (The Body):**
- Icon: Hand/Arm SVG (hand pointing upward)
- Label: "Somatic Language"
- List items: Flowing Stream, Rough Texture, Precise Click

**Styling (Warm Organic Theme):**
- Background: Transparent (matches page)
- Boxes: Light cards (#F4E6D8) with thin borders (#E4D3C3)
- Accent Color: Coral Orange (#F28B6C) for icons, arrows, and headers
- Text: Warm Dark Gray (#4B423D)
- Layout: CSS Grid (3 columns + 2 arrows) on desktop, stacks vertically on mobile

**Responsive Design:**
- Desktop: Horizontal layout with 3 columns and horizontal arrows
- Mobile: Vertical stack with rotated arrows (90 degrees)
- Smooth transitions and proper spacing

**CSS Implementation:**
- Used CSS Grid for main layout
- Flexbox for column internal layout
- Custom SVG icons for each column
- Styled arrows with labels
- Fully responsive with media queries

### Benefits:
- Clean, professional appearance
- Matches warm organic color theme
- Fully responsive design
- No external dependencies (pure CSS/HTML)
- Clear visual hierarchy and flow
- Better than placeholder image

---

## 2024-11-15 - Update Computational Methods to 4-Step Pipeline with Material Prototyping

**Commit:** `feat: Add 4-step computational workflow including Material Prototyping step`

### Changed Files:
- `index.html` - Updated Computational Methods to 4-step pipeline
- `styles.css` - Added styling for 4-card layout with arrows

### Changes Made:

**New 4-Step Pipeline Structure:**
- Step 01: SEEING (Input) - Camera sensor
- Step 02: MAPPING (Logic) - Meridian translation
- Step 03: PROTOTYPING (Material) - **NEW STEP** - Material testing
- Step 04: FEELING (Output) - Tactile language

**Step 01 - SEEING (Input):**
- Icon: Camera SVG
- Title: "SEEING"
- Subtitle: "Input"
- Text: "The camera acts as a sensor. It calculates **movement** and **crowd density** from the video feed."

**Step 02 - MAPPING (Logic):**
- Icon: Brain/Network SVG
- Title: "MAPPING"
- Subtitle: "Logic"
- Text: "The code translates this data onto the **Meridian lines** of the arm. This organizes the signals logically."

**Step 03 - PROTOTYPING (Material) - NEW:**
- Icon: Layered Material/Cube SVG
- Title: "PROTOTYPING"
- Subtitle: "Material"
- Text: "I test materials like **Silicone** (soft) and **Plastic** (hard). Materials act like **filters**—they change how the vibration travels on skin."

**Step 04 - FEELING (Output):**
- Icon: Hand with Waves SVG
- Title: "FEELING"
- Subtitle: "Output"
- Text: "The final result is a **Tactile Language**: Smooth waves for safety, sharp clicks for objects."

**Styling (Warm Organic Theme):**
- Background: #FFF7F0 for cards
- Accent Color: #F28B6C for icons, arrows, and strong text
- Clean, scientific but warm appearance
- Subtle shadows and hover effects

**Layout:**
- Desktop: 4 cards in horizontal row with arrows between
- Mobile: Vertical stack with rotated arrows
- CSS Grid with 7 columns (4 cards + 3 arrows) on desktop
- Responsive breakpoint at 1200px

**Arrows:**
- Animated pulse effect (2s ease-in-out infinite)
- Connect each step to show workflow
- Rotate 90 degrees on mobile

### Benefits:
- Explicitly includes Material Prototyping as computational step
- Clear 4-step workflow
- Simple, readable text
- Warm organic aesthetic
- Professional scientific appearance
- Fully responsive design

---

## 2024-11-15 - Add ProjectStoryboard Component and Remove System Architecture

**Commit:** `feat: Add ProjectStoryboard component with storyboard image, remove System Architecture section`

### Changed Files:
- `index.html` - Added ProjectStoryboard section, removed System Architecture section
- `styles.css` - Added styling for storyboard section with mix-blend-mode

### Changes Made:

**Removed Section:**
- Deleted entire "System Architecture" section including:
  - 3-column flow chart (INPUT, PROCESS, OUTPUT)
  - All arrows, labels, and SVG icons
  - Visual Data, TCM Mapping Algorithm, Somatic Language columns

**Added ProjectStoryboard Component:**

**Section Structure:**
- Title: "A Day with Meridian Ribbon"
- Subtitle: "Follow a user's journey, from an overwhelming commute to intuitive connection, as Meridian Ribbon redefines urban navigation."
- Image container: Centralized, responsive container for storyboard image

**Styling (Warm Organic Theme):**
- Background: Matches page background (#FFF7F0)
- Title: #F28B6C (Salmon Orange) - uses section-title class
- Subtitle/Text: #4B423D (Dark Grey)
- Image: Responsive (max-width: 100%, height auto)

**Image Styling (Crucial):**
- `mix-blend-mode: multiply;` - Makes white background of sketch transparent, blending perfectly with cream page background
- Border: 2px solid #E4D3C3 (Light Beige)
- Border-radius: 16px (rounded corners)
- Box-shadow: Subtle shadow for depth (0 4px 16px rgba(51, 43, 36, 0.08))
- Hover effect: Slight lift (translateY(-4px)) and enhanced shadow
- Framed like a visual narrative

**Layout:**
- Centered container with max-width: 1200px
- Responsive padding and spacing
- Placed after "Material Experiments" section, before "Audience" section

**Image Path:**
- Uses `images/storyboard.png`
- Alt text: "A Day with Meridian Ribbon - Storyboard"

### Benefits:
- Visual narrative component showing user journey
- Seamless integration with page background using mix-blend-mode
- Professional presentation with framing border
- Responsive and accessible
- Matches warm organic theme
- Cleaner page structure without redundant System Architecture

---

