import os

# Basisordner, von dem aus das Skript ausgeführt wird
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

folders = [
    # Wissensarchiv
    "machine-learning/00-fundamentals/ml-vs-ai",
    "machine-learning/00-fundamentals/lifecycle",
    "machine-learning/00-fundamentals/bias-variance",
    "machine-learning/00-fundamentals/overfitting-regularization",
    "machine-learning/00-fundamentals/hyperparameter-tuning",
    "machine-learning/01-data-preprocessing/cleaning",
    "machine-learning/01-data-preprocessing/encoding",
    "machine-learning/01-data-preprocessing/scaling-normalization",
    "machine-learning/01-data-preprocessing/missing-values",
    "machine-learning/02-feature-engineering-selection/feature-engineering",
    "machine-learning/02-feature-engineering-selection/feature-selection",
    "machine-learning/02-feature-engineering-selection/dimensionality-reduction",
    "machine-learning/03-supervised-learning/regression",
    "machine-learning/03-supervised-learning/classification",
    "machine-learning/03-supervised-learning/ensemble-methods/bagging",
    "machine-learning/03-supervised-learning/ensemble-methods/boosting",
    "machine-learning/03-supervised-learning/ensemble-methods/stacking",
    "machine-learning/03-supervised-learning/model-evaluation",
    "machine-learning/03-supervised-learning/evaluation-metrics",
    "machine-learning/03-supervised-learning/cross-validation",
    "machine-learning/04-unsupervised-learning/clustering",
    "machine-learning/04-unsupervised-learning/anomaly-detection",
    "machine-learning/04-unsupervised-learning/association-rules",
    "machine-learning/05-semi-supervised-active-learning/self-training",
    "machine-learning/05-semi-supervised-active-learning/co-training",
    "machine-learning/05-semi-supervised-active-learning/pseudo-labeling",
    "machine-learning/05-semi-supervised-active-learning/consistency-regularization",
    "machine-learning/05-semi-supervised-active-learning/active-learning",
    "machine-learning/06-reinforcement-learning/q-learning",
    "machine-learning/06-reinforcement-learning/policy-gradient",
    "machine-learning/06-reinforcement-learning/applications",
    "machine-learning/07-deep-learning/neural-networks",
    "machine-learning/07-deep-learning/cnn",
    "machine-learning/07-deep-learning/rnn-lstm",
    "machine-learning/07-deep-learning/transformers",
    "machine-learning/07-deep-learning/transfer-learning",
    "machine-learning/07-deep-learning/meta-learning",
    "machine-learning/08-nlp/tokenization",
    "machine-learning/08-nlp/embeddings",
    "machine-learning/08-nlp/sequence-labelling",
    "machine-learning/08-nlp/applications",
    "machine-learning/09-graph-ml/gnn",
    "machine-learning/09-graph-ml/graph-algorithms",
    "machine-learning/10-automl/automl-frameworks",
    "machine-learning/10-automl/best-practices",
    "machine-learning/11-mlops/pipelines",
    "machine-learning/11-mlops/deployment",
    "machine-learning/11-mlops/monitoring",
    "machine-learning/11-mlops/experiment-tracking",
    "machine-learning/11-mlops/reproducibility",
    "machine-learning/12-fairness-privacy-ethics/explainability",
    "machine-learning/12-fairness-privacy-ethics/interpretability-methods",
    "machine-learning/12-fairness-privacy-ethics/bias-mitigation",
    "machine-learning/12-fairness-privacy-ethics/privacy",
    "machine-learning/13-openai-and-llms/gpt-series",
    "machine-learning/13-openai-and-llms/api-usage",
    "machine-learning/13-openai-and-llms/prompt-debugging",
    "machine-learning/13-openai-and-llms/applications",
    "machine-learning/14-time-series/forecasting",
    "machine-learning/14-time-series/arima",
    "machine-learning/14-time-series/prophet",
    # Projekte
    "projects/project-01-customer-churn",
    "projects/project-02-fraud-detection"
]

for folder in folders:
    path = os.path.join(BASE_DIR, folder)
    os.makedirs(path, exist_ok=True)
    # Optionale README.md in jedem Hauptordner:
    if folder.count('/') == 1:
        readme_path = os.path.join(BASE_DIR, folder, 'README.md')
        if not os.path.exists(readme_path):
            with open(readme_path, "w") as f:
                f.write(f"# {folder.split('/')[-1].replace('-', ' ').title()}\n")

print("Ordnerstruktur wurde erfolgreich erstellt.")
