# AI-Gym-Assistant
A Simple but useful Gym Assistant using [MediaPipe](https://google.github.io/mediapipe/solutions/pose) and Python.

Are you like me, finding it difficult
- To count the number of bicep reps while listening to Heavy Metal or just texting your friend at the same time.


Then I believe this micro-app would be of a great use to you.

## Rep Counter
Counts the number of reps and **auto-generates a custom Result Page**.

Features given below are stored.
- date
- start time
- end time
- left/right reps
- total reps

Data is stored in a database(sqlite3) which later can be used to create analytics.


### Example

![reps](https://user-images.githubusercontent.com/90824601/154799596-6a7bb500-61a4-490a-825b-2451cf5f91e9.gif)
<img src="https://user-images.githubusercontent.com/90824601/154799799-8a24871f-cc0e-45dd-a8f2-67f2cc9f5c83.png" width="500" height="330" />
<img src= "https://user-images.githubusercontent.com/90824601/154799638-b9b0ee93-4ede-4045-aed0-a42dfa8a3da6.jpg" width="500" height="330"/>

### Instructions to use the app
1. Clone the repo
2. Install nessessary dependiences 
```
  pip install mediapipe
  ```
3. cd into the folder
4. Run the command
```
python3 rep_counter.py
```