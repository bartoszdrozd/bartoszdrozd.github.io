#!/usr/bin/env python3
"""
Basic tests for the portfolio website
"""

import os
import subprocess
import sys

def test_build():
    """Test that the static site builds successfully"""
    print("Testing static site build...")
    result = subprocess.run([sys.executable, 'static-sitebuilder.py', 'build'], 
                          capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Build failed with error: {result.stderr}")
        return False
    
    # Check that docs directory exists and has expected files
    expected_files = ['index.html', 'about/index.html', 'my-projects/index.html', 
                     'my-resume/index.html', 'my-trips/index.html', 'contact/index.html']
    
    for file_path in expected_files:
        full_path = os.path.join('docs', file_path)
        if not os.path.exists(full_path):
            print(f"Expected file not found: {full_path}")
            return False
    
    print("✓ Build test passed")
    return True

def test_templates():
    """Test that all required templates exist"""
    print("Testing template files...")
    templates_dir = 'app/templates'
    expected_templates = ['base.html', 'about.html', 'my-projects.html', 
                         'my-resume.html', 'my-trips.html', 'contact.html', 
                         '404.html', '500.html']
    
    for template in expected_templates:
        template_path = os.path.join(templates_dir, template)
        if not os.path.exists(template_path):
            print(f"Expected template not found: {template_path}")
            return False
    
    print("✓ Template test passed")
    return True

def test_static_files():
    """Test that static files exist"""
    print("Testing static files...")
    static_dir = 'app/static'
    if not os.path.exists(static_dir):
        print(f"Static directory not found: {static_dir}")
        return False
    
    # Check for favicon
    favicon_path = os.path.join(static_dir, 'img', 'favicon.ico')
    if not os.path.exists(favicon_path):
        print(f"Favicon not found: {favicon_path}")
        return False
    
    print("✓ Static files test passed")
    return True

def main():
    """Run all tests"""
    print("Running portfolio website tests...\n")
    
    tests = [test_templates, test_static_files, test_build]
    passed = 0
    
    for test in tests:
        if test():
            passed += 1
        else:
            print("❌ Test failed")
            return 1
        print()
    
    print(f"All {passed}/{len(tests)} tests passed! 🎉")
    return 0

if __name__ == '__main__':
    sys.exit(main())