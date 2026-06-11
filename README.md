# ✍️ AI Handwriting Generator

## 📌 Project Overview

This project is a web-based application that converts typed text into a handwritten-style image. It demonstrates how a computer system can simulate a simple human activity (writing) using rule-based logic and image processing.

---

## 🎯 Objective

The objective of this project is to design a system that:

* Takes text input from the user
* Processes it using defined rules and constraints
* Generates a handwritten-style output image

---

## ⚙️ How It Works

1. The user enters text through a web interface
2. The system processes the text word by word
3. It applies a rule-based approach to check line width
4. If the line exceeds the limit, it moves text to the next line
5. The processed text is rendered as an image using a handwriting font
6. The final output is displayed on the webpage

---

## 🧠 AI Concepts Used

### 1. Agent Model (PEAS)

* **Performance**: Generate readable handwritten output
* **Environment**: User input text
* **Actuator**: Image generation
* **Sensor**: Text input

---

### 2. Problem Formulation

* **State**: Current line being processed
* **Action**: Add word or move to next line
* **Transition**: Line overflow → new line
* **Cost**: Avoid text overflow and maintain readability

---

### 3. Rule-Based System

The system follows rules such as:

* If line width exceeds limit → move to next line

---

### 4. Constraint Handling

* Text must fit within image width
* Line breaks are controlled using constraints

---

### 5. Knowledge Representation

* Rules and conditions are used to represent logic

---

### 6. Explainable AI

Each output is generated using clear and understandable steps, making the system transparent and explainable.

---

## 🛠️ Technologies Used

* Python
* Flask (Web Framework)
* Pillow (Image Processing)
* HTML & CSS

---

## 📂 Project Structure

```
handwriting-generator/
 ├── app.py
 ├── handwriting.ttf
 ├── templates/
 │    └── index.html
 └── static/
```

---

## ▶️ How to Run

1. Install dependencies:

```
pip install flask pillow
```

2. Run the application:

```
python app.py
```

3. Open browser and go to:

```
http://127.0.0.1:5000
```

---

## 🚀 Future Scope

* Use Machine Learning for realistic handwriting generation
* Add multiple handwriting styles
* Deploy as an online application

---


