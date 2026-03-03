import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        response = emotion_detector("I am happy")
        self.assertEqual(response["dominant_emotion"], "joy")

    def test_anger(self):
        response = emotion_detector("I am angry")
        self.assertEqual(response["dominant_emotion"], "anger")

    def test_sadness(self):
        response = emotion_detector("I am sad")
        self.assertEqual(response["dominant_emotion"], "sadness")

if __name__ == "__main__":
    unittest.main()
