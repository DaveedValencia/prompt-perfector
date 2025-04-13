# Prompt Perfecter 🎨

> Transform simple image ideas into detailed, AI-ready prompts with just one click!

Prompt Perfecter is a Streamlit web application that enhances basic image descriptions into comprehensive, detailed prompts suitable for AI image generation tools like DALL-E, Midjourney, or Stable Diffusion.

## 🌟 Features

- **Prompt Enhancement**: Automatically adds missing details to your basic image ideas
- **Structured Analysis**: Breaks down prompts into 8 key components:
  - Subject
  - Action
  - Style/Medium
  - Lighting/Mood
  - Camera Angle/Composition
  - Background/Environment
  - Specific Details/Accessories
  - Color Scheme/Palette
- **Dual View Interface**: See both the complete prompt and a detailed breakdown
- **Easy Sharing**: Copy enhanced prompts to use with your favorite image generation tools
- **Inspiration Gallery**: Ready-to-use example prompts to get your creativity flowing

## 🚀 Demo

Try it live: [Prompt Perfecter Demo](https://imagepromptbuilder.com)

## 📋 How It Works

1. Enter a basic image idea like "a Mexican cowboy in a toy package set"
2. Click "Enhance my prompt ✨"
3. The app analyzes your input using GPT-4o
4. Missing details are intelligently filled in based on context
5. View and copy your enhanced prompt!

**Before:**
```
a cowboy in a toy package set
```

**After:**
```
A cowboy standing heroically with hands on hips, in a 3D render in the style of Toy Story, with well-lit soft shadows to mimic product packaging, eye-level front view, centered, set inside a plastic toy package with colorful backing. Include cowboy hat, toy lasso, plastic blister packaging, character name label, and use vibrant reds, yellows, and blues typical of children's toys.
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.7+
- OpenAI API key

### Quick Start

1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/prompt-perfecter.git
   cd prompt-perfecter
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```
   For Windows:
   ```
   set OPENAI_API_KEY=your-api-key-here
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

5. Visit `http://localhost:8501` in your browser

### Requirements

```
streamlit>=1.30.0
openai>=1.5.0
```

## 📝 Usage Tips

- **Be specific** about your main subject for better results
- Add at least one distinctive element like style or setting
- Use examples in the app for inspiration
- The more details you provide, the less the AI needs to guess

## 🔮 Use Cases

- Create better prompts for AI art generators
- Learn what makes an effective image prompt
- Quickly generate detailed descriptions for creative projects
- Discover new artistic possibilities you hadn't considered

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-idea`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-idea`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io/) for the amazing framework
- [OpenAI](https://openai.com/) for their powerful API
- [David Valencia](https://github.com/DaveedValencia) for creating this tool

---

**Created by David Valencia**

**Learn how to vibe code -->** [YouTube](https://youtube.com/@DaveedValencia)

**Socials:** [X](https://x.com/DaveedValencia) | [IG](https://instagram.com/DaveedValencia) 🚀
