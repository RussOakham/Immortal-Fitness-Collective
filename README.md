# **Immortal Fitness Collective** - by Russell Oakham

## **Project overview**

## **Deployed site**

## **Table of Contents**

- [**Deployed site**](#deployed-site)
  - [1. **UX**](#1-ux)
    - [**User Stories**](#user-stories)
    - [**Structure**](#structure)
    - [**Skeleton**](#skeleton)
    - [**Surface**](#surface)
      - [**Colour & Styling**](#colour--styling)
      - [**Language/Tone**](#languagetone)
      - [**Styling Considerations**](#styling-considerations)
  - [2. **Features**](#2-features)
    - [**Existing Features**](#existing-features)
    - [**Features to consider implementing in future**](#features-to-consider-implementing-in-future)
  - [3. **Database Design**](#3-database-design)
    - [**Indexes**](#indexes)
      - [**Recipes**](#recipes)
    - [**Queries**](#queries)
      - [**Browsing**](#browsing)
      - [**Users**](#users)
      - [**Searching**](#searching)
      - [**Uploading**](#uploading)
  - [4. **Technologies Used**](#4-technologies-used)
  - [5. **Testing**](#5-testing)
  - [6. **Deployment**](#6-deployment)
    - [Database Deployment](#database-deployment)
    - [Application Hosting](#application-hosting)
    - [**Heroku**](#heroku)
      - [Creating a Heroku app](#creating-a-heroku-app)
      - [Setting Environmental Variables](#setting-environmental-variables)
      - [Deployment](#deployment)
      - [Automatic Deployment](#automatic-deployment)
    - [GitHub and GitPod repository management](#github-and-gitpod-repository-management)
    - [**How to clone 'Immortal Fitness Collective' in GitHub and GitPod.**](#how-to-clone-immortal-fitness-collective-in-github-and-gitpod)
  - [7. **Credits**](#7-credits)
    - [**Design and research**](#design-and-research)
    - [**Technical**](#technical)
    - [**Content**](#content)
    - [**Media**](#media)
      - [Recipe Category Images:](#recipe-category-images)
      - [404 Error Page](#404-error-page)
    - [**Acknowledgements**](#acknowledgements)

## 1. **UX**

Overview of UX design decisions, including examples of websites I have viewed as part of research and inspiration.

### **User Stories**

&nbsp;

### **Structure**

Overview of site and page structure, explaining functionality and purpose.

&nbsp;

### **Skeleton**

At this point I began creating wireframes, using the above structure considerations. I used [Balsamiq](https://balsamiq.com/) these below;

### **Surface**

This is the sensory design section of a website, or how it looks, feels and sounds.

#### **Colour & Styling**

<details>
<summary>Colour Palette</summary>

</details>

I also used a selection of off-white and off-black colours to provide additional accenting to general white/black website elements, such as backgrounds and fonts.

#### **Language/Tone**

#### **Styling Considerations**

Before beginning development, I listed some styling ideas that I felt benefit the website. The majority of these can be seen in the wireframes.

- Favicon: Desktop and Mobile.
- Navigation
  - Sticky top
  - Mobile: 'Burger' menu icon, expanding on click.
  - Logo: Navigates to the home page on click.

## 2. **Features**

### **Existing Features**

&nbsp;

### **Features to consider implementing in future**

&nbsp;

## 3. **Database Design**

MongoDB was the database solution used for the website development, using the below, structured plan.

&nbsp;

## 4. **Technologies Used**

<details>
<summary>
Languages
</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/HTML">HTML</a> - Programming language providing content and structure of the website.</li>
<li><a href="https://en.wikipedia.org/wiki/CSS">CSS</a> - Programming language providing styling of the website.</li>
<li><a href="https://en.wikipedia.org/wiki/JavaScript">JavaScript</a> - Programming language used for various interactive elements of the website, including game logic, audio options etc.</li>
<li><a href="https://en.wikipedia.org/wiki/Python_(programming_language)">Python</a> - Programming language used to drive core site functionality including user login and push/retrieving database information.</li>
<li><a href="https://en.wikipedia.org/wiki/Jinja_(template_engine)">Jinja</a> - Used to generate HTML from site templates</li>
</ul>
</details>

<details>
<summary>Libraries</summary>
<ul>
<li><a href="https://getbootstrap.com/">Bootstrap CSS Framework</a> - Library of pre-built HTML and CSS components, used for various aspects of the site, such as navigation bar.</li>
<li><a href="https://fontawesome.com/">Font Awesome</a> - Library used for icons, such as social links and other images.</li>
<li><a href="https://fonts.google.com/">Google Fonts</a> - Font style library.</li>
<li><a href="https://jqueryui.com/">jQuery</a> - JavaScript library used for simplification of JS scripts and DOM manipulation.</li>
<li><a href="https://flask.palletsprojects.com/en/1.1.x/">Flask</a> - Micro-framework to simplify Python scripting and web server tasks.</li>
<li><a href="https://werkzeug.palletsprojects.com/en/1.0.x/">Werkzeug</a> - Python library to manage user management integrity.</li>
</ul>
</details>

<details>
<summary>Editors</summary>
<ul>
<li><a href="https://github.com/">GitHub</a> - Remote code repository.</li>
<li><a href="https://gitpod.io/">GitPod</a> - IDE (Integrated Development Environment), for writing, editing and saving code.</li>
<li><a href="https://dbdiagram.io/">dbDiagram</a> - Used to plan and visualise database structure</li>
<li><a href="https://balsamiq.com/">Balsamiq</a> - Wireframes for visual design testing.</li>
</ul>
</details>

<details>
<summary>Tools</summary>
<ul>
<li><a href="https://cloudinary.com/">Cloudinary</a> - Plugin used for upload and hosting of user images</li>
<li><a href="https://tinypng.com/">TinyPNG</a> & <a href="https://tinyjpg.com/">TinyJPG</a> -  Minimise image file sizes and maximise page load speed.</li>
<li><a href="https://www.remove.bg/">remove.bg</a> - Remove backgrounds from png images.</li>
<li><a href="https://www.canva.com/">Canva</a> - Color Palette Generation and Logo</li>
<li><a href="https://imagecolorpicker.com/">Image Color Picker</a> - Determine Hex code color in exisiting graphics</li>
<li><a href="https://realfavicongenerator.net/">Real Favicon Generator</a> - Generate favicons and icons for desktop and mobile usage.</li>
<li><a href="https://autoprefixer.github.io/">Autoprefixer</a> - Vendor prefixes to CSS rules.</li>
<li><a href="http://ami.responsivedesign.is/">Am I Responsive?</a> - Responsive design demo in ReadMe summary.</li>
<li><a href="https://www.responsivedesignchecker.com/">Responsive Design Checker</a> - Check website response across device types.</li>
<li><a href="https://www.lambdatest.com/">Lambdatest</a> - Check website response across device types.</li>
</ul>
</details>

<details>
<summary>Database Management</summary>
<ul>
<li><a href="https://www.mongodb.com/">MongoDB</a> - Cloud based database management system, used for storing user profile and recipe information.</li>
</ul>
</details>

<details>
<summary>Deployment Platform</summary>
<ul>
<li><a href="https://www.heroku.com/">Heroku</a> - Remote hosting platform, for hosting of python driven websites and applications.</li>
</ul>
</details>

&nbsp;

## 5. **Testing**

The testing process can be seen in the [TESTING.md](testing.md) document.

&nbsp;

## 6. **Deployment**

### Database Deployment

### Application Hosting

### **Heroku**

The site is hosted using [Heroku](https://www.heroku.com/), deployed directly from the master branch of GitHub. The deployed site will update automatically as new commits are pushed to the master branch.

#### Creating a Heroku app

- From the Heroku dashboard:

  - Select "New"
  - Select "Create new app"

    ![Create New App](assets/README/images/heroku-create-new-app.PNG)

- Add new app details to form:

  - Add app name (must be unique)
  - Select region
  - Click "Create App"

    ![Create New App Details](assets/README/images/heroku-app-name-and-region.PNG)

#### Setting Environmental Variables

- From the Heroku dashboard:

  - Select your app from the list

    ![Heroku App]()

- Select "Settings" from the top menu:

  - Under 'Config Vars', select "Reveal Config Vars"
  - Add environment variables in key-value pairs, click "Add" to add additional pairings.

    ![Config-Vars](assets/README/images/heroku-config-vars.PNG)

#### Deployment

- Create required deployment files in the repository:

  - requirements.txt

    - Lists the required python modules for Heroku to install.
    - To create:
      - In your IDE terminal, type: pip freeze > requirements.txt

  - Procfile

    - Tells Heroku the command to launch the app.
    - To create:
      - in your IDE terminal, type: python app.py > Procfile

  - .gitignore (optional)
    - Lists files and directories which should be deployed to live app, such as files with environmental passkeys.
    - To create:
      - In your IDE terminal, type: touch .gitignore
      - List the files and directories to be excluded from live deployment, within the .gitignore file.
      - Save in your repository root directory.

- From the application top menu:

  - Select 'Deploy'
  - Choose your Deployment method:

    - Github:

      - Select the correct Github account.
      - Type in the repository name you wish to deploy.
      - Choose the correct repository from search results.
      - Select "Connect"

      ![Connect GitHub Repo](assets/README/images/heroku-connect-github-repo.PNG)

    - Manual Deployment:

      - Choose the correct branch you wish to deploy from the drop-down.
      - Select "Deploy Branch"
      - Heroku will return "Your App has successfully deployed". If this shows an error, troubleshooting will be needed.

      ![Deploy Branch](assets/README/images/heroku-deploy-branch.PNG)

#### Automatic Deployment

- From the application top menu:
  - Select 'Deploy'
  - Ensure app is connected to correct repository
  - Under 'Automatic Deployment' section:
    - Select 'Enable Automatic Deployment"

### GitHub and GitPod repository management

### **How to clone 'Immortal Fitness Collective' in GitHub, GitPod and setup on Heroku.**

To run a version of the site locally, you can clone this repository using the following steps;

In a code editor of your choice;

1. Go to [GitHub.com](https://github.com/)
2. Click on 'Responsitories'
3. Click on 'Immortal Fitness Collective'
4. Click on the 'Code' button.
5. Under 'HTTPS' click the clipboard icon to the right of the URL.
6. In your IDE of choice, open a repository or create a new repository.
7. Open Terminal \('Terminal' then 'New Terminal' from the top ribbon menu in GitPod.\)
8. Type 'git clone', paste URL link and press enter.

Additional information around these cloning steps can be found on [GitHub Pages Help Page](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).
&nbsp;

#### Installing Requirements

- Install all requirements modules to your local IDE with the following CL:

```
 pip3 install -r requirements.txt
```

#### Create Collections in MongoDB

- Login to your MongoDB account
- Create a Cluster

- Create a database using the following architecture;

<details>
Placeholder
</details>

#### Setup Environmental Variables

### Setup Unique Identifies / Environment Variables

#### SECRET_KEY

#### MONGO_URI

#### MONGO_DBNAME

This is the name of your database in MongoDB. Which can be foung under the 'Collections' tab, under your cluster.

#### Running Development Server

To launch a Http server using the development mode code for the application, use the following command in your IDE:

```

Placeholder

```

## 7. **Credits**

### **Design and research**

The following are websites and articles that I used for reference and inspiration:

### **Technical**

- [Real Favicon Generator](https://realfavicongenerator.net/) - For the generation of Favicon icons and code.
- [Materialize Docs](https://materializecss.com/getting-started.html) - For guidance on Materialize use and adaptations.
- [CSS-Tricks](https://css-tricks.com/) - For implementing CSS effects such as box-shadow.
- [w3Schools](https://www.w3schools.com/) - For checking proper syntax of HTML and CSS elements.
- [Autoprefixer](https://autoprefixer.github.io/) - For generating CSS browser prefixes.
- [Stackoverflow](https://stackoverflow.com/) - For researching and troubleshooting JavaScript and Python code issues.
- [Miguel Grinberg](https://blog.miguelgrinberg.com/index) - For researching and troubleshooting Python functionality and code issues.
- [MongoDB Documentation](https://docs.mongodb.com/) - For researching and troubleshooting database code commands and issues.

### **Content**

All text content on the site was written originally by myself, with the below notes;

### **Media**

The photos and images used for this site were obtained.

- [**Shutterstock**](https://www.shutterstock.com/): From the following contributors;

#### 404 Error Page

### **Acknowledgements**

- Thanks to my mentor, [Precious Ijege](https://github.com/precious-ijege) for his suggestions, time and support.
- Thanks to those on Slack for reviewing my project and making suggestions.
- Thanks to my housemates, friends and family for reviewing the project and offering constructive feedback.
