---
layout: project
title: "My Personal Portfolio"
date: 2026-02-03
author: Bartosz Drozd
icon: 💼
categories: [web, flask, portfolio]
tags: [flask, tailwind, python]
github: https://github.com/bartoszdrozd/bartoszdrozd.github.io
demo: https://bartoszdrozd.github.io
---

# My Personal Portfolio Website

A modern, minimalist portfolio website built with Flask and Tailwind CSS.

## Features

- 🚀 **Fast Performance** - Static site generation with Frozen-Flask
- 🎨 **Modern Design** - Clean UI with Tailwind CSS
- 🌙 **Dark Mode** - Automatic dark mode support
- 📱 **Responsive** - Works on all devices
- 📝 **Blog System** - Write posts in Markdown
- 💼 **Projects Showcase** - Display your work

## Tech Stack

- **Backend:** Flask 3.x
- **Frontend:** Tailwind CSS 3.x
- **Blog:** Markdown with frontmatter
- **Deployment:** GitHub Pages

## Getting Started

```bash
# Clone the repository
git clone https://github.com/bartoszdrozd/bartoszdrozd.github.io.git

# Install dependencies
pip install -r requirements.txt

# Install frontend dependencies
npm install

# Run in development mode
npm run serve

# Build static site
npm run build:static
```

## Customization

### Adding a Blog Post

Create a new file in `_posts/` with frontmatter:

```yaml
---
layout: post
title: "Your Post Title"
date: 2026-02-03
author: Your Name
categories: [category1, category2]
tags: [tag1, tag2]
---

Your content here...
```

### Adding a Project

Create a new file in `_projects/` with frontmatter:

```yaml
---
layout: project
title: "Your Project"
date: 2026-02-03
icon: 🚀
categories: [web, python]
tags: [flask, api]
github: https://github.com/your-repo
---

Your project description...
```

---

*Built with ❤️ and ☕*
