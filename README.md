# Web App with ML Integration

This repository contains a Django-based web application that seamlessly integrates machine learning capabilities.

## Overview

The project consists of the following components:

- **Step 1: Simple Web App with Authentication**
  - User registration, login, and data submission.
  - Secure password handling and basic validation.
  - Admin and User roles.
 
- **Step 2: Dockerized Web App with ML Integration**
  - Integrated RoBERTa based sentiment model.
  - Users upload text for Sentiment analysis.
  - Dockerized with ML model.

- **Step 3: RESTful API for Data Management**
  - CRUD operations on user data.
  - API for user roles to interact with analysis.

## How to Run

1. Clone this repository.
2. Install Docker.
3. Navigate to the project's root directory.
4. Run `docker-compose up` to build and start the app.
5. Access the web app at `http://localhost:8000`.
