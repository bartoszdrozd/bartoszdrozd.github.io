# Bartosz Drozd - Personal Portfolio Website

A static portfolio website built with Flask and Frozen-Flask, deployed to GitHub Pages.

## Features

- **Flask framework** - Dynamic web application framework
- **Frozen-Flask** - Static site generation from Flask app  
- **Bootstrap** - Responsive frontend framework
- **FontAwesome** - Icon library
- **Mapbox integration** - Interactive maps for travel pages
- **Contact form** - Email contact functionality
- **Responsive design** - Mobile-friendly layout

## Quick Start

### Prerequisites

- Python 3.8+ 
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/bartoszdrozd/bartoszdrozd.github.io.git
cd bartoszdrozd.github.io
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables (optional):
```bash
# Create .env file for configuration
echo "SECRET_KEY=your-secret-key" > .env
echo "MAPBOX_ACCESS_KEY=your-mapbox-key" >> .env
echo "MAIL_USERNAME=your-email@gmail.com" >> .env
echo "MAIL_PASSWORD=your-app-password" >> .env
```

### Development

Run the development server:
```bash
python static-sitebuilder.py debug
```

Visit http://localhost:5000 to view the site.

### Build Static Site

Generate static files for deployment:
```bash
python static-sitebuilder.py build
```

Static files will be generated in the `docs/` directory.

## Project Structure

```
├── app/                    # Flask application
│   ├── templates/         # Jinja2 templates
│   ├── static/           # CSS, JS, images
│   ├── __init__.py       # App factory
│   ├── forms.py          # WTForms definitions
│   └── routes.py         # Route handlers
├── docs/                 # Generated static site
├── config.py            # Configuration settings
├── static-sitebuilder.py # Main build script
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Pages

- **About** (`/`) - Personal introduction and bio
- **Projects** (`/my-projects/`) - Portfolio of development projects  
- **Resume** (`/my-resume/`) - Professional experience and skills
- **Trips** (`/my-trips/`) - Travel maps and experiences
- **Contact** (`/contact/`) - Contact form

## Deployment

The site is automatically deployed to GitHub Pages using the files in the `docs/` directory. Any push to the main branch will update the live site at https://bartoszdrozd.github.io.

## Technologies Used

- **Backend**: Flask, Frozen-Flask, Flask-Mail, Flask-WTF
- **Frontend**: Bootstrap, FontAwesome, Mapbox GL JS
- **Deployment**: GitHub Pages
- **CI/CD**: GitHub Actions (or Travis CI)

## Contributing

This is a personal portfolio site, but suggestions and bug reports are welcome via GitHub issues.

## License

This project is open source and available under the MIT License.