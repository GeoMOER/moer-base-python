---
layout: splash
title: Course Units
permalink: /units.html
sidebar:
        nav: "units"

feature_row:
  - image_path: assets/images/unit_images/u00/grid.png
    alt: "Unit 00"
    title: "Unit 00: How-to-Base-Python"
    excerpt: "Find out how this course is supposed to work."
    url: "/unit00/unit00-01_learning_environment.html"
    btn_label: "Show me more"
    btn_class: "btn--primary"

  - image_path: assets/images/unit_images/u01/grid.png
    alt: "Unit 1"
    title: "Unit 01: Overview and the very basics"
    excerpt: "Setting up Python and introducing some help tools."
    url: "/unit01/unit01-01_Overview.html"
    btn_label: "Show me more"
    btn_class: "btn--primary"

  - image_path: assets/images/unit_images/u02/grid.png
    alt: "Unit 2"
    title: "Unit 02: Basic data types"
    excerpt: "Introduction to basic data types."
    url: "/unit02/unit02-01_Overview.html"
    btn_label: "Show me more"
    btn_class: "btn--primary"

  - image_path: assets/images/unit_images/u03/grid.png
    alt: "Unit 3"
    title: "Unit 03: Working with String and simple operators"
    excerpt: "Introduction to mathematical, comparison and logical operators."
    url: "/unit03/unit03-01_Intro.html"
    btn_label: "Show me more"
    btn_class: "btn--primary"

  - image_path: assets/images/unit_images/u04/grid.png
    alt: "Unit 4"
    title: "Unit 04: Conditionals"
    excerpt: "Introduction to if, elif, and else."
    url: "/unit04/unit04-01_Intro.html"
    btn_label: "Show me more"
    btn_class: "btn--primary"

  - image_path: assets/images/unit_images/u05/grid.png
    alt: "Unit 5"
    title: "Unit 05: Object Data Types"
    excerpt: "Introduction to lists, matrices, data frames, arrays"
    url: "/unit05/unit05-01_Intro.html"
    btn_label: "Show me more"
    btn_class: "btn--primary"
    
  - image_path: assets/images/unit_images/u06/grid.png
    alt: "Unit 6"
    title: "Unit 06: Loops"
    excerpt: "Introduction to loops."
    url: "/unit06/unit06-01_Intro.html"
    btn_label: "Show me more"
    btn_class: "btn--primary"
    
  - image_path: assets/images/unit_images/u07/grid.png
    alt: "Unit 7"
    title: "Unit 07: Working with Files"
    excerpt:  "Introduction to working with Files"
    url: "/unit07/unit07-01_Intro.html"
    btn_label: "Show me more"
    btn_class: "btn--primary"
    
  - image_path: assets/images/unit_images/u08/grid.png
    alt: "Unit 08"
    title: "Unit 08: Simple Visualizations"
    excerpt: "Introduction to simple graphic outputs."
    url: "/unit08/unit08-01_Intro.html"
    btn_label: "Show me more"
    btn_class: "btn--primary"

  - image_path: assets/images/unit_images/u09/grid.png
    alt: "Unit 9"
    title: "Unit 09: OOP"
    excerpt:  "Introduction to OOP"
    url: "/unit09/unit09-01_Intro.html"
    btn_label: "Show me more"
    btn_class: "btn--primary"
    
  - image_path: assets/images/unit_images/u10/grid.png
    alt: "Unit 10"
    title: "Unit 10: Review"
    excerpt:  "Course Review"
    url: "/unit10/unit10-01_Intro.html"
    btn_label: "Show me more"
    btn_class: "btn--primary"

  - image_path: assets/images/spotlights/grid.png
    alt: "Spotlights"
    title: "Spotlights"
    excerpt: "Some Spotlights to make your life easier."
    url: "/unit99/sl01_Intro.html"
    btn_label: "Show me more"
    btn_class: "btn--danger"
---

# Overview of Course Units

{% for post in site.posts limit: 5 %}
  {% include archive-single.html %}
{% endfor %}

{% include feature_row id="intro" type="center" %}

{% include feature_row %}

<!---
your comment goes here
-->