# We-Glove-Boxing

We-Glove-Boxing is a (fictitious) online retailer providing boxing clothing, footwear, equipment and accessories for sale. The idea for this final milestone project is to provide the visitor with a fully functioning, interactive e-commerce website providing easy, familiar navigation and allowing the simulated purchase of items from the store.

The site functionality will allow a common shopping experience for the visitor by providing a shopping cart to save chosen items, a secure checkout / payment facility and order confirmation using both on-screen messages and friendly, personalised emailed message.

***Please note: This site is purely for educational purposes only. The credit card payment facility is real but remains in test mode and so no payments will be taken. Please do not enter real credit card details when using this site.***


### **Contents** ###

- [UX Design](#ux-design)
  - [Project Goals](#project-goals)
  - [User Stories](#user-stories)
    - [Viewing and Navigation](#viewing-and-navigation)
    - [Registration and User Accounts](#registration-and-user-accounts)
    - [Sorting and Searching](#sorting-and-earching)
    - [Purchasing and Checkout](#purchasing-and-checkout)
    - [Admin and Store Management](#admin-and-store-management)
- [Design Choices](#Design-Choices)
  - [Colours](#Colours)
  - [Wireframes](#Wireframes)
- [Technologies](#technologies)
  - [Languages](#languages)
  - [Database](#database)
  - [Libraries](#libraries)
  - [Tools](#tools)
- [Features](#Features)
  - [Features Implemented](#Features-Implemented)
  - [Responsive Front-end Design](#Responsive-Front-end-Design)
  - [Back-end Design](#Back-end-Design)
  - [User Stories Implemented](#User-Stories-Implemented)
  - [Site Construction](#Site-Construction)
    - [Topology](#Topology)
  - [Database Schema](#Database-Schema)
    - [Fixtures JSON File creation](#Fixtures-JSON-File-creation)
  - [CRUD Functionality](#CRUD-Functionality)
  - [Messages](#Messages)
  - [Defensive Programming](#Defensive-Programming)
  - [Additional Site Features](#Additional-Site-Features)
  - [Future Features](#Future-Features)
- [Project Management](#Project-Management)
- [Version Control](#Version-Control)
- [Testing](#Testing)
- [Bugs](#Bugs)
- [Deployment](#deployment)
  - [Cloning We-Glove-Boxing Online from GitHub](#cloning-We-Glove-Boxing-online-from-github)
    - [Prerequisites](#prerequisites)
    - [Cloning the GitHub repository](#cloning-the-GitHub-repository)
    - [Creation of a Python Virtual Environment](#Creation-of-a-Python-Virtual-Environment)
    - [Install the App dependencies and external libraries](#Install-the-App-dependencies-and-external-libraries)
    - [Create the database in sqlite3](#Create-the-database-in-sqlite3)
    - [Create .env file](#Create-.env-file)
    - [Run the application locally](#Run-the-application-locally)
  - [Deploying We-Glove-Boxing Online app to Heroku](#Deploying-We-Glove-Boxing-Online-app-to-Heroku)
    - [Creating the Heroku app](#Creating-the-Heroku-app)
    - [Adding a PostgreSQL database to Heroku](#Adding-a-PostgreSQL-database-to-Heroku)
    - [Load the data into PostgreSQL](#Load-the-data-into-PostgreSQL)
    - [Push your repository to GitHub](#Push-you-repository-to-GitHub)
    - [Launch the app](#Launch-the-app)
- [Credits](#credits)
  - [Images](#images)
  - [Colour](#colour)
  - [Acknowledgements](#acknowledgements)

  ---

## **UX DESIGN** ##

### **Project Goals** ###

The **goal** of this project is to build a fully functioning e-commerce website, similar in design to [Box Fit UK](https://www.boxfituk.com/), allowing the user to browse a range of boxing related products. 