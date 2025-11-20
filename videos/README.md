# Videos Folder

Place your prototype demonstration videos in this folder.

## Required Video

- `prototype-demo.mp4` - Main prototype demonstration (2-3 minutes)

## Video Guidelines

- **Format**: MP4 (H.264 codec recommended)
- **Duration**: 2-3 minutes
- **Size**: Try to keep under 50MB if hosting locally
- **Content**: Should show the device in action, user interactions, and key features

## Alternative: Video Hosting

Instead of hosting videos locally, you can:

1. **Upload to YouTube** and embed:
   - More reliable
   - Better performance
   - Automatic optimization
   - Analytics available

2. **Upload to Vimeo** and embed:
   - Professional appearance
   - Good quality
   - Privacy controls

## Embedding Videos

Edit `index.html` in the Proof of Concept section to replace the placeholder with:

**YouTube:**
```html
<iframe width="100%" height="500" 
  src="https://www.youtube.com/embed/YOUR_VIDEO_ID" 
  frameborder="0" 
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
  allowfullscreen>
</iframe>
```

**Vimeo:**
```html
<iframe src="https://player.vimeo.com/video/YOUR_VIDEO_ID" 
  width="100%" 
  height="500" 
  frameborder="0" 
  allow="autoplay; fullscreen; picture-in-picture" 
  allowfullscreen>
</iframe>
```

## Video Content Suggestions

- Device overview and features
- Three modes demonstration (ORIENT, EXPLORE, CARE)
- User testing footage (with consent)
- User testimonials
- Technical details and system architecture

