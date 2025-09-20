import pickle
from sklearn.linear_model import LinearRegression
from model.preprocessing import load_and_clean_data

def train_and_save_model():
    df = load_and_clean_data()
    X = df[['x']]
    y = df['y']

    model = LinearRegression()
    model.fit(X, y)

    with open("model/trained_model.pkl", "wb") as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    train_and_save_model()
