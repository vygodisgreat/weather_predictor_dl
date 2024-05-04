this is a **per-hour** weather predictor using LSTM (Long Short Term Memory) Deep Learning Technique.
It is a fully deployed web app that first is trained on the NASA POWER dataset of past 15 years of climate conditions of specific locations like maharashtra/haryana/etc.
using LSTM, I have madeper hour predictions for **temperature, pressure and humidity** for this entire year 2024 in advance using previous year data.
The result is stored in database and a web app can be used to access any day of the Year to view the predictions in the browser itself!

<img width="1280" alt="p1" src="https://github.com/vygodisgreat/weather_predictor_dl/assets/125375732/500ec80b-61a4-4e06-a04e-74a20e6024da">
<img width="1280" alt="p2" src="https://github.com/vygodisgreat/weather_predictor_dl/assets/125375732/491b98ea-773e-42b5-aa3d-b8080f4daa7f">
<img width="1280" alt="p3" src="https://github.com/vygodisgreat/weather_predictor_dl/assets/125375732/db15b4d9-dcf3-4903-a640-057bab8aa409">

simply run the flask app by `flask run` and then access the interface
