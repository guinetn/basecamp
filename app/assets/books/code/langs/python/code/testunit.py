# unittest in python

# main.py
# Define object we classify
class PersonInformation(BaseModel):
    sex: str
    pclass: int


class SurvivePredictor:
    """
    Holds the actual process of doing the prediction
    """

    def __init__(self):
        self.clf: DecisionTreeClassifier = load("./model_weights/clf.bin")

    def predict(self, item: PersonInformation):
        # make sure that here the order is the same as in the model training
        print("item:", item)
        x = np.array([1 if item.sex == "female" else 0, item.pclass])
        x = x.reshape(1, -1)
        # be careful to only transform and not fit
        print("numeric representation:", x)
        y = self.clf.predict_proba(x)
        print("survival probability:", y)
        # y looks now like: [[0.78 0.21]] so the second number is probability of survived
        return y[0][1]

# test.py
import unittest

from main import SurvivePredictor, PersonInformation

class TestClassifier(unittest.TestCase):
    def test_classifier(self):
        # One testcase to show, rather trivial
        # We could test legal inputs, like non negatives etc
        # But we did not implement
        self.predictor = SurvivePredictor()
        assert 0.5 > self.predictor.predict(
            PersonInformation(sex='male', pclass=2)), "Issue with prediction negative"
        assert 0.5 < self.predictor.predict(
            PersonInformation(sex='female', pclass=2)), "Issue with prediction positive"

if __name__ == '__main__':
    unittest.main()

# see https://www.youtube.com/watch?v=La1HAYI1j30&t=1s