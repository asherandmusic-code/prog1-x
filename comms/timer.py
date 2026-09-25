#var-init
from pathlib import Path
import winsound
import time

SOUND = Path(__file__).parent / "t.wav"
#var-init

#main-function
def timer():
    x = int(input("Enter seconds:"))
    time.sleep(x)

    winsound.PlaySound(
        str(SOUND),
        winsound.SND_FILENAME | winsound.SND_ASYNC
    )

    input("dismiss:")
    winsound.PlaySound(None, 0)
#main-function

#call-dictionary
plug = {
    "desc": '''timer          - simple tune-playing timer''',

    "comms": {
        "timer": timer
    }
}
#call-dictionary
