import scheduler
import prediction
import time

print("TempSched+ Started")

while True:

    scheduler.schedule()

    future = prediction.predict()

    print("Predicted temperature:", future)

    time.sleep(10)
