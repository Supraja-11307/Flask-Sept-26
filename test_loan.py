import pytest
from loan import app
# def test_loan_application():
#     response=requests.post("http://127.0.0.1:5000/predict", json={})

@pytest.fixture
def client():
    return app.test_client()


def test_home(client):
    resp=client.get('/')
    assert resp.status_code==200
    assert resp.text == "<h1>Welcome to the Loan API V2!</h1>"


def test_predict_million(client):
    data = {
        "Gender": "Male",
        "Married": "No",
        "ApplicantIncome": 5000,
        "LoanAmount": 10000000,
        "Credit_History": 1
    }
    resp=client.post('/predict', json=data)
    assert resp.status_code==200
    assert resp.json == {"prediction": "Loan Not Approved"}


def test_predict_low_amount(client):
    data = {
        "Gender": "Male",
        "Married": "No",
        "ApplicantIncome": 5000,
        "LoanAmount": 100,
        "Credit_History": 1
    }
    resp=client.post('/predict', json=data)
    assert resp.status_code==200
    assert resp.json == {"prediction": "Loan Approved"}
