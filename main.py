from src.predict import predict_email

email = input("Enter email content: ")

result = predict_email(email)

print(f"\nPrediction: {result}")
