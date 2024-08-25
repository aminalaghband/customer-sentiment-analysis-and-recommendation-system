import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns

class SentimentAnalysis:
    def __init__(self, data):
        self.data = pd.DataFrame(data)
        self.model = make_pipeline(CountVectorizer(), MultinomialNB())

    def train_model(self):
        X_train, X_test, y_train, y_test = train_test_split(self.data['feedback'], self.data['sentiment'], test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        print(classification_report(y_test, y_pred))

    def predict_sentiment(self, feedback):
        return self.model.predict([feedback])[0]

    def generate_recommendations(self, feedback):
        sentiment = self.predict_sentiment(feedback)
        if sentiment == 'positive':
            return "Keep up the good work! Your customers are happy."
        elif sentiment == 'neutral':
            return "Consider engaging more with your customers to improve their experience."
        else:
            return "Identify and address the issues causing dissatisfaction among your customers."

    def visualize_sentiment(self):
        sns.countplot(x='sentiment', data=self.data)
        plt.title('Sentiment Distribution')
        plt.show()

# Example usage
data = {
    'feedback': [
        'Great service and friendly staff!',
        'The product quality is average.',
        'I am not satisfied with the customer support.',
        'Excellent experience, will come back again!',
        'The delivery was late and the packaging was damaged.'
    ],
    'sentiment': ['positive', 'neutral', 'negative', 'positive', 'negative']
}

sentiment_analysis = SentimentAnalysis(data)
sentiment_analysis.train_model()
print("Sentiment Prediction:", sentiment_analysis.predict_sentiment('The service was fantastic!'))
print("Recommendation:", sentiment_analysis.generate_recommendations('The service was fantastic!'))
sentiment_analysis.visualize_sentiment()
