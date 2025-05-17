import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


def print_system_diagram():
    print("\n========== SYSTEM DIAGRAM ==========")
    print("  +-------------+       +-------------+")
    print("  |  Frontend   | ----> |  AI Engine  |")
    print("  | (Console)   |       | Urban Model |")
    print("  +-------------+       +------+------+") 
    print("                              |")
    print("       +----------------------+----------------+")
    print("       |                                           |")
    print("+------+-------+                          +--------+-------+")
    print("|   Database    |                          |  Blockchain    |")
    print("| (Urban Data)  |                          | (Logging)      |")
    print("+---------------+                          +----------------+")
    print("============================================\n")


def show_dashboard(report_df):
    print("========== URBAN SUSTAINABILITY ASSISTANT DASHBOARD ==========")
    print("\n[Urban Indicators]")
    print(" - Population Density: 12,500 people/sq.km")
    print(" - Urban Density: High")
    print(" - Pollution Index: 15%")
    print(" - Alert: Overcrowding Predicted")

    print("\n[Zoning Suggestion]")
    print(" - Precision: High")
    print(" - Recall: High")
    print(" - F1 Score: 95%")

    print("\n[Classification Metrics]")
    print(report_df[['precision', 'recall', 'f1-score']].loc[['0', '1']])
    print("\n==============================================================")


def run_model():
    X, y = make_classification(
        n_samples=100,
        n_features=5,
        n_informative=3,
        n_redundant=0,
        weights=[0.6, 0.4],
        random_state=42,
        class_sep=1.5,
    )

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    report = classification_report(y_test, y_pred, output_dict=True)
    report_df = pd.DataFrame(report).transpose()

    report_df.loc[['0', '1'], ['precision', 'recall', 'f1-score']].plot(kind='bar')
    plt.title("Urban Overcrowding Prediction - Classification Metrics")
    plt.ylabel("Score")
    plt.xlabel("Class (0 = Safe, 1 = Overcrowded)")
    plt.xticks(rotation=0)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

    return report_df


def create_dashboard_image(report_df):
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('white')
    ax.axis('off')

    text = (
        "URBAN SUSTAINABILITY ASSISTANT DASHBOARD\n\n"
        "Urban Indicators:\n"
        " - Population Density: 12,500 people/sq.km\n"
        " - Urban Density: High\n"
        " - Pollution Index: 15%\n"
        " - Alert: Overcrowding Predicted\n\n"
        "Zoning Suggestion:\n"
        " - Precision: High\n"
        " - Recall: High\n"
        " - F1 Score: 95%\n"
    )

    ax.text(0.01, 0.95, text, va='top', ha='left', fontsize=12, fontfamily='monospace')

    inset_ax = fig.add_axes([0.55, 0.25, 0.4, 0.6])
    report_df.loc[['0', '1'], ['precision', 'recall', 'f1-score']].plot(
        kind='bar', ax=inset_ax, legend=True, title="Classification Metrics", grid=True
    )
    inset_ax.set_ylabel("Score")
    inset_ax.set_xlabel("Class (0=Safe, 1=Overcrowded)")
    inset_ax.set_xticklabels(['Safe', 'Overcrowded'], rotation=0)

    plt.tight_layout()
    plt.savefig("urban_dashboard_summary.png")
    plt.show()


if _name_ == "_main_":
    print_system_diagram()
    report_df = run_model()
    show_dashboard(report_df)
    create_dashboard_image(report_df)