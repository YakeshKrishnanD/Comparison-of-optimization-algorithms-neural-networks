# 📉 Comparison of Optimization Algorithms for Neural Network Training

A comprehensive deep learning case study and performance benchmarking project evaluating how different optimization algorithms affect convergence speed, stability, and accuracy when training neural networks on image datasets (MNIST).

---

## ⚡ Overview

Different optimizers handle gradient descent updates differently, directly impacting training efficiency and final model performance. This project implements, trains, and benchmarks various gradient-based optimization algorithms under controlled experimental conditions to analyze their empirical behavior.

---

## 🤖 Evaluated Optimization Algorithms

* **SGD (Stochastic Gradient Descent)** — Classic baseline optimizer with optional momentum.
* **Momentum** — Accelerates SGD in the relevant direction and dampens oscillations.
* **RMSprop** — Adapts learning rates based on a moving average of squared gradients.
* **Adam (Adaptive Moment Estimation)** — Combines the benefits of both Momentum and RMSprop for robust adaptive learning.

---

## 📋 Features & Analysis Metrics

* **📊 Loss Curves & Benchmarks** — Tracks training and validation loss over epochs across all optimizers.
* **⏱️ Convergence Speed** — Measures how quickly each algorithm reaches optimal convergence thresholds.
* **📈 Accuracy Evaluation** — Compares final classification performance on the MNIST benchmark dataset.
* **🖥️ Interactive Script & Notebook** — Includes clean Jupyter notebooks for step-by-step experimentation and execution scripts.

---

## 🗂️ Project Structure

```text
case-study-project/
├── .gitignore
├── app.py
├── download_mnist.py
├── loss_curves.csv
├── optimization_algorithm_for_neural_network_training.ipynb
├── optimizer_results.csv
├── data/
│   └── MNIST/
│       └── raw/               ← MNIST dataset files (.gz)
└── screenshots/
    ├── image1.png
    └── image2.png

```

---

## 🚀 Quick Start & Replication

1. **Clone the repository:**
```bash
git clone [https://github.com/YakeshKrishnanD/Comparison-of-optimization-algorithms-neural-networks.git](https://github.com/YakeshKrishnanD/Comparison-of-optimization-algorithms-neural-networks.git)
cd Comparison-of-optimization-algorithms-neural-networks

```


2. **Install required dependencies:**
```bash
pip install torch torchvision numpy pandas matplotlib jupyter

```


3. **Run the Jupyter Notebook:**
```bash
jupyter notebook optimization_algorithm_for_neural_network_training.ipynb

```



---

## 📊 Results Summary

* **Adam** demonstrates the fastest initial convergence and smooth adaptation across complex loss landscapes.
* **RMSprop** shows strong stability in handling non-stationary objectives.
* **SGD with Momentum** achieves competitive generalization performance with proper hyperparameter tuning.

---

## 👨‍💻 Author

**Yakesh Krishnan D**

M.Tech in Computer science and Engineering 
